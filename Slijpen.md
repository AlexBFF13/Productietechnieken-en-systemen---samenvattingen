# Les 8 — Slijpen (Grinding)
**KU Leuven · Productietechnieken en Systemen · Prof. Sylvie Castagne**

---

## Inhoudsopgave

1. [Wat is slijpen?](#1-wat-is-slijpen)
2. [Principe: hoe werkt slijpen?](#2-principe-hoe-werkt-slijpen)
3. [Snijmechanismen](#3-snijmechanismen)
4. [Parameters en hoofdwetten](#4-parameters-en-hoofdwetten)
5. [Slijpen of frezen/draaien?](#5-slijpen-of-frezendraaien)
6. [De slijpschijf](#6-de-slijpschijf)
7. [Thermische aspecten](#7-thermische-aspecten)
8. [Onderhoud van de slijpschijf](#8-onderhoud-van-de-slijpschijf)
9. [Slijpmachines](#9-slijpmachines)
10. [Nabewerkingen](#10-nabewerkingen)

---

## 1. Wat is slijpen?

Slijpen is een **materiaalafnameproces** waarbij kleine harde korrels (abrasieve korrels) het oppervlak van een werkstuk wegnemen bij hoge snijsnelheid en zeer kleine indringdiepten. De korrels zijn samengebonden in een slijpschijf die met hoge rotatiesnelheid draait.

Slijpen valt onder de bredere categorie van **abrasieve bewerkingsmethodes** (abrasive machining). Het onderscheidende kenmerk tegenover draaien of frezen is dat de snijkanten — de individuele korrels — **geometrisch ongedefinieerd** zijn. Bij een frees weet je precies hoeveel snijkanten er zijn, hoe ze georiënteerd zijn, en wat de spaanhoek is. Bij slijpen zijn al die parameters willekeurig: elke korrel heeft een andere vorm, oriëntatie, en positie op het oppervlak van de schijf.

Afhankelijk van hoe de korrels zijn samengebonden, spreekt men van:
- **Vrije korrels** — los in vloeistof of pasta gemengd (bij lappen en polijsten)
- **Gebonden op een riem** — kunsthars op een band (bandslijpen)
- **Dicht verpakt in een schijf of steen** — korrels samengehouden door een bindmiddel (de klassieke slijpschijf)

> **Definitie (DIN 8589):** Slijpen = bewerking met geometrisch ongedefinieerde snijkanten, waarbij het aantal snijkanten, de spaanhoeken, en de positie van de snijkanten op het werkstukoppervlak niet vastgelegd zijn.

---

## 2. Principe: hoe werkt slijpen?

### Analogie met frezen

Je kan een slijpschijf beschouwen als een frees met **enorm veel, willekeurig gevormde snijkanten**. In plaats van een beperkt aantal getande snijkanten die netjes gepositioneerd zijn, heeft een slijpschijf duizenden kleine korrels verspreid over het oppervlak — elk een potentiële snijkant.

Twee fundamentele verschillen met frezen en draaien:
- De **spaanhoek** van de korrels is **bijna altijd sterk negatief** — de korrel snijdt dus niet efficiënt maar werkt meer als een bottige schaver.
- De **snijsnelheid** is veel hoger (tientallen tot meer dan 100 m/s tegenover enkele m/s bij frezen).

### Geometrie en bewegingen

Bij rondslijpen (cilindrisch slijpen) draait de slijpschijf én het werkstuk elk om hun eigen as. De snijsnelheid $v_s$ (of $v_c$) is de omtreksnelheid van de slijpschijf, typisch 20–100 m/s. De snelheid van het werkstuk $v_w$ is een stuk lager.

Andere bewegingsparameters:
- $v_{fa}$, $v_{fr}$, $v_{ft}$ — voedingssnelheden in axiale, radiale of tangentiële richting
- $a_e$ — snedediepte (depth of cut)
- $a_p$ — verspaningsbreedte
- $b_s$ — breedte van de slijpschijf

### Vlakslijpen versus rondslijpen

- **Vlakslijpen** (surface grinding): het werkstuk ligt op een tafel en beweegt heen en terug onder de draaiende schijf. Bedoeld voor platte oppervlakken.
- **Rondslijpen** (cylindrical grinding): het werkstuk draait om zijn as, net als bij draaien. Kan zowel **uitwendig** (de buitenzijde van een cilinder slijpen) als **inwendig** (een boring slijpen).

---

## 3. Snijmechanismen

Niet elke korrel die het werkstuk raakt, snijdt ook effectief materiaal weg. Er zijn drie mogelijke interacties:

### Cutting (snijden)
De korrel dringt diep genoeg in het oppervlak door om werkelijk een span te genereren. Dit is het gewenste mechanisme: materiaal wordt weggenomen.

### Plowing (ploegen)
De korrel dringt iets in het oppervlak maar genereert geen span. In plaats daarvan vormt het oppervlak plastisch om: het materiaal wordt opzijgeduwd zonder te breken. Geen materiaalverwijdering, wel energieverbruik en oppervlaktedeformatie.

### Rubbing (wrijven)
De korrel raakt het oppervlak maar dringt er niet in. De korrel wrijft over het oppervlak. Er wordt energie verbruikt door wrijving, maar er is geen snijden en geen omvormen. Resulteert voornamelijk in warmteproductie.

### Wanneer welk mechanisme?

Dit hangt af van het **specifiek spaandebiet $Q'_w$** (zie sectie 4):

- Bij **lage $Q'_w$**: rubbing en plowing domineren → weinig effectief materiaal wegnemen, veel warmte.
- Bij **hogere $Q'_w$**: het aandeel echte cutting neemt toe → efficiënter materiaalverwijdering.

> **Belangrijk voor examen:** De drie snijmechanismen (cutting, plowing, rubbing) en het effect van Q'w op welk mechanisme domineert.

---

## 4. Parameters en hoofdwetten

### Specifiek spaandebiet Q'w

$$Q'_w = \frac{\text{verspaand volume per tijdseenheid}}{\text{actieve schijfbreedte}} \quad \left[\frac{\text{mm}^3/\text{s}}{\text{mm}}\right]$$

Dit is de **specifieke materiaalafnamesnelheid** — hoeveel volume je per seconde en per mm schijfbreedte wegneemt. Het is de centrale parameter in slijpen: een hogere $Q'_w$ betekent productiever werken, maar ook hogere temperaturen en meer slijtage.

### Equivalente spaandikte (snededikte) $h_{eq}$

$$h_{eq} = \frac{Q'_w}{v_s}$$

Dit is de dikte van een theoretische span die je zou krijgen als elk materiaalaandeel in één keer werd weggenomen. In de praktijk zijn de spanen veel dunner en talrijker, maar deze parameter laat toe om processen te vergelijken.

**Intuïtie:** Als $Q'_w$ hoog is maar $v_s$ ook hoog, dan blijft $h_{eq}$ beperkt — de schijf draait zo snel dat elke korrel slechts een dun laagje snijdt. Als $v_s$ laag is maar $Q'_w$ hoog, dan moeten de korrels dikker snijden → meer belasting per korrel → meer slijtage.

### Slijpverhouding G

$$G = \frac{V_w}{V_s} = \frac{\text{verspaand volume werkstuk}}{\text{versleten volume slijpschijf}}$$

G is een maat voor de efficiëntie van de schijf: hoeveel werkstukmateriaal wordt weggenomen per eenheid van schijfslijtage. Een hoge G is wenselijk — de schijf slijt traag terwijl het werkstuk snel verspaand wordt.

### Keuze van snijparameters

De keuze van parameters hangt af van meerdere factoren die vaak in spanning staan:

| Factor | Toelichting |
|---|---|
| **Nauwkeurigheid** | Kleine diepten, lage $Q'_w$ → meer controle |
| **Oppervlakte-integriteit** | Ruwheid, restspanningen — worden sterk beïnvloed door thermische belasting |
| **Slijpverhouding G** | Wil je de schijf lang laten meegaan |
| **Standvolume** | Hoeveel werkstukken per slijpschijf |
| **Slijpkrachten en vermogen** | Machinecapaciteit, klemkrachten |
| **Kostprijs** | Slijpen is duur → zo efficiënt mogelijk werken |

In de praktijk worden **slijpdiagrammen** gebruikt om de juiste combinatie van parameters te kiezen.

---

## 5. Slijpen of frezen/draaien?

### Waarom is slijpen duurder?

Slijpen heeft **hogere specifieke krachten** dan draaien of frezen — minstens een factor 10 hoger. Dit komt door:
- de negatieve spaanhoek van de korrels (krachtige, inefficiënte snijbeweging)
- het simultane rubbing en plowing naast cutting

Daardoor is het **verspaningsdebiet** bij slijpen laag: je neemt veel energie op per mm³ weggenomen materiaal. Slijpen is dus een **kostbare bewerking** — je kiest er bewust voor.

### Wanneer kies je wél voor slijpen?

Er zijn situaties waar slijpen de enige of beste optie is:

- **Nauwkeurigheid** — toleranties van µm zijn haalbaar, niet met draaien of frezen
- **Oppervlaktekwaliteit** — slijpen geeft Ra-waarden die andere bewerkingen niet halen
- **Harde werkstukken** — geharde staalonderdelen, keramiek — te hard voor conventionele snijgereedschappen
- **Lage toelaatbare bewerkingskrachten** — dunne of fragiele onderdelen die niet te hard belast mogen worden
- **Geringe dikte van de te verwijderen laag** — als je maar een paar µm tot honderden µm hoeft te verwijderen, is slijpen het meest geschikte proces

```
Typisch productiepad voor precisieonderdelen:

ruw staal
--> draaien/frezen (grove bewerking, snel)
--> harden (warmtebehandeling)
--> slijpen (fijne bewerking, nauwkeurig)
--> klaar
```

---

## 6. De slijpschijf

De slijpschijf is geen homogeen blok — ze bestaat uit drie componenten die samen het gedrag bepalen:

$$V_k + V_b + V_p = 1$$

- $V_k$ = volumefractie **korrels** (het eigenlijke snijmateriaal)
- $V_b$ = volumefractie **bindmiddel** (houdt korrels vast)
- $V_p$ = volumefractie **poriën** (luchtspleten, ruimte voor spaanders)

### 6.1 Slijpkorrelmateriaal

De korrels moeten harder zijn dan het werkstuk. Gangbare materialen:

| Materiaal | Symbool | Eigenschappen | Toepassing |
|---|---|---|---|
| **Korund** (aluminiumoxide) | Al₂O₃ | Taai, breed inzetbaar | Staal, RVS |
| **Siliciumcarbide** | SiC | Harder dan korund, brozer | Gietijzer, non-ferrometalen, keramiek |
| **Borcarbide** | BC | Zeer hard | Harde materialen |
| **CBN** (kubisch bornitride) | CBN | Extreem hard, warmtestabiel | Geharde staalsoorten |
| **Diamant** | D | Hardste materiaal | Keramiek, glas, hardmetaal |

Belangrijk concept: **friability** = de neiging van de korrel om te breken bij belasting. Een friabele korrel breekt bij overbelasting en stelt een nieuw snijvlak bloot. Dat is gunstig: de korrel zelf vernieuwd zijn snijkant. Een niet-friabele korrel wordt stom en slijt weg als geheel.

> Harder werkstukmateriaal vereist hardere korrels — maar ook een zachter wiel (zie 6.3).

### 6.2 Korrelgrootte

De korrelgrootte bepaalt de verhouding tussen ruwheid en afnamesnelheid:

- **Grotere korrels** → hogere afnamesnelheid, ruwer oppervlak
- **Kleinere korrels** → betere oppervlaktekwaliteit, lagere afnamesnelheid

Voor standaard slijpen: korrelgrootte **80–380 µm**
(ter vergelijking: honen 30–280 µm, lappen 5–60 µm)

Het **grit number** (korrelnummer) werkt omgekeerd: een **hoger grit number** betekent **kleinere korrels** (fijner schuurpapier). Dit is een valkuil bij het lezen van specificaties.

### 6.3 Hardheidsgraad van de schijf

**Opgelet:** de hardheid van de schijf is *niet* de hardheid van de korrels — het is een maat voor **hoe sterk het bindmiddel de korrels vasthoudt**.

$$\text{Harde schijf} = \text{hoog } V_b \Rightarrow \text{korrels worden sterk vastgehouden}$$
$$\text{Zachte schijf} = \text{laag } V_b \Rightarrow \text{korrels breken sneller los}$$

**Keuzeregel (belangrijk voor examen):**

| Werkstukmateriaal | Kies... | Waarom? |
|---|---|---|
| **Zacht materiaal** | Harde schijf | Zachte materialen slijpen de schijf anders snel op → harde binding houdt korrels langer vast |
| **Hard materiaal** | Zachte schijf | Harde materialen maken korrels snel stom → zachte binding laat stomme korrels sneller los zodat nieuwe scherpe korrels vrijkomen |

- **Harde schijven**: voor hoge verspaningsvolumes en zachte werkstukken
- **Zachte schijven**: voor harde werkstukken en toepassingen met lage afnamesnelheid

### 6.4 Structuur van de schijf (poriënvolume)

De verhouding $V_p / V_k$ bepaalt of de schijf **open** of **dicht** is:

- **Open structuur** ($V_p$ groot, $V_k$ klein): veel ruimte voor spaanders — aanbevolen wanneer er grote hoeveelheden materiaal worden verwijderd of wanneer spaanopstapeling een probleem is.
- **Dichte structuur** ($V_k$ groot, $V_p$ klein): betere oppervlakteafwerking en maatcontrole — voor fijne bewerkingen.

### 6.5 Aard van het bindmiddel

| Type | Eigenschappen | Gebruik |
|---|---|---|
| **Keramisch (vitrified)** | Stijf, poreus, goede spaanruimte | Meest gebruikt (~75% van alle schijven) |
| **Silicaat** | Soepeler dan keramisch | Koelere slijpbewerking |
| **Elastische bindingen** (rubber, hars) | Flexibel, dempt trillingen | Afsmijpschijven, polijsten |
| **Metaalbindingen** | Sterke vasthechting, lang standleven | Altijd gebruikt bij diamant- en CBN-korrels |

### 6.6 Contactlengte

De **contactlengte** is de lengte van de baan die een korrel aflegt over het werkstukoppervlak bij één passage. Ze bepaalt mee hoelang elke korrel warmte genereert en hoe dik de span is.

Voor uitwendig rondslijpen:

$$l_c \approx \sqrt{a_e \cdot d_s}$$

waarbij $a_e$ de snedediepte is en $d_s$ de schijfdiameter. De exacte formule verschilt per slijpvorm.

### 6.7 Classificatie van slijpschijven (DIN ISO 525:2000)

De standaard classificeert schijven van aluminium oxide (korund) en siliciumcarbide. In de specificatiestring van een schijf vind je achtereenvolgens: korrelmateriaal – korrelnummer – hardheidsgraad – structuurnummer – bindmiddeltype.

---

## 7. Thermische aspecten

### Waarom is warmte een probleem bij slijpen?

Slijpen genereert **meer warmte per mm³ verspaand materiaal** dan enig ander bewerkingsproces. De oorzaken:

1. **Hoge snijsnelheid** — enorm veel energie per tijdseenheid
2. **Negatieve spaanhoek** — minder efficiënt snijden → meer energie omgezet in warmte
3. **Lang afschuifvlak** — de spanvorming per korrel kost meer energie
4. **Hoge normaalkrachten** — sterke wrijving
5. **Rubbing en plowing** — een groot deel van de energie wordt niet in spanning geïnvesteerd maar verspreid als warmte in het werkstuk

Het resultaat: de temperatuur in de **contactzone** kan oplopen tot 600–1000 °C en zelfs hoger.

### Gevolgen van overmatige warmte

| Effect | Beschrijving |
|---|---|
| **Vonken** | Zichtbaar teken van hoge temperaturen (verbrandende spanen) |
| **Temperen (tempering)** | Geharde staalonderdelen verliezen hardheid door heruitgloeien in de HAZ |
| **Verbranden (burning)** | Oxidatie van het oppervlak — zichtbaar als verkleuringen |
| **Micro-scheurtjes** | Thermische spanning bij snel opwarmen en afkoelen |
| **Restspanningen** | Trekspanningen in het oppervlak → verminderde vermoeiingsweerstand |
| **HAZ (Heat-Affected Zone)** | Warmte-beïnvloede zone in het werkstuk |

### Meer micro-scheuren bij

- Gebruik van **harde slijpstenen** (bindmiddel houdt korrels langer vast → stomme korrels blijven werken → meer warmte)
- Slijpstenen met **minder friabele korrels** (korrels breken minder snel → minder zelfscherpend effect → hogere temperaturen)

### Koeling

De oplossing is koeling met een slijpvloeistof (koelvloeistof of koelsmeermiddel). De koelvloeistof:
- Voert warmte weg uit de contactzone
- Vermindert wrijving
- Spoelt spaanders weg
- Verlengt de standtijd van de schijf

---

## 8. Onderhoud van de slijpschijf

### Dressing / Richten

Na verloop van tijd raken de korrels aan het oppervlak van de schijf **stom** (worn flat = slijtplateau) of **verstopt** (spaanders vastgeklemd). De schijf snijdt dan slecht, genereert meer warmte, en verliest zijn geometrische nauwkeurigheid.

**Dressing** (ook: richten, afrrichten) is het opnieuw conditioneren van het schijfoppervlak:
- Stomme korrels worden weggebroken zodat scherpe korrels vrijkomen
- Het profiel van de schijf wordt hersteld
- Vereist gespecialiseerde gereedschappen (diamantrollen, single-point dresser, ...)

Het proces heeft twee stappen:
1. **Profileren (truing):** schijf terugbrengen op de juiste geometrie (cirkelvormig, vlak, of een specifiek profiel)
2. **Afrrichten (sharpening/dressing):** schijfoppervlak scherpstellen zodat de korrels goed snijden

### Balanceren

Een slijpschijf is een grote roterende massa die nooit volledig homogeen is. Bij hoge toerentallen (die nodig zijn voor de vereiste snijsnelheid) leidt elke onbalans tot **trillingen**. Die trillingen zetten zich om in:
- Oppervlaktegolven op het werkstuk (waviness)
- Lagerslijtage op de machine
- Gevaar bij brekende schijven

**Balanceren** van de spil met de gemonteerde slijpschijf is dan ook een standaardprocedure voor elke opspanning.

---

## 9. Slijpmachines

### Analogie met conventionele machines

Slijpmachines zijn qua opbouw vergelijkbaar met frees- en draaibanken:
- Ze hebben een **spil** die de slijpschijf aandrijft
- Een **werkstukopspanning** (tafel, centers, of klemming)
- **Bewegingsassen** voor de voedings- en snijbewegingen

Het grote verschil is dat de schijf bij hoge toerentallen draait en de machine stijf en trillingsvrij moet zijn.

### Cilindrisch slijpen (Cylindrical grinding)

Voor het slijpen van cilindrische vlakken, met het werkstuk opgespannen tussen centers of in een klauwplaat:
- **Uitwendig rondslijpen** — buitendiameter van een as
- **Inwendig rondslijpen** — binnendiameter van een boring (met een kleine slijpschijf aan het uiteinde van een spindel)

### Vlakslijpen (Surface grinding)

Het werkstuk ligt op een magnetische tafel of kleminrichting. De schijf beweegt over het oppervlak:
- Met een **cilindrische schijf** (omtreksvlakslijpen)
- Met een **komsteen** (frontvlakslijpen, pendant van de freesbewerking)

### Centerloze slijpmachines (Centerless grinding)

Dit is een bijzondere en industrieel veel gebruikte variant. Het werkstuk wordt **niet tussen centers opgespannen** maar rust op een steunliniaal en wordt aangedreven door een tweede, kleinere schijf: de **regelschijf** (regulating wheel).

```
Opstelling centerloze slijper:

[Slijpschijf]    [Werkstuk]    [Regelschijf]
    -->            draait           -->
              (steunliniaal onderaan)
```

De regelschijf draait langzamer en heeft een hogere wrijvingscoëfficiënt dan de slijpschijf. Daardoor bepaalt de regelschijf de omtreksnelheid van het werkstuk:

$$f_{n,\text{werkstuk-regelschijf}} > f_{n,\text{werkstuk-slijpschijf}}$$
$$f_{w,\text{regelschijf}} > f_{w,\text{slijpschijf}}$$

Er zijn twee modi:

**Doorvoerslijpen (through-feed grinding):**
De regelschijf staat schuin (een kleine hoek $\alpha$). Daardoor krijgt het werkstuk een axiale voedingscomponent en beweegt het langs de schijven in de langsrichting. Ideaal voor **continuproductie van lange cilindrische stukken** (assen, pennen).

**Insteekslijpen (plunge grinding):**
De regelschijf beweegt radiaal naar het werkstuk toe tot de gewenste diameter bereikt is. Geen axiale beweging. Gebruikt voor kortere onderdelen of wanneer schouders aanwezig zijn.

> **Voordelen centerloze slijper:** geen opspanning nodig → snelle cyclustijden, geschikt voor massa-productie.

---

## 10. Nabewerkingen

Wanneer je na het slijpen nóg een fijner oppervlak nodig hebt, ga je naar de **nabewerkingen**. Deze processen werken met kleinere korrels en verwijderen slechts heel weinig materiaal — ze verbeteren de oppervlaktekwaliteit van een al nauwkeurig bewerkt vlak.

```
Korrelgroottevergelijking:

Slijpen:      80 – 380 µm
Honen:        30 – 280 µm
Lappen:        5 –  60 µm   (fijnst)
```

### 10.1 Honen

**Doel:** Nabewerken van boringen (cilindrische inwendige vlakken) of uitwendige cilindrische vlakken. Typisch na het slijpen of fijnboren van cilinderlopers, versnellingsbaklagers, hydraulische cilinders.

**Principe:** Een hoongereedschap met meerdere abrasieve stenen (honing stones) gecombineerd in een cilindrische houder wordt in de boring geplaatst.

- **Hoofdbeweging:** Roterend
- **Voedingsbeweging:** Axiaal (heen en terug)

De combinatie van roteren en axiaal bewegen creëert een **kruisgestreept patroon** op het oppervlak — het typische "hatch pattern" dat je herkent in cilinderlopers. Dat patroon helpt bij het vasthouden van smeermiddel.

### 10.2 Superfijnen (Superfinishing / Microhoning)

**Doel:** Nabewerken van **uitwendige cilindrische vlakken** — typisch assen, rollagers. Verwijdert de allerlaatste ruwheidstopjes.

**Principe:** Een slijpsteentje waarvan de **vorm is aangepast aan de diameter van het cilindervlak** wordt met een lichte oscillerende beweging over het draaiende werkstuk geleid. De druk is zeer laag.

- Cilindrisch microhonen (het werkstuk draait)
- Centerloze microhoning (centerless microhoning)

### 10.3 Lappen

**Doel:** Extreme oppervlaktekwaliteit en vlakheid bereiken op vlakke of cilindrische oppervlakken. Gebruikt in precisie-optiek, vlakke afdichtingsvlakken, naaiden van pompcomponenten.

**Principe:** Abrasieve korrels zijn gemengd in een vloeistof of pasta (het **lapmiddel**). Dit mengsel zit tussen het werkstuk en een zachte tegenplaat (lepschijf). De relatieve beweging tussen werkstuk en lepschijf wrijft de korrels over het werkstuk.

- Werkstukken worden geplaatst tussen twee roterende lepschijven
- Een **kooi** controleert de positie en beweging van de werkstukken
- Verwijdert slechts enkele µm — gebruikt uitsluitend om oppervlaktekwaliteit te verbeteren, niet om materiaal weg te halen

> **Belangrijk voor examen:** De drie nabewerkingen en hun toepassingsgebied — honen voor boringen, superfijnen voor uitwendige cilinders, lappen voor vlakke of cilindrische oppervlakken met extreme vereisten.

---

## Samenvatting: Slijpen in één oogopslag

| Aspect | Kern |
|---|---|
| **Wat** | Materiaalafname met gebonden abrasieve korrels bij hoge snijsnelheid |
| **Snijkanten** | Ongedefinieerd — willekeurig gevormde korrels |
| **Spaanhoek** | Sterk negatief |
| **Snijmechanismen** | Cutting / Plowing / Rubbing |
| **Wanneer kiezen** | Nauwkeurigheid, harde materialen, oppervlaktekwaliteit |
| **Nadeel** | Hoge specifieke krachten → laag debiet → dure bewerking |
| **Schijfsamenstelling** | Korrels + bindmiddel + poriën ($V_k + V_b + V_p = 1$) |
| **Hard wiel voor** | Zachte werkstukken |
| **Zacht wiel voor** | Harde werkstukken |
| **Thermisch gevaar** | Temperen, verbranden, restspanningen in HAZ |
| **Onderhoud** | Dressing (scherpstellen), balanceren |
| **Nabewerkingen** | Honen → Superfijnen → Lappen (steeds fijner) |

---

---

## Wat je echt moet kennen

- Wat "geometrisch ongedefinieerde snijkanten" betekent en hoe slijpen daarin verschilt van frezen
- De drie snijmechanismen: cutting, plowing, rubbing — en welke gewenst is
- Het effect van het specifiek spaandebiet Q'w op welk mechanisme domineert
- De formule voor equivalente spaandikte: h_eq = Q'w / v_s
- Wat de slijpverhouding G betekent (V_w / V_s) en waarom een hoge G wenselijk is
- Wanneer je kiest voor slijpen in plaats van draaien/frezen (hardheid, nauwkeurigheid, dunne laag)
- De drie componenten van de slijpschijf: V_k + V_b + V_p = 1
- De keuzeregel voor schijfhardheid: zacht werkstuk → harde schijf, hard werkstuk → zachte schijf
- Wat friability is en waarom het gunstig is bij korrels
- Het verschil tussen open en dichte schijfstructuur en wanneer elk te gebruiken
- Waarom slijpen meer warmte genereert dan andere processen (negatieve spaanhoek, rubbing, hoge snelheid)
- De gevolgen van overmatige warmte: temperen, verbranden, micro-scheurtjes, restspanningen
- Wat dressing is en waarom het nodig is (stomme korrels, verstopt oppervlak)
- Het verschil tussen profileren (truing) en afrrichten (sharpening)
- Waarom balanceren van de slijpschijf noodzakelijk is (trillingen → oppervlaktegolven)
- Het principe van centerloze slijpen en het verschil tussen doorvoer- en insteekslijpen
- De drie nabewerkingen en hun toepassingsgebied:
  - Honen → boringen (kruisgestreept patroon)
  - Superfijnen → uitwendige cilinders
  - Lappen → vlakke/cilindrische vlakken met extreme kwaliteitseisen

---

*Gebaseerd op slides: "Les 8 Slijpen SC 2526" — Prof. Sylvie Castagne, KU Leuven (AJ 25/26)*
