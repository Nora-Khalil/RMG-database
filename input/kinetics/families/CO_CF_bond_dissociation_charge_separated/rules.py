#!/usr/bin/env python
# encoding: utf-8

name = "CO_CF_bond_dissociation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(5.24346e+06,'s^-1'), n=1.56068, w0=(1295.9,'kJ/mol'), E0=(222.045,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5531404791261569, var=11.78449687448429, Tref=1000.0, N=5, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 5 training reactions at node Root
    Total Standard Deviation in ln(k): 8.271766032541269"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root
Total Standard Deviation in ln(k): 8.271766032541269""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root
Total Standard Deviation in ln(k): 8.271766032541269
""",
)

entry(
    index = 2,
    label = "Root_4F1sH->F1s",
    kinetics = ArrheniusBM(A=(2.25432e+08,'s^-1'), n=1.05811, w0=(1325.5,'kJ/mol'), E0=(239.262,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7638894986512131, var=1.8618430159246833, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4F1sH->F1s',), comment="""BM rule fitted to 3 training reactions at node Root_4F1sH->F1s
    Total Standard Deviation in ln(k): 4.6547687012194086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4F1sH->F1s
Total Standard Deviation in ln(k): 4.6547687012194086""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4F1sH->F1s
Total Standard Deviation in ln(k): 4.6547687012194086
""",
)

entry(
    index = 3,
    label = "Root_N-4F1sH->F1s",
    kinetics = ArrheniusBM(A=(1.0623e+06,'s^-1'), n=1.81122, w0=(1251.5,'kJ/mol'), E0=(200.625,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2919554003484784, var=0.8530328773029784, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4F1sH->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-4F1sH->F1s
    Total Standard Deviation in ln(k): 2.585125168876151"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4F1sH->F1s
Total Standard Deviation in ln(k): 2.585125168876151""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4F1sH->F1s
Total Standard Deviation in ln(k): 2.585125168876151
""",
)

entry(
    index = 4,
    label = "Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(3.2617e+08,'s^-1'), n=0.994879, w0=(1325.5,'kJ/mol'), E0=(242.382,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8620833366700209, var=0.4917666130790975, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 3.5718805205195054"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_5R!H->C
Total Standard Deviation in ln(k): 3.5718805205195054""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_5R!H->C
Total Standard Deviation in ln(k): 3.5718805205195054
""",
)

entry(
    index = 5,
    label = "Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(8.1e+07,'s^-1'), n=1.22, w0=(1325.5,'kJ/mol'), E0=(232.709,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_N-4F1sH->F1s_Ext-3C-R_Ext-2C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(560000,'s^-1'), n=1.87, w0=(1251.5,'kJ/mol'), E0=(201.192,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4F1sH->F1s_Ext-3C-R_Ext-2C-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4F1sH->F1s_Ext-3C-R_Ext-2C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4F1sH->F1s_Ext-3C-R_Ext-2C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4F1sH->F1s_Ext-3C-R_Ext-2C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_5R!H->C_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.63e+08,'s^-1'), n=1.07, w0=(1325.5,'kJ/mol'), E0=(243.012,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_5R!H->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_5R!H->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_5R!H->C_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(7.65e+08,'s^-1'), n=0.9, w0=(1325.5,'kJ/mol'), E0=(241.925,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_5R!H->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_5R!H->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4F1sH->F1s_Ext-3C-R_Ext-5R!H-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

