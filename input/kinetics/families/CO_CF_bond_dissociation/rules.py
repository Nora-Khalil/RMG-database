#!/usr/bin/env python
# encoding: utf-8

name = "CO_CF_bond_dissociation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.24181e+12,'s^-1'), n=0.0957629, w0=(859.833,'kJ/mol'), E0=(232.873,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6986852317502754, var=226.28346166140983, Tref=1000.0, N=24, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 24 training reactions at node Root
    Total Standard Deviation in ln(k): 31.912161418483702"""),
    rank = 11,
    shortDesc = """BM rule fitted to 24 training reactions at node Root
Total Standard Deviation in ln(k): 31.912161418483702""",
    longDesc = 
"""
BM rule fitted to 24 training reactions at node Root
Total Standard Deviation in ln(k): 31.912161418483702
""",
)

entry(
    index = 2,
    label = "Root_3C-u0",
    kinetics = ArrheniusBM(A=(6.92042e+10,'s^-1'), n=0.470996, w0=(854.9,'kJ/mol'), E0=(298.313,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7161723325609523, var=91.48909434035556, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_3C-u0',), comment="""BM rule fitted to 15 training reactions at node Root_3C-u0
    Total Standard Deviation in ln(k): 20.97470529400529"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_3C-u0
Total Standard Deviation in ln(k): 20.97470529400529""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_3C-u0
Total Standard Deviation in ln(k): 20.97470529400529
""",
)

entry(
    index = 3,
    label = "Root_N-3C-u0",
    kinetics = ArrheniusBM(A=(1.22938e+21,'s^-1'), n=-2.50646, w0=(868.056,'kJ/mol'), E0=(148.182,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.861177112590892, var=182.81173872456728, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3C-u0',), comment="""BM rule fitted to 9 training reactions at node Root_N-3C-u0
    Total Standard Deviation in ln(k): 29.269361834359714"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3C-u0
Total Standard Deviation in ln(k): 29.269361834359714""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3C-u0
Total Standard Deviation in ln(k): 29.269361834359714
""",
)

entry(
    index = 4,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.8836e+08,'s^-1'), n=1.25682, w0=(854.9,'kJ/mol'), E0=(341.338,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.751789119911982, var=20.614923106383515, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C',), comment="""BM rule fitted to 10 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C
    Total Standard Deviation in ln(k): 10.991148303219052"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 10.991148303219052""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 10.991148303219052
""",
)

entry(
    index = 5,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.721352,'s^-1'), n=3.52585, w0=(854.9,'kJ/mol'), E0=(181.284,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2512857078886634, var=31.377457158718897, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.861011854233412"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.861011854233412""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.861011854233412
""",
)

