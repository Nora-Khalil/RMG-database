#!/usr/bin/env python
# encoding: utf-8

name = "PFAS_Hydrolysis/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = Arrhenius(A=(3.02515e-09,'m^3/(mol*s)'), n=3.9281, Ea=(244.327,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-2.570724136506341e-15, var=195.88619142638808, Tref=1000.0, N=21, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 21 training reactions at node Root
    Total Standard Deviation in ln(k): 28.05814147032896"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root
Total Standard Deviation in ln(k): 28.05814147032896""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root
Total Standard Deviation in ln(k): 28.05814147032896
""",
)

entry(
    index = 2,
    label = "Root_3F1sH->F1s",
    kinetics = ArrheniusBM(A=(1.43058e-06,'m^3/(mol*s)'), n=3.12583, w0=(933.5,'kJ/mol'), E0=(217.665,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23540423897181106, var=96.14993083317114, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_3F1sH->F1s',), comment="""BM rule fitted to 15 training reactions at node Root_3F1sH->F1s
    Total Standard Deviation in ln(k): 20.24911246950965"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_3F1sH->F1s
Total Standard Deviation in ln(k): 20.24911246950965""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_3F1sH->F1s
Total Standard Deviation in ln(k): 20.24911246950965
""",
)

entry(
    index = 3,
    label = "Root_N-3F1sH->F1s",
    kinetics = Arrhenius(A=(1.80508e-12,'m^3/(mol*s)'), n=4.94167, Ea=(349.875,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-8.997534477772192e-16, var=220.93193224490267, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3F1sH->F1s',), comment="""BM rule fitted to 6 training reactions at node Root_N-3F1sH->F1s
    Total Standard Deviation in ln(k): 29.797939554224715"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-3F1sH->F1s
Total Standard Deviation in ln(k): 29.797939554224715""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-3F1sH->F1s
Total Standard Deviation in ln(k): 29.797939554224715
""",
)

entry(
    index = 4,
    label = "Root_3F1sH->F1s_4R->F",
    kinetics = ArrheniusBM(A=(7.89108e-07,'m^3/(mol*s)'), n=3.21413, w0=(933.5,'kJ/mol'), E0=(305.952,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.14439141369714276, var=184.8915990867023, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F',), comment="""BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_4R->F
    Total Standard Deviation in ln(k): 27.62214769670099"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_4R->F
Total Standard Deviation in ln(k): 27.62214769670099""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_4R->F
Total Standard Deviation in ln(k): 27.62214769670099
""",
)

entry(
    index = 5,
    label = "Root_3F1sH->F1s_N-4R->F",
    kinetics = ArrheniusBM(A=(3.59191e-07,'m^3/(mol*s)'), n=3.2926, w0=(933.5,'kJ/mol'), E0=(183.802,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2854674186772857, var=28.68452758197169, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F',), comment="""BM rule fitted to 11 training reactions at node Root_3F1sH->F1s_N-4R->F
    Total Standard Deviation in ln(k): 11.454202585172888"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_3F1sH->F1s_N-4R->F
Total Standard Deviation in ln(k): 11.454202585172888""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_3F1sH->F1s_N-4R->F
Total Standard Deviation in ln(k): 11.454202585172888
""",
)

entry(
    index = 6,
    label = "Root_N-3F1sH->F1s_4R->H",
    kinetics = Arrhenius(A=(4.21772e-12,'m^3/(mol*s)'), n=4.9125, Ea=(403.136,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-4.048890514997486e-15, var=218.72360481013018, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H',), comment="""BM rule fitted to 4 training reactions at node Root_N-3F1sH->F1s_4R->H
    Total Standard Deviation in ln(k): 29.648642734871736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-3F1sH->F1s_4R->H
