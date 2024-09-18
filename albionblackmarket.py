from mysql.connector import Error
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from config import connection
from data_processing import resource_price_search
from frame.frame1 import create_frame1
from frame.frame2 import Frame2_Class

# 程序開啟時自動執行
def on_startup():

    try:

        # 連接到 MySQL 資料庫
        if connection.is_connected():

            print("成功連接到資料庫")

    # 連線失敗時顯示連接失敗視窗
    except Error as e:

        # 連線失敗視窗建立
        messagebox.showerror("錯誤", f"連接失敗: {e}")
        print(f"連接失敗: {e}")

def on_select(event):

    select_resource = resource_price_search(Frame3_combobox1.get())

    for item in Frame3_tree_resource.get_children():

        Frame3_tree_resource.delete(item)

    for value in select_resource:

        Frame3_tree_resource.insert("", "end", values=value)

# 創建主畫面
root = tk.Tk()
root.title("AlbionBlackMarket God")
root.geometry("795x720")

root.resizable(False, False)

notebook = ttk.Notebook(root)

create_frame1(notebook)

frame2_instance = Frame2_Class(None, None, None, None)
frame2_instance.create_frame2(notebook)

# --------------------------------------------------------------------------#
# 創建頁面3
frame3 = tk.Frame(notebook, bg="#e6e6fa")
notebook.add(frame3, text="半成品價格與裝備成本")

# 頁面3的內容
Frame3_label1 = tk.Label(frame3, text="半成品市場估價", bg="#d8bfd8")
Frame3_label1.place(x=5, y=10)

Frame3_combobox1_options = ["1-布料", "2-皮革", "3-礦條", "4-木條"]
Frame3_combobox1 = ttk.Combobox(frame3, values=Frame3_combobox1_options, state="readonly")
Frame3_combobox1.place(x=102, y=10)

# 設置預設選項
Frame3_combobox1.set("選擇一個選項")

Frame3_combobox1.bind("<<ComboboxSelected>>", on_select)

columns = ("", "附魔0", "附魔1", "附魔2", "附魔3", "附魔4")
Frame3_tree_resource = ttk.Treeview(frame3, columns=columns, show="headings", selectmode="none")

for col in columns:
    Frame3_tree_resource.heading(col, text=col)
    Frame3_tree_resource.column(col, width=100, anchor='center')

data = [("Tier4"), ("Tier5"), ("Tier6"), ("Tier7"), ("Tier8")]

# 插入每一行數據
for row in data:
    Frame3_tree_resource.insert("", "end", values=row)

Frame3_tree_resource.place(x=5, y=40, height=127)
# --------------------------------------------------------------------------#

# 顯示 Notebook (分頁)
notebook.pack(expand=True, fill="both")

# 啟動前執行
on_startup()

# 設定視窗圖示
root.iconbitmap("abm.ico")

# 開始主循環
root.mainloop()