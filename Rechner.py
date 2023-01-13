from tkinter import *
from tkinter import ttk

# root window
root = Tk()
root.title("Stromrechner v1")
root.geometry("1280x720")
root.resizable(width=False, height=False)

# main parent frame
mainFrame = Frame(root)
mainFrame.grid(padx=(10, 0), pady=(10, 0))

# EINGABEN ------------------------------------------------------------------
# eingabe wattverbrauch
label_watt = Label(mainFrame, text="Verbrauch in Watt:")
label_watt.grid(column=0, row=0, sticky=NW)

entry_watt = Entry(mainFrame)
entry_watt.grid(column=1, row=0, sticky=NW, padx=(5, 0))

# eingabe betriebsstunden
label_betriebsstunden = Label(mainFrame, text="Betriebsstunden / Tag:")
label_betriebsstunden.grid(column=2, row=0, sticky=NW, padx=(20, 0))

entry_betriebsstunden = Entry(mainFrame)
entry_betriebsstunden.grid(column=3, row=0, sticky=NW, padx=(5, 0))

# eingabe betriebstage pro woche
label_betriebstage_week = Label(mainFrame, text="Betriebstage / Woche:")
label_betriebstage_week.grid(column=4, row=0, sticky=NW, padx=(20, 0))

number_of_days = [1, 2, 3, 4, 5, 6, 7]

combobox_betriebstage_week_2 = ttk.Combobox(
    mainFrame, values=number_of_days, state="readonly"
)
combobox_betriebstage_week_2.current(0)
combobox_betriebstage_week_2.grid(column=5, row=0, sticky=NW, padx=(5, 0))

# eingabe strompreis
label_strompreis = Label(mainFrame, text="Strompreis pro kWh:")
label_strompreis.grid(column=6, row=0, sticky=NW, padx=(20, 0))

entry_strompreis = Entry(mainFrame)
entry_strompreis.grid(column=7, row=0, sticky=NW, padx=(5, 0))

# ANZEIGEN ------------------------------------------------------------------
# anzeige kwh pro tag
label_kwh_day = Label(mainFrame, text="Verbrauch pro Tag:")
label_kwh_day.grid(column=0, row=1, sticky=W, pady=(10, 0))

label_kwh_day_2 = Label(mainFrame, text="")
label_kwh_day_2.grid(column=1, row=1, sticky=W, padx=(4, 0))
# anzeige kwh pro woche
label_kwh_week = Label(mainFrame, text="Verbrauch pro Woche:")
label_kwh_week.grid(column=0, row=2, sticky=W)

label_kwh_week_2 = Label(mainFrame, text="")
label_kwh_week_2.grid(column=1, row=2, sticky=W, padx=(4, 0))
# anzeige kwh pro monat
label_kwh_month = Label(mainFrame, text="Verbrauch pro Monat:")
label_kwh_month.grid(column=0, row=3, sticky=W)

label_kwh_month_2 = Label(mainFrame, text="")
label_kwh_month_2.grid(column=1, row=3, sticky=W, padx=(4, 0))
# anzeige kwh pro jahr
label_kwh_year = Label(mainFrame, text="Verbrauch pro Jahr:")
label_kwh_year.grid(column=0, row=4, sticky=W)

label_kwh_year_2 = Label(mainFrame, text="")
label_kwh_year_2.grid(column=1, row=4, sticky=W, padx=(4, 0))
# KOSTEN
# anzeige kosten pro tag
label_kosten_day = Label(mainFrame, text="Kosten pro Tag:")
label_kosten_day.grid(column=0, row=5, sticky=W, pady=(10, 0))

label_kosten_day_2 = Label(mainFrame, text="")
label_kosten_day_2.grid(column=1, row=5, sticky=W, padx=(4, 0))
# anzeige kosten pro woche
label_kosten_week = Label(mainFrame, text="Kosten pro Woche:")
label_kosten_week.grid(column=0, row=6, sticky=W)

label_kosten_week_2 = Label(mainFrame, text="")
label_kosten_week_2.grid(column=1, row=6, sticky=W, padx=(4, 0))
# anzeige kosten pro monat
label_kosten_month = Label(mainFrame, text="Kosten pro Monat:")
label_kosten_month.grid(column=0, row=7, sticky=W)

label_kosten_month_2 = Label(mainFrame, text="")
label_kosten_month_2.grid(column=1, row=7, sticky=W, padx=(4, 0))
# anzeige kosten pro jahr
label_kosten_year = Label(mainFrame, text="Kosten pro Jahr:")
label_kosten_year.grid(column=0, row=8, sticky=W)

label_kosten_year_2 = Label(mainFrame, text="")
label_kosten_year_2.grid(column=1, row=8, sticky=W, padx=(4, 0))

# rechenoperation
def calculate():
    try:
        label_kwh_day_2.configure(
            text=f"{int(entry_watt.get())*int(entry_betriebsstunden.get())/1000} kWh"
        )
    except:
        pass

    try:
        label_kwh_week_2.configure(
            text=f"{int(entry_watt.get())*int(entry_betriebsstunden.get())*int(combobox_betriebstage_week_2.get())/1000} kWh"
        )
    except:
        pass

    try:
        label_kwh_month_2.configure(
            text=f"{int(entry_watt.get())*int(entry_betriebsstunden.get())*int(combobox_betriebstage_week_2.get())*4.3/1000} kWh"
        )
    except:
        pass

    try:
        label_kwh_year_2.configure(
            text=f"{int(entry_watt.get())*int(entry_betriebsstunden.get())*int(combobox_betriebstage_week_2.get())*52.1/1000} kWh"
        )
    except:
        pass
    # KOSTEN
    try:
        label_kosten_day_2.configure(
            text=f"{int(entry_watt.get())*int(entry_betriebsstunden.get())/1000*float(entry_strompreis.get())} €"
        )
    except:
        pass

    try:
        label_kosten_week_2.configure(
            text=f"{int(entry_watt.get())*int(entry_betriebsstunden.get())*int(combobox_betriebstage_week_2.get())/1000*float(entry_strompreis.get())} €"
        )
    except:
        pass

    try:
        label_kosten_month_2.configure(
            text=f"{int(entry_watt.get())*int(entry_betriebsstunden.get())*int(combobox_betriebstage_week_2.get())*4.3/1000*float(entry_strompreis.get())} €"
        )
    except:
        pass

    try:
        label_kosten_year_2.configure(
            text=f"{int(entry_watt.get())*int(entry_betriebsstunden.get())*int(combobox_betriebstage_week_2.get())*52.1/1000*float(entry_strompreis.get())} €"
        )
    except:
        pass


# knopf ausrechnen
button_calculate = Button(mainFrame, text="Berechnen", command=calculate)
button_calculate.grid(column=0, row=9, sticky=W, pady=(5, 0))

root.mainloop()
