#!/usr/bin/env python
# encoding: utf-8

name = "Lactone_Formation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = Arrhenius(A=(3.78157e+09,'s^-1'), n=0.978824, Ea=(255.875,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=1.852433568953098e-15, var=85.39031335855428, Tref=1000.0, N=17, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 17 training reactions at node Root
    Total Standard Deviation in ln(k): 18.525131225896594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root
Total Standard Deviation in ln(k): 18.525131225896594""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root
Total Standard Deviation in ln(k): 18.525131225896594
""",
)

entry(
    index = 2,
    label = "Root_6F1sH->F1s",
    kinetics = ArrheniusBM(A=(5.05581e+10,'s^-1'), n=0.672063, w0=(933.5,'kJ/mol'), E0=(130.293,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13904807618260803, var=4.96027607415999, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_6F1sH->F1s',), comment="""BM rule fitted to 12 training reactions at node Root_6F1sH->F1s
    Total Standard Deviation in ln(k): 4.814248286627204"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_6F1sH->F1s
Total Standard Deviation in ln(k): 4.814248286627204""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_6F1sH->F1s
Total Standard Deviation in ln(k): 4.814248286627204
""",
)

entry(
    index = 3,
    label = "Root_N-6F1sH->F1s",
    kinetics = Arrhenius(A=(227460,'s^-1'), n=2.15, Ea=(336.615,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-3.5990137911088763e-16, var=90.82325827284195, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-6F1sH->F1s',), comment="""BM rule fitted to 5 training reactions at node Root_N-6F1sH->F1s
    Total Standard Deviation in ln(k): 19.105373329622687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-6F1sH->F1s
Total Standard Deviation in ln(k): 19.105373329622687""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-6F1sH->F1s
Total Standard Deviation in ln(k): 19.105373329622687
""",
)

entry(
    index = 4,
    label = "Root_6F1sH->F1s_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.58801e+10,'s^-1'), n=0.689585, w0=(933.5,'kJ/mol'), E0=(130.505,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.12650344998242044, var=5.532942723532014, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R',), comment="""BM rule fitted to 11 training reactions at node Root_6F1sH->F1s_Ext-3C-R
    Total Standard Deviation in ln(k): 5.033427425270659"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 5.033427425270659""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 5.033427425270659
""",
)

entry(
    index = 5,
    label = "Root_N-6F1sH->F1s_Ext-3C-R",
    kinetics = Arrhenius(A=(627251,'s^-1'), n=1.995, Ea=(319.29,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-2.6992603433316573e-15, var=89.06593733433054, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R
    Total Standard Deviation in ln(k): 18.919637488778502"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 18.919637488778502""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R
Total Standard Deviation in ln(k): 18.919637488778502
""",
)

