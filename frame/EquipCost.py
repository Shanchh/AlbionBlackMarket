import tkinter as tk
from tkinter import ttk
from equip.list import ECList_First_options, ECList_Second_options, ECList_Third_options, ECList_Third_english

class EquipCost:
    def __init__(self, notebook):

        self.notebook = notebook
        self.EquipCost = tk.Frame(notebook, bg="#D2E9FF")

        self.EquipCost_CB_First = ttk.Combobox(self.EquipCost, values = ECList_First_options, state = "readonly", width=15)
        self.EquipCost_CB_First.place(x=102, y=10)
        self.EquipCost_CB_First.set("選擇一個選項")

        self.EquipCost_CB_Second = ttk.Combobox(self.EquipCost, state = "readonly", width=15)
        self.EquipCost_CB_Second.place(x=235, y=10)


    def Create_EquipCost_Frame(self):
        
        self.notebook.add(self.EquipCost, text="裝備製作成本")

        EC_Info_Label = tk.Label(self.EquipCost, text="裝備製作成本表", bg="#d8bfd8")
        EC_Info_Label.place(x=5, y=10)

        self.EquipCost_CB_First.bind("<<ComboboxSelected>>", self.update_second)
        
    def update_second(self, event):

        select_first = self.EquipCost_CB_First.current()
        self.EquipCost_CB_Second["values"] = ECList_Second_options[select_first]
        self.EquipCost_CB_Second.current(0)