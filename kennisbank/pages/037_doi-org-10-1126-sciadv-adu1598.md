# https://doi.org/10.1126/sciadv.adu1598

Bron: https://doi.org/10.1126/sciadv.adu1598
Opgehaald: 2026-06-18

---

STATUS: OPGELOST - oorspronkelijke fetch gaf lege response (paywall/JavaScript-blokkade). Gebruiker heeft de PDF van dit artikel zelf aangeleverd ("sciadv.adu1598.pdf"). Onderstaande tekst is de volledige, automatisch geëxtraheerde artikeltekst uit die PDF (incl. abstract, hoofdtekst en referenties); lay-out-artefacten van de originele kolomopmaak (bv. losse voetnootletters, doorlopende koppen) kunnen voorkomen maar de inhoud is compleet.


M AT E R I A L S S C I E N C E                                                                                                             Copyright © 2025 The
                                                                                                                                           Authors, some rights
A wireless, self-­powered smart insole for gait                                                                                            reserved; exclusive
                                                                                                                                           licensee American
monitoring and recognition via nonlinear synergistic                                                                                       Association for the
                                                                                                                                           Advancement of
pressure sensing                                                                                                                           Science. No claim to
                                                                                                                                           original U.S.
                                                                                                                                           Government Works.
Qi Wang1,2†, Hui Guan1†, Chen Wang1†, Peiming Lei1, Hongwei Sheng1, Huasheng Bi1, Jinkun Hu1,                                              Distributed under a
Chenhui Guo1, Yichuan Mao1, Jiao Yuan1, Mingjiao Shao1, Zhiwen Jin1*, Jinghua Li2*, Wei Lan1*                                              Creative Commons
                                                                                                                                           Attribution
Wearable insole-­based pressure sensor systems have gained attention for continuous gait monitoring, showing                               NonCommercial
potential for preventing, diagnosing, and treating conditions such as lumbar degenerative disease and diabetic                             License 4.0 (CC BY-­NC).
foot ulcers. However, challenges such as nonlinear response, low stability, and energy limitations have hindered
widespread adoption. Here, we report a fully integrated, self-­powered, wireless smart insole designed for plantar
pressure monitoring and real-­time visualization and analysis of gait. The pressure sensor uses a nonlinear syner-
gistic strategy, achieving remarkable linearity (R2 > 0.999 over 0 to 225 kilopascals) and high durability (>180,000
compression cycles). Powered by flexible solar cells, the insole features 22 pressure sensors, enabling spatially
resolved pressure mapping and real-­time visualization on a smartphone interface. Integration of a support vector
machine model further enables accurate recognition of eight motion states, including static (e.g., sitting and
standing) and dynamic (e.g., walking, running, and squatting) activities. The smart insole provides a practical solu-

tion for improving clinical assessments, personalized treatments, and biomechanics research.

INTRODUCTION                                                                           (37, 38). Capacitive sensors face issues such as weak anti-­interference
Gait results from the coordinated interaction of the skeletal, ner-                    ability, complex measurement circuits, and lower sampling rates and
vous, and muscular systems (1). Therefore, continuous monitoring                       accuracy (39, 40). In comparison, resistive sensors are capable of
of plantar pressure and gait during daily activities has substantial                   accommodating both static and dynamic pressure measurements
potential for the prevention, diagnosis, and treatment of various                      (41), have strong anti-­interference capabilities (42), feature simple
diseases (2). These diseases include neurological disorders such as                    measurement circuits (43), and offer high accuracy, making them an
Parkinson’s disease (3) and stroke (4, 5), orthopedic conditions such                  ideal choice for in-­shoe sensing systems. However, resistive sensors
as flatfoot (6, 7) and lumbar disc degeneration (8), and metabolic                     typically exhibit nonlinear responses to pressure (44), which com-
diseases such as diabetic foot (9–11). Specifically, Parkinson’s dis-                  plicates data processing and analysis, and their stability is often
ease leads to muscle movement control disorders, which manifest                        suboptimal. Another major challenge is the power supply for the
as gait freezing and postural instability (12, 13). Stroke results in                  system. Although self-­powered sensors can directly convert pres-
asymmetrical limb movements, with lower plantar pressure and                           sure signals into electrical signals, the acquisition and transmission
prolonged support time on the affected side (14). Flatfoot alters the                  of these signals still require external power sources (45). Therefore,
contact area of the arch with the ground and changes the center of                     developing a self-­powered in-­shoe sensing system that achieves
plantar pressure (15). Diabetic foot ulcers cause peripheral neuropa-                  high precision, linear response, and high stability remains a formi-
thy (16) and loss of protective sensation in the feet, making patients                 dable challenge.
unaware of plantar pressure (17–19). Real-­time monitoring of plan-                        This work reports a fully integrated, self-­powered, wireless smart
tar pressure and timely adjustment of walking habits to reduce the                     insole system for spatially resolved monitoring of plantar pressure
burden on high-­pressure areas aid in the prevention and healing of                    and real-­time gait visualization. Flexible perovskite solar modules
foot ulcers (9, 20, 21).                                                               (FPSMs), integrated from flexible perovskite solar cells (FPSCs),
     In current medical practice, plantar pressure distribution is mea-                convert solar energy into electrical energy, which is stored in lithium
sured using pressure-­sensing platforms (22–24). However, their use                    batteries to power the wearable system, enabling a self-­sufficient
is limited by time and spatial constraints. To address this issue, inte-               energy supply. On the basis of a nonlinear synergistic strategy, the
grating sensors into shoes to create wearable electronic devices has                   sensors convert pressure signals into linear electrical signals [coef-
become a promising strategy (8, 25–27). Recently, in-­shoe sensors                     ficient of determination (R2) > 0.999] across the entire sensing range
based on resistive (28–30), capacitive (27, 31, 32), piezoelectric                     (0 to 225 kPa) and show no notable performance degradation after
(33, 34), or triboelectric mechanisms (35, 36) have been developed.                    180,000 cycles of compression and release, demonstrating high lin-
However, because of their sensing mechanisms, piezoelectric and                        earity and stability. Pressure sensing data are transmitted in real
triboelectric sensors are limited to measuring dynamic pressure signals                time to a smartphone via a Bluetooth Low Energy (BLE) module,
                                                                                       allowing for the visualization of plantar pressure distribution in
  School of Physical Science and Technology, Lanzhou University, Lanzhou, Gansu        multiple modes on the application (APP). Last, by integrating a
730000, China. 2Department of Materials Science and Engineering, The Ohio State        support vector machine (SVM) learning model, the smart sensor
University, Columbus, OH 43210, USA.                                                   insole successfully collects and recognizes various motion states.
*Corresponding author. Email: lanw@​lzu.​edu.​cn (W.L.); li.​11017@​osu.​edu (J.L.);
jinzw@​lzu.​edu.​cn (Z.J.)                                                             The smart insole has the potential to enable early detection of high-­
†These authors contributed equally to this work.                                       pressure areas in patients with diabetes and assess gait metrics for

Wang et al., Sci. Adv. 11, eadu1598 (2025)   16 April 2025                                                                                                 1 of 13

patients with Parkinson’s disease and stroke. The ease of fabrication,     reduces measurement errors, simplifies calibration, and lowers com-
mechanical robustness, and low cost allow for customized, ergo-            putational complexity. However, most existing resistive sensors typi-
nomic designs for patients with flat feet or high arches. In addition,     cally exhibit nonlinear responses. To address this issue, we propose a
the system has the potential to extend to other fields, such as athlete    strategy based on a nonlinear synergy mechanism. By engineering
posture correction. Overall, the integrated smart insole serves as a       the mechanical and electrical properties of the materials, this ap-
viable solution to revolutionizing next-­generation health care prac-      proach exploits the nonlinear characteristics of both properties to
tices and the internet of things. The concept involving the synergy of     cancel each other out, thereby achieving a linear sensing response.
materials, devices, hardware, and software can potentially expand to           The fabrication process of the CNT/ACET/PDMS sensor is illus-
alternative fields, opening exciting opportunities for digital interac-    trated in fig. S1. Sugar cubes serve as water-­soluble sacrificial tem-
tion between humans and the world.                                         plates, immersed in PDMS, and cross-­linked in situ to form a porous
                                                                           PDMS network. The sugar/PDMS composite exhibits excellent mal-
                                                                           leability, allowing for cutting and polishing to customize size and
RESULTS                                                                    shape, accommodating various sensing requirements. Using a solu-
Overview of the self-­powered smart insole                                 tion ultrasonication method, CNT and ACET are attached to the
The dynamic distribution of plantar pressure contains rich physio-         porous PDMS network obtained after dissolving sugar cubes in wa-
logical information from the skeletal, muscular, and nervous sys-          ter. Figure 2A shows photographs of the sensor in both initial and
tems, offering promising applications in the prevention, diagnosis,        compressed states, along with corresponding scanning electron mi-
and treatment of various diseases. However, developing a highly            croscopy (SEM) image of the sensor in the compressed state. From
integrated wearable system for collecting and analyzing plantar            the SEM images of the sensor at different magnifications in the initial
pressure data remains a major challenge. First, the sensors need to        and compressed states (fig. S2, A and B), a porous structure is ob-
provide both high linearity and long-­term stability while also being      served. In the initial state, the pore size ranges from 100 to 400 μm,

