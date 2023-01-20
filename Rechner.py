from tkinter import *
from tkinter import ttk

# root window
root = Tk()
root.title("Stromrechner v1")
root.geometry("1000x600")
root.resizable(width=False, height=False)
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")

# main parent frame
mainFrame = ttk.Frame(root)
mainFrame.grid(padx=(10, 0), pady=(10, 0))

# EINGABEN ------------------------------------------------------------------
# eingabe name
l_name = ttk.Label(mainFrame, name="l_name", text="Name:")
l_name.grid(column=0, row=0, sticky=W)

e_name = ttk.Entry(mainFrame, name="e_name", width=10)
e_name.grid(column=0, row=0, sticky=E)

# eingabe wattverbrauch
l_watt = ttk.Label(mainFrame, name="l_watt", text="Verbrauch in Watt:")
l_watt.grid(column=1, row=0, sticky=W, padx=(5, 0))

e_watt = ttk.Entry(mainFrame, name="e_watt", width=10)
e_watt.grid(column=2, row=0, sticky=W)

# eingabe betriebsstunden am tag
l_daily_usage = ttk.Label(mainFrame, text="Betriebsstunden / Tag:")
l_daily_usage.grid(column=3, row=0, sticky=W)

com_hours_per_day = ttk.Combobox(
    mainFrame, values=list(range(1, 25)), state="readonly", width=3
)
com_hours_per_day.current(0)
com_hours_per_day.grid(column=4, row=0, sticky=W)

# eingabe betriebstage pro woche
l_days_per_week = ttk.Label(mainFrame, text="Betriebstage / Woche:")
l_days_per_week.grid(column=5, row=0, sticky=W, padx=(5, 0))

com_days_per_week = ttk.Combobox(
    mainFrame, values=list(range(1, 8)), state="readonly", width=3
)
com_days_per_week.current(0)
com_days_per_week.grid(column=6, row=0, sticky=W, padx=(5, 0))

# eingabe strompreis
l_power_cost = ttk.Label(mainFrame, text="Strompreis pro kWh:")
l_power_cost.grid(column=7, row=0, sticky=W, padx=(5, 0))

e_cost = ttk.Entry(mainFrame, width=10)
e_cost.grid(column=8, row=0, sticky=W, padx=(5, 0))

# funktion gerät zur treeview hinzufügen
def add_device():
    name = e_name.get()
    cost = float(e_cost.get().replace(",", "."))
    watt = int(e_watt.get())
    if not int(com_hours_per_day.get()) > 24:
        hours_day = int(com_hours_per_day.get())
    days_per_week = int(com_days_per_week.get())

    tv_items.insert("", "end", values=(name, watt, hours_day, days_per_week, cost))


# knop zum hinzufügen eines gerätes zur treeview
b_add_device = ttk.Button(mainFrame, text="Gerät hinzufügen", command=add_device)
b_add_device.grid(row=1, column=7, columnspan=2, sticky=NE, pady=(10, 0))

# ANZEIGEN ------------------------------------------------------------------
# scrollbar für die treeview mit den geräten
s_items = ttk.Scrollbar(mainFrame)
s_items.grid(column=4, row=1, sticky=["N", "S", "W"], pady=(15, 0))

# treeview, die die geräte anzeigt
tv_items = ttk.Treeview(
    mainFrame,
    columns=[
        "Name",
        "Watt consumption",
        "Hours / day",
        "Days / week",
        "Electricity cost",
    ],
    selectmode=BROWSE,
    yscrollcommand=s_items.set,
    show="headings",
)
tv_items.column("0", anchor=CENTER, stretch=False, width=80)
tv_items.column("1", anchor=CENTER, stretch=False, width=100)
tv_items.column("2", anchor=CENTER, stretch=False, width=100)
tv_items.column("3", anchor=CENTER, stretch=False, width=100)
tv_items.column("4", anchor=CENTER, width=100)
tv_items.heading("0", text="Name", anchor=CENTER)
tv_items.heading("1", text="Wattverbrauch", anchor=CENTER)
tv_items.heading("2", text="Betriebsstunden", anchor=CENTER)
tv_items.heading("3", text="Tage / Woche", anchor=CENTER)
tv_items.heading("4", text="Stromkosten", anchor=CENTER)
tv_items.grid(column=0, row=1, columnspan=4, pady=(15, 0), sticky=W)

# scrollbar mit der treeview verknüpfen
s_items.configure(command=tv_items.yview)

# anzeige kwh pro tag
l_kwh_day = ttk.Label(mainFrame, text="Verbrauch pro Tag:")
l_kwh_day.grid(column=0, row=2, sticky=W, pady=(10, 0))

l_kwh_day_2 = ttk.Label(mainFrame, text="0 kWh")
l_kwh_day_2.grid(column=1, row=2, sticky=W, padx=(4, 0), pady=(10, 0))

