#!/usr/bin/env python
# encoding: utf-8

name = "1+2_Cycloaddition/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(6.65937e+11,'m^3/(mol*s)'), n=-1.84035, w0=(533238,'J/mol'), E0=(139726,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.015371865027778013, var=45.04850372289682, Tref=1000.0, N=42, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 42 training reactions at node Root
    Total Standard Deviation in ln(k): 13.494040180927323"""),
    rank = 11,
    shortDesc = """BM rule fitted to 42 training reactions at node Root
Total Standard Deviation in ln(k): 13.494040180927323""",
    longDesc = 
"""
BM rule fitted to 42 training reactions at node Root
Total Standard Deviation in ln(k): 13.494040180927323
""",
)

entry(
    index = 2,
    label = "Root_Ext-3R-R",
    kinetics = ArrheniusBM(A=(0.00732782,'m^3/(mol*s)'), n=2.12979, w0=(555517,'J/mol'), E0=(104040,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4168016203501518, var=48.87884342126049, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_Ext-3R-R',), comment="""BM rule fitted to 29 training reactions at node Root_Ext-3R-R
    Total Standard Deviation in ln(k): 15.063025996134705"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 15.063025996134705""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_Ext-3R-R
Total Standard Deviation in ln(k): 15.063025996134705
""",
)

entry(
    index = 3,
    label = "Root_1R->C",
    kinetics = ArrheniusBM(A=(2.94176e+08,'m^3/(mol*s)'), n=-0.463393, w0=(476125,'J/mol'), E0=(47612.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.05349156708281672, var=2.5349342802848747, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R->C',), comment="""BM rule fitted to 12 training reactions at node Root_1R->C
    Total Standard Deviation in ln(k): 3.326235253360758"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R->C
Total Standard Deviation in ln(k): 3.326235253360758""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R->C
Total Standard Deviation in ln(k): 3.326235253360758
""",
)

entry(
    index = 4,
    label = "Root_N-1R->C",
    kinetics = Arrhenius(A=(0.53862,'m^3/(mol*s)'), n=1.86213, Ea=(24.8236,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->C
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
    kinetics = ArrheniusBM(A=(4855,'m^3/(mol*s)'), n=0.567463, w0=(543529,'J/mol'), E0=(103672,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1326117462359642, var=88.60016550856807, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R',), comment="""BM rule fitted to 17 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R
    Total Standard Deviation in ln(k): 19.203297702864283"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R
Total Standard Deviation in ln(k): 19.203297702864283""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R
Total Standard Deviation in ln(k): 19.203297702864283
""",
)

entry(
    index = 6,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R",
    kinetics = ArrheniusBM(A=(2.39658e-31,'m^3/(mol*s)'), n=10.1912, w0=(572500,'J/mol'), E0=(36315.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.1270764948984935, var=16.05987157268814, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R
    Total Standard Deviation in ln(k): 10.86578012019332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R
Total Standard Deviation in ln(k): 10.86578012019332""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R
Total Standard Deviation in ln(k): 10.86578012019332
""",
)

entry(
    index = 7,
    label = "Root_1R->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.5716e+09,'m^3/(mol*s)'), n=-0.704858, w0=(474200,'J/mol'), E0=(47420,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.003178602591253677, var=0.5008544564983712, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_1R->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.4267589342073508"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.4267589342073508""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.4267589342073508
""",
)

entry(
    index = 8,
    label = "Root_1R->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(3.33384e+09,'m^3/(mol*s)'), n=-0.775738, w0=(480000,'J/mol'), E0=(48000,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.03181634044488337, var=0.1433731634963656, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->C_Ext-2R-R
    Total Standard Deviation in ln(k): 0.8390264519529201"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->C_Ext-2R-R
Total Standard Deviation in ln(k): 0.8390264519529201""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->C_Ext-2R-R
Total Standard Deviation in ln(k): 0.8390264519529201
""",
)