compatible with high-­density integration to achieve high precision        with an average size of 219 μm. After compression, the porosity de-
and spatiotemporal resolution in data collection. Second, the energy       creases notably. The porosity and density of the sensors, as deter-
supply module needs to suit wearable scenarios, providing consis-          mined by gravimetric measurement, are 70.42% and 0.33 g cm−3,
tent and reliable power.                                                   respectively (46). The contact angle of 115.8° for the sensor indicates
    To address these challenges, we developed a fully self-­powered        hydrophobic properties, which enhance its stability and reliability in
smart insole system for spatially resolved monitoring of plantar           humid environments (fig. S3).
pressure and real-­time visualization of gait. Figure 1 (A and C) il-          Mechanical properties of the sensors are primarily determined
lustrates the structure and workflow of the system. The insole con-        by the porous PDMS network. The excellent elasticity of the porous
sists of upper and lower polyimide (PI) encapsulation layers, upper        network results in the stress curves during compression and release
and lower electrodes, carbon nanotube/acetylene black/polydimeth-          under 0 to 85% strain nearly overlapping, indicating low mechanical
ylsiloxane (CNT/ACET/PDMS), and a PDMS layer. A total of 22                hysteresis (fig. S4A). The attachment of CNT and ACET does not
CNT/ACET/PDMS sensors are densely integrated into the PDMS                 notably affect the mechanical properties of the PDMS network (fig.
layer, converting pressure signals into electrical signals, which are      S4A). Notably, after 100 compression cycles, the strain-­stress curve
collected by the analog-­to-­digital converter (ADC) on the printed        closely matches the initial state, demonstrating excellent mechanical
circuit board (PCB) and transmitted through a BLE module to a              stability and repeatability (fig. S4B).
mobile device. To enhance the comfort, convenience, and stability              Figure 2B illustrates the sensing mechanism of the CNT/ACET/
of the system, the lithium battery and PCB are integrated into the         PDMS sensor. The porous structure allows reversible changes in
arch area of the insole. Notably, using a nonlinear synergistic strat-     the microstructure of the network during compression and release,
egy, the nonlinear elements of the electrical and mechanical proper-       leading to modifications in the conductive pathways and, conse-
ties of the CNT/ACET/PDMS sensors are effectively canceled out,            quently, changes in conductivity. When the sensor is compressed by
resulting in a linear sensing output (Fig. 1B). The transmitted data       an external force, it undergoes different stages. The inner surfaces of
are processed on a smartphone APP, enabling visualization in mul-          the porous structure in the sensor begin to contact each other under
tiple modes. Last, by integrating an SVM learning model, the system        pressure, forming additional conductive pathways. As pressure in-
successfully collects and classifies plantar pressure data for various     creases, porosity further decreases, accompanied by an increase in
motion states, including sitting, standing, single-­leg standing, squat-   conductive pathways. Eventually, porosity disappears, and the inner
ting, walking, running, and ascending and descending stairs. Figure        surfaces are in full contact. Upon removal of the external force, the
1D shows photographs of the system with FPSM mounted on the                excellent elasticity of the PDMS network supports the recovery of
upper surface of the shoe to maximize sunlight exposure. Because of        the porous network structure and conductive pathways to their
the use of PDMS as the sensor structural material and the in situ          original state (2, 46).
cross-­linking technique that embeds the sensors into the PDMS                 The sensitivity of the pressure sensor is defined as
layer, the insole exhibits high durability and can withstand folding,
twisting, and stretching.                                                                                     I − I0
                                                                                                                I0
                                                                                                        S=                                    (1)
Performance of CNT/ACET/PDMS sensors with                                                                    p − p0
nonlinear synergy                                                                                                            I −I
Pressure sensors need to have high sensitivity, stability, and linearity   where S represents the sensitivity of the sensor, I 0 represents rela-
simultaneously to achieve accurate, reliable long-­term pressure sig-      tive current change, p represents pressure, and p0 represents ini-
nal acquisition. Designing sensors with linear responses effectively       tial pressure.

Wang et al., Sci. Adv. 11, eadu1598 (2025)   16 April 2025                                                                                 2 of 13

Fig. 1. Overview of the self-­powered smart insole. (A) Typical scene of using the smart insole system and the exploded overall structure comprising CNT/ACET/PDMS
sensors and PSCs. (B) Schematic illustration of a nonlinear synergistic strategy to achieve high linearity in pressure sensing. The nonlinear components in the mechanical
response and electrical response of the CNT/ACET/PDMS sensor cancel each other out, resulting in a linear sensing response. (C) The workflow of the smart insole system
includes energy harvesting based on PSCs, pressure data collection based on nonlinear synergy, visualization of plantar pressure distribution on a mobile terminal, and data
classification using the SVM learning model. (D) Photographs of the smart insole system and the core sensing layer in the initial, folding, twisting, and stretching states.

    To investigate the optimal preparation parameters, sensors with                    the sensitivity of CNT-­based sensors decreases with increasing con-
varying concentrations of CNTs, ACET, and their mixtures are fabri-                    centration in the linear region, whereas ACET-­based sensors initially
cated (fig. S5). As the concentration of the conductive materials in-                  show an increase in sensitivity, followed by saturation. This behavior is
creases, the sensors exhibit a transition from insulating to nonlinear                 attributed to the strong conductivity of high-­concentration CNTs,
and then to linear responses (fig. S6). Near the percolation threshold,                which form a dense two-­dimensional network and reduce the propor-
the sensors require a certain amount of pressure to activate the con-                  tion of additional conductive pathways generated during compression.
ductive network, resulting in a nonlinear response. At this stage, the                 In contrast, the porous structure of ACET facilitates additional chang-
initial conductivity is relatively low, leading to higher sensitivity. At              es in conductive pathways during compression, thereby maintaining
higher concentrations, the sensors, whether containing CNTs, ACET,                     higher sensitivity.
or their mixtures, consistently exhibit a linear response, demonstrating                   When CNTs and ACET are mixed at a concentration of 5 mg/ml
the general applicability of this strategy. For single-­material sensors,              each, a synergistic effect is observed. The two-­dimensional conductive

Wang et al., Sci. Adv. 11, eadu1598 (2025)   16 April 2025                                                                                                          3 of 13

Fig. 2. Performance of CNT/ACET/PDMS sensors with nonlinear synergy. (A) Photographs of the CNT/ACET/PDMS sensor in the initial state, compressed state, and an
SEM image of the sensor in the compressed state. (B) Schematic of the sensing mechanism. External pressure induces alterations of the microstructure and distribution of
conductive pathways within the sensor, converting changes in mechanical pressure into quantifiable electrical signals. (C) Three-­dimensional plot illustrating the relation-
ship among pressure, strain, and normalized current variations of the sensor during compression. (D) Experimental data and fitting results for the electrical, mechanical, and
sensing planes of the CNT/ACET/PDMS sensor. The linear response is achieved through the cancellation of nonlinear components in the mechanical and electrical proper-
ties of the sensor. (E) The normalized current variation of the CNT/ACET/PDMS sensor under different pressures (1.32 to 23.45 kPa). (F) The normalized current variations of
the CNT/ACET/PDMS sensor at different pressing frequencies (0.1 to 2.0 Hz). (G) Stability of the CNT/ACET/PDMS sensor under cyclic pressure with an amplitude of 3.5 kPa
and a frequency of 2.0 Hz over 180,000 cycles. (H) Comparison of the performance between CNT/ACET/PDMS sensors and other linear pressure sensors.

network formed by CNTs bridges ACET, enabling the formation of                          respectively. At lower CNT concentrations, a uniform and stable two-­
stable conductive pathways under conditions of low initial conductiv-                   dimensional conductive network cannot be formed, and the addition-
ity. This results in high sensitivity (0.36 kPa−1) and excellent linearity              al conductive pathways generated during compression are insufficient,
(0.999). When the concentration of ACET deviates notably from the                       leading to reduced sensitivity. At higher concentrations, however, the
optimal level—either lower or higher—the sensors exhibit high sensi-                    excessive initial conductivity results in a decline in sensitivity. There-
tivity in the nonlinear region or low sensitivity in the linear region,                 fore, CNTs and ACET at 5 mg/ml each are used in subsequent studies.

Wang et al., Sci. Adv. 11, eadu1598 (2025)   16 April 2025                                                                                                            4 of 13

   To investigate the nonlinear synergy strategy, simultaneous mea-             Evaluating the dynamic response capability of the sensor in-
surements of strain, pressure, and relative current change form a           volves conducting cyclic compression tests at different frequencies.
curve in a three-­dimensional parameter space (Fig. 2C). The pres-          The CNT/ACET/PDMS sensor demonstrates a consistent current
sure range of 0 to 225 kPa encompasses most plantar pressure values         response across a frequency range of 0.1 to 2.0 Hz. In contrast, the
experienced during daily activities.                                        current response of the ACET/PDMS sensor notably decreases as
   As pressure gradually increases, the porosity of the porous struc-       the frequency increases (fig. S9). This difference is likely due to the
ture decreases, leading to an increase in Young’s modulus. Conse-           superior adhesion capability and mechanical response provided
quently, larger forces are required to achieve the same strain change,      by the synergistic conductive network formed by one-­dimensional
resulting in an exponential relationship between pressure and strain        CNT and zero-­dimensional ACET. The CNT/ACET network is ca-
                                                                            pable of accurately tracking the movements and deformations of the
                                   p = 0.110e0.07ϵ                   (2)    PDMS framework, resulting in real-­time sensing outputs that are
                                                              2             not influenced by frequency. In contrast, the zero-­dimensional
