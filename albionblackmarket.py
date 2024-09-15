from mysql.connector import Error
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from insert_data import insert_data
from config import connection
from pynput import keyboard
import threading

start_listening = False

def on_startup():
    try:
        # 連接到 MySQL 資料庫
        if connection.is_connected():
            print("成功連接到資料庫")

    except Error as e:
        messagebox.showerror("錯誤", f"連接失敗: {e}")
        print(f"連接失敗: {e}")

def on_press(key):
    try:
        if key.char == 'w':
            value = insert_data()
            for val in value:
                tree.insert("", "end", values=val)
            
                # 自動滾動到最底部
                scroll_to_bottom()
        print(value)
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        global start_listening
        start_listening = False
        print("已退出監聽")
        return False
    
# 啟動鍵盤監聽的函數
def start_keyboard_listener():
    global start_listening
    if start_listening == True:
        pass
    else:
        start_listening = True
        print("監聽啟動！按 'w' 鍵會觸發事件，按 'Esc' 鍵退出。")
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

# Tkinter 按鈕觸發的函數
def start_listener_thread():
    listener_thread = threading.Thread(target=start_keyboard_listener)
    listener_thread.daemon = True  # 設置守護進程，讓程式退出時自動關閉
    listener_thread.start()

# 創建主畫面
root = tk.Tk()
root.title("AlbionBlackMarket God")
root.geometry("1280x720")

root.resizable(False, False)

notebook = ttk.Notebook(root)

# --------------------------------------------------------------------------#
# 創建頁面1
frame1 = tk.Frame(notebook, bg="lightblue")
notebook.add(frame1, text="黑市總覽")

# 頁面1的內容
label1 = tk.Label(frame1, text="這是頁面 1 的內容", bg="lightblue")
label1.pack(pady=20)
# --------------------------------------------------------------------------#

# --------------------------------------------------------------------------#
# 創建頁面2
frame2 = tk.Frame(notebook, bg="lightgreen")
notebook.add(frame2, text="資料新增")

# 頁面2的內容
button = tk.Button(frame2, text="開啟偵測", command = start_listener_thread)
button.place(x=5, y=5)

# 顯示 Treeview
tree = ttk.Treeview(frame2, columns=("Date", "Time", "Item", "Tier", "Enchantment", "SellOrder", "AveragePrice"), show="headings")
tree.place(x=5, y=40)

tree.heading("Date", text="Date")
tree.heading("Time", text="Time")
tree.heading("Item", text="Item")
tree.heading("Tier", text="Tier")
tree.heading("Enchantment", text="Enchantment")
tree.heading("SellOrder", text="Sell Order Now")
tree.heading("AveragePrice", text="Average Price")

tree.column("Date", width=100)
tree.column("Time", width=100)
tree.column("Item", width=120)
tree.column("Tier", width=100)
tree.column("Enchantment", width=100)
tree.column("SellOrder", width=120)
tree.column("AveragePrice", width=120)

vsb = ttk.Scrollbar(frame2, orient="vertical", command=tree.yview)
vsb.place(x=767, y=41, height=225)

tree.configure(yscrollcommand=vsb.set)

def scroll_to_bottom():
    tree.yview_moveto(1)  # 1 代表滾動到最底部
# --------------------------------------------------------------------------#

# 顯示 Notebook (分頁)
notebook.pack(expand=True, fill="both")

# 啟動前執行
on_startup()

# 設定視窗圖示
root.iconbitmap("abm.ico")

# 開始主循環
root.mainloop()

