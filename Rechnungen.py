#Eingabevariablen
Verbrauch = input("Bitte den Verbrauch in Watt eingeben:")
Betriebsstunden = input("Bitte die Betriebsstunden eingeben:") 
Betriebstage = input("Bitte die Betriebstage eingeben:")
Strompreis = input("Bitte den Strompreis eingeben:")

#Datentypen anpassen 
Verbrauch = int(Verbrauch)
Betriebsstunden = int(Betriebsstunden)
Betriebstage = int(Betriebstage)
Strompreis = float(Strompreis)

#Ergebnisvariablen Verbrauch
VerTag = Verbrauch * Betriebsstunden / 1000
VerWoche = Verbrauch * Betriebsstunden * Betriebstage / 1000
VerMonat = Verbrauch * Betriebsstunden * Betriebstage * 4.3 / 1000
VerJahr = Verbrauch * Betriebsstunden * Betriebstage * 52.1 / 1000

#Ergebnisvariablen Kosten
KostenTag = VerTag * Strompreis
KostenWoche = VerWoche * Strompreis
KostenMonat = VerMonat * Strompreis 
KostenJahr = VerJahr * Strompreis

#Ausgabe
print("Ergebnisse")
print("Verbrauch")
print("Verbrauch / Tag: " + str(VerTag) + " kWh")
print("Verbrauch / Woche: " + str(VerWoche) + " kWh")
print("Verbrauch / Monat: " + str(VerMonat) + " kWh")
print("Verbrauch / Jahr: " + str(VerJahr) + " kWh")

print("Kosten")
print("Kosten pro Tag: " + str(KostenTag) + (" €"))
print("Kosten pro Woche: " + str(KostenWoche) + (" €"))
print("Kosten pro Monat: " + str(KostenMonat) + (" €"))
print("Kosten pro Jahr: " + str(KostenJahr) + (" €"))