where p represents pressure, ϵ represents strain, and R = 0.999.
   Simultaneously, the reduction in porosity causes the internal            ACET demonstrates a delay in responding to mechanical changes
walls of the sensor to become more likely to contact each other un-         and current response, particularly in high-­       frequency scenarios.
der the same strain change. This facilitates the formation of addi-         Evaluating the long-­term stability of the CNT/ACET/PDMS sen-
tional conductive pathways, resulting in a faster increase in current       sor involves conducting cyclic compression tests at a frequency of
and leading to an exponential relationship between relative current         2.0 Hz. After 180,000 cycles, the sensor exhibits no notable performance
change and strain                                                           degradation (Fig. 2G), indicating its ability to withstand long-­term,
                                                                            high-­frequency cyclic compression while consistently delivering
                              I − I0                                        stable and precise measurement data. To better contextualize the
                                     = 0.287e0.07ϵ                   (3)
                                I0                                          performance of the CNT/ACET/PDMS sensors, we have included

where I 0 represents relative current change, ϵ represents strain,
       I −I                                                                 table S1 to compare metrics of linearity, stability, and sensitivity
                                                                            among various sensor designs from previous studies (25, 47–54).
and R = 0.999.
                                                                            Figure 2H compares the performance of CNT/ACET/PDMS sen-
   The nonlinear exponential terms e0.07ϵ in both equations are
                                                                            sors with several representative linear pressure sensors in terms of
identical. When Eqs. 2 and 3 are combined, the exponential compo-
                                                                            linearity and stability. It can be observed that, compared to the pub-
nents cancel each other out, resulting in a linear relationship be-
                                                                            lished sensors, the CNT/ACET/PDMS sensors achieve a superior
tween pressure and relative current change
                                                                            combination of stability and linearity, demonstrating enhanced
                             I − I0                                         overall performance.
                               I0         0.110                      (4)
                                      =         = 0.383
                               p          0.287                             Design and characterization of the FPSCs
                                                                            To power the entire system effectively and sustainably, an FPSC is
                                                                            designed with high power density, high power conversion efficiency
                                   I − I0                                   (PCE), and sufficient flexibility to withstand the mechanical stresses
                                          = 0.383p                   (5)    encountered in wearable use scenarios (Fig. 3A). Figure 3B shows
                                     I0
        I −I                                                                the cross-­sectional SEM image of the FPSC, including the electron
where I 0 represents relative current change, p represents pres-            transport layer [tin oxide (SnO2)], the photoactive layer (perovskite),
sure, and R2 = 0.999. This is highly consistent with the fitted result      the hole transport layer [2,2′,7,7′-­tetrakis(N,N-­di-­p-­methoxyphenyl
obtained                                                                    amine)-­9,9′-­ spirobifluorene (Spiro-­ OMeTAD)], and the top and
                                   I − I0                                   bottom electrode layers [silver/molybdenum trioxide (Ag/MoO3)
                                          = 0.370p                   (6)    and polyethylene naphthalate/indium tin oxide (PEN/ITO)]. The
                                     I0                                     image reveals smooth, well-­defined interfaces between these layers,
where the 4% deviation is attributed to linear fitting approximation.       indicating high interface quality with reduced defects and impuri-
    Compared to other linear sensing strategies, this method offers a       ties, which contributes to improved device performance. The PEN
simple fabrication process without requiring micro-­nano process-           layer exhibits high mechanical robustness, temperature resistance,
ing or photolithography. It eliminates complex steps such as fine           and transparency, serving as the substrate and support layer for the
patterning and multilayer designs, reducing costs and equipment             FPSC. The perovskite layer, with a thickness of about 650 nm, acts as
demands. Meanwhile, it maintains excellent linear performance,              the photoactive component, absorbing light and generating electron-­
stability, and scalability, making it suitable for practical applications   hole pairs. It is prepared using a two-­step spin-­coating method that
and large-­scale production.                                                lowers the crystallization temperature to 140°C, ensuring compati-
    The sensor exhibits nearly overlapping strain-­current variation        bility with flexible substrates. SnO2 and Spiro-­OMeTAD serve as the
curves under cyclic compression from 0 to 85% strain, demonstrat-           electron and hole transport layers, respectively, enhancing the sepa-
ing minimal mechanical hysteresis (fig. S7). The sensor demon-              ration efficiency of electrons and holes and preventing recombina-
strates a linear current-­voltage response across a strain range of 0 to    tion. MoO3 acts as a hole injection layer, improving the efficiency of
80% (fig. S8). The current response remains highly stable over 10           hole injection and reducing interface resistance. Detailed fabrication
consecutive cycles of compression and release (1.32 to 23.45 kPa),          steps are provided in Materials and Methods and fig. S10.
consistently returning to its initial value after release. This stability       The surface morphology of the perovskite layer exhibits uni-
and repeatability highlight the excellent consistency and robustness        formly sized micrometer-­level grains, with good contact between
of the sensor (Fig. 2E).                                                    grains and no apparent defects (fig. S11). X-­ray diffraction (XRD)

Wang et al., Sci. Adv. 11, eadu1598 (2025)    16 April 2025                                                                                  5 of 13

Fig. 3. Design and characterization of the FPSCs. (A) Exploded view of the FPSC, including layers of Ag/MoO3, Spiro-­OMeTAD, perovskite, SnO2, ITO, and PEN. (B) Cross-­
sectional SEM image of the FPSC. (C) Photographs of the FPSC in initial (left) and bent (right) states. (D) Ultraviolet-­visible (UV-­Vis) absorption and photoluminescence (PL)
spectra of the FPSC. a.u., arbitrary units. (E) Current density–voltage (J-­V) curves of the FPSC. FF, fill factor. (F) External quantum efficiency (EQE) spectrum and integrated
J of the FPSC. (G) Normalized PCE of FPSCs at different curvature radii. (H) Normalized PCE of the FPSC at different bending numbers. (I) J-­V curves comparing FPSC and
FPSM. (J) J-­V curves of the FPSM under light intensities ranging from 10,000 to 90,000 lux. (K) Output power of the FPSM over time under a light intensity of 10,000 lux.

analysis confirms the crystallinity of the perovskite layer, revealing                    integrated current density of 21.59 mA/cm2 matching the JSC mea-
strong diffraction peaks at 14.36° and 28.5°, corresponding to the                        sured from the J-­V curve.
(110) and (220) crystal planes, respectively. These results indicate                          To meet the demands of wearable applications and ensure con-
the successful preparation of the perovskite layer and its good crys-                     tinuous, stable energy collection, the energy supply device must ex-
tallinity (fig. S12A). Figure 3D presents the ultraviolet-­visible (UV-­                  hibit both environmental and mechanical stability. To assess the
Vis) absorption and steady-­state photoluminescence (PL) spectra of                       flexibility and durability of the FPSCs, a series of bending tests are
the perovskite film. The PL peak occurs at 804 nm, corresponding to                       conducted to evaluate their ability to withstand strains typical of
a bandgap of 1.54 eV, which aligns with the bandgap determined                            wearable environments. Figure 3C shows photographs of the FPSCs
from the Tauc plot (fig. S12B). Figure 3E shows the current density–                      in both initial and bent states. Despite a reduction in the curvature
voltage (J-­V) curve of the FPSCs under air mass 1.5 global illumina-                     radius from 12 to 2.75 mm, the normalized PCE of the FPSCs re-
tion (100 mW/cm2), exhibiting an open-­circuit voltage (VOC) of                           mained at 93.9% (Fig. 3G). Furthermore, after 800 cycles of bend-
1.119 V and a short-­circuit current density (JSC) of 22.01 mA/cm2.                       ing, the FPSCs still retained 96.7% of their initial efficiency (Fig.
The FPSCs demonstrate highly uniform efficiency, with an average                          3H). Environmental stability has consistently been a challenge for the
PCE of 16.2% (n = 20) and a maximum PCE of 16.95% (fig. S13).                             FPSCs. Stored in air [relative humidity (RH) = 10 to 20%], the FPSCs
Figure 3F illustrates the external quantum efficiency (EQE) spec-                         retained 50% of their initial PCE after approximately 800 hours
trum and the integrated current density of the FPSCs, with the                            (fig. S14). In a storage environment isolated from water and oxygen

Wang et al., Sci. Adv. 11, eadu1598 (2025)   16 April 2025                                                                                                              6 of 13

(N2 environment), they maintain more than 90% of their initial PCE         layer secures the electrode to the insole surface, while the PET layer,
even after 1000 hours. This indicates that water and oxygen can cause      with a cross section of 10 mm by 10 mm, is slightly larger than the
phase changes in the perovskite, leading to a decline in performance.      sensing layer, ensuring an initial consistent spacing between the up-
Therefore, in practical use, an encapsulation layer is needed to pre-      per and lower electrodes before compression. The Cu sheet is com-
vent the solar cells from encountering water and air.                      pressed into the CNT/ACET/PDMS sensing layer to enhance the
    To power the system, FPSMs are fabricated using patterned ITO          stability of contact resistance and to fix the position of the electrode,
