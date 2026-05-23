# Les 9 — Oervormen (Gieten)
**KU Leuven · Productietechnieken en Systemen · Prof. Sylvie Castagne**

---

## Inhoudsopgave

1. [Wat is oervormen?](#1-wat-is-oervormen)
2. [Gieten — basisprincipe](#2-gieten--basisprincipe)
3. [De gietvorm en het gietsysteem](#3-de-gietvorm-en-het-gietsysteem)
4. [Stap 1: Verwarmen en smelten](#4-stap-1-verwarmen-en-smelten)
5. [Stap 2: Vloeistromingsanalyse](#5-stap-2-vloeistromingsanalyse)
6. [Stap 3: Stolling](#6-stap-3-stolling)
7. [Krimp en opkomers](#7-krimp-en-opkomers)
8. [Case study: Turbinebladen](#8-case-study-turbinebladen)
9. [Formuleoverzicht](#9-formuleoverzicht)

---

## 1. Wat is oervormen?

Oervormen zijn productiemethodes waarbij je een voorwerp maakt **vanuit vormloos materiaal** — denk aan een vloeistof, een poeder, of een vezelmassa. Het basismateriaal heeft nog geen vaste vorm. Door afkoeling, of een chemisch of fysisch proces, gaat het over naar een vaste toestand die de gewenste vorm heeft.

Concreet: je start met iets dat geen shape heeft en je geeft het permanent een shape.

De drie grote categorieën naargelang het materiaal:
- **Metalen** → gieten (focus van deze les)
- **Keramiek** → bv. glasgieten, persen van keramische poeders
- **Polymeren en PMC's** → spuitgieten, extrusie, ...

Bij metaalgieten wordt het metaal gesmolten, in een gietvorm gegoten en laat men het stollen. Dit onderscheidt gieten van processen zoals smeden of walsen, waar het materiaal nooit volledig vloeibaar wordt maar plastisch wordt vervormd.

---

## 2. Gieten — basisprincipe

### Waarom gieten?

Gieten lost een fundamenteel productieprobleem op: complexe 3D-geometrieën die je onmogelijk of te duur zou kunnen frezen of draaien, kan je in één stap gieten. Denk aan motorblokken, turbinebehuizingen, klokken — vormen met holtes, ribben, slingerende kanalen.

Het gieten is ook een **near-net-shape** of zelfs **net-shape** proces:
- **Net shape**: het gegoten stuk heeft direct de juiste vorm en afmetingen → geen verdere bewerking nodig
- **Near net shape**: minimale nabewerking (bv. enkele passages slijpen of draaien om de eindtolerancties te halen)

Dit maakt gieten bijzonder economisch voor grote volumes en complexe onderdelen.

### Het gieten in een notendop

```
Metaal smelten
  --> vloeibaar metaal in gietvorm gieten
  --> stollen en afkoelen
  --> gietvorm verwijderen
  --> gietsysteem afsnijden
  --> inspecteren
  --> (eventueel nabewerken)
  --> eindproduct
```

### Procestappen

1. Fabricage van de gietvorm en het patroon/model
2. Het metaal verwarmen en smelten
3. Het vloeiende metaal gieten (door zwaartekracht of externe kracht)
4. Stollen en afkoelen tot kamertemperatuur
5. Inspectie

---

## 3. De gietvorm en het gietsysteem

De gietvorm is het **negatief** van het eindproduct — de holte in de vorm heeft precies de shape die je wil gieten. Een gietvorm bestaat typisch uit meerdere delen:

```
┌──────────────────────────────────────────────┐
│             Gietkom (ingang vloeistof)        │
│             Gietloop (verticaal kanaal)       │
│  Bovenkast  Aansnijding (horizontaal kanaal)  │
│──────────────── VORMDELING ───────────────────│
│  Onderkast  Vormholte (= negatief product)    │
│             Kern (voor interne holtes)         │
│             Opkomer (voedt krimp bij)         │
└──────────────────────────────────────────────┘
```

**Onderdelen van het gietsysteem:**
- **Gietkom / gietpan**: ontvangt het vloeibaar metaal uit de gietpan
- **Gietloop** (sprue): verticaal kanaal, voert het metaal naar beneden
- **Aansnijding** (runner): horizontaal kanaal dat de gietloop verbindt met de vormholte
- **Vormholte**: het eigenlijke negatief van het werkstuk
- **Opkomer** (riser): een reservoirtje met gesmolten metaal dat het gietstuk voedt wanneer het krimpt tijdens het stollen (zie sectie 7)
- **Kern**: een inzetstuk van zand of keramiek dat interne holtes definieert

**Vormdeling**: de lijn waarlangs de boven- en onderkast worden gescheiden om het gietstuk te kunnen verwijderen.

### De gietvorm is iets te groot

Het metaal krimpt tijdens het stollen en afkoelen. De holte in de gietvorm moet dus **iets groter** zijn dan het gewenste eindproduct, zodat na het krimpen de juiste afmetingen overblijven.

### Gietvormmateriaal

Gietvormmaterialen variëren van eenmalig gebruik (zand, keramiek) tot herbruikbaar (metaal):
- **Zand**: meest gebruikt, goedkoop, flexibel, eenmalig
- **Gips**: voor niet-ferrolegering bij kleine series
- **Keramiek**: voor hogere nauwkeurigheid en hoge giettemperaturen (bv. superlegering)
- **Metaal**: permanente matrijs, duurdere investering maar geschikt voor grote series

### Zandgieten — hoe werkt de vormholte?

Bij zandgieten wordt het zand rondom een **patroon** (= model van het werkstuk) verpakt. Het patroon wordt vervolgens verwijderd — de resterende holte in het zand heeft de gewenste vorm. Het patroon is iets groter dan het product (krimpcompensatie).

Het zand is vochtig en bevat een **bindmiddel** zodat het zijn vorm behoudt.

---

## 4. Stap 1: Verwarmen en smelten

### Benodigde warmte

Om metaal te smelten en voor te bereiden voor het gieten, heb je drie energiebijdragen nodig:

1. **Warmte om op te warmen tot het smeltpunt**: $C_s \cdot (T_m - T_0)$
2. **Smeltingswarmte** (latente warmte): $H_f$ — energie nodig om de kristalstructuur te breken zonder verdere temperatuurstijging
3. **Warmte om het vloeibare metaal op giettemperatuur te brengen**: $C_l \cdot (T_p - T_m)$

De volledige formule:

$$H_p = \rho V \left[ C_s(T_m - T_0) + H_f + C_l(T_p - T_m) \right]$$

| Symbool | Betekenis | Eenheid |
|---|---|---|
| $H_p$ | Totale benodigde warmte | J |
| $\rho$ | Dichtheid | g/cm³ |
| $V$ | Volume dat verwarmd wordt | cm³ |
| $C_s$ | Soortelijke warmte in vaste toestand | J/g·°C |
| $C_l$ | Soortelijke warmte in vloeibare toestand | J/g·°C |
| $T_m$ | Smelttemperatuur | °C |
| $T_0$ | Starttemperatuur | °C |
| $T_p$ | Giettemperatuur | °C |
| $H_f$ | Smeltingswarmte | J/g |

### Beperkingen van de formule

In de praktijk zijn er complicaties:
- De soortelijke warmte varieert met de temperatuur (niet constant $C_s$)
- Legeringen smelten niet bij één temperatuur maar over een **zone** tussen solidustemperatuur en liquidustemperatuur — dit maakt het lastiger dan voor zuivere metalen
- Er zijn warmteverliezen naar de omgeving tijdens het verwarmen
- Voor legeringen zijn exacte materiaaldata niet altijd beschikbaar

Commerciële simulatiesoftware (bv. MAGMASOFT, ProCAST) wordt in de praktijk gebruikt voor nauwkeurige berekeningen.

> **Belangrijk voor examen:** formule voor totale smeltingswarmte kennen en kunnen toepassen op oefeningen.

---

## 5. Stap 2: Vloeistromingsanalyse

### Waarom is de stromingsstap kritisch?

Het vloeibare metaal moet **alle delen van de holte bereiken vóór het stolt**. Maar als het te snel stroomt, treedt turbulentie op. Turbulente stroming sleurt lucht en metaaloxide mee, die als insluitingen in het gietstuk stollen en de kwaliteit aantasten. De stroom moet dus **laminair** zijn — geordend en gestroomlijnd.

### Wet van Bernoulli

De wet van Bernoulli beschrijft de energiebehoud langs een stroombaan in een ideale vloeistof (geen wrijving, atmosferische druk):

$$h_1 + \frac{v_1^2}{2g} = h_2 + \frac{v_2^2}{2g}$$

Waarbij:
- $h$ = hoogte (cm)
- $v$ = stroomsnelheid (cm/s)
- $g$ = valversnelling = 981 cm/s²

Als je punt 1 aan de **bovenkant van de gietloop** plaatst (waar $v_1 \approx 0$ en $h_1 = h_t$) en punt 2 aan de **onderkant** ($h_2 = 0$ als referentieniveau), dan volgt:

$$v_2 = \sqrt{2g h_t}$$

De snelheid onderaan de gietloop wordt dus volledig bepaald door de **hoogte** van de gietloop.

### Continuïteitswet

In een gesloten buissysteem is de volumestroom overal gelijk:

$$Q = A_1 v_1 = A_2 v_2 = \text{constant}$$

**Gevolg:** Als de snelheid onderaan de gietloop hoger is dan bovenaan (wat Bernoulli voorspelt), moet de **doorsnede kleiner worden** om de volumestroom constant te houden. Dit is waarom een **taps toelopende gietloop** (smaller naar beneden) de juiste geometrie is.

### Aspiratie

Als de gietloop een **constante doorsnede** heeft en de snelheid onderaan hoger is dan bovenaan, dan moet het continuïteitsevenwicht gecompenseerd worden door lucht of gas aan te zuigen. Die lucht komt terecht in het vloeibare metaal → gietstoringen.

**Oplossing:** taps toelopende gietloop (conisch, smaller naar beneden). Dan is de geometrie consistent met de toenemende snelheid en er is geen reden om lucht aan te zuigen.

> **Belangrijk voor examen:** de reden voor de tapse gietloop begrijpen en de formules Bernoulli + continuïteit kunnen toepassen.

### Vultijd

Als de volumestroom $Q$ door de aansnijding (punt 2) bekend is, dan is de minimale vultijd:

$$T_{MF} = \frac{V}{Q}$$

Waarbij $V$ het volume van de holte is. Dit is een minimum — in werkelijkheid is de vultijd iets langer door wrijvingsverliezen.

### Vloeibaarheid van het vloeibare metaal

Naast de geometrie van het gietsysteem speelt ook de **vloeibaarheid** van het metaal zelf een rol. Vloeibaarheid is het vermogen van het vloeibaar metaal om door de holte te stromen voor het stolt. Een hoge viscositeit = lage vloeibaarheid.

Vloeibaarheid wordt gemeten met een **spiraalvormtest** (CUP test): hoe langer de gevulde spiraal, hoe groter de vloeibaarheid.

---

## 6. Stap 3: Stolling

### Van vloeibaar naar vast

Na het gieten koelt het metaal af en stolt. Dit is een faseverandering: de atomen die vrij bewogen in de vloeistof, ordenen zich in een kristalrooster. **Nucleatie en groei** zijn de twee stappen:

1. **Nucleatie**: kristalkerntjes vormen zich op willekeurige plaatsen (homogeen) of op onzuiverheden/wanden (heterogeen — dit is veel couranter)
2. **Kristalgroei**: de kernpjes groeien uit tot korrels totdat ze op andere groeiende korrels botsen → korrelgrenzen

Het resultaat is een **polykristallijne** structuur.

### Korrelstructuur in een gietstuk

Het typische resultaat in een zandgieting toont drie zones:

1. **Gelaagde fijnkorrelige laag** (chill zone) nabij de gietvormwand: de wand koelt het metaal snel en vormt veel kleine willekeurig georiënteerde korrels
2. **Kolomvormige korrels** (columnar grains) gericht naar het midden: alleen de korrels waarvan de groeizrichting in lijn is met de warmteafvoer overleven en groeien lang uit
3. **Equiaxiaal centrumgebied**: in het midden, waar de afkoeling traag en isotropisch is, vormen zich grotere willekeurige korrels

### Zuivere metalen versus legeringen

**Zuivere metalen** stollen bij één welbepaalde temperatuur (het vriespunt). Op de koelcurve is er een **plateau** — de temperatuur daalt niet terwijl het metaal stolt, want de vrijgekomen latente warmte compenseert de afkoeling.

**Legeringen** stollen over een **temperatuurzone** tussen de liquidustemperatuur (eerst vaste kristalletjes) en de solidustemperatuur (volledig vast). Daartussen bestaat de zogenaamde **mushy zone** (pappige zone, L + S tegelijk aanwezig).

In de mushy zone groeien **dendrieten** — boomachtige kristalstructuren. Omdat de dendrieten de rijkere of armere legeringselementen uitstoten aan hun grensvlak, treedt er **segregatie** op: de samenstelling in het midden van het gietstuk verschilt van die nabij de randen. Dit is een metallurgisch kwaliteitsaandachtspunt.

### Stollingstijd: Regel van Chvorinov

**Hoe lang duurt het tot een gietstuk volledig gestold is?**

De stollingstijd hangt af van de verhouding tussen het volume en het oppervlak van het gietstuk. Een grote plak stolt trager dan een dun plaatje van hetzelfde volume, omdat de plak minder oppervlak heeft waarlangs warmte kan weggaan.

$$T_{TS} = C_m \left(\frac{V}{A}\right)^n$$

| Symbool | Betekenis |
|---|---|
| $T_{TS}$ | Totale stollingstijd |
| $C_m$ | Gietvormconstante (afhankelijk van gietvormmateriaal, metaal, giettemperatuur) |
| $V$ | Volume van het gietstuk |
| $A$ | Oppervlakte van het gietstuk |
| $n$ | Exponent, typisch **n = 2** |

**Intuïtie:** hogere $V/A$ → warmte moet een grotere weg afleggen naar het oppervlak → langzamer stollen.

**Bol vs. kubus voorbeeld:** twee stukken met hetzelfde volume maar andere vorm. Een bol heeft het kleinste oppervlak per volume van alle vormen → bol stolt het langzaamst. Een kubus heeft een hoger $A/V$ dan een bol → stolt sneller.

> **Belangrijk voor examen:** de regel van Chvorinov kunnen toepassen en de invloed van V/A op stollingstijd begrijpen.

### Gietvormconstante $C_m$

$C_m$ is geen universele constante — ze hangt af van:
- Het gietvormmateriaal (zand koelt langzamer af dan metaal)
- De thermische eigenschappen van het metaal
- De giettemperatuur (hoe heter het metaal, hoe meer warmte afgevoerd moet worden)

In de praktijk bepaal je $C_m$ experimenteel op basis van eerdere gietingen met hetzelfde materiaal en dezelfde matrijs.

---

## 7. Krimp en opkomers

### Drie fasen van krimp

Tijdens het afkoelen en stollen trekt metaal samen in drie opeenvolgende fasen:

1. **Vloeistofcontractie**: het vloeibare metaal krimpt al tijdens het afkoelen boven het smeltpunt
2. **Stollingskrimp**: tijdens het overgaan van vloeibaar naar vast krimpt het metaal verder (de vaste fase is compacter dan de vloeibare)
3. **Thermische contractie**: het vaste gietstuk krimpt verder bij verdere afkoeling tot kamertemperatuur

Als je deze krimp niet opvangt, krijg je **poriën, holtes of insunkingen** in het gietstuk — defecten die de sterkte verminderen.

### De opkomer (riser)

De opkomer is een **extra reservoir gesmolten metaal** dat in verbinding staat met de vormholte. Terwijl het gietstuk stolt en krimpt, vloeit er gesmolten metaal uit de opkomer de holte in om de krimp op te vullen.

**Ontwerpeis:** de opkomer moet **later stollen** dan het gietstuk. Als de opkomer eerst stolt, kan hij zijn taak niet vervullen.

Chvorinov geeft ons de sleutel: de opkomer moet een **grotere $V/A$ verhouding** hebben dan het gietstuk. Een cilindrische opkomer met gelijke hoogte en diameter (H = D) is een goede startgeometrie.

$$T_{TS,\text{opkomer}} > T_{TS,\text{gietstuk}}$$

$$\left(\frac{V}{A}\right)_{\text{opkomer}} > \left(\frac{V}{A}\right)_{\text{gietstuk}}$$

---

## 8. Case study: Turbinebladen

De turbinebladen in een straalmotorcompressor zijn een van de meest uitdagende gietproducten ter wereld. Ze illustreren perfect waarom **microstructuurcontrole tijdens het gieten** zo belangrijk is.

### Waarom is dit zo moeilijk?

Turbinebladen werken aan het hete einde van de motor:
- Temperaturen van 1000–1100 °C (boven de helft van het smeltpunt van veel staalsoorten)
- Continue centrifugale krachten bij hoge rotatiesnelheid
- Thermische schokken bij opstarten en afzetten

Het dominante faalmechanisme bij hoge temperaturen: **creep** — progressieve plastische vervorming van het materiaal bij constante spanning over lange tijd. Het blad zou langzaam uitrekken en uiteindelijk de motorkast raken.

Bij normale polykristallijne metalen zijn de **korrelgrenzen** de zwakste schakel bij hoge temperaturen. Inter-granulaire breuken (breuk langs de korrelgrenzen) domineren naarmate de temperatuur stijgt.

**Oplossing:** elimineer de korrelgrenzen, of plaats ze strategisch zodat ze geen gevaar vormen.

### Evolutie van turbinebladen

Er zijn drie generaties productieprocessen, elk met betere prestatires:

```
Generatie 1: Conventioneel gegoten (CC)
  → willekeurig georiënteerde korrels
  → korrelgrenzen in alle richtingen
  → gevoelig voor creep + intergranulair falen

Generatie 2: Directionally Solidified (DS)
  → kolomvormige korrels langs de centrifugaalkrachtrichting
  → geen transversale korrelgrenzen
  → sterk verbeterde creep-weerstand in de kritische richting

Generatie 3: Single Crystal (SX)
  → geen enkele korrelgrens
  → optimale creep- en corrosieweerstand
  → langste levensduur, duurste productie
```

### Conventioneel gieten (CC)

Het blad wordt gegoten via **investment casting** (lost wax / verloren was proces):
1. Waxen model van het blad
2. Waxmodel omhuld met keramische slurry (lagen van zirkoon, aluminiumoxide, silica + binders)
3. Wax uitsmolten → keramische gietvorm overblijft
4. Gesmolten superlegering gegoten in de keramische matrijs
5. Stollen bij keramische wanden → polykristallijne structuur
6. Keramiek verwijderd → ruw blad

Resultaat: willekeurig georiënteerde korrels. Redelijk prestaties, maar gevoelig voor intergranulair falen bij hoge temperatuur.

### Gerichte stolling (DS — Directionally Solidified)

Het idee: controleer de koelingsrichting zodat alle korrels in dezelfde richting groeien. Als de korrels kolomvormig zijn en gericht **langs de centrifugaalkrachtrichting** (de longitudinale as van het blad), dan zijn er geen **transversale** korrelgrenzen. Die transversale grenzen zijn precies de zwakste plekken onder centrifugale belasting.

**Productieproces:**
1. Keramische matrijs voorverwarmd met stralingsverwarming
2. Vloeistof superlegering gegoten onder vacuüm (~1550°C)
3. Matrijs rust op een **water-gekoelde koelplaat** (chill plate)
4. Direct na het gieten wordt de matrijs langzaam omlaag getrokken (gecontroleerde terugtreksnelheid)
5. Stolling start aan de koelplaat en propageert strikt van onder naar boven
6. Thermische gradiënt typisch ~4000 K/m

Resultaat: kolomvormige korrels, gericht langs de centrifugaalkrachtrichting. Geen transversale korrelgrenzen → betere creepweerstand in de kritische richting.

### Enkelvoudig kristal (SX — Single Crystal)

Gaan we nog een stap verder: geen enkele korrelgrens, het hele blad is één enkel kristal. Optimale eigenschappen maar moeilijkere productie.

**Hoe selecteer je één korrel?**

Er zijn twee methodes:

**Methode 1: Spiral grain selector (pigtail)**
- De keramische matrijs heeft onderaan een vernauwing in de vorm van een spiraal
- Meerdere korrels groeien vanuit de koelplaat omhoog
- De spiraal is zo smal dat er geometrisch slechts **één korrel** door kan gaan
- Dat ene korrel vult de rest van de matrijs → enkelvoudig kristal

**Methode 2: Seed techniek**
- Een kiem (seed) met de gewenste kristaloriëntatie wordt onderaan de matrijs geplaatst
- Als de verwerkingscondities zo zijn dat de kiem niet significant hersmelt, groeit het kristal verder in de richting van de kiem
- Volledige controle over de kristaloriëntatie

**Eigenschappen:**
- Geen korrelgrenzen → corrosie- en creepweerstand sterk verbeterd
- Marktleider voor bladen in de high-pressure turbine van moderne straalMotoren

### Defecten in single crystal bladen

Zelfs bij SX bladen kunnen er productiedefecten optreden:
- **High angle grain boundaries**: als twee korrels toch doorgroeien, vormt zich een hoge-hoek grenslaag
- **Freckel chains**: ketens van kleine equiaxiale korrels veroorzaakt door convectie-instabiliteiten in de mushy zone

### Vergelijking creep-weerstand

Bij superlegering Mar-M200 onder 206 MPa bij 982°C:
- Conventioneel gegoten: kortste levensduur
- Directioneel gestold: duidelijk langer
- Enkelvoudig kristal: veruit de beste prestaties

---

## 9. Formuleoverzicht

| Formule | Symbolen | Toepassing |
|---|---|---|
| $H_p = \rho V [C_s(T_m-T_0) + H_f + C_l(T_p-T_m)]$ | $\rho$ dichtheid, $C_s$/$C_l$ soortelijke warmte, $H_f$ smeltingswarmte | Benodigde smeltwarmte berekenen |
| $h_1 + \dfrac{v_1^2}{2g} = h_2 + \dfrac{v_2^2}{2g}$ | $h$ hoogte, $v$ snelheid, $g$ valversnelling | Wet van Bernoulli (behoud energie) |
| $v_2 = \sqrt{2g h_1}$ | $h_1$ hoogte gietloopoberste punt | Snelheid onderkant gietloop (v₁ ≈ 0) |
| $Q = A_1 v_1 = A_2 v_2$ | $Q$ volumestroom, $A$ doorsnede | Continuïteitswet |
| $T_{MF} = \dfrac{V}{Q}$ | $V$ volume holte, $Q$ volumestroom | Minimale vultijd |
| $T_{TS} = C_m \left(\dfrac{V}{A}\right)^n$ | $C_m$ gietvormconstante, $n \approx 2$ | Stollingstijd (regel van Chvorinov) |
| $(V/A)_{\text{opkomer}} > (V/A)_{\text{gietstuik}}$ | — | Ontwerpeis opkomer |

---

## Samenvatting: Oervormen in één oogopslag

| Aspect | Kern |
|---|---|
| **Wat** | Voorwerp maken vanuit vormloos materiaal (vloeistof/poeder) |
| **Gietvorm** | Negatief van het product, iets te groot voor krimpcompensatie |
| **Gietsysteem** | Gietloop + aansnijding + opkomer + kern |
| **Tapse gietloop** | Voorkomt aspiratie van lucht/gas |
| **Vloeistromingswetten** | Bernoulli + continuïteit → gietsnelheid en vultijd |
| **Stolling zuiver metaal** | Bij vaste temperatuur, plateau op koelcurve |
| **Stolling legering** | Over temperatuurzone (solidus-liquidus), dendrieten, segregatie |
| **Chvorinov** | $T_{TS} \propto (V/A)^2$ — grotere V/A = langzamer stollen |
| **Opkomer** | Compenseert krimp, moet later stollen dan gietstuk |
| **Turbinebladen** | CC → DS → SX, telkens minder korrelgrenzen → betere creepweerstand |
| **Grain selector** | Spiraalvormige geometrie laat slechts 1 korrel door → SX blade |

---

---

## Wat je echt moet kennen

- Wat oervormen is: vorm geven aan vormloos materiaal (vloeistof, poeder)
- Het verschil tussen net shape en near net shape
- De onderdelen van het gietsysteem: gietloop, aansnijding, opkomer, kern, vormdeling
- Waarom de gietvorm iets te groot gemaakt wordt (krimpcompensatie)
- De formule voor benodigde smeltwarmte: H_p = ρV[C_s(T_m−T_0) + H_f + C_l(T_p−T_m)]
- De wet van Bernoulli en de continuïteitswet toepassen op een gietsysteem
- Waarom de gietloop taps toeloopt (aspiratie vermijden)
- De minimale vultijd berekenen: T_MF = V/Q
- Het verschil in stolling tussen zuivere metalen (plateau) en legeringen (mushy zone)
- Nucleatie en kristalgroei: de drie zones in een gietstuk (chill, kolom, equiaxiaal)
- Wat segregatie is en hoe dendrieten hieraan bijdragen
- De regel van Chvorinov: T_TS = C_m(V/A)^n met n ≈ 2
- Het verschil in stollingstijd tussen een bol en een kubus met hetzelfde volume
- Waarom een opkomer later moet stollen dan het gietstuk: (V/A)_opkomer > (V/A)_gietstuk
- De drie fasen van krimp: vloeistofcontractie, stollingskrimp, thermische contractie
- De evolutie van turbinebladen: CC → DS → SX en de reden (creep, korrelgrenzen)
- Hoe de spiraalvormige grain selector werkt om een enkelvoudig kristal te selecteren
- Het verschil tussen de seed-methode en de grain selector voor SX bladen

---

*Gebaseerd op slides: "Les 9 Oervormen Deel 1" en "Les 9 Oervormen Part 2" — Prof. Sylvie Castagne, KU Leuven (AJ 25/26)*