entry(
    index = 6,
    label = "Root_N-3C-u0_5R->O",
    kinetics = ArrheniusBM(A=(1442.74,'s^-1'), n=2.34038, w0=(884.5,'kJ/mol'), E0=(262.374,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3091352839065547, var=0.07250119342877608, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3C-u0_5R->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3C-u0_5R->O
    Total Standard Deviation in ln(k): 1.3165177009397602"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3C-u0_5R->O
Total Standard Deviation in ln(k): 1.3165177009397602""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3C-u0_5R->O
Total Standard Deviation in ln(k): 1.3165177009397602
""",
)

entry(
    index = 7,
    label = "Root_N-3C-u0_N-5R->O",
    kinetics = ArrheniusBM(A=(9.55205e+15,'s^-1'), n=-0.959491, w0=(863.357,'kJ/mol'), E0=(88.9182,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7733851733129872, var=5.2223486562196975, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-3C-u0_N-5R->O
    Total Standard Deviation in ln(k): 6.524491370261814"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3C-u0_N-5R->O
Total Standard Deviation in ln(k): 6.524491370261814""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3C-u0_N-5R->O
Total Standard Deviation in ln(k): 6.524491370261814
""",
)

entry(
    index = 8,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H",
    kinetics = ArrheniusBM(A=(5.3349e+06,'s^-1'), n=1.68732, w0=(810.5,'kJ/mol'), E0=(371.48,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.670660665159718, var=2.3730954652576832, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H',), comment="""BM rule fitted to 4 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H
    Total Standard Deviation in ln(k): 4.773342294337441"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 4.773342294337441""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 4.773342294337441
""",
)

entry(
    index = 9,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(2.5125e+09,'s^-1'), n=0.944844, w0=(884.5,'kJ/mol'), E0=(316.967,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.813880056941254, var=1.1586816683324892, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H',), comment="""BM rule fitted to 6 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H
    Total Standard Deviation in ln(k): 4.202863236479668"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 4.202863236479668""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 4.202863236479668
""",
)

entry(
    index = 10,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H",
    kinetics = ArrheniusBM(A=(1.26761e+06,'s^-1'), n=1.81828, w0=(810.5,'kJ/mol'), E0=(243.842,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.30118000642634235, var=0.07060990627683612, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H
    Total Standard Deviation in ln(k): 1.2894424057733311"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 1.2894424057733311""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 1.2894424057733311
""",
)

entry(
    index = 11,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(3.00433e+11,'s^-1'), n=0.142234, w0=(884.5,'kJ/mol'), E0=(179.422,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6178170784442248, var=0.4264676173996617, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H',), comment="""BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H
    Total Standard Deviation in ln(k): 2.8614861984768676"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 2.8614861984768676""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 2.8614861984768676
""",
)

entry(
    index = 12,
    label = "Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_7R!H->C",
    kinetics = ArrheniusBM(A=(5066.67,'s^-1'), n=2.17, w0=(884.5,'kJ/mol'), E0=(263.498,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(413.333,'s^-1'), n=2.51, w0=(884.5,'kJ/mol'), E0=(261.256,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_5R->O_Ext-5O-R_Ext-6R!H-R_Ext-6R!H-R_Ext-5O-R_Ext-7R!H-R_Ext-7R!H-R_Ext-5O-R_Ext-6R!H-R_Ext-7R!H-R_Ext-6R!H-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R",
    kinetics = ArrheniusBM(A=(8.03053e+17,'s^-1'), n=-1.6099, w0=(869.7,'kJ/mol'), E0=(87.2212,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.856205285497741, var=9.315169703698727, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R
    Total Standard Deviation in ln(k): 8.26987396678775"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R
Total Standard Deviation in ln(k): 8.26987396678775""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R
Total Standard Deviation in ln(k): 8.26987396678775
""",
)

entry(
    index = 15,
    label = "Root_N-3C-u0_N-5R->O_4F1sH->H",
    kinetics = ArrheniusBM(A=(2.78e+10,'s^-1'), n=0.74, w0=(810.5,'kJ/mol'), E0=(81.5934,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_4F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_4F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_4F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_4F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-3C-u0_N-5R->O_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(5.95e+09,'s^-1'), n=1.2, w0=(884.5,'kJ/mol'), E0=(99.0718,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_N-4F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_N-4F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_N-4F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_N-4F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C",
    kinetics = ArrheniusBM(A=(2.39757e+07,'s^-1'), n=1.55051, w0=(810.5,'kJ/mol'), E0=(376.445,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4330065775066264, var=15.076349500594018, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C
    Total Standard Deviation in ln(k): 8.871996740934037"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C
Total Standard Deviation in ln(k): 8.871996740934037""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C
Total Standard Deviation in ln(k): 8.871996740934037
""",
)

entry(
    index = 18,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C",
    kinetics = ArrheniusBM(A=(1.09356e+06,'s^-1'), n=1.83434, w0=(810.5,'kJ/mol'), E0=(366.415,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9059763464226809, var=0.1539552828983966, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C
    Total Standard Deviation in ln(k): 3.062923104012864"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C
Total Standard Deviation in ln(k): 3.062923104012864""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C
Total Standard Deviation in ln(k): 3.062923104012864
""",
)

entry(
    index = 19,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.7861e+10,'s^-1'), n=0.778365, w0=(884.5,'kJ/mol'), E0=(324.662,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7551313939764669, var=5.2349976425770866, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R
    Total Standard Deviation in ln(k): 6.484172417949625"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R
Total Standard Deviation in ln(k): 6.484172417949625""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R
Total Standard Deviation in ln(k): 6.484172417949625
""",
)

entry(
    index = 20,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.40038e+08,'s^-1'), n=1.04555, w0=(884.5,'kJ/mol'), E0=(303.522,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0007821082272608, var=0.21194032785904834, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 3.4374473425519185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 3.4374473425519185""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 3.4374473425519185
""",
)

entry(
    index = 21,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(5.66667e+08,'s^-1'), n=1.16, w0=(884.5,'kJ/mol'), E0=(327.64,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.865e+06,'s^-1'), n=1.71, w0=(810.5,'kJ/mol'), E0=(241.112,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C",
    kinetics = ArrheniusBM(A=(6.66708e+11,'s^-1'), n=0.00201256, w0=(884.5,'kJ/mol'), E0=(177.986,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6972849589862969, var=1.4477353565342361, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C
    Total Standard Deviation in ln(k): 4.164107089482756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C
Total Standard Deviation in ln(k): 4.164107089482756""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C
Total Standard Deviation in ln(k): 4.164107089482756
""",
)

entry(
    index = 24,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(6.23333e+10,'s^-1'), n=0.42, w0=(884.5,'kJ/mol'), E0=(182.306,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O",
    kinetics = ArrheniusBM(A=(1.50379e+20,'s^-1'), n=-2.28936, w0=(866,'kJ/mol'), E0=(94.1353,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9008765556962844, var=13.349326884548354, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O
    Total Standard Deviation in ln(k): 9.588155493760203"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O
Total Standard Deviation in ln(k): 9.588155493760203""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O
Total Standard Deviation in ln(k): 9.588155493760203
""",
)

entry(
    index = 26,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(2.59e+10,'s^-1'), n=0.65, w0=(884.5,'kJ/mol'), E0=(64.5017,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_N-6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_N-6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.66e+07,'s^-1'), n=1.5, w0=(810.5,'kJ/mol'), E0=(381.549,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.895e+06,'s^-1'), n=1.63, w0=(810.5,'kJ/mol'), E0=(365.991,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(5.8714e+09,'s^-1'), n=0.800009, w0=(884.5,'kJ/mol'), E0=(319.25,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4735898081875363, var=0.32894092038647266, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C
    Total Standard Deviation in ln(k): 2.339707294460993"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C
Total Standard Deviation in ln(k): 2.339707294460993""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C
Total Standard Deviation in ln(k): 2.339707294460993
""",
)

entry(
    index = 30,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.19667e+11,'s^-1'), n=0.77, w0=(884.5,'kJ/mol'), E0=(329.989,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(4.77e+08,'s^-1'), n=1.06, w0=(884.5,'kJ/mol'), E0=(305.835,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(2.65e+08,'s^-1'), n=1.02, w0=(884.5,'kJ/mol'), E0=(301.302,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(2.235e+11,'s^-1'), n=0.12, w0=(884.5,'kJ/mol'), E0=(179.272,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.08e+12,'s^-1'), n=-0.04, w0=(884.5,'kJ/mol'), E0=(176.036,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(6.36325e+12,'s^-1'), n=-0.260601, w0=(884.5,'kJ/mol'), E0=(58.3627,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.68477307054664, var=11.027205435094361, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R
    Total Standard Deviation in ln(k): 8.377706499016323"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 8.377706499016323""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 8.377706499016323
""",
)

entry(
    index = 36,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(5.9e+09,'s^-1'), n=0.8, w0=(884.5,'kJ/mol'), E0=(319.273,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(2.49e+09,'s^-1'), n=0.79, w0=(884.5,'kJ/mol'), E0=(314.86,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(2.26941e+13,'s^-1'), n=-0.460585, w0=(884.5,'kJ/mol'), E0=(42.1611,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0389345804596943, var=3.195481406998891, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C
    Total Standard Deviation in ln(k): 6.194034676001051"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 6.194034676001051""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 6.194034676001051
""",
)

entry(
    index = 39,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(3.4e+06,'s^-1'), n=1.62, w0=(884.5,'kJ/mol'), E0=(71.1229,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1.28224e+10,'s^-1'), n=0.400164, w0=(884.5,'kJ/mol'), E0=(-59.1518,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.69734e+11,'s^-1'), n=0.218411, w0=(884.5,'kJ/mol'), E0=(26.956,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