films and top electrode masks, with an effective area of 12 cm2, a         preventing relative displacement between the electrode and the
VOC of 2.16 V, a JSC of 9.68 mA/cm2, and a PCE of 14.56% (Fig. 3I).        sensing layer.
As the illumination intensity increases from 10,000 to 90,000 lux,             The FPSMs increase the voltage to 4.2 V through a power man-
the output power increases from 10.06 to 102.4 mW, as shown in             agement chip optimized for peak efficiency, providing power to the
Fig. 3J and fig. S15. Under continuous illumination of 10,000 lux,         lithium battery. The lithium battery then steps down the voltage to
the device consistently outputs approximately 10 mW of energy. In          3.3 V via a buck converter, serving as the common positive pole for
the final design, two FPSMs are connected in parallel to serve as the      the system. To reduce power consumption, a series of optimizations
energy harvesting module. It must be acknowledged that the PCE of          have been applied to the operating mode (fig. S21). The system con-
the solar cells in this work still falls short compared to the highest-­   sumes 40.7 mW when sampling 22 sensors at a frequency of 32 Hz.
performing solar cells recently reported (table S2) (55–63). Howev-        By integrating controllable switches into the sensor collection cir-
er, the primary focus of this study lies in proposing an integrated        cuit, which powers the sensors only during ADC collection, the
design strategy—encompassing energy supply, system integration,            power consumption is reduced to 30 mW. In addition, when the BLE
data acquisition, transmission, and visualization—to broaden the           module and MCU are inactive, the system enters sleep mode, fur-
application scenarios of FPSCs.                                            ther reducing power consumption to 10.7 mW. When the sampling
                                                                           rate is reduced to 1 and 1/8 Hz, power consumption is respectively

Design and characterization of smart insole for                            reduced to 4.07 and 3.2 mW. Disconnecting the BLE connection fur-
pressure mapping                                                           ther reduces the power consumption to 0.33 mW, demonstrating the
Integrating the key components forms a fully functional, wireless          potential of the system for low-­power operation.
system for real-­time monitoring of dynamic plantar pressure distri-           In low-­light conditions (below 1000 lux), the energy from the
butions. Figure 4 (A and B) illustrates the system architecture and        FPSCs is insufficient; thus, the lithium battery discharges to com-
photograph of the entire system, respectively. Pink arrows indicate        pensate for the energy gap (fig. S22). When the light intensity reach-
the power supply direction, while blue arrows denote the transmis-         es 5000 lux, the solar cells provide enough energy to fully support
sion direction of sensor data. The insole, integrated with 22 sensors,     the power consumption of the system, and the lithium battery volt-
is connected to the PCB, allowing voltage collection through the           age remains stable. Although the system cannot fully self-­power in
microcontroller unit (MCU) equipped with a 22-­channel ADC                 normal mode under low-­light conditions, the integrated lithium-­
module. The MCU then transmits the sensing data to a mobile ter-           ion battery can rapidly charge under strong light and supplement
minal, such as a smartphone, via a BLE module for further data pro-        energy consumption under indoor lighting. Experimental results
cessing and visualization. Figures S16 and S17 show the schematic          show that after a rapid 6-­min charge under 50,000 lux illumination,
diagram of the PCB used in the smart insole system, along with the         the system can operate continuously for 60 min in an indoor envi-
key models, and parameters of the electronic components.                   ronment with an illumination of approximately 500 lux (fig. S22C).
    Sensors numbered 1 to 22 are sequentially distributed from the             The smartphone APP offers three modes for visualizing sensing
toe area to the heel area, as shown in fig. S18. Because of the complex    data (Fig. 4C). The first mode displays the corresponding positions
pressure patterns typically exhibited in the toe and heel regions, a       of the sensors in the insole, using colors to represent pressure values,
greater number of sensors are placed there, while selectively reduc-       making it suitable for quick identification of sensor locations and
ing the number of sensors in the arch area. This design strategy en-       respective data during debugging and calibration processes. The
sures that essential foot pressure information is effectively captured,    second mode uses biharmonic spline interpolation, a standard
even with a limited number of sensors (8, 27, 34). Only two sensors        method for visualizing pressure distribution (27, 64, 65). This meth-
are retained in the arch area, specifically for the diagnosis of condi-    od is based on Green’s functions and transforms 22 discrete and spa-
tions such as flatfoot, to ensure that critical diagnostic data are not    tially resolved pressure data points into a high-­resolution 150 × 200
missed. In addition, the reduction in the number of sensors in the         mapping, providing a more intuitive visualization of real-­time dis-
arch area provides space for the integration of core components            tribution. It smooths surfaces by minimizing curvature, making it
such as the battery and circuit board, thereby enhancing the integra-      particularly suitable for handling irregularly distributed data points
tion and stability of the system. The insole template is prepared by       and applications that require high data stability and smooth inter-
laser cutting polymethyl methacrylate (PMMA) sheets, and the               polation (66, 67). The third mode allows for continuous pressure
CNT/ACET/PDMS sensing layers are embedded into the PDMS in-                monitoring at specific sensor locations, with a real-­time display of
sole body through in situ cross-­linking to enhance stability and pre-     pressure change curves. This enables tracking of short-­term pres-
vent detachment due to strain and stress during movement (fig.             sure variations and facilitates easy lateral comparisons.
S19). Each sensor within the sensing insole consists of upper and              Monitoring pressure during the static state provides valuable in-
lower electrodes and a CNT/ACET/PDMS sensing layer with a cross            formation for evaluating standing posture and the distribution of
section of 8 mm by 8 mm. The electrode, featuring a protruding             skeletal pressure on the feet. Figure 4D illustrates schematic dia-
structure, is composed of a PI/polyethylene terephthalate (PET)/           grams and plantar pressure distributions for toe, midfoot, and
copper (Cu) sheet stack, which serves as the encapsulation layer,          heel contact. The smart insole system demonstrates excellent spatial
support layer, and conductive layer, respectively (fig. S20). The PI       resolution for plantar pressure, with high-­pressure areas perfectly

Wang et al., Sci. Adv. 11, eadu1598 (2025)   16 April 2025                                                                                  7 of 13

Fig. 4. Design and characterization of smart insole for pressure mapping. (A) System architecture of the smart insole system, including five components: FPSMs,
lithium battery, insole with 22-­channel CNT/ACET/PDMS sensors, PCB, and smartphone. (B) Photograph of the integrated smart insole system showing key functional
components. (C) Various visualization modes for pressure distribution available on the APP. (D) Schematic diagrams and plantar pressure distributions for toe, midfoot,
and heel contact. (E) Schematic diagrams, foot skeletal structure, and plantar pressure distributions for normal stance, genu varum, and genu valgum stances. (F) Dy-
namic pressure distribution heatmaps (0 to 10 s for walking and 10 to 20 s for running). (G) Pressure response curves of the 22-­channel CNT/ACET/PDMS sensors during
walking (6 to 10 s) and running (16 to 20 s), highlighting differences in pressure change frequency and contact time. Dynamic plantar pressure distributions (H) during
walking and (I) during running.

aligning with the contact regions. In addition, it reveals detailed                  valgum stance, the legs angle inward, shifting the center of gravity
pressure information, such as the low-­pressure areas in the arch and                laterally. Calculating the pressure data provides the actual center po-
interdigital spaces due to lack of actual contact with the foot. When                sitions, which are consistent with the analyzed results (fig. S23).
standing on tiptoes, the center of gravity shifts forward, and when                      Dynamic plantar pressure information includes force exertion
standing on heels, it shifts backward. Figure 4E illustrates the corre-              and body position data during movement. Recording the plantar
sponding posture schematics, foot skeletal structure, and measured                   pressure distribution with high spatiotemporal resolution and ana-
plantar pressure distribution for normal, genu varum, and genu val-                  lyzing it through various visualization methods can potentially con-
gum postures. In a normal stance, the center of gravity of the body is               tribute to the monitoring and correction of postures. Because of the
concentrated in the center of the foot. In a genu varum stance, the                  high level of integration, sensitivity, and linearity of the CNT/ACET/
legs bow outward, shifting the center of gravity medially. In a genu                 PDMS sensors, the smart insole system captures dynamic plantar

Wang et al., Sci. Adv. 11, eadu1598 (2025)   16 April 2025                                                                                                     8 of 13

pressure distributions during various movements and visualizes                 Figure 5C details the training process of the SVM model. The
them in real time. Figure 4 (F to I) shows sensor data in different        dataset included 1275 labeled samples, with 80% (1020 samples)
visualization modes for walking and running. Figure 4F shows the           used for training and 20% (255 samples) used for validation. For the
sensor pressure heatmap, illustrating the signal amplitude over time       SVM model, each sample collected from the 22 sensors was pro-
for the 22 sensors, while Fig. 4G presents the pressure variation          cessed into a 22-­dimensional vector, and the average of 160 data
curves over shorter time periods. Both figures reveal distinct and         points was used as the feature input. The SVM model achieved
periodic characteristics during walking (0 to 10 s) and running (10        100% recognition accuracy for the eight motion states (Fig. 5D). In
to 20 s) phases, indicating that the smart insole effectively captures     addition, we evaluated random forest and convolutional neural net-
and displays dynamic pressure distribution differences under vari-         work (CNN) models (fig. S25). The results show that the random
ous movement conditions with stability. Because of the sequential          forest model also achieved 100% recognition accuracy, while the
distribution of the sensors from toe to heel, the differences in the       CNN model achieved 99.55% accuracy but exhibited some instabil-
timing of the pressure curve rises can reveal the contact sequence         ity. This may be because CNN models rely more heavily on large-­
of the sensors with the ground. During walking, pressure is applied        scale datasets, which slightly hindered their performance in the
sequentially from the heel (sensor 22) to the toes (sensor 1), where-      current scenario.
as during running, almost all sensors are subjected to pressure si-            Compared to deep learning models, the SVM model offers advan-
multaneously. In addition, during walking, the pressure application        tages such as faster training speed, independence from large datasets,
time accounts for about half of the total time, while during running,      well-­defined decision boundaries, and clear optimization objectives,
it accounts for only about a quarter. For a more detailed analysis of      making it particularly well suited for precise classification in high-­
pressure distribution characteristics, high temporal resolution plan-      dimensional feature spaces. Therefore, SVM was ultimately selected
tar pressure distribution maps (Fig. 4, H and I) are required. During      as the motion state recognition model in this study. Moreover, the
walking, the heel contacts the ground first (0.2 s), followed by a         high spatiotemporal resolution of the smart insole’s data collection

