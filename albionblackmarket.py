from mysql.connector import Error
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from insert_data import insert_data, insert_resource_data
from config import connection
from pynput import keyboard
from script import check_script, resource_script, resource_tier_script, resource_enchant_script
from data_processing import resource_price_search
import threading
import time

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
            print(value)
            
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
    tree_insert_price.yview_moveto(1)  # 1 代表滾動到最底部

def tree_resource_scroll(val):

    tree_resource_price.insert("", "end", values=val)

    tree_resource_price.yview_moveto(1)  # 自動滾動到最底部 1代表滾動到最底部

def resource_button_click():

    for Category in range(4):

        resource_script(Category)

        for Tier in range(5):

            resource_tier_script(Tier)

            for Enchant in range(5):

                resource_enchant_script(Enchant)

                time.sleep(2)
                data = insert_resource_data(Category, Tier + 4, Enchant)

                print(data)
                for datas in data:
                    tree_resource_scroll(datas)

                tree_resource_price.update()  # 立即更新顯示

def on_select(event):

    select_resource = resource_price_search(Frame3_combobox1.get())

    for item in Frame3_tree_resource.get_children():

        Frame3_tree_resource.delete(item)

    for value in select_resource:

        Frame3_tree_resource.insert("", "end", values=value)

# 創建主畫面
root = tk.Tk()
root.title("AlbionBlackMarket God")
root.geometry("1280x720")

root.resizable(False, False)

notebook = ttk.Notebook(root)

# --------------------------------------------------------------------------#
# 創建頁面1
frame1 = tk.Frame(notebook, bg="#FFE4E1")
notebook.add(frame1, text="黑市總覽")

# 頁面1的內容
label1 = tk.Label(frame1, text="這是頁面 1 的內容", bg="lightblue")
label1.pack(pady=20)
# --------------------------------------------------------------------------#

# --------------------------------------------------------------------------#
# 創建頁面2
frame2 = tk.Frame(notebook, bg='#dbead5')
notebook.add(frame2, text="資料新增")

# 頁面2的內容
button = tk.Button(frame2, text="開啟偵測", command = start_listener_thread)
button.place(x=5, y=5)

label2 = tk.Label(frame2, text="尚未開始偵測", bg="lightblue")
label2.place(x=68, y=7)

# 顯示 Treeview 
tree_insert_price = ttk.Treeview(frame2, columns=("日期", "時間", "裝備名稱", "階級", "附魔等級", "目前黑市售價", "四週平均售價"), show="headings")
tree_insert_price.place(x=5, y=40)

tree_ip_value = ["日期", 100], ["時間", 100], ["裝備名稱", 120], ["階級", 100], ["附魔等級", 100], ["目前黑市售價", 120], ["四週平均售價", 120]

for tree_for in tree_ip_value:
    tree_insert_price.heading(tree_for[0], text=tree_for[0])
    tree_insert_price.column(tree_for[0], width = tree_for[1])

# 滾動軸
vsb = ttk.Scrollbar(frame2, orient="vertical", command=tree_insert_price.yview)
vsb.place(x=767, y=41, height=225)

tree_insert_price.configure(yscrollcommand=vsb.set)

# 半成品價格
button2 = tk.Button(frame2, text="開啟材料腳本", command = resource_button_click)
button2.place(x=5, y=275)

tree_resource_price = ttk.Treeview(frame2, columns=("日期", "時間", "半成品名稱", "階級", "附魔等級", "市場估價"), show="headings")
tree_resource_price.place(x=5, y=310)

tree_rs_value = ["日期", 100], ["時間", 100], ["半成品名稱", 120], ["階級", 100], ["附魔等級", 100], ["市場估價", 120]

for tree_for in tree_rs_value:
    tree_resource_price.heading(tree_for[0], text=tree_for[0])
    tree_resource_price.column(tree_for[0], width = tree_for[1])

# 滾動軸
vsb = ttk.Scrollbar(frame2, orient="vertical", command=tree_resource_price.yview)
vsb.place(x=647, y=310, height=225)
    
tree_resource_price.configure(yscrollcommand=vsb.set)

# --------------------------------------------------------------------------#

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

