import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class WechatBillAnalyzer:
    def __init__(self, file_path):
        self.df = self.load_data(file_path)
        self.preprocess_data()
        
    def load_data(self, file_path):
        """读取Excel文件并提取交易明细"""
        # 读取第二个工作表（交易明细）
        df = pd.read_excel(file_path, sheet_name=1, header=9)  # 跳过前9行元数据
        # 清理空行和无效列
        df = df.dropna(how='all').reset_index(drop=True)
        return df

    def preprocess_data(self):
        """数据预处理"""
        # 转换金额为数值类型
        self.df['金额(元)'] = pd.to_numeric(self.df['金额(元)'], errors='coerce')
        # 转换时间格式
        self.df['交易时间'] = pd.to_datetime(self.df['交易时间'])
        # 添加月份列
        self.df['月份'] = self.df['交易时间'].dt.to_period('M')

    def basic_analysis(self):
        """基础统计分析"""
        analysis = {
            '总交易笔数': len(self.df),
            '总收入': self.df[self.df['收/支'] == '收入']['金额(元)'].sum(),
            '总支出': self.df[self.df['收/支'] == '支出']['金额(元)'].sum(),
            '月度趋势': self.df.groupby('月份')['金额(元)'].sum().to_dict(),
            '支付方式分布': self.df.groupby('支付方式')['金额(元)'].sum().to_dict(),
            '高频商户': self.df['交易对方'].value_counts().head(5).to_dict()
        }
        return analysis

    def generate_charts(self, output_dir='output'):
        """生成可视化图表"""
        # 创建输出目录
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        # 月度趋势图
        monthly = self.df.groupby('月份')['金额(元)'].sum()
        monthly.plot(kind='bar', title='月度消费趋势')
        plt.savefig(f'{output_dir}/monthly_trend.png')
        plt.close()

        # 支付方式分布
        payment = self.df.groupby('支付方式')['金额(元)'].sum()
        payment.plot(kind='pie', autopct='%1.1f%%', title='支付方式分布')
        plt.savefig(f'{output_dir}/payment_distribution.png')
        plt.close()

    def generate_report(self):
        """生成文字分析报告"""
        analysis = self.basic_analysis()
        report = f"""
        【账单分析报告】
        统计周期：{self.df['交易时间'].min().date()} 至 {self.df['交易时间'].max().date()}
        总交易笔数：{analysis['总交易笔数']}笔
        总收入：{analysis['总收入']:.2f}元
        总支出：{analysis['总支出']:.2f}元
        
        【消费趋势】
        峰值月份：{max(analysis['月度趋势'], key=analysis['月度趋势'].get)}月
        {self.format_monthly_trend(analysis['月度趋势'])}
        
        【支付方式】
        {self.format_payment_distribution(analysis['支付方式分布'])}
        """
        return report

    @staticmethod
    def format_monthly_trend(data):
        return "\n".join([f"{k}: {v:.2f}元" for k, v in data.items()])

    @staticmethod
    def format_payment_distribution(data):
        total = sum(data.values())
        return "\n".join([f"{k}: {v/total:.1%}" for k, v in data.items()])

# 使用示例
if __name__ == "__main__":
    file_path = "E:/vs_project/pystudy/mybill/624.xlsx"
    analyzer = WechatBillAnalyzer(file_path)
    ##analyzer = WechatBillAnalyzer("624.xlsx")
    
    # 获取分析结果
    print(analyzer.generate_report())
    
    # 生成图表
    analyzer.generate_charts()
    
    # 获取原始数据
    print(analyzer.df.head())