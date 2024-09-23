import tkinter as tk
from tkinter import ttk
from equip.list import ECList_First_options, ECList_Second_options, EquipCraftList
from data_processing import resource_price_search
import math

class EquipCost:
    def __init__(self, notebook):

        self.notebook = notebook
        self.EquipCost = tk.Frame(notebook, bg="#D2E9FF")

    def Create_EquipCost_Frame(self):

        self.EquipCost_CB_First = ttk.Combobox(self.EquipCost, values = ECList_First_options, state = "readonly", width=15)
        self.EquipCost_CB_First.place(x=102, y=10)
        self.EquipCost_CB_First.set("選擇一個選項")

        self.EquipCost_CB_Second = ttk.Combobox(self.EquipCost, state = "readonly", width=15)
        self.EquipCost_CB_Second.place(x=235, y=10)
        
        self.notebook.add(self.EquipCost, text="黑市總覽")

        EC_Info_Label = tk.Label(self.EquipCost, text="裝備製作成本表", bg="#d8bfd8")
        EC_Info_Label.place(x=5, y=10)

        self.EquipCost_CB_First.bind("<<ComboboxSelected>>", self.update_second)
        self.EquipCost_CB_Second.bind("<<ComboboxSelected>>", self.updata_cost_treeview)

        EC_ReCost_Label = tk.Label(self.EquipCost, text="裝備返還率", bg="#d8bfd8")
        EC_ReCost_Label.place(x=500, y=10)
        
        ReCost_CB_options = [25, 30, 39.3, 41.3, 43.2]
        self.ReCost_CB = ttk.Combobox(self.EquipCost, state = "readonly", width=5, values = ReCost_CB_options)
        self.ReCost_CB.place(x=570, y=10)
        self.ReCost_CB.current(0)

        EC_Quantity_Label = tk.Label(self.EquipCost, text="製作數量", bg="#d8bfd8")
        EC_Quantity_Label.place(x=632, y=10)

        Quantity_CB_options = [100, 50, 10, 1, 2, 3, 5]
        self.Quantity_CB = ttk.Combobox(self.EquipCost, state = "readonly", width=5, values = Quantity_CB_options)
        self.Quantity_CB.place(x=690, y=10)
        self.Quantity_CB.current(0)

        self.ReCost_CB.bind("<<ComboboxSelected>>", self.updata_cost_treeview)
        self.Quantity_CB.bind("<<ComboboxSelected>>", self.updata_cost_treeview)

        Cost_Treeview_columns = ("裝備名稱", "5.0", "5.1", "5.2", "6.0", "6.1", "6.2", "7.0", "7.1", "7.2", "8.0", "8.1", "8.2")
        self.Cost_Treeview = ttk.Treeview(self.EquipCost, columns=Cost_Treeview_columns, show="headings", selectmode="none")
        self.Cost_Treeview.place(x=5, y=40, height=90)

        for index, col in enumerate(Cost_Treeview_columns):
            self.Cost_Treeview.heading(col, text=col)
            if index == 0:
                self.Cost_Treeview.column(col, width=150, anchor='center')
            else:
                self.Cost_Treeview.column(col, width=100, anchor='center')

    def update_second(self, event):

        self.select_first = self.EquipCost_CB_First.current()
        self.EquipCost_CB_Second["values"] = ECList_Second_options[self.select_first]
        self.EquipCost_CB_Second.current(0)
        self.updata_cost_treeview(None)

    def updata_cost_treeview(self, event):
        self.clear_costtreeview()
        self.select_second = self.EquipCost_CB_Second.current()
        total_list = []
        for value in EquipCraftList[self.select_first][self.select_second]:
            itemcost_list = [value[1]]
            if value[2] == 1:
                range_price = self.get_rangerosource_price(value[3])
                for r_price in range_price:
                    one_equipcost = round(self.cost_calculation(r_price, value[4]) / int(self.Quantity_CB.get()))
                    itemcost_list.append(one_equipcost)

            elif value[2] == 2:
                range_price1 = self.get_rangerosource_price(value[3])
                range_price2 = self.get_rangerosource_price(value[5])
                for r_price1, r_pirce2 in zip(range_price1, range_price2):
                    one_equipcost = round((self.cost_calculation(r_price1, value[4]) + self.cost_calculation(r_pirce2, value[6])) / int(self.Quantity_CB.get()))
                    itemcost_list.append(one_equipcost)
            total_list.append(itemcost_list)
        for row in total_list:
            self.Cost_Treeview.insert("", "end", values=row)
            

    def get_rangerosource_price(self, Category):
        result = resource_price_search(Category)
        range_price= []
        for val in result[1:5]:
            for i in val[1:4]:
                range_price.append(i)
        return range_price
    
    def cost_calculation(self, resourceprice, count):
        # 總成本計算 = 半成品價格 * 需求材料數量 * 製作裝備數量 * 返還率

        craft_precent = round((100 - float(self.ReCost_CB.get())) * 0.01, 3)
        quantity = int(self.Quantity_CB.get())

        equipcost_count = resourceprice * math.ceil(count * craft_precent * quantity)

        return equipcost_count
    
    def clear_costtreeview(self):
        for item in self.Cost_Treeview.get_children():
            self.Cost_Treeview.delete(item)