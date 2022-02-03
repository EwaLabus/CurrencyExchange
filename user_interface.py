import tkinter as tk

from tkinter import ttk
from tkcalendar import DateEntry
import datetime

class main_interface:
    def __init__(self):
        self.master = tk.Tk()
        self.master.resizable(False, False)
        self.amount_entry = None
        self.result = None
        self.selected_old_currency = tk.StringVar()
        self.selected_new_currency = tk.StringVar()

        tk.Label(self.master, text="Date:").grid(column=0, row=0, sticky='e')

        today = datetime.date.today()
        self.date_entry = DateEntry(self.master, values="Text", year=today.year, month=today.month, day=today.day, state="readonly", date_pattern="yyyy-mm-dd")
        self.date_entry.grid(column=1, row=0, sticky='w', padx=20, pady=5)
        tc = ttk.Notebook(self.master)
        self.t1 = ttk.Frame(tc)
        self.t2 = ttk.Frame(tc)
        tc.add(self.t1, text='Enter currency')
        tc.add(self.t2, text='Ebay')
        tc.grid(column=0, row=1, columnspan=2)
        self.create_card_1()
        self.create_card_2()

        self.master.mainloop()

    def calculate_card_1(self):
        self.result.configure(text="Text Updated")

    def create_card_1(self):
        tk.Label(self.t1, text="Amount:").grid(column=0, row=1, sticky='w')
        tk.Label(self.t1, text="New amount:").grid(column=0, row=5, sticky='w')
        tk.Label(self.t1, text="Original currency:").grid(column=0, row=2, sticky='w')
        tk.Label(self.t1, text="New Currency:").grid(column=0, row=3, sticky='w')

        self.amount_entry = tk.Entry(self.t1)
        self.amount_entry.grid(column=1, row=1, sticky='e')
        self.result = tk.Label(self.t1, text="test")
        self.result.grid(column=1, row=5, sticky='w')

        old_currency_cb = ttk.Combobox(self.t1, textvariable=self.selected_old_currency)
        new_currency_cb = ttk.Combobox(self.t1, textvariable=self.selected_new_currency)
        old_currency_cb.grid(column=1, row=2, sticky='e')
        new_currency_cb.grid(column=1, row=3, sticky='e')

        old_currency_cb['values'] = ['ABC', 'b']
        old_currency_cb['state'] = 'readonly'
        new_currency_cb['values'] = ['a', 'bs']
        new_currency_cb['state'] = 'readonly'


        tk.Button(self.t1, text="Calculate", command=self.calculate_card_1).grid(column=0, row=4, columnspan=2)

    def create_card_2(self):
        ttk.Label(self.t2, text="Notebook widget demonstration").grid(column=3, row=3)

    def get_combobox_options(self):
        pass
