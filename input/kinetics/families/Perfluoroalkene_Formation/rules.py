#!/usr/bin/env python
# encoding: utf-8

name = "Perfluoroalkene_Formation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.41036,'s^-1'), n=3.62459, w0=(749,'kJ/mol'), E0=(309.023,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.42144634924479984, var=138.50201478194117, Tref=1000.0, N=6, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 6 training reactions at node Root
    Total Standard Deviation in ln(k): 24.65201186427234"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root
Total Standard Deviation in ln(k): 24.65201186427234""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root
Total Standard Deviation in ln(k): 24.65201186427234
""",
)

entry(
    index = 2,
    label = "Root_5R->O",
    kinetics = ArrheniusBM(A=(5.55854e+07,'s^-1'), n=1.15094, w0=(749,'kJ/mol'), E0=(261.364,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4462386572555851, var=16.45716623877578, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_5R->O',), comment="""BM rule fitted to 4 training reactions at node Root_5R->O
    Total Standard Deviation in ln(k): 9.253898258978065"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_5R->O
Total Standard Deviation in ln(k): 9.253898258978065""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_5R->O
Total Standard Deviation in ln(k): 9.253898258978065
""",
)

entry(
    index = 3,
    label = "Root_N-5R->O",
    kinetics = Arrhenius(A=(2.45719e-13,'s^-1'), n=7.875, Ea=(470.656,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=196.83678475308452, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->O
    Total Standard Deviation in ln(k): 28.126139122191674"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->O
Total Standard Deviation in ln(k): 28.126139122191674""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->O
Total Standard Deviation in ln(k): 28.126139122191674
""",
)

entry(
    index = 4,
    label = "Root_5R->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.23968e+11,'s^-1'), n=0.122083, w0=(786,'kJ/mol'), E0=(284.282,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5717287601531608, var=61.314256936670986, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_5R->O_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_5R->O_Ext-2C-R
    Total Standard Deviation in ln(k): 17.134265838662174"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_5R->O_Ext-2C-R
Total Standard Deviation in ln(k): 17.134265838662174""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_5R->O_Ext-2C-R
Total Standard Deviation in ln(k): 17.134265838662174
""",
)

entry(
    index = 5,
    label = "Root_5R->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(206500,'s^-1'), n=1.73, w0=(712,'kJ/mol'), E0=(228.001,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_5R->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5R->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5R->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_N-5R->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.33333e+09,'s^-1'), n=1.49, w0=(786,'kJ/mol'), E0=(495.651,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_5R->O_Ext-2C-R_Ext-3C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1.23e+06,'s^-1'), n=1.56, w0=(786,'kJ/mol'), E0=(289.945,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R->O_Ext-2C-R_Ext-3C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_5R->O_Ext-2C-R_Ext-3C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5R->O_Ext-2C-R_Ext-3C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5R->O_Ext-2C-R_Ext-3C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_5R->O_Ext-2C-R_Ext-3C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(6.23333e+07,'s^-1'), n=1.21, w0=(786,'kJ/mol'), E0=(256.218,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R->O_Ext-2C-R_Ext-3C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_5R->O_Ext-2C-R_Ext-3C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5R->O_Ext-2C-R_Ext-3C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5R->O_Ext-2C-R_Ext-3C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

