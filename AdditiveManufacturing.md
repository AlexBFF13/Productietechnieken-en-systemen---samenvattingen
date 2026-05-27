# Les 15 — Additive Manufacturing (3D printen)
**KU Leuven · Productietechnieken en Systemen · Prof. Brecht Van Hooreweder**

---

## Inhoudsopgave

1. [Inleiding: wat is Additive Manufacturing?](#1-inleiding-wat-is-additive-manufacturing)
2. [Het AM-workflow: van CAD tot eindproduct](#2-het-am-workflow-van-cad-tot-eindproduct)
3. [Classificatie van AM-processen](#3-classificatie-van-am-processen)
4. [Voordelen en nadelen van AM](#4-voordelen-en-nadelen-van-am)
5. [AM voor polymeren](#5-am-voor-polymeren)
6. [AM voor metalen](#6-am-voor-metalen)
7. [SLM: procesparameters en specifieke uitdagingen](#7-slm-procesparameters-en-specifieke-uitdagingen)
8. [Lattice structures](#8-lattice-structures)

---

## 1. Inleiding: wat is Additive Manufacturing?

### Definitie en naamgeving

Additive Manufacturing (AM) heeft veel namen: 3D printing, rapid prototyping, rapid manufacturing, freeform fabrication. De academische term is **Additive Manufacturing**.

Definitie (Wohlers):

> *Process of joining materials to make objects from 3D model data, usually layer upon layer.*

Het kernidee is simpel: bij conventioneel frezen of draaien wordt materiaal **weggenomen** van een blok. Bij AM wordt materiaal **laag per laag toegevoegd** — je bouwt het onderdeel op vanuit niets, precies zoals een printer tekst op papier zet maar dan in 3D.

```
Conventioneel:  blok materiaal --> weghalen tot de gewenste vorm
Additief:       niets --> laag voor laag opbouwen tot de gewenste vorm
```

### Korte geschiedenis

De moderne AM-era begon in 1986 toen Chuck Hull en Raymond Freed **3D Systems** oprichtten. In 1987 verscheen de **SLA-1**, het eerste commercieel beschikbare AM-systeem ter wereld. KU Leuven startte zijn eigen AM-onderzoek in 1990 met stereolithografie (SLA) en begon rond 2000 met metalen (EBM, SLS/SLM).

---

## 2. Het AM-workflow: van CAD tot eindproduct

Elk AM-proces doorloopt dezelfde logische keten, ongeacht de technologie:

```
CAD-ontwerp (3D solid model)
--> CAPP: oriëntatie bepalen, supportstructuren ontwerpen, converteren naar STL
--> CAM: slicen (lagen berekenen), scanpatroon genereren
--> NC: het eigenlijke printproces (laag per laag bouwen)
--> Post-processing: uitharden, supports verwijderen, reinigen, nabewerken
--> Eindonderdeel
```

### Stap 1: STL-bestand

Het CAD-model wordt omgezet naar een **STL-bestand** (Standard Tessellation Language). Dit formaat beschrijft het oppervlak van het model als een netwerk van driehoekjes met hun normaalvectoren. Hoe meer driehoekjes, hoe nauwkeuriger de benadering van gekromde oppervlakken — maar ook hoe groter het bestand.

### Stap 2: Slicen

De software snijdt het STL-model in **horizontale lagen** met een vaste laagdikte (typisch 20–200 µm voor metalen, iets meer voor polymeren). Voor elke laag wordt een scanpatroon berekend dat de laser of nozzle moet volgen. Dit is het NC-programma voor het printproces.

### Stap 3: Bouwen

De machine bouwt het onderdeel laag per laag op. De details hangen af van de technologie (zie secties 5 en 6).

### Stap 4: Post-processing

Na het printen zijn er vrijwel altijd nabewerkingsstappen:
- **Supports verwijderen** — structuren die tijdens het printen overhangende zones ondersteunden
- **Baseplate verwijderen** — het onderdeel zagen of vonken los van de bouwplaat
- **Thermische nabehandeling** — spanningsarm gloeien, HIP (hot isostatic pressing)
- **Oppervlaktebewerking** — gritblasting, polijsten, frezen voor nauwkeurige vlakken

> **Belangrijk voor examen:** De volledige AM-procesketen kennen: STL → slicen → bouwen → post-processing. Begrijpen waarom elke stap nodig is.

---

## 3. Classificatie van AM-processen

AM-processen worden geclassificeerd op basis van de **begintoestand van het materiaal**: vloeibaar (liquid), poeder (powder), vast (solid) of gas.

| Startfase | Proces | Principe | Faseovergang | Materialen |
|---|---|---|---|---|
| **Liquid** | **Stereolithography (SLA)** | Vloeibare hars belicht door UV-laser | Fotopolymerisatie | Acrylaten, epoxyharsen |
| **Liquid** | Inkjet Printing | Druppels gesmolten materiaal via nozzle | Stollen bij koeling | Polymeren, was |
| **Liquid** | **FDM / FFF** | Gesmolten filament via nozzle geëxtrudeerd | Stollen bij koeling | Polymeren, was |
| **Powder** | 3D Printing (binder jetting) | Binder op poederbed gespoten | Geen faseovergang poeder | Keramiek, metalen, polymeren |
| **Powder** | **SLS / SLM** | Laserstraal op poederbed | Sinteren/smelten + stollen | Polymeren, metalen, keramiek |
| **Powder** | **EBM** | Elektronenbundel op poederbed | Smelten + stollen | Non-ferro metalen (Ti, CoCr) |
| **Powder** | **Laser Cladding (LC)** | Poeder via nozzle in laserfocus gespoten | Smelten + stollen | Metalen, composieten |
| **Solid** | Laminated Object Manufacturing | Vellen worden gesneden en gebonden | Binden via fase-overgang | Papier, polymeer, metaal |
| **Gas** | Selective Laser CVD | Gas condenseert in laserfocus | Chemische reactie | Metalen, keramiek |

De meest gebruikte processen in de industrie zijn **SLA, FDM, SLS** (voor polymeren) en **SLM, EBM, Laser Cladding** (voor metalen).

---

## 4. Voordelen en nadelen van AM

### Voordelen

AM lost een fundamenteel designprobleem op: bij conventionele bewerking is de **geometrische complexiteit** van een onderdeel direct gekoppeld aan de productiekosten. Bij AM niet — een complex onderdeel kost niet meer dan een eenvoudig onderdeel van dezelfde grootte.

- **Hoge designvrijheid** — interne koelkanalen, complexe structuren, organische vormen zijn mogelijk
- **Licht gewicht** — door topologie-optimalisatie en lattice structures (skeletstructuren) kan materiaal worden weggelaten zonder stijfheid te verliezen
- **Weinig materiaalverspilling** — ongebruikt poeder kan (gedeeltelijk) worden hergebruikt; geen chips zoals bij frezen
- **Direct produceren** zonder matrijs of gereedschap — ideaal voor prototypes en kleine series
- **Personalisatie** — elk onderdeel kan anders zijn zonder extra kosten (tandheelkundige implantaten, gehoorapparaten)
- **Functie-integratie** — meerdere onderdelen samenvoegen tot één geprint stuk

Een concreet voorbeeld: een vliegtuigdeurscharnnier in SLM Ti6Al4V geeft **65% gewichtsbesparing** ten opzichte van het conventionele ontwerp. Een ruimtevaartbracket in SLM-AlSi10Mg geeft 35% gewichtsbesparing, 40% stijver design, en reduceert 34 onderdelen (4 stukken + 30 klinknagels) naar 1 geprint onderdeel.

### Nadelen

> **Belangrijk voor examen:** AM vervangt conventionele processen NIET — het is complementair voor specifieke gevallen.

- **Niet altijd robuust** — processen zijn gevoelig, kwaliteitscontrole is uitdagend
- **Lage oppervlakruwheid** — oppervlakken zijn ruwer dan bij frezen of slijpen; nabewerking is bijna altijd nodig
- **Traag en duur** — productietijd en kostprijs per onderdeel zijn hoog bij grote series
- **Design for manufacturing is complex** — overhangende vlakken vereisen supportstructuren; oriëntatie heeft grote invloed
- **Veiligheid** — lasers, fijn metaalpoeder (explosief!), chemische harsen
- **3D printing hype** — AM wordt vaak overschat; voor massaproductie is het economisch niet te rechtvaardigen

**Wanneer wél AM kiezen:**
- Kleine tot middelgrote series
- Personalisatie (biomedische implantaten, prothesen)
- Geïntegreerde functionaliteit (koelkanalen in matrijs)
- Lichtgewichtstructuren (lucht- en ruimtevaart)
- Complexe designs onmogelijk door andere processen

---

## 5. AM voor polymeren

### SLA — Stereolithography

**Principe:** Een vat vloeibare fotopolymeer (UV-gevoelige hars) wordt laag per laag uitgehard door een gefocuste UV-laser. De laser scant het oppervlak van de vloeistof en polymeriseert de hars op de belichte plaatsen. Na elke laag zakt het platform een laagdikte naar beneden, een nieuwe laag vloeistof wordt aangebracht, en het proces herhaalt zich.

Er zijn twee varianten:
- **Point-by-point scanning** — laser beweegt punt per punt over het oppervlak
- **Layer-by-layer illumination** — een masker projecteert de hele laag tegelijk

SLA was de **eerste commerciële AM-technologie** (3D Systems, 1987) en blijft de marktleider voor polymeren wat betreft nauwkeurigheid en oppervlakkwaliteit. Een Ford Mondeo dashboard van Materialise (2200×840×640 mm) werd gebouwd in 2700 lagen in 52 uur.

- Materialen: acrylaten, epoxyharsen, gevulde harsen
- Nauwkeurigheid: zeer goed
- Oppervlak: zeer goed
- Zwakte: post-processing (hars reinigen), kleverige vloeistoffen, supports nodig

### FDM — Fused Deposition Modeling (ook: FFF)

**Principe:** Een plastic filament van een spoel wordt door een verwarmde nozzle geperst en gesmolten. De nozzle beweegt over het XY-vlak en deponeert het gesmolten materiaal precies waar het nodig is. Het materiaal stolt onmiddellijk bij koeling. Na elke laag stijgt de nozzle of daalt het bouwplatform een laagdikte.

FDM is de meest bekende vorm van 3D printen voor de consumentenmarkt (desktop printers). Industrieel wordt het gebruikt voor functionele prototypes.

- Materialen: ABS, PLA, PEEK, gevulde polymeren, was
- Nauwkeurigheid: matig (fair)
- Oppervlak: matig (zichtbare lagen)
- Voordeel: goedkoop, desktop-formaat, breed materiaalspectrum
- Zwakte: traag, laag oppervlak

### SLS — Selective Laser Sintering

**Principe:** Een dunne laag poeder wordt uitgespreid op het bouwplatform. Een Nd:YAG-laser (of electronenbundel bij EBM) scant het poeder en sinterert of smelt de korrels samen op de gewenste plaatsen. Het ongesmolten poeder rondom het onderdeel fungeert als **support** — er zijn geen aparte supportstructuren nodig. Dit is een groot voordeel ten opzichte van SLA en FDM.

**Part nesting:** omdat het losse poeder als support werkt, kunnen bij SLS meerdere onderdelen in 3D worden "gestapeld" in de bouwtank (nesting). Dit verhoogt de machine-efficiëntie enorm.

Polymeren voor SLS:
- **Amorfe polymeren** (bijv. polycarbonaat PC)
- **Semi-kristallijne polymeren** (bijv. nylon PA) — meest gebruikt, beste eigenschappen
- **Elastomeren** — flexibele onderdelen
- **Versterkte of gevulde polymeren** (glasvezel, koolstofvezel)

| Eigenschap | Polycarbonaat | Fine Nylon | Glass-filled Nylon | Elastomeer |
|---|---|---|---|---|
| E-modulus (MPa) | 1200 | 1400–1800 | 2800–4400 | 20 |
| Treksterkte (MPa) | 23 | 36–44 | 49–42 | — |
| Brekelongatie (%) | 5 | 6–22 | 1,8 | 111 |
| Oppervlakruwheid Ra (µm) | 7 | 12–8,5 | 15 | — |

### Vergelijking van de drie polymeerprocessen

| | SLA | SLS | FDM |
|---|---|---|---|
| Max. deelgrootte | 30×30×50 cm | 34×34×60 cm | 30×30×50 cm |
| Snelheid | Gemiddeld | Gemiddeld–goed | Slecht |
| Nauwkeurigheid | Zeer goed | Goed | Matig |
| Oppervlak | Zeer goed | Matig | Matig |
| Sterkte | Marktleider, groot formaat, brede producten | Marktleider, nauwkeurigheid, materialen, groot formaat | Desktop, goedkoop, materialen |
| Zwakte | Post-processing, kleverige vloeistoffen | Grootte, gewicht systeem, oppervlak | Snelheid |

> **Belangrijk voor examen:** Weten welke technologie het beste past bij een gegeven toepassing. SLA = hoogste kwaliteit oppervlak, SLS = geen supports nodig + part nesting, FDM = goedkoop en eenvoudig.

---

## 6. AM voor metalen

### Overzicht van de metaalprocessen

Er zijn vier hoofdprocessen voor AM van metalen:

| Proces | Energiebron | Materiaaltoevoer | Principe |
|---|---|---|---|
| **EBM** | Elektronenbundel | Poederbed | Laag poeder smelten met EB in vacuüm |
| **SLS** | Laser | Poederbed | Laag poeder sinteren met laser |
| **SLM** | Laser | Poederbed | Laag poeder volledig smelten met laser |
| **Laser Cladding (LC)** | Laser | Poeder via nozzle | Poeder inspuiten in laservlek |

### Electron Beam Melting (EBM)

**Principe:** Een wolframfilament wordt verhit tot extreem hoge temperaturen en geeft elektronen vrij. Een elektrisch veld versnelt die elektronen, elektromagnetische spoelen focusseren en sturen de bundel. De elektronenbundel smelt laag per laag het metaalpoeder in een **vacuümkamer**.

Procesverloop bij EBM:
1. Poeder deponeren (rake spreidt laag poeder)
2. Poeder **voor-sinteren** met een gedefocuste elektronenbundel (dit verhit het poeder en geeft het mechanische cohesie → geen steunstructuur nodig)
3. Selectief **smelten** met een gefocuste elektronenbundel
4. Post-processing: "cake breaking" (het voor-gesinterde blok opbreken om de onderdelen vrij te krijgen), reiniging van holten, machining, polijsten, thermische nabehandeling

**Kenmerken:**

| Voordelen | Nadelen |
|---|---|
| Weinig supports nodig (dankzij voor-sinteren) | Hoge oppervlakruwheid (voor-gesinterd poeder kleeft) |
| Lage restspanningen (hoge bouwtemperatuur) | Voor-gesinterd poeder moeilijk hergebruiken |
| Snel bouwproces (excl. post-processing) | Moeilijk uit kleine holten te verwijderen |
| Vacuüm: geen reactie met atmosfeer | Enkel non-ferro metalen (Ti, CoCr) |
| Vacuüm: geen gasinsluitsels | Lage druk veroorzaakt verdamping van sommige elementen |

- Laagdikte: 20–200 µm
- Poedergrootte: 20–300 µm
- Toepassingen: medisch, dentaal (Ti6Al4V, CoCrMo)

### Laser Cladding (LC)

**Principe:** Poeder wordt via een of meerdere nozzles gespoten in het focuspunt van een laserstraal. Het poeder smelt ter plekke en stolt op het substraat. Anders dan bij SLM of EBM is er **geen poederbed** — het poeder wordt on-the-fly ingespoten.

LC wordt ook aangeduid als LENS (Laser Engineered Net Shaping), DMD (Direct Metal Deposition), DLF (Direct Laser Fabrication) of LMD (Laser Metal Deposition).

**Hybride machines:** Laser Cladding gecombineerd met frezen (bijv. DMG Mori). Het proces wisselt af: laag cladden → frezen tot vlak → contour frezen → volgende laag cladden. Dit geeft betere maatnauwkeurigheid dan puur cladden.

| Voordelen | Nadelen |
|---|---|
| Relatief snel | Lage nauwkeurigheid (door gespoten poederkegel) |
| Geschikt voor **reparaties** (niet typisch AM) | Geen uitstekende of complexe overhangende structuren |
| Grote onderdelen mogelijk | Post-machining vrijwel altijd nodig |
| Breed materiaalspectrum | |
| **Gradient-materialen (FGM)** mogelijk | |

- Toepassingen: reparaties van turbinebladen, grote onderdelen, functioneel-gradiëntmaterialen

### Selective Laser Melting (SLM)

**Principe:** Een dunne laag metaalpoeder wordt uitgespreid op het bouwplatform. Een gefocuste laserstraal (typisch Yb-fiber laser, 200–400 W) scant het poeder langs het vooraf berekende scanpatroon. Het poeder wordt **volledig gesmolten** (in tegenstelling tot SLS waarbij het enkel sintert). Na stollen vormt zich een dichte, metallische laag. De buildcylinder zakt een laagdikte, nieuwe poeder wordt aangebracht, en het herhaalt zich.

Procesverloop bij SLM:
1. Poeder deponeren (recoater arm spreidt poeder uit van feedcontainer)
2. Laser scant de laag en smelt het poeder selectief
3. Bouwtafel zakt een laagdikte
4. Herhaal voor n lagen

Post-processing bij SLM:
- Onderdeel zagen/vonken los van de bouwplaat
- Supports verwijderen
- Post-machining: polijsten, boren van nauwkeurige gaten
- Optioneel: spanningsarm gloeien, HIP

**Kenmerken:**

| Voordelen | Nadelen |
|---|---|
| Goed oppervlak en nauwkeurigheid | Relatief traag bouwproces |
| Breed materiaalspectrum (ferro, non-ferro, composieten) | Thermische spanningen (residual stresses) |
| Korte doorlooptijden | Support-structuren nodig voor overhangende zones |
| Hoge designvrijheid | Dure installatie en poeder |

- Toepassingen: medisch, dentaal, automotive, lucht- en ruimtevaart, werktuigbouw, mechanische componenten

### Poedereigenschappen voor SLM

Het poeder is een kritieke factor voor SLM-kwaliteit:
- **Morfologie: sferisch** — ronde korrels stromen beter en geven een uniformere laag. Onregelmatige korrels (plat, geblokt) geven slechte laagkwaliteit.
- **Optimale deeltjesgrootteverdeling** — een mix van grote en kleine korrels vult de ruimtes beter op
- **Grootte afhankelijk van laagdikte** — typisch 5–60 µm voor lagen van 30 µm

---

## 7. SLM: procesparameters en specifieke uitdagingen

### Procesparameters

De kwaliteit van een SLM-onderdeel hangt af van vier categorieën parameters die onderling interageren:

**Laserparameters:**
- Vermogen [W]
- Golflengte [nm]
- Vlekgrootte / spot size [µm]
- Modus (CW of gepulst)
- Bundel-kwaliteit M²

**Scanparameters:**
- Scansnelheid [mm/s]
- Laagdikte [µm]
- Scan spacing (afstand tussen parallelle scanlijnen) [µm]
- Inter-layer rotatie (de scanrichting roteert tussen lagen voor betere isotopie)

**Omgevingsparameters:**
- Zuurstofgehalte (SLM werkt in inert gas: Ar of N₂, O₂ < 0,1%)
- Druk
- Temperatuur

**Materiaalparameters:**
- Laseraborptie van het poeder
- Warmtegeleiding
- Smelttemperatuur
- Poedereigenschappen

### Het smeltbad (melt pool)

Voor een goed SLM-resultaat moet het smeltbad aan vier voorwaarden voldoen:
- **Continu** — geen onderbrekingen in de smeltlijn
- **Verbonden met de vorige laag** — goede binding tussen lagen
- **Voldoende hoogte** — om de volgende laag aan te smelten
- **Verbindingshoek ~90°** — goede wetting van het substraat

Het effect van scansnelheid en laservermogen op het smeltbad:
- Te laag vermogen / te hoge snelheid → onvoldoende smelten, poreusheid
- Te hoog vermogen / te lage snelheid → diepe penetratie, spatten, druppelvorming
- Het juiste procesvenster geeft een stabiel, aaneengesloten smeltbad

### Downfacing surfaces — een specifieke uitdaging

Wanneer een laag moet worden gesmolten boven een holte (een **downfacing** of overhang-oppervlak), rust het smeltbad niet op al gestold materiaal maar op **los poeder**. Poeder geleidt warmte veel slechter dan vast metaal. Het gevolg: het smeltbad "zinkt" dieper in het poeder en vormt een onregelmatige, ruwe laag — **drossvorming**.

Oplossingen:
1. **Supportstructuren** plaatsen onder de overhang — fungeren als warmtegeleiders en mechanische steun
2. **Procesparameters aanpassen** voor de eerste downfacing lagen: lager vermogen, hogere scansnelheid, kleinere scan spacing → minder warmteinput → minder zinken van het smeltbad

> **Belangrijk voor examen:** Begrijpen waarom downfacing surfaces een probleem zijn bij SLM en welke twee oplossingen er zijn.

---

## 8. Lattice structures

### Wat zijn lattice structures?

Lattice structures zijn **poreuze, periodieke structuren** opgebouwd uit herhalende eenheidscellen. Ze worden ook wel scaffolds, metamaterials of biomaterials genoemd. De eigenschappen hangen niet alleen af van het basismateriaal maar ook van de **geometrie van de eenheidscel**.

Conventioneel zijn deze structuren vrijwel onmogelijk te produceren — te complex, te veel interne kanalen. AM is bij uitstek geschikt.

### Voordelen

- **Hoge stijfheid-gewicht verhouding** — door materiaal te verwijderen waar het mechanisch niet bijdraagt
- **Integreerbaar in het buitenoppervlak** van een onderdeel
- **Lokaal aanpasbare eigenschappen** via het ontwerp van de eenheidscel

### Toepassingen

- **Biomedische implantaten** — porositeit matcht botstructuur, bevordert ingroei, past stijfheid aan (stress shielding voorkomen)
- **Warmtewisselaars** — groot oppervlak-volumeverhouding
- **Lichtgewicht structuren** in lucht- en ruimtevaart
- **Energieabsorptie** — crashstructuren

### Uitdagingen

- Weinig experimentele data over mechanische eigenschappen en bezwijkmechanismen
- Invloed van SLM-procesparameters op de eigenschappen van dunne traliestructuren
- FEM-simulatie en optimalisatie van lattice designs is complex

---

## Wat je echt moet kennen

**Inleiding en workflow**
- De definitie van AM: materiaal laag per laag toevoegen op basis van een 3D model
- Het verschil met conventionele substractieve productie (frezen = wegnemen, AM = toevoegen)
- De volledige processtappen: CAD → STL → slicen → bouwen → post-processing
- Wat een STL-bestand is (driehoeksnetwerk van het oppervlak) en waarom het gebruikt wordt
- Waarom slicen nodig is en wat het oplevert (scanpatroon per laag)

**Classificatie**
- De classificatie van AM op basis van startfase: liquid / powder / solid / gas
- Welk proces bij welke startfase hoort (SLA = liquid, SLS/SLM/EBM = powder, FDM = liquid/extrusie)

**Voordelen en nadelen**
- De voordelen van AM: designvrijheid, lichtgewicht, gepersonaliseerde productie, functie-integratie, weinig materialenverspilling
- De nadelen: traag, ruw oppervlak, postprocessing vereist, supportstructuren, niet geschikt voor massaproductie
- AM vervangt conventionele processen NIET — het is een aanvulling voor specifieke gevallen

**AM voor polymeren — drie processen kennen**
- **SLA**: UV-laser polymeriseert vloeibare hars laag per laag; beste oppervlak en nauwkeurigheid
- **FDM**: gesmolten filament door nozzle; goedkoop, traag, matig oppervlak
- **SLS**: laser sintert poeder; geen supports nodig (los poeder = support), part nesting mogelijk, breed materiaalspectrum
- Vergelijken: wanneer kies je welk polymeerproces?

**AM voor metalen — vier processen kennen**
- **EBM**: elektronenbundel in vacuüm op poederbed; voor-sinteren = geen supports; hoge ruwheid; enkel non-ferro
- **Laser Cladding (LC)**: poeder via nozzle in laservlek; geschikt voor reparaties en grote stukken; lage nauwkeurigheid; gradient-materialen mogelijk
- **SLM**: laser smelt poeder volledig; breed materiaalspectrum; goed oppervlak; thermische spanningen; supports nodig voor overhangs
- De voor- en nadelen van elk metaalproces kunnen vergelijken

**SLM-specifiek**
- De vier categorieën procesparameters: laser (vermogen, spot size), scan (snelheid, laagdikte, scan spacing), omgeving (O₂-gehalte, temperatuur), materiaal (smelttemperatuur, absorptie)
- Wat een goed smeltbad is: continu, verbonden met vorige laag, juiste hoogte, verbindingshoek ~90°
- Wat downfacing surfaces zijn en waarom ze een probleem vormen (smeltbad op los poeder = drossvorming)
- De twee oplossingen voor downfacing: support structures en aanpassing procesparameters
- Poedereigenschappen voor SLM: sferisch, juiste grootteverdeling, passende grootte voor laagdikte

**Lattice structures**
- Wat het zijn: periodieke poreuze structuren waarvan de eigenschappen afhangen van de eenheidscel-geometrie
- Waarom AM ideaal is voor lattice structures (te complex voor conventionele productie)
- Toepassingen: biomedische implantaten, warmtewisselaars, lichtgewicht aerospace-onderdelen

---

*Gebaseerd op slides: "PMA Les 15 Additive Manufacturing 2022" — Prof. Brecht Van Hooreweder, KU Leuven*
