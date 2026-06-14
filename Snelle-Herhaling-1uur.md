# Snelle Herhaling — Productietechnieken en Systemen (±30 min)

> Doel: kernconcepten + kernformules van alle 9 onderdelen in 1 keer doornemen voor lange-termijngeheugen.
> Voor details: zie de individuele .md-bestanden per onderwerp.

---

## 0. Het grote plaatje — 6 hoofdgroepen

| Groep | Principe | Voorbeeld |
|---|---|---|
| Oervormen | Vorm uit vormloos materiaal | Gieten |
| Omvormen | Plastisch vervormen, geen materiaalverlies | Smeden, walsen, buigen |
| Scheiden/Afnemen | Materiaal weg | Verspanen, lasers, ponsen |
| Verbinden | Delen samenvoegen | Lassen |
| Opbrengen lagen | Materiaal toevoegen op oppervlak | Coaten |
| Eigenschappen veranderen | Structuur aanpassen | Harden, gloeien |

---

## 1. Verspaning (draaien/frezen/boren)

**Gereedschapshoeken:**
$$\alpha + \beta + \gamma = 90°$$
(α = vrijloophoek, β = wighoek, γ = spaanhoek)
- **γ positief** → zachte/taaie materialen, kleine krachten, **zwakke** beitel
- **γ negatief** → harde/brosse materialen, **sterke** beitel
- Vuistregel: harder materiaal → groter β, kleiner γ

**Spaanvorming:**

- $T_2$ (spaandikte) $> T_1$ (snededikte)
- Afschuifhoek (Merchant):
$$\boxed{\phi = 45° + \frac{\gamma}{2} - \frac{\mu}{2}}$$
groter φ → kleinere krachten
- 3 spaantypes: **continu** (taai), **lamel** (getand), **brokkel** (bros)

**Snededoorsnede:**
$$A = a \times f = b \times h \qquad b = \frac{a}{\sin\kappa} \qquad h = f \cdot \sin\kappa$$

**Slankheid:**
$$\delta_\kappa = \frac{b}{h} \quad (\text{staal: } 3\text{–}15)$$

**3 bewegingen:** hoofdsnijbeweging ($v_c$), voeding ($f$), instelling ($a$)
**3 krachten:** $F_c$ (tangentieel), $F_f$ (voeding), $F_p$ (terugdruk → doorbuiging)
$$P_c = F_c \times v_c$$

**Kienzle (specifieke snijkracht):**
$$\boxed{F_c = k_{c1.1} \times b \times h^{(1-e)}}$$

**Snijmaterialen hiërarchie (goedkoop/taai → duur/hard):**
Koolstofstaal → HSS → HM → gecoat HM → Cermets → Keramiek → CBN → Diamant
- HSS: beter tegen stoten → onderbroken snede (boren/frezen)
- ISO-code HM: **XX-Y##** (type–materiaal–getal). Klein getal = bros/hard (finish); groot getal = taai (schrobben)
- **Diamant niet op staal** (C lost op in Fe) → wel Al, Cu, composieten, keramiek

**Slijtage:** $VB$ (vrijloopvlak/flankslijtage), $KT$ (kolkslijtage/krater)
**BUE (opbouwsnijkant)** bij lage $v_c$ → vermijden via grotere γ, coating, **hogere $v_c$**

**Taylor (standtijd):**
$$\boxed{v_c \times T^n = C_T}$$

- $n$: HSS ≈ 0.1–0.2, HM ≈ 0.2–0.4, Keramiek ≈ 0.4–0.6
- Kleine $n$ → snelheid verhogen doet standtijd drastisch dalen

**Snijvloeistoffen:** koelen + smeren + spaanafvoer. **Onderbroken snede** → opgelet thermoshock (continu koelen of helemaal niet)

**Frezen:** Meeloop (climb) = voorkeur op CNC (goed oppervlak, drukt werkstuk vast) vs Tegenloop (conventional, oudere machines)

**Boren:** punthoek 118° = staal (algemeen). Dwarssnijkant → grote $F_f$; **aanpunten** verlaagt $F_f$ en verhoogt standtijd. Spaanhoek wordt sterk **negatief** richting de ziel.

