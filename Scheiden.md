# Deel 6 – Scheiden (Les 12)

---

## Inhoudsopgave

- [Wat is scheiden?](#wat-is-scheiden)
- [Hoe verloopt het snijproces?](#hoe-verloopt-het-snijproces)
  - [De gesneden rand](#de-gesneden-rand)
- [Snijspleet (clearance)](#snijspleet-clearance)
- [Pons- en matrijsafmetingen](#pons--en-matrijsafmetingen)
  - [Bij stansen (blanking)](#bij-stansen-blanking--het-uitgestanste-stuk-is-het-product)
  - [Bij ponsen (punching)](#bij-ponsen-punching--het-gat-is-het-product)
- [Ponskracht berekening](#ponskracht-berekening)
  - [Maximale theoretische ponskracht](#maximale-theoretische-ponskracht)
  - [Aangrijpingspunt resulterende kracht](#waar-grijpt-de-resulterende-kracht-aan)
- [Afgeschuind ponsgereedschap (Shear on tools)](#afgeschuind-ponsgereedschap-shear-on-tools)
- [Gereedschappen en machines](#gereedschappen-en-machines)
  - [Compleetstempel (Compound die)](#compleetstempel-compound-die)
  - [Volgstempel (Progressive die)](#volgstempel-progressive-die)
- [Fijnstansen (Fine blanking)](#fijnstansen-fine-blanking)
- [Diverse plaatwerkprocessen](#diverse-plaatwerkprocessen)
  - [Incrementeel omvormen](#incrementeel-omvormen-incremental-forming)
  - [Vloeidraaien (Spinning)](#vloeidraaien-spinning)
  - [Hydroformen (Hydroforming)](#hydroformen-hydroforming)
- [Samenvatting en examenoverzicht](#samenvatting-en-examenoverzicht)
- [Wat je echt moet kennen](#wat-je-echt-moet-kennen)

---

## Wat is scheiden?

Scheiden is het snijden van plaatmateriaal **zonder spanen te creëren**. Anders dan bij verspanen wordt er geen materiaal weggefreesd of gedraaid — het materiaal wordt gewoon doorgesneden via plastische vervorming tot breuk.

Er zijn drie hoofdbewerkingen:

- **Knippen** (*shearing*): grote platen kleiner maken. De snijlijn is open (recht of gebogen), één mes beweegt t.o.v. het andere.
- **Stansen / uitsnijden** (*blanking*): de **omtrek** van een onderdeel uit een plaat snijden. Het uitgestanste stuk is het **eindproduct** (de *blank*). De rest is schroot.
- **Ponsen** (*punching*): een **gat** maken in een plaat. Het uitgedreven stukje is de *slug* (dop) — het schroot. De plaat met het gat is het eindproduct.

```
Ponsen  → gat in de plaat = product, dop = schroot
Stansen → uitgestanst stuk = product, frame = schroot
```

Het principe is hetzelfde voor alle drie: pons (*punch*) duwt omlaag, matrijs (*die*) ondersteunt van onderen, het materiaal breekt langs de snijranden.

---

## Hoe verloopt het snijproces?

Het snijproces verloopt in vier fasen:

1. **Elastische vervorming**: de pons raakt het werkstuk en het materiaal buigt iets door.
2. **Plastische vervorming**: de pons dringt verder, spanning overschrijdt de vloeigrens → het materiaal vloeit plastisch. Er ontstaat een glad gepolijst oppervlak.
3. **Breukinitiatie**: aan de snijranden van zowel pons als matrijs ontstaan scheurhaarden.
4. **Breukvoortplanting**: de scheuren propageren naar elkaar toe en het materiaal scheidt plots.

### De gesneden rand

De rand van een gestanst of geponst onderdeel bestaat uit vier duidelijk herkenbare zones:

| Zone | Beschrijving |
|---|---|
| **Rollover** (inzakking) | Boven, afgerond — plastische vervorming vóór het snijden |
| **Burnish** (polijstzone) | Glad en glanzend — gevolg van penetratie vóór breuk |
| **Breukzone** | Ruw en schuin — gevolg van de eigenlijke breuk |
| **Braam** (*burr*) | Scherpe rand onderaan — door rek van het materiaal in de laatste fase |

Een goede snijspleet geeft een grotere burnishzone (smooth) en een kleine braam. Bij fijnstansen is de volledige rand burnish — maar daarover later meer.

---

## Snijspleet (clearance)

### Wat is het?

De **snijspleet** *u* is de afstand tussen de snijkant van de pons en de snijkant van de matrijs. Het is één van de meest kritische parameters bij ponsen en stansen.

### Wat doet de snijspleet?

- **Snijspleet te klein**: de breuklijnen van pons- en matrijskant lopen langs elkaar heen en kruisen niet netjes. Resultaat: dubbele polijstzone, grotere krachten, slechte randkwaliteit.
- **Snijspleet te groot**: het materiaal wordt eerder in de matrijs getrokken dan gesneden. Resultaat: grote bramen, slechte toleranties.
- **Optimale snijspleet**: breuklijnen propageren precies naar elkaar toe en ontmoeten in het midden → schone, rechte rand.

### Berekening

$$u = a \cdot t$$

waarbij:
- **u** = snijspleet (op één kant)
- **t** = plaatdikte
- **a** = vergoedingsfactor (afhankelijk van het materiaal)

Typische waarden voor a:

| Materiaal | Vergoeding a |
|---|---|
| Zacht aluminium (1100, 5052) | 0.045 |
| Harder aluminium (2024, 6061), zacht staal, zacht RVS | 0.060 |
| Halfhard staal, halfhard/volledig hard RVS | 0.075 |

In de praktijk: 2% tot 10% van de plaatdikte, afhankelijk van het materiaal en de vereiste randkwaliteit.

> **belangrijk voor examen**: ken het verschil tussen te kleine en te grote snijspleet, en de formule u = a·t.

---

## Pons- en matrijsafmetingen

De snijspleet zit altijd op de juiste kant, afhankelijk van wat het eindproduct is:

### Bij stansen (blanking) — het uitgestanste stuk is het product

Je wil dat de blank de juiste diameter heeft → de **matrijs** bepaalt de blankgrootte:

- Stansmatrijs diameter = **D_b** (gewenste blankdiameter)
- Stansstempel diameter = **D_b − 2u**

De pons is kleiner dan de matrijs zodat er een spleet is aan beide kanten.

### Bij ponsen (punching) — het gat is het product

Je wil dat het gat de juiste diameter heeft → de **pons** bepaalt de gatgrootte:

- Ponsstempel diameter = **D_h** (gewenste gatdiameter)
- Ponsmatrijs diameter = **D_h + 2u**

De matrijs is groter zodat de spleet aan beide zijden aanwezig is.

> **intuition**: de pons bepaalt het gat, de matrijs bepaalt de blank. Onthoud dit en je kan altijd afleiden welke kant de spleet zit.

---

## Ponskracht berekening

### Maximale theoretische ponskracht

$$F_t = \tau \times L \times t$$

waarbij:
- **τ** = schuifsterkte van het materiaal ≈ 0.75 × UTS (treksterkte)
- **L** = totale snijlijnlengte (omtrek van de contour)
- **t** = plaatdikte

Voor een cirkelvormig gat: L = π × d.

> **belangrijk voor examen**: schuifsterkte = 0.75 × UTS, dit is een standaardaanname.

### Waar grijpt de resulterende kracht aan?

Als de snijcontour niet symmetrisch is (meerdere gaten, complexe vormen), is de resulterende kracht niet in het middelpunt van de stempel. Je moet het **zwaartepunt van de snijlijn** (centroid) berekenen:

$$x_0 = \frac{\sum L_i x_i}{\sum L_i}, \quad y_0 = \frac{\sum L_i y_i}{\sum L_i}$$

waarbij L_i de lengte van elk segment is en (x_i, y_i) de coördinaat van het middelpunt van dat segment.

Dit is belangrijk omdat de stempelram gecentreerd moet zijn op de resulterende kracht. Als dat niet zo is, onstaan er buigende momenten op de pons die het gereedschap kunnen beschadigen of een ongelijkmatige snijwerking veroorzaken.

---

## Afgeschuind ponsgereedschap (Shear on tools)

### Probleem

Wanneer een pons gelijktijdig de volledige contour doorknipt, treedt de maximale kracht F_t plotseling op. Dit geeft een hoge piekbelasting op de pers en het gereedschap, met schokken en slijtage als gevolg.

### Oplossing: afschuifhoek

Door een **hoek aan te brengen op de pons of matrijs** snij je niet de volledige omtrek tegelijk maar progressief over een langere slag. De totale arbeid blijft gelijk, maar de piekbelasting is lager.

$$W = F_t \cdot t \cdot p = F_s \cdot s$$

$$F_s = K \cdot F_t \quad \text{met } K = \frac{t \cdot p}{s}$$

waarbij:
- **p** = penetratiepercentage (typisch 30–60%)
- **s** = afschuifafstand (slaglengte met de hoek)
- **K** moet kleiner zijn dan 1 om de kracht te verminderen → dus **s > t·p**

**Voordelen afgeschuind gereedschap:**
- Lagere ponskracht
- Minder schokken op de pers
- Geleidelijk snijden over een langere slag

---

## Gereedschappen en machines

### Compleetstempel (Compound die)

Een compleetstempel combineert **meerdere bewerkingen op dezelfde positie** in één persslag. Typisch: stansen én ponsen tegelijk op dezelfde locatie.

Voordelen:
- Goede toleranties en concentriciteit van gaten t.o.v. de blank.
- Economisch: één pers, één operator.
- Verplaatsingfouten worden geminimaliseerd.

Nadelen:
- Niet geschikt voor complexe vormen waarbij te veel matrijsdetail op één plek zit.
- Bv. een geponst gat te dicht bij de rand van de blank → risico op breuk van het gereedschap.

### Volgstempel (Progressive die)

Een volgstempel voert **meerdere opeenvolgende bewerkingen uit in aparte stations**. De strip metaal beweegt stap voor stap van station naar station: eerst ponsen, dan stansen, misschien ook vormen of trekken. Het onderdeel blijft verbonden met het schrootskeleton tot de laatste bewerking.

Voordelen:
- Zeer hoge productiesnelheid.
- Kan onbeheerd draaien.
- Slechts één pers nodig.

Nadelen:
- Duurder dan eenvoudige matrijzen.
- Nauwkeurige uitlijning nodig.
- Vereist een spoelaanvoersysteem.
- Schade aan één station verplicht demontage van de hele stansset.

```
Strip → [station 1: ponsen] → [station 2: trekken] → [station 3: stansen] → eindproduct
```

---

## Fijnstansen (Fine blanking)

### Wat is het?

Fijnstansen is een speciale variant van stansen waarbij de gesneden rand **volledig glad en scheurvrij** is over de volledige plaatdikte. Bij conventioneel stansen heb je de typische vier zones (rollover, burnish, breuk, braam). Bij fijnstansen is het volledige snijoppervlak een burnishzone.

### Hoe werkt het?

Het principe combineert drie krachten tegelijk:
1. De pons snijdt het materiaal uit.
2. Een **klemring** (*blankholder* met V-rib) omsluit de blankomtrek en verhindert dat het materiaal buiten de snijzone kan vloeien.
3. Een **tegendrukplaat** onderaan ondersteunt de blank van onderen en verhoogt de hydrostatische druk in de snijzone.

De verhoogde **hydrostatische druk** is de sleutel: door druk in alle richtingen te verhogen, wordt scheuren onderdrukt en kan het materiaal meer plastisch vervormen zonder te breken. Het gevolg is een volledig glad oppervlak.

### Voordelen vs conventioneel stansen

| Eigenschap | Conventioneel | Fijnstansen |
|---|---|---|
| Randkwaliteit | Rollover + breukzone + braam | Volledig glad (burnish) |
| Toleranties | Matig | Nauw |
| Scheurvrij? | Nee | Ja |
| Snijspleet | Groter | Veel kleiner (~1% van t) |
| Kracht nodig | Normaal | Hoger (extra klemkrachten) |

> **belangrijk voor examen**: fijnstansen = hogere hydrostatische druk → scheuren onderdrukt → volledig glad snijvlak.

---

## Diverse plaatwerkprocessen

Naast ponsen, stansen en buigen bestaan er nog enkele speciale processen voor plaatwerk.

### Incrementeel omvormen (Incremental forming)

In plaats van één stempel die de volledige vorm in één slag maakt, wordt hier een kleine roterende punt (*tool*) langs een CNC-geprogrammeerd pad over het werkstuk bewogen. Elke pas vervormt het materiaal een klein beetje (*incrementeel*). De gewenste 3D-vorm ontstaat door opeenvolgende kleine vervormingen.

Voordelen:
- Geen specifieke matrijs nodig → lage gereedschapskosten.
- Grote flexibiliteit: elke vorm is mogelijk via programmering.
- Geschikt voor prototypes en kleine series.

Nadelen:
- Traag — niet geschikt voor massaproductie.
- Materiaalbeperkingen (niet alle metalen werken even goed).

Toepassingen: koplampreflectoren, prototypes, medische implantaten.

### Vloeidraaien (Spinning)

Een ronde plaat (*blank*) wordt op een roterende doorn (*mandrel*) gedrukt en met een gereedschap of rol progressief over de doorn gevormd. Het resultaat is een axiaal-symmetrisch hol onderdeel.

Er zijn twee varianten:
- **Conventioneel vloeidraaien**: de plaatdikte blijft min of meer constant, de diameter verandert.
- **Schuifvloeidraaien** (*shear spinning*): de diameter van de blank blijft gelijk, maar de plaatdikte neemt af. Geschikt voor conische vormen.

Kenmerk: cirkelvormige sporen op het buitenoppervlak verraden dat een onderdeel is gedraaid (bv. aluminium kookpotten, lichtreflectoren).

### Hydroformen (Hydroforming)

In plaats van een vaste pons of matrijs gebruik je **vloeistofdruk** om het metaal te vormen.

**Plaat hydroformen**: een rubberzak gevuld met vloeistof onder druk fungeert als de "zachte matrijs". Het plaatmateriaal wordt er tegenaan geperst en neemt de vorm van de starre kant aan.

**Buis hydroformen**: een metalen buis wordt in een matrijs geplaatst en van binnenuit onder hoge vloeistofdruk gezet. De buis expandeert en vult de matrijsvorm.

Voordelen:
- Lage gereedschapskosten (slechts één starre helft nodig).
- Weinig matrijsslijtage.
- Complexe vormen mogelijk.
- Betere vervormbaarheid door meer uniforme spanningsverdeling.
- Goed oppervlak.

Nadelen:
- Traag proces.
- Hoge vloeistofdruk vereist (technisch complexe installatie).

---

## Samenvatting en examenoverzicht

| Concept | Kernformule / Regel |
|---|---|
| Ponsen vs stansen | Pons bepaalt gat, matrijs bepaalt blank |
| Snijspleet | u = a·t (a = 0.045–0.075 afhankelijk van materiaal) |
| Matrijs stansen | D_matrijs = D_blank; D_pons = D_blank − 2u |
| Matrijs ponsen | D_pons = D_gat; D_matrijs = D_gat + 2u |
| Ponskracht | F_t = τ × L × t, met τ = 0.75 × UTS |
| Centroid kracht | x₀ = ΣLᵢxᵢ / ΣLᵢ |
| Afschuifkracht | F_s = K·F_t met K = t·p/s < 1 |
| Fijnstansen | Verhoogde hydrostatische druk → glad snijvlak |

Processen die je moet kennen:
- **Knippen / ponsen / stansen**: werking, snijspleet, kracht, centroid
- **Gereedschappen**: compleetstempel vs volgstempel (wanneer welke gebruiken)
- **Fijnstansen**: principe en voordelen t.o.v. conventioneel stansen
- **Incrementeel omvormen / vloeidraaien / hydroformen**: globaal principe en voor/nadelen

---

## Wat je echt moet kennen

- Het verschil tussen ponsen (gat = product) en stansen (uitgestanst stuk = product)
- De vier fasen van het snijproces: elastisch, plastisch, breukinitiatie, breukvoortplanting
- De vier zones op een gesneden rand: rollover, burnish, breukzone, braam
- Wat een optimale snijspleet doet: breuklijnen ontmoeten elkaar netjes in het midden
- Gevolg van te kleine snijspleet (dubbele polijstzone) vs te grote (grote bramen)
- De formule voor snijspleet: u = a·t, en typische waarden voor a per materiaal
- Welke afmeting de pons bepaalt en welke de matrijs bepaalt bij ponsen vs stansen
- De ponskracht: F_t = τ × L × t, met τ ≈ 0.75 × UTS
- Hoe je het aangrijpingspunt van de resulterende kracht bepaalt (centroid via ΣLᵢxᵢ/ΣLᵢ)
- Waarom je een afschuifhoek aanbrengt op de pons (piekbelasting verlagen)
- Het verschil tussen een compleetstempel en een volgstempel (wanneer welke kiezen)
- Het principe van fijnstansen: drie krachten (pons, klemring, tegendrukplaat), hogere hydrostatische druk
- Waarom hydrostatische druk scheuren onderdrukt → volledig glad (burnish) snijvlak
- Wat incrementeel omvormen is en voor welke situaties het geschikt is (prototypes, kleine series)
- Het principe van vloeidraaien (conventioneel vs schuifvloeidraaien) en de typische toepassing
- Het principe van hydroformen (plaat en buis) en de voordelen t.o.v. klassiek stansen
