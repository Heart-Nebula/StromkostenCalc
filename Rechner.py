from tkinter import *
from tkinter import ttk

# root window
root = Tk()
root.title("Stromrechner v1")
root.geometry("1280x720")
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
l_watt.grid(column=0, row=0, sticky=NSEW)

e_watt = ttk.Entry(mainFrame, name="e_watt", width=10)
e_watt.grid(column=1, row=0, sticky=NSEW, padx=(5, 0))

# eingabe betriebsstunden
l_daily_usage = ttk.Label(mainFrame, text="Betriebsstunden / Tag:")
l_daily_usage.grid(column=2, row=0, sticky=NSEW, padx=(20, 0))

e_hours_day = ttk.Entry(mainFrame, width=10)
e_hours_day.grid(column=3, row=0, sticky=NSEW, padx=(5, 0))

# eingabe betriebstage pro woche
l_days_per_week = ttk.Label(mainFrame, text="Betriebstage / Woche:")
l_days_per_week.grid(column=4, row=0, sticky=NSEW, padx=(20, 0))

days = [1, 2, 3, 4, 5, 6, 7]

com_days_per_week = ttk.Combobox(mainFrame, values=days, state="readonly", width=3)
com_days_per_week.current(0)
com_days_per_week.grid(column=5, row=0, sticky=NSEW, padx=(5, 0))

# eingabe strompreis
l_power_cost = ttk.Label(mainFrame, text="Strompreis pro kWh:")
l_power_cost.grid(column=6, row=0, sticky=NSEW, padx=(20, 0))

e_cost = ttk.Entry(mainFrame, width=10)
e_cost.grid(column=7, row=0, sticky=NSEW, padx=(5, 0))

# ANZEIGEN ------------------------------------------------------------------
# anzeige kwh pro tag
l_kwh_day = ttk.Label(mainFrame, text="Verbrauch pro Tag:")
l_kwh_day.grid(column=0, row=1, sticky=W, pady=(10, 0))

l_kwh_day_2 = ttk.Label(mainFrame, text="")
l_kwh_day_2.grid(column=1, row=1, sticky=W, padx=(4, 0), pady=(10, 0))
# anzeige kwh pro woche
l_kwh_week = ttk.Label(mainFrame, text="Verbrauch pro Woche:")
l_kwh_week.grid(column=0, row=2, sticky=W)

l_kwh_week_2 = ttk.Label(mainFrame, text="")
l_kwh_week_2.grid(column=1, row=2, sticky=W, padx=(4, 0))
# anzeige kwh pro monat
l_kwh_month = ttk.Label(mainFrame, text="Verbrauch pro Monat:")
l_kwh_month.grid(column=0, row=3, sticky=W)

l_kwh_month_2 = ttk.Label(mainFrame, text="")
l_kwh_month_2.grid(column=1, row=3, sticky=W, padx=(4, 0))
# anzeige kwh pro jahr
l_kwh_year = ttk.Label(mainFrame, text="Verbrauch pro Jahr:")
l_kwh_year.grid(column=0, row=4, sticky=W)

l_kwh_year_2 = ttk.Label(mainFrame, text="")
l_kwh_year_2.grid(column=1, row=4, sticky=W, padx=(4, 0))
# KOSTEN
# anzeige kosten pro tag
l_cost_day = ttk.Label(mainFrame, text="Kosten pro Tag:")
l_cost_day.grid(column=0, row=5, sticky=W, pady=(10, 0))

l_cost_day_2 = ttk.Label(mainFrame, text="")
l_cost_day_2.grid(column=1, row=5, sticky=NSEW, padx=(4, 0), pady=(10, 0))
# anzeige kosten pro woche
l_cost_week = ttk.Label(mainFrame, text="Kosten pro Woche:")
l_cost_week.grid(column=0, row=6, sticky=W)

l_cost_week_2 = ttk.Label(mainFrame, text="")
l_cost_week_2.grid(column=1, row=6, sticky=W, padx=(4, 0))
# anzeige kosten pro monat
l_cost_month = ttk.Label(mainFrame, text="Kosten pro Monat:")
l_cost_month.grid(column=0, row=7, sticky=W)

l_cost_month_2 = ttk.Label(mainFrame, text="")
l_cost_month_2.grid(column=1, row=7, sticky=W, padx=(4, 0))
# anzeige kosten pro jahr
l_cost_year = ttk.Label(mainFrame, text="Kosten pro Jahr:")
l_cost_year.grid(column=0, row=8, sticky=W)

l_cost_year_2 = ttk.Label(mainFrame, text="")
l_cost_year_2.grid(column=1, row=8, sticky=W, padx=(4, 0))

# rechenoperation
def calculate():
    cost = float(e_cost.get().replace(",", "."))
    watt = int(e_watt.get())
    if not int(e_hours_day.get()) > 24:
        hours_day = int(e_hours_day.get())
    days_per_week = int(com_days_per_week.get())

    try:
        l_kwh_day_2.configure(text=f"{round(watt*hours_day/1000,1)}0 kWh")
    except:
        pass

    try:
        l_kwh_week_2.configure(
            text=f"{round(watt*hours_day*days_per_week/1000,1)}0 kWh"
        )
    except:
        pass

    try:
        l_kwh_month_2.configure(
            text=f"{round(watt*hours_day*days_per_week*4.3/1000,1)}0 kWh"
        )
    except:
        pass

    try:
        l_kwh_year_2.configure(
            text=f"{round(watt*hours_day*days_per_week*52.1/1000,1)}0 kWh"
        )
    except:
        pass
    # KOSTEN
    try:
        l_cost_day_2.configure(text=f"{format(watt*hours_day/1000*cost,'.2f')} €")
    except:
        pass

    try:
        l_cost_week_2.configure(
            text=f"{format(watt*hours_day*days_per_week/1000*cost,'.2f')} €"
        )
    except:
        pass

    try:
        l_cost_month_2.configure(
            text=f"{format(watt*hours_day*days_per_week*4.3/1000*cost,'.2f')} €"
        )
    except:
        pass

    try:
        l_cost_year_2.configure(
            text=f"{format(watt*hours_day*days_per_week*52.1/1000*cost,'.2f')} €"
        )
    except:
        pass


# knopf ausrechnen
button_calculate = ttk.Button(mainFrame, text="Berechnen", command=calculate)
button_calculate.grid(column=0, row=9, sticky=W, pady=(10, 0))

root.mainloop()
