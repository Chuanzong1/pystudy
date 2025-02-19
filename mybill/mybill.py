import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BillAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("微信账单分析工具")
        self.root.geometry("800x600")
        
        # 初始化数据
        self.df = None
        
        # 创建界面组件
        self.create_widgets()
    
    def create_widgets(self):
        """创建界面布局"""
        # 顶部操作栏
        control_frame = ttk.Frame(self.root)
        control_frame.pack(pady=10, fill=tk.X)
        
        self.btn_open = ttk.Button(
            control_frame, 
            text="选择账单文件", 
            command=self.load_file
        )
        self.btn_open.pack(side=tk.LEFT, padx=5)
        
        self.btn_analyze = ttk.Button(
            control_frame,
            text="开始分析",
            command=self.analyze_data,
            state=tk.DISABLED
        )
        self.btn_analyze.pack(side=tk.LEFT, padx=5)
        
        # 结果显示区域
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill=tk.BOTH)
        
        # 数据预览标签页
        self.preview_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.preview_frame, text="数据预览")
        
        # 分析结果标签页
        self.analysis_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.analysis_frame, text="分析结果")
        
        # 图表容器
        self.figure_frame = ttk.Frame(self.analysis_frame)
        self.figure_frame.pack(expand=True, fill=tk.BOTH)
    
    def load_file(self):
        """选择文件"""
        file_path = filedialog.askopenfilename(
            title="选择微信账单文件",
            filetypes=[("Excel文件", "*.xlsx")]
        )
        
        if file_path:
            try:
                self.df = pd.read_excel(file_path, sheet_name=1, header=9)
                self.df = self.df.dropna(how='all').reset_index(drop=True)
                
                # 启用分析按钮
                self.btn_analyze.config(state=tk.NORMAL)
                
                # 显示数据预览
                self.show_preview()
                
            except Exception as e:
                messagebox.showerror("错误", f"文件读取失败:\n{str(e)}")
    
    def show_preview(self):
        """显示数据预览"""
        # 清空原有内容
        for widget in self.preview_frame.winfo_children():
            widget.destroy()
        
        # 创建表格
        columns = list(self.df.columns)
        tree = ttk.Treeview(
            self.preview_frame, 
            columns=columns, 
            show='headings',
            height=15
        )
        
        # 设置列标题
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        
        # 添加滚动条
        vsb = ttk.Scrollbar(
            self.preview_frame, 
            orient="vertical", 
            command=tree.yview
        )
        tree.configure(yscrollcommand=vsb.set)
        
        # 添加数据
        for _, row in self.df.head(50).iterrows():
            tree.insert("", tk.END, values=list(row))
        
        # 布局
        tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        self.preview_frame.grid_columnconfigure(0, weight=1)
        self.preview_frame.grid_rowconfigure(0, weight=1)
    
    def analyze_data(self):
        """执行分析"""
        try:
            # 清空图表区域
            for widget in self.figure_frame.winfo_children():
                widget.destroy()
            
            # 生成月度趋势图
            fig1 = plt.Figure(figsize=(6, 4))
            ax1 = fig1.add_subplot(111)
            monthly = self.df.groupby(
                pd.to_datetime(self.df['交易时间']).dt.to_period('M'))
            monthly.sum()['金额(元)'].plot(kind='bar', ax=ax1)
            ax1.set_title("月度消费趋势")
            
            canvas1 = FigureCanvasTkAgg(fig1, self.figure_frame)
            canvas1.draw()
            canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            
            # 生成支付方式分布图
            fig2 = plt.Figure(figsize=(6, 4))
            ax2 = fig2.add_subplot(111)
            payment = self.df.groupby('支付方式')['金额(元)'].sum()
            payment.plot(kind='pie', autopct='%1.1f%%', ax=ax2)
            ax2.set_title("支付方式分布")
            
            canvas2 = FigureCanvasTkAgg(fig2, self.figure_frame)
            canvas2.draw()
            canvas2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            
        except Exception as e:
            messagebox.showerror("分析错误", f"数据分析失败:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BillAnalyzerApp(root)
    root.mainloop()