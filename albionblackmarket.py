from mysql.connector import Error
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from config import connection
from frame.frame1 import create_frame1
from frame.frame2 import Frame2_Class
from frame.frame3 import Frame3_Class

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

# 創建主畫面
root = tk.Tk()
root.title("AlbionBlackMarket God")
root.geometry("795x720")

root.resizable(False, False)

notebook = ttk.Notebook(root)

create_frame1(notebook)

Frame2_Class(None, None, None, None).create_frame2(notebook)
Frame3_Class(None, None, None).create_frame3(notebook)

# 顯示 Notebook (分頁)
notebook.pack(expand=True, fill="both")

# 啟動前執行
on_startup()

# 設定視窗圖示
root.iconbitmap("abm.ico")

# 開始主循環
root.mainloop()