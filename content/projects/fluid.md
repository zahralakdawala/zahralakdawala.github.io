### How research drives innovation and technology in the context of Fluidized Bed Crystallizers

Crystalline solid products are around us everywhere – it is an important part of the industrially relevant production as 70% of the products of the chemical and pharmaceutical industry are sold as solids - an example is an aspirin tablet that you’d take for a headache. An important part in designing a crystallization process of getting solid materials from liquid solutions is to control the crystal size and shape of the crystals. Fundamental and applied research in this area of crystallization leads to improved process performance with less energy consumption as well as more efficient material utilization. Also the product quality and specifications like size and its distribution, shape, and agglomeration degree have to be considered in more detail, as many process steps are dependent on such characteristics.

![](/ForParticleMagazine/image002.jpg)
![](/ForParticleMagazine/image004.jpg)

<sup>Figure 1 (left) illustrates such a crystallizer that was set up for experimental validations. The solution is removed from the top of the fluidized bed crystallizer through a filter. It is pumped back into the device from the bottom to fluidize the crystals. The crystallizer is cooled by a double jacket to increase the supersaturation over time. Crystals can be sampled from a variable height in the fluidized bed crystallizer during an experiment. The crystal shape can be analyzed by a flow-through microscope. Right: A schematic view of the geometry model used in simulations.</sup>

Such solid-liquid systems are complex and challenging in many ways and fluid flow and particles interact in a variety of fashions. In the lab setup, the evolution of the crystal size and shape distribution is tracked by means of image-based shape estimation (Figure1-left). This information is then in turn exploited to obtain the crystallization kinetics that are governing the crystallization process. To incorporate these complexities, the numerical methods have been extended and new tools are developed to simulate crystallization in a better way. Our focus has been on relevant phenomena of crystal growth of multi-faceted crystals as well as on crystal agglomeration with specifically developed model experiments working with selected well understood model substances.

Experiments and flow field simulations serve to parameterize a coupled population balance equation system. This equation system allows predicting the dynamic evolution of the crystal size and shape distribution. Crystal agglomeration is a major phenomenon of crystal size enlargement. Our research concentrates on the understanding and modeling of this phenomenon.

The crystal growth and agglomeration can be combined, where the main control variables are temperature profiles and flow rates. Crystals can be separated by size and withdrawn at a varying crystallizer height. The size separation is again controlled by the flow rates.

![](/ForParticleMagazine/image006.png)
![](/ForParticleMagazine/image008.jpg)

<sup>Figure 2: Left: illustrates the computational domain and its decomposition in tetrahedra. The computational domain neglects the small inlet extension at the bottom, compared with the fluidized bed crystallizer used in the experiment. Right: The velocities computed using a Smagorinsky Large Eddy Simulation model.</sup>

Crystallization processes are often modeled in terms of a crystal population instead of considering the behavior of each individual crystal. Utilizing macroscopic conservation laws, one derives a system of coupled equations for the population, a so-called Population Balance System (PBS), that describes an averaged behavior of the crystals. The crystallization process within a moving incompressible fluid is modeled – the movement is in pipes and/or batch crystallizers . It is assumed that the suspension of the crystals is dilute such that the impact of the crystals on the fluid flow is negligible. Then, the first two conservation laws are the balance of the linear momentum and the conservation of mass for the fluid flow, which are modeled by the incompressible Navier–Stokes equations.

![](/ForParticleMagazine/image010.jpg)
![](/ForParticleMagazine/image012.jpg)

<sup>Figure3: Comparison between experiments(left) and simulation results(right). The plots show the crystal growth over time and their average sizes at harvesting depths. One can see that there is a particularly good agreement. In both cases, there is no separation of different sizes of crystals in different heights of the fluidized bed crystallizer. </sup>

Our study shows that the simulations can indeed be used to model the processes in Fluidized Bed Crystallizers. There is a good agreement between experimental and simulation results. These can be further tested virtually using different operating conditions and settings and this paves a way for cheaper, faster and informed design and innovation of future fluidized bed crystallizers.

#### Relevant Articles:

[1] Bartsch, C., Wiedmeyer, V., Lakdawala, Z., Patterson, R. I., Voigt, A., Sundmacher, K., et al. (2019). Stochastic-Deterministic Population Balance Modeling and Simulation of a Fluidized Bed Crystallizer Experiment. Chemical Engineering Science, 208: 115102. doi:10.1016/j.ces.2019.07.020.

[2] Wiedmeyer, V., Voigt, A. and Sundmacher, K.(2017). Crystal population growth in a continuous helically coiled flow tube crystallizer. Chemical Engineering & Technology, 40, 1584-1590.

[3] Wiedmeyer, V., Anker, F., Bartsch, C., Voigt, A., John, V. and Sundmacher, K.(2017). Continuous Crystallization in a Helically Coiled Flow Tube: Analysis of Flow Field, Residence Time Behavior, and Crystal Growth. Industrial & Engineering Chemistry Research, 56 (13), 3699-3712.