# anzeige kwh pro woche
l_kwh_week = ttk.Label(mainFrame, text="Verbrauch pro Woche:")
l_kwh_week.grid(column=0, row=3, sticky=W)

l_kwh_week_2 = ttk.Label(mainFrame, text="0 kWh")
l_kwh_week_2.grid(column=1, row=3, sticky=W, padx=(4, 0))

# anzeige kwh pro monat
l_kwh_month = ttk.Label(mainFrame, text="Verbrauch pro Monat:")
l_kwh_month.grid(column=0, row=4, sticky=W)

l_kwh_month_2 = ttk.Label(mainFrame, text="0 kWh")
l_kwh_month_2.grid(column=1, row=4, sticky=W, padx=(4, 0))

# anzeige kwh pro jahr
l_kwh_year = ttk.Label(mainFrame, text="Verbrauch pro Jahr:")
l_kwh_year.grid(column=0, row=5, sticky=W)

l_kwh_year_2 = ttk.Label(mainFrame, text="0 kWh")
l_kwh_year_2.grid(column=1, row=5, sticky=W, padx=(4, 0))

# KOSTEN ------------------------------------------------------------------
# anzeige kosten pro tag
l_cost_day = ttk.Label(mainFrame, text="Kosten pro Tag:")
l_cost_day.grid(column=0, row=6, sticky=W, pady=(10, 0))

l_cost_day_2 = ttk.Label(mainFrame, text="0 €")
l_cost_day_2.grid(column=1, row=6, sticky=NSEW, padx=(4, 0), pady=(10, 0))

# anzeige kosten pro woche
l_cost_week = ttk.Label(mainFrame, text="Kosten pro Woche:")
l_cost_week.grid(column=0, row=7, sticky=W)

l_cost_week_2 = ttk.Label(mainFrame, text="0 €")
l_cost_week_2.grid(column=1, row=7, sticky=W, padx=(4, 0))

# anzeige kosten pro monat
l_cost_month = ttk.Label(mainFrame, text="Kosten pro Monat:")
l_cost_month.grid(column=0, row=8, sticky=W)

l_cost_month_2 = ttk.Label(mainFrame, text="0 €")
l_cost_month_2.grid(column=1, row=8, sticky=W, padx=(4, 0))

# anzeige kosten pro jahr
l_cost_year = ttk.Label(mainFrame, text="Kosten pro Jahr:")
l_cost_year.grid(column=0, row=9, sticky=W)

l_cost_year_2 = ttk.Label(mainFrame, text="0 €")
l_cost_year_2.grid(column=1, row=9, sticky=W, padx=(4, 0))

# KNÖPFE

# funktion werte ausrechnen
def calculate():
    daily_usage = 0
    weekly_usage = 0
    monthly_usage = 0
    yearly_usage = 0

    daily_cost = 0
    weekly_cost = 0
    monthly_cost = 0
    yearly_cost = 0

    for item in tv_items.get_children():
        consumption = tv_items.item(item)["values"][1]
        device_hours = tv_items.item(item)["values"][2]
        device_days = tv_items.item(item)["values"][3]
        electricity_cost = tv_items.item(item)["values"][4]

        daily_usage += consumption * device_hours / 1000
        weekly_usage += consumption * device_hours * device_days / 1000
        monthly_usage += consumption * device_hours * device_days * 4.3 / 1000
        yearly_usage += consumption * device_hours * device_days * 52.1 / 1000

        daily_cost = daily_usage * float(electricity_cost)
        weekly_cost = weekly_usage * float(electricity_cost)
        monthly_cost = monthly_usage * float(electricity_cost)
        yearly_cost = yearly_usage * float(electricity_cost)

    l_kwh_day_2.configure(text=str(round(daily_usage, 2))+" kWh")
    l_kwh_week_2.configure(text=str(round(weekly_usage, 2))+" kWh")
    l_kwh_month_2.configure(text=str(round(monthly_usage, 2))+" kWh")
    l_kwh_year_2.configure(text=str(round(yearly_usage, 2))+" kWh")

    l_cost_day_2.configure(text=str(round(daily_cost, 2))+" €")
    l_cost_week_2.configure(text=str(round(weekly_cost, 2))+" €")
    l_cost_month_2.configure(text=str(round(monthly_cost, 2))+" €")
    l_cost_year_2.configure(text=str(round(yearly_cost, 2))+" €")


# berechnen knopf
b_calculate = ttk.Button(mainFrame, text="Berechnen", command=calculate)
b_calculate.grid(column=0, row=10, sticky=W, pady=(10, 0))

# funktion geräte aus der liste löschen
def delete():
    selected_item = tv_items.selection()
    if selected_item:
        tv_items.delete(selected_item)


# löschen knopf
button_remove = ttk.Button(mainFrame, text="Löschen", command=delete)
button_remove.grid(column=5, row=1, sticky=NW, pady=(15, 0))

root.mainloop()
