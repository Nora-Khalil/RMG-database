#!/usr/bin/env python
# encoding: utf-8

name = "CO_CF_bond_dissociation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.76451e+11,'s^-1'), n=0.325184, w0=(858.983,'kJ/mol'), E0=(231.209,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6760025142202835, var=182.8012395033658, Tref=1000.0, N=29, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 29 training reactions at node Root
    Total Standard Deviation in ln(k): 28.803320650464393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root
Total Standard Deviation in ln(k): 28.803320650464393""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root
Total Standard Deviation in ln(k): 28.803320650464393
""",
)

entry(
    index = 2,
    label = "Root_3C-u0",
    kinetics = ArrheniusBM(A=(2.4772e+09,'s^-1'), n=0.86143, w0=(854.9,'kJ/mol'), E0=(277.324,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6672460506586875, var=77.76919612534303, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_3C-u0',), comment="""BM rule fitted to 20 training reactions at node Root_3C-u0
    Total Standard Deviation in ln(k): 19.355623747292"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_3C-u0
Total Standard Deviation in ln(k): 19.355623747292""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_3C-u0
Total Standard Deviation in ln(k): 19.355623747292
""",
)

entry(
    index = 3,
    label = "Root_N-3C-u0",
    kinetics = ArrheniusBM(A=(1.22937e+21,'s^-1'), n=-2.50646, w0=(868.056,'kJ/mol'), E0=(148.182,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8611766534535092, var=182.81174578272956, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-3C-u0',), comment="""BM rule fitted to 9 training reactions at node Root_N-3C-u0
    Total Standard Deviation in ln(k): 29.269361204007055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-3C-u0
Total Standard Deviation in ln(k): 29.269361204007055""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-3C-u0
Total Standard Deviation in ln(k): 29.269361204007055
""",
)

entry(
    index = 4,
    label = "Root_3C-u0_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.92191e+10,'s^-1'), n=0.470969, w0=(854.9,'kJ/mol'), E0=(298.313,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.716172917068278, var=91.48910511613158, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R',), comment="""BM rule fitted to 15 training reactions at node Root_3C-u0_Ext-3C-R
    Total Standard Deviation in ln(k): 20.974707891868672"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_3C-u0_Ext-3C-R
Total Standard Deviation in ln(k): 20.974707891868672""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_3C-u0_Ext-3C-R
Total Standard Deviation in ln(k): 20.974707891868672
""",
)

entry(
    index = 5,
    label = "Root_3C-u0_4F1sH->H",
    kinetics = ArrheniusBM(A=(1.06172e+06,'s^-1'), n=1.81129, w0=(810.5,'kJ/mol'), E0=(200.615,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.2914832305231175, var=0.8524145049606645, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_4F1sH->H',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_4F1sH->H
    Total Standard Deviation in ln(k): 2.5832675801593172"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_4F1sH->H
Total Standard Deviation in ln(k): 2.5832675801593172""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_4F1sH->H
Total Standard Deviation in ln(k): 2.5832675801593172
""",
)

entry(
    index = 6,
    label = "Root_3C-u0_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(2.26103e+08,'s^-1'), n=1.05774, w0=(884.5,'kJ/mol'), E0=(239.235,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7620000405643447, var=1.8615817235328695, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3C-u0_N-4F1sH->H',), comment="""BM rule fitted to 3 training reactions at node Root_3C-u0_N-4F1sH->H
    Total Standard Deviation in ln(k): 4.64982936495915"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3C-u0_N-4F1sH->H
Total Standard Deviation in ln(k): 4.64982936495915""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3C-u0_N-4F1sH->H
Total Standard Deviation in ln(k): 4.64982936495915
""",
)

entry(
    index = 7,
    label = "Root_N-3C-u0_5R->O",
    kinetics = ArrheniusBM(A=(1442.74,'s^-1'), n=2.34038, w0=(884.5,'kJ/mol'), E0=(262.374,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.30913528390653977, var=0.07250119342878229, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3C-u0_5R->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3C-u0_5R->O
    Total Standard Deviation in ln(k): 1.316517700939746"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3C-u0_5R->O
Total Standard Deviation in ln(k): 1.316517700939746""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3C-u0_5R->O
Total Standard Deviation in ln(k): 1.316517700939746
""",
)