entry(
    index = 6,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F",
    kinetics = ArrheniusBM(A=(2.22705e+12,'s^-1'), n=0.153067, w0=(933.5,'kJ/mol'), E0=(140.535,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.40475197454840955, var=2.223344349161128, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F',), comment="""BM rule fitted to 7 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F
    Total Standard Deviation in ln(k): 4.006201799354788"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F
Total Standard Deviation in ln(k): 4.006201799354788""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F
Total Standard Deviation in ln(k): 4.006201799354788
""",
)

entry(
    index = 7,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F",
    kinetics = ArrheniusBM(A=(1.30181e+17,'s^-1'), n=-1.06577, w0=(933.5,'kJ/mol'), E0=(138.296,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1186456967201272, var=5.555683734266318, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F
    Total Standard Deviation in ln(k): 5.023365168045757"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F
Total Standard Deviation in ln(k): 5.023365168045757""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F
Total Standard Deviation in ln(k): 5.023365168045757
""",
)

entry(
    index = 8,
    label = "Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(9.28596e+06,'s^-1'), n=1.585, w0=(830,'kJ/mol'), E0=(140.482,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.4470804825027292, var=0.05056132405561579, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 4.08666223823912"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 4.08666223823912""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 4.08666223823912
""",
)

entry(
    index = 9,
    label = "Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(26400,'s^-1'), n=2.44, w0=(830,'kJ/mol'), E0=(222.708,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(2.92779e+11,'s^-1'), n=0.414685, w0=(933.5,'kJ/mol'), E0=(141.825,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4416677496764747, var=0.9456241550195754, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C
    Total Standard Deviation in ln(k): 3.0591866701249932"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C
Total Standard Deviation in ln(k): 3.0591866701249932""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C
Total Standard Deviation in ln(k): 3.0591866701249932
""",
)

entry(
    index = 11,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(3.19e+11,'s^-1'), n=0.34, w0=(933.5,'kJ/mol'), E0=(115.347,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.97608e+14,'s^-1'), n=-0.206667, w0=(933.5,'kJ/mol'), E0=(140.966,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2909360012636315, var=3.5250112540777248, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 4.494887757453772"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 4.494887757453772""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 4.494887757453772
""",
)

entry(
    index = 13,
    label = "Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R",
    kinetics = ArrheniusBM(A=(1.17e+07,'s^-1'), n=1.55, w0=(830,'kJ/mol'), E0=(139.599,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-6F1sH->F1s_Ext-3C-R_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(1.94789e+11,'s^-1'), n=0.477128, w0=(933.5,'kJ/mol'), E0=(139.931,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.48744136220869094, var=0.8574589311291656, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 3.081093245753886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 3.081093245753886""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 3.081093245753886
""",
)

entry(
    index = 15,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(4.465e+10,'s^-1'), n=0.59, w0=(933.5,'kJ/mol'), E0=(146.646,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C",
    kinetics = ArrheniusBM(A=(2.07045e+15,'s^-1'), n=-0.52, w0=(933.5,'kJ/mol'), E0=(147.81,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28872017741727024, var=4.058128093565714, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C
    Total Standard Deviation in ln(k): 4.763925515556063"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C
Total Standard Deviation in ln(k): 4.763925515556063""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C
Total Standard Deviation in ln(k): 4.763925515556063
""",
)

entry(
    index = 17,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(1.8e+12,'s^-1'), n=0.42, w0=(933.5,'kJ/mol'), E0=(127.157,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C",
    kinetics = ArrheniusBM(A=(7.67806e+10,'s^-1'), n=0.611871, w0=(933.5,'kJ/mol'), E0=(136.938,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5640920362918141, var=0.46888698422914693, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
    Total Standard Deviation in ln(k): 2.790065491054413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 2.790065491054413""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 2.790065491054413
""",
)

entry(
    index = 19,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(5.3e+09,'s^-1'), n=0.85, w0=(933.5,'kJ/mol'), E0=(143.216,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C",
    kinetics = ArrheniusBM(A=(7.78e+15,'s^-1'), n=-0.84, w0=(933.5,'kJ/mol'), E0=(133.712,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C",
    kinetics = ArrheniusBM(A=(5.51e+14,'s^-1'), n=-0.2, w0=(933.5,'kJ/mol'), E0=(161.772,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_N-7R!H->F_Ext-3C-R_Ext-8R!H-R_Ext-9R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C",
    kinetics = ArrheniusBM(A=(3.77794e+11,'s^-1'), n=0.398137, w0=(933.5,'kJ/mol'), E0=(135.689,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6695155114419925, var=0.513121543956572, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
    Total Standard Deviation in ln(k): 3.118241685444911"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 3.118241685444911""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 3.118241685444911
""",
)

entry(
    index = 23,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C",
    kinetics = ArrheniusBM(A=(3.66e+07,'s^-1'), n=1.61, w0=(933.5,'kJ/mol'), E0=(137.287,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C",
    kinetics = ArrheniusBM(A=(1.49479e+11,'s^-1'), n=0.513313, w0=(933.5,'kJ/mol'), E0=(131.681,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8508919403261412, var=0.9936358957727015, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C
    Total Standard Deviation in ln(k): 4.136265172106331"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C
Total Standard Deviation in ln(k): 4.136265172106331""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C
Total Standard Deviation in ln(k): 4.136265172106331
""",
)

entry(
    index = 25,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C",
    kinetics = ArrheniusBM(A=(3.35e+10,'s^-1'), n=0.7, w0=(933.5,'kJ/mol'), E0=(138.531,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_N-12R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C",
    kinetics = ArrheniusBM(A=(1.59e+10,'s^-1'), n=0.8, w0=(933.5,'kJ/mol'), E0=(126.028,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C",
    kinetics = ArrheniusBM(A=(1.045e+11,'s^-1'), n=0.55, w0=(933.5,'kJ/mol'), E0=(134.118,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_6F1sH->F1s_Ext-3C-R_7R!H->F_Ext-3C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C_Ext-11C-R_12R!H->C_Ext-12C-R_N-13R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

