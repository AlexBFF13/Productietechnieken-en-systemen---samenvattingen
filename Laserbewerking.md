# Deel 7 – Laserbewerking (Les 13)

---

## Inhoudsopgave

- [Wat is een laser?](#wat-is-een-laser)
- [Kenmerken van laserlicht](#kenmerken-van-laserlicht)
- [Basisconfiguratie van een laserbron](#basisconfiguratie-van-een-laserbron)
- [Types lasersystemen](#types-lasersystemen)
  - [CO₂ laser](#co₂-laser)
  - [Fiber laser](#fiber-laser)
  - [Direct Diode Laser (DDL)](#direct-diode-laser-ddl)
- [Golflengte en absorptie](#golflengte-en-absorptie)
  - [Materiaalafhankelijkheid](#materiaalafhankelijkheid)
  - [Fresnelabsorptie en invalshoek](#fresnelabsorptie-en-invalshoek)
- [Bundelkwaliteit](#bundelkwaliteit)
  - [BPP — Beam Parameter Product](#bpp--beam-parameter-product)
  - [M²-factor](#m²-factor)
  - [Rayleighlengte](#rayleighlengte)
- [Lasersnijden](#lasersnijden)
  - [Rol van het snijgas](#rol-van-het-snijgas)
  - [Kwaliteitsparameters](#kwaliteitsparameters)
- [Problemen bij lasersnijden](#problemen-bij-lasersnijden)
  - [Dross (te hoge snelheid)](#aanhechting--dross-te-hoge-snelheid)
  - [Inbranding (te lage snelheid)](#inbranding-te-lage-snelheid)
  - [Plasmavorming (CO₂ + Al/RVS)](#plasmavorming-bij-co₂--hoge-snelheid-bij-alrvs)
- [Technologieshift: CO₂ vs Fiber vs DDL](#technologieshift-co₂-vs-fiber-vs-ddl)
- [Recente ontwikkelingen](#recente-ontwikkelingen-overzicht)
- [Samenvatting en examenoverzicht](#samenvatting-en-examenoverzicht)

---

## Wat is een laser?

**LASER** staat voor *Light Amplification by Stimulated Emission of Radiation*. De naam zegt eigenlijk alles: het is een lichtbron die werkt via gestimuleerde emissie.

Het principe: atomen kunnen in een hogere energietoestand gebracht worden (*pompen*). Wanneer een elektron terugvalt naar een lager niveau, zendt het spontaan een foton (lichtdeeltje) uit — dat heet *spontane emissie*. Als dat foton vervolgens een ander aangeslagen atoom treft, valt ook dat elektron terug en zendt een tweede foton uit dat **exact in fase** loopt met het eerste. Dit is *gestimuleerde emissie*. Door deze fotonen te versterken in een resonatorcaviteit (tussen twee spiegels) en ze gecontroleerd uit te koppelen, ontstaat de laserstraal.

```
Pompen (energie inbrengen)
    → atomen in aangeslagen toestand
    → gestimuleerde emissie → coherente fotonen
    → versterken in resonatorcaviteit
    → uitkoppelen → laserstraal
```

---

## Kenmerken van laserlicht

Laserlicht onderscheidt zich van gewoon licht door drie eigenschappen:

1. **Monochromatisch**: één enkele golflengte (of een zeer nauwe band). Gewoon wit licht bevat alle golflengtes.
2. **Coherent**: alle golven lopen in fase. Dit maakt constructieve interferentie mogelijk en is verantwoordelijk voor het scherp focusseren.
3. **Directioneel**: de straal plant zich nagenoeg parallel voort — weinig divergentie. Daardoor kan de bundel over grote afstand intensief blijven.

Laserlicht is ook **gepolariseerd**: de elektromagnetische golf trilt in een bepaald vlak (lineair, circulair of elliptisch). De polarisatierichting heeft invloed op hoe goed het licht geabsorbeerd wordt door een materiaal, wat relevant is bij lasersnijden.

---

## Basisconfiguratie van een laserbron

Een laser bestaat altijd uit drie basisonderdelen:

- **Lasermedium**: het materiaal dat fotonen emitteert (gas, vaste stof, vloeistof of halfgeleider).
- **Pompbron**: levert de energie om het medium in de aangeslagen toestand te brengen. Kan elektrisch (gas-discharge) of optisch (diodes) zijn.
- **Resonatorcaviteit**: twee spiegels (één volledig reflecterend, één gedeeltelijk doorlatend als uitkoppelvenster) die de fotonen heen en weer sturen zodat ze verder versterkt worden vóór ze als laserstraal uitkomen.

De twee grote uitdagingen bij het ontwerp: energie-efficiëntie (het meeste vermogen gaat verloren als warmte) en lichtkwaliteit behouden.

---

## Types lasersystemen

Lasers worden ingedeeld op basis van:

- het **lasermedium**: gas, vaste stof (solid state), vloeistof, halfgeleider
- de **golflengte**: infrarood (IR), zichtbaar, ultraviolet (UV)
- de **uitgangsstraal**: continu (*Continuous Wave*, CW) of gepulst
- het **vermogen**: van milliwatts tot meerdere kilowatts
- de **pompbron**: elektrisch of optisch

### Belangrijke types voor materiaalbewerking

| Type | Categorie | Golflengte | Pompbron |
|---|---|---|---|
| **CO₂ laser** | Gaslaser | 10,64 µm | Elektrische ontlading |
| **Fiber laser** (Yb-gedopeerd) | Vastestoflaser | 1070 nm | Laserdiodes |
| **Nd:YAG laser** | Vastestoflaser | 1064 nm | Laserdiodes |
| **Groene laser** (frequentieverdubbeld) | Vastestoflaser | 532 nm | Laserdiodes |
| **Diodelaser (DDL)** | Halfgeleider | 400–1500 nm | Elektrische stroom |

### CO₂ laser

De oudste en lange tijd dominante laser voor industriële snijapplicaties. Golflengte van 10,64 µm (ver-IR). Relatief lage investeringskost, maar hoge gebruikskosten (gas, onderhoud) en lage energetische efficiëntie. De lange golflengte wordt slecht geabsorbeerd door metalen maar goed door niet-metalen (hout, kunststof, glas).

### Fiber laser

Exponentiele groei sinds 2010. Het lasermedium is een ytterbium-gedopeerde glasvezel zelf — de vezel is tegelijk het medium en de geleider. Golflengte 1070 nm (nabij-IR). Voordelen: lage BPP (zie verder) = hoge bundelkwaliteit, hoge energetische efficiëntie, compact en onderhoudsarm. Hogere investeringskost, maar die daalt.

### Direct Diode Laser (DDL)

De nieuwste generatie. Laserdiodes worden gecombineerd via polarisatie of golflengteoptelling om hoog vermogen te bereiken. Hoge energie-efficiëntie, compact, flexibel qua golflengte en polarisatie. Nog relatief experimenteel, maar veelbelovend.

---

## Golflengte en absorptie

### Waarom is de golflengte zo belangrijk?

Een laser die de materie niet absorbeert, kan er ook niet mee bewerken. De golflengte bepaalt grotendeels hoeveel van het licht geabsorbeerd wordt door het werkstukmateriaal.

De drie mogelijkheden aan het oppervlak:
$$R + T + A = 1$$

- **R** = reflectie (weerkaatst)
- **T** = transmissie (doorgelaten, relevant bij glas/polymeren)
- **A** = absorptie = wat echt in het materiaal omgezet wordt in warmte

Voor ondoorzichtige materialen (metalen): T = 0, dus A = 1 − R.

### Materiaalafhankelijkheid

- **Koper en aluminium** zijn bij de golflengtes van CO₂ en fiber lasers sterk reflectief — moeilijk te verwerken. Ze absorberen beter bij kortere golflengtes (nabij-IR).
- **Koolstofstaal** absorbeert redelijk goed bij beide golflengtes.
- **Fiber laser** (1 µm) wordt over het algemeen beter geabsorbeerd door metalen dan CO₂ (10 µm).

> **intuition**: kies de lasergolflengte die goed geabsorbeerd wordt door je materiaal. Een krachtige laser die voor 95% gereflecteerd wordt, is nutteloos (en gevaarlijk).

### Fresnelabsorptie en invalshoek

De absorptie hangt niet alleen af van de golflengte, maar ook van de **invalshoek** van de laserstraal op het oppervlak. De Fresnelformules beschrijven dit:

- Bij loodrechte inval (0°): absorptie is relatief laag voor metalen.
- Bij schuine inval (Brewsterhoek): absorptie heeft een maximum, vooral voor p-gepolariseerd licht.
- Bij zeer schuine inval (>70°): absorptie daalt sterk.

Dit is relevant bij lasersnijden: het snedefront staat onder een hoek → de invalshoek van de laser op het gesmolten materiaal is niet 0°. De polarisatierichting van de laserstraal t.o.v. de snijrichting beïnvloedt dus de efficiëntie.

$$A_p = 1 - R_p = 1 - \left|\frac{n\cos\phi_{in} - 1 + k\cos\phi_{in}}{n\cos\phi_{in} + 1 + k\cos\phi_{in}}\right|^2$$

(De complexe refractie-index n = n + ik karakteriseert het optisch gedrag van het materiaal, met waarden die temperatuur- en golflengteafhankelijk zijn.)

---

## Bundelkwaliteit

### Wat bepaalt de bundelkwaliteit?

Een laser met hoge bundelkwaliteit kan worden gefocust op een **kleine plek** (*spot*) met een **hoge intensiteit**. Dat is cruciaal bij snijden en lassen: hoe kleiner de spot, hoe meer energie per oppervlakte, hoe beter het materiaal verwerkt wordt.

### BPP — Beam Parameter Product

$$\text{BPP} = w_0 \times \theta$$

waarbij:
- **w₀** = straal van de bundel op het smalste punt (focus)
- **θ** = halve divergentiehoek van de bundel buiten de focus

Een lage BPP = betere bundelkwaliteit = scherper focusseerbaar.

Voor een ideale Gaussiaanse bundel geldt:
$$\text{BPP}_{Gauss} = \frac{\lambda}{\pi}$$

Een kortere golflengte geeft een lagere BPP, dus betere bundelkwaliteit. Fiber lasers (λ ≈ 1 µm) hebben dan ook een veel lagere BPP dan CO₂ lasers (λ = 10,6 µm).

### M²-factor

De M²-factor vergelijkt de bundelkwaliteit met die van een ideale Gaussiaanse bundel:

$$M^2 = \frac{\text{BPP}}{\text{BPP}_{Gauss}} = \frac{\text{BPP} \times \pi}{\lambda}$$

Voor een ideale Gaussiaanse bundel: M² = 1 (beste mogelijke kwaliteit). In de praktijk is M² > 1.

Fiber lasers halen typisch M² ≈ 4–10. CO₂ lasers en diodelasers zitten veel hoger (M² > 70).

> **belangrijk voor examen**: lagere BPP en lager M² = betere bundelkwaliteit = kleinere focusspot mogelijk.

### Rayleighlengte

De Rayleighlengte Z_R is de afstand waarover de doorsnede van de bundel in oppervlak verdubbelt (straal groeit met factor √2 t.o.v. de focusstraal). Het geeft aan hoe "diep" de focus is: een grotere Rayleighlengte = de bundel blijft langer smal.

---

## Lasersnijden

### Principe

Bij lasersnijden wordt een gefocuste laserstraal langs een snijcontour bewogen. De energie smelt en/of verdampt het materiaal lokaal. Een **snijgas** (*assist gas*) geblazen doorheen een nozzle verwijdert het gesmolten materiaal en creëert de snede.

De instelbare parameters:
- **Laservermogen** P
- **Snijsnelheid** v
- **Focuspositie** f (boven, op of onder het oppervlak)
- **Stand-off distance** (afstand nozzle tot werkstuk)
- **Gasdruk** p
- **Type snijgas**

### Rol van het snijgas

Het snijgas heeft twee functies tegelijk:

1. **Chemische atmosfeer**: het gas bepaalt of er oxidatie optreedt of niet.
2. **Uitstootkracht**: de gasstroom blaast het gesmolten materiaal uit de snede. Een hoge uitstroomsnelheid is nodig om het werkstuk volledig schoon te snijden.

Er zijn twee snijmodi:

**Smeltsnijden** (*laser fusion cutting*): gebruik van een **inert gas** (stikstof N₂ of argon Ar). Er treedt geen oxidatie op → oxidatievrij snijvlak, geschikt voor **aluminium en roestvrij staal**. Nadeel: hoog gasdebiet nodig, duur.

**Brandsnijden** (*laser flame cutting / oxidative cutting*): gebruik van **zuurstof O₂** als snijgas. De zuurstof reageert exotherm met het staal en verdubbelt het thermisch beschikbaar vermogen in het proces. Hierdoor kunnen dikkere platen gesneden worden bij hogere snelheid. Enkel geschikt voor **koolstofstaal** (bij RVS en aluminium geeft oxidatie slechte kwaliteit).

> **intuition**: zuurstof = meer energie maar oxideert → staal OK, RVS/alu niet.

### Kwaliteitsparameters

Relevante normen: ISO 9013, VDI 2906, DIN 2310.

Kwaliteitsparameters van de gesneden rand:
- Snijvlakruwheid
- Loodrechtheid / hellingshoek van het snijvlak
- Sleutelwijdte (*kerf width*)
- Braam onderaan (*dross*)
- Inbranding of beschadigingen

---

## Problemen bij lasersnijden

### Aanhechting / dross (te hoge snelheid)

Bij een **te hoge snijsnelheid** krijgt het gesmolten materiaal te weinig tijd om volledig uitgestoten te worden door het snijgas. Het stolt opnieuw aan de onderkant van de snede → **heraanhechting** (*dross*). Als de snelheid verder toeneemt, gaat uiteindelijk de snede verloren.

```
Snelheid ↑ → minder tijd voor uitstoot → dross → snedeverlies
```

### Inbranding (te lage snelheid)

Bij een **te lage snijsnelheid** wordt er teveel energie ingebracht per eenheid lengte. Bij brandsnijden (O₂) zorgt de exotherme reactie voor nog extra warmte. Resultaat: **inbranding** (*burning*) met grote ruwheidsvariataties en smeltsporen naast de snede.

```
Snelheid ↓ → te veel energie → inbranding → ruwe rand
```

### Plasmavorming (bij CO₂ + hoge snelheid bij Al/RVS)

Bij het snijden van **aluminium of roestvrij staal met een CO₂ laser** bij hoge snelheid treedt plasmavorming op.

Het mechanisme:
1. Gesmolten materiaal wordt langs het snedefront omlaag gestuwd.
2. Druppels gesmolten materiaal worden uitgestoten.
3. Bij te hoge snelheid ontstaat **lokaal plasma** onderaan het snedefront.
4. Dit plasma groeit snel uit tot een **plasmawolk boven de plaat**.
5. De plasmawolk **absorbeert de laserstraal volledig** → de bundel bereikt het werkstuk niet meer.
6. Resulteert in volledig snedeverlies. Als het niet tijdig afgebroken en hernieuwd wordt, gaat het werkstuk verloren.

Reden: bij CO₂ golflengte (10,6 µm) zijn de Fresnelabsorptiecoëfficiënten voor aluminium en RVS al laag bij loodrechte inval, maar de hoekverdeling verandert bij hogere snelheden (hoek van het snedefront neemt toe), wat de absorptie nog verder vermindert en plasmavorming bevordert.

> **belangrijk voor examen**: plasmavorming is specifiek voor CO₂ + Al/RVS bij te hoge snelheid en betekent totaal snedeverlies.

---

## Technologieshift: CO₂ vs Fiber vs DDL

De industriële lasermarkt is de afgelopen decennia fundamenteel verschoven:

| | CO₂ laser | Fiber laser | Direct Diode (DDL) |
|---|---|---|---|
| In gebruik sinds | ~1965 | Exponentieel vanaf 2010 | Opkomend (R&D-fase) |
| Golflengte | 10,6 µm | 1,07 µm | 0,4–1,5 µm |
| BPP / bundelkwaliteit | Matig | Uitstekend (lage BPP) | Wisselend |
| Energetische efficiëntie | Laag | Hoog | Zeer hoog |
| Investeringskost | Laag | Hoog (dalend) | Potentieel laag |
| Gebruikskost | Hoog | Lager | Laag |
| Onderhoud | Complex | Onderhoudsarm | Compact |

**Fiber lasers** domineren vandaag de dunne plaat snijmarkt dankzij hun uitstekende bundelkwaliteit, hoge efficiëntie en dalende prijs.

**DDL** is de volgende generatie: zeer energiezuinig, compact, geen bewegende optische onderdelen, flexibel in golflengte en polarisatie. Staat nog op het niveau van R&D voor hoogvermogenstoepassingen.

> **intuition**: fiber = hogere golflengtekwaliteit (1 µm vs 10 µm), minder energie verloren als warmte, kleiner focuspunt mogelijk → betere snijprestaties voor metaal.

---

## Recente ontwikkelingen (overzicht)

- **DDL lasersnijden met *free beam propagation***: elimineer de transportvezel → lagere BPP door vermijden van fiberkoppeling.
- **Natural beam shaping**: de elliptische bundelvorm van DDL wordt benut i.p.v. gecorrigeerd.
- **Polarisatiestrategieën**: polarisatie afstemmen op snijrichting voor betere absorptie aan het snedefront.
- **Dynamische bundelvorming**: real-time aanpassen van de bundelgeometrie tijdens het snijden.
- **In-procesmetingen en -observaties**: sensorintegratie voor kwaliteitsbewaking.
- **Microbewerking met ultrakorte pulslasers** (femto-/picoseconde): geen thermische zone, uiterst fijne bewerkingen op harde en brosse materialen.

---

## Samenvatting en examenoverzicht

| Concept | Kernpunt |
|---|---|
| LASER principe | Gestimuleerde emissie → coherent, monochromatisch, directioneel licht |
| Lasertypes | CO₂ (10,6 µm), Fiber (1,07 µm), DDL (0,4–1,5 µm) |
| Absorptie | A = 1 − R (metalen); korter golflengte = beter geabsorbeerd door metaal |
| BPP | w₀ × θ; lager = betere kwaliteit |
| M² | BPP / BPP_Gauss; M² = 1 is ideaal |
| Smeltsnijden | Inert gas (N₂/Ar), geen oxidatie → Al, RVS |
| Brandsnijden | O₂ → exotherme reactie, meer vermogen → staal, dikkere platen |
| Dross | Te hoge snelheid → gesmolten materiaal hecht opnieuw aan |
| Inbranding | Te lage snelheid → te veel energie → ruwe rand |
| Plasma | CO₂ + Al/RVS + hoge snelheid → plasmawolk absorbeert bundel → snedeverlies |
| Fiber vs CO₂ | Fiber: kortere golflengte, betere absorptie in metaal, hogere efficiëntie, kleinere spot |

Concepten die je moet kennen:
- **Laserfysica**: principe gestimuleerde emissie, kenmerken laserlicht
- **Lasertypes**: CO₂ vs Fiber vs DDL — golflengte, voordelen, nadelen
- **Absorptie**: golflengte + invalshoek bepalen absorptie; Fresnel; combinatie laser–materiaal
- **Bundelkwaliteit**: BPP en M²; wat betekent een lage waarde
- **Lasersnijden**: principeschema, rol snijgas, smeltsnijden vs brandsnijden
- **Problemen**: dross, inbranding, plasmavorming — oorzaak en gevolg
