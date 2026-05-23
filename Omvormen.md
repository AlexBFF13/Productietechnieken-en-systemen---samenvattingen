# Deel 4 – Omvormen (Les 10 & 11)

---

## Wat is omvormen?

Omvormen (*metal forming*) is een productieproces waarbij je een metalen werkstuk zijn definitieve vorm geeft door het **opzettelijk plastisch te vervormen**. Dat klinkt eenvoudig, maar het verschil met andere bewerkingen is cruciaal: je verwijdert geen materiaal (zoals bij verspanen), en je voegt niets toe (zoals bij lassen). Het volume blijft constant — je hervormt alleen de geometrie.

Concreet: je oefent krachten uit die groter zijn dan de vloeigrens van het materiaal, zodat het metaal permanent van vorm verandert.

Omvormen wordt ingedeeld in twee grote categorieën:

- **Massief omvormen** (bulk forming): het volledige volume van het werkstuk vervormt. Voorbeelden: walsen, smeden, extruderen, draadtrekken.
- **Plaatomvormen** (sheet forming): dunne platen worden gevormd zonder het volume fundamenteel te wijzigen. Voorbeelden: dieptrekken, buigen, stempelen.

Les 10 behandelt de basisprincipes van vervorming én massief omvormen (walsen). Les 11 gaat verder met plaatomvormen, specifiek buigen.

---

## Basisprincipes van vervorming

### Elastisch vs plastisch — het verschil

Wanneer je een kracht uitoefent op een metaal, reageert het op twee manieren afhankelijk van hoe groot die kracht is:

**Elastische vervorming** gebeurt bij kleine krachten. De atomen worden iets uit hun evenwichtspositie geduwd, maar zodra je de kracht wegneemt, veren ze terug. Het werkstuk keert terug naar zijn oorspronkelijke vorm. Het volume verandert licht.

**Plastische vervorming** treedt op als de kracht groot genoeg is om de vloeigrens te overschrijden. De atomen glijden dan collectief over elkaar heen (*dislocatiebeweging*) in plaats van alleen uit te rekken. De vervorming blijft permanent, ook als je de kracht wegneemt. Het volume blijft **constant** bij plastische vervorming — dit is een experimenteel vastgesteld feit.

Bij omvormen wil je altijd plastische vervorming bereiken: dat is het doel. Elastische vervorming is onvermijdelijk aanwezig maar is bijzaak.

### Volumebehoud

Het feit dat volume constant blijft bij plastische vervorming is enorm nuttig in de praktijk: het laat je toe de afmetingen van het eindproduct te berekenen als je het uitgangsproduct kent.

Voorbeeld — een cilinder die wordt samengedrukt:

$$\pi R_0^2 H_0 = \pi R^2 H \quad \Rightarrow \quad R = R_0 \sqrt{\frac{H_0}{H}}$$

Als je de hoogte halveert, neemt de straal toe met factor √2. Simpel, maar fundamenteel.

---

## Spanning en rek

### Waarom spanning en geen kracht?

Als je twee staven trekt met dezelfde kracht, maar de ene heeft dubbel zo grote doorsnede, vervormt de kleinere veel meer. De **kracht** op zich zegt dus niets over het gedrag van het materiaal — je moet die kracht normeren over de doorsnede. Dat is **spanning**:

$$\sigma = \frac{F}{A}$$

Op dezelfde manier: als je een staaf van 1000 mm met 1 mm verlengt en een staaf van 100 mm met 1 mm verlengt, is de tweede proportioneel 10× meer vervormd. Vervorming moet genormeerd worden — dat is **rek**.

### Ware rek vs nominale rek

In de plaatleer kennen we *nominale rek* (engineering strain):

$$e = \frac{\Delta H}{H_0} = \frac{H - H_0}{H_0}$$

Maar bij grote vervormingen (zoals bij omvormen) is dit niet meer nauwkeurig. We gebruiken **ware rek** (true strain):

$$\varepsilon = \ln\left(\frac{H}{H_0}\right)$$

Het verschil: nominale rek telt altijd vanaf de beginlengte, terwijl ware rek incrementeel optelt. Bij kleine vervormingen zijn ze ongeveer gelijk; bij grote vervormingen weerspiegelt ware rek beter wat er werkelijk in het materiaal gebeurt.

