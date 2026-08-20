#!/usr/bin/env python
# encoding: utf-8


name = "GenX"
shortDesc = "thermo library for GenX thermal treatment (Rocchio & Goldsmith 2025)"
longDesc = """
Caroline L. Rocchio, Kurt D. Pennell, C. Franklin Goldsmith; Computational Investigation of the Reaction Mechanism for the Thermal Treatment of Hexafluoropropylene Oxide Dimer Acid (GenX). J. Phys. Chem. A 19 June 2025; 129 (24): 5343–5358. https://doi.org/10.1021/acs.jpca.5c01170

Obtained from: https://pubs.acs.org/jpcafh/article-abstract/129/24/5343/3647996/Computational-Investigation-of-the-Reaction?redirectedFrom=fulltext

This library contains thermo for species involved in GenX (Hexafluoropropylene Oxide Dimer Acid) thermal treatment, including a perfluoro alpha-lactone ether, C3-C2 perfluoroaldehydes, perfluoroester, perfluorocarboxylic acids, perfluoro alpha-lactones, perfluorinated radicals, and a perfluorinated singlet carbene (CF2). 

It is recommended for GenX degradation mechanisms. 
"""

entry(
    index = 0,
    label = "Ar",
    molecule = 
"""
1 Ar u0 p4 c0

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5, 4.30732087e-14, -5.2891251e-17, 2.10457488e-20, -2.57139738e-24, -745.0, 4.36630363], Tmin=(100.0,'K'), Tmax=(4996.86,'K')),
            NASAPolynomial(coeffs=[-48.6862231, 0.0190728012, 8.49269033e-07, -9.90485659e-10, 9.34419177e-14, 77752.0762, 361.019322], Tmin=(4996.86,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = 'Thermo library: BurkeH2O2',
    referenceType = "Theory",
)


entry(
    index = 1,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61262639, -0.0010089351, 2.49899677e-06, -1.43376603e-09, 2.58638299e-13, -1051.10291, 2.65270163], Tmin=(100.0,'K'), Tmax=(1817.02,'K')),
            NASAPolynomial(coeffs=[2.97586378, 0.00164146126, -7.19746362e-07, 1.25382687e-10, -7.9156364e-15, -1025.82202, 5.53779188], Tmin=(1817.02,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = 'Thermo library: BurkeH2O2',
    referenceType = "Theory",
)


entry(
    index = 2,
    label = "Ne",
    molecule = 
"""
1 Ne u0 p4 c0

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5, 0.0, 0.0, 0.0, 0.0, -745.375, 3.35532], Tmin=(200.0,'K'), Tmax=(6000.0,'K')),
            NASAPolynomial(coeffs=[2.5, 0.0, 0.0, 0.0, 0.0, -745.375, 3.35532], Tmin=(6000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'Thermo library: primaryThermoLibrary',
    referenceType = "Theory",
)


entry(
    index = 3,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53763815, -0.00122828996, 5.36763616e-06, -4.93134247e-09, 1.45957569e-12, -1037.99031, 4.67179344], Tmin=(100.0,'K'), Tmax=(1087.7,'K')),
            NASAPolynomial(coeffs=[3.16426522, 0.00169454876, -8.00342202e-07, 1.59031564e-10, -1.14892257e-14, -1048.44232, 6.08307006], Tmin=(1087.7,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = 'Thermo library: BurkeH2O2',
    referenceType = "Theory",
)


entry(
    index = 4,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99881979, -0.000554829156, 2.76773769e-06, -1.55664565e-09, 3.02329219e-13, -30274.5569, -0.0308934271], Tmin=(100.0,'K'), Tmax=(1281.45,'K')),
            NASAPolynomial(coeffs=[3.19560188, 0.00195240322, -1.6712008e-07, -2.97934039e-11, 4.45135462e-15, -30068.7015, 4.04335519], Tmin=(1281.45,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = 'Thermo library: BurkeH2O2',
    referenceType = "Theory",
)


entry(
    index = 5,
    label = "CO2",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.27790408, 0.00275780553, 7.12794156e-06, -1.07855513e-08, 4.1423182e-12, -48475.6032, 5.97855262], Tmin=(100.0,'K'), Tmax=(988.18,'K')),
            NASAPolynomial(coeffs=[4.55070635, 0.00290729332, -1.14643705e-06, 2.25799154e-10, -1.69527436e-14, -48986.0066, -1.45658492], Tmin=(988.18,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = 'Thermo library: BurkeH2O2',
    referenceType = "Theory",
)


entry(
    index = 6,
    label = "CO",
    molecule = 
"""
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59709639, -0.00102423527, 2.83335709e-06, -1.75824624e-09, 3.4258537e-13, -14343.1899, 3.45822277], Tmin=(100.0,'K'), Tmax=(1669.94,'K')),
            NASAPolynomial(coeffs=[2.9279682, 0.00181928966, -8.35300151e-07, 1.5126742e-10, -9.88858948e-15, -14292.7149, 6.5114997], Tmin=(1669.94,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = 'Thermo library: BurkeH2O2',
    referenceType = "Theory",
)


entry(
    index = 7,
    label = "HF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 H u0 p0 c0 {1,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47861056, 0.000230210129, -7.26207054e-07, 8.90789862e-10, -2.44257848e-13, -33844.0904, 1.03719885], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[2.92408264, 0.00085227914, -1.60115398e-07, 1.31455482e-11, -2.46281644e-16, -33618.6854, 4.19417238], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = 'Thermo library: C1_C2_Fluorine',
    referenceType = "Theory",
)


entry(
    index = 8,
    label = "F",
    molecule = 
"""
multiplicity 2
1 F u1 p3 c0

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.4193242, 0.00293848449, -8.91441625e-06, 9.90063549e-09, -3.78936967e-12, 8998.3259, 4.73388583], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[2.73547309, -0.000318376264, 1.80404747e-07, -4.76650983e-11, 4.82178946e-15, 9007.23724, 3.62700929], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = 'Thermo library: C1_C2_Fluorine',
    referenceType = "Theory",
)


