#待办事项管理器
# 1.添加待办事项
# 2.删除待办事项
# 3.修改待办事项
# 4.查询待办事项
# 5.显示所有待办事项
# 6.退出
# 7.保存数据
# 8.读取数据
# 9.清空数据
# 10.导出数据
# 11.导入数据
# 12.帮助
# 13.关于
# 14.退出

import os
import time
import datetime
import pickle
import json

#待办事项类
class TodoItem:
    def __init__(self, id, content, status, create_time, update_time):
        self.id = id
        self.content = content
        self.status = status
        self.create_time = create_time
        self.update_time = update_time

    def __str__(self):
        return f"{self.id} {self.content} {self.status} {self.create_time} {self.update_time}"
    
    def __repr__(self):
        return self.__str__()
    
#待办事项管理器类
class TodoManager:
    def __init__(self):
        self.items = []
        self.load_data()
    
    #添加待办事项
    def add(self, content):
        id = len(self.items) + 1
        status = "未完成"
        create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        update_time = create_time
        item = TodoItem(id, content, status, create_time, update_time)
        self.items.append(item)
        print(f"添加成功: {item}")
    
    #删除待办事项
    def delete(self, id):
        for item in self.items:
            if item.id == id:
                self.items.remove(item)
                print(f"删除成功: {item}")
                return
        print(f"删除失败: 未找到id为{id}的待办事项")
    
    #修改待办事项
    def update(self, id, content=None, status=None):
        for item in self.items:
            if item.id == id:
                if content is not None:
                    item.content = content
                if status is not None:
                    item.status = status
                item.update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"修改成功: {item}")
                return
        print(f"修改失败: 未找到id为{id}的待办事项")
    
    #查询待办事项
    def query(self, id):
        for item in self.items:
            if item.id == id:
                print(f"查询结果: {item}")
                return
        print(f"查询失败: 未找到id为{id}的待办事项")
    
    #显示所有待办事项
    def show_all(self):
        print("所有待办事项:")
        for item in self.items:
            print(item)
    
    #保存数据
    def save_data(self):
        with open("data.pkl", "wb") as file:
            pickle.dump(self.items, file)
        print("保存成功")
    
    #读取数据
    def load_data(self):
        if os.path.exists("data.pkl"):
            with open("data.pkl", "rb") as file:
                self.items = pickle.load(file)
            print("读取成功")
    
    #清空数据
    def clear_data(self):
        self.items = []
        print("清空成功")
    
    #导出数据
    def export_data(self):
        with open("data.json", "w") as file:
            json.dump([item.__dict__ for item in self.items], file)
        print("导出成功")
    
    #导入数据
    def import_data(self):
        with open("data.json", "r") as file:
            data = json.load(file)
            self.items = [TodoItem(**item) for item in data]
        print("导入成功")
    
    #帮助
    def help(self):
        print("待办事项管理器")
        print("1.添加待办事项")
        print("2.删除待办事项")
        print("3.修改待办事项")
        print("4.查询待办事项")
        print("5.显示所有待办事项")
        print("6.退出")
        print("7.保存数据")
        print("8.读取数据")
        print("9.清空数据")
        print("10.导出数据")
        print("11.导入数据")
        print("12.帮助")
        print("13.关于")
        print("14.退出")
    
    #关于
    def about(self):
        print("待办事项管理器 v1.0")
        print("作者: xxx")
        print("日期: 2021-01-01")
    
    #运行
    def run(self):
        while True:
            print()
            print("待办事项管理器")
            print("1.添加待办事项")
            print("2.删除待办事项")
            print("3.修改待办事项")
            print("4.查询待办事项")
            print("5.显示所有待办事项")
            print("6.退出")
            print("7.保存数据")
            print("8.读取数据")
            print("9.清空数据")
            print("10.导出数据")
            print("11.导入数据")
            print("12.帮助")
            print("13.关于")
            print("14.退出")
            choice = input("请选择操作:")
            if choice == "1":
                content = input("请输入待办事项内容:")
                self.add(content)
            elif choice == "2":
                id = int(input("请输入待办事项id:"))
                self.delete(id)
            elif choice == "3":
                id = int(input("请输入待办事项id:"))
                content = input("请输入新的待办事项内容:")
                self.update(id, content)
            elif choice == "4":
                id = int(input("请输入待办事项id:"))
                self.query(id)
            elif choice == "5":
                self.show_all()
            elif choice == "6":
                break
            elif choice == "7":
                self.save_data()
            elif choice == "8":
                self.load_data()
            elif choice == "9":
                self.clear_data()
            elif choice == "10":
                self.export_data()
            elif choice == "11":
                self.import_data()
            elif choice == "12":
                self.help()
            elif choice == "13":
                self.about()
            elif choice == "14":
                break
            else:
                print("无效操作")
    
if __name__ == "__main__":
    manager = TodoManager()
    manager.run()
