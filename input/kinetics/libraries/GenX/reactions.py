#!/usr/bin/env python
# encoding: utf-8

name = "GenX"
shortDesc = "GenX"
longDesc = """
Thermal treatment of Hexafluoropropylene oxide dimer acid (HFPO-DA, C3F7OCF­(CF3)­C­(O)­OH) or "GenX". Computed by Goldsmith group using microcanonical rate theory and master equation. Includes reactions involving perflouro alpha-lactone ethers, perfluoroesters, perfluoroaldehydes, perfluorocarboxylic acids, perfluoro alpha-lactones, perfluorinated radicals, and perfluorinated singlet carbene (CF2). 

Caroline L. Rocchio, Kurt D. Pennell, C. Franklin Goldsmith; Computational Investigation of the Reaction Mechanism for the Thermal Treatment of Hexafluoropropylene Oxide Dimer Acid (GenX). J. Phys. Chem. A 19 June 2025; 129 (24): 5343–5358. https://doi.org/10.1021/acs.jpca.5c01170


Obtained from : https://pubs.acs.org/jpcafh/article-abstract/129/24/5343/3647996/Computational-Investigation-of-the-Reaction?redirectedFrom=fulltext
"""


entry(
index = 0,    
label = "GenX <=> C3F7OC(CF3)OCO + HF", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (5.760e+23, 's^-1'),
            n = -3.29,
            Ea = (52.47, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.820e+19, 's^-1'),
            n = -1.89,
            Ea = (50.98, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (4.040e+17, 's^-1'),
            n = -1.38,
            Ea = (50.42, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.750e+17, 's^-1'),
            n = -1.26,
            Ea = (50.3, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (6.940e+16, 's^-1'),
            n = -1.14,
            Ea = (50.16, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 1,    
label = "C3F7OC(CF3)OCO <=> C3F7OC(O)CF3 + CO", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (3.490e+38, 's^-1'),
            n = -8.66,
            Ea = (23.97, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (6.600e+37, 's^-1'),
            n = -8.41,
            Ea = (23.85, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (3.270e+37, 's^-1'),
            n = -8.31,
            Ea = (23.76, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (3.020e+37, 's^-1'),
            n = -8.3,
            Ea = (23.75, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.820e+37, 's^-1'),
            n = -8.29,
            Ea = (23.75, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 2,    
label = "C3F7OC(O)CF3 <=> C2F5CFO + CF3CFO", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (1.020e+18, 's^-1'),
            n = -1.87,
            Ea = (52.23, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.940e+17, 's^-1'),
            n = -1.7,
            Ea = (52.05, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.620e+17, 's^-1'),
            n = -1.69,
            Ea = (52.03, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.580e+17, 's^-1'),
            n = -1.68,
            Ea = (52.03, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.540e+17, 's^-1'),
            n = -1.68,
            Ea = (52.03, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 3,    
label = "C2F5CFO <=> CF2CFO + CF3", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (3.570e+48, 's^-1'),
            n = -9.7,
            Ea = (95.82, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.540e+40, 's^-1'),
            n = -7.09,
            Ea = (93.41, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.210e+35, 's^-1'),
            n = -5.41,
            Ea = (91.75, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.010e+33, 's^-1'),
            n = -4.76,
            Ea = (91.09, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (4.220e+27, 's^-1'),
            n = -3.08,
            Ea = (89.32, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 4,    
label = "CF3CFO <=> CF3 + CFO", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (3.510e+48, 's^-1'),
            n = -9.89,
            Ea = (98.1, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.360e+43, 's^-1'),
            n = -8.05,
            Ea = (96.94, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (5.600e+38, 's^-1'),
            n = -6.61,
            Ea = (95.79, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (6.670e+36, 's^-1'),
            n = -5.99,
            Ea = (95.26, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (7.640e+30, 's^-1'),
            n = -4.09,
            Ea = (93.49, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 5,    
label = "CF2CFO <=> CF2 + CFO", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (5.750e+47, 's^-1'),
            n = -10.44,
            Ea = (61.48, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.430e+47, 's^-1'),
            n = -9.96,
            Ea = (62.03, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (5.370e+45, 's^-1'),
            n = -9.33,
            Ea = (62.16, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (6.090e+44, 's^-1'),
            n = -8.96,
            Ea = (62.1, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.440e+40, 's^-1'),
            n = -7.33,
            Ea = (61.3, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 6,    
label = "C2F5CFO + H2O <=> C2F5C(O)OH + HF", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(1.850000e-02, 'cm^3/(mol*s)'), n=3.71, Ea=(28.439, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 7,    
label = "CF3CFO + H2O <=> CF3C(O)OH + HF", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(5.140000e-02, 'cm^3/(mol*s)'), n=3.6, Ea=(28.042, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 8,    
label = "CF2O + H2O <=> FC(O)OH + HF", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(2.420000e-01, 'cm^3/(mol*s)'), n=3.33, Ea=(32.745, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 9,    
label = "C2F5C(O)OH <=> CF3-c_FCOC(O) + HF", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (1.410e+21, 's^-1'),
            n = -2.59,
            Ea = (60.12, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.130e+17, 's^-1'),
            n = -1.31,
            Ea = (58.79, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (7.250e+14, 's^-1'),
            n = -0.62,
            Ea = (58.06, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.200e+14, 's^-1'),
            n = -0.38,
            Ea = (57.8, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.580e+12, 's^-1'),
            n = 0.2,
            Ea = (57.17, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 10,    
label = "CF3-c_FCOC(O) <=> CF3CFO + CO", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (5.040e+38, 's^-1'),
            n = -8.85,
            Ea = (20.81, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.530e+34, 's^-1'),
            n = -7.14,
            Ea = (20.65, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (8.920e+29, 's^-1'),
            n = -5.53,
            Ea = (20.0, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (7.860e+27, 's^-1'),
            n = -4.81,
            Ea = (19.63, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (6.290e+21, 's^-1'),
            n = -2.72,
            Ea = (18.4, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 11,    
label = "CF3C(O)OH <=> HF + c_F2COC(O)", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (3.670e+24, 's^-1'),
            n = -3.61,
            Ea = (57.08, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.640e+18, 's^-1'),
            n = -1.6,
            Ea = (55.1, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.790e+15, 's^-1'),
            n = -0.68,
            Ea = (54.15, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.340e+14, 's^-1'),
            n = -0.4,
            Ea = (53.86, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (4.940e+12, 's^-1'),
            n = 0.12,
            Ea = (53.3, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 12,    
label = "c_F2COC(O) <=> CF2O + CO", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (2.240e+22, 's^-1'),
            n = -4.09,
            Ea = (9.887, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (5.860e+22, 's^-1'),
            n = -3.87,
            Ea = (10.48, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (3.390e+22, 's^-1'),
            n = -3.55,
            Ea = (10.89, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (7.000e+22, 's^-1'),
            n = -3.55,
            Ea = (11.22, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (7.150e+19, 's^-1'),
            n = -2.32,
            Ea = (11.17, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 13,    
label = "FC(O)OH <=> CO2 + HF", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (3.950e+30, 's^-1'),
            n = -6.14,
            Ea = (35.43, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (7.460e+29, 's^-1'),
            n = -5.62,
            Ea = (36.45, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (5.250e+28, 's^-1'),
            n = -5.09,
            Ea = (36.91, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (6.160e+27, 's^-1'),
            n = -4.74,
            Ea = (36.9, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (6.470e+22, 's^-1'),
            n = -3.06,
            Ea = (35.82, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 14,    
label = "GenX <=> C2F5C(O)OH + C2F5CFO", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (4.990e+29, 's^-1'),
            n = -5.52,
            Ea = (83.14, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.070e+20, 's^-1'),
            n = -2.59,
            Ea = (80.07, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.020e+17, 's^-1'),
            n = -1.56,
            Ea = (78.96, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.130e+16, 's^-1'),
            n = -1.35,
            Ea = (78.72, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (4.000e+15, 's^-1'),
            n = -1.12,
            Ea = (78.48, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 15,    
label = "c_F2COC(O) <=> CF2 + CO2", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (1.080e+04, 's^-1'),
            n = 1.3,
            Ea = (20.51, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.730e+05, 's^-1'),
            n = 1.12,
            Ea = (18.85, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (4.930e+08, 's^-1'),
            n = 0.29,
            Ea = (17.95, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (5.870e+11, 's^-1'),
            n = -0.57,
            Ea = (18.14, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (3.060e+18, 's^-1'),
            n = -2.16,
            Ea = (19.37, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 16,    
label = "C2F5C(O)OH <=> CF2 + CF3C(O)OH", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (9.810e+56, 's^-1'),
            n = -14.81,
            Ea = (127.8, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (4.090e+54, 's^-1'),
            n = -13.42,
            Ea = (129.1, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.560e+47, 's^-1'),
            n = -10.88,
            Ea = (127.9, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.310e+43, 's^-1'),
            n = -9.52,
            Ea = (127.0, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.930e+28, 's^-1'),
            n = -4.71,
            Ea = (122.8, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 17,    
label = "C2F5CFO <=> CF2 + CF3CFO", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (4.740e+55, 's^-1'),
            n = -14.28,
            Ea = (127.4, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.300e+59, 's^-1'),
            n = -14.71,
            Ea = (131.5, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.580e+56, 's^-1'),
            n = -13.36,
            Ea = (132.2, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.930e+53, 's^-1'),
            n = -12.4,
            Ea = (131.8, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.810e+40, 's^-1'),
            n = -8.1,
            Ea = (128.1, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 18,    
label = "CF2CFO + CFO <=> CF3CFO + CO", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (4.250e+09, 'cm^3/(mol*s)'),
            n = 0.29,
            Ea = (14.73, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.000e+05, 'cm^3/(mol*s)'),
            n = 1.74,
            Ea = (14.85, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.210e-02, 'cm^3/(mol*s)'),
            n = 3.83,
            Ea = (13.44, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.660e-06, 'cm^3/(mol*s)'),
            n = 4.92,
            Ea = (12.52, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.110e-18, 'cm^3/(mol*s)'),
            n = 8.53,
            Ea = (9.06, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 19,    
label = "CF2 + O2 <=> CF2O + O", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(1.700000e+13, 'cm^3/(mol*s)'), n=0.0, Ea=(26.53, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 20,    
label = "CF2 + c_F2COC(O) <=> CF3-c_FCOC(O)", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(2.671640e+00, 'cm^3/(mol*s)'), n=3.355, Ea=(62.702, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 21,    
label = "CFO + CFO <=> CF2O + CO", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(2.230000e+13, 'cm^3/(mol*s)'), n=0.0, Ea=(0.318, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 22,    
label = "CF3 + O2 <=> CF3O + O", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (1.580e+18, 'cm^3/(mol*s)'),
            n = -1.38,
            Ea = (1.38, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.390e+19, 'cm^3/(mol*s)'),
            n = -1.69,
            Ea = (2.74, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (4.020e+18, 'cm^3/(mol*s)'),
            n = -1.42,
            Ea = (3.49, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (3.510e+17, 'cm^3/(mol*s)'),
            n = -1.09,
            Ea = (3.58, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.210e+11, 'cm^3/(mol*s)'),
            n = 0.84,
            Ea = (2.7, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 23,    
label = "CF3O + CO <=> CF3 + CO2", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(2.210000e+03, 'cm^3/(mol*s)'), n=2.56, Ea=(6.054, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 24,    
label = "CF3O <=> CF3 + O", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(4.020000e+17, 's^-1'), n=-0.71, Ea=(96.599, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 25,    
label = "CF3CFO <=> CF2CFO + F", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (1.810e+26, 's^-1'),
            n = -5.33,
            Ea = (124.8, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.460e+29, 's^-1'),
            n = -5.91,
            Ea = (121.4, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.670e+34, 's^-1'),
            n = -7.07,
            Ea = (121.2, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (4.260e+36, 's^-1'),
            n = -7.55,
            Ea = (121.7, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.010e+38, 's^-1'),
            n = -7.44,
            Ea = (123.1, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 26,    
label = "CF3 + O <=> CF2O + F", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (6.660e+12, 'cm^3/(mol*s)'),
            n = 0.17,
            Ea = (0.0, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (6.650e+12, 'cm^3/(mol*s)'),
            n = 0.17,
            Ea = (0.0, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (6.650e+12, 'cm^3/(mol*s)'),
            n = 0.17,
            Ea = (0.0, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (6.650e+12, 'cm^3/(mol*s)'),
            n = 0.17,
            Ea = (0.0, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (6.650e+12, 'cm^3/(mol*s)'),
            n = 0.17,
            Ea = (0.0, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 27,    
label = "CF3O <=> CF2O + F", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (9.120e+36, 's^-1'),
            n = -7.97,
            Ea = (33.25, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.810e+35, 's^-1'),
            n = -7.12,
            Ea = (33.83, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.090e+32, 's^-1'),
            n = -5.94,
            Ea = (33.52, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (9.230e+29, 's^-1'),
            n = -5.23,
            Ea = (33.08, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.180e+21, 's^-1'),
            n = -2.35,
            Ea = (30.45, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 28,    
label = "CO + F <=> CFO", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 0.215, 0.464, 1.0, 2.15, 4.64, 10.0, 21.5, 46.4, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (3.040e+18, 'cm^3/(mol*s)'),
            n = -3.05,
            Ea = (0.306, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (7.350e+18, 'cm^3/(mol*s)'),
            n = -3.07,
            Ea = (0.368, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.760e+19, 'cm^3/(mol*s)'),
            n = -3.08,
            Ea = (0.442, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (4.220e+19, 'cm^3/(mol*s)'),
            n = -3.09,
            Ea = (0.523, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (9.940e+19, 'cm^3/(mol*s)'),
            n = -3.1,
            Ea = (0.619, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (2.180e+20, 'cm^3/(mol*s)'),
            n = -3.1,
            Ea = (0.717, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (4.210e+20, 'cm^3/(mol*s)'),
            n = -3.09,
            Ea = (0.817, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (7.280e+20, 'cm^3/(mol*s)'),
            n = -3.06,
            Ea = (0.923, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.180e+21, 'cm^3/(mol*s)'),
            n = -3.02,
            Ea = (1.052, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.790e+21, 'cm^3/(mol*s)'),
            n = -2.98,
            Ea = (1.205, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 29,    
label = "CF2 + O <=> CFO + F", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(2.450000e+13, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 30,    
label = "CFO + F <=> CF2O", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(1.000000e+12, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 31,    
label = "CFO + O <=> CO2 + F", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(3.000000e+13, 'cm^3/(mol*s)'), n=0.0, Ea=(0.0, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 32,    
label = "CF3 <=> CF2 + F", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(3.129385e+20, 's^-1'), n=-1.3, Ea=(85.946, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 33,    
label = "C2F5CFO + OH <=> C2F5C(O)OH + F", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(1.320000e+02, 'cm^3/(mol*s)'), n=2.75, Ea=(28.483, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 34,    
label = "CF3CFO + OH <=> CF3C(O)OH + F", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(7.460000e+02, 'cm^3/(mol*s)'), n=2.55, Ea=(28.353000000000005, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 35,    
label = "FC(O)OH <=> CFO + OH", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (1.200e+37, 's^-1'),
            n = -10.46,
            Ea = (103.8, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.440e+36, 's^-1'),
            n = -10.09,
            Ea = (114.6, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (5.210e+35, 's^-1'),
            n = -9.89,
            Ea = (114.0, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.030e-13, 's^-1'),
            n = 3.41,
            Ea = (79.71, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (6.880e-90, 's^-1'),
            n = 25.4,
            Ea = (29.77, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 36,    
label = "CF3 + OH <=> CF2O + HF", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (6.830e+12, 'cm^3/(mol*s)'),
            n = 0.13,
            Ea = (0.03, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (6.840e+12, 'cm^3/(mol*s)'),
            n = 0.13,
            Ea = (0.03, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (6.830e+12, 'cm^3/(mol*s)'),
            n = 0.13,
            Ea = (0.03, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (6.830e+12, 'cm^3/(mol*s)'),
            n = 0.13,
            Ea = (0.03, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (6.800e+12, 'cm^3/(mol*s)'),
            n = 0.14,
            Ea = (0.03, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 37,    
label = "CFO + OH <=> CO2 + HF", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (6.000e+13, 'cm^3/(mol*s)'),
            n = 0.0,
            Ea = (0.225, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (6.000e+13, 'cm^3/(mol*s)'),
            n = 0.0,
            Ea = (0.225, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (6.000e+13, 'cm^3/(mol*s)'),
            n = 0.0,
            Ea = (0.225, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (5.990e+13, 'cm^3/(mol*s)'),
            n = 0.0,
            Ea = (0.225, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (5.540e+13, 'cm^3/(mol*s)'),
            n = 0.01,
            Ea = (0.203, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 38,    
label = "CF2 + OH <=> CFO + HF", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(5.390000e+10, 'cm^3/(mol*s)'), n=0.6, Ea=(-0.349, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 39,    
label = "F + H2O <=> HF + OH", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(1.300000e+08, 'cm^3/(mol*s)'), n=1.6, Ea=(-1.099, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 40,    
label = "F + OH <=> HF + O", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(1.400000e+12, 'cm^3/(mol*s)'), n=0.5, Ea=(0.0, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 41,    
label = "CF3O + H <=> CF2O + HF", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (3.340e+13, 'cm^3/(mol*s)'),
            n = 0.1,
            Ea = (0.07, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (3.330e+13, 'cm^3/(mol*s)'),
            n = 0.1,
            Ea = (0.07, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (3.340e+13, 'cm^3/(mol*s)'),
            n = 0.1,
            Ea = (0.07, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (3.340e+13, 'cm^3/(mol*s)'),
            n = 0.1,
            Ea = (0.07, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (3.320e+13, 'cm^3/(mol*s)'),
            n = 0.1,
            Ea = (0.07, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 42,    
label = "CF3 + H <=> CF2 + HF", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 1.0, 5.0, 10.0, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (9.880e+13, 'cm^3/(mol*s)'),
            n = 0.03,
            Ea = (0.136, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (9.880e+13, 'cm^3/(mol*s)'),
            n = 0.03,
            Ea = (0.136, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (9.870e+13, 'cm^3/(mol*s)'),
            n = 0.03,
            Ea = (0.136, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (9.850e+13, 'cm^3/(mol*s)'),
            n = 0.03,
            Ea = (0.135, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.100e+14, 'cm^3/(mol*s)'),
            n = 0.02,
            Ea = (0.316, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 43,    
label = "CF2O + H <=> CFO + HF", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 0.215, 0.464, 1.0, 2.15, 4.64, 10.0, 21.5, 46.4, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (1.590e+11, 'cm^3/(mol*s)'),
            n = 0.76,
            Ea = (25.526, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.590e+11, 'cm^3/(mol*s)'),
            n = 0.76,
            Ea = (25.526, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.590e+11, 'cm^3/(mol*s)'),
            n = 0.76,
            Ea = (25.526, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.590e+11, 'cm^3/(mol*s)'),
            n = 0.76,
            Ea = (25.526, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.590e+11, 'cm^3/(mol*s)'),
            n = 0.76,
            Ea = (25.526, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.590e+11, 'cm^3/(mol*s)'),
            n = 0.76,
            Ea = (25.526, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.590e+11, 'cm^3/(mol*s)'),
            n = 0.76,
            Ea = (25.526, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.590e+11, 'cm^3/(mol*s)'),
            n = 0.76,
            Ea = (25.526, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.590e+11, 'cm^3/(mol*s)'),
            n = 0.76,
            Ea = (25.526, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.590e+11, 'cm^3/(mol*s)'),
            n = 0.76,
            Ea = (25.526, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 44,    
label = "CFO + H <=> CO + HF", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(6.140000e+13, 'cm^3/(mol*s)'), n=0.04, Ea=(0.155, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 45,    
label = "CF2 + OH <=> CF2O + H", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(5.620000e+13, 'cm^3/(mol*s)'), n=-0.16, Ea=(0.17, 'kcal/mol'), T0=(1,'K')),
)



entry(
    index=46,
    label="HF <=> F + H ",
    kinetics=ThirdBody(
        arrheniusLow=Arrhenius(A=(4.708000e+18, 'cm^3/(mol*s)'), n=-1.0, Ea=(134.082, 'kcal/mol'), T0=(1, 'K'))),
)

entry(
index = 47,    
label = "CF2 + HO2 <=> CF2O + OH", 
degeneracy = 1.0, 
kinetics = PDepArrhenius(
    pressures = ([0.1, 0.215, 0.464, 1.0, 2.15, 4.64, 10.0, 21.5, 46.4, 100.0], 'atm'),
    arrhenius = [

        Arrhenius(
            A = (7.080e-13, 'cm^3/(mol*s)'),
            n = 6.21,
            Ea = (-3.234, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (7.090e-13, 'cm^3/(mol*s)'),
            n = 6.21,
            Ea = (-3.234, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (7.090e-13, 'cm^3/(mol*s)'),
            n = 6.21,
            Ea = (-3.231, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (7.110e-13, 'cm^3/(mol*s)'),
            n = 6.21,
            Ea = (-3.231, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (7.150e-13, 'cm^3/(mol*s)'),
            n = 6.21,
            Ea = (-3.229, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (7.230e-13, 'cm^3/(mol*s)'),
            n = 6.21,
            Ea = (-3.224, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (7.420e-13, 'cm^3/(mol*s)'),
            n = 6.21,
            Ea = (-3.215, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (7.840e-13, 'cm^3/(mol*s)'),
            n = 6.2,
            Ea = (-3.196, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (8.850e-13, 'cm^3/(mol*s)'),
            n = 6.18,
            Ea = (-3.148, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

        Arrhenius(
            A = (1.160e-12, 'cm^3/(mol*s)'),
            n = 6.15,
            Ea = (-3.045, 'kcal/mol'),
            T0 = (1, 'K'),
    ),

    ],
),
)

entry(
index = 48,    
label = "F + HO2 <=> HF + O2", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(2.900000e+12, 'cm^3/(mol*s)'), n=0.5, Ea=(0.0, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 49,    
label = "F + H2O2 <=> HF + HO2", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(1.730000e+12, 'cm^3/(mol*s)'), n=0.5, Ea=(0.0, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 50,    
label = "CFO + O2 <=> CO + FO2", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(1.003666e+13, 'cm^3/(mol*s)'), n=0.144, Ea=(23.466, 'kcal/mol'), T0=(1,'K')),
)



entry(
index = 51,    
label = "F + O2 <=> FO2", 
degeneracy = 1.0, 
kinetics = Arrhenius(A=(1.822714e+10, 'cm^3/(mol*s)'), n=0.726, Ea=(0.0, 'kcal/mol'), T0=(1,'K')),
)