gradual increase in contact area (0.4 s), with the center of gravity       capability is another key factor contributing to the high recognition
still on the heel. Subsequently, the heel lifts off, and the center of     accuracy. This capability ensures that the raw data contain distinctive
gravity shifts to the forefoot (0.6 s). In contrast, during running, the   features for different motion states. Principal components analysis
heel also contacts the ground first (0.1 s), but the contact area quick-   (PCA) in Fig. 5E further confirms this, as data points for the eight
ly increases to almost the entire foot (excluding some heel areas) by      motion states cluster in distinct regions, notably reducing classifica-
0.2 s, and then only the forefoot bears the pressure (0.3 s). The com-     tion difficulty. To provide a comparison of this system with previously
plementary use of different visualization modes enables multidi-           reported systems, including their advantages and limitations, table S3
mensional visualization and analysis of the dynamic pressure data.         has been included, highlighting its integration of self-­powering, pres-
    To evaluate the stability and consistency of the smart insole, a       sure sensing, and machine learning (8, 26–28, 34, 68–70).
test protocol comprising 315 s of jogging followed by 100 s of sprint-
ing is employed (fig. S24). Throughout the entire test, all sensors
operate stably without any signal loss or distortion, demonstrating        DISCUSSION
stable data output and reliable motion characteristics. This indicates     In summary, this work reports a fully integrated, wireless smart in-
that the smart insole can withstand the impacts of high-­intensity         sole system designed to collect plantar pressure with high spatio-
exercise and has long-­term stability in feature extraction, thereby       temporal resolution and visualize and analyze the results in real
laying a foundation for motion state acquisition and recognition           time on a smartphone. Major achievements include (i) the design
based on the smart insole.                                                 and fabrication of CNT/ACET/PDMS pressure sensors based on a
                                                                           nonlinear synergy strategy, which exhibit high linearity (R2 > 0.999)
Machine learning integration for motion detection in                       across the entire sensing range (0 to 225 kPa) and maintain perfor-
smart insole                                                               mance even after 180,000 cycles of compression and release testing;
The smart insole system incorporates an SVM model to classify and          (ii) the use of FPSCs to convert solar energy into electrical energy,
recognize different human motion states. Figure 5A outlines the            stored in lithium batteries, ensuring sustainable power supply for
main workflow. Plantar pressure data with spatiotemporal features          the wearable system; and (iii) the integration of an SVM learning
are collected under eight motion states, including sitting, standing,      model, enabling the insole to capture and accurately recognize eight
single-­leg standing, squatting, walking, running, and ascending and       distinct motion states. Beyond motion state recognition, the combi-
descending stairs. These data are then used to train the SVM model.        nation of machine learning and high-­resolution monitoring high-
After training, the model could classify incoming input data and           lights the system’s potential in diverse applications. In health care, it
generate recognition results. Figure 5B presents representative data       could support gait analysis to detect early abnormalities associated
collected under the eight motion states, shown as heatmaps over a          with foot pressure–related conditions (e.g., lumbar degenerative
duration of 5 s with a sampling rate of 32 Hz. In static states (e.g.,     diseases and diabetic foot ulcers), musculoskeletal disorders (e.g.,
sitting, standing, and single-­leg standing), the plantar pressure dis-    plantar fasciitis), or neurological conditions (e.g., Parkinson’s dis-
tribution remains stable and constant over time, with the primary          ease). Machine learning also offers opportunities for personalized
differences reflected in the signal amplitude. In dynamic states,          health management, including real-­time posture correction, injury
walking and running exhibit distinct temporal characteristics, such        prevention, and rehabilitation monitoring. Furthermore, in sports
as frequency and foot contact time. Squatting shows periodic pres-         science and ergonomics, the system could enable fatigue prediction,
sure variations on a relatively high baseline due to sustained pres-       motion optimization, and customized fitness training. In addition,
sure on the entire foot. Stair ascent primarily involves forefoot          the system is compatible with detecting other biosignals. Future in-
pressure, while stair descent involves more hindfoot pressure.             tegration of multimodal sensors, such as those for temperature,

Wang et al., Sci. Adv. 11, eadu1598 (2025)   16 April 2025                                                                                   9 of 13

Fig. 5. Machine learning integration for motion detection in smart insole. (A) Workflow diagram of the SVM learning model, including data collection, model setup,
classification, and result output. (B) Representative data for SVM training, capturing sitting, standing, single-­leg standing, squatting, walking, running, stair descent, and
stair ascent over 5 s at 32 Hz. (C) Flowchart of the SVM model training process. (D) Confusion matrix for the classification results on the test dataset. (E) Principal compo-
nents analysis (PCA) of data for different motions.