Total Standard Deviation in ln(k): 29.648642734871736""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-3F1sH->F1s_4R->H
Total Standard Deviation in ln(k): 29.648642734871736
""",
)

entry(
    index = 7,
    label = "Root_N-3F1sH->F1s_N-4R->H",
    kinetics = Arrhenius(A=(3.30624e-13,'m^3/(mol*s)'), n=5, Ea=(243.351,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.2933955811797526e-15, var=0.31031412803920555, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3F1sH->F1s_N-4R->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_N-4R->H
    Total Standard Deviation in ln(k): 1.1167546352479913"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_N-4R->H
Total Standard Deviation in ln(k): 1.1167546352479913""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_N-4R->H
Total Standard Deviation in ln(k): 1.1167546352479913
""",
)

entry(
    index = 8,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.05095e-07,'m^3/(mol*s)'), n=3.44969, w0=(933.5,'kJ/mol'), E0=(350.482,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11424386486741601, var=0.17687060504801752, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.130156012026342"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.130156012026342""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.130156012026342
""",
)

entry(
    index = 9,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H",
    kinetics = ArrheniusBM(A=(3.68755e-06,'m^3/(mol*s)'), n=3.19922, w0=(933.5,'kJ/mol'), E0=(232.662,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17731783347351104, var=64.43917074282453, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H',), comment="""BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H
    Total Standard Deviation in ln(k): 16.53833505015124"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H
Total Standard Deviation in ln(k): 16.53833505015124""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H
Total Standard Deviation in ln(k): 16.53833505015124
""",
)

entry(
    index = 10,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H",
    kinetics = ArrheniusBM(A=(1.75761e-09,'m^3/(mol*s)'), n=3.84232, w0=(933.5,'kJ/mol'), E0=(151.493,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.38983648738716925, var=2.8510662036288443, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H',), comment="""BM rule fitted to 7 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H
    Total Standard Deviation in ln(k): 4.364503996257688"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H
Total Standard Deviation in ln(k): 4.364503996257688""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H
Total Standard Deviation in ln(k): 4.364503996257688
""",
)

entry(
    index = 11,
    label = "Root_N-3F1sH->F1s_4R->H_Ext-1C-R",
    kinetics = Arrhenius(A=(1.69161e-12,'m^3/(mol*s)'), n=4.93333, Ea=(381.31,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.7995068955544384e-15, var=368.757286781224, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R
    Total Standard Deviation in ln(k): 38.497036148082216"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R
Total Standard Deviation in ln(k): 38.497036148082216""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R
Total Standard Deviation in ln(k): 38.497036148082216
""",
)

