import tkinter as tk
import requests

def convert():
    amount = float(amount_entry.get())
    
    if from_currency.get() == "USD" and to_currency.get() == "UAH":
        converted_amount = amount / usd_rate
    elif from_currency.get() == "UAH" and to_currency.get() == "USD":
        converted_amount = amount * usd_rate
    elif from_currency.get() == "EUR" and to_currency.get() == "UAH":
        converted_amount = amount / eur_rate
    elif from_currency.get() == "UAH" and to_currency.get() == "EUR":
        converted_amount = amount * eur_rate
    elif from_currency.get() == "EUR" and to_currency.get() == "USD":
        converted_amount = (amount * usd_rate) / eur_rate
    elif from_currency.get() == "USD" and to_currency.get() == "EUR":
        converted_amount = (amount * eur_rate) / usd_rate
    else:
        converted_amount = amount
    
    result_label.config(text="Результат: {:.2f} {}".format(converted_amount, to_currency.get()))

def handle_keypress(event):
    key = event.keysym
    if key == "Return" or key == "space":
        convert()

# Отримання актуальних курсів валют
response = requests.get("https://api.exchangerate-api.com/v4/latest/UAH")
data = response.json()
usd_rate = data['rates']['USD']
eur_rate = data['rates']['EUR']

# Створення графічного інтерфейсу
window = tk.Tk()
window.title("Конвертор валют")
window.geometry("300x250")

window.image = PhotoImage(file='bg/rain.png')
bg=Label(window, image=window.image)
bg.grid(row=0, column=0)

# Написи та поля вводу
amount_label = tk.Label(window, text="Сума:")
amount_label.pack()

amount_entry = tk.Entry(window)
amount_entry.pack()

from_currency_label = tk.Label(window, text="З:")
from_currency_label.pack()

from_currency = tk.StringVar(window)
from_currency.set("UAH")
from_currency_option = tk.OptionMenu(window, from_currency, "UAH", "USD", "EUR")
from_currency_option.pack()

to_currency_label = tk.Label(window, text="У:")
to_currency_label.pack()

to_currency = tk.StringVar(window)
to_currency.set("USD")
to_currency_option = tk.OptionMenu(window, to_currency, "UAH", "USD", "EUR")
to_currency_option.pack()

convert_button = tk.Button(window, text="Конвертувати", command=convert)
convert_button.pack()

result_label = tk.Label(window, text="Результат:")
result_label.pack()

# Прив'язка кнопок Enter і Space до функції обробки натискання клавіш
window.bind('<Key>', handle_keypress)

window.mainloop()
