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
# 隐藏
root.withdraw()

# 标题
root.title("数字时钟")
# 图标
ico_path = "image/app.ico"
if os.path.exists(ico_path):
    root.iconbitmap(ico_path)
# 固定窗口大小
root.resizable(width=False, height=False)

# 设置窗口大小 屏幕居中
w = 500
h = 250
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = int(screen_w / 2 - w / 2)
y = int(screen_h / 2 - (h + 30) / 2)
# 格式widthxheight±x±y
root.geometry(f"{w}x{h}+{x}+{y}")

# 显示
root.deiconify()

# 背景图片
bg_path = "image/app_bg.png"
if os.path.exists(bg_path):
    bg_image = PhotoImage(file=bg_path)
    Label(root, image=bg_image).place(x=0, y=0)

# 背景颜色
bg_color = "#f7f1e5"
# 当前时间
Label(root, text="当前时间", pady=22, font="宋体 20", bg=bg_color).pack(side=TOP)

# 数字时间
time_label = Label(root, text="00:00:00", bg="white", font="宋体 45", padx=12, pady=12)
time_label.pack(side=TOP)

# 单选框
frame = Frame(root, pady=30, bg=bg_color)
# 特殊变量和单选框进行关联
var = StringVar()
Radiobutton(frame, text="24h", value="24h", font="宋体 12", bg=bg_color, padx=5, variable=var,
            activebackground=bg_color).pack(side=LEFT)
Radiobutton(frame, text="12h", value="12h", font="宋体 12", bg=bg_color, padx=5, variable=var,
            activebackground=bg_color).pack(side=RIGHT)
var.set("24h")
frame.pack(side=BOTTOM)


def update_time():
    """更新时间"""
    if var.get() == "24h":
        current_time = time.strftime("%H:%M:%S")
    else:
        current_time = time.strftime("%p %I:%M:%S")
    time_label.config(text=current_time)
    time_label.after(200, update_time)


update_time()
# 消息循环
root.mainloop()
