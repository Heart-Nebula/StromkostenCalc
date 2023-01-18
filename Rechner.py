from tkinter import *
from tkinter import ttk

items = []
# root window
root = Tk()
root.title("Stromrechner v1")
root.geometry("1000x600")
root.resizable(width=False, height=False)
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")
# root.attributes("-fullscreen", True)

# main parent frame
mainFrame = ttk.Frame(root)
mainFrame.grid(padx=(10, 0), pady=(10, 0))


# EINGABEN ------------------------------------------------------------------
# eingabe wattverbrauch
l_watt = ttk.Label(mainFrame, name="l_watt", text="Verbrauch in Watt:")
l_watt.grid(column=0, row=0, sticky=W)

e_watt = ttk.Entry(mainFrame, name="e_watt", width=10)
e_watt.grid(column=1, row=0, sticky=W)

# eingabe betriebsstunden
l_daily_usage = ttk.Label(mainFrame, text="Betriebsstunden / Tag:")
l_daily_usage.grid(column=2, row=0, sticky=W, padx=(20, 0))

# e_hours_day = ttk.Entry(mainFrame, width=10)
# e_hours_day.grid(column=3, row=0, sticky=NSEW, padx=(5, 0))
hours = list(range(1, 25))

com_hours_per_day = ttk.Combobox(mainFrame, values=hours, state="readonly", width=3)
com_hours_per_day.current(0)
com_hours_per_day.grid(column=3, row=0, sticky=W, padx=(5, 0))

# eingabe betriebstage pro woche
l_days_per_week = ttk.Label(mainFrame, text="Betriebstage / Woche:")
l_days_per_week.grid(column=4, row=0, sticky=W, padx=(20, 0))

days = list(range(1, 8))

com_days_per_week = ttk.Combobox(mainFrame, values=days, state="readonly", width=3)
com_days_per_week.current(0)
com_days_per_week.grid(column=5, row=0, sticky=W, padx=(5, 0))

# eingabe strompreis
l_power_cost = ttk.Label(mainFrame, text="Strompreis pro kWh:")
l_power_cost.grid(column=6, row=0, sticky=W, padx=(20, 0))

e_cost = ttk.Entry(mainFrame, width=10)
e_cost.grid(column=7, row=0, sticky=W, padx=(5, 0))

# ANZEIGEN ------------------------------------------------------------------
# anzeige kwh pro tag
s_items = ttk.Scrollbar(mainFrame)
s_items.grid(column=4, row=1, sticky=["N", "S", "W"], pady=(15, 0))


tv_items = ttk.Treeview(
    mainFrame,
    columns=["1", "2", "3", "4", "5"],
    selectmode=BROWSE,
    yscrollcommand=s_items.set,
    show="headings",
)
tv_items.column("1", anchor=CENTER, stretch=False, width=100)
tv_items.column("2", anchor=CENTER, stretch=False, width=100)
tv_items.column("3", anchor=CENTER, stretch=False, width=100)
tv_items.column("4", anchor=CENTER, stretch=False, width=100)
tv_items.column("5", anchor=CENTER, width=80)
tv_items.heading("1", text="Name", anchor=CENTER)
tv_items.heading("2", text="Watt usage", anchor=CENTER)
tv_items.heading("3", text="Hours / day", anchor=CENTER)
tv_items.heading("4", text="Days / week", anchor=CENTER)
tv_items.heading("5", text="Power cost", anchor=CENTER)
tv_items.grid(column=0, row=1, columnspan=4, pady=(15, 0), sticky=W)

s_items.configure(command=tv_items.yview)

tv_items.insert("", index="end", text="lol", values=("pog", "pog", "pog", "pog", "pog"))

l_kwh_day = ttk.Label(mainFrame, text="Verbrauch pro Tag:")
l_kwh_day.grid(column=0, row=2, sticky=W, pady=(10, 0))

l_kwh_day_2 = ttk.Label(mainFrame, text="")
l_kwh_day_2.grid(column=1, row=2, sticky=W, padx=(4, 0), pady=(10, 0))
# anzeige kwh pro woche
l_kwh_week = ttk.Label(mainFrame, text="Verbrauch pro Woche:")
l_kwh_week.grid(column=0, row=3, sticky=W)

l_kwh_week_2 = ttk.Label(mainFrame, text="")
l_kwh_week_2.grid(column=1, row=3, sticky=W, padx=(4, 0))
# anzeige kwh pro monat
l_kwh_month = ttk.Label(mainFrame, text="Verbrauch pro Monat:")
l_kwh_month.grid(column=0, row=4, sticky=W)

l_kwh_month_2 = ttk.Label(mainFrame, text="")
l_kwh_month_2.grid(column=1, row=4, sticky=W, padx=(4, 0))
# anzeige kwh pro jahr
l_kwh_year = ttk.Label(mainFrame, text="Verbrauch pro Jahr:")
l_kwh_year.grid(column=0, row=5, sticky=W)

l_kwh_year_2 = ttk.Label(mainFrame, text="")
l_kwh_year_2.grid(column=1, row=5, sticky=W, padx=(4, 0))
# KOSTEN
# anzeige kosten pro tag
l_cost_day = ttk.Label(mainFrame, text="Kosten pro Tag:")
l_cost_day.grid(column=0, row=6, sticky=W, pady=(10, 0))

l_cost_day_2 = ttk.Label(mainFrame, text="")
l_cost_day_2.grid(column=1, row=6, sticky=NSEW, padx=(4, 0), pady=(10, 0))
# anzeige kosten pro woche
l_cost_week = ttk.Label(mainFrame, text="Kosten pro Woche:")
l_cost_week.grid(column=0, row=7, sticky=W)

l_cost_week_2 = ttk.Label(mainFrame, text="")
l_cost_week_2.grid(column=1, row=7, sticky=W, padx=(4, 0))
# anzeige kosten pro monat
l_cost_month = ttk.Label(mainFrame, text="Kosten pro Monat:")
l_cost_month.grid(column=0, row=8, sticky=W)

l_cost_month_2 = ttk.Label(mainFrame, text="")
l_cost_month_2.grid(column=1, row=8, sticky=W, padx=(4, 0))
# anzeige kosten pro jahr
l_cost_year = ttk.Label(mainFrame, text="Kosten pro Jahr:")
l_cost_year.grid(column=0, row=9, sticky=W)

l_cost_year_2 = ttk.Label(mainFrame, text="")
l_cost_year_2.grid(column=1, row=9, sticky=W, padx=(4, 0))

# rechenoperation
def calculate():
    cost = float(e_cost.get().replace(",", "."))
    watt = int(e_watt.get())
    if not int(com_hours_per_day.get()) > 24:
        hours_day = int(com_hours_per_day.get())
    days_per_week = int(com_days_per_week.get())

    # tv_items.insert(99999999, cost)
    # tv_items.grid(column=0, row=1, sticky=W, pady=(15, 0))


# knopf ausrechnen
button_calculate = ttk.Button(mainFrame, text="Berechnen", command=calculate)
button_calculate.grid(column=0, row=10, sticky=W, pady=(10, 0))

root.mainloop()
