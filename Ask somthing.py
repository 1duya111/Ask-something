import tkinter as tk
from tkinter import messagebox
import random
import datetime

# 准备题库
questions = [
    "你这周做过最正确的决定是什么？",
    "你最近在玩什么游戏？",
    "最近有么有发现好吃的外卖？",
    "截至目前你是否实现了自己一个小小的目标？",
    "爱吃甜的还是辣的？"
    "你觉得软工还有出路吗？"
    "我要不要买这次的周边？"
    "猜猜这个程序是deepseek写的还是豆包写的？"
    "我能找到专业相关工作吗？"
    "十年之后我还喜欢画画吗？"
    "三年之后我会不再纠结烂人烂事，过上自由自在的生活吗?"
]

# 抽题按钮点击后执行的函数
def pick_question():
    # 随机抽一题，并显示在界面的文字标签上
    question = random.choice(questions)
    question_label.config(text=question, fg="blue")

# 保存按钮点击后执行的函数
def save_answer():
    question = question_label.cget("text") # 获取当前界面上显示的问题
    answer = answer_entry.get()            # 获取输入框里的回答
    
    if question == "点击下方按钮抽取问题" or answer.strip() == "":
        messagebox.showwarning("提示", "请先抽取问题，并输入回答哦！")
        return

    today = datetime.date.today()
    # 写入文件
    with open("my_answers.txt", "a", encoding="utf-8") as f:
        f.write(f"[{today}] 问题：{question}\n")
        f.write(f"回答：{answer}\n")
        f.write("-------------------\n")
    
    messagebox.showinfo("成功", "回答已保存！")
    answer_entry.delete(0, tk.END) # 清空输入框
    question_label.config(text="点击下方按钮抽取问题", fg="black") # 恢复提示

# 查看历史按钮点击后执行的函数
def view_history():
    try:
        with open("my_answers.txt", "r", encoding="utf-8") as f:
            history_text = f.read()
        # 弹出一个大窗口显示历史记录
        messagebox.showinfo("历史记录", history_text)
    except FileNotFoundError:
        messagebox.showinfo("历史记录", "你还没有回答过任何问题哦！")

# ================= 界面搭建 =================
window = tk.Tk()
window.title("每日一问小工具")
window.geometry("400x300")

# 1. 显示问题的标签
question_label = tk.Label(window, text="点击下方按钮抽取问题", font=("微软雅黑", 12), wraplength=350)
question_label.pack(pady=20)

# 2. 输入回答的框
answer_entry = tk.Entry(window, font=("微软雅黑", 12), width=30)
answer_entry.pack(pady=10)

# 3. 按钮们
btn_pick = tk.Button(window, text="抽 取 问 题", command=pick_question, bg="lightblue")
btn_pick.pack(pady=5)

btn_save = tk.Button(window, text="保 存 回 答", command=save_answer, bg="lightgreen")
btn_save.pack(pady=5)

btn_history = tk.Button(window, text="查 看 历 史", command=view_history)
btn_history.pack(pady=5)

# 运行主循环
window.mainloop()