# Lastechnieken — Productietechnieken en Systemen (H01O1)
**KU Leuven · Arnout Dejans · Semester 6**

---

## Inhoudsopgave

1. [Wat is lassen?](#1-wat-is-lassen)
2. [Onderverdeling lasprocessen](#2-onderverdeling-lasprocessen)
3. [Smeltlassen](#3-smeltlassen)
   - [BMBE — Booglassen met beklede elektrode](#31-bmbe--booglassen-met-beklede-elektrode)
   - [MIG/MAG-lassen](#32-migmag-lassen)
   - [TIG-lassen](#33-tig-lassen)
   - [OP-lassen — Onder poederdek lassen](#34-op-lassen--onder-poederdek-lassen)
   - [Autogeen lassen](#35-autogeen-lassen)
4. [Druklassen](#4-druklassen)
   - [Puntlassen (weerstandslassen)](#41-puntlassen-weerstandslassen)
   - [Rolnaadlassen](#42-rolnaadlassen)
   - [Weerstandstomplassen](#43-weerstandstomplassen)
   - [Afbrandstuiklassen](#44-afbrandstuiklassen)
   - [Projectielassen](#45-projectielassen)
5. [Lasposities](#5-lasposities)
6. [Kwaliteit van lasverbindingen — overzicht](#6-kwaliteit-van-lasverbindingen--overzicht)
7. [Imperfecties in lasverbindingen](#7-imperfecties-in-lasverbindingen)
8. [Kwaliteit bij ontwerp — dimensionering](#8-kwaliteit-bij-ontwerp--dimensionering)
9. [Kwaliteit bij aankoop van materiaal](#9-kwaliteit-bij-aankoop-van-materiaal)
10. [Lasnaadvoorbereiding en lasnaadvormen](#10-lasnaadvoorbereiding-en-lasnaadvormen)
11. [Formuleoverzicht](#11-formuleoverzicht)

---

## 1. Wat is lassen?

**Definitie:**
> Het **verbinden** van materialen door middel van **druk en/of warmte**, waarbij het materiaal op de verbindingsplaats in **vloeibare of deegachtige toestand** wordt gebracht, terwijl al of niet materiaal met ongeveer dezelfde **samenstelling** wordt toegevoegd, waarbij **continuïteit** ontstaat tussen de te verbinden delen.

Het doel is een **homogene** verbinding op vlak van:
- Samenstelling
- Metallurgische structuur
- Mechanische eigenschappen

Dit is in de praktijk **niet altijd volledig haalbaar** — de warmte-inbreng wijzigt de microstructuur in de zone naast de las (de **HAZ**: Heat-Affected Zone). Dit is een belangrijk aandachtspunt bij sterkte-berekeningen en materiaalkeuze.

### Anatomie van een lasverbinding

```
┌─────────────────────────────────────────────────────────┐
│  Base metal │   HAZ   │  Las (filler)  │   HAZ   │ Base metal │
│             │         │                │         │            │
│         Fusion line               Fusion line               │
│                    ← seam preparation →                    │
└─────────────────────────────────────────────────────────┘
```

- **Base metal (BM):** Basismateriaal — ongewijzigde microstructuur
- **HAZ (Heat-Affected Zone):** Warmte-beïnvloede zone — microstructuur gewijzigd door warmte, maar nooit gesmolten
- **Fusion line:** Grens tussen vloeibaar en vast materiaal
- **Filler material:** Lasmetaal dat werd toegevoegd

### Wat is brazeren?

Bij **brazeren** smelt het **toevoegmateriaal** maar het **basismateriaal niet**. Het toevoegmateriaal vloeit door capillaire werking in de naad. Het basismateriaal blijft vast — dit onderscheidt brazeren van lassen.

---

## 2. Onderverdeling lasprocessen

```
LASSEN
├── Smeltlassen
│   ├── Elektrisch (booglassen)
│   │   ├── BMBE (beklede elektrode)
│   │   ├── MIG/MAG
│   │   ├── TIG
│   │   ├── OP-lassen (onder poederdek)
│   │   └── Plasmалassen
│   ├── Thermo-chemisch
│   │   └── Autogeen lassen (zuurstof-acetyleen)
│   └── Straling
│       └── Laserlassen, elektronenstraalslassen
└── Druklassen
    ├── Weerstandslassen
    │   ├── Puntlassen
    │   ├── Rolnaadlassen
    │   ├── Weerstandstomplassen
    │   ├── Afbrandstuiklassen
    │   └── Projectielassen
    └── Wrijvingslassen
```

---

## 3. Smeltlassen

Bij smeltlassen wordt het materiaal op de verbindingsplaats plaatselijk gesmolten, al dan niet met toevoeging van vulmateriaal. De warmtebron is elektrisch (boog), chemisch (vlam) of straling (laser).

### 3.1 BMBE — Booglassen met beklede elektrode

**Principe:** Een afsmeltende elektrode (kern + bekleding) wekt een elektrische boog op tussen elektrode en werkstuk. De boog smelt zowel de kern als het basismateriaal. De bekleding beschermt het smeltbad.

**Stroombron:** **CC-bron** (Constant Current = dalende karakteristiek)
- De spanning varieert sterk met de booglengte, de stroom blijft nagenoeg constant.
- Dit maakt de boog stabiel: als de booglengte wijzigt, compenseert de spanning automatisch.

**Elektrodeafmetingen:**
- Kern: 300–500 mm lang, ⌀ 1,6–6 mm
- Kern is altijd een metaallegering; de bekleding bepaalt de laseigenschappen

**Functies van de bekleding:**

| Functie | Mechanisme |
|---|---|
| Richten van de boog | Kelkvorming aan het tipje |
| Stabiele boog | Creëren van een geleidende atmosfeer (ionen) |
| Bescherming tegen oxidatie | Gas vrijmaken tijdens verbranding bekleding |
| Bescherming druppels tijdens transfer | Druppel omhullen in slaklaag |
| Bescherming stolled lasmetaal | Slaklaag over de koelende las |
| Ondersteuning lasmetaal | Slak ondersteunt smeltbad (positie lassen) |
| Legeren lasmetaal | Metaalelektroden voegen legeringselementen toe |

**Types bekleding:**

| Type | Eigenschappen | Aandacht |
|---|---|---|
| **Rutiel** | Goede aanvloeiing, weinig spatten, zachte boog, alle posities, goede sterkte | Meest courant |
| **Basisch** | Laag waterstofgehalte → minder koudscheuren | Grof uiterlijk, moeilijk te verwijderen slak |
| **Cellulose** | Hoge lassnelheid, alle posities, diepe inbranding | Hoog waterstofgehalte → gevaar voor koudscheuren |

**Polariteit en stroom:** afhankelijk van bekleding, positie, basismateriaal, en plaatdikte.

---

### 3.2 MIG/MAG-lassen

**MIG** = Metal **Inert** Gas (edelgas: Ar, He) — voor aluminium, RVS  
**MAG** = Metal **Active** Gas (reactief gas: CO₂, mengsels) — voor staal

**Principe:** Een continu-aangedreven draad dient als afsmeltende elektrode én als toevoegmateriaal. Het smeltbad wordt beschermd door een gasstroom uit het mondstuk.

**Stroombron:** **CV-bron** (Constant Voltage = vlakke karakteristiek)
- Bij verandering van booglengte wijzigt de stroom sterk → draad smelt sneller/trager → zelfregulering booglengte.

**Draadeigenschappen:**
- Dikte: 0,8 – 1 – 1,2 mm (massief of gevuld)
- Stalen draad steeds **verkoperd**: goede elektrische geleiding én bescherming tegen corrosie
- Gevulde draad: uitstekend voor positielassen
- **Draad steeds aan de positieve pool** (meer afsmeltenergie)

**Beschermgassen:**

| Gas | Toepassing |
|---|---|
| Argon (Ar) | Inert, voor aluminium en RVS (MIG) |
| CO₂ | Actief, voor staal (MAG) — goedkoop, diepe inbranding |
| Ar + CO₂ mengsels | Compromis: betere boogstabiliteit dan zuiver CO₂ |
| Helium (He) | Hogere energie-inbreng, duurder |

**Druppelovergang** (transfer van draad naar smeltbad):

Er zijn 4 krachten die de druppelovergang bepalen:
1. **Zwaartekracht** — enkel in flat positie gunstig
2. **Lorenz-kracht** (elektromagnetisch) — drijft druppel af van de draad
3. **Oppervlaktespanning** — houdt druppel vast aan de draad, tot hij groot genoeg is
4. **Kracht door plasmastroming** — gas sleurt druppel mee

**Types druppelovergang:**

| Type | Stroom | Kenmerken |
|---|---|---|
| Short Circuit Transfer | Laag | Druppel raakt smeltbad aan → kortsluiting → druppel losgemaakt |
| Globular Transfer | Matig | Grote druppels, onregelmatig, spatten |
| Spray Transfer | Hoog | Kleine druppels, vloeiend, weinig spatten — gunstig |
| Pulse Spray Transfer | Gepulst | Gecontroleerde spray in alle posities — modern |

---

### 3.3 TIG-lassen

**TIG** = Tungsten Inert Gas

**Principe:** Een **niet-afsmeltende wolframelektrode** wekt de boog op. Het toevoegmateriaal wordt als staaf apart ingevoerd. Het smeltbad is volledig beschermd door inert gas.

**Kenmerken:**
- Wolframelektrode: **niet** afsmeltend → blijft intact
- Toevoegmateriaal: staafvorm, 1000 mm lang, ⌀ 1,6–2 mm
- Kan ook **zonder toevoegmateriaal** op dunne plaat
- Gas: **steeds inert** (Ar of He) — actief gas zou de wolframelektrode aantasten
- **Wolfram steeds aan de negatieve pool** — anders smelt de elektrode zelf (omgekeerde polariteit geeft 3× hogere elektrodetemperatuur)

**Toepassingen:**
- Hoge laskwaliteit vereist (lucht- en ruimtevaart, voedingsindustrie, drukhouders)
- Dunne platen
- Wurzellas bij meerdere lagen

---

### 3.4 OP-lassen — Onder poederdek lassen

**Principe:** Een draadelektrode (of strip) smelt onder een laag van korrelig **flux** (poeder). De boog en het smeltbad zijn volledig bedekt — niet zichtbaar, geen straling.

**Kenmerken:**
- Afsmeltende draad of strip (eventueel gevuld)
- Draaddikte: 3 mm en meer (veel hogere stroomsterktes dan MIG/MAG)
- CC of CV-regeling
- Flux beschermt lasbad én de boog → geen beschermgas nodig
- Sterk geautomatiseerd: geschikt voor lange rechte lassen (buizen, platen, profielen)
- Hoge lasneersmeltsnelheid → economisch voor grote volumes lasmetaal
- Kan ook gebruikt worden voor het aanbrengen van **deklagen** (surfacing/cladding)

---

### 3.5 Autogeen lassen

**Principe:** Een **mengsel van zuurstof en een brandgas** (meestal acetyleen: C₂H₂) brandt en levert de warmte. De verbrandingsproducten fungeren ook als schermgas.

**Vlaminstellingen:**

| Vlamtype | Samenstelling | Toepassing |
|---|---|---|
| **Neutraal** | O₂/C₂H₂ ≈ 1:1 | Staal en RVS lassen |
| **Oxiderend** | Overschot O₂ | Messing lassen |
| **Reducerend** (carburerend) | Overschot C₂H₂ | Hoog-koolstofstaal lassen |

**Toevoegmateriaal:** optioneel — staafvorm of geen.

**Nadelen:** Langzaam, grote warmte-inbreng → brede HAZ, grotere kans op vervorming. Nauwelijks nog industrieel gebruikt voor lassen, wel voor snijden (zuurstofsnijden).

---

## 4. Druklassen

Bij druklassen wordt de verbinding tot stand gebracht door **druk**, al dan niet in combinatie met warmte. Er is **geen smeltbad** zoals bij smeltlassen — het materiaal blijft vast of wordt plastisch vervormd.

### 4.1 Puntlassen (weerstandslassen)

**Principe:** Twee elektroden klemmen de werkstukken samen. Een korte krachtige stroompuls (wisselstroom of gelijkstroom) verhit het materiaal plaatselijk door **weerstandsverwarming** (Joule-effect). De smeltzone (laslens) stolt onder druk.

$$Q = I^2 \cdot R \cdot t$$

**Procesparameters:**
- **Stroomsterkte** (kA-klasse)
- **Lastijd** (ms tot s)
- **Elektrodekracht** (kN)
- Stroomdichtheid: ≈ 0,5 kA/mm²

**Laslensgrootte:**

$$d_{\text{lens}} = 4\sqrt{t}$$

waarbij $t$ de plaatdikte is (in mm). De laslens is nooit groter dan de elektrode-diameter.

**Weerstandsverdeling tijdens het lassen:**
In de beginfase is de contactweerstand tussen de twee werkstukken het grootst → warmte ontstaat juist daar waar de las moet komen. Naarmate de temperatuur stijgt, neemt de weerstand af en neemt de volumieke weerstand van het materiaal over.

**Toepassingen:** automotive (plaatdelen, karrosseriedelen), elektronica, dunne platen.

---

### 4.2 Rolnaadlassen

Variante van puntlassen waarbij de elektroden **rollen** zijn. De platen worden continu door de rollende elektroden gevoerd. Zo ontstaat een **aaneengesloten las** (naad) in plaats van losse punten. Toepassing: benzinereservoirs, conservenblikken.

---

### 4.3 Weerstandstomplassen

**Principe:** De uiteinden van twee stukken worden tegenover elkaar gezet en de stroom loopt axiaal door beide stukken. De contactweerstand verwarmt de aanrakingsvlakken → zachte deformatie onder druk → verbinding.

**Kenmerken:**
- Stomplas (butt joint)
- Voorbereiding: parallelle, vlakke, schone oppervlakken
- Toepassingsgebied staal: ⌀ 0,5–30 mm, max. 600 mm²
- Aluminium: kleinere afmetingen (oxidehuid problematisch)

---

### 4.4 Afbrandstuiklassen

Variant van weerstandstomplassen. De twee stukken worden kortsluitend in contact gebracht zodat er **kleine boogontladingen** (flashing) optreden aan het oppervlak. Door de intense lokale verhitting verbrandt het oppervlak weg. Daarna volgt een krachtige stomp die het gesmolten en geoxideerd materiaal naar buiten perst.

**Voordeel:** Voorbereiding minder kritisch dan bij weerstandstomplassen (ruwe zaagsnede volstaat).  
**Toepassingsgebied staal:** ⌀ 1,5–300 mm, max. 100.000 mm².

---

### 4.5 Projectielassen

**Principe:** De werkstukken worden samengelegd. Op het ene werkstuk zijn **uitstulpingen** (projectielen) aangebracht. Stroom loopt geconcentreerd door de uitstulpingen → lokale verhitting → druk versmelt de uitstulpingen → lasverbinding op meerdere punten tegelijk.

**Toepassing:** Moeren en bouten aan plaatwerk; massa-assemblage in automotive.

---

## 5. Lasposities

De laspositie beïnvloedt het proces en de toegelaten parameters sterk. Standaard ISO-aanduidingen:

| Code | Positie |
|---|---|
| PA | Vlak (flat) — smeltbad rust op de las |
| PB | Hoeklas horizontaal |
| PC | Horizontaal (dwarslassen op verticale plaat) |
| PD | Hoeklas boven het hoofd |
| PE | Boven het hoofd (overhead) |
| PF | Verticaal omhoog |
| PG | Verticaal omlaag |

**Gevolgen voor het proces:**
- In PA-positie is de zwaartekracht gunstig: het smeltbad blijft op zijn plaats.
- In PE-positie (boven het hoofd) is de zwaartekracht ongunstig: het smeltbad dreigt te vallen.
- Niet alle processen zijn in alle posities toepasbaar. Cellulose- en rutielelektroden voor BMBE zijn positie-onafhankelijk; basische elektroden minder.
- Gevulde draad bij MIG/MAG geeft betere positie-eigenschappen dan massieve draad.

---

## 6. Kwaliteit van lasverbindingen — overzicht

**Lassen is een "speciaal proces"** — de kwaliteit van een las kan **niet uitsluitend door een controle achteraf** worden vastgesteld. Inwendige fouten zijn vaak onzichtbaar. Kwaliteitsopvolging moet op meerdere niveaus georganiseerd worden:

| Niveau | Voorbeelden |
|---|---|
| **Tijdens het ontwerp** | Lasnaadvoorbereiding, dimensionering |
| **Bij aankoop van materiaal** | Materiaalcertificaat (CE, Z-kwaliteit, onzuiverheden) |
| **Kunde van de lasser** | Lasserscertificaat (EN 9606) |
| **Kwalificatie van het lasproces** | Procedurekwalificatie (WPQR/WPS) |
| **Opvolging tijdens het lassen** | Procesmonitoring (stroom, spanning, snelheid) |
| **NDO na het lassen** | Ultrasoon, radiografie, magnetisch poeder, vloeistofpenetratie |

---

## 7. Imperfecties in lasverbindingen

### Imperfecties vs. defecten

- **Imperfectie ≠ defect**: een imperfectie is een afwijking van de norm. Een defect is een imperfectie die de aanvaardbaarheidsgrenzen overschrijdt.
- Imperfecties zijn **in bepaalde mate toegelaten**, afhankelijk van het **kwaliteitsniveau** (B, C of D volgens ISO 5817).

### Classificatie van imperfecties

**Naar scherpte (belang voor vermoeiing):**
- **Scherpe** imperfecties (bv. scheuren, lack of fusion): extreme spanningsconcentratie → gevaarlijkst
- **Ronde** imperfecties (bv. poriën, insluitsels): minder gevaarlijk

**Naar geometrie (detectie):**
- **Vlakke** imperfecties: liggen in een vlak — moeilijker te detecteren met ultrasoon
- **Volumetrische** imperfecties: hebben een zeker volume — gemakkelijker te detecteren

### Overzicht van typische imperfecties (ISO 5817)

| Imperfectie | Beschrijving | Toelaatbaarheid |
|---|---|---|
| **Crack / scheur** | Breuk in las of HAZ | Nooit toegelaten (niveau B, C, D) |
| **Porie** | Gasinsluiting in lasmetaal | Beperkt toegelaten |
| **Lack of fusion** | Onvolledige samensmelting wand of tussenlagen | Niet toegelaten in B/C |
| **Lack of penetration** | Onvolledige doorbranding wortel | Beperkt toegelaten in D |
| **Undercut** | Sleufje in basismateriaal naast la | Beperkt toegelaten (vloeiende overgang vereist) |
| **Overlap** | Las vloeit over basismateriaal zonder samensmelting | Niet toegelaten |
| **Spatter** | Opgespat materiaal rondom de las | Toegelaten in D, beperkt in C/B |
| **Stray arc** | Onbedoelde boogindruk op werkstuk | Niet toegelaten in B/C |
| **Crater crack** | Kratercrack aan het einde van de las | Niet toegelaten |
| **Sagging** | Doorhangen van lasmetaal | Beperkt |

### Undercut — nader bekeken

**Undercut** = de rand van het basismateriaal naast de las is meeomgesmolten, waardoor een langwerpige groef overblijft.
- Scherpe onvolmaaktheid → spanningsconcentratie → gevaarlijk bij vermoeiingsbelasting
- Sterk procesafhankelijk (te hoge stroom, verkeerde hoek) en operatorafhankelijk

### Scheuren — types

```
Las-dwarsdoorsnede (scheurtypes genummerd):
1) Crater crack         — in de kratervulling achteraan de las
2) Transverse crack (weld) — dwars door het lasmetaal
3) Transverse crack (HAZ)  — dwars door de HAZ
4) Longitudinal crack (weld) — langs het lasmetaal
5) Cold crack (HAZ)         — koud scheur in de HAZ
6) Lack of fusion           — onvolledige samensmelting
7) Root crack               — scheuren in de wortel
8) Edge crack               — langs de rand
```

**Koud-** vs. **warmscheuren** — zie sectie 9.

---

## 8. Kwaliteit bij ontwerp — dimensionering

### Warmte-beïnvloede zone en microstructuur

Bij smeltlassen doorloopt het materiaal nabij de las **een thermische cyclus** (opwarming tot hoge temperatuur, snelle afkoeling). Op het Fe-C diagram is te zien welke zones van de HAZ welke temperatuur bereikten:

| Zone | Piektemperatuur | Microstructuureffect |
|---|---|---|
| **Weld Metal** | > T_liquidus | Gestold lasmetaal — nieuwe korrels |
| **CGHAZ** (Coarse Grain HAZ) | ~1200–1500 °C | Sterke korrelgroei → verminderde taaiheid |
| **FGHAZ** (Fine Grain HAZ) | ~900–1100 °C | Fijne korrels → goede eigenschappen |
| **ICHAZ** (Intercritical HAZ) | ~730–900 °C | Gedeeltelijk getransformeerd |
| **SC HAZ** (Subcritical HAZ) | < ~730 °C | Aangelaten/teruggehard |
| **BM** (Base Metal) | kamertemperatuur | Niet beïnvloed |

### Invloed op sterkte: materiaalafhankelijk

**S235 – S460 (laag koolstofstaal, warmgewalst):**
- Sterkte bepaald door chemische samenstelling → niet beïnvloed door lassen
- Geen verlies in sterkte in las of HAZ verondersteld → **geen reductiefactor**

**S690+ (hoog-sterk staal, thermomechanisch gewalst of QT):**
- Sterkte bepaald door harden, ontlaten, korrelverfijning → **microstructuur wordt tenietgedaan door laswarmt**
- Verschillende eigenschappen in BM / WBZ / las → rekening mee houden in ontwerp

**Aluminium:**
- Sterkte bepaald door koudvervorming (werkverharding) of precipitatieharden
- Beide mechanismen worden **tenietgedaan door laswarmt** → sterkteverlies in HAZ
- Ongelijksoortig toevoegmateriaal vaak vereist
- **Reductiefactoren** (HAZ-factor) uit norm EN 1999-1-1 toepassen

### Berekening stompe lasverbinding (butt weld)

Bij **S235** en gelijkaardig staal: dezelfde sterkte als basismateriaal verondersteld → geen aparte controle van de las vereist.

Bij **aluminium**: sterkteverlies in HAZ → reductiefactoren toepassen. De effectieve dikte van de HAZ (b₀,₂) en de HAZ-factor (ρ_haz) uit de norm bepalen de berekende sterkte.

**Onderscheid stomp vs. niet-stomp:**
- **Stomp** = de lasverbinding vult de volledige dwarsdoorsnede
- **Niet-stomp** = de las is kleiner dan de dwarsdoorsnede

### Berekening hoeklasverbinding (statisch)

Bij een hoeklas wordt de doorsnede bepaald door de **keelhoogte** $a$ (inclusief inbranding). Alle spanningen worden berekend en beoordeeld in het **keelvlak**.

**Aandachtspunt:** De hoeklas kan convex, vlak of concaaf zijn → de keelhoogte $a$ varieert.

**Ontwerpformules (Eurocode 3 / EN 1993-1-8):**

$$\sqrt{\sigma_\perp^2 + 3\left(\tau_\parallel^2 + \tau_\perp^2\right)} \leq \frac{f_u}{\beta \cdot \gamma_{M2}}$$

$$\sigma_\perp \leq \frac{0{,}9 \cdot f_u}{\gamma_{M2}}$$

Waarbij:
- $\sigma_\perp$ = normale spanning loodrecht op het keelvlak
- $\tau_\parallel$ = schuifspanning parallel aan de las
- $\tau_\perp$ = schuifspanning loodrecht op de las
- $f_u$ = treksterkte basismateriaal
- $\beta$ = correlatiefactor (materiaalafhankelijk)
- $\gamma_{M2}$ = veiligheidscoëfficiënt (= 1,25)

---

## 9. Kwaliteit bij aankoop van materiaal

De aankoop van het juiste materiaal is cruciaal. Drie parameters verdienen bijzondere aandacht:

### 9.1 Koolstofequivalent (CE) — koudscheuren

Het **koolstofequivalent** is een maat voor de neiging van een staal tot martensietvorming tijdens het afkoelen na het lassen. Hoe meer martensite, hoe harder en brozer het materiaal — en hoe groter het risico op **koudscheuren**.

$$CE_{IIW} = C + \frac{Mn}{6} + \frac{Cr + Mo + V}{5} + \frac{Ni + Cu}{15}$$

| CE | Risico | Maatregel |
|---|---|---|
| CE < 0,4 | Amper kans op koudscheuren | Geen speciale maatregelen |
| CE > 0,4 | Risico op koudscheuren | Voorverwarmen, laagtemperdraad, waterstofarm lassen |

**Koudscheuren:**
- Ontstaan **na** het lassen (uren tot dagen later)
- Gelokaliseerd in de **HAZ** (hoge hardheid, lage vervormbaarheid)
- Oorzaken: hoge hardheid (martensite) + waterstof + restspanningen
- Voorkomen: **laagwaterstof-elektrodes** (basisch), **voorverwarmen** (vertraagt afkoeling)

### 9.2 Onzuiverheden S en P — warmscheuren

**Zwavel (S) en fosfor (P)** vormen **laagsmeltende fasen** in staal. Deze worden tijdens de stolling naar de korrelgrenzen gestoten (segregatie) en veroorzaken bij afkoeling **warmscheuren** (solidification cracking).

**Warmscheuren:**
- Ontstaan **tijdens** of vlak na het lassen, terwijl het metaal nog in deegachtige toestand is
- In het **lasmetaal** (niet in de HAZ) — het smeltbad stolt van buiten naar binnen
- Factoren:
  1. Samenstelling van het lasmetaal (FM + BM)
  2. Stollingsgedrag van het smeltbad (dendrieten)
  3. Spanningen op het werkstuk (hoe meer ingeklemd, hoe groter het risico)

### 9.3 Z-kwaliteit — lamellaire scheuren

**Z-kwaliteit** is een maat voor de gevoeligheid van een gewalst staal voor **lamellaire scheuren**.

**Mechanisme:**
Bij het walsen worden **MnS-insluitsels** uitgerokken in de plaat (in de walsrichting). Wanneer spanningen loodrecht op de plaat optreden (bv. bij een T-lasverbinding die krimpt), kunnen deze MnS-insluitsels bezwijken → **lamellaire scheur**.

**Kenmerken van lamellaire scheuren:**
- "Getrapte" scheurpatronen: horizontale scheuren verbonden door verticale
- Parallel aan de plaat en de fusielijn, buiten de WBZ
- Vezelachtig (fibrous) uiterlijk op het breukvlak

**5 factoren die het risico bepalen (Z-klasse vereist):**

| Factor | Effect |
|---|---|
| Materiaaldikte | Dikkere plaat = minder flexibel = hogere spanningen |
| Lashoogte | Grotere las = meer krimpspanningen in de plaat |
| Geometrie en positie | Spanningen loodrecht op de plaat zijn gevaarlijker |
| Starheid (inklemming) | Verhinderde krimp = hogere spanning |
| Voorverwarmen | Vertraagt afkoeling → lagere krimpspanningen |

**Z-kwaliteit** wordt gemeten via een trekproef in de diktererichting (Z-richting). Garantiewaarden: Z15, Z25, Z35 (reductiemaat in doorsnede bij breuk).

### 9.4 Materiaalcertificaat

Al de bovenstaande parameters (CE, S, P, Z-kwaliteit, mechanische eigenschappen) worden vermeld op een **materiaalcertificaat** (EN 10204 type 3.1). Binnen één "staalkwaliteit" (bv. S355) kunnen nog sterke verschillen bestaan — het certificaat geeft de exacte smeltanalyse van de geleverde charge.

---

## 10. Lasnaadvoorbereiding en lasnaadvormen

### Definitie en doel

**Lasnaadvoorbereiding** = de lasnaadvorm van de doorsnede van de lasnaad + reinigen, verwijderen van oxides, ontbramen, positioneren van werkstukken.

**Doel:** het behalen van de vereisten op vlak van **sterkte, metallurgie en economie**.

### Lasnaadvormen

| Naadvorm | Symbool | Toepassing |
|---|---|---|
| I-naad (Square seam) | ‖ | Dunne platen, enkelvoudige doorgang |
| V-naad (Vee seam) | V | Eenzijdige toegang, middelgrote diktes |
| Bevel-naad (halve V) | / | Eenzijdige toegang, T-verbinding |
| U-naad | U | Grotere diktes, minder lasvolume dan V |
| X-naad (Double V) | X | Tweezijdige toegang, dikke platen |
| K-naad (Double bevel) | K | Tweezijdige T-verbinding |
| Y-naad en dubbele Y | Y | Varianten met smalle opening onderaan |

**Verbindingstypes:**
- **Stompe las (butt weld):** I, V, U, X, K, Y-naden
- **Hoeklas (fillet weld):** geen naadvoorbereiding, maar let op: keelhoogte $a$
- **Overlapverbinding**

### Factoren bij het ontwerp van een lasnaad

**1. Lasproces:**
- Maximale inbranding verschilt per proces: EB-lassen > OP > BMBE > TIG/MIG
- Geometrie van de lastoorts beperkt de toegankelijkheid (bv. TIG-toorts voor nauwe U-naad)
- MIG/MAG: grotere kans op bindingsfouten langs de wanden bij nauwe naden

**2. Plaatdikte:**
- Dunne platen: I-naad zonder voorbereiding
- Toenemende dikte: V → U → X-naad (U-naad heeft minder lasvolume dan V voor dezelfde dikte)
- Economie: volume lasmetaal × prijs + voorbereidingstijd

**3. Materiaal — openingshoek:**
| Materiaal | Openingshoek |
|---|---|
| Staal | 60° |
| Roestvrij staal | 70° |
| Aluminium, Nikkel | 80°–90° |

Bredere hoek bij aluminium en nikkel vanwege hogere viscositeit van het smeltbad.

**4. Bereikbaarheid:**
- Tweezijdige toegang → X- of K-naad → minder lasmetaal, minder vervorming
- Eénzijdige toegang → V-naad; wortellas dan via backing of tweede zijde slijpen en teruglassen
- Gesloten constructies: tweezijdig lassen onmogelijk → corrosie-aandachtspunt aan de binnenzijde

**5. Soort verbinding:**
- Volledige doorlassing (full penetration) vereist bij dynamische belasting en vermoeiingsgevoelige constructies
- Gedeeltelijke doorlassing (partial penetration) voor statisch belaste constructies

**Principe:** *De beste las is geen las* — ontwerp constructies zo dat lassen wordt vermeden of geminimaliseerd.

---

## 11. Formuleoverzicht

| Formule | Symbolen | Toepassing |
|---|---|---|
| $CE_{IIW} = C + \dfrac{Mn}{6} + \dfrac{Cr+Mo+V}{5} + \dfrac{Ni+Cu}{15}$ | CE = koolstofequivalent | Koudscheurisico |
| CE < 0,4 → geen koudscheuren | — | Grens koudscheuren |
| $d_{lens} = 4\sqrt{t}$ | t = plaatdikte [mm] | Laslensgrootte puntlassen |
| $Q = I^2 \cdot R \cdot t$ | I [A], R [Ω], t [s] | Warmteontwikkeling weerstandslassen |
| $\sqrt{\sigma_\perp^2 + 3(\tau_\parallel^2 + \tau_\perp^2)} \leq \dfrac{f_u}{\beta \cdot \gamma_{M2}}$ | σ [N/mm²], f_u = treksterkte | Hoeklas sterktecondite (EC3) |
| $\sigma_\perp \leq \dfrac{0{,}9 \cdot f_u}{\gamma_{M2}}$ | γ_M2 = 1,25 | Aanvullende hoeklas-conditie |

---

---

## Wat je echt moet kennen

- Het verschil tussen lassen en brazeren (basismateriaal smelt wel/niet mee)
- De anatomie van een lasverbinding: BM, HAZ, fusielijn, lasmetaal
- Het onderscheid tussen smeltlassen en druklassen
- Het principe van BMBE: CC-bron, bekleding, functies van de slaklaag
- De drie typen bekleding (rutiel, basisch, cellulose) en wanneer elk gebruikt wordt
- Het verschil tussen MIG en MAG (inert vs actief gas, toepassingen)
- Waarom MIG/MAG een CV-bron gebruikt (zelfregeling booglengte)
- De vier types druppelovergang bij MIG/MAG en bij welke stroom elk optreedt
- Het principe van TIG: niet-afsmeltende wolframelektrode, altijd inert gas
- Waarom wolfram aan de negatieve pool hangt bij TIG
- Het principe van puntlassen: Q = I²·R·t, laslensgrootte d = 4√t
- Wat de vier lasposities (PA, PB, PE, PF/PG) inhouden en wat de gevolgen zijn
- Het verschil tussen imperfectie en defect (en de kwaliteitsniveaus B, C, D)
- De gevaarlijkste imperfecties: scheuren en lack of fusion (scherp = spanningsconcentratie)
- Wat undercut is en waarom het gevaarlijk is bij vermoeiingsbelasting
- De HAZ-zones (CGHAZ, FGHAZ, ICHAZ) en welke het slechtste is (CGHAZ)
- Waarom hoog-sterk staal (S690+) en aluminium extra aandacht vragen bij lassen
- De sterktecondities voor een hoeklas (Eurocode 3 formules kennen/lezen)
- Het koolstofequivalent CE_IIW: formule, grenswaarde (0.4) en gevolg (koudscheuren)
- Het verschil tussen koudscheuren en warmscheuren (wanneer, waar, oorzaken)
- Wat lamellaire scheuren zijn en hoe Z-kwaliteit ze voorkomt
- De vijf factoren die het risico op lamellaire scheuren bepalen
- De keuze van lasnaadvorm in functie van plaatdikte, bereikbaarheid en lasproces
- Waarom de openingshoek breder is voor aluminium dan voor staal

---

*Bestand gegenereerd op basis van slides: "Inleiding lastechnieken 2025b" en "Les 5 Lastechnieken (2026)" — Arnout Dejans, KU Leuven*
