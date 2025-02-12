#!/usr/bin/env python
# encoding: utf-8

name = "1+2_Cycloaddition/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = Arrhenius(A=(0.0150447,'m^3/(mol*s)'), n=2.17501, Ea=(38.7806,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=4.380293979232772, var=373.1072122785276, Tref=1000.0, N=42, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 42 training reactions at node Root
    Total Standard Deviation in ln(k): 49.72919311713049"""),
    rank = 11,
    shortDesc = """BM rule fitted to 42 training reactions at node Root
Total Standard Deviation in ln(k): 49.72919311713049""",
    longDesc = 
"""
BM rule fitted to 42 training reactions at node Root
Total Standard Deviation in ln(k): 49.72919311713049
""",
)

entry(
    index = 2,
    label = "Root_Ext-3R-R",
    kinetics = Arrhenius(A=(1.09994e-06,'m^3/(mol*s)'), n=3.23343, Ea=(54.5683,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=1.17963534744807, var=402.79928391993826, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_Ext-3R-R',), comment="""BM rule fitted to 29 training reactions at node Root_Ext-3R-R
    Total Standard Deviation in ln(k): 43.19866042337103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 43.19866042337103""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 43.19866042337103
""",
)

entry(
    index = 3,
    label = "Root_1R->C",
    kinetics = ArrheniusBM(A=(2.94176e+08,'m^3/(mol*s)'), n=-0.463393, w0=(476.125,'kJ/mol'), E0=(74.6089,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.053491550641994165, var=2.5349342642613375, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R->C',), comment="""BM rule fitted to 12 training reactions at node Root_1R->C
    Total Standard Deviation in ln(k): 3.3262352019642294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R->C
Total Standard Deviation in ln(k): 3.3262352019642294""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R->C
Total Standard Deviation in ln(k): 3.3262352019642294
""",
)

entry(
    index = 4,
    label = "Root_N-1R->C",
    kinetics = ArrheniusBM(A=(0.53862,'m^3/(mol*s)'), n=1.86213, w0=(572.5,'kJ/mol'), E0=(98.3778,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_Ext-3R-R_Sp-4R!H-3R",
    kinetics = Arrhenius(A=(4.47946e-06,'m^3/(mol*s)'), n=3.1361, Ea=(-22.2219,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-2.75034136163567, var=452.29371524833783, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R',), comment="""BM rule fitted to 17 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R
    Total Standard Deviation in ln(k): 49.54550347074846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R
Total Standard Deviation in ln(k): 49.54550347074846""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R
Total Standard Deviation in ln(k): 49.54550347074846
""",
)

entry(
    index = 6,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R",
    kinetics = ArrheniusBM(A=(0.00018461,'m^3/(mol*s)'), n=2.48631, w0=(572.5,'kJ/mol'), E0=(122.12,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6967267538731547, var=4.168299002354572, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R
    Total Standard Deviation in ln(k): 5.843519566927737"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R
Total Standard Deviation in ln(k): 5.843519566927737""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R
Total Standard Deviation in ln(k): 5.843519566927737
""",
)

entry(
    index = 7,
    label = "Root_1R->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.5716e+09,'m^3/(mol*s)'), n=-0.704858, w0=(474.2,'kJ/mol'), E0=(76.9274,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0574153355798587, var=0.5893395756050561, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.6832637924207203"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.6832637924207203""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.6832637924207203
""",
)

entry(
    index = 8,
    label = "Root_1R->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(3.33384e+09,'m^3/(mol*s)'), n=-0.775738, w0=(480,'kJ/mol'), E0=(85.117,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03181634091221043, var=0.14337316333857583, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_Ext-2R-R
    Total Standard Deviation in ln(k): 0.8390264527094017"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_Ext-2R-R
Total Standard Deviation in ln(k): 0.8390264527094017""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_Ext-2R-R
Total Standard Deviation in ln(k): 0.8390264527094017
""",
)

