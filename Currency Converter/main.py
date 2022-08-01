from concurrent.futures import process
import tkinter as tk
from tkinter import Frame, StringVar, ttk
from tkinter import font
from __init__ import *

# Functions --------------------------------------

def convert_currency():
    conv1 = selectedUsdAmount.get()
    conv2 = selectedAmount.get()
    convert_currency = selectedCurrency.get()

    if conv2 == "":
        converter = processed_data.get(convert_currency)
        finalAmount = float(conv1) * float(converter[0])
        convertAmount.set(f"{finalAmount:.2f} {convert_currency}")

    elif conv1 == "":
        converter = processed_data.get(convert_currency)
        finalAmount = float(conv1) * float(converter[0])
        convertAmount.set(f"{finalAmount:.2f} US Dollars")

def refresh():
    recheck_prices(refresh_data())
    return True

# Main Window -------------------------------------
if __name__ == "__main__":
# Window Generation ---------------------

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.grid(column=0, row=0, sticky='nsew')
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.title("Currency Converter")
    root.iconbitmap('images/favicon.ico')
    root.resizable(False, False)

    HEIGHT = 400
    WIDTH = 200

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width/2 - HEIGHT/2)
    center_y = int(screen_height/2 - WIDTH/2)

    root.geometry(f"{HEIGHT}x{WIDTH}+{center_x}+{center_y}")

# ---------------------------------------

# Window Widgets ------------------------
    style = ttk.Style()
    
    currencies = [x for x in processed_data.keys()]

    usdLabel = ttk.Label(frame, text="US Dollars")
    usdLabel.pack(pady=(15, 3))

    selectedUsdAmount = tk.StringVar()
    usdAmount = tk.Entry(frame, textvariable=selectedUsdAmount)
    usdAmount.pack(pady=(0, 10))

    selectedCurrency = tk.StringVar()
    currenciesMenu = ttk.Combobox(frame, textvariable=selectedCurrency, justify='center', width=17)
    currenciesMenu.pack(pady=(0, 5))
    currenciesMenu['values'] = currencies
    currenciesMenu['state'] = 'readonly'

    selectedAmount = tk.StringVar()
    amount = tk.Entry(frame, textvariable=selectedAmount)
    amount.pack(pady=(0, 10))

    convertButton = ttk.Button(frame, text="Convert", command=convert_currency)
    convertButton.pack(pady=(0, 5))

    convertMsgLabel = ttk.Label(frame, text="You would have:", justify="center")
    convertMsgLabel.pack()

    convertAmount = tk.StringVar(value="0 Dollars")
    convertLabel = ttk.Label(frame, textvariable=convertAmount, justify="center")
    convertLabel.pack()

    style.configure("export.TButton", font=(None, 7))
    exportButton = ttk.Button(frame, text="Refresh", style="export.TButton", command=refresh)
    exportButton.place(x=295, y=170, height=25, width=100)







    root.mainloop()