entry(
    index = 9,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48578967, 0.00133404082, -4.70069034e-06, 5.64412829e-09, -2.0633202e-12, 3411.95729, 1.99789881], Tmin=(100.0,'K'), Tmax=(1005.23,'K')),
            NASAPolynomial(coeffs=[2.88227829, 0.00103864428, -2.35626827e-07, 1.40170436e-11, 6.35069671e-16, 3669.54919, 5.59038746], Tmin=(1005.23,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = 'Thermo library: BurkeH2O2',
    referenceType = "Theory",
)


entry(
    index = 10,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5, 4.30732087e-14, -5.2891251e-17, 2.10457488e-20, -2.57139738e-24, 25472.7081, -0.459566246], Tmin=(100.0,'K'), Tmax=(4996.86,'K')),
            NASAPolynomial(coeffs=[-48.6862231, 0.0190728012, 8.49269033e-07, -9.90485659e-10, 9.34419177e-14, 103969.784, 356.193452], Tmin=(4996.86,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = 'Thermo library: BurkeH2O2',
    referenceType = "Theory",
)


entry(
    index = 11,
    label = "O",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5, 4.30732087e-14, -5.2891251e-17, 2.10457488e-20, -2.57139738e-24, 29226.7216, 5.1110677], Tmin=(100.0,'K'), Tmax=(4996.86,'K')),
            NASAPolynomial(coeffs=[-48.6862231, 0.0190728012, 8.49269033e-07, -9.90485659e-10, 9.34419177e-14, 107723.798, 361.764086], Tmin=(4996.86,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = 'Thermo library: BurkeH2O2',
    referenceType = "Theory",
)


entry(
    index = 12,
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.02957457, -0.0026400329, 1.52237058e-05, -1.71680814e-08, 6.26781469e-12, 322.676656, 4.84422794], Tmin=(100.0,'K'), Tmax=(923.9,'K')),
            NASAPolynomial(coeffs=[4.15128932, 0.00191153557, -4.11318445e-07, 6.3506292e-11, -4.86473582e-15, 83.4383072, 3.09364933], Tmin=(923.9,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = 'Thermo library: BurkeH2O2',
    referenceType = "Theory",
)


entry(
    index = 13,
    label = "H2O2",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72867176, 0.00413375413, 5.67504918e-06, -1.01866712e-08, 4.286169e-12, -17696.396, 5.35910987], Tmin=(100.0,'K'), Tmax=(923.27,'K')),
            NASAPolynomial(coeffs=[4.95151361, 0.00354230547, -1.01041145e-06, 1.61942965e-10, -1.1021038e-14, -18122.7923, -1.52909488], Tmin=(923.27,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = 'Thermo library: BurkeH2O2',
    referenceType = "Theory",
)


entry(
    index = 14,
    label = "FO2",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 F u0 p3 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.09573104, 0.0113826157, -1.7233058e-05, 1.38769848e-08, -4.52972342e-12, 1495.69342, 10.7381197], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.09030167, 0.00270913318, -1.59858244e-06, 4.37280609e-10, -4.55829164e-14, 1089.47013, 1.17522481], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = 'Thermo library: C1_C2_Fluorine',
    referenceType = "Theory",
)


