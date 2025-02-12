#!/usr/bin/env python
# encoding: utf-8

name = "F_Abstraction/rules"
shortDesc = ""
longDesc = """
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')


.. [MRHCBSQB3RRHO] M.R. Harper (mrharper_at_mit_dot_edu or michael.harper.jr_at_gmail_dot_com)
The geometries of all reactants, products, and the transition state were optimized using the CBS-QB3 calculations.  The zero-point
energy is that computed by the CBS-QB3 calculations.  The frequencies were computed with B3LYP/CBSB7.
In computing k(T), an asymmetric tunneling correction was employed, the calculated frequencies were scaled by 0.99, and the
temperatures used were: 300, 331, 370, 419, 482, 568, 692, 885, 1227, 2000 (evenly spaced on inverse temperature scale).

.. [Tsang1990] W. Tsang; "Chemical kinetic database for combustion chemistry. Part IV. Isobutane" J. Phys. Chem. Ref. Data 19 (1990) 1-68

.. [Tsang1991] W. Tsang; "Chemical kinetic database for combustion chemistry. Part V. Propene" J. Phys. Chem. Ref. Data 20 (1991) 221-273
"""
entry(
    index = 1,
    label = "Root",
    kinetics = Arrhenius(A=(2.25152e-05,'m^3/(mol*s)'), n=3.50774, Ea=(172.559,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.5748623854914848, var=161.15070570425195, Tref=1000.0, N=242, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 242 training reactions at node Root
    Total Standard Deviation in ln(k): 26.89351693911438"""),
    rank = 11,
    shortDesc = """BM rule fitted to 242 training reactions at node Root
Total Standard Deviation in ln(k): 26.89351693911438""",
    longDesc = 
"""
BM rule fitted to 242 training reactions at node Root
Total Standard Deviation in ln(k): 26.89351693911438
""",
)

entry(
    index = 2,
    label = "Root_1R->O",
    kinetics = ArrheniusBM(A=(1.73627e-08,'m^3/(mol*s)'), n=4.3161, w0=(337.688,'kJ/mol'), E0=(90.7442,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23610443096910189, var=5.666706571291651, Tref=1000.0, N=64, data_mean=0.0, correlation='Root_1R->O',), comment="""BM rule fitted to 64 training reactions at node Root_1R->O
    Total Standard Deviation in ln(k): 5.365468040910369"""),
    rank = 11,
    shortDesc = """BM rule fitted to 64 training reactions at node Root_1R->O
Total Standard Deviation in ln(k): 5.365468040910369""",
    longDesc = 
"""
BM rule fitted to 64 training reactions at node Root_1R->O
Total Standard Deviation in ln(k): 5.365468040910369
""",
)

entry(
    index = 3,
    label = "Root_N-1R->O",
    kinetics = Arrhenius(A=(6.70662e-06,'m^3/(mol*s)'), n=3.68067, Ea=(222.922,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.7370252660678116, var=109.7793048847225, Tref=1000.0, N=178, data_mean=0.0, correlation='Root_N-1R->O',), comment="""BM rule fitted to 178 training reactions at node Root_N-1R->O
    Total Standard Deviation in ln(k): 25.369121102191077"""),
    rank = 11,
    shortDesc = """BM rule fitted to 178 training reactions at node Root_N-1R->O
Total Standard Deviation in ln(k): 25.369121102191077""",
    longDesc = 
"""
BM rule fitted to 178 training reactions at node Root_N-1R->O
Total Standard Deviation in ln(k): 25.369121102191077
""",
)

entry(
    index = 4,
    label = "Root_1R->O_3R->O",
    kinetics = ArrheniusBM(A=(0.00307126,'m^3/(mol*s)'), n=3.25289, w0=(222,'kJ/mol'), E0=(115.574,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03761016185453279, var=0.6021141240354595, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_3R->O',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
    Total Standard Deviation in ln(k): 1.6500923862631345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
Total Standard Deviation in ln(k): 1.6500923862631345""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_3R->O
Total Standard Deviation in ln(k): 1.6500923862631345
""",
)

entry(
    index = 5,
    label = "Root_1R->O_N-3R->O",
    kinetics = ArrheniusBM(A=(47405.9,'m^3/(mol*s)'), n=0.687846, w0=(354.214,'kJ/mol'), E0=(142.706,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.20423146785167035, var=4.909941979595041, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_1R->O_N-3R->O',), comment="""BM rule fitted to 56 training reactions at node Root_1R->O_N-3R->O
    Total Standard Deviation in ln(k): 4.955314337129389"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_1R->O_N-3R->O
Total Standard Deviation in ln(k): 4.955314337129389""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_1R->O_N-3R->O
Total Standard Deviation in ln(k): 4.955314337129389
""",
)

entry(
    index = 6,
    label = "Root_N-1R->O_3R->O",
    kinetics = ArrheniusBM(A=(1.07897e-08,'m^3/(mol*s)'), n=4.6493, w0=(354.214,'kJ/mol'), E0=(76.8866,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.25670297575742307, var=5.2825473347558445, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_N-1R->O_3R->O',), comment="""BM rule fitted to 56 training reactions at node Root_N-1R->O_3R->O
    Total Standard Deviation in ln(k): 5.252623923653388"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_N-1R->O_3R->O
Total Standard Deviation in ln(k): 5.252623923653388""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_N-1R->O_3R->O
Total Standard Deviation in ln(k): 5.252623923653388
""",
)

entry(
    index = 7,
    label = "Root_N-1R->O_N-3R->O",
    kinetics = ArrheniusBM(A=(4.69923e+18,'m^3/(mol*s)'), n=-3.32677, w0=(479.308,'kJ/mol'), E0=(227.108,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6972086991031786, var=12.189859256918252, Tref=1000.0, N=122, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O',), comment="""BM rule fitted to 122 training reactions at node Root_N-1R->O_N-3R->O
    Total Standard Deviation in ln(k): 8.751108479027286"""),
    rank = 11,
    shortDesc = """BM rule fitted to 122 training reactions at node Root_N-1R->O_N-3R->O
Total Standard Deviation in ln(k): 8.751108479027286""",
    longDesc = 
"""
BM rule fitted to 122 training reactions at node Root_N-1R->O_N-3R->O
Total Standard Deviation in ln(k): 8.751108479027286
""",
)

entry(
    index = 8,
    label = "Root_1R->O_3R->O_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.0549438,'m^3/(mol*s)'), n=2.89629, w0=(222,'kJ/mol'), E0=(116.204,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1862381689223558, var=5.707928743481837, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
    Total Standard Deviation in ln(k): 7.770064999671787"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
Total Standard Deviation in ln(k): 7.770064999671787""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_3R->O_Ext-1O-R
Total Standard Deviation in ln(k): 7.770064999671787
""",
)

entry(
    index = 9,
    label = "Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(3.88038e-05,'m^3/(mol*s)'), n=3.96851, w0=(222,'kJ/mol'), E0=(70.7103,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-3O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_1R->O_3R->O_1O-u0",
    kinetics = ArrheniusBM(A=(1.72685e-05,'m^3/(mol*s)'), n=3.8992, w0=(222,'kJ/mol'), E0=(112.651,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_1O-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_1O-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_1O-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_1R->O_3R->O_N-1O-u0",
    kinetics = ArrheniusBM(A=(0.198965,'m^3/(mol*s)'), n=2.25903, w0=(222,'kJ/mol'), E0=(120.696,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.31081505617103056, var=1.141349567679458, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
    Total Standard Deviation in ln(k): 2.922680285507011"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
Total Standard Deviation in ln(k): 2.922680285507011""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_N-1O-u0
Total Standard Deviation in ln(k): 2.922680285507011
""",
)

entry(
    index = 12,
    label = "Root_1R->O_N-3R->O_1O-u0",
    kinetics = ArrheniusBM(A=(109.525,'m^3/(mol*s)'), n=1.45616, w0=(354.37,'kJ/mol'), E0=(125.848,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15270405341566873, var=3.1500120322536502, Tref=1000.0, N=46, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0',), comment="""BM rule fitted to 46 training reactions at node Root_1R->O_N-3R->O_1O-u0
    Total Standard Deviation in ln(k): 3.941737120173576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 46 training reactions at node Root_1R->O_N-3R->O_1O-u0
Total Standard Deviation in ln(k): 3.941737120173576""",
    longDesc = 
"""
BM rule fitted to 46 training reactions at node Root_1R->O_N-3R->O_1O-u0
Total Standard Deviation in ln(k): 3.941737120173576
""",
)

entry(
    index = 13,
    label = "Root_1R->O_N-3R->O_N-1O-u0",
    kinetics = Arrhenius(A=(0.00302672,'m^3/(mol*s)'), n=2.63652, Ea=(41.4496,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-0.9603078257217335, var=8.581094336445169, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0',), comment="""BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_N-1O-u0
    Total Standard Deviation in ln(k): 8.2854054290299"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_N-1O-u0
Total Standard Deviation in ln(k): 8.2854054290299""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_N-1O-u0
Total Standard Deviation in ln(k): 8.2854054290299
""",
)

entry(
    index = 14,
    label = "Root_N-1R->O_3R->O_Ext-3O-R",
    kinetics = ArrheniusBM(A=(7.7204e-09,'m^3/(mol*s)'), n=4.6122, w0=(355.318,'kJ/mol'), E0=(67.3881,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5043728803223331, var=2.3409702276540245, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
    Total Standard Deviation in ln(k): 4.334559220689914"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 4.334559220689914""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R
Total Standard Deviation in ln(k): 4.334559220689914
""",
)

entry(
    index = 15,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(1.2647,'m^3/(mol*s)'), n=2.47382, w0=(353.5,'kJ/mol'), E0=(114.411,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12672790686968555, var=11.655300414690176, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 7.162549316144963"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 7.162549316144963""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 7.162549316144963
""",
)

entry(
    index = 16,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(6.22075e+09,'m^3/(mol*s)'), n=-0.495315, w0=(353.5,'kJ/mol'), E0=(172.152,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9514000486668078, var=7.72059187809254, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 7.960799860692724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 7.960799860692724""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 7.960799860692724
""",
)

entry(
    index = 17,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F",
    kinetics = ArrheniusBM(A=(0.22677,'m^3/(mol*s)'), n=2.32228, w0=(326.667,'kJ/mol'), E0=(102.334,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18793572344502307, var=1.3698943409224622, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F
    Total Standard Deviation in ln(k): 2.818592072196614"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 2.818592072196614""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 2.818592072196614
""",
)

entry(
    index = 18,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F",
    kinetics = ArrheniusBM(A=(5.55471e+12,'m^3/(mol*s)'), n=-1.63065, w0=(487.203,'kJ/mol'), E0=(213.839,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5446126964690786, var=11.926723329519996, Tref=1000.0, N=116, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F',), comment="""BM rule fitted to 116 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F
    Total Standard Deviation in ln(k): 8.29174392711576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 116 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 8.29174392711576""",
    longDesc = 
"""
BM rule fitted to 116 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F
Total Standard Deviation in ln(k): 8.29174392711576
""",
)

entry(
    index = 19,
    label = "Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(0.0487535,'m^3/(mol*s)'), n=3.06244, w0=(222,'kJ/mol'), E0=(73.6796,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_1R->O_3R->O_Ext-1O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.00501001,'m^3/(mol*s)'), n=3.19468, w0=(222,'kJ/mol'), E0=(113.816,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3116729497350754, var=4.9816223982621395, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 7.770138832350752"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 7.770138832350752""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 7.770138832350752
""",
)

entry(
    index = 21,
    label = "Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0779944,'m^3/(mol*s)'), n=2.62416, w0=(222,'kJ/mol'), E0=(110.956,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.0730252,'m^3/(mol*s)'), n=2.39118, w0=(222,'kJ/mol'), E0=(123.094,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.00111026,'m^3/(mol*s)'), n=2.89721, w0=(222,'kJ/mol'), E0=(111.276,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_N-1O-u0_Ext-3O-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1",
    kinetics = ArrheniusBM(A=(406.971,'m^3/(mol*s)'), n=1.27384, w0=(354.611,'kJ/mol'), E0=(126.452,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12337915491397056, var=4.075617990927758, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1',), comment="""BM rule fitted to 36 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1
    Total Standard Deviation in ln(k): 4.35718910138627"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1
Total Standard Deviation in ln(k): 4.35718910138627""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1
Total Standard Deviation in ln(k): 4.35718910138627
""",
)

entry(
    index = 25,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1",
    kinetics = ArrheniusBM(A=(1.18901e-06,'m^3/(mol*s)'), n=3.82331, w0=(353.5,'kJ/mol'), E0=(67.7625,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.021250960384210114, var=1.160438535339773, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1',), comment="""BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1
    Total Standard Deviation in ln(k): 2.212968225372079"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1
Total Standard Deviation in ln(k): 2.212968225372079""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1
Total Standard Deviation in ln(k): 2.212968225372079
""",
)

entry(
    index = 26,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R",
    kinetics = Arrhenius(A=(0.00378399,'m^3/(mol*s)'), n=2.59346, Ea=(43.4203,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.0506922609414964, var=16.835551477486465, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 10.865588571514216"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R
Total Standard Deviation in ln(k): 10.865588571514216""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R
Total Standard Deviation in ln(k): 10.865588571514216
""",
)

entry(
    index = 27,
    label = "Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1",
    kinetics = ArrheniusBM(A=(0.00154,'m^3/(mol*s)'), n=2.64, w0=(353.5,'kJ/mol'), E0=(109.457,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1",
    kinetics = ArrheniusBM(A=(0.000996795,'m^3/(mol*s)'), n=2.97758, w0=(353.5,'kJ/mol'), E0=(143.459,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_N-3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O",
    kinetics = ArrheniusBM(A=(8.23395e-08,'m^3/(mol*s)'), n=4.30203, w0=(353.5,'kJ/mol'), E0=(55.6862,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5329381125750059, var=7.210902680481687, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O
    Total Standard Deviation in ln(k): 6.722380443990002"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O
Total Standard Deviation in ln(k): 6.722380443990002""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O
Total Standard Deviation in ln(k): 6.722380443990002
""",
)

entry(
    index = 30,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(3.75604e-09,'m^3/(mol*s)'), n=4.73935, w0=(357.136,'kJ/mol'), E0=(83.1722,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3067210424071087, var=3.5288716280406187, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O
    Total Standard Deviation in ln(k): 4.536609091996524"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O
Total Standard Deviation in ln(k): 4.536609091996524""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O
Total Standard Deviation in ln(k): 4.536609091996524
""",
)

entry(
    index = 31,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.921807,'m^3/(mol*s)'), n=2.51063, w0=(353.5,'kJ/mol'), E0=(113.555,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14762088125318962, var=12.843703382170844, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 23 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 7.55549894619012"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 7.55549894619012""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 7.55549894619012
""",
)

entry(
    index = 32,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_3O-u1",
    kinetics = ArrheniusBM(A=(0.00127734,'m^3/(mol*s)'), n=3.49913, w0=(353.5,'kJ/mol'), E0=(103.497,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_N-3O-u1",
    kinetics = ArrheniusBM(A=(3.71371e-05,'m^3/(mol*s)'), n=3.67929, w0=(353.5,'kJ/mol'), E0=(105.646,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.0235125,'m^3/(mol*s)'), n=2.67238, w0=(353.5,'kJ/mol'), E0=(85.7434,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.4472182228592687, var=10.103390614597473, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 12.521006570348037"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 12.521006570348037""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 12.521006570348037
""",
)

entry(
    index = 35,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1",
    kinetics = ArrheniusBM(A=(0.00226498,'m^3/(mol*s)'), n=3.15133, w0=(353.5,'kJ/mol'), E0=(127.522,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.000137082,'m^3/(mol*s)'), n=3.52572, w0=(353.5,'kJ/mol'), E0=(140.961,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->H",
    kinetics = ArrheniusBM(A=(29364.5,'m^3/(mol*s)'), n=0.785655, w0=(360,'kJ/mol'), E0=(105.952,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_3CClFH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H",
    kinetics = ArrheniusBM(A=(0.0789065,'m^3/(mol*s)'), n=2.39473, w0=(320,'kJ/mol'), E0=(92.9853,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04515383280298885, var=0.6729740783861372, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H
    Total Standard Deviation in ln(k): 1.7580362080520624"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H
Total Standard Deviation in ln(k): 1.7580362080520624""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H
Total Standard Deviation in ln(k): 1.7580362080520624
""",
)

entry(
    index = 39,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H",
    kinetics = ArrheniusBM(A=(5.91801,'m^3/(mol*s)'), n=2.07168, w0=(518.487,'kJ/mol'), E0=(170.135,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5360482116895531, var=5.127097611782693, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H
    Total Standard Deviation in ln(k): 5.886195528231643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H
Total Standard Deviation in ln(k): 5.886195528231643""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H
Total Standard Deviation in ln(k): 5.886195528231643
""",
)

entry(
    index = 40,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H",
    kinetics = ArrheniusBM(A=(3.07604e+15,'m^3/(mol*s)'), n=-2.4981, w0=(481.457,'kJ/mol'), E0=(224.749,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5033430380015966, var=10.506318905715563, Tref=1000.0, N=98, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H',), comment="""BM rule fitted to 98 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H
    Total Standard Deviation in ln(k): 7.762719482283143"""),
    rank = 11,
    shortDesc = """BM rule fitted to 98 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H
Total Standard Deviation in ln(k): 7.762719482283143""",
    longDesc = 
"""
BM rule fitted to 98 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H
Total Standard Deviation in ln(k): 7.762719482283143
""",
)

entry(
    index = 41,
    label = "Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1",
    kinetics = ArrheniusBM(A=(0.0049864,'m^3/(mol*s)'), n=3.19625, w0=(222,'kJ/mol'), E0=(113.797,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.640932,'m^3/(mol*s)'), n=2.39839, w0=(222,'kJ/mol'), E0=(121.687,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_3R->O_Ext-1O-R_4R!H->C_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.0547071,'m^3/(mol*s)'), n=2.33633, w0=(353.5,'kJ/mol'), E0=(109.325,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08422783170099031, var=3.877957487404518, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R',), comment="""BM rule fitted to 31 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 4.15945833888862"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 4.15945833888862""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 4.15945833888862
""",
)

entry(
    index = 44,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->H",
    kinetics = ArrheniusBM(A=(1.04105,'m^3/(mol*s)'), n=2.3137, w0=(393.5,'kJ/mol'), E0=(121.366,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->H',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_3CClFH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H",
    kinetics = ArrheniusBM(A=(5.15234e-10,'m^3/(mol*s)'), n=4.89163, w0=(353.5,'kJ/mol'), E0=(58.1422,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10970347417673583, var=4.530602388423006, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H
    Total Standard Deviation in ln(k): 4.542757930405607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H
Total Standard Deviation in ln(k): 4.542757930405607""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H
Total Standard Deviation in ln(k): 4.542757930405607
""",
)

entry(
    index = 46,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000245593,'m^3/(mol*s)'), n=3.10149, w0=(353.5,'kJ/mol'), E0=(62.672,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.1830702118999947, var=15.116405154627513, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R',), comment="""BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 13.279475219944665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 13.279475219944665""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R
Total Standard Deviation in ln(k): 13.279475219944665
""",
)

entry(
    index = 47,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.000178698,'m^3/(mol*s)'), n=3.25898, w0=(353.5,'kJ/mol'), E0=(114.913,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH",
    kinetics = Arrhenius(A=(0.00423866,'m^3/(mol*s)'), n=2.57109, Ea=(34.3089,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-0.7811768145180682, var=4.435065715994784, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH',), comment="""BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH
    Total Standard Deviation in ln(k): 6.184646839552331"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH
Total Standard Deviation in ln(k): 6.184646839552331""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH
Total Standard Deviation in ln(k): 6.184646839552331
""",
)

entry(
    index = 49,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH",
    kinetics = ArrheniusBM(A=(0.00171,'m^3/(mol*s)'), n=2.75, w0=(353.5,'kJ/mol'), E0=(229.178,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_N-Sp-4R!H-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(6.44529e-06,'m^3/(mol*s)'), n=3.82527, w0=(353.5,'kJ/mol'), E0=(85.3443,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9431001763240277, var=1.01696777332508, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 4.391269914484271"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 4.391269914484271""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 4.391269914484271
""",
)

entry(
    index = 51,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0",
    kinetics = ArrheniusBM(A=(2.81472e-06,'m^3/(mol*s)'), n=3.81984, w0=(353.5,'kJ/mol'), E0=(116.193,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1712716741547082, var=11.928027365862736, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0
    Total Standard Deviation in ln(k): 9.8666424526943"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 9.8666424526943""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0
Total Standard Deviation in ln(k): 9.8666424526943
""",
)

entry(
    index = 52,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->H",
    kinetics = ArrheniusBM(A=(0.000687874,'m^3/(mol*s)'), n=2.99039, w0=(393.5,'kJ/mol'), E0=(120.004,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_1BrCClFHINPSSi->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H",
    kinetics = ArrheniusBM(A=(1.36075,'m^3/(mol*s)'), n=2.3096, w0=(353.5,'kJ/mol'), E0=(120.785,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21814001551781906, var=2.046637824119378, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H
    Total Standard Deviation in ln(k): 3.4160795320314543"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H
Total Standard Deviation in ln(k): 3.4160795320314543""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H
Total Standard Deviation in ln(k): 3.4160795320314543
""",
)

entry(
    index = 54,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(1.72013,'m^3/(mol*s)'), n=2.4493, w0=(353.5,'kJ/mol'), E0=(175.233,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(1.25229,'m^3/(mol*s)'), n=2.47248, w0=(353.5,'kJ/mol'), E0=(114.024,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14997521827239893, var=12.834895059233478, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 7.558950315538469"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 7.558950315538469""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi
Total Standard Deviation in ln(k): 7.558950315538469
""",
)

entry(
    index = 56,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi",
    kinetics = ArrheniusBM(A=(0.026185,'m^3/(mol*s)'), n=2.65783, w0=(353.5,'kJ/mol'), E0=(85.7434,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.4764185473892115, var=16.163686387534245, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi
    Total Standard Deviation in ln(k): 16.79457438260444"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 16.79457438260444""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 16.79457438260444
""",
)

entry(
    index = 57,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi",
    kinetics = ArrheniusBM(A=(0.0387235,'m^3/(mol*s)'), n=2.8378, w0=(353.5,'kJ/mol'), E0=(143.208,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H-1BrCClFHINPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R",
    kinetics = ArrheniusBM(A=(0.0108084,'m^3/(mol*s)'), n=2.63211, w0=(320,'kJ/mol'), E0=(83.1131,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.38328273573855226, var=1.3861367512733498, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R
    Total Standard Deviation in ln(k): 3.323282939489239"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R
Total Standard Deviation in ln(k): 3.323282939489239""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R
Total Standard Deviation in ln(k): 3.323282939489239
""",
)

entry(
    index = 59,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->Cl",
    kinetics = ArrheniusBM(A=(650.29,'m^3/(mol*s)'), n=1.25799, w0=(407.77,'kJ/mol'), E0=(121.039,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_1CClH->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl",
    kinetics = Arrhenius(A=(4.09512e-10,'m^3/(mol*s)'), n=5.00371, Ea=(116.731,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-0.052059800531379416, var=7.291004331568231, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl
    Total Standard Deviation in ln(k): 5.54396107036548"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl
Total Standard Deviation in ln(k): 5.54396107036548""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl
Total Standard Deviation in ln(k): 5.54396107036548
""",
)

entry(
    index = 61,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C",
    kinetics = ArrheniusBM(A=(1.45624e-09,'m^3/(mol*s)'), n=4.44899, w0=(492.473,'kJ/mol'), E0=(168.477,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1256329410325774, var=4.8578818493646, Tref=1000.0, N=91, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C',), comment="""BM rule fitted to 91 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C
    Total Standard Deviation in ln(k): 4.734217671667623"""),
    rank = 11,
    shortDesc = """BM rule fitted to 91 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C
Total Standard Deviation in ln(k): 4.734217671667623""",
    longDesc = 
"""
BM rule fitted to 91 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C
Total Standard Deviation in ln(k): 4.734217671667623
""",
)

entry(
    index = 62,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C",
    kinetics = ArrheniusBM(A=(214.578,'m^3/(mol*s)'), n=1.53134, w0=(338.253,'kJ/mol'), E0=(105.421,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7987268021680305, var=17.24494022079666, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C
    Total Standard Deviation in ln(k): 10.331920152595425"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C
Total Standard Deviation in ln(k): 10.331920152595425""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C
Total Standard Deviation in ln(k): 10.331920152595425
""",
)

entry(
    index = 63,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(5.89739e-06,'m^3/(mol*s)'), n=3.34803, w0=(353.5,'kJ/mol'), E0=(99.0058,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.865438312506608, var=15.298175891282746, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl
    Total Standard Deviation in ln(k): 15.040690532497113"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl
Total Standard Deviation in ln(k): 15.040690532497113""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl
Total Standard Deviation in ln(k): 15.040690532497113
""",
)

entry(
    index = 64,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(0.000271622,'m^3/(mol*s)'), n=3.0151, w0=(353.5,'kJ/mol'), E0=(96.5972,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04574810517930828, var=4.5785451964465835, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl',), comment="""BM rule fitted to 27 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 4.4045839592449045"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.4045839592449045""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 4.4045839592449045
""",
)

entry(
    index = 65,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.0397432,'m^3/(mol*s)'), n=2.50094, w0=(353.5,'kJ/mol'), E0=(107.939,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12727213483056368, var=0.09203472660077262, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R
    Total Standard Deviation in ln(k): 0.9279602392954537"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R
Total Standard Deviation in ln(k): 0.9279602392954537""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R
Total Standard Deviation in ln(k): 0.9279602392954537
""",
)

entry(
    index = 66,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000340767,'m^3/(mol*s)'), n=3.06, w0=(353.5,'kJ/mol'), E0=(73.6425,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.911279361112928, var=69.36738547860872, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 31.54931480980135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 31.54931480980135""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 31.54931480980135
""",
)

entry(
    index = 67,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R",
    kinetics = ArrheniusBM(A=(1.85866e-05,'m^3/(mol*s)'), n=3.19173, w0=(353.5,'kJ/mol'), E0=(113.846,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C",
    kinetics = Arrhenius(A=(5.46803e-05,'m^3/(mol*s)'), n=3.42277, Ea=(19.8982,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-3.6596417089766777e-16, var=0.04610066343987495, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C
    Total Standard Deviation in ln(k): 0.43043797255559474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 0.43043797255559474""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 0.43043797255559474
""",
)

entry(
    index = 69,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.07293e-05,'m^3/(mol*s)'), n=3.59914, w0=(353.5,'kJ/mol'), E0=(106.801,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O",
    kinetics = ArrheniusBM(A=(0.000485831,'m^3/(mol*s)'), n=2.91263, w0=(353.5,'kJ/mol'), E0=(110.441,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7783893338106116, var=0.8038852052149753, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O
    Total Standard Deviation in ln(k): 3.753190460950988"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O
Total Standard Deviation in ln(k): 3.753190460950988""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O
Total Standard Deviation in ln(k): 3.753190460950988
""",
)

entry(
    index = 71,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.1396e-10,'m^3/(mol*s)'), n=4.67699, w0=(353.5,'kJ/mol'), E0=(116.92,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20417774179252346, var=1.6704029360263537, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O
    Total Standard Deviation in ln(k): 3.1040105872980646"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O
Total Standard Deviation in ln(k): 3.1040105872980646""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O
Total Standard Deviation in ln(k): 3.1040105872980646
""",
)

entry(
    index = 72,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(6.48644e-06,'m^3/(mol*s)'), n=3.82406, w0=(353.5,'kJ/mol'), E0=(85.3443,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9654716715421346, var=1.0825276972362354, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 4.511626637258912"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 4.511626637258912""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 4.511626637258912
""",
)

entry(
    index = 73,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(9.76112e+14,'m^3/(mol*s)'), n=-2.15023, w0=(353.5,'kJ/mol'), E0=(179.903,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28557474229017404, var=91.69606982868704, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 19.914479631941294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 19.914479631941294""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 19.914479631941294
""",
)

entry(
    index = 74,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(0.000635821,'m^3/(mol*s)'), n=3.24928, w0=(353.5,'kJ/mol'), E0=(107.269,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7853855342652726, var=4.6338958371333066, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 6.288820572279257"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 6.288820572279257""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 6.288820572279257
""",
)

entry(
    index = 75,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(1338.35,'m^3/(mol*s)'), n=1.49764, w0=(353.5,'kJ/mol'), E0=(132.52,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.015227606370530776, var=0.5148571469056276, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 1.476728838185456"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 1.476728838185456""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C
Total Standard Deviation in ln(k): 1.476728838185456
""",
)

entry(
    index = 76,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F",
    kinetics = ArrheniusBM(A=(7299.69,'m^3/(mol*s)'), n=1.44021, w0=(353.5,'kJ/mol'), E0=(145.34,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2863230626541202, var=1.9795537304908053, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F
    Total Standard Deviation in ln(k): 3.539999061709846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F
Total Standard Deviation in ln(k): 3.539999061709846""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F
Total Standard Deviation in ln(k): 3.539999061709846
""",
)

entry(
    index = 77,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F",
    kinetics = ArrheniusBM(A=(40470,'m^3/(mol*s)'), n=1.16274, w0=(353.5,'kJ/mol'), E0=(125.062,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09460852833782482, var=23.7660067232626, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F
    Total Standard Deviation in ln(k): 10.010871859767997"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F
Total Standard Deviation in ln(k): 10.010871859767997""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F
Total Standard Deviation in ln(k): 10.010871859767997
""",
)

entry(
    index = 78,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O",
    kinetics = ArrheniusBM(A=(0.0338635,'m^3/(mol*s)'), n=2.6202, w0=(353.5,'kJ/mol'), E0=(96.5492,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.2318203518434205, var=14.865670896190005, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O
    Total Standard Deviation in ln(k): 15.849613281157865"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O
Total Standard Deviation in ln(k): 15.849613281157865""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O
Total Standard Deviation in ln(k): 15.849613281157865
""",
)

entry(
    index = 79,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.95806e+20,'m^3/(mol*s)'), n=-3.41724, w0=(353.5,'kJ/mol'), E0=(173.275,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3501671717020229, var=69.16912497985501, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O
    Total Standard Deviation in ln(k): 17.55279321528487"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O
Total Standard Deviation in ln(k): 17.55279321528487""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O
Total Standard Deviation in ln(k): 17.55279321528487
""",
)

entry(
    index = 80,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R",
    kinetics = ArrheniusBM(A=(0.0823982,'m^3/(mol*s)'), n=2.3774, w0=(320,'kJ/mol'), E0=(92.9853,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0326027877527767, var=0.3475770852570388, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R
    Total Standard Deviation in ln(k): 1.2638215194034916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R
Total Standard Deviation in ln(k): 1.2638215194034916""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R
Total Standard Deviation in ln(k): 1.2638215194034916
""",
)

entry(
    index = 81,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R",
    kinetics = Arrhenius(A=(2.13642e-10,'m^3/(mol*s)'), n=5.08394, Ea=(118.133,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-0.27838936131625447, var=7.177930469902688, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R
    Total Standard Deviation in ln(k): 6.070488820805335"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R
Total Standard Deviation in ln(k): 6.070488820805335""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R
Total Standard Deviation in ln(k): 6.070488820805335
""",
)

entry(
    index = 82,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1",
    kinetics = ArrheniusBM(A=(1.3611e-09,'m^3/(mol*s)'), n=4.45713, w0=(493,'kJ/mol'), E0=(168.418,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12645127501202907, var=4.838110257164557, Tref=1000.0, N=85, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1',), comment="""BM rule fitted to 85 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1
    Total Standard Deviation in ln(k): 4.727272849923811"""),
    rank = 11,
    shortDesc = """BM rule fitted to 85 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1
Total Standard Deviation in ln(k): 4.727272849923811""",
    longDesc = 
"""
BM rule fitted to 85 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1
Total Standard Deviation in ln(k): 4.727272849923811
""",
)

entry(
    index = 83,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1",
    kinetics = ArrheniusBM(A=(1.81909e-05,'m^3/(mol*s)'), n=3.64993, w0=(485,'kJ/mol'), E0=(159.215,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04751105928478793, var=12.866477605013023, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1
    Total Standard Deviation in ln(k): 7.31033370355403"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1
Total Standard Deviation in ln(k): 7.31033370355403""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1
Total Standard Deviation in ln(k): 7.31033370355403
""",
)

entry(
    index = 84,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H",
    kinetics = ArrheniusBM(A=(54732.4,'m^3/(mol*s)'), n=0.561845, w0=(383.885,'kJ/mol'), E0=(124.022,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1386451578478001, var=0.1631298144326113, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H
    Total Standard Deviation in ln(k): 1.1580537753094704"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H
Total Standard Deviation in ln(k): 1.1580537753094704""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H
Total Standard Deviation in ln(k): 1.1580537753094704
""",
)

entry(
    index = 85,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H",
    kinetics = ArrheniusBM(A=(9.7094e+09,'m^3/(mol*s)'), n=-0.320702, w0=(320,'kJ/mol'), E0=(138.359,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7370601198433495, var=2.067165882974821, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H
    Total Standard Deviation in ln(k): 4.734246165368837"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H
Total Standard Deviation in ln(k): 4.734246165368837""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H
Total Standard Deviation in ln(k): 4.734246165368837
""",
)

entry(
    index = 86,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R",
    kinetics = ArrheniusBM(A=(1.41898e-06,'m^3/(mol*s)'), n=3.52361, w0=(353.5,'kJ/mol'), E0=(95.7533,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.705400020897316, var=25.456443303468912, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R
    Total Standard Deviation in ln(k): 19.42481658324702"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R
Total Standard Deviation in ln(k): 19.42481658324702""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R
Total Standard Deviation in ln(k): 19.42481658324702
""",
)

entry(
    index = 87,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(2.40529e-06,'m^3/(mol*s)'), n=3.70283, w0=(353.5,'kJ/mol'), E0=(138.874,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(1.9965e-05,'m^3/(mol*s)'), n=3.06368, w0=(353.5,'kJ/mol'), E0=(93.4586,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1095182195769392, var=0.8144638925993362, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 2.0843977681841785"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 2.0843977681841785""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 2.0843977681841785
""",
)

entry(
    index = 89,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(0.00502134,'m^3/(mol*s)'), n=2.89121, w0=(353.5,'kJ/mol'), E0=(173.92,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi",
    kinetics = ArrheniusBM(A=(1.24392e-07,'m^3/(mol*s)'), n=4.02029, w0=(353.5,'kJ/mol'), E0=(65.9793,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19713229542458505, var=4.026634706913659, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi',), comment="""BM rule fitted to 21 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi
    Total Standard Deviation in ln(k): 4.51810416473341"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 4.51810416473341""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi
Total Standard Deviation in ln(k): 4.51810416473341
""",
)

entry(
    index = 91,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.000476496,'m^3/(mol*s)'), n=3.27616, w0=(353.5,'kJ/mol'), E0=(125.819,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0280362,'m^3/(mol*s)'), n=2.53741, w0=(353.5,'kJ/mol'), E0=(106.354,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3461974473326123, var=0.17221426982182148, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C
    Total Standard Deviation in ln(k): 1.701781972143114"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 1.701781972143114""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C
Total Standard Deviation in ln(k): 1.701781972143114
""",
)

entry(
    index = 93,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C",
    kinetics = ArrheniusBM(A=(0.000290035,'m^3/(mol*s)'), n=3.07816, w0=(353.5,'kJ/mol'), E0=(80.7316,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.4258573754702875, var=60.299906073343585, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C
    Total Standard Deviation in ln(k): 29.20017961021842"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 29.20017961021842""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C
Total Standard Deviation in ln(k): 29.20017961021842
""",
)

entry(
    index = 94,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(2.47592e+10,'m^3/(mol*s)'), n=-0.535493, w0=(353.5,'kJ/mol'), E0=(52.3754,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 95,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH",
    kinetics = ArrheniusBM(A=(3.03844e-05,'m^3/(mol*s)'), n=3.46112, w0=(353.5,'kJ/mol'), E0=(113.457,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_Sp-4C-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH",
    kinetics = ArrheniusBM(A=(9.84034e-05,'m^3/(mol*s)'), n=3.38442, w0=(353.5,'kJ/mol'), E0=(140.646,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_4R!H->C_N-Sp-4C-3CClFH
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_3CClFH-u1",
    kinetics = ArrheniusBM(A=(0.000576508,'m^3/(mol*s)'), n=2.8908, w0=(353.5,'kJ/mol'), E0=(110.642,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_3CClFH-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_3CClFH-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_N-3CClFH-u1",
    kinetics = ArrheniusBM(A=(0.0988204,'m^3/(mol*s)'), n=2.35704, w0=(353.5,'kJ/mol'), E0=(138.06,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_N-3CClFH-u1',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_N-3CClFH-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_N-3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_4R!H->O_N-3CClFH-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->C",
    kinetics = ArrheniusBM(A=(5.27678,'m^3/(mol*s)'), n=1.68981, w0=(353.5,'kJ/mol'), E0=(146.6,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_4CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C",
    kinetics = ArrheniusBM(A=(9.09828e-11,'m^3/(mol*s)'), n=4.70447, w0=(353.5,'kJ/mol'), E0=(116.607,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18717347720884508, var=1.7010605887705823, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C
    Total Standard Deviation in ln(k): 3.0849550994445063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C
Total Standard Deviation in ln(k): 3.0849550994445063""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C
Total Standard Deviation in ln(k): 3.0849550994445063
""",
)

entry(
    index = 101,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi",
    kinetics = ArrheniusBM(A=(5.8091e-05,'m^3/(mol*s)'), n=3.43326, w0=(353.5,'kJ/mol'), E0=(85.4072,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.717147087762446, var=2.3202219957308396, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
    Total Standard Deviation in ln(k): 7.368107505266617"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 7.368107505266617""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 7.368107505266617
""",
)

entry(
    index = 102,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi",
    kinetics = ArrheniusBM(A=(0.00523766,'m^3/(mol*s)'), n=2.97537, w0=(353.5,'kJ/mol'), E0=(94.6013,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.62569228034744, var=12.437155380495636, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
    Total Standard Deviation in ln(k): 13.667185946541299"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 13.667185946541299""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi
Total Standard Deviation in ln(k): 13.667185946541299
""",
)

entry(
    index = 103,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(354736,'m^3/(mol*s)'), n=0.720118, w0=(353.5,'kJ/mol'), E0=(91.4106,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 104,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000645269,'m^3/(mol*s)'), n=3.24696, w0=(353.5,'kJ/mol'), E0=(107.244,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7850264841947997, var=4.658032947514155, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 6.299143135274848"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.299143135274848""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 6.299143135274848
""",
)

entry(
    index = 105,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.69175,'m^3/(mol*s)'), n=2.2228, w0=(353.5,'kJ/mol'), E0=(121.476,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.04546378086073348, var=0.6170109796788148, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.688950939605304"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.688950939605304""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.688950939605304
""",
)

entry(
    index = 106,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(3.95544e+06,'m^3/(mol*s)'), n=0.662683, w0=(353.5,'kJ/mol'), E0=(157.82,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.43801691174399543, var=2.3077805722777383, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 4.146014444424883"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 4.146014444424883""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 4.146014444424883
""",
)

entry(
    index = 107,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_3O-u1",
    kinetics = ArrheniusBM(A=(0.150831,'m^3/(mol*s)'), n=2.7069, w0=(353.5,'kJ/mol'), E0=(105.444,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 108,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.00138537,'m^3/(mol*s)'), n=3.40706, w0=(353.5,'kJ/mol'), E0=(127.101,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 109,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(6.82681e+09,'m^3/(mol*s)'), n=-0.34993, w0=(353.5,'kJ/mol'), E0=(207.493,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.347108557697195, var=172.661745148035, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 27.214514610749784"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 27.214514610749784""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 27.214514610749784
""",
)

entry(
    index = 110,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi",
    kinetics = ArrheniusBM(A=(8.67215e+08,'m^3/(mol*s)'), n=-0.0764862, w0=(353.5,'kJ/mol'), E0=(132.819,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5067634685233431, var=17.3462608599284, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 9.622764606399254"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 9.622764606399254""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 9.622764606399254
""",
)

entry(
    index = 111,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.0305183,'m^3/(mol*s)'), n=2.6347, w0=(353.5,'kJ/mol'), E0=(91.254,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=5.3942369436223006, var=58.909467307985445, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 28.94020267734718"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 28.94020267734718""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 28.94020267734718
""",
)

entry(
    index = 112,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_3O-u1",
    kinetics = ArrheniusBM(A=(0.00474579,'m^3/(mol*s)'), n=2.96408, w0=(353.5,'kJ/mol'), E0=(109.07,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_N-3O-u1",
    kinetics = ArrheniusBM(A=(1.32859,'m^3/(mol*s)'), n=2.43214, w0=(353.5,'kJ/mol'), E0=(135.901,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 114,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(2.23848e+07,'m^3/(mol*s)'), n=0.359183, w0=(353.5,'kJ/mol'), E0=(82.2933,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_N-4R!H->O_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 115,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_4R!H->O",
    kinetics = ArrheniusBM(A=(0.00484591,'m^3/(mol*s)'), n=2.74561, w0=(320,'kJ/mol'), E0=(86.9193,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(0.367477,'m^3/(mol*s)'), n=2.16709, w0=(320,'kJ/mol'), E0=(90.9595,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.143033367643316, var=1.9536651408417827, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O
    Total Standard Deviation in ln(k): 3.1614701460007337"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O
Total Standard Deviation in ln(k): 3.1614701460007337""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O
Total Standard Deviation in ln(k): 3.1614701460007337
""",
)

entry(
    index = 117,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F",
    kinetics = Arrhenius(A=(5.38898e-10,'m^3/(mol*s)'), n=4.9261, Ea=(129.363,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-0.08580901697803098, var=3.278137638352536, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F
    Total Standard Deviation in ln(k): 3.8452992921885283"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F
Total Standard Deviation in ln(k): 3.8452992921885283""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F
Total Standard Deviation in ln(k): 3.8452992921885283
""",
)

entry(
    index = 118,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F",
    kinetics = Arrhenius(A=(4.57077e-11,'m^3/(mol*s)'), n=5.34703, Ea=(99.4154,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-0.23801412471858555, var=1.1768129525219777, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F
    Total Standard Deviation in ln(k): 2.7727822982738677"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F
Total Standard Deviation in ln(k): 2.7727822982738677""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F
Total Standard Deviation in ln(k): 2.7727822982738677
""",
)

entry(
    index = 119,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H",
    kinetics = Arrhenius(A=(4.47972e-14,'m^3/(mol*s)'), n=5.4495, Ea=(183.096,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.42403003549241625, var=10.830918806663643, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H',), comment="""BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H
    Total Standard Deviation in ln(k): 7.663057669308568"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H
Total Standard Deviation in ln(k): 7.663057669308568""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H
Total Standard Deviation in ln(k): 7.663057669308568
""",
)

entry(
    index = 120,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H",
    kinetics = ArrheniusBM(A=(1.04239e-06,'m^3/(mol*s)'), n=3.76371, w0=(485,'kJ/mol'), E0=(179.665,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007412698011367947, var=3.2119615157364767, Tref=1000.0, N=68, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H',), comment="""BM rule fitted to 68 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H
    Total Standard Deviation in ln(k): 3.6115002671111944"""),
    rank = 11,
    shortDesc = """BM rule fitted to 68 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H
Total Standard Deviation in ln(k): 3.6115002671111944""",
    longDesc = 
"""
BM rule fitted to 68 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H
Total Standard Deviation in ln(k): 3.6115002671111944
""",
)

entry(
    index = 121,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.24207e-07,'m^3/(mol*s)'), n=4.41751, w0=(485,'kJ/mol'), E0=(146.158,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05122312707765374, var=0.1080714602645949, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 0.7877424239732709"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.7877424239732709""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.7877424239732709
""",
)

entry(
    index = 122,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(2.19997e-06,'m^3/(mol*s)'), n=3.79688, w0=(485,'kJ/mol'), E0=(176.429,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3545102319141825, var=33.374376548679535, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 12.472196123677442"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 12.472196123677442""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 12.472196123677442
""",
)

entry(
    index = 123,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(1.71492e-09,'m^3/(mol*s)'), n=4.37345, w0=(485,'kJ/mol'), E0=(128.047,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 124,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_3ClF->Cl",
    kinetics = ArrheniusBM(A=(1580.64,'m^3/(mol*s)'), n=1.06012, w0=(407.77,'kJ/mol'), E0=(123.551,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_3ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_3ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_3ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_3ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_N-3ClF->Cl",
    kinetics = ArrheniusBM(A=(10572.3,'m^3/(mol*s)'), n=0.709227, w0=(360,'kJ/mol'), E0=(109.24,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_N-3ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_N-3ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_N-3ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_1CClH->H_N-3ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 126,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(193955,'m^3/(mol*s)'), n=1.03354, w0=(320,'kJ/mol'), E0=(112.267,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0953941796415763, var=3.773100850870637, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R
    Total Standard Deviation in ln(k): 6.646338578992126"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R
Total Standard Deviation in ln(k): 6.646338578992126""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R
Total Standard Deviation in ln(k): 6.646338578992126
""",
)

entry(
    index = 127,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C",
    kinetics = ArrheniusBM(A=(8.19658e-06,'m^3/(mol*s)'), n=3.30549, w0=(353.5,'kJ/mol'), E0=(98.8969,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(9.46969e-05,'m^3/(mol*s)'), n=2.97971, w0=(353.5,'kJ/mol'), E0=(149.359,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_4R!H->Cl_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi",
    kinetics = ArrheniusBM(A=(1.9354e-06,'m^3/(mol*s)'), n=3.35153, w0=(353.5,'kJ/mol'), E0=(87.5501,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08060586253333689, var=0.269547350563194, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
    Total Standard Deviation in ln(k): 1.2433446427813617"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 1.2433446427813617""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 1.2433446427813617
""",
)

entry(
    index = 130,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi",
    kinetics = ArrheniusBM(A=(2.22405e-05,'m^3/(mol*s)'), n=3.55361, w0=(353.5,'kJ/mol'), E0=(151.807,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 131,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi",
    kinetics = ArrheniusBM(A=(2.61514e-08,'m^3/(mol*s)'), n=4.20257, w0=(353.5,'kJ/mol'), E0=(71.2531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.30087764318985794, var=5.772145225413982, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi',), comment="""BM rule fitted to 16 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
    Total Standard Deviation in ln(k): 5.57240798407346"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 5.57240798407346""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 5.57240798407346
""",
)

entry(
    index = 132,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi",
    kinetics = ArrheniusBM(A=(1.28376e-06,'m^3/(mol*s)'), n=3.80533, w0=(353.5,'kJ/mol'), E0=(91.2355,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3011986784288935, var=0.748061486926763, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
    Total Standard Deviation in ln(k): 2.4906869506641205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 2.4906869506641205""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi
Total Standard Deviation in ln(k): 2.4906869506641205
""",
)

entry(
    index = 133,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.000849095,'m^3/(mol*s)'), n=3.17369, w0=(353.5,'kJ/mol'), E0=(115.83,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_4BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 134,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.01745,'m^3/(mol*s)'), n=2.59, w0=(353.5,'kJ/mol'), E0=(104.922,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_N-3CClFH->H_Ext-1O-R_N-4R!H->C_N-4BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C",
    kinetics = ArrheniusBM(A=(5.31202e+07,'m^3/(mol*s)'), n=0.114184, w0=(353.5,'kJ/mol'), E0=(73.8142,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22082647409963763, var=1.976197361605038, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 3.3730425702214295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 3.3730425702214295""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 3.3730425702214295
""",
)

entry(
    index = 136,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0002226,'m^3/(mol*s)'), n=3.1084, w0=(353.5,'kJ/mol'), E0=(94.5663,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 137,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(2.37397e-06,'m^3/(mol*s)'), n=3.44245, w0=(353.5,'kJ/mol'), E0=(138.84,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0817355097988577, var=1.4686957120371893, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 2.6348991645691346"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.6348991645691346""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.6348991645691346
""",
)

entry(
    index = 138,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C",
    kinetics = ArrheniusBM(A=(4.61854e-05,'m^3/(mol*s)'), n=3.71313, w0=(353.5,'kJ/mol'), E0=(141.91,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.533816630288395, var=0.018703501560800268, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C
    Total Standard Deviation in ln(k): 1.6154168788838004"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C
Total Standard Deviation in ln(k): 1.6154168788838004""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C
Total Standard Deviation in ln(k): 1.6154168788838004
""",
)

entry(
    index = 139,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.000215818,'m^3/(mol*s)'), n=3.25392, w0=(353.5,'kJ/mol'), E0=(87.4802,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 140,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.000541723,'m^3/(mol*s)'), n=3.2573, w0=(353.5,'kJ/mol'), E0=(85.3443,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 141,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.69582e-06,'m^3/(mol*s)'), n=3.94767, w0=(353.5,'kJ/mol'), E0=(138.068,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 142,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->Cl",
    kinetics = ArrheniusBM(A=(6.65995e-06,'m^3/(mol*s)'), n=3.94804, w0=(353.5,'kJ/mol'), E0=(146.969,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 143,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(5.27349e-06,'m^3/(mol*s)'), n=3.9638, w0=(353.5,'kJ/mol'), E0=(132.925,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 144,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(23683.6,'m^3/(mol*s)'), n=1.01364, w0=(353.5,'kJ/mol'), E0=(138.828,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5311374402950372, var=7.859704199276205, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 6.954823846704408"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 6.954823846704408""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 6.954823846704408
""",
)

entry(
    index = 145,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(4.6139e-06,'m^3/(mol*s)'), n=3.99356, w0=(353.5,'kJ/mol'), E0=(98.0064,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 146,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5397.72,'m^3/(mol*s)'), n=1.36912, w0=(353.5,'kJ/mol'), E0=(140.433,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21342496067016337, var=1.1512740510283421, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.6872730253646218"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.6872730253646218""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.6872730253646218
""",
)

entry(
    index = 147,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(0.0215072,'m^3/(mol*s)'), n=2.81865, w0=(353.5,'kJ/mol'), E0=(100.151,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 148,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(0.0117015,'m^3/(mol*s)'), n=2.97295, w0=(353.5,'kJ/mol'), E0=(103.134,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O",
    kinetics = ArrheniusBM(A=(376.856,'m^3/(mol*s)'), n=1.78142, w0=(353.5,'kJ/mol'), E0=(148.974,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2763781190439087, var=6.106748895892984, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O
    Total Standard Deviation in ln(k): 5.648486037400134"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O
Total Standard Deviation in ln(k): 5.648486037400134""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O
Total Standard Deviation in ln(k): 5.648486037400134
""",
)

entry(
    index = 150,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(15832.9,'m^3/(mol*s)'), n=1.36631, w0=(353.5,'kJ/mol'), E0=(146.07,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.37689763253647396, var=3.1269035627583026, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O
    Total Standard Deviation in ln(k): 4.491962598286164"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O
Total Standard Deviation in ln(k): 4.491962598286164""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O
Total Standard Deviation in ln(k): 4.491962598286164
""",
)

entry(
    index = 151,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-4CClO-R",
    kinetics = ArrheniusBM(A=(0.000377996,'m^3/(mol*s)'), n=3.50982, w0=(353.5,'kJ/mol'), E0=(152.625,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-4CClO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-4CClO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-4CClO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-4CClO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 152,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(0.290402,'m^3/(mol*s)'), n=2.70882, w0=(353.5,'kJ/mol'), E0=(133.726,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04728668766212546, var=0.11659326979309688, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 0.8033427342388866"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 0.8033427342388866""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 0.8033427342388866
""",
)

entry(
    index = 153,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1",
    kinetics = ArrheniusBM(A=(0.293027,'m^3/(mol*s)'), n=2.5626, w0=(353.5,'kJ/mol'), E0=(108.124,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 154,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.00232171,'m^3/(mol*s)'), n=3.27276, w0=(353.5,'kJ/mol'), E0=(226.932,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 155,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(198486,'m^3/(mol*s)'), n=1.14409, w0=(353.5,'kJ/mol'), E0=(89.6195,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.6690213870302952, var=54.489417666867446, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 24.016989135680586"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 24.016989135680586""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 24.016989135680586
""",
)

entry(
    index = 156,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1",
    kinetics = ArrheniusBM(A=(0.00168156,'m^3/(mol*s)'), n=3.00925, w0=(353.5,'kJ/mol'), E0=(94.0774,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.021653749110700612, var=0.3876711913547304, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1
    Total Standard Deviation in ln(k): 1.30261955557131"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 1.30261955557131""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1
Total Standard Deviation in ln(k): 1.30261955557131
""",
)

entry(
    index = 157,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.00100398,'m^3/(mol*s)'), n=3.43964, w0=(353.5,'kJ/mol'), E0=(108.085,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 158,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_5R!H->C",
    kinetics = ArrheniusBM(A=(0.0258927,'m^3/(mol*s)'), n=2.65481, w0=(353.5,'kJ/mol'), E0=(91.7276,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 159,
    label = "Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2.98958e+12,'m^3/(mol*s)'), n=-1.30667, w0=(353.5,'kJ/mol'), E0=(71.1161,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_N-1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-4R!H-1BrCClFHINPSSi_4R!H->O_Ext-1BrCClFHINPSSi-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 160,
    label = "Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O_Ext-3CClF-R",
    kinetics = ArrheniusBM(A=(0.145146,'m^3/(mol*s)'), n=2.24269, w0=(320,'kJ/mol'), E0=(93.1337,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O_Ext-3CClF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O_Ext-3CClF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O_Ext-3CClF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_1BrCClFHINPSSi->F_N-3CClFH->H_Ext-3CClF-R_Ext-3CClF-R_N-4R!H->O_Ext-3CClF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 161,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R",
    kinetics = ArrheniusBM(A=(2.32388e-06,'m^3/(mol*s)'), n=3.87693, w0=(525,'kJ/mol'), E0=(162.535,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.40405999545659355, var=4.002554743944122, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R
    Total Standard Deviation in ln(k): 5.025976465848059"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R
Total Standard Deviation in ln(k): 5.025976465848059""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R
Total Standard Deviation in ln(k): 5.025976465848059
""",
)

entry(
    index = 162,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi",
    kinetics = Arrhenius(A=(4.38641e-13,'m^3/(mol*s)'), n=6.02538, Ea=(108.443,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-0.24946267419827067, var=0.23735508985517292, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 1.6034795656410965"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 1.6034795656410965""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 1.6034795656410965
""",
)

entry(
    index = 163,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi",
    kinetics = Arrhenius(A=(4.66583e-10,'m^3/(mol*s)'), n=5.00785, Ea=(94.9017,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=4.555001829372172e-15, var=0.905647815829145, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi
    Total Standard Deviation in ln(k): 1.9078167676187665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 1.9078167676187665""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi
Total Standard Deviation in ln(k): 1.9078167676187665
""",
)

entry(
    index = 164,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R",
    kinetics = Arrhenius(A=(1.44474e-14,'m^3/(mol*s)'), n=5.5798, Ea=(181.849,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.36171727979665164, var=11.029042813727346, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R
    Total Standard Deviation in ln(k): 7.566563125881567"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R
Total Standard Deviation in ln(k): 7.566563125881567""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R
Total Standard Deviation in ln(k): 7.566563125881567
""",
)

entry(
    index = 165,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.42397e-07,'m^3/(mol*s)'), n=3.77581, w0=(485,'kJ/mol'), E0=(179.648,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.014576580586415892, var=3.282066548170195, Tref=1000.0, N=56, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R',), comment="""BM rule fitted to 56 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R
    Total Standard Deviation in ln(k): 3.668497801231794"""),
    rank = 11,
    shortDesc = """BM rule fitted to 56 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R
Total Standard Deviation in ln(k): 3.668497801231794""",
    longDesc = 
"""
BM rule fitted to 56 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R
Total Standard Deviation in ln(k): 3.668497801231794
""",
)

entry(
    index = 166,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(4.97707e-05,'m^3/(mol*s)'), n=3.41316, w0=(485,'kJ/mol'), E0=(181.191,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2740281683782734, var=0.9608410806975933, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C
    Total Standard Deviation in ln(k): 2.653604457865634"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.653604457865634""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.653604457865634
""",
)

entry(
    index = 167,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(1.04396e-05,'m^3/(mol*s)'), n=3.41775, w0=(485,'kJ/mol'), E0=(178.695,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23338913056573896, var=0.3363096895790088, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C
    Total Standard Deviation in ln(k): 1.7489951088135431"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 1.7489951088135431""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 1.7489951088135431
""",
)

entry(
    index = 168,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O",
    kinetics = Arrhenius(A=(7.33803e-10,'m^3/(mol*s)'), n=5.15307, Ea=(83.6194,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=2.5832765004541253e-16, var=0.13094448662163297, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O
    Total Standard Deviation in ln(k): 0.7254384960155565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 0.7254384960155565""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 0.7254384960155565
""",
)

entry(
    index = 169,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(8.68377e-05,'m^3/(mol*s)'), n=3.62888, w0=(485,'kJ/mol'), E0=(152.865,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 170,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C",
    kinetics = ArrheniusBM(A=(2.08267e-06,'m^3/(mol*s)'), n=3.44277, w0=(485,'kJ/mol'), E0=(172.692,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(4.03653e-08,'m^3/(mol*s)'), n=4.6553, w0=(485,'kJ/mol'), E0=(175.804,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Sp-4R!H-3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.53289e+07,'m^3/(mol*s)'), n=0.481201, w0=(320,'kJ/mol'), E0=(124.304,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3887130076109249, var=3.3668007543218645, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 7.167685778135642"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 7.167685778135642""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 7.167685778135642
""",
)

entry(
    index = 173,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-4BrCFINOPSSi-R",
    kinetics = ArrheniusBM(A=(8.83229e-06,'m^3/(mol*s)'), n=3.59735, w0=(353.5,'kJ/mol'), E0=(117.975,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 174,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R",
    kinetics = ArrheniusBM(A=(2.62839e-06,'m^3/(mol*s)'), n=3.30957, w0=(353.5,'kJ/mol'), E0=(87.9188,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7680594107793358, var=0.5068946612148024, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R
    Total Standard Deviation in ln(k): 3.3570994278277206"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R
Total Standard Deviation in ln(k): 3.3570994278277206""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R
Total Standard Deviation in ln(k): 3.3570994278277206
""",
)

entry(
    index = 175,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.50169e-06,'m^3/(mol*s)'), n=3.68796, w0=(353.5,'kJ/mol'), E0=(71.2531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4125515777474352, var=13.9993164115234, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C',), comment="""BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 8.537410432508615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 8.537410432508615""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 8.537410432508615
""",
)

entry(
    index = 176,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(0.000699968,'m^3/(mol*s)'), n=2.91672, w0=(353.5,'kJ/mol'), E0=(109.953,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.020448556504258156, var=0.42035847515207864, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 1.3511494337235"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 1.3511494337235""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 1.3511494337235
""",
)

entry(
    index = 177,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.07246e-05,'m^3/(mol*s)'), n=3.56773, w0=(353.5,'kJ/mol'), E0=(105.004,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.044221994969172, var=7.113647583797902, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 10.48314971885026"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 10.48314971885026""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 10.48314971885026
""",
)

entry(
    index = 178,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(7.08191e-06,'m^3/(mol*s)'), n=3.53568, w0=(353.5,'kJ/mol'), E0=(71.7831,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2372395445577914, var=1.8951355453933132, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 3.3558761933734216"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.3558761933734216""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.3558761933734216
""",
)

entry(
    index = 179,
    label = "Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(1.13121e+08,'m^3/(mol*s)'), n=-0.0669906, w0=(353.5,'kJ/mol'), E0=(81.6653,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_N-3CClFH-u1_Ext-3CClFH-R_Ext-3CClFH-R_4R!H->C_5R!H->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 180,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000214,'m^3/(mol*s)'), n=2.82, w0=(353.5,'kJ/mol'), E0=(150.907,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 181,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_5R!H->O",
    kinetics = ArrheniusBM(A=(0.000778,'m^3/(mol*s)'), n=2.78, w0=(353.5,'kJ/mol'), E0=(151.182,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 182,
    label = "Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(0.000591,'m^3/(mol*s)'), n=2.76, w0=(353.5,'kJ/mol'), E0=(139.596,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_N-1O-u0_Ext-3CClFH-R_Sp-4R!H-3CClFH_N-4R!H->O_N-4CF->C_Ext-3CClFH-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 183,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(8.38302e-05,'m^3/(mol*s)'), n=3.60203, w0=(353.5,'kJ/mol'), E0=(138.734,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_4R!H->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_Sp-5R!H=1BrBrCCClClFFHHIINNPPSSSiSi_5R!H->C_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 184,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.37515e-06,'m^3/(mol*s)'), n=3.75034, w0=(353.5,'kJ/mol'), E0=(86.9747,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_4BrCClFINPSSi->C_Ext-1C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 185,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.05616,'m^3/(mol*s)'), n=2.3798, w0=(353.5,'kJ/mol'), E0=(126.609,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(0.285485,'m^3/(mol*s)'), n=2.54097, w0=(353.5,'kJ/mol'), E0=(126.586,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(0.340714,'m^3/(mol*s)'), n=2.59484, w0=(353.5,'kJ/mol'), E0=(110.612,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_Ext-3O-R_N-4R!H->O_N-1BrCClFHINPSSi->H_N-4BrCClFINPSSi->C_Ext-1C-R_Ext-1C-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 188,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_3O-u1",
    kinetics = ArrheniusBM(A=(4.84958,'m^3/(mol*s)'), n=2.26492, w0=(353.5,'kJ/mol'), E0=(126.301,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 189,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.0378484,'m^3/(mol*s)'), n=2.98508, w0=(353.5,'kJ/mol'), E0=(149.624,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_5R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 190,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(1.07646e+06,'m^3/(mol*s)'), n=0.844589, w0=(353.5,'kJ/mol'), E0=(152.953,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4413960265367777, var=18.481760023730722, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 9.727475050899121"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 9.727475050899121""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 9.727475050899121
""",
)

entry(
    index = 191,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_3O-u1",
    kinetics = ArrheniusBM(A=(4.39416,'m^3/(mol*s)'), n=2.31879, w0=(353.5,'kJ/mol'), E0=(117.73,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 192,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.0372336,'m^3/(mol*s)'), n=3.03896, w0=(353.5,'kJ/mol'), E0=(137.484,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 193,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1",
    kinetics = ArrheniusBM(A=(0.0379121,'m^3/(mol*s)'), n=2.90824, w0=(353.5,'kJ/mol'), E0=(126.106,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 194,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(7.30096,'m^3/(mol*s)'), n=2.36151, w0=(353.5,'kJ/mol'), E0=(142.638,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 195,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->Cl",
    kinetics = ArrheniusBM(A=(0.0308105,'m^3/(mol*s)'), n=2.88761, w0=(353.5,'kJ/mol'), E0=(141.13,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_4CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 196,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->Cl",
    kinetics = ArrheniusBM(A=(737.893,'m^3/(mol*s)'), n=1.8413, w0=(353.5,'kJ/mol'), E0=(72.5651,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.0696082343213145, var=16.366626197588495, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->Cl
    Total Standard Deviation in ln(k): 13.310314192736145"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->Cl
Total Standard Deviation in ln(k): 13.310314192736145""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->Cl
Total Standard Deviation in ln(k): 13.310314192736145
""",
)

entry(
    index = 197,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_4CClO->Cl",
    kinetics = ArrheniusBM(A=(0.00381903,'m^3/(mol*s)'), n=3.24993, w0=(353.5,'kJ/mol'), E0=(137.265,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_4CClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_4CClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_4CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_4CClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 198,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl",
    kinetics = ArrheniusBM(A=(0.00139606,'m^3/(mol*s)'), n=3.03068, w0=(353.5,'kJ/mol'), E0=(93.4452,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.24036189963721574, var=0.37472679916741264, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl
    Total Standard Deviation in ln(k): 1.8311216004045205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl
Total Standard Deviation in ln(k): 1.8311216004045205""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl
Total Standard Deviation in ln(k): 1.8311216004045205
""",
)

entry(
    index = 199,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F",
    kinetics = ArrheniusBM(A=(5.97567e-06,'m^3/(mol*s)'), n=3.74007, w0=(525,'kJ/mol'), E0=(165.942,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.41502436959272, var=3.608170919263771, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F
    Total Standard Deviation in ln(k): 4.850806369521371"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F
Total Standard Deviation in ln(k): 4.850806369521371""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F
Total Standard Deviation in ln(k): 4.850806369521371
""",
)

entry(
    index = 200,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(5.86191e-10,'m^3/(mol*s)'), n=4.99656, w0=(525,'kJ/mol'), E0=(142.536,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9423094015406189, var=6.107335727119703, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F
    Total Standard Deviation in ln(k): 7.321918240717543"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F
Total Standard Deviation in ln(k): 7.321918240717543""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F
Total Standard Deviation in ln(k): 7.321918240717543
""",
)

entry(
    index = 201,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_Ext-1CH-R",
    kinetics = Arrhenius(A=(2.80067e-20,'m^3/(mol*s)'), n=8.17077, Ea=(92.4857,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_Ext-1CH-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_Ext-1CH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_Ext-1CH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_Ext-1CH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 202,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_4BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(5.18265e-09,'m^3/(mol*s)'), n=4.74784, w0=(525,'kJ/mol'), E0=(136.977,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_4BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 203,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C",
    kinetics = Arrhenius(A=(2.09116e-10,'m^3/(mol*s)'), n=5.09452, Ea=(95.7445,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=3.711482972081029e-15, var=0.4616292785593304, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 1.3620832815409953"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 1.3620832815409953""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C
Total Standard Deviation in ln(k): 1.3620832815409953
""",
)

entry(
    index = 204,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl",
    kinetics = Arrhenius(A=(2.19505e-15,'m^3/(mol*s)'), n=5.78938, Ea=(216.223,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.4620993526379812e-15, var=7.346114596943411, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 5.4335771623628215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 5.4335771623628215""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl
Total Standard Deviation in ln(k): 5.4335771623628215
""",
)

entry(
    index = 205,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl",
    kinetics = Arrhenius(A=(1.89102e-14,'m^3/(mol*s)'), n=5.54986, Ea=(176.939,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.21177653809717784, var=8.241295978795362, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 6.287226648130523"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 6.287226648130523""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 6.287226648130523
""",
)

entry(
    index = 206,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0",
    kinetics = ArrheniusBM(A=(8.64116e-07,'m^3/(mol*s)'), n=3.78655, w0=(485,'kJ/mol'), E0=(179.584,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.013163610600771935, var=3.267380381428161, Tref=1000.0, N=50, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0',), comment="""BM rule fitted to 50 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0
    Total Standard Deviation in ln(k): 3.656812796811706"""),
    rank = 11,
    shortDesc = """BM rule fitted to 50 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0
Total Standard Deviation in ln(k): 3.656812796811706""",
    longDesc = 
"""
BM rule fitted to 50 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0
Total Standard Deviation in ln(k): 3.656812796811706
""",
)

entry(
    index = 207,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0",
    kinetics = ArrheniusBM(A=(226.684,'m^3/(mol*s)'), n=1.41927, w0=(485,'kJ/mol'), E0=(172.862,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.47620233444766813, var=9.700063969632213, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0
    Total Standard Deviation in ln(k): 7.440220781206078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0
Total Standard Deviation in ln(k): 7.440220781206078""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0
Total Standard Deviation in ln(k): 7.440220781206078
""",
)

entry(
    index = 208,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.8148e-05,'m^3/(mol*s)'), n=3.38383, w0=(485,'kJ/mol'), E0=(179.393,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.2149616755423822, var=2.123797586144167, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 5.9742190570817675"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 5.9742190570817675""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 5.9742190570817675
""",
)

entry(
    index = 209,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_4R!H->O",
    kinetics = ArrheniusBM(A=(3.95e-05,'m^3/(mol*s)'), n=3.43, w0=(485,'kJ/mol'), E0=(182.949,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 210,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_N-4R!H->O",
    kinetics = ArrheniusBM(A=(3.70857e-08,'m^3/(mol*s)'), n=4.36701, w0=(485,'kJ/mol'), E0=(179.598,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 211,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.48449e-05,'m^3/(mol*s)'), n=3.39528, w0=(485,'kJ/mol'), E0=(181.012,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2840077946476841, var=0.7833768100046159, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 2.487949901748954"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 2.487949901748954""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 2.487949901748954
""",
)

entry(
    index = 212,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C",
    kinetics = ArrheniusBM(A=(2.26291e-08,'m^3/(mol*s)'), n=4.37484, w0=(485,'kJ/mol'), E0=(173.742,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24436438432485383, var=0.014235358056972383, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
    Total Standard Deviation in ln(k): 0.8531698562866338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 0.8531698562866338""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 0.8531698562866338
""",
)

entry(
    index = 213,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.972e-05,'m^3/(mol*s)'), n=3.28397, w0=(485,'kJ/mol'), E0=(175.447,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1309384567838519, var=3.7654530018551404, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C
    Total Standard Deviation in ln(k): 6.731697260808464"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C
Total Standard Deviation in ln(k): 6.731697260808464""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C
Total Standard Deviation in ln(k): 6.731697260808464
""",
)

entry(
    index = 214,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_5R!H->C",
    kinetics = ArrheniusBM(A=(1.10332e-07,'m^3/(mol*s)'), n=4.39237, w0=(485,'kJ/mol'), E0=(138.074,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 215,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_N-5R!H->C",
    kinetics = Arrhenius(A=(4.88042e-12,'m^3/(mol*s)'), n=5.91377, Ea=(84.5653,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_N-3C-u1_Ext-3C-R_Ext-3C-R_4R!H->O_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 216,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(830.61,'m^3/(mol*s)'), n=1.7707, w0=(320,'kJ/mol'), E0=(89.765,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_4R!H->O",
    kinetics = ArrheniusBM(A=(14.1008,'m^3/(mol*s)'), n=2.18545, w0=(320,'kJ/mol'), E0=(90.1727,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(814.812,'m^3/(mol*s)'), n=1.79633, w0=(320,'kJ/mol'), E0=(82.2358,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_N-3CClF->C_N-1CClH->H_Ext-1C-R_Ext-1C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.20903e-06,'m^3/(mol*s)'), n=3.28294, w0=(353.5,'kJ/mol'), E0=(88.1477,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 220,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.000106385,'m^3/(mol*s)'), n=3.20001, w0=(353.5,'kJ/mol'), E0=(140.681,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_Ext-1O-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 221,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(5.43644e-05,'m^3/(mol*s)'), n=3.30995, w0=(353.5,'kJ/mol'), E0=(55.5613,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02227882775117408, var=14.297730926439584, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 7.636349486192913"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R
Total Standard Deviation in ln(k): 7.636349486192913""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R
Total Standard Deviation in ln(k): 7.636349486192913
""",
)

entry(
    index = 222,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.000106567,'m^3/(mol*s)'), n=3.23582, w0=(353.5,'kJ/mol'), E0=(135.421,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 223,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(5.62416e-08,'m^3/(mol*s)'), n=4.11181, w0=(353.5,'kJ/mol'), E0=(79.5433,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06842683596843384, var=0.9569025969019228, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R
    Total Standard Deviation in ln(k): 2.132986608830523"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 2.132986608830523""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 2.132986608830523
""",
)

entry(
    index = 224,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->O",
    kinetics = ArrheniusBM(A=(0.000118485,'m^3/(mol*s)'), n=3.29853, w0=(353.5,'kJ/mol'), E0=(109.065,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 225,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O",
    kinetics = ArrheniusBM(A=(0.0008528,'m^3/(mol*s)'), n=2.86905, w0=(353.5,'kJ/mol'), E0=(110.115,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06865433593186293, var=0.324358085390257, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O',), comment="""BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O
    Total Standard Deviation in ln(k): 1.314243949622305"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 1.314243949622305""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 1.314243949622305
""",
)

entry(
    index = 226,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.82278e-05,'m^3/(mol*s)'), n=3.44719, w0=(353.5,'kJ/mol'), E0=(107.142,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 227,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.000485841,'m^3/(mol*s)'), n=3.11646, w0=(353.5,'kJ/mol'), E0=(147.641,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 228,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.000246125,'m^3/(mol*s)'), n=3.06199, w0=(353.5,'kJ/mol'), E0=(76.3786,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15291669914558925, var=3.622234114288285, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R
    Total Standard Deviation in ln(k): 4.199658252051798"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 4.199658252051798""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R
Total Standard Deviation in ln(k): 4.199658252051798
""",
)

entry(
    index = 229,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_3O-u1",
    kinetics = ArrheniusBM(A=(34.915,'m^3/(mol*s)'), n=2.08375, w0=(353.5,'kJ/mol'), E0=(106.274,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 230,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_N-3O-u1",
    kinetics = ArrheniusBM(A=(0.129776,'m^3/(mol*s)'), n=2.87392, w0=(353.5,'kJ/mol'), E0=(149.459,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_N-3O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_N-3O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_4R!H->F_Ext-1BrCClFHINPSSi-R_N-5R!H->O_Ext-1BrCClFHINPSSi-R_N-3O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 231,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->Cl_Ext-1BrCClFHINPSSi-R",
    kinetics = ArrheniusBM(A=(147.866,'m^3/(mol*s)'), n=2.04113, w0=(353.5,'kJ/mol'), E0=(69.632,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->Cl_Ext-1BrCClFHINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->Cl_Ext-1BrCClFHINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->Cl_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_Ext-1BrCClFHINPSSi-R_N-4CClO->Cl_Ext-1BrCClFHINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 232,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R",
    kinetics = ArrheniusBM(A=(0.00211237,'m^3/(mol*s)'), n=3.19107, w0=(353.5,'kJ/mol'), E0=(120.015,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.14649321907291513, var=0.08544573799067572, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R
    Total Standard Deviation in ln(k): 0.9540795891838967"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R
Total Standard Deviation in ln(k): 0.9540795891838967""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R
Total Standard Deviation in ln(k): 0.9540795891838967
""",
)

entry(
    index = 233,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->O",
    kinetics = ArrheniusBM(A=(0.00678858,'m^3/(mol*s)'), n=3.1372, w0=(353.5,'kJ/mol'), E0=(110.664,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_4CO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 234,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->O",
    kinetics = ArrheniusBM(A=(0.00108931,'m^3/(mol*s)'), n=3.05784, w0=(353.5,'kJ/mol'), E0=(92.5778,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_N-4CO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 235,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R",
    kinetics = ArrheniusBM(A=(6.65294e-06,'m^3/(mol*s)'), n=3.72603, w0=(525,'kJ/mol'), E0=(166.297,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.41260528013977593, var=3.766944304691461, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R
    Total Standard Deviation in ln(k): 4.927610299945598"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R
Total Standard Deviation in ln(k): 4.927610299945598""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R
Total Standard Deviation in ln(k): 4.927610299945598
""",
)

entry(
    index = 236,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_5BrCClINOPSSi->C",
    kinetics = Arrhenius(A=(1.84865e-10,'m^3/(mol*s)'), n=5.13872, Ea=(109.875,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_5BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_N-5BrCClINOPSSi->C",
    kinetics = ArrheniusBM(A=(6.15e-07,'m^3/(mol*s)'), n=4.14, w0=(525,'kJ/mol'), E0=(164.016,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_N-5BrCClINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_N-5BrCClINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_N-5R!H->F_N-5BrCClINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C_Ext-1CH-R",
    kinetics = Arrhenius(A=(7.71142e-12,'m^3/(mol*s)'), n=5.47558, Ea=(94.535,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C_Ext-1CH-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C_Ext-1CH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C_Ext-1CH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C_Ext-1CH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 239,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C_4ClO->Cl",
    kinetics = Arrhenius(A=(3.57367e-11,'m^3/(mol*s)'), n=5.32561, Ea=(91.9755,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C_4ClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C_4ClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C_4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C_4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 240,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C_N-4ClO->Cl",
    kinetics = ArrheniusBM(A=(3.31829e-08,'m^3/(mol*s)'), n=4.48236, w0=(525,'kJ/mol'), E0=(137.569,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C_N-4ClO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C_N-4ClO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C_N-4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_N-4R!H->F_N-Sp-4BrBrCCCClClHIINNOOPPSSSiSi=1BrBrCCCCClClHHIINNOOPPSSSiSi_N-4BrCClINOPSSi->C_N-4ClO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 241,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl_Ext-3C-R",
    kinetics = Arrhenius(A=(1.14861e-16,'m^3/(mol*s)'), n=6.26453, Ea=(226.951,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 242,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R",
    kinetics = Arrhenius(A=(3.78607e-14,'m^3/(mol*s)'), n=5.31392, Ea=(185.138,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.4396055164435505e-15, var=13.213307581282198, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
    Total Standard Deviation in ln(k): 7.287234778450718"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 7.287234778450718""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R
Total Standard Deviation in ln(k): 7.287234778450718
""",
)

entry(
    index = 243,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.08155e-09,'m^3/(mol*s)'), n=4.21534, w0=(525,'kJ/mol'), E0=(162.625,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4865493283001421, var=9.409053617132892, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
    Total Standard Deviation in ln(k): 7.371846351776555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 7.371846351776555""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R
Total Standard Deviation in ln(k): 7.371846351776555
""",
)

entry(
    index = 244,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(8.646e-12,'m^3/(mol*s)'), n=4.97681, w0=(525,'kJ/mol'), E0=(136.768,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 245,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C",
    kinetics = Arrhenius(A=(2.53105e-21,'m^3/(mol*s)'), n=7.72849, Ea=(150.183,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-0.12254612175455146, var=2.3442106179447664, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 3.3773176560977074"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.3773176560977074""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 3.3773176560977074
""",
)

entry(
    index = 246,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.4072e-05,'m^3/(mol*s)'), n=3.45455, w0=(485,'kJ/mol'), E0=(188.572,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0985724738003168, var=6.096049042481217, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R',), comment="""BM rule fitted to 24 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R
    Total Standard Deviation in ln(k): 5.197396181709261"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 5.197396181709261""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R
Total Standard Deviation in ln(k): 5.197396181709261
""",
)

entry(
    index = 247,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(7.98997e-08,'m^3/(mol*s)'), n=4.06507, w0=(485,'kJ/mol'), E0=(170.994,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06281027474987426, var=0.5772293032820927, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C',), comment="""BM rule fitted to 21 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 1.6809244274004382"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 1.6809244274004382""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 1.6809244274004382
""",
)

entry(
    index = 248,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(6.93639e-07,'m^3/(mol*s)'), n=3.84128, w0=(485,'kJ/mol'), E0=(181.27,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1761447262271474, var=1.3084767087797642, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 2.735764416523126"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 2.735764416523126""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 2.735764416523126
""",
)

entry(
    index = 249,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(86.3166,'m^3/(mol*s)'), n=1.5824, w0=(485,'kJ/mol'), E0=(174.861,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.40395656897540017, var=13.200380407841584, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 8.298635444986433"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 8.298635444986433""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C
Total Standard Deviation in ln(k): 8.298635444986433
""",
)

entry(
    index = 250,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1.28573e-06,'m^3/(mol*s)'), n=3.56699, w0=(485,'kJ/mol'), E0=(129.946,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 251,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->O",
    kinetics = ArrheniusBM(A=(8.35e-05,'m^3/(mol*s)'), n=3.36, w0=(485,'kJ/mol'), E0=(179.463,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 252,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(4.362e-07,'m^3/(mol*s)'), n=3.96684, w0=(485,'kJ/mol'), E0=(178.635,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 253,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.34e-05,'m^3/(mol*s)'), n=3.35, w0=(485,'kJ/mol'), E0=(183.315,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 254,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(6.36303e-10,'m^3/(mol*s)'), n=4.82658, w0=(485,'kJ/mol'), E0=(166.608,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.47458481579289263, var=0.005426392301842782, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 1.34010106579824"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 1.34010106579824""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 1.34010106579824
""",
)

entry(
    index = 255,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.35e-05,'m^3/(mol*s)'), n=3.34, w0=(485,'kJ/mol'), E0=(179.728,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 256,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.894e-08,'m^3/(mol*s)'), n=4.35365, w0=(485,'kJ/mol'), E0=(174.899,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 257,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->O",
    kinetics = ArrheniusBM(A=(7.33269e-08,'m^3/(mol*s)'), n=4.23045, w0=(485,'kJ/mol'), E0=(172.474,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 258,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->O",
    kinetics = ArrheniusBM(A=(2.43e-05,'m^3/(mol*s)'), n=3.25, w0=(485,'kJ/mol'), E0=(175.575,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C_N-4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 259,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000936334,'m^3/(mol*s)'), n=3.09886, w0=(353.5,'kJ/mol'), E0=(69.4048,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 260,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH",
    kinetics = ArrheniusBM(A=(3.84196e-06,'m^3/(mol*s)'), n=3.49798, w0=(353.5,'kJ/mol'), E0=(56.4557,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.54733577033311, var=3.882517426944977, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH
    Total Standard Deviation in ln(k): 7.837929306881217"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 7.837929306881217""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 7.837929306881217
""",
)

entry(
    index = 261,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH",
    kinetics = Arrhenius(A=(0.00188279,'m^3/(mol*s)'), n=2.80199, Ea=(22.9797,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=4.73600691749923e-16, var=0.13958961150199875, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH',), comment="""BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH
    Total Standard Deviation in ln(k): 0.7490029680824501"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 0.7490029680824501""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH
Total Standard Deviation in ln(k): 0.7490029680824501
""",
)

entry(
    index = 262,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.000211362,'m^3/(mol*s)'), n=3.09043, w0=(353.5,'kJ/mol'), E0=(111.923,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0038107431948011636, var=1.0722663488170394, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 2.085483807954196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.085483807954196""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 2.085483807954196
""",
)

entry(
    index = 263,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.296927,'m^3/(mol*s)'), n=2.14524, w0=(353.5,'kJ/mol'), E0=(124.445,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.006604255366205997, var=0.2118708156893044, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 0.9393616769526077"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R
Total Standard Deviation in ln(k): 0.9393616769526077""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R
Total Standard Deviation in ln(k): 0.9393616769526077
""",
)

entry(
    index = 264,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_5R!H->O",
    kinetics = ArrheniusBM(A=(0.002697,'m^3/(mol*s)'), n=2.63489, w0=(353.5,'kJ/mol'), E0=(82.3497,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 265,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(0.02065,'m^3/(mol*s)'), n=2.64, w0=(353.5,'kJ/mol'), E0=(99.8313,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_N-Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 266,
    label = "Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R",
    kinetics = ArrheniusBM(A=(0.00185843,'m^3/(mol*s)'), n=3.22261, w0=(353.5,'kJ/mol'), E0=(119.68,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_3R->O_1BrCClFHINPSSi-u0_Ext-1BrCClFHINPSSi-R_N-Sp-4R!H#1BrBrBrCCCClClClFFFHHHIIINNNPPPSSSSiSiSi_N-4R!H->F_N-Sp-4BrCCCClClClFHINOOPSSi=1BrBrCCCCClClClClFFHHIINNOOPPSSSiSi_3O-u1_N-4CClO->Cl_Ext-4CO-R_Ext-4CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 267,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.42161e-06,'m^3/(mol*s)'), n=3.86841, w0=(525,'kJ/mol'), E0=(163.125,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.41486138459508337, var=5.691383831211721, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C
    Total Standard Deviation in ln(k): 5.824985856486633"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C
Total Standard Deviation in ln(k): 5.824985856486633""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C
Total Standard Deviation in ln(k): 5.824985856486633
""",
)

entry(
    index = 268,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.00402118,'m^3/(mol*s)'), n=3.10034, w0=(525,'kJ/mol'), E0=(178.333,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08508954654125693, var=0.39720517041396236, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_N-6R!H->C
    Total Standard Deviation in ln(k): 1.4772613802801813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.4772613802801813""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_N-6R!H->C
Total Standard Deviation in ln(k): 1.4772613802801813
""",
)

entry(
    index = 269,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.45641e-12,'m^3/(mol*s)'), n=4.72226, w0=(525,'kJ/mol'), E0=(161.06,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5528808129554397, var=8.70129443499065, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R
    Total Standard Deviation in ln(k): 7.302706601732126"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R
Total Standard Deviation in ln(k): 7.302706601732126""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R
Total Standard Deviation in ln(k): 7.302706601732126
""",
)

entry(
    index = 270,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C",
    kinetics = Arrhenius(A=(1.65359e-14,'m^3/(mol*s)'), n=5.65246, Ea=(171.372,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 271,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.76419e-08,'m^3/(mol*s)'), n=3.82916, w0=(525,'kJ/mol'), E0=(174.017,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12119844424491734, var=1.1399486738098006, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 2.444941847991148"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.444941847991148""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C
Total Standard Deviation in ln(k): 2.444941847991148
""",
)

entry(
    index = 272,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O",
    kinetics = ArrheniusBM(A=(3.11488e-10,'m^3/(mol*s)'), n=4.50478, w0=(525,'kJ/mol'), E0=(139.949,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6312385292942233, var=0.5298110164819361, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O
    Total Standard Deviation in ln(k): 3.045235395133315"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 3.045235395133315""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 3.045235395133315
""",
)

entry(
    index = 273,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->O",
    kinetics = Arrhenius(A=(5.00048e-45,'m^3/(mol*s)'), n=14.5269, Ea=(79.3637,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 274,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(2.0018e-06,'m^3/(mol*s)'), n=3.59463, w0=(485,'kJ/mol'), E0=(184.963,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07127624793996981, var=7.212346077028083, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C
    Total Standard Deviation in ln(k): 5.562964771179898"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 5.562964771179898""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C
Total Standard Deviation in ln(k): 5.562964771179898
""",
)

entry(
    index = 275,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.000112377,'m^3/(mol*s)'), n=3.34717, w0=(485,'kJ/mol'), E0=(193.047,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11649469106514121, var=6.542463158001412, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 5.420459544326922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 5.420459544326922""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C
Total Standard Deviation in ln(k): 5.420459544326922
""",
)

entry(
    index = 276,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F",
    kinetics = ArrheniusBM(A=(8.07217e-08,'m^3/(mol*s)'), n=4.09577, w0=(485,'kJ/mol'), E0=(171.561,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1655518040696462, var=1.1972657364618726, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F
    Total Standard Deviation in ln(k): 2.609533188159146"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F
Total Standard Deviation in ln(k): 2.609533188159146""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F
Total Standard Deviation in ln(k): 2.609533188159146
""",
)

entry(
    index = 277,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F",
    kinetics = ArrheniusBM(A=(8.39475e-08,'m^3/(mol*s)'), n=4.02792, w0=(485,'kJ/mol'), E0=(170.508,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02802009624664621, var=0.06812965722815455, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F
    Total Standard Deviation in ln(k): 0.5936713540060956"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F
Total Standard Deviation in ln(k): 0.5936713540060956""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F
Total Standard Deviation in ln(k): 0.5936713540060956
""",
)

entry(
    index = 278,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O",
    kinetics = ArrheniusBM(A=(6.78271e-07,'m^3/(mol*s)'), n=3.84344, w0=(485,'kJ/mol'), E0=(181.257,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18844179925228297, var=1.324387256172609, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O
    Total Standard Deviation in ln(k): 2.7805615876520835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O
Total Standard Deviation in ln(k): 2.7805615876520835""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O
Total Standard Deviation in ln(k): 2.7805615876520835
""",
)

entry(
    index = 279,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->O",
    kinetics = ArrheniusBM(A=(5.7299e-06,'m^3/(mol*s)'), n=3.76087, w0=(485,'kJ/mol'), E0=(180.492,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 280,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C",
    kinetics = ArrheniusBM(A=(18908.5,'m^3/(mol*s)'), n=0.81744, w0=(485,'kJ/mol'), E0=(176.149,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5132741930501487, var=34.97113585052325, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C
    Total Standard Deviation in ln(k): 13.144914821215234"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 13.144914821215234""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C
Total Standard Deviation in ln(k): 13.144914821215234
""",
)

entry(
    index = 281,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.0158688,'m^3/(mol*s)'), n=2.79422, w0=(485,'kJ/mol'), E0=(172.35,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.15750843404517775, var=8.5683853241071, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C
    Total Standard Deviation in ln(k): 6.263971138772201"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 6.263971138772201""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C
Total Standard Deviation in ln(k): 6.263971138772201
""",
)

entry(
    index = 282,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C",
    kinetics = ArrheniusBM(A=(3.19591e-10,'m^3/(mol*s)'), n=4.92231, w0=(485,'kJ/mol'), E0=(166.297,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 283,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.29256e-09,'m^3/(mol*s)'), n=4.72835, w0=(485,'kJ/mol'), E0=(166.942,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-3C-R_N-Sp-4R!H=3C_Ext-3C-R_4R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 284,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R",
    kinetics = ArrheniusBM(A=(4.11983e-05,'m^3/(mol*s)'), n=3.20075, w0=(353.5,'kJ/mol'), E0=(86.0782,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_Sp-5R!H-3CClFH_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 285,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R",
    kinetics = ArrheniusBM(A=(0.00425626,'m^3/(mol*s)'), n=2.65728, w0=(353.5,'kJ/mol'), E0=(143.351,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_4BrCFINOPSSi->C_Ext-3CClFH-R_N-Sp-5R!H-3CClFH_Ext-1O-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 286,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.00442,'m^3/(mol*s)'), n=2.67, w0=(353.5,'kJ/mol'), E0=(124.435,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 287,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->O",
    kinetics = ArrheniusBM(A=(0.00765,'m^3/(mol*s)'), n=2.68, w0=(353.5,'kJ/mol'), E0=(125.05,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 288,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(0.00705,'m^3/(mol*s)'), n=2.66, w0=(353.5,'kJ/mol'), E0=(109.14,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_Ext-1O-R_Ext-3CClFH-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 289,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R_Ext-3CClFH-R",
    kinetics = ArrheniusBM(A=(0.00175,'m^3/(mol*s)'), n=2.74, w0=(353.5,'kJ/mol'), E0=(102.532,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R_Ext-3CClFH-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R_Ext-3CClFH-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R_Ext-3CClFH-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 290,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R_5R!H->O",
    kinetics = ArrheniusBM(A=(0.00303,'m^3/(mol*s)'), n=2.77, w0=(353.5,'kJ/mol'), E0=(124.009,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 291,
    label = "Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(0.00212,'m^3/(mol*s)'), n=2.75, w0=(353.5,'kJ/mol'), E0=(115.497,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->O_N-3R->O_1O-u0_3CClFH-u1_Ext-3CClFH-R_N-4R!H->Cl_N-Sp-4BrBrBrCCCCCClClFFFFFHHIIINNNOOOPPPSSSSiSiSi#3BrBrBrCCCCCCClClClFFFFFFHHHIIINNNOOOPPPSSSSiSiSi_Sp-4BrCFINOPSSi-3BrCCClFFHINOPSSi_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3CClFH-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 292,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(0.00141277,'m^3/(mol*s)'), n=2.88157, w0=(525,'kJ/mol'), E0=(171.476,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.42210879601893136, var=24.14527302708228, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 10.911409976907741"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 10.911409976907741""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 10.911409976907741
""",
)

entry(
    index = 293,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(6.10667e-09,'m^3/(mol*s)'), n=4.67466, w0=(525,'kJ/mol'), E0=(156.356,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4438403302429515, var=1.1880731948002283, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 3.30031329322498"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 3.30031329322498""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 3.30031329322498
""",
)

entry(
    index = 294,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(9.77854e-10,'m^3/(mol*s)'), n=3.7989, w0=(525,'kJ/mol'), E0=(168.767,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5227374995623516, var=47.32046836774433, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 15.103958245331878"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 15.103958245331878""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 15.103958245331878
""",
)

entry(
    index = 295,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_N-5R!H->C",
    kinetics = Arrhenius(A=(8.55352e-15,'m^3/(mol*s)'), n=5.47489, Ea=(178.942,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-2.6430257528455813e-15, var=1.2028998380513876, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 2.1987290914740947"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.1987290914740947""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 2.1987290914740947
""",
)

entry(
    index = 296,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O",
    kinetics = ArrheniusBM(A=(7.33133e-11,'m^3/(mol*s)'), n=4.61882, w0=(525,'kJ/mol'), E0=(163.129,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_4FO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 297,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O",
    kinetics = ArrheniusBM(A=(1.95847e-08,'m^3/(mol*s)'), n=3.80315, w0=(525,'kJ/mol'), E0=(174.726,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27233996320061055, var=0.5147314000071954, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O
    Total Standard Deviation in ln(k): 2.1225641110218754"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 2.1225641110218754""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O
Total Standard Deviation in ln(k): 2.1225641110218754
""",
)

entry(
    index = 298,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O_Sp-4O-3C",
    kinetics = ArrheniusBM(A=(1.10502e-10,'m^3/(mol*s)'), n=4.61742, w0=(525,'kJ/mol'), E0=(137.152,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O_Sp-4O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O_Sp-4O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O_Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O_Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 299,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O_N-Sp-4O-3C",
    kinetics = ArrheniusBM(A=(2.93442e-08,'m^3/(mol*s)'), n=4.04113, w0=(525,'kJ/mol'), E0=(155.17,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O_N-Sp-4O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O_N-Sp-4O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O_N-Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_N-4BrCFINOPSSi->C_4FO->O_N-Sp-4O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 300,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.58883e-06,'m^3/(mol*s)'), n=3.55742, w0=(485,'kJ/mol'), E0=(187.883,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05890870598558351, var=7.3507010726739095, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 5.583284922501438"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 5.583284922501438""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 5.583284922501438
""",
)

entry(
    index = 301,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C",
    kinetics = ArrheniusBM(A=(2.5027e-05,'m^3/(mol*s)'), n=3.59925, w0=(485,'kJ/mol'), E0=(178.513,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Sp-4C=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 302,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C",
    kinetics = ArrheniusBM(A=(1.59331e-06,'m^3/(mol*s)'), n=3.65749, w0=(485,'kJ/mol'), E0=(166.464,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.1815956553119347, var=7.038092624430188, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C
    Total Standard Deviation in ln(k): 10.79983874351861"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C
Total Standard Deviation in ln(k): 10.79983874351861""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C
Total Standard Deviation in ln(k): 10.79983874351861
""",
)

entry(
    index = 303,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O",
    kinetics = ArrheniusBM(A=(0.16178,'m^3/(mol*s)'), n=2.43248, w0=(485,'kJ/mol'), E0=(190.562,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2894535009314266, var=26.574338000377328, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O
    Total Standard Deviation in ln(k): 11.061740288205078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O
Total Standard Deviation in ln(k): 11.061740288205078""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O
Total Standard Deviation in ln(k): 11.061740288205078
""",
)

entry(
    index = 304,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O",
    kinetics = ArrheniusBM(A=(7.52263e-05,'m^3/(mol*s)'), n=3.39773, w0=(485,'kJ/mol'), E0=(193.259,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09250275042822766, var=6.906895104070973, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O
    Total Standard Deviation in ln(k): 5.501057695204191"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O
Total Standard Deviation in ln(k): 5.501057695204191""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O
Total Standard Deviation in ln(k): 5.501057695204191
""",
)

entry(
    index = 305,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.17543e-08,'m^3/(mol*s)'), n=4.12767, w0=(485,'kJ/mol'), E0=(171.42,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17797986955583806, var=1.2172289884104004, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 2.6589717441261294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 2.6589717441261294""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 2.6589717441261294
""",
)

entry(
    index = 306,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(8.34353e-08,'m^3/(mol*s)'), n=4.02818, w0=(485,'kJ/mol'), E0=(170.502,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02698394112529595, var=0.0626350540818045, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 0.5695238194983124"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 0.5695238194983124""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 0.5695238194983124
""",
)

entry(
    index = 307,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->O",
    kinetics = ArrheniusBM(A=(5.29538e-06,'m^3/(mol*s)'), n=3.74, w0=(485,'kJ/mol'), E0=(173.466,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_4CO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 308,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->O",
    kinetics = ArrheniusBM(A=(3.39606e-06,'m^3/(mol*s)'), n=3.80021, w0=(485,'kJ/mol'), E0=(174.472,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2499361162926204, var=0.047641473097659884, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->O
    Total Standard Deviation in ln(k): 1.0655522483929576"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->O
Total Standard Deviation in ln(k): 1.0655522483929576""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->O
Total Standard Deviation in ln(k): 1.0655522483929576
""",
)

entry(
    index = 309,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.22395e-07,'m^3/(mol*s)'), n=3.97282, w0=(485,'kJ/mol'), E0=(180.817,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7406508227715416, var=2.810420050104228, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R
    Total Standard Deviation in ln(k): 5.221731239208402"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 5.221731239208402""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 5.221731239208402
""",
)

entry(
    index = 310,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.0092079,'m^3/(mol*s)'), n=2.80941, w0=(485,'kJ/mol'), E0=(151.694,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.33265691981176837, var=4.254857720679727, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 4.971049889141961"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.971049889141961""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 4.971049889141961
""",
)

entry(
    index = 311,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.71639e-05,'m^3/(mol*s)'), n=3.56319, w0=(485,'kJ/mol'), E0=(152.498,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_N-4R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 312,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(0.104833,'m^3/(mol*s)'), n=2.12, w0=(525,'kJ/mol'), E0=(177.905,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 313,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(0.001275,'m^3/(mol*s)'), n=3.12, w0=(525,'kJ/mol'), E0=(169.6,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_3CClFH->H_N-1CClH->Cl_Ext-1CH-R_4R!H->F_Ext-1CH-R_5R!H->F_Ext-1CH-R_6R!H->C_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 314,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(5.44367e-08,'m^3/(mol*s)'), n=2.98637, w0=(525,'kJ/mol'), E0=(175.514,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 315,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(6.71872e-09,'m^3/(mol*s)'), n=3.87148, w0=(525,'kJ/mol'), E0=(168.449,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-4BrCFINOPSSi-R_Ext-3C-R_5R!H->C_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 316,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.84546e-08,'m^3/(mol*s)'), n=3.73033, w0=(525,'kJ/mol'), E0=(177.279,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7733021379689478, var=0.39722531548039053, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 3.2064707849561476"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 3.2064707849561476""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_1CClH->H_Ext-3C-R_N-4R!H->Cl_Ext-3C-R_N-4BrCFINOPSSi->C_N-4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 3.2064707849561476
""",
)

entry(
    index = 317,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.68723e-05,'m^3/(mol*s)'), n=2.95314, w0=(485,'kJ/mol'), E0=(193.721,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0030046029818399877, var=14.743691214756408, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C
    Total Standard Deviation in ln(k): 7.705233678445653"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C
Total Standard Deviation in ln(k): 7.705233678445653""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C
Total Standard Deviation in ln(k): 7.705233678445653
""",
)

entry(
    index = 318,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(8.96821e-07,'m^3/(mol*s)'), n=3.83775, w0=(485,'kJ/mol'), E0=(185.213,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07754259022967674, var=1.7540564002424495, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 2.8499176894052165"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C
Total Standard Deviation in ln(k): 2.8499176894052165""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C
Total Standard Deviation in ln(k): 2.8499176894052165
""",
)

entry(
    index = 319,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.5333e-06,'m^3/(mol*s)'), n=3.65941, w0=(485,'kJ/mol'), E0=(166.429,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 320,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C",
    kinetics = ArrheniusBM(A=(1.21333e-05,'m^3/(mol*s)'), n=3.66599, w0=(485,'kJ/mol'), E0=(168.262,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 321,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.38922e-05,'m^3/(mol*s)'), n=3.5758, w0=(485,'kJ/mol'), E0=(168.916,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_N-Sp-4C=1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 322,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00331206,'m^3/(mol*s)'), n=2.81802, w0=(485,'kJ/mol'), E0=(196.029,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 323,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.13872e-05,'m^3/(mol*s)'), n=3.55176, w0=(485,'kJ/mol'), E0=(193.142,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02778356663965037, var=7.287454974231614, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 5.481647749084141"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 5.481647749084141""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R
Total Standard Deviation in ln(k): 5.481647749084141
""",
)

entry(
    index = 324,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.839925,'m^3/(mol*s)'), n=2.36463, w0=(485,'kJ/mol'), E0=(184.976,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 325,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.73445e-08,'m^3/(mol*s)'), n=4.20668, w0=(485,'kJ/mol'), E0=(169.253,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16996406794972516, var=1.1819908294519843, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 2.606581377612547"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 2.606581377612547""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 2.606581377612547
""",
)

entry(
    index = 326,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.84564e-07,'m^3/(mol*s)'), n=3.87954, w0=(485,'kJ/mol'), E0=(178.087,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9426494231411795, var=6.577083312728128, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 7.5097743500714635"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 7.5097743500714635""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 7.5097743500714635
""",
)

entry(
    index = 327,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O",
    kinetics = ArrheniusBM(A=(6.28296e-08,'m^3/(mol*s)'), n=4.04865, w0=(485,'kJ/mol'), E0=(170.739,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07071074993195803, var=0.23643663206652124, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O
    Total Standard Deviation in ln(k): 1.1524626220495908"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O
Total Standard Deviation in ln(k): 1.1524626220495908""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O
Total Standard Deviation in ln(k): 1.1524626220495908
""",
)

entry(
    index = 328,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O",
    kinetics = ArrheniusBM(A=(1.00712e-07,'m^3/(mol*s)'), n=4.01588, w0=(485,'kJ/mol'), E0=(170.299,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.10014952363021072, var=0.02295701392788906, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O
    Total Standard Deviation in ln(k): 0.5553808510259662"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O
Total Standard Deviation in ln(k): 0.5553808510259662""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O
Total Standard Deviation in ln(k): 0.5553808510259662
""",
)

entry(
    index = 329,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->O_Ext-4C-R",
    kinetics = ArrheniusBM(A=(4.51365e-06,'m^3/(mol*s)'), n=3.78897, w0=(485,'kJ/mol'), E0=(175.572,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->O_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->O_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->O_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_N-4CO->O_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 330,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.63e-05,'m^3/(mol*s)'), n=3.37, w0=(485,'kJ/mol'), E0=(197.415,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 331,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(3.56033e-08,'m^3/(mol*s)'), n=4.21745, w0=(485,'kJ/mol'), E0=(177.011,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 332,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2.58576e-05,'m^3/(mol*s)'), n=3.2457, w0=(485,'kJ/mol'), E0=(186.26,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_N-Sp-4R!H-1C_4R!H->O_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 333,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(4.47723e-05,'m^3/(mol*s)'), n=3.46134, w0=(485,'kJ/mol'), E0=(152.048,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 334,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.5032e-05,'m^3/(mol*s)'), n=3.5135, w0=(485,'kJ/mol'), E0=(138.997,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_N-1C-u0_Sp-4R!H-1C_4R!H->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 335,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.000145249,'m^3/(mol*s)'), n=2.84864, w0=(485,'kJ/mol'), E0=(194.031,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_7R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 336,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->O",
    kinetics = ArrheniusBM(A=(2.47232e-06,'m^3/(mol*s)'), n=3.97637, w0=(485,'kJ/mol'), E0=(194.828,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 337,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O",
    kinetics = ArrheniusBM(A=(4.86924e-07,'m^3/(mol*s)'), n=3.84755, w0=(485,'kJ/mol'), E0=(182.435,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09600916366896428, var=2.0878678437696117, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O
    Total Standard Deviation in ln(k): 3.1379622231005637"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O
Total Standard Deviation in ln(k): 3.1379622231005637""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O
Total Standard Deviation in ln(k): 3.1379622231005637
""",
)

entry(
    index = 338,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(1.50053e-05,'m^3/(mol*s)'), n=3.79284, w0=(485,'kJ/mol'), E0=(187.083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005088750932892984, var=2.137679533398564, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O
    Total Standard Deviation in ln(k): 2.9438699700405464"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O
Total Standard Deviation in ln(k): 2.9438699700405464""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O
Total Standard Deviation in ln(k): 2.9438699700405464
""",
)

entry(
    index = 339,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(7.70505e-06,'m^3/(mol*s)'), n=3.51763, w0=(485,'kJ/mol'), E0=(196.685,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0495939191877359, var=1.7912645495126294, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 2.8077078101376474"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O
Total Standard Deviation in ln(k): 2.8077078101376474""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O
Total Standard Deviation in ln(k): 2.8077078101376474
""",
)

entry(
    index = 340,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.63939e-08,'m^3/(mol*s)'), n=4.20067, w0=(485,'kJ/mol'), E0=(170.79,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22661832906729848, var=4.962422799104255, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 5.035240106288135"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.035240106288135""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 5.035240106288135
""",
)

entry(
    index = 341,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.43185e-08,'m^3/(mol*s)'), n=4.29567, w0=(485,'kJ/mol'), E0=(166.374,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14352505810455957, var=0.3600922451326591, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 1.5636108663242947"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 1.5636108663242947""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 1.5636108663242947
""",
)

entry(
    index = 342,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C",
    kinetics = ArrheniusBM(A=(5.94509e-05,'m^3/(mol*s)'), n=3.37621, w0=(485,'kJ/mol'), E0=(190.622,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14501143760180155, var=0.5353198014536468, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C
    Total Standard Deviation in ln(k): 1.8311258333110456"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 1.8311258333110456""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 1.8311258333110456
""",
)

entry(
    index = 343,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C",
    kinetics = ArrheniusBM(A=(2.46705e-07,'m^3/(mol*s)'), n=4.01497, w0=(485,'kJ/mol'), E0=(174.93,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.847640744505439, var=15.359050530710228, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C
    Total Standard Deviation in ln(k): 12.498995403598462"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 12.498995403598462""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C
Total Standard Deviation in ln(k): 12.498995403598462
""",
)

entry(
    index = 344,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.02769e-08,'m^3/(mol*s)'), n=4.09467, w0=(485,'kJ/mol'), E0=(170.981,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1344579195349329, var=0.5134742245781719, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O_Ext-3C-R
    Total Standard Deviation in ln(k): 1.7743693047131486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O_Ext-3C-R
Total Standard Deviation in ln(k): 1.7743693047131486""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O_Ext-3C-R
Total Standard Deviation in ln(k): 1.7743693047131486
""",
)

entry(
    index = 345,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_5R!H->O",
    kinetics = ArrheniusBM(A=(9.11574e-08,'m^3/(mol*s)'), n=4.14961, w0=(485,'kJ/mol'), E0=(177.038,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 346,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1.04194e-07,'m^3/(mol*s)'), n=3.9712, w0=(485,'kJ/mol'), E0=(168.055,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1234180432834245, var=0.03795975830797721, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O
    Total Standard Deviation in ln(k): 0.7006834173627307"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O
Total Standard Deviation in ln(k): 0.7006834173627307""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O
Total Standard Deviation in ln(k): 0.7006834173627307
""",
)

entry(
    index = 347,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_Sp-6R!H=4C",
    kinetics = ArrheniusBM(A=(3.8501e-07,'m^3/(mol*s)'), n=3.92844, w0=(485,'kJ/mol'), E0=(191.208,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_Sp-6R!H=4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_Sp-6R!H=4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_Sp-6R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_Sp-6R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 348,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C",
    kinetics = ArrheniusBM(A=(9.19497e-07,'m^3/(mol*s)'), n=3.75122, w0=(485,'kJ/mol'), E0=(180.122,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16931575465283877, var=3.51591493297969, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C
    Total Standard Deviation in ln(k): 4.184449732912665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C
Total Standard Deviation in ln(k): 4.184449732912665""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C
Total Standard Deviation in ln(k): 4.184449732912665
""",
)

entry(
    index = 349,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.68364e-05,'m^3/(mol*s)'), n=3.9376, w0=(485,'kJ/mol'), E0=(195.002,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 350,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C",
    kinetics = ArrheniusBM(A=(2.28891e-06,'m^3/(mol*s)'), n=3.82239, w0=(485,'kJ/mol'), E0=(176.853,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_Sp-6O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 351,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C",
    kinetics = ArrheniusBM(A=(0.00168439,'m^3/(mol*s)'), n=3.12619, w0=(485,'kJ/mol'), E0=(197.881,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_6R!H->O_N-Sp-6O-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 352,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(1.43033e-06,'m^3/(mol*s)'), n=3.73989, w0=(485,'kJ/mol'), E0=(195.288,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.029338637895179966, var=3.73188578337298, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 3.9464803168381457"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 3.9464803168381457""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 3.9464803168381457
""",
)

entry(
    index = 353,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(0.00139188,'m^3/(mol*s)'), n=2.83127, w0=(485,'kJ/mol'), E0=(200.974,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13039194749268868, var=3.223254338261695, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 3.9268038465422546"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 3.9268038465422546""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 3.9268038465422546
""",
)

entry(
    index = 354,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.31087e-08,'m^3/(mol*s)'), n=4.12499, w0=(485,'kJ/mol'), E0=(171.382,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 355,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.14559e-08,'m^3/(mol*s)'), n=4.27069, w0=(485,'kJ/mol'), E0=(170.247,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-3C-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 356,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.45985e-08,'m^3/(mol*s)'), n=4.20193, w0=(485,'kJ/mol'), E0=(166.436,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 357,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(6.21207e-09,'m^3/(mol*s)'), n=4.38354, w0=(485,'kJ/mol'), E0=(166.362,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 358,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0001135,'m^3/(mol*s)'), n=3.32, w0=(485,'kJ/mol'), E0=(195.165,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 359,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.05889e-05,'m^3/(mol*s)'), n=3.30617, w0=(485,'kJ/mol'), E0=(194.249,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2144316870556855, var=0.08400851638092163, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 1.1198299618386702"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 1.1198299618386702""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R
Total Standard Deviation in ln(k): 1.1198299618386702
""",
)

entry(
    index = 360,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(4.11856e-08,'m^3/(mol*s)'), n=4.0381, w0=(485,'kJ/mol'), E0=(165.871,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 361,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(6.32707e-08,'m^3/(mol*s)'), n=4.09227, w0=(485,'kJ/mol'), E0=(176.621,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_4CO->O_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 362,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O_Ext-4C-R",
    kinetics = ArrheniusBM(A=(9.11391e-08,'m^3/(mol*s)'), n=3.97251, w0=(485,'kJ/mol'), E0=(166.8,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12852274226468294, var=0.1318692368220644, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O_Ext-4C-R
    Total Standard Deviation in ln(k): 1.0509170317075407"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 1.0509170317075407""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O_Ext-4C-R
Total Standard Deviation in ln(k): 1.0509170317075407
""",
)

entry(
    index = 363,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.83125e-07,'m^3/(mol*s)'), n=3.8806, w0=(485,'kJ/mol'), E0=(197.6,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 364,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_6R!H->C",
    kinetics = ArrheniusBM(A=(6.55056e-06,'m^3/(mol*s)'), n=3.42741, w0=(485,'kJ/mol'), E0=(172.504,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 365,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.50479e-07,'m^3/(mol*s)'), n=3.85832, w0=(485,'kJ/mol'), E0=(171.028,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_4R!H->C_Ext-4C-R_Ext-3C-R_N-7R!H->C_N-5R!H->O_N-Sp-6R!H=4C_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 366,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(5.76532e-06,'m^3/(mol*s)'), n=3.58647, w0=(485,'kJ/mol'), E0=(192.053,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 367,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.00057e-07,'m^3/(mol*s)'), n=4.05084, w0=(485,'kJ/mol'), E0=(197.154,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 368,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(0.00676365,'m^3/(mol*s)'), n=2.69434, w0=(485,'kJ/mol'), E0=(203.157,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19203964514781294, var=11.520881032749609, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 7.287068342570391"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.287068342570391""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 7.287068342570391
""",
)

entry(
    index = 369,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.96e-05,'m^3/(mol*s)'), n=3.23, w0=(485,'kJ/mol'), E0=(204.744,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 370,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.915e-05,'m^3/(mol*s)'), n=3.31, w0=(485,'kJ/mol'), E0=(197.747,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_4R!H->F_Ext-3C-R_N-5R!H->C_N-Sp-5BrBrClClFFIINNOOPPSSSiSi=3C_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 371,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O_Ext-4C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(7.80562e-08,'m^3/(mol*s)'), n=3.96948, w0=(485,'kJ/mol'), E0=(166.513,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O_Ext-4C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O_Ext-4C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 372,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O_Ext-4C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.03271e-07,'m^3/(mol*s)'), n=3.97927, w0=(485,'kJ/mol'), E0=(167.054,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O_Ext-4C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O_Ext-4C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Sp-4R!H-1C_N-4R!H->F_Ext-3C-R_N-4CO->O_N-5R!H->O_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 373,
    label = "Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.000284922,'m^3/(mol*s)'), n=3.00496, w0=(485,'kJ/mol'), E0=(205.158,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->O_N-3R->O_N-1BrCClFHINPSSi->F_N-3CClFH->H_3CClF->C_3C-u1_N-1CClH->H_Ext-1C-R_1C-u0_Ext-1C-R_N-4R!H->C_N-4FO->O_Ext-3C-R_N-6R!H->O_N-6BrCClFINPSSi->C_Ext-1C-R_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

