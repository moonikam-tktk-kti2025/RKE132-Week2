""" Kirjuta programm, mis küsib kasutajalt tema perekonnanime ja sugu (vali „m“ või „n“).
Programm tervitab kasutajat vastavalt soole:
Kui kasutaja valib „m“, väljasta: „Tere, härra [Perekonnanimi]!“
Kui kasutaja valib „n“, väljasta: „Tere, proua [Perekonnanimi]!“
Kui kasutaja sisestab midagi muud, väljasta: „Tere tulemast, [Perekonnanimi]! (sugu ei olegi tähtis).“ """

#Alusta programmi.
#Küsi kasutajalt tema perekonnanime.
#Küsi kasutajalt tema sugu (m/n).
#Kui sugu on võrdne "m"-ga, siis väljasta ekraanile "Tere, härra [Perekonnanimi]!".
#Muidu kui sugu on võrdne "n"-ga, siis väljasta ekraanile "Tere, proua [Perekonnanimi]!".
#Muidu (kui sisestus ei olnud õige), siis väljasta ekraanile: "Tere tulemast, [Perekonnanimi]! (sugu ei olegi tähtis).".
#Lõpeta programm.

perekonnanimi = input('Sisesta enda perekonnanimi: ')
sugu = input('Sisesta enda sugu (m/n): ')

if sugu == 'm':
    print(f'Tere, härra {perekonnanimi}!')
elif sugu == 'n':
    print(f'Tere, proua {perekonnanimi}!')
else:
    print(f'Tere tulemast, {perekonnanimi}! (sugu ei olegi tähtis).')