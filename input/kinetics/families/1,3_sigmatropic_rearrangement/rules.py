#!/usr/bin/env python
# encoding: utf-8

name = "1,3_sigmatropic_rearrangement/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(7.62583e+17,'s^-1'), n=-1.3482, w0=(671.075,'kJ/mol'), E0=(296.677,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.25985372316562816, var=138.4495237325701, Tref=1000.0, N=40, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 40 training reactions at node Root
    Total Standard Deviation in ln(k): 24.24152902797637"""),
    rank = 11,
    shortDesc = """BM rule fitted to 40 training reactions at node Root
Total Standard Deviation in ln(k): 24.24152902797637""",
    longDesc = 
"""
BM rule fitted to 40 training reactions at node Root
Total Standard Deviation in ln(k): 24.24152902797637
""",
)

entry(
    index = 2,
    label = "Root_1R!H-inRing",
    kinetics = Arrhenius(A=(6.24446e+10,'s^-1'), n=1.24268, Ea=(377.896,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.2652782859367144e-16, var=94.78298575514019, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H-inRing',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H-inRing
    Total Standard Deviation in ln(k): 19.51740984963649"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 19.51740984963649""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 19.51740984963649
""",
)

entry(
    index = 3,
    label = "Root_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.49353e+12,'s^-1'), n=0.167256, w0=(675.328,'kJ/mol'), E0=(279.456,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.23479729137655592, var=139.94599847138903, Tref=1000.0, N=32, data_mean=0.0, correlation='Root_N-1R!H-inRing',), comment="""BM rule fitted to 32 training reactions at node Root_N-1R!H-inRing
    Total Standard Deviation in ln(k): 24.305713058081665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 32 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 24.305713058081665""",
    longDesc = 
"""
BM rule fitted to 32 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 24.305713058081665
""",
)

entry(
    index = 4,
    label = "Root_1R!H-inRing_2R!H->N",
    kinetics = ArrheniusBM(A=(3.43789e+29,'s^-1'), n=-4.07982, w0=(638,'kJ/mol'), E0=(383.138,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11727679289277122, var=88.81499227153824, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
    Total Standard Deviation in ln(k): 19.187630768227077"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 19.187630768227077""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 19.187630768227077
""",
)