entry(
    index = 15,
    label = "GenX",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {21,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {17,S}
5  F u0 p3 c0 {4,S}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 F u0 p3 c0 {13,S}
17 C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
18 F u0 p3 c0 {17,S}
19 F u0 p3 c0 {17,S}
20 F u0 p3 c0 {17,S}
21 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.88999965, 0.136820589, -0.000124121094, 2.77388986e-08, 9.38555607e-12, -355987.026, 10.9636838], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[36.6682419, 0.0322299144, -1.69748299e-05, 2.6659657e-09, 1.24657209e-13, -363064.939, -146.862225], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = 'Thermo library: Abeywardane_Goldsmith_PFAS',
    referenceType = "Theory",
)


entry(
    index = 16,
    label = "C3F7OC(CF3)OCO",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {16,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 F u0 p3 c0 {12,S}
16 C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 F u0 p3 c0 {16,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.03353843, 0.153196799, -0.000200578715, 1.27712779e-07, -3.20899329e-11, -303410.417, 28.9283905], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[34.0750842, 0.0278927383, -1.68617898e-05, 4.6547325e-09, -4.86295876e-13, -310595.123, -132.750483], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = 'Thermo library: GenX_thermo',
    referenceType = "Theory",
)


entry(
    index = 17,
    label = "C3F7OC(O)CF3",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {14,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 F u0 p3 c0 {10,S}
14 C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
15 F u0 p3 c0 {14,S}
16 F u0 p3 c0 {14,S}
17 F u0 p3 c0 {14,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73679111, 0.116981322, -0.00013639976, 7.77834835e-08, -1.79573812e-11, -303341.534, 18.0799567], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[29.9863394, 0.0270195735, -1.73064672e-05, 4.9822402e-09, -5.37230787e-13, -309591.691, -112.918353], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = 'Thermo library: GenX_thermo',
    referenceType = "Theory",
)


entry(
    index = 18,
    label = "C2F5CFO",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 F u0 p3 c0 {7,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.36994, 0.0682513, -0.000108793, 9.95316e-08, -3.84993e-11, -176437.0, 13.9257], Tmin=(10.0,'K'), Tmax=(605.78,'K')),
            NASAPolynomial(coeffs=[8.40417, 0.0350098, -2.64819e-05, 8.94648e-09, -1.11532e-12, -177047.0, -7.83814], Tmin=(605.78,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (10.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = 'Thermo library: CHOF_G4',
    referenceType = "Theory",
)


entry(
    index = 19,
    label = "CF3CFO",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 F u0 p3 c0 {4,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1326305, 0.0328571031, -2.83102366e-05, 8.88924879e-09, 1.10706912e-13, -124882.17, 13.8855197], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[10.0949054, 0.0118266899, -6.9325105e-06, 1.88610627e-09, -1.95738381e-13, -126643.072, -21.4556292], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = 'Thermo library: C1_C2_Fluorine',
    referenceType = "Theory",
)


entry(
    index = 20,
    label = "CF2O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.21606409, 0.013238051, -4.23784631e-06, -6.67863953e-09, 4.37910484e-12, -74160.5798, 14.772971], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.20117804, 0.00661606316, -3.82471522e-06, 1.0303664e-09, -1.06158338e-13, -75002.6091, -0.880396197], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = 'Thermo library: C1_C2_Fluorine',
    referenceType = "Theory",
)


entry(
    index = 21,
    label = "C2F5C(O)OH",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {11,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 F u0 p3 c0 {7,S}
11 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.200950982, 0.0748973361, -7.98183007e-05, 3.6453052e-08, -4.79392345e-12, -176554.313, 28.2351243], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[16.9328776, 0.0180874443, -1.07004707e-05, 2.92324439e-09, -3.03980537e-13, -180436.107, -55.0398361], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = 'Thermo library: Abeywardane_Goldsmith_PFAS',
    referenceType = "Theory",
)


entry(
    index = 22,
    label = "CF3C(O)OH",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {8,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 F u0 p3 c0 {4,S}
8 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.0435424, 0.0304394678, 1.70910981e-06, -3.26143026e-08, 1.73541771e-11, -125687.346, 19.5016045], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[10.3983389, 0.0155451203, -9.30450851e-06, 2.56055653e-09, -2.67512617e-13, -128193.14, -25.1296592], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = 'Thermo library: Abeywardane_Goldsmith_PFAS',
    referenceType = "Theory",
)


entry(
    index = 23,
    label = "FC(O)OH",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {5,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {3,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96655, 0.00185137, 4.47909e-05, -7.96564e-08, 4.23622e-11, -75247.4, 7.80392], Tmin=(10.0,'K'), Tmax=(614.34,'K')),
            NASAPolynomial(coeffs=[2.83475, 0.0173246, -1.27762e-05, 4.2862e-09, -5.35304e-13, -75261.2, 11.4681], Tmin=(614.34,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (10.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = 'Thermo library: CHOF_G4',
    referenceType = "Theory",
)


entry(
    index = 24,
    label = "CF3-c_FCOC(O)",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7 F u0 p3 c0 {6,S}
8 F u0 p3 c0 {6,S}
9 F u0 p3 c0 {6,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.30416192, 0.0615380588, -7.46510167e-05, 4.47854935e-08, -1.0695366e-11, -124631.611, 21.2721701], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[14.0808752, 0.01478695, -8.72265657e-06, 2.38455794e-09, -2.48394986e-13, -127498.05, -41.6774073], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = 'Thermo library: PFCA_regen',
    referenceType = "Theory",
)


entry(
    index = 25,
    label = "c_F2COC(O)",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91016, 0.00539278, 7.97343e-05, -1.73137e-07, 1.08322e-10, -71590.6, 9.98725], Tmin=(10.0,'K'), Tmax=(556.58,'K')),
            NASAPolynomial(coeffs=[4.52605, 0.0208631, -1.55805e-05, 5.25783e-09, -6.57826e-13, -71967.3, 4.60833], Tmin=(556.58,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (10.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = 'Thermo library: CHOF_G4',
    referenceType = "Theory",
)


entry(
    index = 26,
    label = "CF2CFO",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63301884, 0.0279611995, -2.99996935e-05, 1.69928295e-08, -4.13170259e-12, -75336.2003, 12.5018934], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[8.92401195, 0.00992185214, -5.80362067e-06, 1.57692944e-09, -1.63521017e-13, -76612.5386, -13.9590933], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = 'Thermo library: C1_C2_Fluorine',
    referenceType = "Theory",
)


entry(
    index = 27,
    label = "CF3O",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 F u0 p3 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.79814049, 0.0255607305, -2.18881631e-05, 5.3104816e-09, 1.14830319e-12, -77056.9173, 16.9982065], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[7.78726745, 0.0075152445, -4.47481513e-06, 1.23045799e-09, -1.28662165e-13, -78552.3516, -13.3551556], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = 'Thermo library: C1_C2_Fluorine',
    referenceType = "Theory",
)


entry(
    index = 28,
    label = "CFO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 F u0 p3 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44442764, 0.00358299017, 3.3175635e-06, -7.17713557e-09, 3.14601149e-12, -22557.6575, 9.13877709], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[4.06597351, 0.00397110832, -2.26619886e-06, 6.0487021e-10, -6.18959515e-14, -22815.9283, 5.45702826], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = 'Thermo library: C1_C2_Fluorine',
    referenceType = "Theory",
)


entry(
    index = 29,
    label = "CF3",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.46154028, 0.012950989, -2.16596832e-06, -9.8060505e-09, 5.70993719e-12, -57563.5077, 14.0623986], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.91197113, 0.00585949131, -3.47369564e-06, 9.51960392e-10, -9.9279589e-14, -58559.94, -4.16067146], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = 'Thermo library: C1_C2_Fluorine',
    referenceType = "Theory",
)


entry(
    index = 30,
    label = "CF2",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {2,S}
2 C u2 p0 c0 {1,S} {3,S}
3 F u0 p3 c0 {2,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65163442, 0.000518866653, 1.52247353e-05, -2.21767603e-08, 9.27643387e-12, -24486.645, 7.48151723], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[4.59662945, 0.00342444206, -2.0202923e-06, 5.51455076e-10, -5.73243175e-14, -24951.3874, 1.42802895], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = 'Thermo library: C1_C2_Fluorine',
    referenceType = "Theory",
)
