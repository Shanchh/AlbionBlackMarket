import tkinter as tk
import threading
from pynput import keyboard
from tkinter import ttk
import time

from insert_data import insert_data, insert_resource_data
from script import check_script, resource_script, resource_tier_script, resource_enchant_script


class Frame2_Class:
    def __init__(self, frame2, label2, tree_insert_price, tree_resource_price):
        self.frame2 = frame2
        self.start_listening = False
        self.label2 = label2
        self.tree_insert_price = tree_insert_price
        self.tree_resource_price = tree_resource_price

    # 創建頁面2
    def create_frame2(self, notebook):

        self.frame2 = tk.Frame(notebook, bg='#dbead5')
        notebook.add(self.frame2, text="資料新增")

        # 頁面2的內容
        button = tk.Button(self.frame2, text="開啟偵測", command = self.start_listener_thread)
        button.place(x=5, y=5)

        self.label2 = tk.Label(self.frame2, text="尚未開始偵測", bg="lightblue")
        self.label2.place(x=68, y=7)

        # 顯示 Treeview 
        self.tree_insert_price = ttk.Treeview(self.frame2, columns=("日期", "時間", "裝備名稱", "階級", "附魔等級", "目前黑市售價", "四週平均售價"), show="headings")
        self.tree_insert_price.place(x=5, y=40)

        tree_ip_value = ["日期", 100], ["時間", 100], ["裝備名稱", 120], ["階級", 100], ["附魔等級", 100], ["目前黑市售價", 120], ["四週平均售價", 120]

        for tree_for in tree_ip_value:
            self.tree_insert_price.heading(tree_for[0], text=tree_for[0])
            self.tree_insert_price.column(tree_for[0], width = tree_for[1])

        # 滾動軸
        vsb = ttk.Scrollbar(self.frame2, orient="vertical", command=self.tree_insert_price.yview)
        vsb.place(x=767, y=41, height=225)

        self.tree_insert_price.configure(yscrollcommand=vsb.set)

        # 半成品價格
        button2 = tk.Button(self.frame2, text="開啟材料腳本", command = self.resource_button_click)
        button2.place(x=5, y=275)

        self.tree_resource_price = ttk.Treeview(self.frame2, columns=("日期", "時間", "半成品名稱", "階級", "附魔等級", "市場估價"), show="headings")
        self.tree_resource_price.place(x=5, y=310)

        tree_rs_value = ["日期", 100], ["時間", 100], ["半成品名稱", 120], ["階級", 100], ["附魔等級", 100], ["市場估價", 120]

        for tree_for in tree_rs_value:
            self.tree_resource_price.heading(tree_for[0], text=tree_for[0])
            self.tree_resource_price.column(tree_for[0], width = tree_for[1])

        # 滾動軸
        vsb = ttk.Scrollbar(self.frame2, orient="vertical", command=self.tree_resource_price.yview)
        vsb.place(x=647, y=310, height=225)
            
        self.tree_resource_price.configure(yscrollcommand=vsb.set)

    # Tkinter 按鈕觸發的函數
    def start_listener_thread(self):
        listener_thread = threading.Thread(target=self.start_keyboard_listener)
        listener_thread.daemon = True  # 設置守護進程，讓程式退出時自動關閉
        listener_thread.start() # 啟動鍵盤監聽器

    # 啟動鍵盤監聽的函數
    def start_keyboard_listener(self):

        # 如果 start_listening 為 True 代表已開啟監聽,忽略不處理
        if self.start_listening == True:

            pass

        else:

            # 設定 start_listening 為啟用
            self.start_listening = True
            print("監聽啟動！按 'w' 鍵會觸發事件，按 'Esc' 鍵退出。")
            # 更新 label2 監聽狀態顯示文字
            self.label2.config(text="正在偵測中", bg="red")
            # 鍵盤監聽器 on_press鍵盤按下, on_release鍵盤釋放
            with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
                listener.join()

    # 監聽器中:按鍵按下
    def on_press(self, key):

        try:

            # 如果按下 W 鍵 (單獨上傳黑市裝備價格)
            if key.char == 'w':
                
                # 黑市裝備價格擷取並讀取內容,將數據導入至資料庫 | value = (日期, 時間, 裝備名稱, 階級, 附魔等級, 現在售價, 四週平均價)
                value = insert_data()
                # 單獨取 value 內的值
                for val in value:
                    # 輸入數值進 tree_insert_price 樹狀顯示
                    self.tree_scroll(val)
                print(value)
            
            # 如果按下 E 鍵 (4.0~8.4 整套查價)
            if key.char == 'e':
                
                # 執行黑市裝備 4.0~8.4 查價腳本並回傳總數據
                value = check_script()
                # 單獨讀取各階級各附魔價格資料
                for i in value:
                    # 單獨讀取各項數據
                    for val in i:
                        # 輸入數值進 tree_insert_price 樹狀顯示
                        self.tree_scroll(val)
                print(value)

        # 按下特殊按鍵的例外事件處理
        except AttributeError:
            pass
        # 輸入錯誤數值的例外事件處理
        except TypeError as e:
            print(f"輸入錯誤: {e}")
        # 常見錯誤例外事件處理
        except Exception as e:
            print(f"其他錯誤: {e}")

    # 監聽器中:按鍵釋放
    def on_release(self, key):

        # 如果按下 W 鍵 (中斷監聽)
        if key == keyboard.Key.esc:
            # 全域 裝備價格監聽狀態
            global start_listening
            # 設定 裝備價格監聽狀態 為關閉
            start_listening = False
            print("已退出監聽")
            # 更新 Label2 內容及背景顏色為"亮藍色"
            self.label2.config(text="尚未開始偵測", bg="lightblue")
            return False
        
    def resource_button_click(self):

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
                        self.tree_resource_scroll(datas)

                    self.tree_resource_price.update()  # 立即更新顯示

    # 輸入數值進 tree_insert_price 樹狀顯示
    def tree_scroll(self, val):

        self.tree_insert_price.insert("", "end", values=val)

        self.tree_insert_price.yview_moveto(1) # 自動滾動到最底部 1代表滾動到最底部

    def tree_resource_scroll(self, val):

        self.tree_resource_price.insert("", "end", values=val)

        self.tree_resource_price.yview_moveto(1) # 自動滾動到最底部 1代表滾動到最底部