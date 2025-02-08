
import digitalguess.digitalguess as digitalguess

print("模块的名称是:", digitalguess.__name__)  # 会打印 "digitalguess"
print("当前文件的名称是:", __name__)          # 会打印 "__main__"

# 只有手动调用才会执行游戏
digitalguess.guess_number()