""" Arstid soovitavad juua päevas 2 liitrit vett.
Kirjuta programm, mis küsib kasutajalt, kui palju klaase vett ta juba joonud on. Oletame, et üks klaas = 250 ml.
Programm arvutab, mitu protsenti päevanormist on täidetud, ja annab tagasisidet:
Kui protsent < 50: väljasta: „Joo rohkem vett, keha vajab seda!“
Kui protsent < 100: väljasta: „Tubli, jätka samas vaimus!“
Kui protsent ≥ 100: väljasta: „Suurepärane, oled oma päevase eesmärgi täitnud!“ """

#Alusta programmi.
#Küsi kasutajalt, kui mitu klaasi vett ta täna on juba joonud.
#Programm arvutab, mitu % päevanormist on täidetud.
#Kui % on <50, siis väljasta ekraanile "Joo rohkem vett, keha vajab seda!".
#Muidu kui % on <100, siis väljasta ekraanile "Tubli, jätka samas vaimus!".
#Muidu kui % on >= 100, siis väljasta ekraanile: "Suurepärane, oled oma päevase eesmärgi täitnud!".
#Lõpeta programm.

DAILY_WATER_ML = 2000
GLASS_VOLUME_ML = 250

daily_glasses = DAILY_WATER_ML / GLASS_VOLUME_ML

glasses_drunk = int(input('Mitu klaasi vett oled täna joonud? (1 klaas = 250 ml) '))
percentage = (glasses_drunk / daily_glasses) * 100

if percentage < 50:
    print('Joo rohkem vett, keha vajab seda!')
elif percentage < 100:
    print('Tubli, jätka samas vaimus!')
else:
    print('Suurepärane, oled oma päevase eesmärgi täitnud!')