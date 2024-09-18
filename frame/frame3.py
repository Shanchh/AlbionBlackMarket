import tkinter as tk
from tkinter import ttk
from data_processing import resource_price_search

class Frame3_Class:
    def __init__(self, frame3, Frame3_combobox1, Frame3_tree_resource):
        
        self.frame3 = frame3
        self.Frame3_combobox1 = Frame3_combobox1
        self.Frame3_tree_resource = Frame3_tree_resource

    # 創建頁面3
    def create_frame3(self, notebook):

        self.frame3 = tk.Frame(notebook, bg="#e6e6fa")
        notebook.add(self.frame3, text="半成品價格")

        # 頁面3的內容
        Frame3_label1 = tk.Label(self.frame3, text="半成品市場估價", bg="#d8bfd8")
        Frame3_label1.place(x=5, y=10)

        Frame3_combobox1_options = ["1-布料", "2-皮革", "3-礦條", "4-木條"]
        self.Frame3_combobox1 = ttk.Combobox(self.frame3, values = Frame3_combobox1_options, state = "readonly")
        self.Frame3_combobox1.place(x=102, y=10)

        # 設置預設選項
        self.Frame3_combobox1.set("選擇一個選項")

        self.Frame3_combobox1.bind("<<ComboboxSelected>>", self.on_select)

        columns = ("", "附魔0", "附魔1", "附魔2", "附魔3", "附魔4")
        self.Frame3_tree_resource = ttk.Treeview(self.frame3, columns=columns, show="headings", selectmode="none")

        for col in columns:
            self.Frame3_tree_resource.heading(col, text=col)
            self.Frame3_tree_resource.column(col, width=100, anchor='center')

        data = [("Tier4"), ("Tier5"), ("Tier6"), ("Tier7"), ("Tier8")]

        # 插入每一行數據
        for row in data:
            self.Frame3_tree_resource.insert("", "end", values=row)

        self.Frame3_tree_resource.place(x=5, y=40, height=127)

    def on_select(self, event):

        select_resource = resource_price_search(self.Frame3_combobox1.get())

        for item in self.Frame3_tree_resource.get_children():

            self.Frame3_tree_resource.delete(item)

        for value in select_resource:

            self.Frame3_tree_resource.insert("", "end", values=value)