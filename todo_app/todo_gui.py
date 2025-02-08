import tkinter as tk
from tkinter import ttk, messagebox
from datemanage import TodoManager, TodoItem
import datetime

class TodoGui:
    def __init__(self):
        self.manager = TodoManager()
        self.window = tk.Tk()
        self.window.title("待办事项管理器")
        self.window.geometry("800x600")
        
        # 创建列表显示区域
        self.tree = ttk.Treeview(self.window, columns=("ID", "内容", "状态", "创建时间", "更新时间"))
        self.tree.heading("ID", text="ID", anchor="center")
        self.tree.heading("内容", text="内容", anchor="center")
        self.tree.heading("状态", text="状态", anchor="center")
        self.tree.heading("创建时间", text="创建时间", anchor="center")
        self.tree.heading("更新时间", text="更新时间", anchor="center")
        
        # 设置列的对齐方式
        self.tree.column("ID", anchor="center")
        self.tree.column("内容", anchor="center")
        self.tree.column("状态", anchor="center")
        self.tree.column("创建时间", anchor="center")
        self.tree.column("更新时间", anchor="center")
        
        # 绑定双击事件用于切换状态
        self.tree.bind('<Double-1>', self.toggle_status)
        
        self.tree.pack(pady=10)

        # 创建按钮框架
        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)

        # 添加按钮
        tk.Button(button_frame, text="添加", command=self.add_item).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="删除", command=self.delete_item).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="修改", command=self.update_item).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="保存", command=self.save_data).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="刷新", command=self.refresh_list).pack(side=tk.LEFT, padx=5)

        # 初始化显示
        self.refresh_list()

    def add_item(self):
        # 创建新窗口输入待办事项
        add_window = tk.Toplevel(self.window)
        add_window.title("添加待办事项")
        add_window.geometry("300x150")
        
        # 设置窗口居中显示
        add_window.withdraw()  # 暂时隐藏窗口
        # 获取主窗口和新窗口的尺寸
        window_width = 300
        window_height = 150
        screen_width = add_window.winfo_screenwidth()
        screen_height = add_window.winfo_screenheight()
        # 计算居中位置
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        # 设置窗口位置
        add_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        add_window.deiconify()  # 显示窗口
        
        tk.Label(add_window, text="内容:").pack(pady=5)
        content = tk.Entry(add_window)
        content.pack(pady=5)
        
        def submit():
            if content.get():
                self.manager.add(content.get())
                self.refresh_list()
                add_window.destroy()
            
        tk.Button(add_window, text="确定", command=submit).pack(pady=10)

    def delete_item(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("警告", "请选择要删除的项目")
            return
        
        if messagebox.askyesno("确认", "确定要删除选中的项目吗？"):
            item_id = int(self.tree.item(selected[0])['values'][0])
            self.manager.delete(item_id)
            self.refresh_list()

    def update_item(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("警告", "请选择要修改的项目")
            return
            
        item_id = int(self.tree.item(selected[0])['values'][0])
        
        update_window = tk.Toplevel(self.window)
        update_window.title("修改待办事项")
        update_window.geometry("300x150")
        
        # 设置窗口居中显示
        update_window.withdraw()
        window_width = 300
        window_height = 150
        screen_width = update_window.winfo_screenwidth()
        screen_height = update_window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        update_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        update_window.deiconify()
        
        tk.Label(update_window, text="新内容:").pack(pady=5)
        content = tk.Entry(update_window)
        content.pack(pady=5)
        
        def submit():
            if content.get():
                self.manager.update(item_id, content.get())
                self.refresh_list()
                update_window.destroy()
            
        tk.Button(update_window, text="确定", command=submit).pack(pady=10)

    def save_data(self):
        self.manager.save_data()
        messagebox.showinfo("提示", "保存成功")

    def refresh_list(self):
        # 清空列表
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # 重新加载数据
        for item in self.manager.items:
            self.tree.insert("", tk.END, values=(
                item.id,
                item.content,
                item.status,
                item.create_time,
                item.update_time
            ))

    def toggle_status(self, event):
        selected = self.tree.selection()
        if not selected:
            return
            
        item_id = int(self.tree.item(selected[0])['values'][0])
        
        # 更新状态
        for item in self.manager.items:
            if item.id == item_id:
                item.status = "完成" if item.status == "未完成" else "未完成"
                item.update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                break
        
        self.refresh_list()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = TodoGui()
    app.run()
