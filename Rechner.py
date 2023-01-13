from tkinter import *

root = Tk()
root.title("Lustiger Titel")
root.geometry("600x600")

label_watt = Label(root, text="Verbrauch in Watt")
label_watt.grid()

entry_watt = Entry(root)
entry_watt.grid(column=2, row=0)

label_betriebsstunden = Label(root, text="Betriebsstunden / Tag")
label_betriebsstunden.grid(column=3, row=0)

entry_betriebsstunden = Entry(root)
entry_betriebsstunden.grid(column=4, row=0)

label_result = Label(root, text="Watt per hours:")
label_result.grid(column=0, row=1)

label_result_2 = Label(root, text="")
label_result_2.grid(column=1, row=1)


def calculate():
    label_result_2.configure(
        text=f"{int(entry_watt.get())*int(entry_betriebsstunden.get())}"
    )


button_calculate = Button(root, text="Calculate Watt per hours", command=calculate)
button_calculate.grid(column=0, row=2)

root.mainloop()
