#!/usr/bin/env python
# encoding: utf-8

name = "CO2_Elimination_From_Carboxylic_Acid/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = Arrhenius(A=(1.5451e-09,'s^-1'), n=6.16571, Ea=(141.549,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-2.2654506452962126e-15, var=1.272793823822732, Tref=1000.0, N=7, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 7 training reactions at node Root
    Total Standard Deviation in ln(k): 2.2617053171441315"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 2.2617053171441315""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root
Total Standard Deviation in ln(k): 2.2617053171441315
""",
)

entry(
    index = 2,
    label = "Root_Ext-2R-R",
    kinetics = Arrhenius(A=(3.09757e-08,'s^-1'), n=5.795, Ea=(148.162,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-4.5831191246152106e-15, var=0.06445785928019568, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-2R-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-2R-R
    Total Standard Deviation in ln(k): 0.5089732155400254"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-2R-R
Total Standard Deviation in ln(k): 0.5089732155400254""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-2R-R
Total Standard Deviation in ln(k): 0.5089732155400254
""",
)

entry(
    index = 3,
    label = "Root_Ext-2R-R_7R!H->F",
    kinetics = Arrhenius(A=(5.85e-12,'s^-1'), n=6.85, Ea=(136.108,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_7R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_7R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_7R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_Ext-2R-R_N-7R!H->F",
    kinetics = Arrhenius(A=(1.72105e-07,'s^-1'), n=5.584, Ea=(150.573,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-3.75647064446989e-15, var=0.0749712632054184, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-2R-R_N-7R!H->F
    Total Standard Deviation in ln(k): 0.548914121410332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-2R-R_N-7R!H->F
Total Standard Deviation in ln(k): 0.548914121410332""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-2R-R_N-7R!H->F
Total Standard Deviation in ln(k): 0.548914121410332
""",
)

entry(
    index = 5,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R",
    kinetics = Arrhenius(A=(6.89952e-07,'s^-1'), n=5.41, Ea=(152.637,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=1.6495479875915685e-15, var=0.16969764973346085, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R
    Total Standard Deviation in ln(k): 0.8258380771907274"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.8258380771907274""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R
Total Standard Deviation in ln(k): 0.8258380771907274
""",
)

entry(
    index = 6,
    label = "Root_Ext-2R-R_N-7R!H->F_6F1sH->H",
    kinetics = ArrheniusBM(A=(181000,'s^-1'), n=2.09, w0=(828.5,'kJ/mol'), E0=(191.012,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_6F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_6F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H",
    kinetics = Arrhenius(A=(2.54e-21,'s^-1'), n=9.6, Ea=(116.332,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_N-6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C",
    kinetics = ArrheniusBM(A=(0.00202536,'s^-1'), n=4.39922, w0=(828.5,'kJ/mol'), E0=(157.642,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.5914123253367701, var=33.04804209529663, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C
    Total Standard Deviation in ln(k): 13.010666664655005"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 13.010666664655005""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C
Total Standard Deviation in ln(k): 13.010666664655005
""",
)

entry(
    index = 9,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_N-9R!H->C",
    kinetics = Arrhenius(A=(1.15e-12,'s^-1'), n=7.1, Ea=(136.768,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H",
    kinetics = ArrheniusBM(A=(1.36e+06,'s^-1'), n=1.81, w0=(828.5,'kJ/mol'), E0=(194.626,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H",
    kinetics = Arrhenius(A=(2.1e-13,'s^-1'), n=7.32, Ea=(137.634,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-2R-R_N-7R!H->F_Ext-7BrCClINOPSSi-R_Ext-8R!H-R_9R!H->C_N-6F1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