humidity, and electromyography, promises further exploration of                          dimethyl sulfoxide (DMSO)] was spin coated at 1600 rpm for 20 s
foot physiological data.                                                                 and 4000 rpm for 30 s and then annealed at 70°C for 2 min. Sub-
                                                                                         sequently, 120 μl of formamidine iodide/methylamine chloride/
                                                                                         methylamine bromide (FAI/MACl/MABr) solution (110 mg of
MATERIALS AND METHODS                                                                    FAI, 15 mg of MACl, and 10 mg of MABr in 1.5 ml of IPA) was
Preparation of PSC                                                                       spin coated at 2300 rpm for 20 s, transferred to an air atmosphere
Conductive substrates (ITO PEN, Peccell Technologies Inc., Japan)                        (RH = 40 to 45%), and annealed at 140°C for 20 min. After return-
were ultrasonically cleaned in anhydrous ethanol (Alfa Aesar) and                        ing to the glove box, 120 μl of IPA was spin coated at 4000 rpm for
isopropanol (IPA, Alfa Aesar), followed by drying with compressed                        30 s to clean unreacted components. The Spiro-­OMeTAD solution
air and oxygen plasma treatment. For ITO PEN, 100 μl of SnO2                             [726 mg of Spiro-­OMeTAD in 1 ml of chlorobenzene (CB) with
precursor (5% H2O colloidal dispersion, Alfa Aesar) was spin coated                      18 μl of lithium bis(trifluoromethanesulfonyl)imide (Li-­TFSI), 29 μl
onto the ITO PEN at 3000 rpm for 30 s, followed by annealing at                          of FK209, and 29 μl of tert-­butylpyridine] was spin coated at
150°C for 30 min. The conductive substrate was then treated with                         5000 rpm for 30 s and oxidized in a drying oven for 24 hours. Last,
oxygen plasma before being transferred to a glove box for the de-                        8 nm of MoO3 and 30 nm of Ag were evaporated as electrodes, and
position of the perovskite layer. The perovskite layer was applied                       the PSCs (area: 0.09 cm2) were encapsulated by spin coating pre-
using a two-­step spin-­coating method. First, 80 μl of lead iodide/                     configured Ecoflex onto the surface at 1500 rpm for 30 s. All chemicals,
cesium iodide (PbI2/CsI) solution [760 mg of PbI2 and 82 mg of                           including PbI2, CsI, FAI, MACl, MABr, Spiro-­OMeTAD, Li-­TFSI,
CsI in 1 ml of N,N′-­dimethylformamide (DMF) and 160 μl of                               and FK209, were sourced from Xi’an Polymer Light Technology

Wang et al., Sci. Adv. 11, eadu1598 (2025)   16 April 2025                                                                                                            10 of 13

Corp. The solvents, including DMF, DMSO, IPA, and CB, were pur-           Data processing and machine learning development
chased from Alfa Aesar and Innochem.                                      Participants performed sitting, standing, single-­leg standing, squat-
                                                                          ting, walking, running, and stair ascent and descent activities while
Preparation of the CNT/ACET/PDMS sensor                                   wearing the smart insole. Data were collected at a frequency of
The cube sugar (purchased from the supermarket) was immersed              32 Hz using an APP and stored locally. The raw data were processed
in PDMS prepolymer (PDMS:hardener 15:1, Dow Corning Corp.,                and segmented using a MATLAB script. Specifically, the first 10 s of
USA) and placed in vacuum for at least 6 hours to allow the PDMS          each dataset was removed to ensure alignment between data type
prepolymer to penetrate the pores of the cube sugar. Afterward, the       and activity state. Data were divided into 5-­s segments, each labeled
PDMS-­impregnated cube sugar was placed in an oven at 100°C for           accordingly. For each of the 22 sensors, 1000 data points were aver-
1 hour to fully cure the PDMS prepolymer. The cured PDMS/sugar            aged to form a 22-­dimensional feature vector. The SVM model was
complex was immersed in deionized water and placed in an oven at          trained using a linear kernel function with a penalty parameter set
60°C for 2 hours to dissolve the sugar to obtain PDMS foam. The           to 1. Standardization was applied to the features, ensuring a mean of
CNT/ACET/PDMS foam was obtained by immersing PDMS foam                    0 and a variance of 1. The random forest model was trained using
into the ethanol dispersion of CNT/ACET (Sigma-­Aldrich) and              100 decision trees, with each tree built using a bootstrap sample of
sonicating for 3 hours to make CNT/ACET fully enter the pores of          the training data and a random subset of features at each split. The
the PDMS foam. Last, the CNT/ACET/PDMS foam was dried to                  model used the bagging method, with the number of learning cycles
remove the ethanol and connected to the Cu electrode to obtain the        set to 100. No additional hyperparameter tuning was applied, and
strain sensor.                                                            the default Gini impurity criterion was used for measuring the qual-
                                                                          ity of splits. The CNN model was designed with an input size of
Preparation of the self-­powered smart insole                             22 × 1 × 1, corresponding to the 22 sensor features. The network
The self-­powered smart insole comprised two main modules: an en-         architecture consisted of two convolutional layers with filter sizes of

ergy harvesting and storage module, and a signal acquisition and          3 × 1 and filter counts of 16 and 32, respectively, each followed by
transmission module. A laser-­etched mask was used to sputter a           rectified linear unit activation and max-­pooling layers with strides
flexible Ag circuit onto a PET substrate, and two PSCs were installed     of 2 × 1. A fully connected layer mapped the feature space to eight
at designated positions to form the FPSM. The FPSM was then se-           motion states, followed by a softmax layer and a classification layer.
cured to the shoe upper and connected to the lithium battery and          The network was trained using the Adam optimizer with a learning
PCB with wires. The cured PDMS/sugar block was cut and polished           rate of 1 × 10−3 and a minibatch size of 32 for 20 epochs. Categorical
into 6 mm–by–6 mm–by–10 mm rectangular shapes and embedded                labels were used for training, and the input data were reshaped into
into slots in a custom template (made from laser-­cut PMMA sheets)        22 × 1 × 1 tensors to match the input format.
(fig. S19). PDMS was then poured for in situ curing. After curing,
the protruding sections were polished, and the entire insole was          Measurement and characterization
immersed in water to dissolve the sugar. Subsequently, CNTs and           The surface and cross-­sectional morphologies of the samples were
ACET were ultrasonically attached according to the sensor prepara-        imaged using a Hitachi S-­4800 scanning electron microscope. XRD
tion parameters. The insole electrode featured a protruding struc-        patterns were obtained with a Bruker D2 PHASER Diffractometer
ture (fig. S20), with 22 sensors sharing a common negative electrode.     using Cu Kα radiation. Absorbance spectra were measured using a
This electrode was connected to a flexible flat cable via an enamel-­     Hitachi U-­3900H UV-­Vis spectrometer. PL spectra were obtained
coated wire and then to the PCB. The core components of the PCB           with an RF-­5301PC fluorescence spectrophotometer. The J-­V mea-
included an MCU chip with an integrated 22-­channel ADC and a             surements of the devices under 1-­sun illumination (solar simulator,
BLE chip (fig. S16).                                                      AM 1.5G, SS-­F5-­3A, Enlitech) were performed using a program-
                                                                          mable Keithley 2400 source meter. The EQE spectrum and integrated
Reconstruction of pressure mapping of the insole                          J were obtained using a solar cell spectral response measurement
The smart insole system integrated 22 CNT/ACET/PDMS sensors               system (QE-­R3011, Enlitech). A multifunctional stress-­strain tester
with an uneven distribution, as shown in fig. S18. To analyze the         and Keithley 2612B source meter were used to simultaneously de-
pressure distribution characteristics of the entire foot, a 0-­pressure   tect the stress, resistance (potentiostatic method, bias voltage of 3 V),
boundary condition was applied at the edges of the insole. The            and I-­V curves (linear voltammetry, from −10 to 10 V) of strain sensors
biharmonic spline interpolation method, based on Green’s func-            at different strains. Mechanical stability tests of the strain sensors were
tions, was used to transform discrete pressure measurements into          performed on a homemade compression platform.
a high-­resolution 150 × 200 pressure distribution map. A Green’s
function matrix was constructed using sensor coordinates to de-
fine kernel function values between   [ sensor] points. The kernel        Supplementary Materials
function was expressed as ϕ(d) = d 2 ln(d) − 1 , where 𝑑 represents       This PDF file includes:
the Euclidean distance between sensor points. Gaussian elimina-           Figs. S1 to S25
                                                                          Tables S1 to S3
tion was used to invert this matrix, and the resulting coefficients
were multiplied by the pressure values recorded by the 22 sensors
to calculate the interpolation weights. These weights and the ker-        REFERENCES AND NOTES
                                                                            1. Z. Zhang, Y. Dai, Z. Xu, N. Grimaldi, J. Wang, M. Zhao, R. Pang, Y. Sun, S. Gao, H. Boyi, Insole
nel function were then applied to each point in the target grid
                                                                               systems for disease diagnosis and rehabilitation: A review. Biosensors 13, 833 (2023).
to generate the interpolated surface. Parallelization directives were       2. K. E. Chatwin, C. A. Abbott, A. J. M. Boulton, F. L. Bowling, N. D. Reeves, The role of foot
implemented within the interpolation loop to improve computa-                  pressure measurement in the prediction and prevention of diabetic foot ulceration—
tional efficiency.                                                             A comprehensive review. Diabetes Metab. Res. Rev. 36, e3258 (2020).

Wang et al., Sci. Adv. 11, eadu1598 (2025)   16 April 2025                                                                                                           11 of 13

 3.	C. Herbers, R. Zhang, A. Erdman, M. D. Johnson, Distinguishing features of Parkinson’s                 29.	D. Rajendran, R. Ramalingame, S. Palaniyappan, G. Wagner, O. Kanoun, Flexible ultra-­thin
    disease fallers based on wireless insole plantar pressure monitoring. NPJ Parkinsons Dis.                  nanocomposite-­based piezoresistive pressure sensors for foot pressure distribution
    10, 67 (2024).                                                                                             measurement. Sensors 21, 6082 (2021).
 4. M. Seo, M.-­J. Shin, T. S. Park, J. H. Park, Clinometric gait analysis using smart insoles in          30. X. Wu, Y. Khan, J. Ting, J. Zhu, S. Ono, X. Zhang, S. Du, J. W. Evans, C. Lu, A. C. Arias,
    patients with hemiplegia after stroke: Pilot study. JMIR Mhealth Uhealth 8, e22208 (2020).                 Large-­area fabrication of high-­performance flexible and wearable pressure sensors.
 5. R. J. Davies, J. Parker, P. McCullagh, H. Zheng, C. Nugent, N. D. Black, S. Mawson,                        Adv. Electron. Mater. 6, 1901310 (2020).
    A personalized self-­management rehabilitation system for stroke survivors: A                          31. A. G. Samarentsis, G. Makris, S. Spinthaki, G. Christodoulakis, M. Tsiknakis, A. K. Pantazis,
    quantitative gait analysis using a smart insole. JMIR Rehabil. Assist. Technol. 3, e11 (2016).             A 3D-­printed capacitive smart insole for plantar pressure monitoring. Sensors 22, 9725
 6. J. S. Lee, K. B. Kim, J. O. Jeong, N. Y. Kwon, S. M. Jeong, Correlation of foot posture index              (2022).
    with plantar pressure and radiographic measurements in pediatric flatfoot.                             32. J. Tang, D. L. Bader, D. Moser, D. J. Parker, S. Forghany, C. J. Nester, L. Jiang, A wearable
    Ann. Rehabil. Med. 39, 10–17 (2015).                                                                       insole system to measure plantar pressure and shear for people with diabetes. Sensors
 7. F. Khan, M. F. Chevidikunnan, E. A. BinMulayh, N. S. Al-­Lehidan, Plantar pressure                         23, 3126 (2023).
    distribution in the evaluation and differentiation of flatfeet. Gait Posture 101, 82–89                33. W. Wang, J. Cao, J. Yu, R. Liu, C. R. Bowen, W.-­H. Liao, Self-­powered smart insole for
    (2023).                                                                                                    monitoring human gait signals. Sensors 19, 5336 (2019).
 8.	D. Liu, D. Zhang, Z. Sun, S. Zhou, W. Li, C. Li, W. Li, W. Tang, Z. L. Wang, Active-­matrix            34.	C. Deng, W. Tang, L. Liu, B. Chen, M. Li, Z. L. Wang, Self-­powered insole plantar pressure
    sensing array assisted with machine-­learning approach for lumbar degenerative disease                     mapping system. Adv. Funct. Mater. 28, 1801606 (2018).
    diagnosis and postoperative assessment. Adv. Funct. Mater. 32, 2113008 (2022).                         35. Z. Lin, Z. Wu, B. Zhang, Y.-­C. Wang, H. Guo, G. Liu, C. Chen, Y. Chen, J. Yang, Z. L. Wang,
 9.	D. De León Rodriguez, L. Allet, A. Golay, J. Philippe, J. P. Assal, C. A. Hauert, Z. Pataky,               A triboelectric nanogenerator-­based smart insole for multifunctional gait monitoring.
    Biofeedback can reduce foot pressure to a safe level and without causing new at-­risk                      Adv. Mater. Technol. 4, 1800360 (2019).
    zones in patients with diabetes and peripheral neuropathy. Diabetes Metab. Res. Rev. 29,               36. Q. Zhang, T. Jin, J. Cai, L. Xu, T. He, T. Wang, Y. Tian, L. Li, Y. Peng, C. Lee, Wearable
    139–144 (2013).                                                                                            triboelectric sensors enabled gait analysis and waist motion capture for IoT-­based smart
10.	C. Gerlach, D. Krumm, M. Illing, J. Lange, O. Kanoun, S. Odenwald, A. Hübler, Printed                      healthcare applications. Adv. Sci. 9, 2103694 (2022).
    MWCNT-­PDMS-­composite pressure sensor system for plantar pressure monitoring in                       37. Z. Shi, L. Meng, X. Shi, H. Li, J. Zhang, Q. Sun, X. Liu, J. Chen, S. Liu, Morphological
    ulcer prevention. IEEE Sens. J. 15, 3647–3656 (2015).                                                      engineering of sensing materials for flexible pressure sensors and artificial intelligence
11. R. Ramalingame, Z. Hu, C. Gerlach, D. Rajendran, T. Zubkova, R. Baumann, O. Kanoun,                        applications. Nano-­Micro Lett. 14, 141 (2022).

    Flexible piezoresistive sensor matrix based on a carbon nanotube PDMS composite for                    38. S. Li, Y. Cheng, K. Deng, H. Sun, A self-­powered flexible tactile sensor utilizing chemical
    dynamic pressure distribution measurement. J. Sens. Sens. Syst. 8, 1–7 (2019).                             battery reactions to detect static and dynamic stimuli. Nano Energy 124, 109461 (2024).
12. A. S. Pollock, B. R. Durward, P. J. Rowe, J. P. Paul, What is balance? Clin. Rehabil. 14,              39.	D. Yoo, D.-­J. Won, W. Cho, J. Lim, J. Kim, Double-­side electromagnetic interference-­
    402–406 (2000).                                                                                            shielded bending-­insensitive capacitive-­type flexible touch sensor with linear response
13. S. D. Kim, N. E. Allen, C. G. Canning, V. S. Fung, Postural instability in patients with                   over a wide detection range. Adv. Mater. Technol. 6, 2100358 (2021).
    Parkinson’s disease: Epidemiology, pathophysiology and management. CNS Drugs 27,                       40. S. R. A. Ruth, V. R. Feig, M.-­g. Kim, Y. Khan, J. K. Phong, Z. Bao, Flexible fringe effect
    97–112 (2013).                                                                                             capacitive sensors with simultaneous high-­performance contact and non-­contact
14.	E. B. Titianova, K. Pitkänen, A. Pääkkönen, J. Sivenius, I. M. Tarkka, Gait characteristics and            sensing capabilities. Small Struct. 2, 2000079 (2021).
    functional ambulation profile in patients with chronic unilateral stroke. Am. J. Phys. Med.            41. S. Liu, X. Wu, D. Zhang, C. Guo, P. Wang, W. Hu, X. Li, X. Zhou, H. Xu, C. Luo, J. Zhang, J. Chu,
    Rehabil. 82, 778–786 (2003).                                                                               Ultrafast dynamic pressure sensors based on graphene hybrid structure. ACS Appl. Mater.
15.	C.-­B. Phan, K. M. Lee, S.-­S. Kwon, S. Koo, Kinematic instability in the joints of flatfoot               Interfaces 9, 24148–24154 (2017).
    subjects during walking: A biplanar fluoroscopic study. J. Biomech. 127, 110681 (2021).                42.	N. Luo, W. Dai, C. Li, Z. Zhou, L. Lu, C. C. Y. Poon, S.-­C. Chen, Y. Zhang, N. Zhao, Flexible
16. R. G. Frykberg, L. A. Lavery, H. Pham, C. Harvey, L. Harkless, A. Veves, Role of neuropathy                piezoresistive sensor patch enabling ultralow power cuffless blood pressure
    and high foot pressures in diabetic foot ulceration. Diabetes Care 21, 1714–1719 (1998).                   measurement. Adv. Funct. Mater. 26, 1178–1187 (2016).
17. S. C. Wu, R. T. Crews, D. G. Armstrong, The pivotal role of offloading in the management of            43.	H.-­B. Yao, J. Ge, C.-­F. Wang, X. Wang, W. Hu, Z.-­J. Zheng, Y. Ni, S.-­H. Yu, A flexible and highly
    neuropathic foot ulceration. Curr. Diab. Rep. 5, 423–429 (2005).                                           pressure-­sensitive graphene–polyurethane sponge based on fractured microstructure
18. A. A. Gomes, M. Ackermann, J. P. Ferreira, M. I. V. Orselli, I. C. N. Sacco, Muscle force                  design. Adv. Mater. 25, 6692–6698 (2013).
    distribution of the lower limbs during walking in diabetic individuals with and without                44. A. Dzedzickis, E. Sutinys, V. Bucinskas, U. Samukaite-­Bubniene, B. Jakstys, A. Ramanavicius,
    polyneuropathy. J. Neuroeng. Rehabil. 14, 111 (2017).                                                      I. Morkvenaite-­Vilkonciene, Polyethylene-­carbon composite (Velostat®)-­based tactile
19.	D. G. Armstrong, A. J. Boulton, S. A. Bus, Diabetic foot ulcers and their recurrence.                      sensor. Polymers 12, 2905 (2020).
    N. Engl. J. Med. 376, 2367–2375 (2017).                                                                45. Y. Song, D. Mukasa, H. Zhang, W. Gao, Self-­powered wearable biosensors. Acc. Mater. Res.
20. K. Busch, E. Chantelau, Effectiveness of a new brand of stock ‘diabetic’ shoes to protect                  2, 184–197 (2021).
    against diabetic foot ulcer relapse: A prospective cohort study. Diabet. Med. 20, 665–669              46. W. Zhai, Q. Xia, K. Zhou, X. Yue, M. Ren, G. Zheng, K. Dai, C. Liu, C. Shen, Multifunctional
    (2003).                                                                                                    flexible carbon black/polydimethylsiloxane piezoresistive sensor with ultrahigh linear
21.	V. Scirè, E. Leporati, I. Teobaldi, L. A. Nobili, L. Rizzo, A. Piaggesi, Effectiveness and safety of       range, excellent durability and oil/water separation capability. Chem. Eng. J. 372, 373–382
    using Podikon digital silicone padding in the primary prevention of neuropathic lesions                    (2019).
    in the forefoot of diabetic patients. J. Am. Podiatr. Med. Assoc. 99, 28–34 (2009).                    47. B. Ji, Q. Zhou, B. Hu, J. Zhong, J. Zhou, B. Zhou, Bio-­inspired hybrid dielectric for capacitive
22. M. J. Hessert, M. Vyas, J. Leach, K. Hu, L. A. Lipsitz, V. Novak, Foot pressure distribution               and triboelectric tactile sensors with high sensitivity and ultrawide linearity range.
    during walking in young and old adults. BMC Geriatr. 5, 8 (2005).                                          Adv. Mater. 33, 2100859 (2021).
23.	C. Xu, X.-­X. Wen, L.-­Y. Huang, L. Shang, X.-­X. Cheng, Y.-­B. Yan, W. Lei, Normal foot loading       48.	N. Bai, L. Wang, Y. Xue, Y. Wang, X. Hou, G. Li, Y. Zhang, M. Cai, L. Zhao, F. Guan, X. Wei,
    parameters and repeatability of the Footscan® platform system. J. Foot Ankle Res. 10, 30                   C. F. Guo, Graded interlocks for iontronic pressure sensors with high sensitivity and high
    (2017).                                                                                                    linearity over a broad range. ACS Nano 16, 4338–4347 (2022).
24. S. A. Bus, J. S. Ulbrecht, P. R. Cavanagh, Pressure relief and load redistribution by                  49. Y. R. Kim, M. P. Kim, J. Park, Y. Lee, S. K. Ghosh, J. Kim, D. Kang, H. Ko, Binary spiky/spherical
    custom-­made insoles in diabetic patients with neuropathy and foot deformity.                              nanoparticle films with hierarchical micro/nanostructures for high-­performance flexible
    Clin. Biomech. 19, 629–638 (2004).                                                                         pressure sensors. ACS Appl. Mater. Interfaces 12, 58403–58411 (2020).
25. J. Xu, H. Li, Y. Yin, X. Li, J. Cao, H. Feng, W. Bao, H. Tan, F. Xiao, G. Zhu, High sensitivity and    50.	T. Zhao, L. Yuan, T. Li, L. Chen, X. Li, J. Zhang, Pollen-­shaped hierarchical structure for
    broad linearity range pressure sensor based on hierarchical in-­situ filling porous                        pressure sensors with high sensitivity in an ultrabroad linear response range.
    structure. npj Flex Electron. 6, 62 (2022).                                                                ACS Appl. Mater. Interfaces 12, 55362–55371 (2020).
26. Q. Zheng, X. Dai, Y. Wu, Q. Liang, Y. Wu, J. Yang, B. Dong, G. Gao, Q. Qin, L.-­B. Huang,              51.	H. Xu, L. Gao, Y. Wang, K. Cao, X. Hu, L. Wang, M. Mu, M. Liu, H. Zhang, W. Wang, Y. Lu,
    Self-­powered high-­resolution smart insole system for plantar pressure mapping. BMEMat                    Flexible waterproof piezoresistive pressure sensors with wide linear working range based
    1, e12008 (2023).                                                                                          on conductive fabrics. Nanomicro Lett. 12, 159 (2020).
27. J. Tao, M. Dong, L. Li, C. Wang, J. Li, Y. Liu, R. Bao, C. Pan, Real-­time pressure mapping            52. M. Zhong, L. Zhang, X. Liu, Y. Zhou, M. Zhang, Y. Wang, L. Yang, D. Wei, Wide linear range
    smart insole system based on a controllable vertical pore dielectric layer.                                and highly sensitive flexible pressure sensor based on multistage sensing process for
    Microsyst. Nanoeng. 6, 62 (2020).                                                                          health monitoring and human-­machine interfaces. Chem. Eng. J. 412, 128649 (2021).
28. X. Li, X. Liu, W. Zeng, D. Ding, B. Liu, Y. Li, Z. Zhao, S. Zhan, W. Zhu, Z. Chen, J. Huang, J. Luo,   53. R. Chen, T. Luo, J. Wang, R. Wang, C. Zhang, Y. Xie, L. Qin, H. Yao, W. Zhou, Nonlinearity
    Carbon fiber-­based smart plantar pressure mapping insole system for remote gait                           synergy: An elegant strategy for realizing high-­sensitivity and wide-­linear-­range pressure
    analysis and motion identification. Adv. Mater. Technol. 8, 2300095 (2023).                                sensing. Nat. Commun. 14, 6641 (2023).

Wang et al., Sci. Adv. 11, eadu1598 (2025)            16 April 2025                                                                                                                                     12 of 13

54. Y. Xiao, D. Guo, L. Yang, Y. Tong, X. Wu, Y. Wang, Fabric-­based capacitive pressure sensors        65.	D. Chen, Y. Cai, J. Cui, J. Chen, H. Jiang, M.-­C. Huang, Risk factors identification and
    for porous four-­phase composites with high sensitivity and wide linearity range.                       visualization for work-­related musculoskeletal disorders with wearable and connected
    Compos. Sci. Technol. 256, 110794 (2024).                                                               gait analytics system and Kinect skeleton models. Smart Health 7–8, 60–77 (2018).
55.	V.-­D. Tran, S. V. N. Pammi, B.-­J. Park, Y. Han, C. Jeon, S.-­G. Yoon, Transfer-­free graphene     66. X. Deng, Z. A. Tang, Moving surface spline interpolation based on Green’s function. Math.
    electrodes for super-­flexible and semi-­transparent perovskite solar cells fabricated under            Geosci. 43, 663–680 (2011).
    ambient air. Nano Energy 65, 104018 (2019).                                                         67.	D. T. Sandwell, Biharmonic spline interpolation of GEOS-­3 and SEASAT altimeter data.
56. Z. Wang, L. Zeng, C. Zhang, Y. Lu, S. Qiu, C. Wang, C. Liu, L. Pan, S. Wu, J. Hu, G. Liang,             Geophys. Res. Lett. 14, 139–142 (1987).
    P. Fan, H.-­J. Egelhaaf, C. J. Brabec, F. Guo, Y. Mai, Rational interface design and morphology     68. W. Li, K. Zou, J. Guo, C. Zhang, J. Feng, J. You, G. Cheng, Q. Zhou, M. Kong, G. Li, C. F. Guo,
    control for blade-­coating efficient flexible perovskite solar cells with a record fill factor of       J. Yang, Integrated fibrous iontronic pressure sensors with high sensitivity and reliability
    81%. Adv. Funct. Mater. 30, 2001240 (2020).                                                             for human plantar pressure and gait analysis. ACS Nano 18, 14672–14684 (2024).
57. X. Meng, Z. Cai, Y. Zhang, X. Hu, Z. Xing, Z. Huang, Z. Huang, Y. Cui, T. Hu, M. Su, X. Liao,       69.	H. Zhou, Y. Gui, G. Gu, H. Ren, W. Zhang, Z. Du, G. Cheng, A plantar pressure detection and
    L. Zhang, F. Wang, Y. Song, Y. Chen, Bio-­inspired vertebral design for scalable and flexible           gait analysis system based on flexible triboelectric pressure sensor array and deep
    perovskite solar cells. Nat. Commun. 11, 3016 (2020).                                                   learning. Small 21, 2405064 (2025).
58. M. Karimipour, S. Khazraei, B. J. Kim, G. Boschloo, E. M. J. Johansson, Efficient and bending       70. A. Mensah, S. Liao, J. Amesimeku, J. Li, Y. Chen, Y. Hao, J. Yang, Q. Wang, F. Huang, Y. Liu,
    durable flexible perovskite solar cells via interface modification using a combination of               Q. Wei, P. Lv, Therapeutic smart insole technology with Archimedean algorithmic spiral
    thin MoS2 nanosheets and molecules binding to the perovskite. Nano Energy 95, 107044                    triboelectric nanogenerator-­based power system and sensors. Adv. Fiber Mater. 6,
    (2022).                                                                                                 1746–1764 (2024).
59. Z. Lu, Y. Lou, L. Xiao, X. Xu, C. Wang, L. Li, X. Su, G. Zou, Grain-­slip derived network
    topology to remarkable strength–toughness combination of perovskite film for flexible               Acknowledgments
    solar cells. Adv. Energy Mater. 12, 2202298 (2022).                                                 Funding: This work was supported by the National Natural Science Foundation of China
60. X. Yang, H. Yang, M. Su, J. Zhao, X. Meng, X. Hu, T. Xue, Z. Huang, Y. Lu, Y. Li,                   (62374077 to W.L. and 62404088 to H.S.); the Key Project of Natural Science Foundation of
    Z. Yang, Scalable flexible perovskite solar cells based on a crystalline and                        Gansu Province (24JRRA395 to W.L.); the Gansu Province Joint Scientific Research Fund Project
    printable template with intelligent temperature sensitivity. Solar RRL 6, 2100991                   (24JRRA818 to H.S.); the Key Research and Development Projects in Gansu Province (to W.L.);
    (2022).                                                                                             the State Key Laboratory of Flexible Electronics Technology (to W.L.); and the Supporting Fund
61. S. Kim, H. Oh, G. Kang, I. K. Han, I. Jeong, M. Park, High-­power and flexible indoor solar         for Young Researchers from Lanzhou University (to H.S.). Author contributions:

    cells via controlled growth of perovskite using a greener antisolvent. ACS Appl. Energy             Conceptualization: W.L., Q.W., and H.G. Methodology: W.L., Q.W., and H.G. Software: C.W., Q.W.,
    Mater. 3, 6995–7003 (2020).                                                                         and C.G. Investigation: Q.W., H.G., P.L., H.S., H.B., J.H., C.G., Y.M., J.Y., and M.S. Resources: W.L., Z.J.,
62. W. Deng, F. Li, J. Li, M. Wang, Y. Hu, M. Liu, Anti-­solvent free fabrication of FA-­based          J.L., and H.S. Writing—original draft: Q.W. and H.G. Writing—review and editing: Q.W., W.L., and
    perovskite at low temperature towards high performance flexible perovskite solar cells.             J.L. Visualization: Q.W., H.G., W.L., and J.L. Funding acquisition: W.L. and H.S. Competing
    Nano Energy 70, 104505 (2020).                                                                      interests: The authors declare that they have no competing interests. Data and materials
63. Q. Sun, S. Duan, G. Liu, X. Meng, D. Hu, J. Deng, B. Shen, B. Kang, S. R. P. Silva,                 availability: All data needed to evaluate the conclusions in the paper are present in the paper
    Porous lead iodide layer promotes organic amine salt diffusion to achieve                           and/or the Supplementary Materials.
    high-­performance p-­i-­n flexible perovskite solar cells. Adv. Energy Mater. 13,
    2301259 (2023).                                                                                     Submitted 25 October 2024
64. F. Xiao, Z. Wei, Z. Xu, H. Wang, J. Li, J. Zhu, Fully 3D-­printed soft capacitive                   Accepted 12 March 2025
    sensor of high toughness and large measurement range. Adv. Sci. 12, 2410284                         Published 16 April 2025
    (2025).                                                                                             10.1126/sciadv.adu1598

Wang et al., Sci. Adv. 11, eadu1598 (2025)          16 April 2025                                                                                                                                        13 of 13

    A wireless, self-powered smart insole for gait monitoring and recognition via
    nonlinear synergistic pressure sensing
    Qi Wang, Hui Guan, Chen Wang, Peiming Lei, Hongwei Sheng, Huasheng Bi, Jinkun Hu, Chenhui Guo, Yichuan Mao, Jiao
    Yuan, Mingjiao Shao, Zhiwen Jin, Jinghua Li, and Wei Lan

    Sci. Adv. 11 (16), eadu1598. DOI: 10.1126/sciadv.adu1598

    View the article online

    https://www.science.org/doi/10.1126/sciadv.adu1598
    Permissions
    https://www.science.org/help/reprints-and-permissions

Use of this article is subject to the Terms of service

Science Advances (ISSN 2375-2548) is published by the American Association for the Advancement of Science. 1200 New York Avenue
NW, Washington, DC 20005. The title Science Advances is a registered trademark of AAAS.

Copyright © 2025 The Authors, some rights reserved; exclusive licensee American Association for the Advancement of Science. No claim
to original U.S. Government Works. Distributed under a Creative Commons Attribution NonCommercial License 4.0 (CC BY-NC).

