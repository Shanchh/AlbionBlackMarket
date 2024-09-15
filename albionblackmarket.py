from mysql.connector import Error
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from insert_data import insert_data
from config import connection
from pynput import keyboard
from script import check_script
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
                tree_scroll(val)
        if key.char == 'e':
            value = check_script()
            for i in value:
                for val in i:
                    tree_scroll(val)
        print(value)
    except AttributeError:
        pass
    except TypeError as e:
        print(f"輸入錯誤: {e}")
    except Exception as e:
        print(f"其他錯誤: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        global start_listening
        start_listening = False
        print("已退出監聽")
        label2.config(text="尚未開始偵測", bg="lightblue")
        return False
    
# 啟動鍵盤監聽的函數
def start_keyboard_listener():
    global start_listening
    if start_listening == True:
        pass
    else:
        start_listening = True
        print("監聽啟動！按 'w' 鍵會觸發事件，按 'Esc' 鍵退出。")
        label2.config(text="正在偵測中", bg="red")
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

# Tkinter 按鈕觸發的函數
def start_listener_thread():
    listener_thread = threading.Thread(target=start_keyboard_listener)
    listener_thread.daemon = True  # 設置守護進程，讓程式退出時自動關閉
    listener_thread.start()

def tree_scroll(val):
    tree_insert_price.insert("", "end", values=val)
    # 自動滾動到最底部
    scroll_to_bottom()

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

label2 = tk.Label(frame2, text="尚未開始偵測", bg="lightblue")
label2.place(x=65, y=7)

# 顯示 Treeview 
tree_insert_price = ttk.Treeview(frame2, columns=("Date", "Time", "Item", "Tier", "Enchantment", "SellOrder", "AveragePrice"), show="headings")
tree_insert_price.place(x=5, y=40)

tree_ip_value = ["Date", 100], ["Time", 100], ["Item", 120], ["Tier", 100], ["Enchantment", 100], ["SellOrder", 120], ["AveragePrice", 120]

for tree_for in tree_ip_value:
    tree_insert_price.heading(tree_for[0], text=tree_for[0])
    tree_insert_price.column(tree_for[0], width = tree_for[1])

vsb = ttk.Scrollbar(frame2, orient="vertical", command=tree_insert_price.yview)
vsb.place(x=767, y=41, height=225)

tree_insert_price.configure(yscrollcommand=vsb.set)

def scroll_to_bottom():
    tree_insert_price.yview_moveto(1)  # 1 代表滾動到最底部
# --------------------------------------------------------------------------#

# 顯示 Notebook (分頁)
notebook.pack(expand=True, fill="both")

# 啟動前執行
on_startup()

# 設定視窗圖示
root.iconbitmap("abm.ico")

# 開始主循環
root.mainloop()