- Drukspanning (werkstuk wordt korter) → ε < 0
- Trekspanning (werkstuk wordt langer) → ε > 0

### Poisson's ratio en volumebehoud

In 3D zijn er drie spanningsrichtingen en drie rekrichtingen. Ze zijn gekoppeld via de elasticiteitsmodulus E en de **Poisson's ratio ν**:

$$\varepsilon_1 = \frac{1}{E}[\sigma_1 - \nu(\sigma_2 + \sigma_3)]$$

Bij **plastische vervorming** is het volume constant, wat wiskundig neerkomt op:

$$\varepsilon_1 + \varepsilon_2 + \varepsilon_3 = 0 \quad \Rightarrow \quad \nu = 0.5$$

Voor elastische vervorming geldt 0 < ν < 0.5. Zodra je volledig plastisch vervormt, wordt ν = 0.5.

> **belangrijk voor examen**: bij plastische vervorming is ν = 0.5 en is het volume constant.

---

## De verstevigingskromme

### Vloeispanning en verstevigingsfunctie

Het verband tussen spanning en rek bij plastische vervorming wordt beschreven door de **verstevigingsfunctie** (*flow rule* of *strain hardening law*):

$$\sigma = K \varepsilon^n$$

waarbij:
- **K** = sterkteconstante van het materiaal (MPa)
- **n** = verstevigingsexponent (0 < n < 1)
- **σ** = ware spanning
- **ε** = ware rek

Deze kromme geeft aan hoeveel spanning er nodig is om het materiaal te laten vloeien bij een gegeven hoeveelheid vervorming. Bij omvormen werken we altijd met ware spanning en ware rek.

### Versteviging (work hardening / strain hardening)

Wanneer je een metaal plastisch vervormt, wordt het **harder en sterker**, maar ook **brosser**. Dit heet versteviging. Het mechanisme zit op atomair niveau: bij plastische vervorming bewegen dislocaties door het kristalrooster, maar ze blokkeren elkaar steeds meer. Bijkomende vervorming vereist hogere spanning.

Praktisch gevolg: na een bepaalde mate van koudverstevigen is het materiaal zo hard dat verdere vervorming bijna onmogelijk wordt zonder het te beschadigen. Oplossing: **gloeien** (*annealing*) — het materiaal verwarmen tot de rekristallisatietemperatuur, waardoor de dislocatiedichtheid afneemt en de ductiliteit terugkeert.

---

## Omvormtemperatuur

De temperatuur waarbij je omvormt, heeft een enorme invloed op het proces.

```
Koud          Halfwarm        Warm
|-------------|----------------|-------------|
Tk         0.3Tsm          0.5Tsm       Tsm
```

(Tsm = smelttemperatuur in Kelvin)

- **Koudomvormen** (cold forming): rond kamertemperatuur. Versteviging treedt op → hogere krachten nodig, maar betere maatnauwkeurigheid en oppervlakteafwerking.
- **Halfwarmomvormen** (warm forming): tussen kamertemperatuur en rekristallisatietemperatuur. Versteviging is gedeeltelijk verminderd.
- **Warmomvormen** (hot forming): boven rekristallisatietemperatuur. Het metaal rekristalliseert tijdens het vervormen → geen versteviging, lagere krachten, grote vervormingen mogelijk, maar minder nauwkeurig.

### Invloed op de materiaalwet

Bij **kamertemperatuur** is de rek dominant:
$$\sigma = K\varepsilon^n$$

Bij **hoge temperatuur** wordt de reksnelheid dominant:
$$\sigma = C\dot{\varepsilon}^m$$

waarbij $\dot{\varepsilon} = \frac{d\varepsilon}{dt}$ de reksnelheid is en **m** de reksnelheidsexponent.

---

## Vloeicriteria

Bij omvormen werk je bijna nooit in een puur uniaxiale situatie — er zijn krachten in meerdere richtingen. Je moet weten wanneer het materiaal begint te vloeien onder die gecombineerde belasting. Daar dienen de **vloeicriteria**.

### Tresca-criterium (maximale schuifspanning)

