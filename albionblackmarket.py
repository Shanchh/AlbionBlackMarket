from mysql.connector import Error
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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
            insert_data()
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        print("已退出監聽")
        return False
    
# 啟動鍵盤監聽的函數
def start_keyboard_listener():
    global start_listening
    if start_listening == True:
        pass
    else:
        start_listening = True
        print("監聽啟動！按 'a' 鍵會觸發事件，按 'Esc' 鍵退出。")
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
# 創建頁面12
frame2 = tk.Frame(notebook, bg="lightgreen")
notebook.add(frame2, text="資料新增")

# 頁面2的內容
label2 = tk.Label(frame2, text="這是頁面 2 的內容", bg="lightgreen")
label2.pack(pady=20)

button = tk.Button(frame2, text="輸入資料", command = start_listener_thread)
button.pack(pady=50)
# --------------------------------------------------------------------------#

# 顯示 Notebook (分頁)
notebook.pack(expand=True, fill="both")

# 啟動前執行
on_startup()

# 設定視窗圖示
root.iconbitmap("abm.ico")

# 開始主循環
root.mainloop()