entry(
    index = 9,
    label = "Root_1R->C_Sp-2R=1C",
    kinetics = ArrheniusBM(A=(5.30858e+06,'m^3/(mol*s)'), n=-0.130328, w0=(480,'kJ/mol'), E0=(154.657,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.7979378610166568, var=0.4192186479711914, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Sp-2R=1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Sp-2R=1C
    Total Standard Deviation in ln(k): 3.3028767487161854"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Sp-2R=1C
Total Standard Deviation in ln(k): 3.3028767487161854""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Sp-2R=1C
Total Standard Deviation in ln(k): 3.3028767487161854
""",
)

entry(
    index = 10,
    label = "Root_1R->C_N-Sp-2R=1C",
    kinetics = ArrheniusBM(A=(1.52735e+09,'m^3/(mol*s)'), n=-0.643653, w0=(462.5,'kJ/mol'), E0=(85.8622,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-Sp-2R=1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-Sp-2R=1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_N-Sp-2R=1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_N-Sp-2R=1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O",
    kinetics = Arrhenius(A=(1.23126e-08,'m^3/(mol*s)'), n=3.72567, Ea=(-199.751,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.4396055164435505e-15, var=504.7261217330454, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O
    Total Standard Deviation in ln(k): 45.03859980474871"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O
Total Standard Deviation in ln(k): 45.03859980474871""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O
Total Standard Deviation in ln(k): 45.03859980474871
""",
)

entry(
    index = 12,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O",
    kinetics = Arrhenius(A=(5.22706e-05,'m^3/(mol*s)'), n=2.89044, Ea=(51.7485,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=2.793302606005478, var=69.49159572937879, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O
    Total Standard Deviation in ln(k): 23.730144488948955"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O
Total Standard Deviation in ln(k): 23.730144488948955""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O
Total Standard Deviation in ln(k): 23.730144488948955
""",
)

entry(
    index = 13,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(8.4226e-05,'m^3/(mol*s)'), n=2.57191, w0=(572.5,'kJ/mol'), E0=(120.119,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7472816737787236, var=4.576674577811986, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R
    Total Standard Deviation in ln(k): 6.166354735712154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R
Total Standard Deviation in ln(k): 6.166354735712154""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R
Total Standard Deviation in ln(k): 6.166354735712154
""",
)

entry(
    index = 14,
    label = "Root_1R->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.18e+07,'m^3/(mol*s)'), n=3.34379e-08, w0=(486,'kJ/mol'), E0=(121.323,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_1R->C_Ext-1C-R_Sp-2R=1C",
    kinetics = ArrheniusBM(A=(9.41381e+08,'m^3/(mol*s)'), n=-0.607357, w0=(480,'kJ/mol'), E0=(101.897,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8061640700917053, var=0.27679018591745186, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_Sp-2R=1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C
    Total Standard Deviation in ln(k): 3.0802460902618374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C
Total Standard Deviation in ln(k): 3.0802460902618374""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C
Total Standard Deviation in ln(k): 3.0802460902618374
""",
)

entry(
    index = 16,
    label = "Root_1R->C_Ext-1C-R_N-Sp-2R=1C",
    kinetics = ArrheniusBM(A=(4.65123e+09,'m^3/(mol*s)'), n=-0.763972, w0=(462.5,'kJ/mol'), E0=(90.9129,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1396007814667642, var=0.8124977918268483, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_N-Sp-2R=1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C
    Total Standard Deviation in ln(k): 2.1577970555953048"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C
Total Standard Deviation in ln(k): 2.1577970555953048""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C
Total Standard Deviation in ln(k): 2.1577970555953048
""",
)

entry(
    index = 17,
    label = "Root_1R->C_Ext-2R-R_3R->C",
    kinetics = ArrheniusBM(A=(4.13595e+09,'m^3/(mol*s)'), n=-0.801251, w0=(474,'kJ/mol'), E0=(97.1562,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18237254724139285, var=0.005024605839000183, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_3R->C
    Total Standard Deviation in ln(k): 0.6003270321662865"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_3R->C
Total Standard Deviation in ln(k): 0.6003270321662865""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_3R->C
Total Standard Deviation in ln(k): 0.6003270321662865
""",
)

entry(
    index = 18,
    label = "Root_1R->C_Ext-2R-R_N-3R->C",
    kinetics = ArrheniusBM(A=(3.86082e+06,'m^3/(mol*s)'), n=0.0243325, w0=(486,'kJ/mol'), E0=(92.826,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0023056582247643507, var=1.6591495502960631, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C
    Total Standard Deviation in ln(k): 2.5880518524180083"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C
Total Standard Deviation in ln(k): 2.5880518524180083""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C
Total Standard Deviation in ln(k): 2.5880518524180083
""",
)

entry(
    index = 19,
    label = "Root_1R->C_Sp-2R=1C_3R->C",
    kinetics = ArrheniusBM(A=(1.98e+06,'m^3/(mol*s)'), n=-1.39065e-08, w0=(474,'kJ/mol'), E0=(153.583,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Sp-2R=1C_3R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_3R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_3R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_3R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_1R->C_Sp-2R=1C_N-3R->C",
    kinetics = ArrheniusBM(A=(700000,'m^3/(mol*s)'), n=1.26784e-08, w0=(486,'kJ/mol'), E0=(119.69,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Sp-2R=1C_N-3R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_N-3R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_N-3R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_N-3R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R",
    kinetics = Arrhenius(A=(3.78574e-12,'m^3/(mol*s)'), n=3.31677, Ea=(-184.434,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.1891272779868196e-15, var=0.35857914072772035, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.200464994296705"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.200464994296705""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.200464994296705
""",
)

entry(
    index = 22,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-5R!H-R",
    kinetics = Arrhenius(A=(2.73238e-05,'m^3/(mol*s)'), n=4.17252, Ea=(-219.263,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C",
    kinetics = ArrheniusBM(A=(2.65277e+11,'m^3/(mol*s)'), n=-1.63781, w0=(490.417,'kJ/mol'), E0=(146.247,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13397801687989275, var=5.325801172482285, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C
    Total Standard Deviation in ln(k): 4.963095131278134"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C
Total Standard Deviation in ln(k): 4.963095131278134""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C
Total Standard Deviation in ln(k): 4.963095131278134
""",
)

entry(
    index = 24,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C",
    kinetics = Arrhenius(A=(9.61526e-05,'m^3/(mol*s)'), n=2.84303, Ea=(78.2212,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-8.997534477772192e-16, var=86.8889913183679, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C
    Total Standard Deviation in ln(k): 18.68699060315099"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C
Total Standard Deviation in ln(k): 18.68699060315099""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C
Total Standard Deviation in ln(k): 18.68699060315099
""",
)

entry(
    index = 25,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O",
    kinetics = Arrhenius(A=(2.17596e-11,'m^3/(mol*s)'), n=4.37463, Ea=(150.001,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-7.198027582217753e-16, var=27.439778177234164, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O
    Total Standard Deviation in ln(k): 10.501402088694494"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O
Total Standard Deviation in ln(k): 10.501402088694494""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O
Total Standard Deviation in ln(k): 10.501402088694494
""",
)

entry(
    index = 26,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1103.61,'m^3/(mol*s)'), n=0.603336, w0=(572.5,'kJ/mol'), E0=(136.682,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.287168463750937, var=5.482259913532943, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O
    Total Standard Deviation in ln(k): 5.415460872735751"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O
Total Standard Deviation in ln(k): 5.415460872735751""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O
Total Standard Deviation in ln(k): 5.415460872735751
""",
)

entry(
    index = 27,
    label = "Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.54e+07,'m^3/(mol*s)'), n=2.18427e-08, w0=(486,'kJ/mol'), E0=(120.733,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(4.29568e+09,'m^3/(mol*s)'), n=-0.811807, w0=(462.5,'kJ/mol'), E0=(82.3565,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(2.40609e+09,'m^3/(mol*s)'), n=-0.732703, w0=(474,'kJ/mol'), E0=(102.225,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(5.13998e+06,'m^3/(mol*s)'), n=0.0486651, w0=(486,'kJ/mol'), E0=(122.28,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C",
    kinetics = Arrhenius(A=(1.77162e-11,'m^3/(mol*s)'), n=3.14677, Ea=(-183.048,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-5.62345904860762e-16, var=0.292680771133422, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C
    Total Standard Deviation in ln(k): 1.0845612528249908"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C
Total Standard Deviation in ln(k): 1.0845612528249908""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C
Total Standard Deviation in ln(k): 1.0845612528249908
""",
)

entry(
    index = 32,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C",
    kinetics = Arrhenius(A=(1.72865e-13,'m^3/(mol*s)'), n=3.65675, Ea=(-187.206,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F",
    kinetics = Arrhenius(A=(1.42848e-05,'m^3/(mol*s)'), n=2.92501, Ea=(35.9671,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=1.669464405055387e-15, var=2.29620033507037, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F
    Total Standard Deviation in ln(k): 3.03781888342419"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F
Total Standard Deviation in ln(k): 3.03781888342419""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F
Total Standard Deviation in ln(k): 3.03781888342419
""",
)

entry(
    index = 34,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F",
    kinetics = ArrheniusBM(A=(0.531384,'m^3/(mol*s)'), n=1.91075, w0=(474,'kJ/mol'), E0=(98.7387,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05772002806466054, var=2.936408172201264, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F
    Total Standard Deviation in ln(k): 3.580329404755293"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F
Total Standard Deviation in ln(k): 3.580329404755293""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F
Total Standard Deviation in ln(k): 3.580329404755293
""",
)

entry(
    index = 35,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R",
    kinetics = ArrheniusBM(A=(0.00193156,'m^3/(mol*s)'), n=2.48801, w0=(572.5,'kJ/mol'), E0=(119.869,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1169437380568294, var=195.4150575788199, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R
    Total Standard Deviation in ln(k): 30.83077057032501"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R
Total Standard Deviation in ln(k): 30.83077057032501""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R
Total Standard Deviation in ln(k): 30.83077057032501
""",
)

entry(
    index = 36,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-4BrCClF-R",
    kinetics = ArrheniusBM(A=(9.45453e-05,'m^3/(mol*s)'), n=2.81848, w0=(572.5,'kJ/mol'), E0=(133.877,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-4BrCClF-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-4BrCClF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-4BrCClF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-4BrCClF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.35775e-11,'m^3/(mol*s)'), n=4.20211, w0=(572.5,'kJ/mol'), E0=(91.0862,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1691937435912194, var=0.1262154367344573, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 3.6498911836364294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.6498911836364294""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.6498911836364294
""",
)

entry(
    index = 38,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.50469e-12,'m^3/(mol*s)'), n=4.73863, w0=(572.5,'kJ/mol'), E0=(128.163,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R",
    kinetics = ArrheniusBM(A=(0.0710555,'m^3/(mol*s)'), n=1.7866, w0=(572.5,'kJ/mol'), E0=(115.679,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.49042410619337257, var=3.504500032529071, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R
    Total Standard Deviation in ln(k): 4.985147566648897"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 4.985147566648897""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 4.985147566648897
""",
)

entry(
    index = 40,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-5BrCClFINPSSi-R",
    kinetics = ArrheniusBM(A=(2.25175e-06,'m^3/(mol*s)'), n=3.12644, w0=(572.5,'kJ/mol'), E0=(134.468,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-5BrCClFINPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-5BrCClFINPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-5BrCClFINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-5BrCClFINPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = Arrhenius(A=(2.91753e-11,'m^3/(mol*s)'), n=3.05655, Ea=(-182.493,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = Arrhenius(A=(1.07579e-11,'m^3/(mol*s)'), n=3.237, Ea=(-183.604,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->O_Ext-4O-R_Ext-3R-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-7R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-8R!H-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4.10298e-06,'m^3/(mol*s)'), n=3.07477, w0=(474,'kJ/mol'), E0=(78.6589,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.01799e-05,'m^3/(mol*s)'), n=2.87159, w0=(474,'kJ/mol'), E0=(101.042,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_2R->C",
    kinetics = ArrheniusBM(A=(2.07011e-05,'m^3/(mol*s)'), n=2.98446, w0=(474,'kJ/mol'), E0=(119.563,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_N-2R->C",
    kinetics = ArrheniusBM(A=(4.81575e-05,'m^3/(mol*s)'), n=2.76922, w0=(572.5,'kJ/mol'), E0=(109.078,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_4BrCClF->F_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_4BrCCl->Cl",
    kinetics = ArrheniusBM(A=(8.68219e-05,'m^3/(mol*s)'), n=2.97056, w0=(474,'kJ/mol'), E0=(87.4167,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_4BrCCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_4BrCCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_4BrCCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_4BrCCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_N-4BrCCl->Cl",
    kinetics = ArrheniusBM(A=(0.000161154,'m^3/(mol*s)'), n=2.94391, w0=(474,'kJ/mol'), E0=(70.9316,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_N-4BrCCl->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_N-4BrCCl->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_N-4BrCCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_1R->C_N-4BrCClF->F_N-4BrCCl->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C",
    kinetics = ArrheniusBM(A=(9715.32,'m^3/(mol*s)'), n=0.563891, w0=(572.5,'kJ/mol'), E0=(149.825,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1568080779655681, var=296.20073523838585, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C
    Total Standard Deviation in ln(k): 34.8964497055051"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C
Total Standard Deviation in ln(k): 34.8964497055051""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C
Total Standard Deviation in ln(k): 34.8964497055051
""",
)

entry(
    index = 50,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_N-4BrCClF->C",
    kinetics = ArrheniusBM(A=(0.00491008,'m^3/(mol*s)'), n=2.38401, w0=(572.5,'kJ/mol'), E0=(83.113,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_N-4BrCClF->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_N-4BrCClF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_N-4BrCClF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_N-4BrCClF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C",
    kinetics = ArrheniusBM(A=(3.09714e-11,'m^3/(mol*s)'), n=4.27056, w0=(572.5,'kJ/mol'), E0=(91.8207,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.212801594511404, var=0.03325776986424597, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C
    Total Standard Deviation in ln(k): 3.4128379683690864"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 3.4128379683690864""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 3.4128379683690864
""",
)

entry(
    index = 52,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(3.89377e-10,'m^3/(mol*s)'), n=3.9548, w0=(572.5,'kJ/mol'), E0=(90.596,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 53,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(3.98227e-05,'m^3/(mol*s)'), n=2.70596, w0=(572.5,'kJ/mol'), E0=(112.407,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5910490826304248, var=0.27235984613876246, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 2.531281223796797"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 2.531281223796797""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 2.531281223796797
""",
)

entry(
    index = 54,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_N-5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(0.000352549,'m^3/(mol*s)'), n=2.48352, w0=(572.5,'kJ/mol'), E0=(92.4375,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_N-5BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_N-5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 55,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(1.24121e-05,'m^3/(mol*s)'), n=3.07293, w0=(572.5,'kJ/mol'), E0=(157.079,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.33631353739566155, var=705.9390473680339, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C
    Total Standard Deviation in ln(k): 54.10984458091796"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 54.10984458091796""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 54.10984458091796
""",
)

entry(
    index = 56,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.87031e-05,'m^3/(mol*s)'), n=3.04873, w0=(572.5,'kJ/mol'), E0=(64.607,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 57,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C",
    kinetics = ArrheniusBM(A=(2.35526e-11,'m^3/(mol*s)'), n=4.30096, w0=(572.5,'kJ/mol'), E0=(91.826,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(4.0727e-11,'m^3/(mol*s)'), n=4.24017, w0=(572.5,'kJ/mol'), E0=(91.8153,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(4.6487e-05,'m^3/(mol*s)'), n=2.69436, w0=(572.5,'kJ/mol'), E0=(112.945,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5944663503659997, var=0.9376777933368812, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 3.4348944884024393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 3.4348944884024393""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 3.4348944884024393
""",
)

entry(
    index = 60,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.81961e-05,'m^3/(mol*s)'), n=2.73363, w0=(572.5,'kJ/mol'), E0=(111.291,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(0.00828286,'m^3/(mol*s)'), n=2.34779, w0=(572.5,'kJ/mol'), E0=(89.4849,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(2.67496e-08,'m^3/(mol*s)'), n=3.75287, w0=(572.5,'kJ/mol'), E0=(224.016,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->O_N-1R->C_Ext-3R-R_4BrCClF->C_Ext-4C-R_6R!H->C_Ext-6C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(6.58773e-05,'m^3/(mol*s)'), n=2.61294, w0=(572.5,'kJ/mol'), E0=(114.005,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(4.67866e-05,'m^3/(mol*s)'), n=2.73161, w0=(572.5,'kJ/mol'), E0=(112.296,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFINPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

