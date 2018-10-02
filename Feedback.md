# Prosjekt 1: Godkjent

Totalvurdering
==============
Hei. Dette er et meget bra prosjekt. Du har fått til alle oppgavene, skrevet stort sett ryddig kode med gode løsninger som også er dekket godt av docstrings. Det ser også ut som du har brukt git godt, men inkrementale commits. Under skriver jeg et par punkter som kunne vært enda bedre, men dette er stort sett pirk. Det viktigste er at kodestilen din er litt inkonsekvent, som gjør at den ser litt mer rotete ut enn den egentlig er.

Kommentar ang Animasjon
=======================
Leit at det ikke ordnet seg med animasjonen, det må ha vært frustrende. Derimot gjør det ingenting med tanke på prosjektet. Animasjon/plotting er ikke del av pensum i kurset, og oppgaven var bare inkludert så dere kunne lage noe "kult" for deres egen del. Her antar jeg det ikke er problemer med matplotlib direkte, men programvaren matplotlib bruker for å lage selve animasjonen, f.eks. ffmpeg. Uansett ser jeg jo animasjonen når jeg kjører double_pendulum.py :)

Forbedringspotensialer
======================
- I call-metodene tar vi inn en tuppel av statsene til løsningen, som du har kallt `y`. Du bruker så `u[0]`, `u[1]` osv når dere skriver ut uttrykkene. Det er ikke noe galt i å gjøre det slik, men jeg ville foretrukket om dere først pakket ut statsene til navngitte variabler og så brukt de. F.eks i Pendulum.__call__ kunne du endret til:
```Python
g = self.g
L = self.L
theta, omega = y
deriv_omega = -(g/L)*np.sin(theta)
deriv_theta = omega
```
Dette gjør kodene mer lik matematikken, og det blir lettere for andre å lese koden, samt å feilsøke den. Dette er spesielt relevant i double_pendulum.py uttrykket som blir så voldomst.

- - Linje 23/24 i double_pendulum.py, som er selve det matematiske uttrykket, er altfor lange. Husk at PEP8 sier at man bør bruke linjelengde på 80 karakterer. Denne kan til nød økes til 120 om det er ekstremt ønske for lengre linjer, men disse linjene er mye lengre enn det og. Her bør du dele over flere linjer for å forbedre lesbarhet. Dette kan gjøres på flere måter, men nøkkelen er å bruke linjeskift mellom de ulike leddene.`Her er slik det er skrevet i løsningsforslaget:
```Python
domega1_dt = (M2*L1*omega1*omega1*np.sin(delta)*np.cos(delta)
              + M2*G*np.sin(theta2)*np.cos(delta)
              + M2*L2*omega2**2*np.sin(delta)
              - (M1+M2)*G*np.sin(theta1))
domega1_dt /= (M1+M2)*L1 - M2*L1*np.cos(delta)**2

domega2_dt = (-M2*L2*omega2**2*np.sin(delta)*np.cos(delta)
              + (M1+M2)*G*np.sin(theta1)*np.cos(delta)
              - (M1+M2)*L1*omega1**2*np.sin(delta)
              - (M1+M2)*G*np.sin(theta2))
domega2_dt /= (M1+M2)*L2 - M2*L2*np.cos(delta)**2
```

- Når du bruker `solve_ivp` i `solve` metoden skriver du:
```Python
solve_ivp(self.__call__, ...)
```
Men merk at `__call__` er en spesiell metode som gjør `self` til et callable objekt, det holder altså her å sende inn self:
```Python
solve_ivp(self, ...)
```
Det er helt tilsvarende det du gjør, men er en mer Pythonsk måte å gjøre det på.


Kommentarer på stil
===================
- Pass på bruk av whitespace rundt likhetstegn (=), det er et par steder dette blir litt feil:
```Python
thet, omeg =pen(0.0, [0.0, 0.0])
# burde vært
thet, omeg = pen(0.0, [0.0, 0.0])
```
```Python
pen.solve([0.0, 0.0], T, dt, angles = "deg")
#burde vært
pen.solve([0.0, 0.0], T, dt, angles="deg")
```
Veldig pirkete å trekke frem slikt, men det står litt ut i en kode som ellers er forholdsvis ryddig!

- Pass på å bruke små bokstover fra instanser sånn som her:
```
ED = ExponentialDecay(a)
```
Kall den heller `ed`, eller noe mer beskrivende, som `model`, `decay`, `solver`, etc.