entry(
    index = 8,
    label = "Root_N-3C-u0_N-5R->O",
    kinetics = ArrheniusBM(A=(9.55194e+15,'s^-1'), n=-0.95949, w0=(863.357,'kJ/mol'), E0=(88.9182,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7733850029318071, var=5.222362404353374, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-3C-u0_N-5R->O
    Total Standard Deviation in ln(k): 6.524496972449019"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-3C-u0_N-5R->O
Total Standard Deviation in ln(k): 6.524496972449019""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-3C-u0_N-5R->O
Total Standard Deviation in ln(k): 6.524496972449019
""",
)

entry(
    index = 9,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.88362e+08,'s^-1'), n=1.25682, w0=(854.9,'kJ/mol'), E0=(341.338,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.751789007266164, var=20.614923819808272, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C',), comment="""BM rule fitted to 10 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C
    Total Standard Deviation in ln(k): 10.991148177690718"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 10.991148177690718""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C
Total Standard Deviation in ln(k): 10.991148177690718
""",
)

entry(
    index = 10,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.721084,'s^-1'), n=3.5259, w0=(854.9,'kJ/mol'), E0=(181.284,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.25128579495512327, var=31.37748004021832, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.861016167508886"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.861016167508886""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.861016167508886
""",
)

entry(
    index = 11,
    label = "Root_3C-u0_4F1sH->H_Ext-2C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(560000,'s^-1'), n=1.87, w0=(810.5,'kJ/mol'), E0=(201.182,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_4F1sH->H_Ext-2C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_4F1sH->H_Ext-2C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_4F1sH->H_Ext-2C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_4F1sH->H_Ext-2C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.24512e+08,'s^-1'), n=0.995513, w0=(884.5,'kJ/mol'), E0=(242.35,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8599959327159881, var=0.48860182104282157, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C
    Total Standard Deviation in ln(k): 3.562104797269159"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C
Total Standard Deviation in ln(k): 3.562104797269159""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C
Total Standard Deviation in ln(k): 3.562104797269159
""",
)

entry(
    index = 13,
    label = "Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(8.1e+07,'s^-1'), n=1.22, w0=(884.5,'kJ/mol'), E0=(232.674,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
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
    index = 15,
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
    index = 16,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R",
    kinetics = ArrheniusBM(A=(8.0307e+17,'s^-1'), n=-1.6099, w0=(869.7,'kJ/mol'), E0=(87.2213,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8562054685260497, var=9.315189985105619, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R
    Total Standard Deviation in ln(k): 8.269881087504746"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R
Total Standard Deviation in ln(k): 8.269881087504746""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R
Total Standard Deviation in ln(k): 8.269881087504746
""",
)

entry(
    index = 17,
    label = "Root_N-3C-u0_N-5R->O_4F1sH->H",
    kinetics = ArrheniusBM(A=(2.78e+10,'s^-1'), n=0.74, w0=(810.5,'kJ/mol'), E0=(81.5933,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_4F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_4F1sH->H
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
    index = 18,
    label = "Root_N-3C-u0_N-5R->O_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(5.95e+09,'s^-1'), n=1.2, w0=(884.5,'kJ/mol'), E0=(99.0717,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_N-4F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_N-4F1sH->H
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
    index = 19,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H",
    kinetics = ArrheniusBM(A=(5.3349e+06,'s^-1'), n=1.68732, w0=(810.5,'kJ/mol'), E0=(371.48,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6706606488369297, var=2.3730955428349056, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H',), comment="""BM rule fitted to 4 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H
    Total Standard Deviation in ln(k): 4.773342303803581"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 4.773342303803581""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 4.773342303803581
""",
)

entry(
    index = 20,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(2.5125e+09,'s^-1'), n=0.944844, w0=(884.5,'kJ/mol'), E0=(316.967,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.8138799923068958, var=1.158681683889361, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H',), comment="""BM rule fitted to 6 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H
    Total Standard Deviation in ln(k): 4.2028630885684075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 4.2028630885684075""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 4.2028630885684075
""",
)

entry(
    index = 21,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H",
    kinetics = ArrheniusBM(A=(1.26761e+06,'s^-1'), n=1.81828, w0=(810.5,'kJ/mol'), E0=(243.842,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.30118000642634013, var=0.07060990627683565, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H
    Total Standard Deviation in ln(k): 1.2894424057733238"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 1.2894424057733238""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_4F1sH->H
Total Standard Deviation in ln(k): 1.2894424057733238
""",
)

entry(
    index = 22,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H",
    kinetics = ArrheniusBM(A=(3.00432e+11,'s^-1'), n=0.142235, w0=(884.5,'kJ/mol'), E0=(179.422,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6178164804268671, var=0.4264679313820882, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H',), comment="""BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H
    Total Standard Deviation in ln(k): 2.8614851778565327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 2.8614851778565327""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H
Total Standard Deviation in ln(k): 2.8614851778565327
""",
)

entry(
    index = 23,
    label = "Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.63e+08,'s^-1'), n=1.07, w0=(884.5,'kJ/mol'), E0=(242.979,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(7.65e+08,'s^-1'), n=0.9, w0=(884.5,'kJ/mol'), E0=(241.903,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3C-u0_N-4F1sH->H_Ext-5R-R_Ext-5R-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O",
    kinetics = ArrheniusBM(A=(1.50386e+20,'s^-1'), n=-2.28936, w0=(866,'kJ/mol'), E0=(94.1354,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9008768672428535, var=13.349377527774235, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O
    Total Standard Deviation in ln(k): 9.588170170251486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O
Total Standard Deviation in ln(k): 9.588170170251486""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O
Total Standard Deviation in ln(k): 9.588170170251486
""",
)

entry(
    index = 26,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(2.59e+10,'s^-1'), n=0.65, w0=(884.5,'kJ/mol'), E0=(64.5018,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_N-6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_N-6R!H->O
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
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C",
    kinetics = ArrheniusBM(A=(2.3976e+07,'s^-1'), n=1.55051, w0=(810.5,'kJ/mol'), E0=(376.445,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4330065775066377, var=15.07634950059399, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C
    Total Standard Deviation in ln(k): 8.87199674093406"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C
Total Standard Deviation in ln(k): 8.87199674093406""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_Sp-6C-3C
Total Standard Deviation in ln(k): 8.87199674093406
""",
)

entry(
    index = 28,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C",
    kinetics = ArrheniusBM(A=(1.09356e+06,'s^-1'), n=1.83434, w0=(810.5,'kJ/mol'), E0=(366.415,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9059763464226837, var=0.15395528289839155, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C
    Total Standard Deviation in ln(k): 3.062923104012858"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C
Total Standard Deviation in ln(k): 3.062923104012858""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_4F1sH->H_N-Sp-6C-3C
Total Standard Deviation in ln(k): 3.062923104012858
""",
)

entry(
    index = 29,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R",
    kinetics = ArrheniusBM(A=(2.78615e+10,'s^-1'), n=0.778363, w0=(884.5,'kJ/mol'), E0=(324.662,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7551313936170779, var=5.234997640238447, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R
    Total Standard Deviation in ln(k): 6.484172416022089"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R
Total Standard Deviation in ln(k): 6.484172416022089""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R
Total Standard Deviation in ln(k): 6.484172416022089
""",
)

entry(
    index = 30,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.40038e+08,'s^-1'), n=1.04555, w0=(884.5,'kJ/mol'), E0=(303.522,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0007821082272703, var=0.2119403278590172, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 3.437447342551875"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 3.437447342551875""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-6C-R_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 3.437447342551875
""",
)

entry(
    index = 31,
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
    index = 32,
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
    index = 33,
    label = "Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C",
    kinetics = ArrheniusBM(A=(6.66604e+11,'s^-1'), n=0.00203199, w0=(884.5,'kJ/mol'), E0=(177.986,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6972849589863044, var=1.447735356534282, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C
    Total Standard Deviation in ln(k): 4.164107089482813"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C
Total Standard Deviation in ln(k): 4.164107089482813""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_N-6R!H->C_N-4F1sH->H_Ext-5R-R_Ext-5R-R_7R!H->C
Total Standard Deviation in ln(k): 4.164107089482813
""",
)

entry(
    index = 34,
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
    index = 35,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(6.36369e+12,'s^-1'), n=-0.260609, w0=(884.5,'kJ/mol'), E0=(58.3628,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.6847718043905662, var=11.027192081063516, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R
    Total Standard Deviation in ln(k): 8.37769928677563"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 8.37769928677563""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R
Total Standard Deviation in ln(k): 8.37769928677563
""",
)

entry(
    index = 36,
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
    index = 37,
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
    index = 38,
    label = "Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(5.8714e+09,'s^-1'), n=0.800009, w0=(884.5,'kJ/mol'), E0=(319.25,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.4735898081875393, var=0.32894092038645034, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C
    Total Standard Deviation in ln(k): 2.339707294460961"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C
Total Standard Deviation in ln(k): 2.339707294460961""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3C-u0_Ext-3C-R_6R!H->C_N-4F1sH->H_Ext-3C-R_Ext-6C-R_Ext-6C-R_8R!H->C
Total Standard Deviation in ln(k): 2.339707294460961
""",
)

entry(
    index = 39,
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
    index = 40,
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
    index = 41,
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
    index = 42,
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
    index = 43,
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
    index = 44,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(2.26871e+13,'s^-1'), n=-0.460546, w0=(884.5,'kJ/mol'), E0=(42.1607,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.0389345554572418, var=3.195481073880878, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C
    Total Standard Deviation in ln(k): 6.1940344263893765"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 6.1940344263893765""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C
Total Standard Deviation in ln(k): 6.1940344263893765
""",
)

entry(
    index = 45,
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
    index = 46,
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
    index = 47,
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
    index = 48,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(4.5e+06,'s^-1'), n=1.39, Ea=(90.007,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_8R!H->C
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
    index = 49,
    label = "Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(1.69735e+11,'s^-1'), n=0.218411, w0=(884.5,'kJ/mol'), E0=(26.956,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3C-u0_N-5R->O_Ext-5CFH-R_6R!H->O_Ext-2C-R_7R!H->C_Ext-7C-R_N-8R!H->C
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

