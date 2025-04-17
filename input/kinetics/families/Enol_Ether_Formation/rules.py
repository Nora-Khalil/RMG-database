#!/usr/bin/env python
# encoding: utf-8

name = "Enol_Ether_Formation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.97366e+20,'s^-1'), n=-2.35923, w0=(803.9,'kJ/mol'), E0=(307.75,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.16412588009088758, var=10.34295692324268, Tref=1000.0, N=5, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 5 training reactions at node Root
    Total Standard Deviation in ln(k): 6.859698383552445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root
Total Standard Deviation in ln(k): 6.859698383552445""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root
Total Standard Deviation in ln(k): 6.859698383552445
""",
)

entry(
    index = 2,
    label = "Root_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.21706e+08,'s^-1'), n=1.19767, w0=(833.5,'kJ/mol'), E0=(286.717,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05997385471225133, var=0.32494273902965326, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2C-R
    Total Standard Deviation in ln(k): 1.2934622270832161"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2C-R
Total Standard Deviation in ln(k): 1.2934622270832161""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2C-R
Total Standard Deviation in ln(k): 1.2934622270832161
""",
)

entry(
    index = 3,
    label = "Root_Ext-3O-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(80.6667,'s^-1'), n=3.11, w0=(759.5,'kJ/mol'), E0=(232.176,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3O-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3O-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3O-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3O-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.15964e+08,'s^-1'), n=1.22, w0=(833.5,'kJ/mol'), E0=(289.567,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.07569027970350209, var=0.14841472880861026, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 0.9624933978250596"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_7R!H->C
Total Standard Deviation in ln(k): 0.9624933978250596""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_7R!H->C
Total Standard Deviation in ln(k): 0.9624933978250596
""",
)

entry(
    index = 5,
    label = "Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.30333e+09,'s^-1'), n=0.87, w0=(833.5,'kJ/mol'), E0=(283.664,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1.05333e+07,'s^-1'), n=1.56, w0=(833.5,'kJ/mol'), E0=(287.903,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.27667e+09,'s^-1'), n=0.88, w0=(833.5,'kJ/mol'), E0=(291.23,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2C-R_Ext-3O-R_Ext-6R!H-R_Ext-3O-R_Ext-7R!H-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

