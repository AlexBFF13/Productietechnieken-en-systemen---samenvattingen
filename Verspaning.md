# Verspaning — Productietechnieken en Systemen (H01O1)
**KU Leuven · Prof. Brecht Van Hooreweder · Semester 6**

---

## Inhoudsopgave

1. [Overzicht productietechnieken](#1-overzicht-productietechnieken)
2. [Wat is verspaning?](#2-wat-is-verspaning)
3. [Gereedschapsgeometrie](#3-gereedschapsgeometrie)
4. [Spaanvorming](#4-spaanvorming)
5. [Bewegingen en krachten](#5-bewegingen-en-krachten)
6. [Snijmaterialen](#6-snijmaterialen)
7. [Gereedschapslijtage en standtijd (Taylor)](#7-gereedschapslijtage-en-standtijd-taylor)
8. [Snijvloeistoffen](#8-snijvloeistoffen)
9. [Draaidiagrammen](#9-draaidiagrammen)
10. [Boren](#10-boren)
11. [Frezen](#11-frezen)
12. [Economische aspecten en werkvoorbereiding](#12-economische-aspecten-en-werkvoorbereiding)
13. [Formuleoverzicht](#13-formuleoverzicht)

---

## 1. Overzicht productietechnieken

Er zijn **6 hoofdgroepen** van vervaardigingstechnieken:

| Hoofdgroep | Principe | Voorbeelden |
|---|---|---|
| **Oervormen** | Vorm geven aan vormloos materiaal | Gieten, spuitgieten, zandgieten |
| **Omvormen** | Plastisch vervormen zonder materiaalverlies | Smeden, walsen, plaatbuigen, ponsen |
| **Scheiden / Afnemen** | Materiaal verwijderen | Lasers, waterstraal, **verspanen** |
| **Verbinden** | Delen samenvoegen | Lassen, lijmen, schroeven |
| **Opbrengen van lagen** | Materiaal toevoegen aan oppervlak | Coaten, galvaniseren, spuiten |
| **Veranderen van materiaaleigenschappen** | Structuur aanpassen | Harden, gloeien, nitreren |

**Verspaning** valt onder *Scheiden/Afnemen*: door een snijbeweging wordt materiaal verwijderd als spaan.

### Bewerkingskeuze

De keuze van een productietechniek hangt af van:

- **Productiekosten** — eenmalige kosten (matrijs), herhaalkosten, repeterende kosten
- **Productiesnelheid** — hoe snel kan een batch gemaakt worden?
- **Materiaal** — niet elk materiaal is even goed verspanbaar of gietbaar
- **Flexibiliteit** — productgebonden vs. universeel gereedschap
- **Kwaliteit** — nauwkeurigheid, oppervlakteruwheid, mechanische eigenschappen
- **Milieueffect**
- **Ontwerp** — vlakke dunne delen kunnen niet gegoten worden; complexe vormen zijn moeilijk te smeden

---

## 2. Wat is verspaning?

### Definitie

Verspaning is het **verwijderen van materiaal** door de relatieve beweging tussen een **gereedschap** (met gedefinieerde snijkantgeometrie) en een **werkstuk**, waardoor een **spaan** gevormd wordt.

### Voordelen van verspaning

- **Vormvrijheid** — vrijwel elke vorm is mogelijk
- Geschikt voor **kleine series** (geen dure matrijs nodig)
- Vermijdt lange levertijd van smeedmatrijzen
- Hoge **nauwkeurigheid** en goede **oppervlaktegesteldheid**

### Nadelen van verspaning

- **Materiaalverlies** (verspaand materiaal wordt spaan → recycleerbaar maar energie-intensief)
- **Energie-intensief** proces
- **Tijdrovend** ten opzichte van massaproductietechnieken
- **Vervuiling** van machines en werkplaatsen
- Gebruik van **koelvloeistoffen** (milieu-impact) → trend naar MQL (Minimum Quantity Lubrication)

### Indeling van verspaningsprocessen

```
GECONTROLEERDE SNIJKANTGEOMETRIE
├── Enkelvoudige snijkant:   schaven, draaien, kotteren
├── Meervoudige snijkanten:  boren, frezen, ruimen, tappen, trekfrezen, zagen
│
ONGECONTROLEERDE SNIJKANTGEOMETRIE
└── Veelvuldige snijkanten:  slijpen, honen, lappen, polieren
    (1000 … ∞ abrasieve korrels)
```

### Nauwkeurigheid en ruwheid

Verspaning levert een van de **beste nauwkeurigheden** van alle productietechnieken:
- Toleranties: IT5 – IT10 (afhankelijk van de bewerking)
- Oppervlakteruwheid Ra: 0.1 – 6.3 µm (fijndraaien/slijpen zelfs fijner)

---

## 3. Gereedschapsgeometrie

### 3.1 De basishoeken

Het snijgereedschap (beitel) heeft een **wigvorm** met drie basishoeken die samenhangen:

$$\alpha + \beta + \gamma = 90°$$

| Symbool | Naam | Uitleg |
|---|---|---|
| **α** (alpha) | **Vrijloophoek** | Hoek tussen vrijloopvlak en het gesneden vlak. Vermindert wrijving op het vrijloopvlak. Typisch 6°–10°. |
| **β** (beta) | **Wighoek** | Bepaalt de sterkte van de snijwig en warmteafvoer. Zo groot mogelijk voor sterke beitel. |
| **γ** (gamma) | **Spaanhoek** | Hoek van het spaanvlak. Bepaalt hoe de spaan wegloopt. Typisch −10° tot +30°. |

**Extra hoeken:**

| Symbool | Naam | Uitleg |
|---|---|---|
| **κ** (kappa) | **Instelhoek** (= aanzethoek) | Hoek tussen hoofdsnijkant en voedingsrichting |
| **λ** (lambda) | **Hellingshoek** | Helling van de snijkant t.o.v. een vlak loodrecht op de snijrichting |
| **ε** (epsilon) | **Neushoek** | Hoek aan de punt van het gereedschap |

### 3.2 Invloed van de spaanhoek γ

**Positieve spaanhoek** (γ > 0°):
- Gereedschap snijdt gemakkelijk
- Kleinere snijkrachten, minder trillingsgevaar
- Spanen vloeien vlot weg
- **Maar**: wighoek β is kleiner → beitel is zwakker
- Toepassing: zachte, taaie materialen (aluminium, kunststoffen)

**Negatieve spaanhoek** (γ < 0°):
- Spaan wordt meer gestuikt → grotere krachten en meer warmte
- Beitel is echter **zeer sterk**
- Toepassing: harde, brosse materialen (staal >1200 N/mm², keramiek)

> **Vuistregel:** hoe harder het materiaal, hoe groter de wighoek β en hoe kleiner de spaanhoek γ.

### 3.3 Vrijloophoek α

- Te klein → veel wrijving tussen vrijloopvlak en werkstuk → warmte en slijtage
- Te groot → kleinere wighoek β → zwakkere beitel
- **Zachte/taaie materialen**: grote vrijloophoek
- **Harde materialen**: kleine vrijloophoek

### 3.4 Hellingshoek λ

De hellingshoek bepaalt de richting van de spaanafvoer:
- λ > 0°: spaan loopt weg van de neus (gunstig)
- λ = 0°: spaan loopt loodrecht weg
- λ < 0°: spaan loopt naar de neus (ongunstig, gevaar voor beschadiging)

### 3.5 Onderdelen van het gereedschap

```
Schacht
  └── Werkend deel
        ├── Hoofdsnijkant S        (doet het eigenlijke snijwerk)
        ├── Hulpsnijkant S'
        ├── Eerste spaanvlak Aγ1
        ├── Tweede spaanvlak Aγ2
        ├── Eerste vrijloopvlak Aα1
        ├── Tweede vrijloopvlak Aα2
        ├── Hulpvrijloopvlak Aα1'
        ├── Neus (punt)
        ├── Neusafronding rε
        └── Neusafschuining bε
```

---

## 4. Spaanvorming

### 4.1 Principe

Bij verspaning dringt de snijkant in het werkstuk. Het materiaal vóór de snijkant wordt **afgeschoven** langs een **afschuifvlak** en vormt een **spaan**.

Twee belangrijke diktes:
- **T₁ = snededikte** (dikte van het onvervormd materiaal)
- **T₂ = spaandikte** (dikte van de spaan na vervorming)

T₂ > T₁: de spaan is dikker dan de snede (opstuikverhouding).

### 4.2 Afschuifhoek φ (Merchant)

De afschuifhoek φ bepaalt de grootte van het afschuifvlak en daarmee de snijkrachten:

$$\boxed{\phi = 45° + \frac{\gamma}{2} - \frac{\mu}{2}}$$

- φ **groter** → kleiner afschuifvlak → **kleinere krachten**
- φ groter door: grotere spaanhoek γ of kleinere wrijving µ (coating, smering)
- Grotere spaanhoek → kleinere wighoek → zwakkere beitel (trade-off!)

> **Niet-examenleerstof:** de volledige afleiding van de Merchant-formule (4.2 fysische verspaningswetten).

### 4.3 Snededoorsnede

De snededoorsnede A is de doorsnede van het materiaal dat per snede verwijderd wordt:

$$A = a \times f = b \times h$$

Met de relaties (via de instelhoek κ):

$$b = \frac{a}{\sin \kappa} \qquad h = f \cdot \sin \kappa$$

| Symbool | Naam | Eenheid |
|---|---|---|
| a | snijdiepte (insteldiepte, ingrijping) | mm |
| f | voeding (aanzet per omwenteling) | mm/omw |
| b | snedebreedte | mm |
| h | snededikte | mm |
| κ | instelhoek (= aanzethoek) | ° |

### 4.4 Slankheid van de snede

De **slankheid** δ_κ is de verhouding snedebreedte / snededikte:

$$\delta_\kappa = \frac{b}{h}$$

Voor een goede spaanvorming en spaanbreking moet δ_κ binnen bepaalde grenzen liggen:
- **Staal**: 3 < δ_κ < 15
- **Gietijzer**: 3 < δ_κ < 30 (broos materiaal brokkelt gemakkelijker af)

### 4.5 Soorten spanen

| Type | Omstandigheden | Kenmerken |
|---|---|---|
| **Continue spaan** | Taaie materialen, positieve spaanhoek, hoge snijsnelheid | Lange aaneengesloten lint, gevaar voor verstrengeling |
| **Lamelspaan** (getande spaan) | Variabele afschuiving | Getand uiterlijk, tussentoestand |
| **Brokkelspaan** | Brosse materialen (gietijzer, brons, messing) | Losse brokjes, gunstig voor spaanafvoer |

> **Praktisch:** spaanbrekers op snijplaatjes zorgen ervoor dat continue spanen breken tot kortere stukken, wat spaanafvoer vergemakkelijkt.

---

## 5. Bewegingen en krachten

### 5.1 De drie bewegingen

Bij elke verspaningsbewerking zijn er drie bewegingen:

1. **Hoofdsnijbeweging** — de beweging die de spaan afneemt (bijv. rotatie werkstuk bij draaien, rotatie frees bij frezen). Snelheid = snijsnelheid v_c [m/min]
2. **Voedingsbeweging** — de langzame voorwaartse beweging. Voeding f [mm/omw] of [mm/tand]
3. **Instelbeweging** — eenmalige instelling van de snijdiepte a [mm]

### 5.2 De drie krachten

De totale snijkracht F wordt ontleed in drie componenten:

| Kracht | Symbool | Richting | Belang |
|---|---|---|---|
| **Hoofdsnijkracht** | F_c | Tangentieel, richting v_c | Bepaalt snijvermogen: P_c = F_c × v_c |
| **Voedingskracht** | F_f | Langs de voedingsrichting | Beïnvloedt doorbuiging |
| **Terugdrukkracht** | F_p | Loodrecht op bewerkt vlak | Beïnvloedt doorbuiging werkstuk |

**Waarom F_c kennen?**
- Berekenen van het benodigde **machinevermogen**: P_c = F_c × v_c
- De machinestructuur voldoende **stijf** construeren
- **Levensduur** van het gereedschap bepalen

### 5.3 Formule van Kienzle

Voor de hoofdsnijkracht F_c geldt de empirische wet van Kienzle:

$$\boxed{F_c = k_{c1.1} \times b \times h^{(1-e)}}$$

Of equivalent, uitgedrukt in snijdiepte a en voeding f (voor gegeven instelhoek κ):

$$F_c = k_{c1.1} \times a \times f^{(1-\varepsilon)}$$

| Parameter | Betekenis |
|---|---|
| k_c1.1 [N/mm²] | **Specifieke snijkracht** — materiaaleigenschap (zie tabel) |
| e (= z) | **Invloedscoëfficiënt** — hoe sterk verandert F_c met h |
| b | snedebreedte [mm] |
| h | snededikte [mm] |

**Waarden k_c1.1 en z (Kienzle):**

| Materiaal | k_c1.1 [N/mm²] | z |
|---|---|---|
| St 42 | 1780 | 0.167 |
| St 50 | 1190 | 0.253 |
| St 60 | 2110 | 0.155 |
| C 45 | 2190 | 0.139 |
| C 60 | 2120 | 0.173 |

### 5.4 Vermogen en temperatuur

**Snijvermogen:**
$$P_c = F_c \times v_c$$

Let op: spilvermogen ≠ motorvermogen (er zijn verliezen in reductiekast, lagers, enz.)

**Warmteontwikkeling:** bij verspaning komt energie vrij als warmte:
- **Vervormingswarmte** in de afschuifzone (primaire zone) — ~75%
- **Wrijvingswarmte** tussen spaan en spaanvlak (secundaire zone) — ~18%
- Kleinere hoeveelheden in het vrijloopvlak en werkstuk

**Warmhardheid** = het vermogen van het gereedschapsmateriaal om tot hoge temperaturen hard te blijven. Dit is de sleuteleigenschap die HSS, HM en keramiek onderscheidt.

---

## 6. Snijmaterialen

### 6.1 Hiërarchie van snijmaterialen

Van goedkoop/taai naar duur/hard:

```
Gereedschapsstaal (koolstofstaal)
    ↓
HSS (snelstaal)
    ↓
HM (hardmetaal / WIDIA)
    ↓
Gecoat HM
    ↓
Cermets
    ↓
Keramiek (Al₂O₃, Si₃N₄)
    ↓
CBN (kubisch boornitride)
    ↓
Diamant (PKD)
```

> **Examenrelevant:** ken de hiërarchie, de eigenschappen per type, en de ISO-codering.

### 6.2 Eigenschappen per type

| Snijmateriaal | Hardheid (HRC) | Max. temp. (°C) | V_max (m/min) |
|---|---|---|---|
| Koolstofstaal | 60–65 | 200 | 5–7 |
| HSS | 60–65 | 500 | 20–40 |
| Hardmetaal (HM) | 75 | 1000 | 50–400 |
| Keramiek | 80 | 1300 | 200–1000 |
| CBN | — | 2000 | ~3000 |
| Diamant | — | — | hoog |

**Tegenstrijdige eisen aan snijmaterialen:**
- Slijtagebestendig + warmhardheid (want hoge temperaturen)
- Breukbestendigheid (weerstand tegen stoten en impactbelasting)
- Weerstand tegen vermoeiing en thermoshock
- Oxidatiebestendigheid, weerstand tegen opbouwsnijkant
- Goede prijs, bewerkbaarheid, constantheid van eigenschappen

### 6.3 Gereedschapsstaal (koolstofstaal)

- **Samenstelling:** 0.9–1.2% C, gehard
- **v_c:** zeer laag (0.1–0.2 m/s)
- **Toepassing:** eenvoudige gereedschappen, lage snelheden, hobbygebruik

### 6.4 HSS — High Speed Steel (snelstaal)

- **Samenstelling:** hooggelegeerd met W, Cr, V, Mo (totaal 20–30% legeringselementen)
- W en C vormen harde wolfraamcarbiden
- **v_c:** 0.3–1 m/s
- **Voordeel t.o.v. HM:** beter bestand tegen stoten → geschikter voor **onderbroken snede** (boren, frezen)
- **Toepassing vandaag:** ingewikkeld gevormde gereedschappen (tappen, ruimers, profielfrezen)

### 6.5 Hardmetaal (HM) — WIDIA

- **Samenstelling:** composiet — kobaltmatrix (taai) + wolfraamcarbiden (hard)
  - Kobalt (Co): geeft taaiheid en bindmiddel
  - Carbiden (WC): geven hardheid en hittebestendigheid
- **v_c:** 1–10 m/s
- **Nadeel:** weinig taai → gevoelig voor stoten

#### ISO-codering HM snijmaterialen

**Format: XX-Y##**

**Eerste deel** (type gereedschap):
| Code | Betekenis |
|---|---|
| HW | Onbekleed hardmetaal op wolframbasis |
| HC | **Gecoat hardmetaal** |
| HT | Cermets |
| CA | Keramiek op aluminiumbasis |
| CM | Keramiek op siliciumnitridebasis |
| CC | Gecoat keramiek |
| BN | Kubisch boriumnitride (CBN) |
| DP | Polykristallijn diamant (PKD) |

**Tweede deel** (te bewerken materiaal):
| Letter | Materiaal | Kleur |
|---|---|---|
| P | Staal (behalve RVS) | Blauw |
| M | Roestvrij/austenitisch staal | Geel |
| K | Gietijzer, non-ferro, Ti/Ni/Co legeringen | Rood |
| N | Non-ferrometalen | Groen |
| S | Hittebestendige legeringen | Oranje |
| H | Geharde materialen | Grijs |

**Derde deel** (getal 10–40):
- **Klein getal** (bijv. P10): **bros, hard, hittebestendig** → finisseren, hoge snijsnelheid
- **Groot getal** (bijv. P40): **taai** → grote snijkrachten, dynamische belastingen, schrobben

**Voorbeeld:** `HC-K15` = gecoat hardmetaal, voor gietijzer, relatief hard/bros (finisseren)

### 6.6 Gecoate hardmetalen

- **Principe:** taaie hardmetaalsoort als substraat + dunne slijtbestendige coating (2–20 µm)
- **Coatinglagen:** TiN, TiC,N, Al₂O₃ (meerdere lagen mogelijk = multi-coating)
- **Voordeel:** combinatie van taaiheid (substraat) en slijtvastheid (coating)
- Gecoat HM heeft een **langere standtijd** dan ongecoat HM bij dezelfde snijsnelheid

### 6.7 Cermets

- **Keramiek in metallieke matrix** (cf. hardmetaal, maar met andere samenstelling)
- Matrix: Co, Ni, Fe of Mo
- Keramische fase: metaalcarbides, -nitrides of -oxides
- **Toepassingen:** hoge snelheden (hoge temperaturen), niet-onderbroken snede, kleine snededoorsneden

### 6.8 Keramiek

- **Materialen:** Al₂O₃ (aluminiumoxide), TiC, Si₃N₄ (siliciumnitride)
- **Productie:** sintering
- Hoge hardheid, uitmuntende warmhardheid
- **Nadeel:** broos, gevoelig voor thermoshock → niet geschikt voor onderbroken snede

### 6.9 CBN — Kubisch Boornitride

- Tweede hardste materiaal na diamant
- **Toepassing:** hardverspanen (gehard staal, 55–65 HRC)
- Kan worden toegepast als alternatief voor slijpen bij geharde staalonderdelen

### 6.10 Diamant (PKD — Polykristallijn Diamant)

- Hardste bekend materiaal
- **Beperking:** koolstof uit diamant lost op in ijzer (Fe) van werkstuk → **niet bruikbaar voor staal**
- **Toepassingen:** aluminium, koper, composieten, keramiek, hout

### 6.11 Snijplaatjes (inserts)

In de praktijk worden **wisselplaatjes** gebruikt i.p.v. massieve beitels:
- Goedkoper (alleen het plaatje vervangen, niet de schacht)
- Meerdere bruikbare snijkanten per plaatje (indexeerbaar)
- Klemsystemen: klemvinger of klemstuk (zie cursus)

---

## 7. Gereedschapslijtage en standtijd (Taylor)

### 7.1 Soorten slijtage

| Type | Locatie | Symbool | Typische waarden |
|---|---|---|---|
| **Vrijloopvlakslijtage** | Vrijloopvlak (flank) | VB | 0.3–0.6 mm |
| **Kolkslijtage** (kraterslijtage) | Spaanvlak (rake face) | KT | 40–200 µm |
| **Opbouwsnijkant** (BUE) | Snijkant | — | — |

**Oorzaken slijtage:**
- Mechanische slijtage (abrasie)
- Diffusieprocessen (materiaaluitwisseling op atomair niveau)
- Oxidatieprocessen
- Thermische spanningen (thermoshock)
- Opbouwsnijkant (BUE)

### 7.2 Opbouwsnijkant (BUE — Build-Up Edge)

- **Mechanisme:** zacht, ductiel werkstukmateriaal "last" vast aan de snijkant bij lage snijsnelheden
- Verandert de effectieve snijkantgeometrie → slechtere oppervlaktekwaliteit
- **Vermijden door:**
  - Grotere spaanhoek γ
  - Coating op het gereedschap
  - **Hogere snijsnelheid** (BUE verdwijnt bij hogere temperaturen)
  - Hogere druk van snijvloeistoffen

### 7.3 Slijtageverloop en standtijd

De vrijloopvlakslijtage VB neemt toe met de snijtijd. Er is een **slijtagecriterium** (bijv. VB = 0.3 mm) dat bepaalt wanneer het gereedschap verwisseld of nagescherpt moet worden.

De **standtijd T** [min] is de totale snijtijd waarbij het gereedschap het slijtagecriterium bereikt.

### 7.4 Formule van Taylor

Empirisch verband tussen snijsnelheid v_c en standtijd T:

$$\boxed{v_c \times T^n = C_T}$$

- **n** = Taylor-exponent (materiaalkonstante, afhankelijk van gereedschapsmateriaal)
  - HSS: n ≈ 0.1–0.2
  - HM: n ≈ 0.2–0.4
  - Keramiek: n ≈ 0.4–0.6
- **C_T** = constante (afhankelijk van gereedschaps-/werkstukmateriaal, VB, snededoorsnede)

**Interpretatie:** snijsnelheid v_c verhogen → standtijd T daalt sterk (machtsverband).

> **Voorbeeld:** als n = 0.125 en v_c stijgt met 50%, dan daalt T met factor (1.5)^(1/0.125) = (1.5)^8 ≈ 25 → standtijd wordt ~25× korter!

**Praktische vuistregels standtijd:**
- Draaien: T = 10–20 min
- Frezen: T = 60 min

### 7.5 Veralgemeende wet van Taylor

De eenvoudige Taylor-formule geldt alleen voor constante snededoorsnede. In werkelijkheid verandert C_T met VB, h en b:

$$\boxed{v \cdot T^m = \frac{C_{TVB} \cdot VB^n}{h^p \cdot b^q}}$$

**Richtwaarden constanten:**
- m ≈ 0.25–0.34 (afhankelijk van materiaal en gereedschap)
- n ≈ 0.42–0.47
- p ≈ 0.16–0.26 (invloed van snededikte h)
- q ≈ 0.05–0.1 (invloed van snedebreedte b, vaak verwaarloosbaar)

**Omgeschreven naar instelgrootheden f en a** (met h = f·sinκ en b = a/sinκ):

$$v \cdot T^m = \frac{C_{TVB} \cdot VB^n}{f^p \cdot a^q \cdot (\sin \kappa)^{p-q}}$$

**Invloed van instelhoek κ:** hoe schuiner de snijkant (kleinere κ), hoe groter de standtijd T of hoe hogere snijsnelheid v mogelijk is.

---

## 8. Snijvloeistoffen

### 8.1 Functies

| Functie | Effect |
|---|---|
| **Koelen** | Hogere maatnauwkeurigheid, lagere oppervlakteruwheid |
| **Smeren** | Langere standtijd, hogere snijsnelheid mogelijk, hogere voeding mogelijk, onderdrukken BUE |
| **Spaanafvoer** | Spanen wegspoelen uit de snijzone |

### 8.2 Types snijvloeistoffen

| Type | Eigenschappen | Toepassing |
|---|---|---|
| **Water** | Goede koeling, slechte smering | Bijproduct van emulsies |
| **Snijolie** | Goede smering, matige koeling | Lage snelheden, tappen, boren |
| **Water-olie emulsie** | Combinatie koeling + smering | Meest gebruikt (3–10% olie) |

### 8.3 Aandachtspunten

- **Onderbroken snede** (frezen, boren): opgelet met koeling! Plotselinge koeling bij warme beitel → thermoshock → scheuren in beitel. Ofwel continu koelen ofwel helemaal niet.
- **MQL (Minimum Quantity Lubrication):** minieme hoeveelheid olie verstuiven → milieuvriendelijker

---

## 9. Draaidiagrammen

### 9.1 De draaibank

**Onderdelen:**
- **Vaste kop** — bevat hoofdspil, aandrijving, schakelkasten voor spilsnelheden en voedingen
- **Klauwplaat** — klemming van het werkstuk (3 of 4 kaken)
- **Losse kop** — ondersteuning van het werkstuk + boren
- **Schort** — verbindt sleden met de spindel voor handmatige of automatische voeding
- **Langsslede** — beweging langs de rotatieas (z-richting)
- **Dwarsslede** — beweging loodrecht op de rotatieas (x-richting)
- **Beitelslede** — instelbeweging onder hoek (voor konische oppervlakken)

### 9.2 Kronenberg-diagram

Het **Kronenbergdiagram** toont in dubbellogaritmische schaal hoe snededoorsnede A samenhangt met snijkracht F_c, vermogen P, snijsnelheid v, debiet Q en standtijd T.

**Twee randvoorwaarden om het optimum te vinden:**

1. T = T_e → v_e = v_m (economische standtijd bereikt bij maximale snijsnelheid van machine)
2. P_e = P_m (snijvermogen = machinaal beschikbaar vermogen)

**Werkingspunt:** als A > A_crit (kritische snededoorsnede), kan men van k3 naar k2 verschuiven:
- v_c daalt → T stijgt → minder gereedschapskosten (K_G daalt)
- Debiet Q stijgt → kortere bewerkingstijd → minder bewerkingskosten

### 9.3 TNO-diagram

Het **TNO-diagram** toont voor een gegeven draaistuk (diameter d) het verband tussen voeding f [mm/omw] en:
- Snijkracht F_c [kN]
- Koppel M_c [Nm]
- Maximaal machinevermogen P_max
- Optimale snijsnelheid v_c,opt (= v_e)
- Maximale snijsnelheid v_c,max (= v_m)
- Debiet Q [mm³/s]

**Hoe aflezen:**
- Stel f in op x-as
- Lees F_c en M_c af (blauwe en oranje lijnen)
- Controleer dat P ≤ P_max (rode lijn)
- Lees v_c af (paarse lijn = optimaal, rode lijn = maximum)
- Lees debiet Q af (groen = maximaal, geel = economisch)

---

## 10. Boren

### 10.1 Principe

Bij **gatbewerkingen** (boren, kotteren, ruimen, tappen):
- **Hoofdbeweging:** rotatie van het gereedschap
- **Voedingsbeweging:** translatie langs de rotatieas

### 10.2 Types boren

| Type | Principe |
|---|---|
| **Volboren** | Boor door massief materiaal (geen voorgat nodig) |
| **Kernboren** | Boren met kernboor, laat kern staan (voor grote diameters) |
| **Opboren** | Vergroten van bestaand gat |
| **Verzinken** | Conische of cilindrische verzinking maken |

**Blind gat vs. doorlopend gat:** spaanafvoer is moeilijker bij blind gat. Bij rechte spaangroef: spanen gaan omhoog (moeilijk). Schroefvormige spaangroef helpt spaanafvoer bij blind gat.

**Nauwkeurigheid van boren:** lager dan draaien of ruimen. Voor precisisgaten: eerst boren, dan ruimen.

### 10.3 Boorgeometrie

De spiraalboor heeft dezelfde basishoeken als een draaibeitel, maar met extra complicaties:

```
Boor
├── Spiraalhoek (helix angle) — bepaalt spaanhoek
├── Punthoek (= 2 × κ) — halfpunthoek is de instelhoek
├── Hoofdsnijkanten (2 stuks)
├── Dwarssnijkant (chisel edge) — aan de punt, in het centrum
├── Geleiderand — centreert de boor in het gat
└── Spaangroeven — afvoer van de spanen
```

**Punthoeken voor verschillende materialen:**

| Punthoek | Toepassing |
|---|---|
| 60° | Plastics |
| 90° | Non-ferrometalen en hout |
| 118° | **Staal (algemeen gebruik)** |
| 135° | Harde en taaie materialen |

### 10.4 Variatie van spaanhoek over de diameter

**Aan de omtrek:** de effectieve spaanhoek ≈ spiraalhoek (gunstig, positief)

**Aan de ziel (centrum):** de effectieve spaanhoek wordt sterk **negatief** (tot −56°!) door de kleine omtreksnelheid. De verspaningscondities zijn hier **zeer ongunstig**.

**Spoedhoek σ** bepaalt de relatie tussen omtreksnelheid en voeding:

$$\sigma = \frac{f}{\pi \cdot d}$$

Hoe kleiner d (dichter bij de ziel), hoe groter de relatieve invloed van f op de effectieve hoeken.

### 10.5 Dwarssnijkant en aanpunten

De **dwarssnijkant** (chisel edge) in het centrum van de boor:
- Bijdrage tot **grote snijkrachten** (voedingskracht F_f)
- Klein bijdrage tot het snijmoment
- Functioneert meer als een **duwende** dan snijdende werking

**Aanpunten (web thinning):** de dwarssnijkant inkorten/dunner maken:
- Beperkt de voedingskracht F_f
- Verhoogt de standtijd
- Betere centreernauwkeurigheid

### 10.6 Krachten en vermogen bij boren

| Grootheid | Formule | Vergelijk draaien |
|---|---|---|
| Verspaningsmoment | M_c = C_M × d^x_M × f^y_M | F_c = k_c1.1 × a × f^(1-ε) |
| Verspaningsvermogen | P_c = M_c × ω = M_c × 2π × n | P_c = F_c × v_c |
| Voedingskracht | F_f = C_f × d^x_f × f^y_f | F_f ~ F_c |

Richtwaarden voor constructiestaal: C_f ≈ 1500, x_f ≈ 0.8, y_f ≈ 0.8; C_M ≈ 0.45, x_M ≈ 1.8, y_M ≈ 0.8

### 10.7 Keuze van de voeding f

De voeding f is beperkt door:
- **Maximaal toelaatbaar torsiemoment op de boorziel** (hoofdeis → breukgrens boor)
- Vrijslijphoek (effectieve vrijloophoek moet positief blijven)
- Spaanafvoer
- Vermogen van de boormachine
- Sterkte van het werkstuk en de opspanning
- "Happen van de boor" (bij te grote f springt de boor door)

### 10.8 Boormachines

Types: **tafelboormachine**, **kolomboormachine**, **radiaalboormachine**

**Spilconstructie:** de spil kan axiaal bewegen (voedingsbeweging) terwijl de spilbus stationair blijft.

---

## 11. Frezen

### 11.1 Principe en vergelijking met draaien

| Aspect | Draaien | Frezen |
|---|---|---|
| Hoofdbeweging | Rotatie werkstuk | Rotatie gereedschap |
| Werkstuk | Roteert | Staat stil |
| Snijkanten | Enkelvoudig | Meervoudig (z tanden) |
| Snededikte | Constant | **Varieert** tijdens rotatie |
| Snede | Ononderbroken | **Onderbroken** (intermitterend) |

Bij frezen: **zijdelingse krachten op de spil** → complexe lagering nodig.

### 11.2 Types frezen

| Type | Principe | Toepassing |
|---|---|---|
| **Mantelfrees** | Snijkanten op de mantel | Vlakke oppervlakken loodrecht op het gereedschap |
| **Kopfrees** | Snijkanten op de voorzijde | Vlakke oppervlakken (face milling) |
| **Mantelkopfrees** | Combinatie mantel + kop | Vlakke oppervlakken en schouders |

**Kopfrezen = face milling = rechte vlakken maken**

### 11.3 Meeloop vs. Tegenloop

Dit is een essentieel concept bij het frezen:

| | **Tegenloop** (conventional) | **Meeloop** (climb) |
|---|---|---|
| Rotatie vs. voeding | Tegen elkaar in | In dezelfde richting |
| Spaandikte | Begint dun, eindigt dik | **Begint dik, eindigt dun** |
| Eerste contact | Wrijven, dan snijden | Meteen snijden |
| Oppervlaktekwaliteit | Matig | **Goed** |
| Kracht op werkstuk | Optillen | Vastdrukken |
| Speling in voedingsmechanisme | Niet kritisch | **Speling moet gecompenseerd worden** |
| Voorkeur? | Oudere machines | **Moderne CNC-machines (voorkeur)** |

> **Samenvatting:** meeloop is te verkiezen op moderne machines (goede geleiding, geen speling) omdat de oppervlaktekwaliteit beter is en het werkstuk wordt vastgedrukt.

### 11.4 Krachten bij frezen

De gemiddelde snededikte bij mantelfrezen (tegenloop):

$$h_{gem} = f_z \times \sqrt{\frac{a}{d}}$$

Met f_z = voeding per tand, a = radiële ingrijping, d = freesdiameter.

**Snijkracht per tand:**
$$F_c = k_{c1.1} \times h_{gem}^{(1-\varepsilon)} \times b$$

**Koppel en vermogen:**
$$M_c = F_c \times \frac{d}{2} \times z_i \qquad P_c = F_c \times v_c \times z_i = M_c \times \omega$$

**Debiet:**
$$Q = a \times b \times f_z \times n \times z = a \times b \times v_f$$

### 11.5 Freesgereedschappen

**Mantelfrezen:**
- Zachte materialen → **grote spaangroef** (grote spanen, want zachte materialen geven lange continue spanen)
- Harde materialen → **veel tanden** (krachtvariaties beperken; kleine snededoorsnede per tand)
- Materiaal: HSS of hardmetaal

**Kopfrezen (meskopfrees):**
- Hardmetalen of keramische wisselplaten
- Hoge snijsnelheden mogelijk

### 11.6 Freesmachines

Types:
- **Verticale freesmachine** — spil verticaal (meest gebruikt voor kopfrezen)
- **Horizontale freesmachine** — spil horizontaal (voor mantelfrezen)
- **Vlakfreesmachine** — voor grote vlakken

---

## 12. Economische aspecten en werkvoorbereiding

### 12.1 Veralgemeende Taylor en economische standtijd

De veralgemeende Taylor (zie §7.5) geeft de standtijd als functie van v, f, a.

**Effectieve standtijd:** T = ψ₁(v, f, a | WM, GM, crit, ...) — de werkelijk bereikbare standtijd.

**Economische standtijd** (te kiezen i.f.v. doelstelling):

$$\boxed{T_e = \left(\frac{1}{m} - 1\right) \frac{K_G}{K_U}} \quad \text{(voor minimale kost per stuk)}$$

$$\boxed{T_p = \left(\frac{1}{m} - 1\right) T_{CT}} \quad \text{(voor minimale productietijd)}$$

| Symbool | Betekenis |
|---|---|
| m | Taylor-exponent |
| K_G | Gereedschapskost (aanschaf + wisselkost) per gereedschapsleven |
| K_U | Kost voor bezetten van de machine per tijdseenheid (= K_M + K_L) |
| T_CT | Gereedschapswisseltijd [min] |

> T_e > T_p altijd: minimale kost vereist langere standtijd dan maximale productiviteit.
> Te en Tp zijn lager voor betere gereedschapsmaterialen: hogere snijsnelheden zijn dan economisch.

**Voorbeelden:**

| Bewerking | T_e (min. kost) | T_p (max. prod.) |
|---|---|---|
| Draaien met HSS beitel | 23.3 min | 5.7 min |
| Draaien met gebraseerde HM plaat | 14.7 min | 2.0 min |
| Draaien met indexeerbare HM plaat | 11.1 min | 2.0 min |
| Frezen met HSS profielfrees | 3.6 uur | 1 uur |

### 12.2 Kostenformule

De totale verspaningskost per stuk K_V:

$$\boxed{K_V = t_h \cdot K_U + \frac{t_h}{T} \cdot K_G + t_a \cdot K_U}$$

| Term | Symbool | Betekenis |
|---|---|---|
| Directe verspaningskosten | K_Vh = t_h · K_U | Dalen bij hogere v (kortere hoofdtijd t_h) |
| Gereedschapskosten | K_VG = (t_h/T) · K_G | Stijgen bij hogere v (kortere T) |
| Vaste nevenkosten | K_Va = t_a · K_U | Onafhankelijk van v |

Met:
- t_h = hoofdtijd = eigenlijke verspaningstijd
- t_a = neventijd (opspannen, nameten, ...) — onafhankelijk van snijsnelheid
- T = standtijd gereedschap
- K_U = K_M + K_L (machine + loonkosten per tijdseenheid)
- K_G = gereedschapskost per gereedschapsleven

**Optimale snijsnelheid v_c,opt** ligt in het minimum van de K_V-curve (totale kostenoptimum).

> **Niet-examenleerstof:** berekeningsvoorbeelden voor kosten (§6.4) en wiskundige optimalisatieprocedure (§7.4.4).

### 12.3 Werkvoorbereiding

**Werkvoorbereiding** is het plannen van het productieproces vóór de eigenlijke productie:

```
Input tekening (maten, toleranties)
    ↓
Selectie werkstukmateriaal
    ↓
Identificatie van te bewerken features (vlakken, gaten, profielen)
    ↓
Analyse bewerkingsstappen
    ↓
Selectie bewerkingen per feature (voordraaien, finisseren, slijpen, ...)
    ↓
Selectie gereedschappen per bewerking
    ↓
Bepalen werkstukvolgorde
    ↓
Selectie machines per bewerking
    ↓
Bepalen van snijvoorwaarden (a, f, v)
    ↓
Bepalen opspanningen
    ↓
NC-programmatie / werkkaarten
```

### 12.4 Keuze van snijvoorwaarden (a, f, v)

De keuze van optimale snijvoorwaarden verloopt stapsgewijs:

**Stap 1: Koppel machine- en gereedschapscapaciteit**
- Via Kronenbergdiagram: zoek A_crit, stel T = T_e en P = P_m

**Stap 2: Optimaliseer debiet Q**
- Via TNO-diagram: kies f en v_c

**Stap 3: Corrigeer a op basis van beperkingen**

#### Beperking 1: Toelaatbare kracht

De terugdrukkracht F_p veroorzaakt **doorbuiging** van het werkstuk:

$$y_w = (s_m + s_w) \cdot F_p$$

- s_m = soepelheid machine [µm/N]
- s_w = soepelheid werkstuk [µm/N]

**Soepelheid werkstuk** (opspanning tussen 2 punten):

$$s_w = \frac{y_w}{F_p} = \frac{L^3}{48 \cdot E \cdot I} \qquad \text{met } I = \frac{\pi d^4}{64}$$

**Soepelheid werkstuk** (opspanning in klauwplaat):

$$s_w = \frac{L^3}{3 \cdot E \cdot I}$$

> Opspanning in klauwplaat geeft 16× meer doorbuiging dan tussen 2 punten bij gelijke L!

#### Beperking 2: Oppervlakteruwheid

Het beitelpunt heeft een afronding r_ε. Dit geeft een theoretische ruwheid:

$$R_t = \frac{(f/2)^2}{2 r_\varepsilon} = \frac{f^2}{8 r_\varepsilon}$$

De **maximale voeding** voor een gewenste ruwheid R_t,max:

$$f_{max} = \sqrt{8 \cdot r_\varepsilon \cdot R_{t,max}}$$

> **Praktisch:** de voeding f wordt in de praktijk bijna altijd beperkt door de toelaatbare oppervlakteruwheid, niet door de theoretische optimale waarde uit de kostenformule.

### 12.5 COP — Cutting Optimisation Program

**COP** (Cutting Optimisation Program, ook COPTURN) is een computerprogramma dat:

1. Alle verspaningswetten en beperkingen uitdrukt als functies van b, h, v
2. Een 3D-ruimte (v = f(b,h)) definieert waarbinnen oplossingen liggen
3. Optimaliseert naar minimale kost of maximale productiviteit (Lagrange-methode)

**Invoer:** machine-nr, gereedschap-nr, materiaal-nr, opspandata, werkstukgegevens

**Uitvoer:** lijst van optimale snijvoorwaarden (v_opt, f_opt, a_opt)

---

## 13. Formuleoverzicht

| Formule | Naam | Gebruik |
|---|---|---|
| α + β + γ = 90° | Hoekrelatie gereedschap | Altijd |
| φ = 45° + γ/2 − µ/2 | Afschuifhoek (Merchant) | Spaanvorming |
| A = a·f = b·h | Snededoorsnede | Kienzle |
| b = a/sinκ; h = f·sinκ | Geometrie → instelhoek | Kienzle |
| δ_κ = b/h | Slankheid snede | Spaanvorming (3 < δ < 15 staal) |
| F_c = k_c1.1 · b · h^(1-e) | Kienzle | Snijkracht |
| P_c = F_c · v_c | Snijvermogen | Vermogen |
| v_c · T^n = C_T | Taylor (eenvoudig) | Standtijd |
| v·T^m = C_TVB·VB^n / (h^p·b^q) | Veralgemeende Taylor | Standtijd |
| T_e = (1/m−1)·K_G/K_U | Economische standtijd (min. kost) | Optimalisatie |
| T_p = (1/m−1)·T_CT | Productiviteitsstandtijd | Optimalisatie |
| K_V = t_h·K_U + (t_h/T)·K_G + t_a·K_U | Kostenformule | Economie |
| R_t = f²/(8·r_ε) | Theoretische ruwheid | Oppervlaktekwaliteit |
| y_w = (s_m + s_w)·F_p | Doorbuiging werkstuk | Nauwkeurigheid |
| s_w = L³/(48EI) | Soepelheid (tussen 2 punten) | Doorbuiging |
| s_w = L³/(3EI) | Soepelheid (klauwplaat) | Doorbuiging |

---

## Niet-examenleerstof (expliciet vermeld)

- §4.2 Fysische verspaningswetten (afleiding Merchant-formule)
- Proef van Mathon (§5.6.2.3)
- §6.4 Berekeningsvoorbeelden voor kosten
- §7.4.4 Wiskundige optimalisatieprocedure
- §7.4.5 Toepassing op optimalisatie van snijvoorwaarden

---

---

## Wat je echt moet kennen

- De 6 hoofdgroepen van productietechnieken en waar verspaning onder valt
- Het verschil tussen gecontroleerde en ongecontroleerde snijkantgeometrie
- De drie basishoeken van het gereedschap (α, β, γ) en hun som = 90°
- Wat de spaanhoek γ doet: positief = zachte materialen, negatief = harde materialen
- De drie bewegingen bij verspaning: hoofdsnijbeweging, voedingsbeweging, instelbeweging
- De drie krachten: F_c (tangentieel), F_f (voeding), F_p (terugdruk)
- De formule van Kienzle voor de hoofdsnijkracht: F_c = k_c1.1 × b × h^(1-e)
- De snededoorsnede: A = a × f = b × h, en de relaties via instelhoek κ
- De slankheid δ_κ = b/h en de grenzen (3–15 voor staal)
- De drie soorten spanen: continu, lamel, brokkel — en wanneer elke optreedt
- De twee soorten gereedschapsslijtage: vrijloopvlakslijtage (VB) en kolkslijtage (KT)
- Wat opbouwsnijkant (BUE) is en hoe je het vermijdt
- De formule van Taylor: v_c × T^n = C_T — en wat n betekent voor HSS vs HM vs keramiek
- De hiërarchie van snijmaterialen van goedkoop naar duur/hard
- De ISO-codering van hardmetalen: XX-Y## (type, materiaal, getal)
- Wat het getal in de ISO-code betekent: klein = bros/hard (finisseren), groot = taai (schrobben)
- Wanneer je gecoat HM gebruikt en waarom (taaiheid + slijtvastheid combineren)
- Waarom diamant niet op staal gebruikt mag worden (koolstof lost op in ijzer)
- De functies van snijvloeistoffen: koelen, smeren, spaanafvoer
- Waarom je bij onderbroken snede voorzichtig moet zijn met koeling (thermoshock)
- Het verschil tussen meeloop en tegenloop bij frezen (voorkeur meeloop op CNC)
- Waarom de spaanhoek van een boor sterk negatief wordt aan de ziel
- Wat de dwarssnijkant doet en hoe aanpunten helpt
- De economische standtijd T_e (minimale kost) vs T_p (maximale productiviteit)
- De kostenformule K_V = t_h·K_U + (t_h/T)·K_G + t_a·K_U en de drie termen daarin
- De ruwheidsformule R_t = f²/(8·r_ε) en de maximale voeding hieruit
- Doorbuigingsberekening via soepelheid: y_w = (s_m + s_w)·F_p

---

*Gebaseerd op slides Les 1, 2, 3, 4 en 6 — Productietechnologie H01O1, KU Leuven 2024*