entry(
    index = 5,
    label = "Root_1R!H-inRing_N-2R!H->N",
    kinetics = Arrhenius(A=(1.15312e+11,'s^-1'), n=1.11936, Ea=(326.147,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=2.024445257498743e-15, var=122.59631229248639, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
    Total Standard Deviation in ln(k): 22.19707210432194"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 22.19707210432194""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 22.19707210432194
""",
)

entry(
    index = 6,
    label = "Root_N-1R!H-inRing_2R!H->N",
    kinetics = Arrhenius(A=(4.41572e+12,'s^-1'), n=0.37672, Ea=(179.094,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=7.085558401245599e-16, var=70.29706821168217, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_2R!H->N
    Total Standard Deviation in ln(k): 16.808369855776906"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 16.808369855776906""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 16.808369855776906
""",
)

entry(
    index = 7,
    label = "Root_N-1R!H-inRing_N-2R!H->N",
    kinetics = ArrheniusBM(A=(37399,'s^-1'), n=2.21932, w0=(680.182,'kJ/mol'), E0=(282.823,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.012445031943407119, var=117.99878943142576, Tref=1000.0, N=22, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N',), comment="""BM rule fitted to 22 training reactions at node Root_N-1R!H-inRing_N-2R!H->N
    Total Standard Deviation in ln(k): 21.80815430722297"""),
    rank = 11,
    shortDesc = """BM rule fitted to 22 training reactions at node Root_N-1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 21.80815430722297""",
    longDesc = 
"""
BM rule fitted to 22 training reactions at node Root_N-1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 21.80815430722297
""",
)

entry(
    index = 8,
    label = "Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.02096e+24,'s^-1'), n=-2.59989, w0=(645.667,'kJ/mol'), E0=(390.108,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.007665487925580284, var=79.12297569832336, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 17.851598353978"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 17.851598353978""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 17.851598353978
""",
)

entry(
    index = 9,
    label = "Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(6.1544e+10,'s^-1'), n=1.34775, w0=(615,'kJ/mol'), E0=(272.121,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_1R!H-inRing_N-2R!H->N_4R!H->N",
    kinetics = ArrheniusBM(A=(4.0435e+11,'s^-1'), n=1.01704, w0=(559.5,'kJ/mol'), E0=(142.636,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_4R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N",
    kinetics = Arrhenius(A=(7.5901e+10,'s^-1'), n=1.15346, Ea=(353.925,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-3.3740754291645717e-15, var=65.13185752936086, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N
    Total Standard Deviation in ln(k): 16.17907624003862"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 16.17907624003862""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 16.17907624003862
""",
)

entry(
    index = 12,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C",
    kinetics = Arrhenius(A=(2.69041e+12,'s^-1'), n=0.443332, Ea=(190.827,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=2.136914438470895e-15, var=51.28388173357306, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C
    Total Standard Deviation in ln(k): 14.356462285826806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C
Total Standard Deviation in ln(k): 14.356462285826806""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C
Total Standard Deviation in ln(k): 14.356462285826806
""",
)

entry(
    index = 13,
    label = "Root_N-1R!H-inRing_2R!H->N_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.81632e+14,'s^-1'), n=-0.222789, w0=(559.5,'kJ/mol'), E0=(144.22,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->N",
    kinetics = ArrheniusBM(A=(3.75419e+11,'s^-1'), n=0.319312, w0=(707,'kJ/mol'), E0=(164.547,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19877057070932752, var=20.677741900160488, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N
    Total Standard Deviation in ln(k): 9.615512291779684"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N
Total Standard Deviation in ln(k): 9.615512291779684""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N
Total Standard Deviation in ln(k): 9.615512291779684
""",
)

entry(
    index = 15,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N",
    kinetics = ArrheniusBM(A=(156286,'s^-1'), n=2.02322, w0=(674.222,'kJ/mol'), E0=(307.578,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10366666465677646, var=73.21544399323605, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N
    Total Standard Deviation in ln(k): 17.414189906478633"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 17.414189906478633""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 17.414189906478633
""",
)

entry(
    index = 16,
    label = "Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.03859e+24,'s^-1'), n=-2.55197, w0=(661,'kJ/mol'), E0=(403.659,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21956710944033278, var=198.92006906735597, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 28.826264461491245"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 28.826264461491245""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 28.826264461491245
""",
)

entry(
    index = 17,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(2.1761e+10,'s^-1'), n=0.996245, w0=(707,'kJ/mol'), E0=(403.723,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.6259e+11,'s^-1'), n=1.19107, w0=(707,'kJ/mol'), E0=(254.322,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.23586e+11,'s^-1'), n=1.27308, w0=(707,'kJ/mol'), E0=(193.538,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R",
    kinetics = Arrhenius(A=(1.12483e+12,'s^-1'), n=0.514355, Ea=(216.937,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-5.061113143746858e-16, var=39.96748608377522, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 12.673903779177413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 12.673903779177413""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 12.673903779177413
""",
)

entry(
    index = 21,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing",
    kinetics = ArrheniusBM(A=(8.0616e+13,'s^-1'), n=0.109951, w0=(661,'kJ/mol'), E0=(263.087,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.40026673433751325, var=87.91033202747225, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing
    Total Standard Deviation in ln(k): 19.802193604569734"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing
Total Standard Deviation in ln(k): 19.802193604569734""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing
Total Standard Deviation in ln(k): 19.802193604569734
""",
)

entry(
    index = 22,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing",
    kinetics = ArrheniusBM(A=(6.58736e+08,'s^-1'), n=1.38338, w0=(707,'kJ/mol'), E0=(163.931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3190920317195911, var=56.5119977162676, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing
    Total Standard Deviation in ln(k): 15.872226908913033"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing
Total Standard Deviation in ln(k): 15.872226908913033""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing
Total Standard Deviation in ln(k): 15.872226908913033
""",
)

entry(
    index = 23,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N",
    kinetics = ArrheniusBM(A=(1.48372e+12,'s^-1'), n=0.181284, w0=(707,'kJ/mol'), E0=(188.93,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.19549948898845299, var=18.26774832479612, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N
    Total Standard Deviation in ln(k): 9.059600143716137"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N
Total Standard Deviation in ln(k): 9.059600143716137""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N
Total Standard Deviation in ln(k): 9.059600143716137
""",
)

entry(
    index = 24,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N",
    kinetics = ArrheniusBM(A=(7.47609e+10,'s^-1'), n=0.487141, w0=(707,'kJ/mol'), E0=(139.835,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.22804644275645197, var=23.772021230970356, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N
    Total Standard Deviation in ln(k): 10.347379579471236"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 10.347379579471236""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N
Total Standard Deviation in ln(k): 10.347379579471236
""",
)

entry(
    index = 25,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C",
    kinetics = ArrheniusBM(A=(5.31428e+06,'s^-1'), n=1.61759, w0=(661.083,'kJ/mol'), E0=(304.931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.43332429719187016, var=101.32008196400893, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C
    Total Standard Deviation in ln(k): 21.267992193627688"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C
Total Standard Deviation in ln(k): 21.267992193627688""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C
Total Standard Deviation in ln(k): 21.267992193627688
""",
)

entry(
    index = 26,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C",
    kinetics = ArrheniusBM(A=(3881.43,'s^-1'), n=2.4474, w0=(700.5,'kJ/mol'), E0=(310.521,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6012962809209815, var=99.03603528756301, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C
    Total Standard Deviation in ln(k): 21.46128676987773"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C
Total Standard Deviation in ln(k): 21.46128676987773""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C
Total Standard Deviation in ln(k): 21.46128676987773
""",
)

entry(
    index = 27,
    label = "Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->N",
    kinetics = ArrheniusBM(A=(1.04679e+11,'s^-1'), n=1.26667, w0=(615,'kJ/mol'), E0=(334.785,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->N",
    kinetics = ArrheniusBM(A=(1.37586e+09,'s^-1'), n=1.6158, w0=(707,'kJ/mol'), E0=(401.885,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_2N-inRing",
    kinetics = ArrheniusBM(A=(3.54394e+12,'s^-1'), n=0.452411, w0=(615,'kJ/mol'), E0=(336.068,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_2N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_2N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_N-2N-inRing",
    kinetics = ArrheniusBM(A=(3.57015e+11,'s^-1'), n=0.576299, w0=(707,'kJ/mol'), E0=(152.637,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_N-2N-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_N-2N-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_N-2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_Ext-1R!H-R_N-2N-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N",
    kinetics = ArrheniusBM(A=(5.66862e+16,'s^-1'), n=-0.814873, w0=(615,'kJ/mol'), E0=(311.721,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3842118872536021, var=56.55937128112604, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N
    Total Standard Deviation in ln(k): 16.042160049178467"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N
Total Standard Deviation in ln(k): 16.042160049178467""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N
Total Standard Deviation in ln(k): 16.042160049178467
""",
)

entry(
    index = 32,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N",
    kinetics = ArrheniusBM(A=(3.85259e+20,'s^-1'), n=-1.69467, w0=(707,'kJ/mol'), E0=(239.372,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5340962056458511, var=72.11369728605635, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N
    Total Standard Deviation in ln(k): 18.366117256919125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N
Total Standard Deviation in ln(k): 18.366117256919125""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N
Total Standard Deviation in ln(k): 18.366117256919125
""",
)

entry(
    index = 33,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N",
    kinetics = ArrheniusBM(A=(2.70202e+10,'s^-1'), n=0.86017, w0=(707,'kJ/mol'), E0=(186.64,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24949252742356204, var=32.25929115847389, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N
    Total Standard Deviation in ln(k): 12.013212246091811"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N
Total Standard Deviation in ln(k): 12.013212246091811""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N
Total Standard Deviation in ln(k): 12.013212246091811
""",
)

entry(
    index = 34,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_N-5R!H->N",
    kinetics = ArrheniusBM(A=(1.09588e+09,'s^-1'), n=1.44217, w0=(707,'kJ/mol'), E0=(127.072,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_N-5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_N-5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_N-5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_N-5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.74216e+12,'s^-1'), n=0.0183475, w0=(707,'kJ/mol'), E0=(176.462,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->N_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(9.74444e+12,'s^-1'), n=-0.195371, w0=(707,'kJ/mol'), E0=(155.613,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br",
    kinetics = ArrheniusBM(A=(6.98406e+11,'s^-1'), n=0.40768, w0=(541,'kJ/mol'), E0=(206.795,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005374602454955672, var=0.05576325998062374, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br
    Total Standard Deviation in ln(k): 0.4869070930049241"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br
Total Standard Deviation in ln(k): 0.4869070930049241""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br
Total Standard Deviation in ln(k): 0.4869070930049241
""",
)

entry(
    index = 38,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br",
    kinetics = ArrheniusBM(A=(1.58089e+07,'s^-1'), n=1.47583, w0=(685.1,'kJ/mol'), E0=(308.741,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3905131633662209, var=98.21980218770655, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br
    Total Standard Deviation in ln(k): 20.849297076484756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br
Total Standard Deviation in ln(k): 20.849297076484756""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br
Total Standard Deviation in ln(k): 20.849297076484756
""",
)

entry(
    index = 39,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(88.0296,'s^-1'), n=2.8262, w0=(700.5,'kJ/mol'), E0=(296.641,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6073086253794192, var=146.97885288396296, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 25.830273760087284"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 25.830273760087284""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 25.830273760087284
""",
)

entry(
    index = 40,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(5.01986e+12,'s^-1'), n=0.418833, w0=(615,'kJ/mol'), E0=(328.858,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(8.78669e+12,'s^-1'), n=0.204119, w0=(615,'kJ/mol'), E0=(273.65,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_3R!H->N_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(9.16767e+14,'s^-1'), n=-0.000952816, w0=(707,'kJ/mol'), E0=(256.163,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.03924e+16,'s^-1'), n=-0.601612, w0=(707,'kJ/mol'), E0=(196.261,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.88231e+11,'s^-1'), n=0.661449, w0=(707,'kJ/mol'), E0=(174.499,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_N-2N-inRing_Ext-4C-R_5R!H->N_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br_Ext-2CO-R",
    kinetics = ArrheniusBM(A=(1.94657e+12,'s^-1'), n=0.28187, w0=(541,'kJ/mol'), E0=(206.892,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br_Ext-2CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br_Ext-2CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_4R!H->Br_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl",
    kinetics = ArrheniusBM(A=(4.21261e+11,'s^-1'), n=0.487024, w0=(583,'kJ/mol'), E0=(230.521,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005445922515400975, var=0.10372712383064285, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl
    Total Standard Deviation in ln(k): 0.6593421453783316"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl
Total Standard Deviation in ln(k): 0.6593421453783316""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl
Total Standard Deviation in ln(k): 0.6593421453783316
""",
)

entry(
    index = 47,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl",
    kinetics = ArrheniusBM(A=(3.52682e+07,'s^-1'), n=1.36919, w0=(710.625,'kJ/mol'), E0=(311.775,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.34779624500056483, var=97.31677669386079, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl
    Total Standard Deviation in ln(k): 20.65042428983906"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl
Total Standard Deviation in ln(k): 20.65042428983906""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl
Total Standard Deviation in ln(k): 20.65042428983906
""",
)

entry(
    index = 48,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1.12329e+07,'s^-1'), n=1.41589, w0=(700.5,'kJ/mol'), E0=(340.757,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4309712583665733, var=124.36438977764455, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 23.43940397889382"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 23.43940397889382""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 23.43940397889382
""",
)

entry(
    index = 49,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1.575e+06,'s^-1'), n=1.45, w0=(700.5,'kJ/mol'), E0=(213.634,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl_Ext-2CO-R",
    kinetics = ArrheniusBM(A=(1.046e+12,'s^-1'), n=0.380659, w0=(583,'kJ/mol'), E0=(230.604,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl_Ext-2CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl_Ext-2CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_4CClF->Cl_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-2CO-R",
    kinetics = ArrheniusBM(A=(1.69499e+12,'s^-1'), n=0.570599, w0=(741,'kJ/mol'), E0=(311.809,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-2CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-2CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_2CO->C",
    kinetics = ArrheniusBM(A=(2.11883e+10,'s^-1'), n=0.811585, w0=(741,'kJ/mol'), E0=(311.115,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C",
    kinetics = ArrheniusBM(A=(2.22832e+07,'s^-1'), n=1.41656, w0=(700.5,'kJ/mol'), E0=(311.523,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3304165548111776, var=101.5170657913083, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C
    Total Standard Deviation in ln(k): 21.029036472346878"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C
Total Standard Deviation in ln(k): 21.029036472346878""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C
Total Standard Deviation in ln(k): 21.029036472346878
""",
)

entry(
    index = 54,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(3.42876e+06,'s^-1'), n=1.6089, w0=(700.5,'kJ/mol'), E0=(342.475,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22311928446129792, var=433.4532007343185, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R
    Total Standard Deviation in ln(k): 42.29826118018058"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 42.29826118018058""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R
Total Standard Deviation in ln(k): 42.29826118018058
""",
)

entry(
    index = 55,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R",
    kinetics = ArrheniusBM(A=(162442,'s^-1'), n=1.90885, w0=(700.5,'kJ/mol'), E0=(297.288,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.25011726673372126, var=153.21583306555183, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R
    Total Standard Deviation in ln(k): 25.443122986523573"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R
Total Standard Deviation in ln(k): 25.443122986523573""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R
Total Standard Deviation in ln(k): 25.443122986523573
""",
)

entry(
    index = 56,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(7.89e+07,'s^-1'), n=1.5, w0=(700.5,'kJ/mol'), E0=(423.772,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-3CO->C_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-1R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O",
    kinetics = ArrheniusBM(A=(814.378,'s^-1'), n=2.38084, w0=(700.5,'kJ/mol'), E0=(223.083,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.36117901058176244, var=117.41376442524769, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O
    Total Standard Deviation in ln(k): 22.630319556225153"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O
Total Standard Deviation in ln(k): 22.630319556225153""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O
Total Standard Deviation in ln(k): 22.630319556225153
""",
)

entry(
    index = 58,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(5.23853e+08,'s^-1'), n=1.09056, w0=(700.5,'kJ/mol'), E0=(374.429,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3940358245667629, var=173.63083761942892, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O
    Total Standard Deviation in ln(k): 27.406244356336003"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O
Total Standard Deviation in ln(k): 27.406244356336003""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O
Total Standard Deviation in ln(k): 27.406244356336003
""",
)

entry(
    index = 59,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(5.4394e+08,'s^-1'), n=0.631892, w0=(700.5,'kJ/mol'), E0=(265.587,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(8.67544e+08,'s^-1'), n=1.19995, w0=(700.5,'kJ/mol'), E0=(424.648,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_3CO->C_N-4R!H->Br_N-4CClF->Cl_N-2CO->C_Ext-4CF-R_N-5R!H->O_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