**Economische standtijd:**
$$T_e = \left(\frac{1}{m}-1\right)\frac{K_G}{K_U} \qquad\qquad T_p = \left(\frac{1}{m}-1\right) T_{CT}$$
→ $T_e$ (min. kost/stuk) **>** $T_p$ (max. productiviteit), altijd

**Kostprijs per stuk:**
$$\boxed{K_V = t_h \cdot K_U + \frac{t_h}{T} \cdot K_G + t_a \cdot K_U}$$

**Ruwheid:**
$$R_t = \frac{f^2}{8 \cdot r_\varepsilon}$$
→ bepaalt vaak de praktische voedingslimiet

**Doorbuiging:**
$$y_w = (s_m + s_w) \cdot F_p$$
klauwplaat geeft 16× meer doorbuiging dan tussen 2 punten

---

## 2. Omvormen (massief + plaat/buigen)

**Plastisch vervormen:** volume blijft constant
$$\varepsilon_1 + \varepsilon_2 + \varepsilon_3 = 0 \;\Rightarrow\; \boxed{\nu = 0.5}$$

**Ware rek** (gebruikt bij grote vervormingen):
$$\varepsilon = \ln\left(\frac{H}{H_0}\right)$$

**Verstevigingsfunctie:**
$$\sigma = K \varepsilon^n$$
→ na koudversteviging: **gloeien** herstelt ductiliteit

**Temperatuurzones:** koud (versteviging, nauwkeurig) / halfwarm / warm (rekristallisatie, geen versteviging, lagere krachten, minder nauwkeurig)

**Vloeicriteria:**

