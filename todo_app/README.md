# ToDo应用程序

## 学习目标
- 掌握Python基础语法
- 学习命令行交互程序开发
- 理解文件操作和数据持久化
- 实践面向对象编程概念

## 涉及知识点
- Python类和对象
- 文件读写操作
- 命令行参数处理
- 列表和字典操作
- JSON数据格式处理

## 项目描述
一个简单的命令行ToDo任务管理器，支持添加、删除、查看和更新待办事项。数据通过JSON文件持久化存储。

## 项目结构
```
todo_app/
├── src/
│   ├── todo.py           # 主程序文件
│   └── todo_manager.py   # ToDo管理类
├── data/
│   └── tasks.json        # 任务数据存储文件
└── README.md             # 当前文档
```

## 运行方式
```bash
# 查看所有任务
python src/todo.py list

# 添加新任务
python src/todo.py add "完成Python学习"

# 完成任务
python src/todo.py done 1

# 删除任务
python src/todo.py remove 1
```

## 学习笔记
### 重要概念
- 类的设计：使用TodoManager类管理任务操作
- 数据持久化：使用JSON文件存储任务数据
- 命令行参数：使用sys.argv处理命令行输入

### 遇到的问题
- JSON文件操作时的异常处理
- 命令行参数的规范化处理
- 任务ID的唯一性保证

### 心得体会
- 通过实践项目加深了对Python面向对象编程的理解
- 学会了如何设计简单但实用的命令行工具
- 理解了数据持久化的重要性和实现方法

## 参考资料
- [Python JSON处理](https://docs.python.org/3/library/json.html)
- [命令行参数处理](https://docs.python.org/3/library/argparse.html)
