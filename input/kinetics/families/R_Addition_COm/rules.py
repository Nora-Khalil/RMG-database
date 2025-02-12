#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_COm/rules"
shortDesc = ""
longDesc = """
.. [MRHCBSQB31DHR] M.R. Harper (mrharper_at_mit_dot_edu or michael_dot_harper_dot_jr_at_gmail_dot_com)
The geometries of all reactants, products, and the transition state were optimized using the CBS-QB3 method.
The zero-point energy is that computed by the CBS-QB3 calculations.  The frequencies were computed with B3LYP/CBSB7.
In computing k(T), an asymmetric tunneling correction was employed, the calculated frequencies were scaled by 0.99, and the 
temperatures used were from 600 K to 2000 K (in 200 K increments).
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(6.29556,'m^3/(mol*s)'), n=1.66134, w0=(309.26,'kJ/mol'), E0=(34.9876,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11587695774326513, var=2.2452394087902117, Tref=1000.0, N=25, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 25 training reactions at node Root
    Total Standard Deviation in ln(k): 3.295067825213994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root
Total Standard Deviation in ln(k): 3.295067825213994""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root
Total Standard Deviation in ln(k): 3.295067825213994
""",
)

entry(
    index = 2,
    label = "Root_3R->O",
    kinetics = ArrheniusBM(A=(34.1,'m^3/(mol*s)'), n=1.08616e-08, w0=(315.5,'kJ/mol'), E0=(36.9372,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-3R->O",
    kinetics = ArrheniusBM(A=(7.97917,'m^3/(mol*s)'), n=1.63265, w0=(309,'kJ/mol'), E0=(35.2551,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11174292439078873, var=2.1796560685714166, Tref=1000.0, N=24, data_mean=0.0, correlation='Root_N-3R->O',), comment="""BM rule fitted to 24 training reactions at node Root_N-3R->O
    Total Standard Deviation in ln(k): 3.2404834861363154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 3.2404834861363154""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 3.2404834861363154
""",
)

entry(
    index = 4,
    label = "Root_N-3R->O_3BrCClFHINPSSi-inRing",
    kinetics = ArrheniusBM(A=(2.98732e+12,'m^3/(mol*s)'), n=-1.83866, w0=(309.5,'kJ/mol'), E0=(88.3418,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7492643522316527, var=19.22517846662447, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing
    Total Standard Deviation in ln(k): 10.672640628777671"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing
Total Standard Deviation in ln(k): 10.672640628777671""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing
Total Standard Deviation in ln(k): 10.672640628777671
""",
)

entry(
    index = 5,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing",
    kinetics = ArrheniusBM(A=(70.5621,'m^3/(mol*s)'), n=1.36558, w0=(308.955,'kJ/mol'), E0=(37.173,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07479358444803016, var=1.8511619733966365, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing',), comment="""BM rule fitted to 22 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing
    Total Standard Deviation in ln(k): 2.9155142703146564"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing
Total Standard Deviation in ln(k): 2.9155142703146564""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing
Total Standard Deviation in ln(k): 2.9155142703146564
""",
)

entry(
    index = 6,
    label = "Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_4R!H->O",
    kinetics = ArrheniusBM(A=(0.00721,'m^3/(mol*s)'), n=2.333, w0=(309.5,'kJ/mol'), E0=(57.4773,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(1.48e+06,'m^3/(mol*s)'), n=-9.07899e-08, w0=(309.5,'kJ/mol'), E0=(55.6691,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_N-4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_N-4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi-inRing_Ext-3BrCClFHINPSSi-R_N-4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C",
    kinetics = ArrheniusBM(A=(82.6642,'m^3/(mol*s)'), n=1.34621, w0=(309.5,'kJ/mol'), E0=(37.4135,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07308513515084755, var=1.7913293764861609, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C',), comment="""BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C
    Total Standard Deviation in ln(k): 2.8667795169095367"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 2.8667795169095367""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 2.8667795169095367
""",
)

entry(
    index = 9,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C",
    kinetics = ArrheniusBM(A=(55.8514,'m^3/(mol*s)'), n=1.28151, w0=(307.1,'kJ/mol'), E0=(1.044,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06328150149896698, var=19.051457869329827, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C
    Total Standard Deviation in ln(k): 8.909261551491594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 8.909261551491594""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C
Total Standard Deviation in ln(k): 8.909261551491594
""",
)

entry(
    index = 10,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.0975522,'m^3/(mol*s)'), n=2.1272, w0=(309.5,'kJ/mol'), E0=(28.7802,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15060154103229048, var=1.1242738863912818, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R
    Total Standard Deviation in ln(k): 2.504052165279655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 2.504052165279655""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R
Total Standard Deviation in ln(k): 2.504052165279655
""",
)

entry(
    index = 11,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_3BrClHS->H",
    kinetics = ArrheniusBM(A=(108630,'m^3/(mol*s)'), n=-2.7391e-06, w0=(342,'kJ/mol'), E0=(42.0739,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2296595295004966, var=3.331278170672866, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_3BrClHS->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_3BrClHS->H
    Total Standard Deviation in ln(k): 4.236034241462012"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_3BrClHS->H
Total Standard Deviation in ln(k): 4.236034241462012""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_3BrClHS->H
Total Standard Deviation in ln(k): 4.236034241462012
""",
)

entry(
    index = 12,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H",
    kinetics = ArrheniusBM(A=(8419.86,'m^3/(mol*s)'), n=0.883532, w0=(283.833,'kJ/mol'), E0=(0.361281,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2546598720704877, var=15.318883907289857, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H
    Total Standard Deviation in ln(k): 8.48625087071034"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H
Total Standard Deviation in ln(k): 8.48625087071034""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H
Total Standard Deviation in ln(k): 8.48625087071034
""",
)

entry(
    index = 13,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(0.000102254,'m^3/(mol*s)'), n=2.95462, w0=(309.5,'kJ/mol'), E0=(24.6457,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.2741715754954765, var=13.94060942338895, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H=3C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H=3C
    Total Standard Deviation in ln(k): 15.711666270028696"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 15.711666270028696""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H=3C
Total Standard Deviation in ln(k): 15.711666270028696
""",
)

entry(
    index = 14,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C",
    kinetics = ArrheniusBM(A=(0.159164,'m^3/(mol*s)'), n=2.07023, w0=(309.5,'kJ/mol'), E0=(28.7921,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12693614321566082, var=1.309007783144315, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C
    Total Standard Deviation in ln(k): 2.61259008452317"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.61259008452317""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C
Total Standard Deviation in ln(k): 2.61259008452317
""",
)

entry(
    index = 15,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_3BrClS->S",
    kinetics = ArrheniusBM(A=(0.0785,'m^3/(mol*s)'), n=2.33, w0=(272.5,'kJ/mol'), E0=(17.2876,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_3BrClS->S',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_3BrClS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_3BrClS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_3BrClS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S",
    kinetics = ArrheniusBM(A=(2.15963e+08,'m^3/(mol*s)'), n=-0.382318, w0=(289.5,'kJ/mol'), E0=(1.07698,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21204009292314446, var=5.181763014014456, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S
    Total Standard Deviation in ln(k): 5.096239968118646"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S
Total Standard Deviation in ln(k): 5.096239968118646""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S
Total Standard Deviation in ln(k): 5.096239968118646
""",
)

entry(
    index = 17,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00292607,'m^3/(mol*s)'), n=2.53895, w0=(309.5,'kJ/mol'), E0=(28.4287,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_Sp-4R!H=3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C",
    kinetics = ArrheniusBM(A=(0.344935,'m^3/(mol*s)'), n=1.926, w0=(309.5,'kJ/mol'), E0=(28.9215,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11210723179104833, var=0.9530755689829208, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C',), comment="""BM rule fitted to 10 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
    Total Standard Deviation in ln(k): 2.2388108953718624"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 2.2388108953718624""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C
Total Standard Deviation in ln(k): 2.2388108953718624
""",
)

entry(
    index = 19,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C",
    kinetics = ArrheniusBM(A=(0.044717,'m^3/(mol*s)'), n=2.50145, w0=(309.5,'kJ/mol'), E0=(31.5754,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=-9.63129e-10, w0=(300,'kJ/mol'), E0=(8.34816,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl",
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_N-3BrCClFHINPSSi->C_N-3BrClHS->H_N-3BrClS->S_N-3BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(8.00026,'m^3/(mol*s)'), n=1.49535, w0=(309.5,'kJ/mol'), E0=(29.2407,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1328573251035702, var=1.2297000251801051, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 2.5568999956979166"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.5568999956979166""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.5568999956979166
""",
)

entry(
    index = 23,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(86.1,'m^3/(mol*s)'), n=1.36, w0=(309.5,'kJ/mol'), E0=(35.1189,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(0.00377485,'m^3/(mol*s)'), n=2.39679, w0=(309.5,'kJ/mol'), E0=(23.2264,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20471932392857392, var=1.0213668974866748, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O
    Total Standard Deviation in ln(k): 2.5404095223351244"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O
Total Standard Deviation in ln(k): 2.5404095223351244""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O
Total Standard Deviation in ln(k): 2.5404095223351244
""",
)

entry(
    index = 25,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(0.35789,'m^3/(mol*s)'), n=1.93149, w0=(309.5,'kJ/mol'), E0=(23.325,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.02721028527163593, var=1.462534236268213, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 2.492799564353115"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O
Total Standard Deviation in ln(k): 2.492799564353115""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O
Total Standard Deviation in ln(k): 2.492799564353115
""",
)

entry(
    index = 26,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00319398,'m^3/(mol*s)'), n=2.29874, w0=(309.5,'kJ/mol'), E0=(13.0203,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_5R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R",
    kinetics = ArrheniusBM(A=(0.0078093,'m^3/(mol*s)'), n=2.36815, w0=(309.5,'kJ/mol'), E0=(19.3816,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-5BrCClFINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.00120086,'m^3/(mol*s)'), n=2.6776, w0=(309.5,'kJ/mol'), E0=(14.7213,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi-inRing_3BrCClFHINPSSi->C_Ext-3C-R_N-Sp-4R!H=3C_4R!H->C_Ext-4C-R_N-5R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

