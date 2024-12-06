#!/usr/bin/env python
# encoding: utf-8

name = "1,3_sigmatropic_rearrangement/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.30791e+26,'s^-1'), n=-3.67984, w0=(664000,'J/mol'), E0=(247189,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4163866947181062, var=128.1927359939506, Tref=1000.0, N=20, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 20 training reactions at node Root
    Total Standard Deviation in ln(k): 23.74425553407489"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root
Total Standard Deviation in ln(k): 23.74425553407489""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root
Total Standard Deviation in ln(k): 23.74425553407489
""",
)

entry(
    index = 2,
    label = "Root_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.07986e-21,'s^-1'), n=9.62589, w0=(636417,'J/mol'), E0=(33022,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3571800124903484, var=28.092031200167057, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R
    Total Standard Deviation in ln(k): 14.035480087290036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R
Total Standard Deviation in ln(k): 14.035480087290036""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R!H-R
Total Standard Deviation in ln(k): 14.035480087290036
""",
)

entry(
    index = 3,
    label = "Root_1R!H-inRing",
    kinetics = ArrheniusBM(A=(5.95588e+67,'s^-1'), n=-15.1817, w0=(654062,'J/mol'), E0=(403939,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5544159323717395, var=269.88167642966965, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R!H-inRing',), comment="""BM rule fitted to 8 training reactions at node Root_1R!H-inRing
    Total Standard Deviation in ln(k): 36.83950759794208"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 36.83950759794208""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R!H-inRing
Total Standard Deviation in ln(k): 36.83950759794208
""",
)

entry(
    index = 4,
    label = "Root_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(1.58597e+12,'s^-1'), n=0.0440307, w0=(704833,'J/mol'), E0=(136609,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.06241320838115143, var=8.945969542406907, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R!H-inRing',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing
    Total Standard Deviation in ln(k): 6.152942370306084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 6.152942370306084""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R!H-inRing
Total Standard Deviation in ln(k): 6.152942370306084
""",
)

entry(
    index = 5,
    label = "Root_Ext-2R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.91531e-14,'s^-1'), n=7.49565, w0=(624125,'J/mol'), E0=(13825.8,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8129505795286808, var=3.6728302512857196, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 5.88458990276278"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_5R!H->C
Total Standard Deviation in ln(k): 5.88458990276278""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-2R!H-R_5R!H->C
Total Standard Deviation in ln(k): 5.88458990276278
""",
)

entry(
    index = 6,
    label = "Root_Ext-2R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.48161e-36,'s^-1'), n=13.8864, w0=(661000,'J/mol'), E0=(11036.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=8.649252153480784, var=28.6187499376758, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 32.45641936565119"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 32.45641936565119""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 32.45641936565119
""",
)

entry(
    index = 7,
    label = "Root_1R!H-inRing_2R!H->N",
    kinetics = ArrheniusBM(A=(2.50818e+88,'s^-1'), n=-21.0628, w0=(638000,'J/mol'), E0=(484196,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.168561953451146, var=422.3137326737107, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
    Total Standard Deviation in ln(k): 51.671627485424715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 51.671627485424715""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_2R!H->N
Total Standard Deviation in ln(k): 51.671627485424715
""",
)

entry(
    index = 8,
    label = "Root_1R!H-inRing_N-2R!H->N",
    kinetics = ArrheniusBM(A=(4.09681e+60,'s^-1'), n=-13.1585, w0=(670125,'J/mol'), E0=(360582,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.5668157718817215, var=547.8562761169217, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N',), comment="""BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
    Total Standard Deviation in ln(k): 50.860213488451016"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 50.860213488451016""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R!H-inRing_N-2R!H->N
Total Standard Deviation in ln(k): 50.860213488451016
""",
)

entry(
    index = 9,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(7.50839e+11,'s^-1'), n=0.136197, w0=(707000,'J/mol'), E0=(134212,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01703312323488117, var=1.3519057502930525, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R
    Total Standard Deviation in ln(k): 2.373731974677581"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.373731974677581""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R
Total Standard Deviation in ln(k): 2.373731974677581
""",
)

entry(
    index = 10,
    label = "Root_N-1R!H-inRing_2R!H->C",
    kinetics = ArrheniusBM(A=(0.00257114,'s^-1'), n=4.34785, w0=(700500,'J/mol'), E0=(369438,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C
Total Standard Deviation in ln(k): 48.62918961607295""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_2R!H->N_4R!H->C_2N-inRing_N-3R!H->N_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_N-1R!H-inRing_N-2R!H->C",
    kinetics = ArrheniusBM(A=(7040,'s^-1'), n=2.66, w0=(700500,'J/mol'), E0=(384026,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H->C_N-1C-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R
Total Standard Deviation in ln(k): 69.54052263328794""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_Ext-3CO-R_Ext-4C-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(9.97305e-124,'s^-1'), n=38.6249, w0=(710.728,'kJ/mol'), E0=(-39.1433,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.357064565186675, var=274.40677911565723, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R
    Total Standard Deviation in ln(k): 41.64372925318938"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 41.64372925318938""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 41.64372925318938
""",
)

entry(
    index = 50,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(8.21122e+11,'s^-1'), n=-0.0143805, w0=(700.5,'kJ/mol'), E0=(274.543,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6207405736219249, var=351.89209664433315, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R
    Total Standard Deviation in ln(k): 39.16604836119211"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 39.16604836119211""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R
Total Standard Deviation in ln(k): 39.16604836119211
""",
)

entry(
    index = 51,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F_Ext-2CO-R",
    kinetics = ArrheniusBM(A=(1.69499e+12,'s^-1'), n=0.570599, w0=(741,'kJ/mol'), E0=(311.809,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F_Ext-2CO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F_Ext-2CO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_4BrClF->F_Ext-2CO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R",
    kinetics = ArrheniusBM(A=(9.28368e+11,'s^-1'), n=0.384751, w0=(562,'kJ/mol'), E0=(218.281,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11545916601888881, var=15.400657637499883, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R
    Total Standard Deviation in ln(k): 8.157414917229724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R
Total Standard Deviation in ln(k): 8.157414917229724""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R
Total Standard Deviation in ln(k): 8.157414917229724
""",
)

entry(
    index = 53,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_4BrCl->Cl",
    kinetics = ArrheniusBM(A=(1.69656e+11,'s^-1'), n=0.593389, w0=(583,'kJ/mol'), E0=(230.439,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_4BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_4BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_N-4BrCl->Cl",
    kinetics = ArrheniusBM(A=(2.5058e+11,'s^-1'), n=0.533491, w0=(541,'kJ/mol'), E0=(206.698,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_N-4BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_N-4BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_N-4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_N-4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C",
    kinetics = ArrheniusBM(A=(2.39834e-43,'s^-1'), n=15.6472, w0=(808.892,'kJ/mol'), E0=(282.345,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.413224139712793, var=151.6362425968821, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C
    Total Standard Deviation in ln(k): 28.23725619810417"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C
Total Standard Deviation in ln(k): 28.23725619810417""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C
Total Standard Deviation in ln(k): 28.23725619810417
""",
)

entry(
    index = 56,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_N-Sp-5R!H-4C",
    kinetics = ArrheniusBM(A=(1.575e+06,'s^-1'), n=1.45, w0=(700.5,'kJ/mol'), E0=(212.781,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_N-Sp-5R!H-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_N-Sp-5R!H-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_N-Sp-5R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_N-Sp-5R!H-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.36187e+16,'s^-1'), n=-1.17746, w0=(700.5,'kJ/mol'), E0=(343.057,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.93207e+11,'s^-1'), n=-0.056024, w0=(700.5,'kJ/mol'), E0=(216.564,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_N-2CO->C_Ext-4C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_4BrCl->Cl",
    kinetics = ArrheniusBM(A=(1.046e+12,'s^-1'), n=0.380659, w0=(583,'kJ/mol'), E0=(230.604,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_4BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_4BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_N-4BrCl->Cl",
    kinetics = ArrheniusBM(A=(1.94657e+12,'s^-1'), n=0.28187, w0=(541,'kJ/mol'), E0=(206.892,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_N-4BrCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_N-4BrCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_N-4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_N-4R!H->C_N-4BrClF->F_Ext-2CO-R_N-4BrCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(4.27634e-17,'s^-1'), n=8.17123, w0=(860.57,'kJ/mol'), E0=(386.289,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.3040681658067679, var=151.69969300022254, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 27.968159292647"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R
Total Standard Deviation in ln(k): 27.968159292647""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R
Total Standard Deviation in ln(k): 27.968159292647
""",
)

entry(
    index = 62,
    label = "Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(7.89e+07,'s^-1'), n=1.5, w0=(911.88,'kJ/mol'), E0=(423.493,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_N-2R!H->N_N-3R!H->N_4R!H->C_2CO->C_Ext-4C-R_Sp-5R!H-4C_Ext-1R!H-R_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_Ext-2R!H-R_5R!H->C_4R!H->N",
    kinetics = ArrheniusBM(A=(7.88104e+10,'s^-1'), n=0.444174, w0=(559500,'J/mol'), E0=(121694,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_4R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_4R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_Ext-2R!H-R_5R!H->C_N-4R!H->N",
    kinetics = ArrheniusBM(A=(1.84746e-16,'s^-1'), n=8.14258, w0=(645667,'J/mol'), E0=(64566.7,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7487509793916722, var=1.4587138791120244, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_N-4R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N
    Total Standard Deviation in ln(k): 4.3025473220224155"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N
Total Standard Deviation in ln(k): 4.3025473220224155""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N
Total Standard Deviation in ln(k): 4.3025473220224155
""",
)

entry(
    index = 14,
    label = "Root_Ext-2R!H-R_N-5R!H->C_3R!H->N",
    kinetics = ArrheniusBM(A=(3.19239e+10,'s^-1'), n=0.633646, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C_3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->N",
    kinetics = ArrheniusBM(A=(7.16673e+09,'s^-1'), n=0.77465, w0=(707000,'J/mol'), E0=(194100,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_N-5R!H->C_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_1R!H-inRing_2R!H->N_3R!H->N",
    kinetics = ArrheniusBM(A=(7.79562e-25,'s^-1'), n=11.2893, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0768327727097848, var=36.91907930296372, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_3R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N
    Total Standard Deviation in ln(k): 14.886595318028107"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N
Total Standard Deviation in ln(k): 14.886595318028107""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N
Total Standard Deviation in ln(k): 14.886595318028107
""",
)

entry(
    index = 17,
    label = "Root_1R!H-inRing_2R!H->N_N-3R!H->N",
    kinetics = ArrheniusBM(A=(1.14287e+10,'s^-1'), n=1.07105, w0=(707000,'J/mol'), E0=(428529,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_N-3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_1R!H-inRing_N-2R!H->N_4R!H->N",
    kinetics = ArrheniusBM(A=(3.23202e+11,'s^-1'), n=0.959257, w0=(559500,'J/mol'), E0=(116309,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_4R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_4R!H->N
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
    index = 19,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N",
    kinetics = ArrheniusBM(A=(5.17463e+69,'s^-1'), n=-15.7846, w0=(707000,'J/mol'), E0=(419904,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.6020204647519467, var=752.2013288923092, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N
    Total Standard Deviation in ln(k): 59.0076206693908"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 59.0076206693908""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N
Total Standard Deviation in ln(k): 59.0076206693908
""",
)

entry(
    index = 20,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N",
    kinetics = ArrheniusBM(A=(7.42118e+12,'s^-1'), n=-0.057127, w0=(707000,'J/mol'), E0=(136643,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.010222737318967457, var=0.4833412136116934, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N
    Total Standard Deviation in ln(k): 1.4194321346238945"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N
Total Standard Deviation in ln(k): 1.4194321346238945""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N
Total Standard Deviation in ln(k): 1.4194321346238945
""",
)

entry(
    index = 21,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N",
    kinetics = ArrheniusBM(A=(7.42131e+10,'s^-1'), n=0.332427, w0=(707000,'J/mol'), E0=(131754,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0006044627176402661, var=1.3355604139234127, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N
    Total Standard Deviation in ln(k): 2.318319891761889"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N
Total Standard Deviation in ln(k): 2.318319891761889""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N
Total Standard Deviation in ln(k): 2.318319891761889
""",
)

entry(
    index = 22,
    label = "Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(9.35695e+11,'s^-1'), n=0.214198, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_3R!H->N",
    kinetics = ArrheniusBM(A=(9.61405e+11,'s^-1'), n=0.233577, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_N-3R!H->N",
    kinetics = ArrheniusBM(A=(3.83567e+11,'s^-1'), n=0.27432, w0=(707000,'J/mol'), E0=(70700,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_N-3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_N-3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R!H-R_5R!H->C_N-4R!H->N_N-3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.55603e-17,'s^-1'), n=9.13956, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=7.73338536715972, var=0.32655979383658124, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C
    Total Standard Deviation in ln(k): 20.576230589316168"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 20.576230589316168""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C
Total Standard Deviation in ln(k): 20.576230589316168
""",
)

entry(
    index = 26,
    label = "Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3.92014e+10,'s^-1'), n=1.31782, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.61854e+10,'s^-1'), n=0.947053, w0=(707000,'J/mol'), E0=(429654,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-1R!H-R
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
    index = 28,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.42792e+11,'s^-1'), n=1.12171, w0=(707000,'J/mol'), E0=(70700,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_5R!H->C
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
    index = 29,
    label = "Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.48935e+10,'s^-1'), n=1.24936, w0=(707000,'J/mol'), E0=(189635,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_N-2R!H->N_N-4R!H->N_Ext-4C-R_N-5R!H->C
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
    index = 30,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.00957e+13,'s^-1'), n=-0.120785, w0=(707000,'J/mol'), E0=(137481,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_2R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(1.84315e+12,'s^-1'), n=-0.0912511, w0=(707000,'J/mol'), E0=(137560,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R!H-inRing_Ext-4R!H-R_N-2R!H->N_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R",
    kinetics = ArrheniusBM(A=(8.04681e+10,'s^-1'), n=1.21369, w0=(615000,'J/mol'), E0=(61500,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R!H-inRing_2R!H->N_3R!H->N_Ext-4R!H-R_5R!H->C_Ext-1R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

