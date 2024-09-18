import tkinter as tk

def create_frame1(notebook):

    # 創建頁面1
    frame1 = tk.Frame(notebook, bg="#FFE4E1")
    notebook.add(frame1, text="黑市總覽")

    # 頁面1的內容
    label1 = tk.Label(frame1, text="這是頁面 1 的內容", bg="lightblue")
    label1.pack(pady=20)