entry(
    index = 9,
    label = "Root_1R->C_Sp-2R=1C",
    kinetics = ArrheniusBM(A=(0.00650771,'m^3/(mol*s)'), n=2.42295, w0=(480000,'J/mol'), E0=(48000,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.587997258796586, var=0.16964704494037178, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Sp-2R=1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Sp-2R=1C
    Total Standard Deviation in ln(k): 4.815657794528946"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Sp-2R=1C
Total Standard Deviation in ln(k): 4.815657794528946""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Sp-2R=1C
Total Standard Deviation in ln(k): 4.815657794528946
""",
)

entry(
    index = 10,
    label = "Root_1R->C_N-Sp-2R=1C",
    kinetics = Arrhenius(A=(1.77e+09,'m^3/(mol*s)'), n=-0.662, Ea=(0.157737,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_N-Sp-2R=1C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_N-Sp-2R=1C
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
    label = "Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(7.16184e+14,'m^3/(mol*s)'), n=-2.64648, w0=(572500,'J/mol'), E0=(127653,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.07648217837847994, var=113.59298862896648, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 21.558635048513597"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R
Total Standard Deviation in ln(k): 21.558635048513597""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R
Total Standard Deviation in ln(k): 21.558635048513597
""",
)

entry(
    index = 12,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_4R!H->Br",
    kinetics = Arrhenius(A=(0.000145611,'m^3/(mol*s)'), n=2.95653, Ea=(-0.108502,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_4R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_4R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br",
    kinetics = ArrheniusBM(A=(3.8459e-26,'m^3/(mol*s)'), n=8.95319, w0=(516214,'J/mol'), E0=(24089.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-2.0834270483536974, var=33.31806584682626, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br
    Total Standard Deviation in ln(k): 16.806433722841042"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br
Total Standard Deviation in ln(k): 16.806433722841042""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br
Total Standard Deviation in ln(k): 16.806433722841042
""",
)

entry(
    index = 14,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R",
    kinetics = Arrhenius(A=(3.6439e-06,'m^3/(mol*s)'), n=2.96431, Ea=(157.913,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=5.398520686663315e-15, var=68.49531188665861, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R
    Total Standard Deviation in ln(k): 16.591567306581247"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R
Total Standard Deviation in ln(k): 16.591567306581247""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R
Total Standard Deviation in ln(k): 16.591567306581247
""",
)

entry(
    index = 15,
    label = "Root_1R->C_Ext-1C-R_Ext-1C-R",
    kinetics = Arrhenius(A=(3.18e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Ext-1C-R
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
    index = 16,
    label = "Root_1R->C_Ext-1C-R_Sp-2R=1C",
    kinetics = ArrheniusBM(A=(9.41381e+08,'m^3/(mol*s)'), n=-0.607357, w0=(480000,'J/mol'), E0=(48000,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2790521167276606, var=0.007777354492480229, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_Sp-2R=1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C
    Total Standard Deviation in ln(k): 0.877932175956457"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C
Total Standard Deviation in ln(k): 0.877932175956457""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C
Total Standard Deviation in ln(k): 0.877932175956457
""",
)

entry(
    index = 17,
    label = "Root_1R->C_Ext-1C-R_N-Sp-2R=1C",
    kinetics = ArrheniusBM(A=(4.63231e+09,'m^3/(mol*s)'), n=-0.7664, w0=(462500,'J/mol'), E0=(46250,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0009309671137264789, var=1.1655949953965052, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_N-Sp-2R=1C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C
    Total Standard Deviation in ln(k): 2.1667057286443416"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C
Total Standard Deviation in ln(k): 2.1667057286443416""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C
Total Standard Deviation in ln(k): 2.1667057286443416
""",
)

entry(
    index = 18,
    label = "Root_1R->C_Ext-2R-R_3R->C",
    kinetics = ArrheniusBM(A=(4.13595e+09,'m^3/(mol*s)'), n=-0.801251, w0=(474000,'J/mol'), E0=(47400,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0395530227295251, var=0.0335984334446083, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_3R->C
    Total Standard Deviation in ln(k): 0.46684489712018756"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_3R->C
Total Standard Deviation in ln(k): 0.46684489712018756""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_3R->C
Total Standard Deviation in ln(k): 0.46684489712018756
""",
)

entry(
    index = 19,
    label = "Root_1R->C_Ext-2R-R_N-3R->C",
    kinetics = ArrheniusBM(A=(3.86082e+06,'m^3/(mol*s)'), n=0.0243327, w0=(486000,'J/mol'), E0=(48600,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.02516094828390788, var=1.7607258136569388, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_N-3R->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C
    Total Standard Deviation in ln(k): 2.7233484267253916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C
Total Standard Deviation in ln(k): 2.7233484267253916""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C
Total Standard Deviation in ln(k): 2.7233484267253916
""",
)

entry(
    index = 20,
    label = "Root_1R->C_Sp-2R=1C_3R->C",
    kinetics = Arrhenius(A=(1.98e+06,'m^3/(mol*s)'), n=0, Ea=(22.1334,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Sp-2R=1C_3R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_3R->C
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
    index = 21,
    label = "Root_1R->C_Sp-2R=1C_N-3R->C",
    kinetics = Arrhenius(A=(700000,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Sp-2R=1C_N-3R->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Sp-2R=1C_N-3R->C
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
    index = 22,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C",
    kinetics = ArrheniusBM(A=(5.85682e-17,'m^3/(mol*s)'), n=6.26389, w0=(572500,'J/mol'), E0=(78058.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6071513265831525, var=68.94099118638233, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C
    Total Standard Deviation in ln(k): 18.170963910401014"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C
Total Standard Deviation in ln(k): 18.170963910401014""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C
Total Standard Deviation in ln(k): 18.170963910401014
""",
)

entry(
    index = 23,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_N-4R!H->C",
    kinetics = Arrhenius(A=(0.00310834,'m^3/(mol*s)'), n=2.31619, Ea=(-79.5432,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=4.2175942864557146e-16, var=0.2943661708621067, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_N-4R!H->C
    Total Standard Deviation in ln(k): 1.0876794885557737"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_N-4R!H->C
Total Standard Deviation in ln(k): 1.0876794885557737""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_N-4R!H->C
Total Standard Deviation in ln(k): 1.0876794885557737
""",
)

entry(
    index = 24,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_4CClFO->Cl",
    kinetics = Arrhenius(A=(8.68219e-05,'m^3/(mol*s)'), n=2.97056, Ea=(7.89502,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_4CClFO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_4CClFO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_4CClFO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_4CClFO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl",
    kinetics = ArrheniusBM(A=(4.18864e-27,'m^3/(mol*s)'), n=9.22532, w0=(523250,'J/mol'), E0=(21513.5,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6221926323009443, var=6.186682839180891, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl
    Total Standard Deviation in ln(k): 6.549684313298245"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl
Total Standard Deviation in ln(k): 6.549684313298245""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl
Total Standard Deviation in ln(k): 6.549684313298245
""",
)

entry(
    index = 26,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O",
    kinetics = Arrhenius(A=(2.12789e-07,'m^3/(mol*s)'), n=3.23493, Ea=(137.926,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-5.038619307552427e-15, var=211.67435572753095, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O
    Total Standard Deviation in ln(k): 29.166956417817097"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O
Total Standard Deviation in ln(k): 29.166956417817097""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O
Total Standard Deviation in ln(k): 29.166956417817097
""",
)

entry(
    index = 27,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1106.35,'m^3/(mol*s)'), n=0.603027, w0=(572500,'J/mol'), E0=(136674,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.28581201102463416, var=5.4824686992705765, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O
    Total Standard Deviation in ln(k): 5.41214208078228"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O
Total Standard Deviation in ln(k): 5.41214208078228""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O
Total Standard Deviation in ln(k): 5.41214208078228
""",
)

entry(
    index = 28,
    label = "Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R",
    kinetics = Arrhenius(A=(1.54e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_Sp-2R=1C_Ext-2R-R
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
    index = 29,
    label = "Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R",
    kinetics = Arrhenius(A=(4.7e+09,'m^3/(mol*s)'), n=-0.823, Ea=(0.096232,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-1C-R_N-Sp-2R=1C_Ext-2R-R
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
    index = 30,
    label = "Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R",
    kinetics = Arrhenius(A=(1.85e+09,'m^3/(mol*s)'), n=-0.7, Ea=(-0.281165,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_3R->C_Ext-4R!H-R
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
    index = 31,
    label = "Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R",
    kinetics = Arrhenius(A=(7.6e+06,'m^3/(mol*s)'), n=0, Ea=(0.4184,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->C_Ext-2R-R_N-3R->C_Ext-2R-R
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
    index = 32,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.2412e-05,'m^3/(mol*s)'), n=3.07293, w0=(572500,'J/mol'), E0=(157072,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.33631353739567954, var=705.9390473680345, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 54.10984458091803"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 54.10984458091803""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 54.10984458091803
""",
)

entry(
    index = 33,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R",
    kinetics = ArrheniusBM(A=(3361.38,'m^3/(mol*s)'), n=0.562546, w0=(572500,'J/mol'), E0=(99718.2,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4502840599014801, var=7.056833173820324, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R
    Total Standard Deviation in ln(k): 6.456885693796707"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R
Total Standard Deviation in ln(k): 6.456885693796707""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R
Total Standard Deviation in ln(k): 6.456885693796707
""",
)

entry(
    index = 34,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_N-4R!H->C_Ext-5R!H-R",
    kinetics = Arrhenius(A=(0.0012042,'m^3/(mol*s)'), n=2.3973, Ea=(-81.1746,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_N-4R!H->C_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_N-4R!H->C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_N-4R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_N-4R!H->C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C",
    kinetics = ArrheniusBM(A=(3.57904e-20,'m^3/(mol*s)'), n=7.10843, w0=(498625,'J/mol'), E0=(38339.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.30875733744126155, var=3.774398665489801, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C
    Total Standard Deviation in ln(k): 4.670533759173948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C
Total Standard Deviation in ln(k): 4.670533759173948""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C
Total Standard Deviation in ln(k): 4.670533759173948
""",
)

entry(
    index = 36,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_N-1R->C",
    kinetics = ArrheniusBM(A=(1.9185e-28,'m^3/(mol*s)'), n=9.62535, w0=(572500,'J/mol'), E0=(19147.6,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8386173492855382, var=89.94821518002225, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_N-1R->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_N-1R->C
    Total Standard Deviation in ln(k): 21.120193306403337"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_N-1R->C
Total Standard Deviation in ln(k): 21.120193306403337""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_N-1R->C
Total Standard Deviation in ln(k): 21.120193306403337
""",
)

entry(
    index = 37,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(2.57068e-10,'m^3/(mol*s)'), n=4.0012, w0=(572500,'J/mol'), E0=(117610,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.9425259231974631, var=0.5426107518291939, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 3.84488588925859"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.84488588925859""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 3.84488588925859
""",
)

entry(
    index = 38,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-6R!H-R",
    kinetics = Arrhenius(A=(1.15698e-06,'m^3/(mol*s)'), n=3.09659, Ea=(41.7143,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-6R!H-R
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
    kinetics = ArrheniusBM(A=(0.0711577,'m^3/(mol*s)'), n=1.78642, w0=(572500,'J/mol'), E0=(115669,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.48915167951968164, var=3.504724156362121, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R
    Total Standard Deviation in ln(k): 4.9820705185212395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 4.9820705185212395""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 4.9820705185212395
""",
)

entry(
    index = 40,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R",
    kinetics = Arrhenius(A=(2.25175e-06,'m^3/(mol*s)'), n=3.12644, Ea=(164.45,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-5BrCClFILiNPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-5R!H-R_6R!H->C",
    kinetics = Arrhenius(A=(0.00828286,'m^3/(mol*s)'), n=2.34779, Ea=(55.5774,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-5R!H-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-5R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-5R!H-R_N-6R!H->C",
    kinetics = Arrhenius(A=(2.67496e-08,'m^3/(mol*s)'), n=3.75287, Ea=(187.312,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-5R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-5R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O",
    kinetics = ArrheniusBM(A=(3.33198e-07,'m^3/(mol*s)'), n=3.35824, w0=(572500,'J/mol'), E0=(78725.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7021832608712043, var=0.41675860888694344, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O
    Total Standard Deviation in ln(k): 3.058473243601828"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O
Total Standard Deviation in ln(k): 3.058473243601828""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O
Total Standard Deviation in ln(k): 3.058473243601828
""",
)

entry(
    index = 44,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_N-6R!H->O",
    kinetics = Arrhenius(A=(3.87031e-05,'m^3/(mol*s)'), n=3.04873, Ea=(22.9526,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_N-6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_N-6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_N-6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_Ext-1C-R",
    kinetics = Arrhenius(A=(4.10298e-06,'m^3/(mol*s)'), n=3.07477, Ea=(21.6954,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_Ext-2R-R",
    kinetics = Arrhenius(A=(1.01799e-05,'m^3/(mol*s)'), n=2.87159, Ea=(40.5376,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_2R->C",
    kinetics = Arrhenius(A=(2.07011e-05,'m^3/(mol*s)'), n=2.98446, Ea=(43.7961,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_N-2R->C",
    kinetics = Arrhenius(A=(4.81575e-05,'m^3/(mol*s)'), n=2.76922, Ea=(37.8393,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_1R->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_N-1R->C_Ext-3R-R",
    kinetics = Arrhenius(A=(0.00491008,'m^3/(mol*s)'), n=2.38401, Ea=(88.3837,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_N-1R->C_Ext-3R-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_N-1R->C_Ext-3R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_N-1R->C_Ext-3R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_N-4R!H->Br_N-4CClFO->Cl_N-1R->C_Ext-3R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C",
    kinetics = ArrheniusBM(A=(1.657e-11,'m^3/(mol*s)'), n=4.33286, w0=(572500,'J/mol'), E0=(112849,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.8465175727437481, var=2.4434345313971364, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C
    Total Standard Deviation in ln(k): 5.260628036421414"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 5.260628036421414""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 5.260628036421414
""",
)

entry(
    index = 51,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C",
    kinetics = Arrhenius(A=(2.95732e-08,'m^3/(mol*s)'), n=3.42975, Ea=(205.997,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_N-9R!H->C
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
    index = 52,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C",
    kinetics = ArrheniusBM(A=(3.98222e-05,'m^3/(mol*s)'), n=2.70597, w0=(572500,'J/mol'), E0=(112396,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.589832865664426, var=0.2723554110138554, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 2.5282168837751797"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 2.5282168837751797""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 2.5282168837751797
""",
)

entry(
    index = 53,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_N-5BrCClFILiNPSSi->C",
    kinetics = Arrhenius(A=(0.000352549,'m^3/(mol*s)'), n=2.48352, Ea=(177.184,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_N-5BrCClFILiNPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_N-5BrCClFILiNPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_N-5BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_N-5BrCClFILiNPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C",
    kinetics = ArrheniusBM(A=(6.12805e-07,'m^3/(mol*s)'), n=3.30623, w0=(572500,'J/mol'), E0=(78964.4,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7324852241880312, var=0.06828575048354131, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C
    Total Standard Deviation in ln(k): 2.3642833316159972"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C
Total Standard Deviation in ln(k): 2.3642833316159972""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C
Total Standard Deviation in ln(k): 2.3642833316159972
""",
)

entry(
    index = 55,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_N-8R!H->C",
    kinetics = Arrhenius(A=(5.63836e-08,'m^3/(mol*s)'), n=3.53169, Ea=(61.6704,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C",
    kinetics = Arrhenius(A=(9.06356e-06,'m^3/(mol*s)'), n=2.60924, Ea=(181.13,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_10R!H->C
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
    index = 57,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C",
    kinetics = Arrhenius(A=(5.08293e-09,'m^3/(mol*s)'), n=3.69996, Ea=(221.959,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_5R!H->O_Ext-5O-R_Ext-2R-R_Ext-6R!H-R_Ext-6R!H-R_Ext-6R!H-R_Ext-8R!H-R_9R!H->C_Ext-9C-R_N-10R!H->C
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
    index = 58,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(4.64857e-05,'m^3/(mol*s)'), n=2.69436, w0=(572500,'J/mol'), E0=(112934,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5944663503659965, var=0.9376777933368773, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 3.434894488402427"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 3.434894488402427""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 3.434894488402427
""",
)

entry(
    index = 59,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(2.81961e-05,'m^3/(mol*s)'), n=2.73363, Ea=(177.495,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = Arrhenius(A=(2.21234e-06,'m^3/(mol*s)'), n=3.11884, Ea=(61.5712,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = Arrhenius(A=(1.7641e-07,'m^3/(mol*s)'), n=3.48883, Ea=(61.0651,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_Sp-4R!H-3R_Ext-4R!H-R_4R!H->C_Ext-3R-R_6R!H->O_Ext-6O-R_Ext-7R!H-R_Ext-6O-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-8R!H-R_Ext-6O-R_Ext-6O-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(6.58773e-05,'m^3/(mol*s)'), n=2.61294, Ea=(182.613,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(4.67866e-05,'m^3/(mol*s)'), n=2.73161, Ea=(179.832,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-3R-R_N-Sp-4R!H-3R_Ext-2R-R_N-5R!H->O_Ext-2R-R_5BrCClFILiNPSSi->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