- Tresca:
$$\sigma_{\max} - \sigma_{\min} = Y$$
- Von Mises:
$$\sqrt{\frac{1}{2}\left[(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2\right]} = Y$$
(fysisch correcter, gebruikt in simulaties)

**Walsen:** rollen trekken in (via wrijving) én drukken samen

- Meeneemvoorwaarde:
$$\boxed{d_{\max} = \mu^2 R}$$
(te grote reductie → rol kan niet intrekken)
- Neutraal punt: snelheden rol/werkstuk gelijk
- Walskracht:
$$F \approx wL\,\bar{Y}_f\left(1 + \frac{\mu w}{2h_{av}}\right) \qquad L = \sqrt{R \cdot d}$$

**Buigen:** binnenkant = druk, buitenkant = trek, neutrale laag tussenin
- **Luchtbuigen**: flexibel, meer springback
- **Matrijsbuigen/bottoming**: nauwkeurig, minder springback
- **Rolbuigen**: grote stralen (cilinders)

**Plooiverlies (blanklengte):**
$$\boxed{l_b = \alpha \left(r_i + C_a \cdot s\right)} \qquad C_a = \frac{k}{2}$$

- $k = 0.66$ als $r_i/s < 2$ (uitrekken), anders $k = 1$

**Springback:**
$$\boxed{\alpha_t = 3\,\frac{R_e}{E}\cdot\frac{\alpha_i}{r_i + C_a \cdot s}}$$

- Staal veert minder terug dan aluminium (hogere $E$)
- Compensatie: **overbuigen** of **bottoming**

**Plooikracht:**
$$F_b = C_b \cdot b \cdot s^2 \cdot \frac{R_m}{w}$$

- $C_b$: luchtbuigen 0.30–0.34, V-buigen 0.75, strijkbuigen 1.2–1.33, U-buigen 0.4–0.5

**Min. buigradius:**
$$\frac{R_{\min}}{t} = \frac{50}{r} - 1$$
→ buigas **loodrecht** op walsrichting voor max. ductiliteit

---

## 3. Lassen

**Definitie:** verbinden via druk en/of warmte; **HAZ** = warmte-beïnvloede zone (niet gesmolten)
**Brazeren** ≠ lassen: alleen toevoegmateriaal smelt, basismateriaal niet

**Smeltlassen vs Druklassen** (geen smeltbad bij druklassen)

| Proces | Bron/elektrode | Gas | Kenmerk |
|---|---|---|---|
| **BMBE** | CC-bron, afsmeltende beklede elektrode | bekleding (rutiel/basisch/cellulose) | basisch = laag H₂ → minder koudscheuren |
| **MIG/MAG** | CV-bron (zelfregeling booglengte), draad = + pool | MIG=inert(Ar)→Al/RVS; MAG=actief(CO₂)→staal | druppelovergang: short-circuit/globular/spray/pulse |
| **TIG** | niet-afsmeltende W-elektrode (− pool!) | steeds inert (Ar/He) | hoogste kwaliteit, dunne platen |
| **OP-lassen** | draad onder poederdek (flux) | geen beschermgas nodig | hoge depositie, geautomatiseerd |

**Puntlassen:**
$$Q = I^2 \cdot R \cdot t \qquad\qquad d_{\text{lens}} = 4\sqrt{t}$$

**Lasposities:** PA (vlak, gunstig — zwaartekracht helpt) ... PE (overhead, ongunstig)

**Imperfecties (ISO 5817, niveaus B/C/D):**
- **Scherp** (scheuren, lack of fusion) = gevaarlijk → spanningsconcentratie, vaak NIET toegelaten
- **Rond** (poriën) = minder gevaarlijk, beperkt toegelaten
- **Undercut** = scherpe groef naast las → gevaarlijk bij vermoeiing

**HAZ-zones:** CGHAZ (grove korrels, **slechtste taaiheid**) > FGHAZ (fijn, goed) > ICHAZ > SCHAZ

**Materiaalkeuze bij ontwerp:**
- S235–S460: geen reductiefactor nodig (sterkte niet door lassen beïnvloed)
- S690+ en aluminium: sterkteverlies in HAZ → reductiefactoren toepassen

**Koolstofequivalent (koudscheuren):**
$$\boxed{CE_{IIW} = C + \frac{Mn}{6} + \frac{Cr+Mo+V}{5} + \frac{Ni+Cu}{15}}$$
→ $CE_{IIW} > 0.4$ = risico → voorverwarmen, basische elektroden

**Warmscheuren:** door S/P-segregatie, **in lasmetaal** (niet HAZ), tijdens stollen
**Lamellaire scheuren (Z-kwaliteit):** MnS-insluitsels bezwijken bij spanning loodrecht op plaat → "getrapt" scheurpatroon

**Lasnaadvormen:** I (dun) → V → U → X/K (dik, tweezijdig). Openingshoek: staal 60°, RVS 70°, Al/Ni 80–90°

---

## 4. Oervormen (Gieten)

**Net shape vs near net shape**

**Gietsysteem:** gietkom → gietloop (sprue, **taps toelopend**) → aansnijding (runner) → vormholte → opkomer (riser) + kern
- Gietvorm **iets te groot** (krimpcompensatie)

**Smeltwarmte:**
$$H_p = \rho V \left[C_s(T_m-T_0) + H_f + C_l(T_p-T_m)\right]$$

**Vloei:**

- Bernoulli (snelheid onderaan gietloop):
$$v_2 = \sqrt{2g h_1}$$
- Continuïteit:
$$Q = A_1 v_1 = A_2 v_2$$
→ **tapse gietloop** voorkomt aspiratie (lucht aanzuigen)
- Vultijd:
$$T_{MF} = \frac{V}{Q}$$

**Stolling:**
- Zuiver metaal: plateau (vaste temperatuur)
- Legering: **mushy zone** (liquidus–solidus), dendrieten → segregatie
- 3 zones in gietstuk: chill (fijnkorrelig, rand) → kolomvormig → equiaxiaal (centrum)

**Chvorinov (stollingstijd):**
$$\boxed{T_{TS} = C_m \left(\frac{V}{A}\right)^n} \qquad n \approx 2$$
→ grotere $V/A$ = langzamer stollen

**Krimp (3 fasen):** vloeistofcontractie → stollingskrimp → thermische contractie

**Opkomer moet later stollen:**
$$\left(\frac{V}{A}\right)_{\text{opkomer}} > \left(\frac{V}{A}\right)_{\text{gietstuk}}$$

**Turbinebladen — evolutie (minder korrelgrenzen = betere creepweerstand):**
CC (willekeurige korrels) → **DS** (kolomvormig, langs centrifugaalrichting, koelplaat) → **SX** (single crystal, via grain selector spiraal of seed-techniek)

---

## 5. Scheiden (ponsen/stansen/buigen plaat)

**Ponsen** (gat = product) vs **Stansen** (uitgestanst stuk = product)

**4 fasen snijproces:** elastisch → plastisch → breukinitiatie → breukvoortplanting
**Gesneden rand (4 zones):** rollover → burnish (glad) → breukzone (ruw) → braam (burr)

**Snijspleet:**
$$u = a \cdot t \qquad (a \approx 0.045\text{–}0.075 \text{ afh. materiaal/hardheid})$$
- Te klein → dubbele polijstzone, hoge kracht
- Te groot → grote braam

**Maten:**

- Stansen: matrijs = $D_b$ (blank), pons = $D_b - 2u$
- Ponsen: pons = $D_h$ (gat), matrijs = $D_h + 2u$
→ **pons bepaalt het gat, matrijs bepaalt de blank**

**Ponskracht:**
$$\boxed{F_t = \tau \times L \times t} \qquad \tau \approx 0.75 \cdot UTS$$

**Centroid** (zwaartepunt snijlijn) = aangrijpingspunt resulterende kracht:
$$x_0 = \frac{\sum L_i x_i}{\sum L_i} \qquad y_0 = \frac{\sum L_i y_i}{\sum L_i}$$

**Afschuifhoek op gereedschap** → verlaagt piekkracht:
$$F_s = K \cdot F_t \qquad K = \frac{t \cdot p}{s} < 1$$

**Gereedschappen:**
- **Compleetstempel**: meerdere bewerkingen op 1 positie, 1 slag — goede toleranties, beperkt complex
- **Volgstempel**: meerdere stations, strip beweegt door — hoge snelheid, duurder

**Fijnstansen:** klemring + tegendrukplaat → hoge **hydrostatische druk** → scheuren onderdrukt → volledig glad (burnish) oppervlak, kleine snijspleet (~1% t)

**Overige processen:**
- **Incrementeel omvormen**: kleine tool, CNC-pad, geen matrijs, traag, voor prototypes
- **Vloeidraaien (spinning)**: roterende doorn + rol, conventioneel (dikte ~constant) vs schuif (dikte neemt af)
- **Hydroformen**: vloeistofdruk i.p.v. starre matrijs, complexe vormen, traag

---

## 6. Slijpen

**Geometrisch ongedefinieerde snijkanten** (vs vast aantal tanden bij frezen)

- Spaanhoek korrels **sterk negatief**, $v_s = 20$–$100$ m/s (veel hoger dan frezen)

**3 snijmechanismen:** **Cutting** (gewenst, spaanvorming), **Plowing** (plastisch verdringen, geen spaan), **Rubbing** (alleen wrijving/warmte)

- Hogere $Q'_w$ → meer cutting, minder rubbing/plowing

**Specifiek spaandebiet:**
$$Q'_w \;\left[\frac{\text{mm}^3/\text{s}}{\text{mm schijfbreedte}}\right]$$

**Equivalente spaandikte:**
$$h_{eq} = \frac{Q'_w}{v_s}$$

**Slijpverhouding** (hoge $G$ = efficiënte schijf):
$$G = \frac{V_w}{V_s}$$

**Waarom slijpen (i.p.v. draaien/frezen)?** nauwkeurigheid (µm), oppervlaktekwaliteit, **harde** werkstukken, dunne af te nemen laag. Maar: hoge specifieke krachten (×10) → duur, laag debiet.

**Slijpschijf (volumefracties):**
$$V_k + V_b + V_p = 1$$
(korrels + bindmiddel + poriën)
- **Keuzeregel (examen!):** zacht werkstuk → **harde** schijf; hard werkstuk → **zachte** schijf (laat stomme korrels sneller los)
- **Friability** = korrel breekt bij overbelasting → zelfscherpend (gunstig)
- Open structuur (veel $V_p$) = ruimte voor spaanders; dicht = beter oppervlak

**Warmte (groot probleem):** negatieve spaanhoek + hoge snelheid + rubbing/plowing → 600–1000°C
→ temperen, verbranden, micro-scheuren, restspanningen (trek!)

**Onderhoud:** **Dressing** = profileren (truing, geometrie) + africhten (sharpening, scherpe korrels vrijmaken). **Balanceren** noodzakelijk (trillingen bij hoog toerental).

**Centerloos slijpen:** regelschijf bepaalt $v_w$ (langzamer, hoger wrijvingscoëff.)
- Doorvoerslijpen (schuine regelschijf, axiale voeding, lange stukken)
- Insteekslijpen (radiale beweging, korte stukken)

**Nabewerkingen (steeds fijner):** Honen (boringen, kruisgestreept patroon, 30–280µm) → Superfijnen (uitwendige cilinders) → Lappen (extreme kwaliteit, 5–60µm, geen materiaalafname-doel)

---

## 7. Laserbewerking

**LASER:** gestimuleerde emissie → monochromatisch, coherent, directioneel licht
**3 onderdelen laserbron:** medium + pompbron + resonatorcaviteit

| Type | Golflengte | Eigenschap |
|---|---|---|
| CO₂ | 10.64 µm | oudste, slecht geabsorbeerd door metalen, slechte BPP |
| Fiber | 1.07 µm | hoge bundelkwaliteit (lage BPP), efficiënt, dominant vandaag |
| DDL | 0.4–1.5 µm | nieuwste, zeer efficiënt, R&D |

**Absorptie (metalen, T=0):**
$$R + T + A = 1 \;\Rightarrow\; A = 1-R$$
Kortere golflengte → beter geabsorbeerd door metaal (Cu/Al sterk reflectief → moeilijk)

**Bundelkwaliteit:**
$$\text{BPP} = w_0 \times \theta \qquad\qquad M^2 = \frac{\text{BPP}}{\text{BPP}_{Gauss}}$$

- lager $\text{BPP}$ = beter (scherper focus)
- $M^2=1$ ideaal; fiber ≈ 4–10, CO₂ > 70

**Lasersnijden — snijgas:**
- **Smeltsnijden** (N₂/Ar, inert): geen oxidatie → **Al, RVS**
- **Brandsnijden** (O₂, exotherm): meer vermogen → dikker **koolstofstaal**

**Problemen:**
- **Dross** (te hoge snelheid): gesmolten materiaal hecht opnieuw onderaan
- **Inbranding** (te lage snelheid): te veel energie → ruwe rand
- **Plasmavorming**: CO₂ + Al/RVS + hoge snelheid → plasmawolk absorbeert bundel → **totaal snedeverlies**

---

## 8. Fysische & chemische bewerkingen (niet-conventioneel)

**Waarom?** Harde/brosse materialen, extreme toleranties, geen mechanische schade gewenst.
Conventioneel = contact + kracht. Niet-conventioneel = energie zonder contact.

**Mechanisch (abrasief):**
- **AFM**: abrasieve pasta door kanalen — interne oppervlakken
- **WJM**: waterstraal (~300MPa, 600-900 m/s) — **geen HAZ**, niet-metalen
- **AWJM**: water + abrasief — metalen + keramiek
- **AJM**: gas + abrasief — glas, deburren
- **USM**: ultrasone trilling + slurry — **brosse** materialen

**EDM (vonkerosie):** vonken tussen elektrode/werkstuk in diëlektricum (~10 000°C). **Enkel geleidende materialen.**
- **Zinkvonken**: elektrode = negatieve vorm → 3D holte (matrijzen)
- **Draadvonken**: dunne draad volgt contour → 2D/2.5D
- Pulsenergie:
$$W_e = \int_0^{t_e} u_e(t) \cdot i_e(t) \, dt$$
grote puls = ruw+snel, kleine puls = fijn+traag
- 6 fasen: bubble growth → ionization → thermal erosion → debris diffusion → accumulation → spurious discharges (doorspoelen cruciaal!)

**ECM (elektrochemisch):** werkstuk = anode (+), gereedschap = kathode (−), elektrolyt
$$Me \rightarrow Me^{z+} + z \cdot e^-$$
- Gereedschap slijt NIET, **zelf-corrigerend** (smalle gap = meer stroom = meer afname)
- **Hoogste afnamesnelheid** van alle niet-conventionele processen, geen HAZ

**CHM:** masker (resist) + zuur/alkalisch bad — alleen ondiepe 2D, kleine series

**USP-laser (ultrakorte pulsen, ps/fs):**
- **ns-puls** → smeltzone, redeposition, microcracks, opgeworpen randen
- **fs-puls** → **sublimatie**, ~geen HAZ, scherpe schone geometrie ← **kernverschil!**
- **Textureren** (µm/nm-schaal, ≠ graveren): lotusbladeffect (hydrofoob), haaienhuideffect (minder wrijving), gekko-effect (kleefkracht)
- **LIPSS**: spontane periodieke nanostructuren, periodiciteit ∝ golflengte, mechanisme niet volledig begrepen. LSFL (<1µm) vs HSFL (≤100nm)

---

## 9. Additive Manufacturing (3D printen)

**Definitie:** materiaal **laag per laag toevoegen** (i.p.v. wegnemen)
**Workflow:** CAD → **STL** (driehoeksnetwerk) → **slicen** (lagen + scanpatroon) → bouwen → post-processing (supports, baseplate, HIP, oppervlak)

**Classificatie naar startfase:**
| Startfase | Processen |
|---|---|
| Liquid | SLA (fotopolymerisatie), FDM (extrusie filament) |
| Powder | SLS (sinteren), SLM (volledig smelten), EBM (e-bundel, vacuüm), Laser Cladding (poeder via nozzle) |

**Voordelen:** designvrijheid (complexiteit = gratis), lichtgewicht (lattice/topologie-optimalisatie), personalisatie, functie-integratie, weinig verspilling
**Nadelen:** traag/duur, ruw oppervlak (nabewerking nodig), supports nodig, niet voor massaproductie

**Polymeren:**
- **SLA**: UV-laser polymeriseert hars — **beste oppervlak/nauwkeurigheid**, supports nodig
- **FDM**: gesmolten filament — goedkoop, traag, matig oppervlak
- **SLS**: laser sintert poeder — **geen supports nodig** (los poeder = support) → part nesting mogelijk

**Metalen:**
- **EBM**: e-bundel, vacuüm, **voor-sinteren = geen supports**, hoge ruwheid, enkel non-ferro (Ti, CoCr)
- **SLM**: laser smelt poeder **volledig**, breed materiaalspectrum, goed oppervlak, thermische spanningen, **supports nodig**
- **Laser Cladding**: geen poederbed (poeder via nozzle), geschikt voor **reparaties**, gradient-materialen (FGM), lage nauwkeurigheid

**SLM smeltbad — 4 voorwaarden:** continu, verbonden met vorige laag, voldoende hoogte, hoek ~90°

**Downfacing surfaces:** smeltbad rust op los poeder (slechte warmtegeleiding) → zinkt dieper → dross
→ oplossing: **supportstructuren** OF aangepaste parameters (lager vermogen, hogere snelheid voor eerste lagen)

**Poeder voor SLM:** sferisch, juiste grootteverdeling, grootte afgestemd op laagdikte

**Lattice structures:** periodieke poreuze structuren, eigenschappen via eenheidscel-geometrie — biomedisch (botingroei), warmtewisselaars, lichtgewicht aerospace

---

## Snelle cross-checks (vaak verward)

- **Meeloop vs tegenloop** (frezen): meeloop = voorkeur CNC
- **MIG vs MAG**: inert/Ar vs actief/CO₂
- **Smeltsnijden vs brandsnijden** (laser): N₂/Ar geen oxidatie vs O₂ exotherm
- **EDM vs ECM**: EDM = thermisch (gereedschap slijt), ECM = elektrochemisch (gereedschap slijt niet, zelf-corrigerend)
- **ns- vs fs-laser**: HAZ+smelt vs sublimatie zonder HAZ
- **SLS vs SLM**: sinteren (geen supports) vs volledig smelten (supports nodig)
- **Harde vs zachte slijpschijf**: hard→zacht werkstuk omgekeerd! (harde schijf voor zacht werkstuk)
- **Stansen vs ponsen**: product = uitgestanste stuk vs gat
- **DS vs SX turbineblad**: kolomvormige korrels vs geen korrelgrenzen