Vloeien treedt op wanneer het verschil tussen de grootste en kleinste hoofdspanning gelijk is aan de vloeispanning:

$$\sigma_{\max} - \sigma_{\min} = Y$$

Eenvoudig te gebruiken, maar iets minder nauwkeurig.

### Von Mises-criterium

Vloeien treedt op wanneer de effectieve spanning Y bereikt:

$$\sigma = \sqrt{\frac{1}{2}\left[(\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2\right]} = Y$$

Von Mises is fysisch correcter en wordt vaker gebruikt bij numerieke simulaties.

De bijbehorende effectieve rek is:

$$\varepsilon = \frac{\sqrt{2}}{3}\sqrt{(\varepsilon_1 - \varepsilon_2)^2 + (\varepsilon_2 - \varepsilon_3)^2 + (\varepsilon_3 - \varepsilon_1)^2}$$

> **belangrijk voor examen**: ken het verschil Tresca vs Von Mises, en weet hoe je effectieve spanning/rek gebruikt om vloeien te voorspellen.

### Vlakke vervormingstoestand

Een nuttige vereenvoudiging bij processen zoals walsen van brede platen is de **vlakke vervormingstoestand** (*plane strain*): het materiaal kan niet vrij uitbreiden in de breedterichting:

$$\varepsilon_2 = 0 \quad \Rightarrow \quad \sigma_2 = \frac{\sigma_1 + \sigma_3}{2}$$

Met deze aanname vereenvoudigen de vloeicriteria aanzienlijk:
$$\sigma_3 - \sigma_1 = \frac{2}{\sqrt{3}} Y \quad \text{(Von Mises)}$$

---

## Arbeid bij omvormen

De energie die nodig is om een werkstuk te vervormen is gelijk aan de oppervlakte onder de spanning-rekcurve:

$$u = \int_0^{\varepsilon_f} \sigma \, d\varepsilon$$

Als σ = Kεⁿ geldt:

$$u = \frac{K \varepsilon_f^{n+1}}{n+1} = \bar{Y} \varepsilon_f$$

waarbij $\bar{Y}$ de **gemiddelde vloeispanning** is. Dit getal is handig omdat je ermee de gemiddelde weerstand van het materiaal over het hele proces samenvat in één waarde.

---

## Walsen

### Wat is walsen?

Walsen (*rolling*) is het meest gebruikte massieve omvormproces. Het werkstuk wordt door twee tegenroterende rollen geleid, die het samendrukken en tegelijk vooruit trekken via wrijving. Het resultaat: een dunnere, langere plaat of profiel.

```
Invoer
  --> [Rol]     [Rol]  --> Uitvoer (dunner, langer)
```

De rollen vervullen twee functies tegelijk:
1. Het werkstuk in de spleet trekken via **wrijving**.
2. Het werkstuk **samendrukken** om de dikte te verminderen.

### Soorten walsen

**Op basis van werkstukgeometrie:**
- *Vlakwalsen*: dikke platen dunner maken → plaatstaal, coilmateriaal.
- *Profielwalsen*: I-profielen, rails, staven... in specifieke dwarsdoorsneden walsen.

**Op basis van temperatuur:**
- *Warmwalsen*: boven rekristallisatietemperatuur, grote reductie mogelijk.
- *Koudwalsen*: onder rekristallisatietemperatuur, betere maatnauwkeurigheid, koudverstevigd eindproduct.

### Terminologie

- **Draft** (diktereductie): $d = h_0 - h_f$
- **Reductieverhouding**: $r = \frac{d}{h_0}$

Waarbij $h_0$ = begindikte en $h_f$ = einddikte.

### Walssnelheden en neutraal punt

Omdat het materiaal dunner wordt maar het volume constant blijft, moet het sneller bewegen aan de uitgang dan aan de ingang:

$$h_0 v_0 = h_f v_f \quad \Rightarrow \quad v_f > v_0$$

Ergens in het contactvlak tussen rol en werkstuk zijn de snelheden gelijk — dit is het **neutrale punt**:

- Vóór het neutrale punt: het werkstuk beweegt trager dan de rol → wrijving drijft het naar voren.
- Na het neutrale punt: het werkstuk beweegt sneller dan de rol → wrijving remt het.

De **forward slip** kwantificeert hoe snel het werkstuk uitloopt t.o.v. de rol:
$$s = \frac{v_f - v_r}{v_r}$$

De **reksnelheid** bij walsen:
$$\dot{\varepsilon} = \frac{v_r \ln(h_0/h_f)}{L}$$

waarbij $L = \sqrt{R \cdot d}$ de geprojecteerde contactlengte is.

### Wrijving en meeneemvoorwaarde

Zonder wrijving is walsen onmogelijk — de rollen zouden gewoon glijden over het werkstuk. De wrijvingskrachten zijn verantwoordelijk voor het "inslikken" van het materiaal.

Er bestaat een maximale diktereductie die afhangt van de wrijvingscoëfficiënt µ en de rolstraal R:

$$d_{\max} = \mu^2 R$$

De maximale meeneemhoek θ_max = arctan(µ). Als de werkelijke contacthoek groter is, kan de rol het werkstuk niet meer intrekken.

> **intuition**: grotere rollen en hogere wrijving → meer reductie per stap mogelijk.

### Walskracht en vermogen

**Gemiddelde druk** (benadering):
$$p_{av} \approx \frac{2h_0}{\mu w} \left(e^{\mu w/h_0} - 1\right) \sigma$$

**Walskracht** (vereenvoudigde benadering):
$$F \approx w L \bar{Y}_f \left(1 + \frac{\mu w}{2 h_{av}}\right)$$

waarbij $w$ de walscontactbreedte, $L = \sqrt{Rd}$, $h_{av} = (h_0 + h_f)/2$, en $\bar{Y}_f$ de gemiddelde vloeispanning.

**Koppel per rol:**
$$T_{approx} \approx \frac{F \cdot L}{2}$$

**Vermogen voor 2 rollen:**
$$P = 2\pi N F L$$

waarbij N het toerental is (toeren/min of rad/s).

> **belangrijk voor examen**: walsberekening — controleer meeneemvoorwaarde, bereken walskracht en vermogen.

---

---

# Deel 5 – Omvormen van plaat: Buigen (Les 11)

---

## Waarom plaatwerk?

Plaatwerk (*sheet metal*) is alomtegenwoordig: auto's, witgoed, behuizingen, vliegtuigen... De reden is eenvoudig:

- Hoge sterkte met laag gewicht.
- Goede oppervlakteafwerking (klaar voor lakken, anodiseren...).
- Uitstekend maatnauwkeurig.
- Lage kostprijs bij grotere series.

Het materiaal voor plaatbewerking is **anisotropisch** — het gedraagt zich anders in de walsrichting dan dwars erop. Dit heeft gevolgen bij o.a. buigen.

Plaatbewerkingen worden ingedeeld in:

- **Buigen** ← dit is de focus van les 11
- Dieptrekken
- Scheiden (snijden, ponsen...)

---

## Buigen — wat is het?

Buigen is het vormgeven van een werkstuk waarbij de plastische toestand hoofdzakelijk wordt veroorzaakt door een **buigend moment**. Je vervormt niet het volledige materiaalvolume uniform, maar je buigt het rond een as.

Toepassingsgebied: plaatmateriaal én profielmateriaal (balken, buizen, staven).

Bij buigen geldt altijd:
- De **binnenkant** van de buiging staat onder **druk** (korter worden).
- De **buitenkant** staat onder **trek** (langer worden).
- De **neutrale laag** zit ergens tussen beide zones en verandert in principe niet van lengte.

---

## Types buigprocessen

### Luchtbuigen (Air bending / vrijbuigen)

Het werkstuk ligt op twee steunpunten (de randen van de matrijs). De stempel drukt in het midden naar beneden en creëert zo een buiging. Het werkstuk raakt de matrijs **niet volledig** — vandaar "luchtbuigen". De buighoek hangt af van hoe ver de stempel daalt.

Voordeel: flexibel in hoek met dezelfde tooling.
Nadeel: meer terugvering (springback), minder herhaalbaar.

### Matrijsbuigen / V-buigen / U-buigen (Die bending / Bottoming)

Het werkstuk wordt volledig in de matrijs gedrukt en neemt de exacte matrijsvorm aan. Bij *bottoming* wordt hoge slotdruk gebruikt zodat de plastische vervorming in de buigzone maximaal is.

Voordeel: betere herhaalnauwkeurigheid, minder terugvering.
Nadeel: aparte matrijs nodig per vorm en hoek.

- **V-buigen**: stempel en matrijs zijn V-vormig. Begint als luchtbuigen, eindigt als matrijsbuigen.
- **U-buigen**: geeft definitieve U-profielen, vaak met een steunschijf om uitpuilen te voorkomen.

### Rolbuigen (Roll bending)

Drie rollen buigen het werkstuk in een grote radius. Door de relatieve positie van de rollen aan te passen, kan je de kromtestraal variëren. Gebruikt voor grote onderdelen zoals cilinders, bogen, en constructieprofielen.

---

## Plooiverlies en blankgrootte

### Waarom is dit belangrijk?

Als je een strip buigt, wordt de buitenkant uitgerekt en de binnenkant samengedrukt. De neutrale laag zit niet exact in het midden — ze verschuift iets naar de binnenkant. Als je de strip gewoon platgooit om de ongebogen lengte te meten, kom je te kort uit. Je moet **het plooiverlies meenemen in de berekening van de startlengte**.

Dit is cruciaal in de productie: je moet de blanke (ongebogen) strip op de juiste maat zagen vóór het buigen.

### Formule

De totale startlengte $l_0$ is:

$$l_0 = l_1 + l_b + l_2$$

waarbij:
- $l_1$, $l_2$ = lengte van de rechte stukken na het buigen (gegeven op de tekening).
- $l_b$ = **plooiverlies** (*bend allowance*).

Het plooiverlies:

$$l_b = \frac{\alpha}{360°} \cdot 2\pi \left(r_i + k \cdot \frac{s}{2}\right)$$

of in radialen:

$$l_b = \alpha \cdot \left(r_i + C_a \cdot s\right) \quad \text{met } C_a = \frac{k}{2}$$

Betekenis van de parameters:
- **α** = plooihoek (in graden of radialen)
- **r_i** = binnenste buigradius
- **s** = plaatdikte
- **k** = correctiefactor voor de positie van de neutrale as

### Correctiefactor k

De neutrale as zit niet op 50% van de plaatdikte maar iets meer naar de binnenkant:

| Verhouding r_i/s | Correctiefactor k |
|---|---|
| < 2 | 0.66 (uitrekken treedt op) |
| ≥ 2 | 1 (alleen buigen, geen netto uitrekking) |

De reden: bij een kleine buigradius t.o.v. de dikte is de buitenste laag sterk uitgerekt. De vloeigrens in compressie is iets hoger dan in trek, dus de binnenzijde weerhoudt zich beter → de neutrale as verschuift richting binnenzijde.

In de praktijk bestaan meer gedetailleerde tabellen (zie appendix 1 in de cursustekst en Labo pp07).

> **belangrijk voor examen**: blankgrootte berekenen met de plooiverliesformule is een typisch rekenexamen.

---

## Terugvering (Springback)

### Wat is springback?

Na het buigen, wanneer je de stempel verwijdert, veert het werkstuk **gedeeltelijk terug** naar zijn oorspronkelijke vorm. Dit is onvermijdelijk: elke plastische vervorming gaat gepaard met een elastische component. Wanneer de kracht wegvalt, veert het elastische deel terug.

Gevolg: de werkelijke buighoek na het loslaten is **kleiner** dan de hoek die je tijdens het buigen hebt opgelegd. De buigradius is ook iets groter geworden.

### Formule

De terugveerhoek:

$$\alpha_t = 3 \frac{R_e}{E} \cdot \frac{\alpha_i}{r_i + C_a \cdot s}$$

waarbij:
- $R_e$ = rekgrens van het materiaal
- $E$ = elasticiteitsmodulus
- $\alpha_i$ = opgelegde buighoek
- $r_i$ = binnenste buigradius

De resulterende hoek na terugvering:

$$\alpha_{res} = \alpha_i - \alpha_t$$

**Intuition**: grotere rekgrens of kleinere E → meer terugvering. Een zachter materiaal (laag $R_e$) of een stijver materiaal (hoog E) veert minder terug. Staal heeft minder springback dan aluminium bij gelijke rekgrens, want E van staal is ~3× groter.

### Compensatiemethoden

1. **Overbuigen**: je buigt méér dan de gewenste hoek, zodat na terugvering de juiste hoek overblijft. Bv. je wil 90° → je buigt naar 85°.
2. **Bottoming**: je duwt het werkstuk met hoge druk volledig in de matrijs. Hierdoor treedt extra plastische vervorming op in de buigzone → minder elastische energie overblijft → minder terugvering.

---

## Plooikracht

### Formule

De maximale buigkracht wordt benaderd door:

$$F_b = C_b \cdot \frac{b \cdot s^2 \cdot R_m}{w}$$

waarbij:
- $b$ = breedte van het werkstuk (in richting van de buigas)
- $s$ = plaatdikte
- $R_m$ = treksterkte van het materiaal (niet rekgrens!)
- $w$ = breedte van de buigopening (afstand tussen de twee steunpunten van de matrijs)
- $C_b$ = processpecifieke factor

### Waarden van C_b

| Type buigen | C_b |
|---|---|
| Luchtbuigen | 0.30 – 0.34 |
| V-buigen | 0.75 |
| Strijkbuigen | 1.2 – 1.33 |
| U-buigen | 0.4 – 0.5 |

> **intuition**: V-buigen vraagt meer kracht dan luchtbuigen omdat het werkstuk volledig in contact komt met de matrijs. Strijkbuigen is het zwaarst omdat het werkstuk wordt aangedrukt langs de gehele matrijswand.

> **belangrijk voor examen**: ken de formule en de waarden van C_b voor elk buigtype.

---

## Minimale buigradius en buigbaarheid

### Waarom bestaat er een minimale buigradius?

Als je te strak buigt, scheurt de buitenzijde van de buiging. De buitenste laag wordt bij een kleine buigradius enorm uitgerekt, en als die rek de breukrek van het materiaal overschrijdt, ontstaat een scheur.

De minimale buigradius R_min waarbij nog geen scheur optreedt hangt af van de vervormbaarheid van het materiaal, uitgedrukt via de **oppervlaktereductie** r:

$$\varepsilon_f = \ln\left(\frac{A_0}{A_f}\right) = \ln\left(\frac{100}{100 - r}\right)$$

De relatie tussen minimale buigradius en plaatdikte t:

$$\frac{R_{\min}}{t} = \frac{50}{r} - 1$$

Voor volledig buigbaar materiaal (r → 50%) gaat R_min → 0: je kan het platgooien zonder te scheuren.

### Factoren die buigbaarheid beïnvloeden

- **Materiaalvervormbaarheid** (hogere r → kleine R_min mogelijk).
- **Niveau van koudverstevigen**: hoe meer koudversteviging, hoe brosser, hoe groter R_min.
- **Randkwaliteit**: ruwe of beschadigde randen zijn spanningsconcentraties en leiden eerder tot scheuren.
- **Anisotropie**: plaat is gewalst, dus de eigenschappen zijn niet gelijk in alle richtingen. Buigen **loodrecht** op de walsrichting is gunstiger dan parallel eraan.

> **praktisch**: onderdelen altijd zo neerleggen dat de buigas loodrecht staat op de walsrichting. Zo benut je de maximale ductiliteit.

---

## Veel voorkomende buigbewerkingen

### Afkantpers (Press brake)

De meest gebruikte machine voor buigen in de werkplaats. Lange bovenste matrijs (*stempel*) en onderste matrijs. Geschikt voor relatief korte stukken en kleine series. De tooling is eenvoudig en snel te wisselen.

### Rolvormen (Roll forming)

Een strip metaal gaat door een reeks rollen die de strip in stappen progressief buigen tot de gewenste dwarsdoorsnede. Geschikt voor **continue productie** van lange profielen: dakgoten, raamprofielen, constructieprofielen...

```
strip --> [rol1] --> [rol2] --> [rol3] --> ... --> eindprofiel
```

Voordeel: hoge productiesnelheid voor grote series.
Nadeel: dure, vaste tooling per profiel.

### Flenzen (Flanging)

Een rand (*flens*) wordt omgebogen langs de rand van een plaat of gat. Doel: stijfheid geven aan de rand van een component zonder materiaal toe te voegen. Toepassingen: autocarrosserie-panelen, behuizingen.

Varianten:
- **Randflens**: ombuigen van de buitenrand van een plaat.
- **Halsflens** (*hole flanging*): een gat in de plaat wordt uitgedrukt tot een kraag — nuttig voor schroefdraad of montage.
- **Dimpling**: kleine verdieping in plaat drukken, bv. voor verzonken boutkoppen.

### Buizen buigen

Buizen buigen is technisch uitdagender dan plaatbuigen omdat de buis kan instorten (ovaliteit of knik aan de binnenzijde). Oplossingen:

- Inwendige **doorn** (*mandrel*) plaatsen om de buis van binnenuit te ondersteunen.
- Buis vullen met zand of granulaat.
- **Axiale drukkracht**: een compressieve kracht langs de buisas zorgt voor gunstige drukvormgeving — drukspanning vertraagt breuk.

---

## Samenvatting en examenoverzicht

| Concept | Kernformule / Regel |
|---|---|
| Volumebehoud | $V = \text{const}$, $\nu = 0.5$ plastisch |
| Ware rek | $\varepsilon = \ln(H/H_0)$ |
| Verstevigingsfunctie | $\sigma = K\varepsilon^n$ |
| Von Mises vloeien | $\sigma_{eff} = Y$ |
| Meeneemvoorwaarde walsen | $d_{max} = \mu^2 R$ |
| Walskracht | $F \approx wL\bar{Y}_f(1 + \mu w / 2h_{av})$ |
| Plooiverlies | $l_b = \alpha(r_i + C_a \cdot s)$ |
| Terugveerhoek | $\alpha_t = 3\frac{R_e}{E}\frac{\alpha_i}{r_i + C_a s}$ |
| Plooikracht | $F_b = C_b \frac{b s^2 R_m}{w}$ |
| Min. buigradius | $R_{min}/t = 50/r - 1$ |

Processen die je moet kennen:
- **Walsen**: werking, soorten, analyse (kracht, koppel, vermogen, meeneemvoorwaarde)
- **Buigen**: types (lucht/matrijs/rol), plooiverlies, terugvering, plooikracht, minimale buigradius

---

## Wat je echt moet kennen

- Het verschil tussen elastische en plastische vervorming (terugveren vs permanent)
- Waarom volume constant blijft bij plastische vervorming (ν = 0.5)
- Het verschil tussen nominale rek en ware rek, en wanneer je welke gebruikt
- De verstevigingsfunctie: σ = Kεⁿ — wat K en n betekenen
- Wat versteviging (work hardening) is en hoe gloeien het ongedaan maakt
- De drie omvormtemperaturenzones (koud/halfwarm/warm) en de gevolgen voor het proces
- Het verschil tussen koudomvormen en warmomvormen (nauwkeurigheid vs lagere krachten)
- Het Tresca-criterium (σ_max − σ_min = Y) en het Von Mises-criterium (effectieve spanning)
- Wanneer je vlakke vervormingstoestand (plane strain) mag toepassen
- Het principe van walsen: twee functies van de rollen (intrekken via wrijving + samendrukken)
- Wat het neutrale punt is bij walsen en wat er aan weerszijden ervan gebeurt
- De meeneemvoorwaarde: d_max = µ²R — wanneer de rol het werkstuk niet meer kan intrekken
- Walskracht berekenen: formule met gemiddelde vloeispanning en contactlengte L = √(Rd)
- De drie types buigen: luchtbuigen, matrijsbuigen (bottoming), rolbuigen
- Het plooiverlies berekenen: l_b = α(r_i + C_a·s) en de correctiefactor k
- Waarom de neutrale as niet in het midden zit bij een kleine buigradius (k < 1)
- Terugvering (springback): formule, en waarom aluminium meer terugveert dan staal
- De twee compensatiemethoden voor springback: overbuigen en bottoming
- De plooikracht: F_b = C_b·b·s²·R_m/w en de waarden van C_b per type buigen
- Minimale buigradius: R_min/t = 50/r − 1 en welke factoren buigbaarheid beïnvloeden
- Waarom je buist loodrecht op de walsrichting (maximale ductiliteit benutten)
