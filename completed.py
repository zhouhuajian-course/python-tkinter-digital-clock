"""
Python Tkinter 数字时钟小项目

@author  : 周华健
@github  : https://github.com/zhouhuajian-course
@version : v1.0
"""

import os
import time
from tkinter import *

# 主窗口
root = Tk()
# 隐藏窗口
root.withdraw()

# 窗口标题
root.title("数字时钟")
# 窗口置顶
root.attributes("-topmost", 1)
# 窗口图标
ico_path = "image/app.ico"
if os.path.exists(ico_path):
    root.iconbitmap(ico_path)
# 固定窗口大小
root.resizable(width=False, height=False)

# 设置窗口大小并屏幕居中
w = 500
h = 250
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = int(screen_w / 2 - w / 2)
y = int(screen_h / 2 - (h + 30) / 2)
# 格式widthxheight±x±y
root.geometry(f"{w}x{h}+{x}+{y}")
# 显示窗口
root.deiconify()

# 主窗口的背景图片
bg_path = "image/app_bg.png"
if os.path.exists(bg_path):
    bg_image = PhotoImage(file=bg_path)
    Label(root, image=bg_image).place(x=0, y=0)
    
# 背景图片的背景颜色
bg_color = "#f7f1e5"
# 当前时间文本标签
Label(root, text="当前时间", font="宋体 20", bg=bg_color, pady=22).pack(side=TOP)

# 数字时间文本标签
time_label = Label(root, text="", font="宋体 45", bg="white", padx=12, pady=12)
time_label.pack(side=TOP)

# 24h/12h单选框
frame = Frame(root, pady=30, bg=bg_color)
frame.pack(side=BOTTOM)
var = StringVar()
Radiobutton(frame, text="24h", value="24h", font="宋体 12", variable=var, bg=bg_color, padx=5,
            activebackground=bg_color).pack(side=LEFT)
Radiobutton(frame, text="12h", value="12h", font="宋体 12", variable=var, bg=bg_color, padx=5,
            activebackground=bg_color).pack(side=RIGHT)
# 默认选中24h单选框
var.set("24h")


def update_time():
    """更新时间"""
    if var.get() == "24h":
        current_time = time.strftime("%H:%M:%S")
    else:
        current_time = time.strftime("%p %I:%M:%S")
    time_label.config(text=current_time)
    time_label.after(200, update_time)


update_time()

# 进入消息循环
root.mainloop()
