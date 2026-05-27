# Les 14 — Fysische en chemische afnemende bewerkingen
**KU Leuven · Productietechnieken en Systemen · Prof. Sylvie Castagne**

---

## Inhoudsopgave

1. [Inleiding: waarom niet-conventionele processen?](#1-inleiding-waarom-niet-conventionele-processen)
2. [Overzicht van alle niet-conventionele methoden](#2-overzicht-van-alle-niet-conventionele-methoden)
3. [Mechanische bewerkingen (abrasieve methodes)](#3-mechanische-bewerkingen-abrasieve-methodes)
4. [Elektrothermische bewerkingen: EDM (vonkerosie)](#4-elektrothermische-bewerkingen-edm-vonkerosie)
5. [Andere elektrothermische methoden](#5-andere-elektrothermische-methoden)
6. [Elektrochemische bewerkingen (ECM)](#6-elektrochemische-bewerkingen-ecm)
7. [USP-laserbewerking (ultrakorte-puls-laser)](#7-usp-laserbewerking-ultrakorte-puls-laser)
8. [Vergelijking van alle methoden](#8-vergelijking-van-alle-methoden)
9. [Belangrijke begrippen](#9-belangrijke-begrippen)

---

## 1. Inleiding: waarom niet-conventionele processen?

Conventionele bewerkingen zoals frezen, draaien en boren werken altijd via **direct mechanisch contact**: het gereedschap is harder dan het werkstuk en slijt het materiaal weg door kracht. Dat werkt prima voor staal en aluminium, maar stuit op grenzen zodra je:

- **harde of brosse materialen** wil bewerken, zoals keramiek, composieten of gehard staal — het gereedschap kan ze niet aanpakken zonder zichzelf te beschadigen
- **extreem kleine toleranties** nodig hebt, zoals bij microcomponenten
- **oppervlakteschade wil vermijden** — de mechanische spanningen die bij conventioneel snijden ontstaan kunnen microbeschadigingen veroorzaken, onaanvaardbaar in de lucht- en ruimtevaart of elektronica

Daarboven komen er steeds meer nieuwe materialen met verbeterde chemische, mechanische en thermische eigenschappen die letterlijk onmogelijk zijn om conventioneel te bewerken.

De oplossing: **niet-conventionele processen** die gebruik maken van elektrothermische, mechanische, chemische of elektrochemische principes om materiaal af te nemen — zonder dat het gereedschap het werkstuk hoeft aan te raken.

```
Conventioneel:       gereedschap (harder) --> direct contact --> materiaalafname
Niet-conventioneel:  energie (elektrisch / chemisch / mechanisch) --> materiaalafname
                     zonder direct contact
```

---

## 2. Overzicht van alle niet-conventionele methoden

Er zijn vier grote families:

| Familie | Methoden |
|---|---|
| **Elektrothermisch** | LBM, EDM, EBM, IBM, PBM |
| **Mechanisch (abrasief)** | USM, WJM, AWJM, AJM, AFM |
| **Chemisch** | CHM (chemical machining) |
| **Elektrochemisch** | ECM |

---

## 3. Mechanische bewerkingen (abrasieve methodes)

De mechanische niet-conventionele methoden verwijderen materiaal niet door snijden maar door **erosie**: kleine harde deeltjes of een krachtige vloeistofstraal slijpen het oppervlak weg, zonder dat er een snijgereedschap aan te pas komt.

### Abrasive Flow Machining (AFM)

**Principe:** Een visceuze pasta gemengd met abrasieve korrels wordt onder druk door of langs het werkstuk gepompt. De korrels schuren het oppervlak glad terwijl de pasta doorstroomt. Het proces werkt in twee richtingen via twee zuigers.

AFM is ideaal voor het afwerken en polijsten van **moeilijk bereikbare interne oppervlakken** — complexe kanalen in turbineonderdelen of spuitgietmatrijzen die geen enkel slijpwerktuig bereikt.

- Tool: harde stalen cilinder + zuigers
- Medium: viskeuze abrasieve slurry
- Druk: 20–80 bar
- Toepassingen: slijpen, polijsten, reinigen, kleine gaten afwerken

### Water Jet Machining (WJM)

**Principe:** Water wordt onder extreem hoge druk (tot 300 MPa ≈ 3 kbar) door een klein mondstuk geperst, wat een waterstraal van 600–900 m/s oplevert. Die straal snijdt door het materiaal puur via **mechanische impact**.

WJM laat **geen HAZ** achter — de snede is koud. Perfect voor materialen die je niet wil verhitten (composieten, titanium) of voor voedingsproductie.

- Druk: ~300 MPa → 600–900 m/s
- Vormen: 2D snijden
- Materialen: platen, folies, plastics, steen, composieten
- Geen thermische schade

### Abrasive Water Jet Machining (AWJM)

**Principe:** Zelfde als WJM, maar abrasieve deeltjes (zand, granaat) worden aan de waterstraal toegevoegd. De combinatie van waterimpact + schurende deeltjes maakt het mogelijk om **metalen en keramiek** te snijden.

AWJM is een van de meest veelzijdige snijmethoden: bijna elk materiaal, geen HAZ, goede kantwaliteit. Druk iets lager dan WJM maar snijvermogen veel hoger.

- Snijsnelheid: tot 7,5 m/min
- Materialen: staal, aluminium, keramiek, composieten

### Abrasive Jet Machining (AJM)

**Principe:** Abrasieve deeltjes gemengd in een gasstroom (2–8 bar, ~300 m/s) worden via een nozzle op het werkstuk geblazen. Materiaalafname door directe impact van de deeltjes.

- Vormen: 2D–3D
- Materialen: harde materialen, glas
- Toepassingen: slijpen, reinigen van glas, deburren

### Ultrasonic Machining (USM)

**Principe:** Een werktuig trilt met ultrasonische frequentie (20–100 kHz) en een amplitude van 20–60 µm. Dit trillende werktuig pompt een abrasieve slurry in het contactgebied. De trillingen veroorzaken **cavitatie-erosie** en directe impact op het werkstuk.

USM werkt specifiek goed op **brosse materialen** zoals glas, steen en keramiek.

- Tool: bijv. wolfraamcarbide
- Medium: abrasieve slurry
- Toepassingen: boren, snijden, lassen, reinigen

---

## 4. Elektrothermische bewerkingen: EDM (vonkerosie)

### Wat is EDM?

**Electro Discharge Machining (EDM)**, ook wel **vonkerosie** of **vonkverspaning**, verwijdert materiaal via elektrische vonken. Er is **geen direct contact** tussen gereedschap en werkstuk. Beiden worden gescheiden door een kleine spleet gevuld met een **diëlektrische vloeistof** (isolerende olie).

Wanneer een korte hoogspanningspuls over die spleet wordt aangelegd, ioniseert het diëlektricum plaatselijk en ontstaat er een vonk. Die vonk produceert lokaal temperaturen tot 10 000 °C die het materiaal smelten en verdampen. De diëlektrische vloeistof spoelt de restjes (debris) weg.

> **Belangrijk voor examen:** EDM werkt enkel op **elektrisch geleidende** materialen. Het gereedschap slijt ook, maar veel langzamer dan het werkstuk.

### Twee types: zinkvonken vs draadvonken

**Zinkvonken (EDM die sinking)**
De elektrode heeft de exacte **negatieve** vorm van de gewenste holte en wordt langzaam in het werkstuk "gezonken". De vorm van de elektrode wordt zo overgedragen op het werkstuk. Typisch voor matrijzen en stempelgereedschappen.

**Draadvonken (EDM wire cutting)**
Een dunne draad (0,1–0,3 mm messing of koper) snijdt door het werkstuk terwijl vonken het materiaal wegslijten langs het snijspoor. De draad wordt continu ververst. Geschikt voor complexe 2D-contouren.

```
Zinkvonken:   elektrode met negatieve vorm --> holte in werkstuk (3D)
Draadvonken:  draad beweegt langs contour  --> uitsnijden (2D/2.5D)
```

### Pulsparameters

EDM werkt niet continu maar via **kortdurende pulsen**. De energie per puls bepaalt hoeveel materiaal wordt weggeslagen:

$$W_e = \int_0^{t_e} u_e(t) \cdot i_e(t) \cdot dt$$

| Parameter | Betekenis |
|---|---|
| U_i | Open gap voltage — spanning vóór de vonk |
| t_d | Discharge delay time — tijd tot de vonk springt |
| t_e | Discharge duration — duur van de vonk (eigenlijke bewerking) |
| t_p | Pulse period — totale cyclustijd |
| t_o | Pulse interval — rustperiode tussen vonken |
| i_e | Discharge current — stroom tijdens de vonk |
| U_e | Discharge voltage — spanning tijdens de vonk |

Grotere pulsenergie → meer materiaal weg per vonk → ruwer oppervlak maar hogere afnamesnelheid. Kleine pulsen → fijnere afwerking.

> **Belangrijk voor examen:** Ken het verband tussen pulsenergie en oppervlakkwaliteit. Finishing = kleine pulsen, roughing = grote pulsen.

### Materiaalafname stap voor stap (positieve polariteit)

Bij positieve polariteit: werkstuk = anode (+), gereedschap = kathode (−).

1. **Bubble Growth** — het diëlektricum ioniseert; een gasbel groeit in de spleet
2. **Ionization** — volledig plasmakanaal vormt zich; materiaal smelt en verdampt
3. **Thermal Erosion + Pressure Wave** — plasma imploodeert; drukgolf schiet debris weg
4. **Debris Diffusion** — losgekomen deeltjes verspreiden zich in het diëlektricum
5. **Debris Accumulation** — opeenvolgende vonken stapelen debris op
6. **Spurious Discharges** — als debris niet goed afgevoerd wordt, treden parasiete vonken op die de kwaliteit verminderen

Het continu doorspoelen met diëlektricum is cruciaal: het voert debris af en voorkomt spurious discharges.

### EDM technische samenvatting

- Tool: elektrode (+ of −, afhankelijk van polariteit)
- Medium: diëlektrisch (olie of gedeioniseerd water)
- Stroom: 1–100 A (100–300 V) → 10⁵–10⁷ W/mm²
- Spleetgrootte: 0,005–1 mm
- Vormen: 3D (zinkvonken), 2.5D (draadvonken)
- Materialen: **enkel geleidend**
- Toepassingen: precisiebewerking, matrijs maken, snijden van superharde materialen

---

## 5. Andere elektrothermische methoden

### Electron Beam Machining (EBM)

Elektronen worden versneld tot ~200 000 km/s (30–150 kV) en via magnetische lenzen gefocust op het werkstuk in **vacuüm**. Kinetische energie → warmte → materiaal verdampt.

- Vermogensdichtheid: 10³–10⁹ W/cm²
- Vereist vacuüm (nadeel voor grote onderdelen)
- Voordeel: weinig temperatuurinvloed op omgeving, weinig reflectie
- Toepassingen: boren en textureren van kleine onderdelen, electron beam melting (AM)

### Ion Beam Machining (IBM)

Ionen van een inert gas (Argon) worden versneld en schieten atomen weg van het oppervlak. Belangrijk: **niet-thermisch** — geen smelten, alleen directe kinetische overdracht.

- Per ion: 0,1–10 atomen verwijderd
- Extreem hoge nauwkeurigheid, maar zeer lage snelheid
- Toepassingen: ion beam sputter etching, miniaturuuronderdelen

### Plasma Beam Machining (PBM)

Een plasma (4 000–20 000 °C) van Argon-gas wordt met de geluidssnelheid (340 m/s) op het werkstuk gericht. Hitte smelt het materiaal; de snelheid van het plasma blaast het weg.

- Stroom: 5–1000 A (100–250 V)
- Materialen: (harde) metalen
- Toepassingen: plasma-frezen, plasma-snijden, plasma-lassen

---

## 6. Elektrochemische bewerkingen (ECM)

### Principe van ECM

**Electro Chemical Machining (ECM)** verwijdert materiaal via een **elektrochemische reactie** — het omgekeerde van galvaniseren. Het werkstuk is de **anode** (+), het gereedschap is de **kathode** (−), en een elektrolyt (zoutoplossing) stroomt onder hoge druk door de spleet.

Wanneer stroom vloeit, oxideert het werkstukmateriaal en lost het op. Het gereedschap slijt **niet** — aan de kathode vormt zich alleen waterstofgas.

### De chemische reacties

Aan de **anode (werkstuk)** — oxidatie:
$$Me \rightarrow Me^{z+} + z \cdot e^-$$

Aan de **kathode (gereedschap)** — reductie van water:
$$z \cdot H_2O + z \cdot e^- \rightarrow \frac{1}{2}z \cdot H_2 \uparrow + z \cdot OH^-$$

Gecombineerd — metaal lost op als metaalhydroxide, waterstofgas borrelt vrij:
$$Me + z \cdot OH^- \rightarrow Me(OH)_z \downarrow + \frac{1}{2}z \cdot H_2 \uparrow$$

> **Belangrijk voor examen:** Ken de drie reacties en de rolverdeling: werkstuk = anode (+), gereedschap = kathode (−).

### Unieke eigenschappen van ECM

Materiaalafname is het hoogst waar de spleet het **smalst** is (hogere stroomdichtheid). Daardoor is het proces **zelf-correcting**: het werkstuk convergeert automatisch naar de vorm van het gereedschap. 
> De kern van het ECM-principe: de stroomdichtheid j is omgekeerd evenredig met de lokale gap g. Waar de gap kleiner is, lost er meer materiaal op — en dat is precies waarom de werkstuksvorm uiteindelijk de negatieve afdruk van de elektrode wordt.

- **Geen slijtage van het gereedschap**
- **Geen HAZ** — volledig thermiekvrij
- **Hoogste materiaalafnamesnelheid** van alle niet-conventionele processen
- Werkt op alle **geleidende** materialen, ook superharde

### ECM technische samenvatting

- Tool: elektrode (kathode −)
- Medium: elektrolyt (zoutoplossing) onder hoge druk
- Stroom: ~10 000 A (15 V)
- Snelheid: 2,5–12 mm/min (afhankelijk van stroomdichtheid)
- Vormen: 3D
- Toepassingen: matrijs-zinken, kleine gaten boren, ontbramen, polijsten, turbinebladen, scheerapparaten (Philips)

### Chemical Machining (CHM)

Puur chemische variant: werkstuk onderdompeld in een zuur of alkalisch bad. Zones die niet bewerkt mogen worden, zijn afgedekt met een **masker** (resist). De onbedekte zones worden chemisch weggeëtst.

- Tool: masker (resist)
- Medium: zuur/alkalisch bad
- Vormen: 2D–2.5D (max. enkele mm diep)
- Materialen: metalen (staal, nikkel, aluminium), halfgeleiders (silicium)
- Toepassingen: dunne lagen verwijderen, MEMS, elektronica, microstructuuranalyse
- Nadeel: masker relatief duur → enkel rendabel bij kleine series

---

## 7. USP-laserbewerking (ultrakorte-puls-laser)

### Pulslasers: het verschil met een gewone laser

Een gewone (CW = continuous wave) laser levert constant vermogen. Bij een **gepulsde laser** wordt dezelfde gemiddelde energie geconcentreerd in korte pulsen met hoog piekvermogen. Hoe korter de puls, hoe hoger het piekvermogen bij hetzelfde gemiddeld vermogen.

```
CW laser:     ────────────────── (constant, laag vermogen)
Pulsed laser: |||  |||  |||  ||| (korte pieken, hoog piekvermogen)
USP laser:    |  |  |  |  |  |  (ultrakorte pieken, extreem hoog piekvermogen)
```

USP staat voor **Ultra-Short Pulse** — pulsduur van picoseconden (ps, 10⁻¹²s) tot femtoseconden (fs, 10⁻¹⁵s).

### Lange vs ultrakorte pulsen: het cruciale verschil

Bij **lange pulsen** (ms/µs/ns) heeft het materiaal **tijd** om warmte te geleiden naar de omgeving terwijl de laser nog belicht:
- grote **heat-affected zone (HAZ)**
- gesmolten materiaal dat herdeponeerd wordt (redeposition)
- microcracks door thermische spanningen
- slordig gat met opgeworpen randen

Bij **ultrakorte pulsen** (ps/fs) is de puls zo kort dat het materiaal **geen tijd** heeft om warmte te verspreiden:
- het materiaal **sublimeert** direct (vast → gas, zonder vloeibaar te zijn)
- nauwelijks HAZ
- minimale schade rondom het bewerkte gebied
- scherpe, schone geometrieën

> **Belangrijk voor examen:** ns-laser → smeltzone + herdeponering + microcracks. fs-laser → ablatie zonder smeltzone, minimale schade. Dit verschil is een kernvraag.

De slides illustreren dit duidelijk: een gat geboord met een ns-laser heeft rafelige opgeworpen randen; hetzelfde gat met een fs-laser is scherp omlijnd en schoon.

### Schaal en typische bewerkingen

USP-laserbewerking werkt op de **microschaal**: structuren van enkele micron tot enkele honderden micron. De bewerkte onderdelen zelf kunnen groot zijn, maar de structuren erop zijn klein.

Typische bewerkingen: microgaten boren, snijden, frezen, markeren, **structureren en textureren**.

### Oppervlaktetexturering

**Textureren** ≠ graveren. Graveren gaat enkele tienden mm diep en maakt macrogeometrieën. Textureren verandert het oppervlak op **micrometer- of nanometerschaal** — structuren zo klein dat ze de functionele eigenschappen fundamenteel wijzigen.

Elke laserpuls (gefocust op een vlekgrootte in de orde van een haardiameter) verdampt een miniem volume materiaal. Door pulsen nauwkeurig te positioneren bouw je gecontroleerde patronen op.

**Effecten en toepassingen van oppervlaktetextuur:**

| Eigenschap | Effect | Toepassing |
|---|---|---|
| Tribologisch | minder wrijving en slijtage | gereedschappen, matrijzen |
| Bevochtigbaarheid | hydrofoob/hydrofiel | spuitgietmatrijzen |
| Biocompatibiliteit | betere celgroei | biomedische implantaten |
| Optisch | kleurverandering via diffractie | esthetiek, optische elementen |
| Thermisch | betere warmteoverdracht | koellichamen, warmtewisselaars |

### Biomimetische texturen: inspiratie uit de natuur

**Lotusbladeffect** — microscopische uitsteeksels maken het oppervlak superhydrofoob (waterdruppels rollen af). USP-lasers kunnen dezelfde nanostructuur op metalen reproduceren voor waterafstotende oppervlakken zonder coating.

**Haaienhuideffect** — schubachtige ribbels verminderen de vloeistofweerstand. Toegepast op turbinebladen of vliegtuigoppervlakken.

**Gekko-effect** — nanohaartjes op de poten creëren Van der Waals-kleefkracht. Basis voor droge kleefmaterialen.

### LIPSS: Laser-Induced Periodic Surface Structures

Een bijzonder fenomeen: USP-lasers genereren **vanzelf** periodieke nanostructuren op het oppervlak, zonder expliciete programmering.

- Afmetingen **kleiner** dan de vlekgrootte van de laserstraal
- Periodiciteit **evenredig** met de golflengte van de laser
- Komen voornamelijk voor bij ultrakorte pulsen (ps/fs)
- **Onafhankelijk** van kristaloriëntatie
- Het exacte mechanisme is nog **niet volledig begrepen**

| Type | Periodiciteit | Structuur |
|---|---|---|
| **LSFL** (Low Spatial Frequency) | Λ < 1 µm | ribbelvormige structuren |
| **HSFL** (High Spatial Frequency) | Λ ≤ 100 nm | fijnere structuren |

LIPSS worden uitgebuit voor kleuring (diffractie-effecten), tribologie en anti-wrijvingscoatings.

### Toepassingen van USP-laserbewerking

**Tribologie**
LSFL en hybride structuren op Ti6Al4V kunnen de wrijvingscoëfficiënt van ~0,53 (gepolijst) naar ~0,14 brengen — factor 4 minder wrijving (Bonse et al., 2018).

**Matrijstexturering voor kunststofspuitgieten**
Een hydrofobe textuur gelaserd in de matrijs wordt direct overgedragen op het gespoten plastic onderdeel. Waterafstotende oppervlakken zonder extra nabewerking.

**Batterijen**
fs-laser-structuren in silicium/grafietelektroden vergroten het actief oppervlak → meer ionentransport → betere batterijcapaciteit en efficiëntie.

**Inkleuring via diffractie**
LIPSS-structuren veranderen de reflectiviteit als functie van golflengte. Aluminium kan goud, grijs of zwart lijken — zonder pigment of coating. Toepassingen: sieraden, horloges, antireflectiecoatings.

**Warmteoverdracht**
Schuine microscopische gaatjes creëren meer nucleatiecentra voor kookbellen → betere warmteafvoer. Relevant voor elektronica-koeling en ruimtevaart (ook bij 0g).

### Bundelvormgeving (beam shaping) — huidige trends

In plaats van een simpele Gaussische spot kan je de laserbundel actief of passief vormen:

- **Passieve apparaten**: lenzen, diffractieve optische elementen (DOE)
- **Actieve apparaten**: ruimtelijke lichtmodulatoren (SLM), beweegbare spiegels

Voorbeelden van resultaten:
- Twee-golflengte fs-pulsen → roostersstructuren (1 µm)
- Donut-vormige bundel → ringvormig ablatieprofiel
- Vier interfererende bundels → piramidestructuren
- **Bessel-bundel** → nanokanaal met hoge aspectverhouding in één enkele puls

---

## 8. Vergelijking van alle methoden

### Kwalitatieve vergelijking snijprocessen

| Methode | Nauwkeurigheid | HAZ | Materiaalbeperking | Snelheid |
|---|---|---|---|---|
| Waterjet (WJM) | ±0,08 mm | Geen | Bijna alles behalve harde keramiek | 5–10× sneller dan EDM bij dikte <25 mm |
| Wire EDM | ±0,0025 mm | Weinig | Enkel geleidend | 5–10× trager dan waterjet |
| Laser (LBM) | ±0,025 mm | Ja | Niet-reflecterende metalen | Zeer snel bij dun materiaal |
| Plasma (PBM) | ±0,75 mm | Ja | Metalen algemeen | Snel bij dunne platen |
| Frezen | ±0,008 mm | Geen | Niet ideaal voor zeer harde materialen | Goed |

### Proceskarakteristieken

| Methode | Typisch gebruik | Materiaalafname |
|---|---|---|
| Chemical Machining (CM) | Ondiepe lagen op grote vlakke oppervlakken | 0,0025–0,1 mm/min |
| ECM | Complexe vormen met diepe holten | 2,5–12 mm/min |
| EDM | Complexe vormen in hard materiaal | ~300 mm³/min |
| Wire EDM | Contoursnijden | Afhankelijk van materiaal/dikte |
| WJM | Niet-metallische materialen | Sterk variabel |
| AWJM | Metalen en niet-metalen | Tot 7,5 m/min |
| AJM | Snijden, ontbramen, reinigen | Sterk variabel |

### Oppervlakruwheid en tolerantie (vuistregel)

- **Elektrochemische methoden** (ECM, electrochemical grinding): uitstekende oppervlakruwheid + nauwkeurige toleranties
- **Thermische methoden finishing** (EDM fine): goed oppervlak, goede toleranties
- **Thermische methoden roughing** (EDM rough, plasma): ruwer oppervlak, ruimere toleranties
- **Mechanische methoden** (AFM, waterjet): gemiddeld oppervlak

---

## 9. Belangrijke begrippen

| Term | Uitleg |
|---|---|
| **Diëlektricum** | Isolerende vloeistof in EDM die de spleet vult en debris afvoert |
| **Vonkspleet (spark gap)** | Kleine afstand tussen elektrode en werkstuk bij EDM |
| **Elektrolyt** | Geleidende vloeistof (zoutoplossing) bij ECM |
| **Ablatie** | Verwijderen van materiaal door een laser (verdampen/sublimeren) |
| **HAZ (Heat-Affected Zone)** | Zone naast de snede die thermisch beschadigd is |
| **LIPSS** | Laser-Induced Periodic Surface Structures — vanzelf gevormde nanostructuren |
| **USP** | Ultra-Short Pulse — pulsen in de ps/fs-range |
| **AFM** | Abrasive Flow Machining — erosie via abrasieve pasta |
| **WJM / AWJM** | Water Jet / Abrasive Water Jet Machining |
| **ECM** | Electro Chemical Machining — materiaalafname via oxidatie |
| **EDM** | Electro Discharge Machining — vonkerosie |
| **Textureren** | Oppervlak structureren op micro-/nanoschaal voor functionele doeleinden |
| **Debris** | Losgekomen materiaaldeeltjes bij EDM die moeten worden afgevoerd |
| **Discharge delay time (t_d)** | Tijd tussen aanleggen spanning en het springen van de vonk |
| **Lotusbladeffect** | Superhydrofobe eigenschap door micro/nanostructuren op het oppervlak |
| **LSFL / HSFL** | Lage / hoge ruimtelijke frequentie LIPSS-structuren |
| **Spurious discharge** | Parasiete vonk door debris-opstapeling bij EDM |

---

## Wat je echt moet kennen

**Inleiding**
- Waarom conventionele bewerking tekortschiet bij harde materialen, nauwe toleranties en oppervlakteschadevereisten
- Het fundamentele verschil: conventioneel = direct contact en mechanische kracht; niet-conventioneel = energie zonder contact

**Mechanische methoden**
- De vijf abrasieve methoden en hun principe: AFM (pasta door kanaal), WJM (water onder druk), AWJM (water + slijpkorrels), AJM (gas + slijpkorrels), USM (ultrasonische trillingen + slurry)
- Wanneer kies je WJM vs AWJM: WJM voor zachte/niet-metallische materialen zonder HAZ-vereiste, AWJM wanneer je metalen of keramiek wil snijden
- Dat WJM en AWJM **geen HAZ** produceren — thermisch koude snijprocessen

**EDM — vonkerosie**
- Wat EDM is: materiaalafname via elektrische vonken, geen direct contact, diëlektricum in de spleet
- Dat EDM **enkel werkt op geleidende materialen**
- Het verschil tussen **zinkvonken** (negatieve elektrodevorm → 3D holte) en **draadvonken** (draad langs contour → 2D/2.5D)
- De pulsparameters: U_i, t_d, t_e, t_p, t_o, i_e, U_e en wat ze betekenen
- De pulsenergie formule: $W_e = \int_0^{t_e} u_e(t) \cdot i_e(t) \cdot dt$
- Het verband pulsenergie ↔ oppervlakkwaliteit: grote puls = ruw + snel, kleine puls = fijn + traag
- De zes fasen van materiaalafname: Bubble Growth → Ionization → Thermal Erosion + Pressure Wave → Debris Diffusion → Debris Accumulation → Spurious Discharges
- Waarom doorspoelen met diëlektricum cruciaal is (debris afvoeren, spurious discharges vermijden)

**ECM — elektrochemische bewerking**
- Principe: werkstuk = anode (+), gereedschap = kathode (−), elektrolyt stroomt door spleet
- De drie chemische reacties kunnen uitleggen: oxidatie aan anode, reductie aan kathode, gecombineerde reactie
- Dat het gereedschap **niet slijt**
- Dat ECM **zelf-correcting** is (smalle spleet = meer stroom = meer afname = spleet vergroot)
- Geen HAZ, hoogste afnamesnelheid van alle niet-conventionele processen

**CHM**
- Principe: masker + zuur/alkalisch bad
- Enkel ondiepe 2D-bewerking, kleine series

**USP-laserbewerking**
- Wat CW vs gepulsde vs USP laser betekent
- Het **cruciale verschil** tussen ns- en fs-pulsen:
  - ns: HAZ + redeposition + microcracks + opgeworpen randen
  - fs: ablatie zonder smeltzone, geen HAZ, schone geometrie
- Wat textureren is (micro/nanometerschaal) vs graveren (tiende mm)
- De drie biomimetische texturen: lotusbladeffect, haaienhuideffect, gekko-effect en wat ze functioneel doen
- Wat LIPSS zijn: spontaan gevormde periodieke nanostructuren bij USP-laserbewerking, periodiciteit ∝ golflengte, onafhankelijk van kristaloriëntatie, mechanisme niet volledig begrepen
- LSFL (Λ < 1 µm) vs HSFL (Λ ≤ 100 nm)
- De toepassingen van USP-texturering: tribologie, matrijstexturering, batterijen, inkleuring, warmteoverdracht

**Vergelijking**
- Globaal kunnen vergelijken: wire EDM is nauwkeuriger dan waterjet, waterjet heeft geen HAZ, plasma is snel maar onnauwkeurig en heeft HAZ
- ECM heeft de hoogste materiaalafnamesnelheid van de niet-conventionele processen

---

*Gebaseerd op slides: "Les 14 Phys Chemi SC 2024" — Prof. Sylvie Castagne, KU Leuven*