entry(
    index = 12,
    label = "Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R",
    kinetics = Arrhenius(A=(2.56e-13,'m^3/(mol*s)'), n=5.03, Ea=(241.31,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_N-4R->H_Ext-4CF-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.75863e-08,'m^3/(mol*s)'), n=3.56448, w0=(933.5,'kJ/mol'), E0=(343.352,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12926701701687024, var=0.5979954658498097, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 1.875056474257757"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 1.875056474257757""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 1.875056474257757
""",
)

entry(
    index = 14,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(6.1125e-06,'m^3/(mol*s)'), n=3.22, w0=(933.5,'kJ/mol'), E0=(364.742,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.23566e-06,'m^3/(mol*s)'), n=3.12804, w0=(933.5,'kJ/mol'), E0=(219.457,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1919167921591581, var=109.29372123069817, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R
    Total Standard Deviation in ln(k): 21.44043269894466"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R
Total Standard Deviation in ln(k): 21.44043269894466""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R
Total Standard Deviation in ln(k): 21.44043269894466
""",
)

entry(
    index = 16,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.63316e-09,'m^3/(mol*s)'), n=3.836, w0=(933.5,'kJ/mol'), E0=(154.191,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4048869721399211, var=1.4148588836064402, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R',), comment="""BM rule fitted to 6 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R
    Total Standard Deviation in ln(k): 3.401893038849115"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R
Total Standard Deviation in ln(k): 3.401893038849115""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R
Total Standard Deviation in ln(k): 3.401893038849115
""",
)

entry(
    index = 17,
    label = "Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(5.62739e-12,'m^3/(mol*s)'), n=4.88187, w0=(830,'kJ/mol'), E0=(403.276,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4358985115299699, var=5.184484677090042, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 5.659896606344689"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 5.659896606344689""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 5.659896606344689
""",
)

entry(
    index = 18,
    label = "Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(1.6075e-13,'m^3/(mol*s)'), n=5.03, Ea=(244.582,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(5.64167e-09,'m^3/(mol*s)'), n=3.77, w0=(933.5,'kJ/mol'), E0=(341.667,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(2.48333e-07,'m^3/(mol*s)'), n=3.36, w0=(933.5,'kJ/mol'), E0=(345.028,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_4R->F_Ext-1C-R_Ext-1C-R_7R!H->C_Ext-7C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.48217e-06,'m^3/(mol*s)'), n=3.2847, w0=(933.5,'kJ/mol'), E0=(255.158,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1540170364824906, var=1.3921655949535954, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C
    Total Standard Deviation in ln(k): 2.752365742891332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 2.752365742891332""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C
Total Standard Deviation in ln(k): 2.752365742891332
""",
)

entry(
    index = 22,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(4.305e-07,'m^3/(mol*s)'), n=3.26, w0=(933.5,'kJ/mol'), E0=(144.118,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.42588e-09,'m^3/(mol*s)'), n=3.84875, w0=(933.5,'kJ/mol'), E0=(156.347,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.446171756736079, var=1.0626160556577413, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C
    Total Standard Deviation in ln(k): 3.1875810375394575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 3.1875810375394575""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 3.1875810375394575
""",
)

entry(
    index = 24,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.285e-08,'m^3/(mol*s)'), n=3.6, w0=(933.5,'kJ/mol'), E0=(144.915,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R",
    kinetics = ArrheniusBM(A=(1.21667e-12,'m^3/(mol*s)'), n=4.98, w0=(830,'kJ/mol'), E0=(402.608,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3F1sH->F1s_4R->H_Ext-1C-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R",
    kinetics = ArrheniusBM(A=(7.3e-07,'m^3/(mol*s)'), n=3.33, w0=(933.5,'kJ/mol'), E0=(255.119,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_4CH->H_Ext-1C-R_7R!H->C_Ext-7C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(1.4517e-09,'m^3/(mol*s)'), n=3.84466, w0=(933.5,'kJ/mol'), E0=(158.991,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.4850583044966158, var=0.5794415510473455, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 2.7447650147364535"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 2.7447650147364535""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 2.7447650147364535
""",
)

entry(
    index = 28,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(4.615e-09,'m^3/(mol*s)'), n=3.71, w0=(933.5,'kJ/mol'), E0=(147.126,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = ArrheniusBM(A=(1.68159e-09,'m^3/(mol*s)'), n=3.82474, w0=(933.5,'kJ/mol'), E0=(161.648,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5495230148809352, var=0.1698912722471196, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 2.207020170072092"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 2.207020170072092""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 2.207020170072092
""",
)

entry(
    index = 30,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = ArrheniusBM(A=(1.335e-09,'m^3/(mol*s)'), n=3.86, w0=(933.5,'kJ/mol'), E0=(151.411,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C",
    kinetics = ArrheniusBM(A=(1.49519e-09,'m^3/(mol*s)'), n=3.83388, w0=(933.5,'kJ/mol'), E0=(162.234,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.6737934600289128, var=0.4443677318010403, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
    Total Standard Deviation in ln(k): 3.0293230972556895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 3.0293230972556895""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C
Total Standard Deviation in ln(k): 3.0293230972556895
""",
)

entry(
    index = 32,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C",
    kinetics = ArrheniusBM(A=(2.24e-09,'m^3/(mol*s)'), n=3.8, w0=(933.5,'kJ/mol'), E0=(160.532,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C",
    kinetics = ArrheniusBM(A=(2.545e-09,'m^3/(mol*s)'), n=3.78, w0=(933.5,'kJ/mol'), E0=(162.332,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C",
    kinetics = ArrheniusBM(A=(9.35e-10,'m^3/(mol*s)'), n=3.88, w0=(933.5,'kJ/mol'), E0=(162.203,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3F1sH->F1s_N-4R->F_N-4CH->H_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C_Ext-9C-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

