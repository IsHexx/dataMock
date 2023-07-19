"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
@Project : Demo
@File : mockDataGUI.py
@Time : 2023/4/28 10:12
"""
import logging
from tkinter import *
import tkinter as tk
from tkinter import INSERT, ttk
import ttkbootstrap as ttkp
from mock import MockData

operation = {
    "当前日期": "get_today_date",
    "当前时间": "get_current_datetime",
    "中文姓名": "generate_name",
    "电话号码": "generate_phone_number",
    "指定位数小数": "generate_random_float",
    "银行卡号": "generate_bank_card_number",
    "身份证号码": "generate_ssn",
    "组织机构代码": "generate_organization_code",
    "统一社会信用代码": "generate_credit_code",
    "邮箱": "get_email"
}

WINDOW_TITLE = "模拟数据生成器"
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 700
WINDOW_PADDING = 10
LABEL_TEXT = "请输入一个方法名:"
# ENTRY_WIDTH = 30
BUTTON_TEXT = "执行"
TEXT_WIDTH = 40
TEXT_HEIGHT = 22

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("mock_data_gui.log")
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


class MockDataGUI:
    def __init__(self):
        """
        构造MockDataGUI对象所需的所有属性。参数
        ----
        None
        """

        # 创建一个根窗口，并设置它的标题、大小和位置
        # self.root = tk.Tk()
        # self.root.title(WINDOW_TITLE)
        self.root = ttkp.Window(size=(510, 800), title=WINDOW_TITLE)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - WINDOW_WIDTH) // 2
        y = (screen_height - WINDOW_HEIGHT) // 2
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")
        # self.root.position_center()
        # 创建一个MockData实例，用来生成模拟数据
        self.md = MockData()

        # 创建一个标签，用来显示方法名输入框的提示，并按照网格布局放置它
        self.method_label = tk.Label(self.root, text=LABEL_TEXT)

        # 创建一个标签，用来显示参数输入框的提示，并按照网格布局放置它
        self.param_label = tk.Label(
            self.root, text=LABEL_TEXT.replace(
                "方法名", "参数"))

        # 创建一个标签，用来显示数量输入框的提示，并按照网格布局放置它
        self.number_label = tk.Label(self.root, text="生成数量:")
        self.method_label.grid(
            row=0,
            column=0,
            columnspan=1,
            padx=(0, 30),
            pady=WINDOW_PADDING,
            sticky="e"
            )
        self.param_label.grid(
            row=1,
            column=0,
            columnspan=1,
            padx=(0, 30),
            pady=WINDOW_PADDING,
            sticky="e"
            )
        self.number_label.grid(
            row=2,
            column=0,
            columnspan=1,
            padx=(0, 30),
            pady=WINDOW_PADDING,
            sticky="e"
        )

        # 创建一个下拉列表框组件
        self.combo = ttk.Combobox(self.root)

        # 设置下拉列表框的值为字典的键
        self.combo["values"] = list(operation.keys())
        # 设置默认选项为第一个键
        self.combo.current(0)

        # 创建一个输入框，用来接收用户输入的参数，并按照网格布局放置它
        self.param_entry = tk.Entry(self.root)

        # 创建一个输入框，用来获取生成数据的个数
        self.number_entry = tk.Entry(
            self.root)
        self.number_entry.insert(END, "1")
        self.combo.grid(
            row=0,
            column=1,
            columnspan=1,
            padx=(0, 10),
            pady=WINDOW_PADDING,
            sticky="nesw"
            )
        self.param_entry.grid(
            row=1,
            column=1,
            columnspan=1,
            padx=(0, 10),
            pady=WINDOW_PADDING,
            sticky="nesw"
            )
        self.number_entry.grid(
            row=2,
            column=1,
            columnspan=1,
            padx=(0, 10),
            pady=WINDOW_PADDING,
            sticky="nesw"
            )

        # 创建一个按钮，用来执行方法并显示结果，并绑定execute_method函数，并按照网格布局放置它
        self.execute_button = tk.Button(
            self.root, text=BUTTON_TEXT, command=self.execute_method)
        self.execute_button.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=WINDOW_PADDING,
            pady=WINDOW_PADDING,
            sticky="e")

        # 创建一个文本控件，用来显示结果或错误信息，并按照网格布局放置它
        self.result_text = tk.Text(
            self.root, width=TEXT_WIDTH, height=TEXT_HEIGHT)
        self.result_text.grid(row=4, column=0, columnspan=2, rowspan=5, padx=WINDOW_PADDING, pady=WINDOW_PADDING,
                              sticky=N + W + W + E)

    def execute_method(self):
        """
        执行用户输入的方法并显示结果或错误信息。
        参数None
        返回None
        """
        # 获取用户选择的键
        # 清空文本控件
        self.result_text.delete(1.0, tk.END)
        key = self.combo.get()
        # 获取字典的对应值（函数名）
        func = operation[key]

        # 从输入框中获取方法名
        method_name = func
        print(f"{method_name} datatype is {type(method_name)}")

        # 获取循环的次数
        n = self.number_entry.get()

        # 从输入框中获取参数
        params = self.param_entry.get()

        # 尝试将参数转换为正确的类型
        try:
            if params:
                params = self.param_entry.get().split(",")
                params = [eval(param) for param in params]
        except (SyntaxError, ValueError) as e:
            # 处理无效的参数
            logger.error(f"Invalid parameters: {params}")
            logger.exception(e)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "无效的参数")
            return

        # 尝试使用getattr函数从md中获取对应的方法
        try:
            method = getattr(self.md, method_name)
        except AttributeError as e:
            # 处理无效的方法名
            logger.error(f"Invalid method name: {method_name}")
            logger.exception(e)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "无效的方法名")
            return

        # 尝试使用*params调用方法并获取结果
        for i in range(int(n)):
            try:
                result = method(*params)
            except (TypeError, NameError) as e:
                # 处理不匹配的参数
                logger.error(f"Mismatched parameters: {params}")
                logger.exception(e)
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, "参数不匹配")
                return
            # 将结果插入到文本控件中
            self.result_text.insert(tk.END, result)
            self.result_text.insert(INSERT, "\n")


md_gui = MockDataGUI()
md_gui.root.mainloop()
