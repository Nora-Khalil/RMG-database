#!/usr/bin/env python
# encoding: utf-8

name = "XY_Addition_MultipleBond/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = Arrhenius(A=(2.66085e-10,'m^3/(mol*s)'), n=4.42669, Ea=(171.978,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=5.177180883347417, var=64.2942429028851, Tref=1000.0, N=66, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 66 training reactions at node Root
    Total Standard Deviation in ln(k): 29.082697952358057"""),
    rank = 11,
    shortDesc = """BM rule fitted to 66 training reactions at node Root
Total Standard Deviation in ln(k): 29.082697952358057""",
    longDesc = 
"""
BM rule fitted to 66 training reactions at node Root
Total Standard Deviation in ln(k): 29.082697952358057
""",
)

entry(
    index = 2,
    label = "Root_2Br1sCl1sF1sH->H",
    kinetics = Arrhenius(A=(1.58276e-34,'m^3/(mol*s)'), n=11.4288, Ea=(151.279,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-2.3978429383262894e-14, var=73.86978362074643, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H',), comment="""BM rule fitted to 20 training reactions at node Root_2Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 17.23020334425648"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 17.23020334425648""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 17.23020334425648
""",
)

entry(
    index = 3,
    label = "Root_N-2Br1sCl1sF1sH->H",
    kinetics = Arrhenius(A=(9.07595,'m^3/(mol*s)'), n=1.38229, Ea=(180.977,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=8.742178028591693, var=44.43344979502941, Tref=1000.0, N=46, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H',), comment="""BM rule fitted to 46 training reactions at node Root_N-2Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 35.328518740383714"""),
    rank = 11,
    shortDesc = """BM rule fitted to 46 training reactions at node Root_N-2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 35.328518740383714""",
    longDesc = 
"""
BM rule fitted to 46 training reactions at node Root_N-2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 35.328518740383714
""",
)

entry(
    index = 4,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H",
    kinetics = Arrhenius(A=(6.91734e-51,'m^3/(mol*s)'), n=16.2669, Ea=(196.268,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=5.719861203726608e-15, var=14.882279556975556, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H',), comment="""BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 7.733778305904556"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 7.733778305904556""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 7.733778305904556
""",
)

entry(
    index = 5,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H",
    kinetics = Arrhenius(A=(1.01944e-25,'m^3/(mol*s)'), n=8.82369, Ea=(127.055,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.1489159410078335e-14, var=19.193810893548722, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H',), comment="""BM rule fitted to 13 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 8.78289306766849"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 8.78289306766849""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 8.78289306766849
""",
)

entry(
    index = 6,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s",
    kinetics = Arrhenius(A=(0.021302,'m^3/(mol*s)'), n=2.10088, Ea=(197.884,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=7.772080499672817, var=16.55607655264384, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 19 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 27.68493887115633"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 27.68493887115633""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 27.68493887115633
""",
)

entry(
    index = 7,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(2.72448e-07,'m^3/(mol*s)'), n=3.69681, w0=(696.037,'kJ/mol'), E0=(164.04,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5840965477385872, var=49.789097033774866, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 27 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 15.61326855130901"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 15.61326855130901""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 15.61326855130901
""",
)

entry(
    index = 8,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd",
    kinetics = Arrhenius(A=(4.93692e-45,'m^3/(mol*s)'), n=14.6587, Ea=(237.299,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-5.806221467687367e-15, var=0.6217489163885642, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 1.5807547952531646"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 1.5807547952531646""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 1.5807547952531646
""",
)

entry(
    index = 9,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd",
    kinetics = Arrhenius(A=(1.08455e-58,'m^3/(mol*s)'), n=18.4112, Ea=(141.559,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-2.3993425274059177e-15, var=3.50354823365654, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 3.752416524813781"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 3.752416524813781""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 3.752416524813781
""",
)

entry(
    index = 10,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(7.03268e-31,'m^3/(mol*s)'), n=10.3464, Ea=(144.205,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=2.5493014353687877e-15, var=8.766926873416574, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 5.935819435055477"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 5.935819435055477""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 5.935819435055477
""",
)

entry(
    index = 11,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd",
    kinetics = Arrhenius(A=(2.4889e-27,'m^3/(mol*s)'), n=9.43559, Ea=(127.721,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd",
    kinetics = Arrhenius(A=(2.74366e-20,'m^3/(mol*s)'), n=7.19899, Ea=(109.795,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=2.5493014353687877e-15, var=7.930699220877809, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 5.645634118129398"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 5.645634118129398""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 5.645634118129398
""",
)

entry(
    index = 13,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(7.39604e-06,'m^3/(mol*s)'), n=3.08253, Ea=(200.216,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=7.0738787522901925, var=6.625696999199499, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 22.93383885428921"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 22.93383885428921""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 22.93383885428921
""",
)

entry(
    index = 14,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct",
    kinetics = Arrhenius(A=(2.57016e+31,'m^3/(mol*s)'), n=-7.53001, Ea=(301.787,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct",
    kinetics = ArrheniusBM(A=(7.69995e-06,'m^3/(mol*s)'), n=3.26448, w0=(897.333,'kJ/mol'), E0=(176.857,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.7032922893991234, var=129.1552837793603, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct
    Total Standard Deviation in ln(k): 27.062742613786018"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 27.062742613786018""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct
Total Standard Deviation in ln(k): 27.062742613786018
""",
)

entry(
    index = 16,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s",
    kinetics = ArrheniusBM(A=(5.93272e-05,'m^3/(mol*s)'), n=2.63647, w0=(575,'kJ/mol'), E0=(143.795,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s",
    kinetics = ArrheniusBM(A=(2.51165e-07,'m^3/(mol*s)'), n=3.71207, w0=(700.692,'kJ/mol'), E0=(164.286,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.5919033609206577, var=50.79754736408883, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s',), comment="""BM rule fitted to 26 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s
    Total Standard Deviation in ln(k): 15.775422033992045"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 15.775422033992045""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s
Total Standard Deviation in ln(k): 15.775422033992045
""",
)

entry(
    index = 18,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(1.21533e-40,'m^3/(mol*s)'), n=13.3404, Ea=(247.821,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=4.395670489661623e-15, var=0.2604925944054029, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 1.0231862139882297"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 1.0231862139882297""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 1.0231862139882297
""",
)

entry(
    index = 19,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R",
    kinetics = Arrhenius(A=(4.79811e-59,'m^3/(mol*s)'), n=18.4562, Ea=(143.294,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.1809264002076e-15, var=0.24993616492162954, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R
    Total Standard Deviation in ln(k): 1.0022395581061199"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R
Total Standard Deviation in ln(k): 1.0022395581061199""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R
Total Standard Deviation in ln(k): 1.0022395581061199
""",
)

entry(
    index = 20,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O",
    kinetics = Arrhenius(A=(4.42709e-31,'m^3/(mol*s)'), n=10.3673, Ea=(150.06,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=2.4743219813873527e-15, var=10.588577462665173, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O',), comment="""BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O
    Total Standard Deviation in ln(k): 6.523426874874019"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O
Total Standard Deviation in ln(k): 6.523426874874019""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O
Total Standard Deviation in ln(k): 6.523426874874019
""",
)

entry(
    index = 21,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O",
    kinetics = Arrhenius(A=(1.7747e-30,'m^3/(mol*s)'), n=10.3046, Ea=(132.493,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=4.034831867375967e-15, var=0.07825253831463978, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O
    Total Standard Deviation in ln(k): 0.560797677470466"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O
Total Standard Deviation in ln(k): 0.560797677470466""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O
Total Standard Deviation in ln(k): 0.560797677470466
""",
)

entry(
    index = 22,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R",
    kinetics = Arrhenius(A=(1.59698e-20,'m^3/(mol*s)'), n=7.24665, Ea=(112.595,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=2.6092849985539355e-15, var=7.227740380242292, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R',), comment="""BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R
    Total Standard Deviation in ln(k): 5.38962143514485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R
Total Standard Deviation in ln(k): 5.38962143514485""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R
Total Standard Deviation in ln(k): 5.38962143514485
""",
)

entry(
    index = 23,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(1.26987e-18,'m^3/(mol*s)'), n=6.7386, Ea=(174.694,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=6.851499578265867, var=3.382486178571792, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 20.901838912336032"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 20.901838912336032""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 20.901838912336032
""",
)

entry(
    index = 24,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2029.2,'m^3/(mol*s)'), n=0.783867, w0=(852.75,'kJ/mol'), E0=(253.649,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-3.126609618874954, var=30.76618011360788, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C
    Total Standard Deviation in ln(k): 18.975521190109983"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 18.975521190109983""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 18.975521190109983
""",
)

entry(
    index = 25,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(116.28,'m^3/(mol*s)'), n=1.10103, w0=(858.5,'kJ/mol'), E0=(260.264,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.468039065173333, var=12.956440840012434, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C
    Total Standard Deviation in ln(k): 10.90459557909581"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.90459557909581""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.90459557909581
""",
)

entry(
    index = 26,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d",
    kinetics = ArrheniusBM(A=(7.2121e-08,'m^3/(mol*s)'), n=3.97622, w0=(975,'kJ/mol'), E0=(139.614,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-4.001394183593172, var=42.86692184236844, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d
    Total Standard Deviation in ln(k): 23.179323218075133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d
Total Standard Deviation in ln(k): 23.179323218075133""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d
Total Standard Deviation in ln(k): 23.179323218075133
""",
)

entry(
    index = 27,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d",
    kinetics = ArrheniusBM(A=(172.263,'m^3/(mol*s)'), n=0.999089, w0=(858.5,'kJ/mol'), E0=(234.51,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.3350239494678902, var=9.480572936792417, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d',), comment="""BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d
    Total Standard Deviation in ln(k): 9.52701889560153"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d
Total Standard Deviation in ln(k): 9.52701889560153""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d
Total Standard Deviation in ln(k): 9.52701889560153
""",
)

entry(
    index = 28,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(0.415759,'m^3/(mol*s)'), n=1.80821, w0=(693,'kJ/mol'), E0=(204.05,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20327991062227035, var=13.653669162845564, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 18 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 7.918424399581313"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 7.918424399581313""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 7.918424399581313
""",
)

entry(
    index = 29,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd",
    kinetics = Arrhenius(A=(288.28,'m^3/(mol*s)'), n=1.17797, Ea=(168.451,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-0.6150095239471267, var=3.285845520463147, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 8 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 5.1792135554496745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 5.1792135554496745""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 5.1792135554496745
""",
)

entry(
    index = 30,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C",
    kinetics = Arrhenius(A=(2.00663e-58,'m^3/(mol*s)'), n=18.5017, Ea=(200.636,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C",
    kinetics = Arrhenius(A=(9.45813e-32,'m^3/(mol*s)'), n=10.7598, Ea=(271.413,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=2.263442267064567e-15, var=0.04724858379782651, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C
    Total Standard Deviation in ln(k): 0.43576403861953117"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.43576403861953117""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.43576403861953117
""",
)

entry(
    index = 32,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-5R!H-R",
    kinetics = Arrhenius(A=(1.61903e-58,'m^3/(mol*s)'), n=18.2608, Ea=(143.651,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(8.1309e-33,'m^3/(mol*s)'), n=10.8531, Ea=(136.003,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-3.936421334025334e-15, var=5.235215607081033, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 4.586952845972053"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 4.586952845972053""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 4.586952845972053
""",
)

entry(
    index = 34,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O_Ext-3COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(1.88854e-35,'m^3/(mol*s)'), n=11.7495, Ea=(119.448,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O_Ext-3COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O_Ext-3COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_N-5R!H->O_Ext-3COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 35,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R",
    kinetics = Arrhenius(A=(1.28651e-21,'m^3/(mol*s)'), n=7.55997, Ea=(115.824,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=1.6870377145822858e-15, var=4.425036247275305, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R',), comment="""BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R
    Total Standard Deviation in ln(k): 4.217114624842865"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R
Total Standard Deviation in ln(k): 4.217114624842865""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R
Total Standard Deviation in ln(k): 4.217114624842865
""",
)

entry(
    index = 36,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(1.45694e-22,'m^3/(mol*s)'), n=7.87452, Ea=(164.087,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=7.215782560651578, var=3.473864102034971, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 21.86659330146963"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 21.86659330146963""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 21.86659330146963
""",
)

entry(
    index = 37,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_3COCdCddCtO2d->Cd",
    kinetics = ArrheniusBM(A=(3.14941,'m^3/(mol*s)'), n=1.63113, w0=(858.5,'kJ/mol'), E0=(244.653,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_N-3COCdCddCtO2d->Cd",
    kinetics = Arrhenius(A=(3.60487e+39,'m^3/(mol*s)'), n=-9.93467, Ea=(299.5,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_N-3COCdCddCtO2d->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_N-3COCdCddCtO2d->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_5R!H->C_N-3COCdCddCtO2d->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(125.266,'m^3/(mol*s)'), n=1.1096, w0=(858.5,'kJ/mol'), E0=(261.872,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=2.2421825927801793, var=22.54268582700557, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 15.151934023400578"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 15.151934023400578""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 15.151934023400578
""",
)

entry(
    index = 40,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_4COCdCddCtO2d->Cdd",
    kinetics = ArrheniusBM(A=(7.80335e-09,'m^3/(mol*s)'), n=4.28272, w0=(975,'kJ/mol'), E0=(135.897,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_4COCdCddCtO2d->Cdd',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_4COCdCddCtO2d->Cdd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_N-4COCdCddCtO2d->Cdd",
    kinetics = ArrheniusBM(A=(0.140494,'m^3/(mol*s)'), n=1.80918, w0=(975,'kJ/mol'), E0=(171.141,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_N-4COCdCddCtO2d->Cdd',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_N-4COCdCddCtO2d->Cdd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_N-4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_3CdO2d->O2d_N-4COCdCddCtO2d->Cdd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(186.02,'m^3/(mol*s)'), n=0.98704, w0=(858.5,'kJ/mol'), E0=(235.96,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.6430744923162597, var=11.605668420676011, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 10.957877551169943"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 10.957877551169943""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 10.957877551169943
""",
)

entry(
    index = 43,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(12854.1,'m^3/(mol*s)'), n=0.363006, w0=(711,'kJ/mol'), E0=(209.858,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.13092445016475623, var=2.188845897317373, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 3.294911077254892"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 3.294911077254892""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 3.294911077254892
""",
)

entry(
    index = 44,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.00593306,'m^3/(mol*s)'), n=2.39407, w0=(657,'kJ/mol'), E0=(201.372,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20958379838337265, var=23.189468236813536, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 10.180483310370724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 10.180483310370724""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 10.180483310370724
""",
)

entry(
    index = 45,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s",
    kinetics = Arrhenius(A=(1509.09,'m^3/(mol*s)'), n=0.955731, Ea=(164.703,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.45297920065729186, var=1.63383732031588, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 3.70062407031725"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 3.70062407031725""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 3.70062407031725
""",
)

entry(
    index = 46,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s",
    kinetics = Arrhenius(A=(2.00962,'m^3/(mol*s)'), n=1.84468, Ea=(179.697,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-5.399606312741216, var=80.88740450988514, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 31.596921138220473"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 31.596921138220473""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 31.596921138220473
""",
)

entry(
    index = 47,
    label = "Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R",
    kinetics = Arrhenius(A=(5.27052e-32,'m^3/(mol*s)'), n=10.824, Ea=(269.603,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_1Br1sCl1sF1sH->H_3COCdCddCtO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->C_Ext-5BrClFINOPSSi-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C",
    kinetics = Arrhenius(A=(4.7072e-32,'m^3/(mol*s)'), n=10.6641, Ea=(146.873,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.3496301716658287e-15, var=0.9738927325582215, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C
    Total Standard Deviation in ln(k): 1.9783929325818657"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C
Total Standard Deviation in ln(k): 1.9783929325818657""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C
Total Standard Deviation in ln(k): 1.9783929325818657
""",
)

entry(
    index = 49,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C",
    kinetics = Arrhenius(A=(2.426e-34,'m^3/(mol*s)'), n=11.2313, Ea=(114.264,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C",
    kinetics = Arrhenius(A=(1.57007e-22,'m^3/(mol*s)'), n=7.8069, Ea=(116.407,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=3.149137067220267e-15, var=5.44704148787925, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C
    Total Standard Deviation in ln(k): 4.678830701303669"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C
Total Standard Deviation in ln(k): 4.678830701303669""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C
Total Standard Deviation in ln(k): 4.678830701303669
""",
)

entry(
    index = 51,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_N-5R!H->C",
    kinetics = Arrhenius(A=(7.07779e-19,'m^3/(mol*s)'), n=6.81918, Ea=(114.076,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C",
    kinetics = Arrhenius(A=(1.00581e-56,'m^3/(mol*s)'), n=17.6896, Ea=(122.712,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=2.249383619443048e-16, var=0.7933951414725892, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C
    Total Standard Deviation in ln(k): 1.7856722835294994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C
Total Standard Deviation in ln(k): 1.7856722835294994""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C
Total Standard Deviation in ln(k): 1.7856722835294994
""",
)

entry(
    index = 53,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(126606,'m^3/(mol*s)'), n=0.247248, w0=(858.5,'kJ/mol'), E0=(289.294,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=4.727391208462328, var=96.91891204362884, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C
    Total Standard Deviation in ln(k): 31.613963612962447"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C
Total Standard Deviation in ln(k): 31.613963612962447""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C
Total Standard Deviation in ln(k): 31.613963612962447
""",
)

entry(
    index = 54,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F",
    kinetics = ArrheniusBM(A=(8.1991,'m^3/(mol*s)'), n=1.36893, w0=(858.5,'kJ/mol'), E0=(229.331,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.04845398419745517, var=1.725197754976297, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F
    Total Standard Deviation in ln(k): 2.7548987218074017"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F
Total Standard Deviation in ln(k): 2.7548987218074017""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F
Total Standard Deviation in ln(k): 2.7548987218074017
""",
)

entry(
    index = 55,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(4.49727,'m^3/(mol*s)'), n=1.54397, w0=(858.5,'kJ/mol'), E0=(265.753,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_N-6R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_N-6R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_N-6R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F",
    kinetics = ArrheniusBM(A=(6.06163,'m^3/(mol*s)'), n=1.35437, w0=(858.5,'kJ/mol'), E0=(211.118,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.035091495465060504, var=2.4739257353495328, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F
    Total Standard Deviation in ln(k): 3.2413608793147755"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F
Total Standard Deviation in ln(k): 3.2413608793147755""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F
Total Standard Deviation in ln(k): 3.2413608793147755
""",
)

entry(
    index = 57,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(24.851,'m^3/(mol*s)'), n=1.25249, w0=(858.5,'kJ/mol'), E0=(239.116,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(513.484,'m^3/(mol*s)'), n=0.745458, w0=(711,'kJ/mol'), E0=(208.015,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17663473519832149, var=3.301651894293219, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R
    Total Standard Deviation in ln(k): 4.086499364233209"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 4.086499364233209""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 4.086499364233209
""",
)

entry(
    index = 59,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(3.25796e+07,'m^3/(mol*s)'), n=-0.707939, w0=(711,'kJ/mol'), E0=(214.596,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.12884403577218856, var=0.8149613183060809, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 2.1335074944641392"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.1335074944641392""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 2.1335074944641392
""",
)

entry(
    index = 60,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(0.00284364,'m^3/(mol*s)'), n=2.5143, w0=(657,'kJ/mol'), E0=(210.075,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.27209892572783456, var=35.40550089394089, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R
    Total Standard Deviation in ln(k): 12.612344888310176"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 12.612344888310176""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R
Total Standard Deviation in ln(k): 12.612344888310176
""",
)

entry(
    index = 61,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(7.85783,'m^3/(mol*s)'), n=1.416, w0=(657,'kJ/mol'), E0=(183.795,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 62,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R",
    kinetics = ArrheniusBM(A=(23.95,'m^3/(mol*s)'), n=1.57664, w0=(699.5,'kJ/mol'), E0=(220.022,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.11479703517840971, var=2.2200481478295266, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R
    Total Standard Deviation in ln(k): 3.2754551443633493"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R
Total Standard Deviation in ln(k): 3.2754551443633493""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R
Total Standard Deviation in ln(k): 3.2754551443633493
""",
)

entry(
    index = 63,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R",
    kinetics = Arrhenius(A=(0.00133391,'m^3/(mol*s)'), n=2.79669, Ea=(155.174,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.8537489663478762, var=2.022167327200047, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 4.995889922174026"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 4.995889922174026""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 4.995889922174026
""",
)

entry(
    index = 64,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_3CtO2d->O2d",
    kinetics = ArrheniusBM(A=(2.0193e-06,'m^3/(mol*s)'), n=3.68936, w0=(773.5,'kJ/mol'), E0=(107.272,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_3CtO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_3CtO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_N-3CtO2d->O2d",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=-8.49602e-09, w0=(645.5,'kJ/mol'), E0=(276.05,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_N-3CtO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_N-3CtO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_N-3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_N-3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = Arrhenius(A=(6.67386e-32,'m^3/(mol*s)'), n=10.6691, Ea=(147.163,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = Arrhenius(A=(3.32008e-32,'m^3/(mol*s)'), n=10.6591, Ea=(146.583,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_Ext-4COCdCddCtO2d-R_5R!H->O_Ext-3COCdCddCtO2d-R_Ext-5O-R_Ext-7R!H-R_Ext-5O-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_Ext-8R!H-R_Ext-5O-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C",
    kinetics = Arrhenius(A=(1.35617e-22,'m^3/(mol*s)'), n=7.8294, Ea=(121.12,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=1.7995068955544384e-15, var=11.898295581002191, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 6.915114351688682"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 6.915114351688682""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 6.915114351688682
""",
)

entry(
    index = 69,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(2.10439e-22,'m^3/(mol*s)'), n=7.76191, Ea=(106.982,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(8.98638e-58,'m^3/(mol*s)'), n=17.983, Ea=(122.1,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 71,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(1.12577e-55,'m^3/(mol*s)'), n=17.3962, Ea=(123.325,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(295311,'m^3/(mol*s)'), n=-0.0463084, w0=(858.5,'kJ/mol'), E0=(228.949,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.032098671944279795, var=38.442285366203414, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 12.510376884004948"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->F
Total Standard Deviation in ln(k): 12.510376884004948""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->F
Total Standard Deviation in ln(k): 12.510376884004948
""",
)

entry(
    index = 73,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->F",
    kinetics = ArrheniusBM(A=(12.1292,'m^3/(mol*s)'), n=1.44664, w0=(858.5,'kJ/mol'), E0=(294.712,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_N-7BrClFINOPSSi->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(4.45749,'m^3/(mol*s)'), n=1.21594, w0=(858.5,'kJ/mol'), E0=(218.95,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_6R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 75,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(14.8208,'m^3/(mol*s)'), n=1.21604, w0=(858.5,'kJ/mol'), E0=(215.271,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_N-3COCdCddCtO2d->Ct_N-3CdO2d->O2d_Ext-4COCdCddCtO2d-R_5R!H->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 76,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(24407.7,'m^3/(mol*s)'), n=0.242665, w0=(711,'kJ/mol'), E0=(208.95,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15340339459177385, var=3.419911884045154, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl
    Total Standard Deviation in ln(k): 4.092792999036203"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl
Total Standard Deviation in ln(k): 4.092792999036203""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl
Total Standard Deviation in ln(k): 4.092792999036203
""",
)

entry(
    index = 77,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.10391,'m^3/(mol*s)'), n=1.64361, w0=(711,'kJ/mol'), E0=(221.034,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(1.25612e+07,'m^3/(mol*s)'), n=-0.637747, w0=(711,'kJ/mol'), E0=(216.725,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.6085e+08,'m^3/(mol*s)'), n=-0.88707, w0=(711,'kJ/mol'), E0=(213.432,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(8.97967e+06,'m^3/(mol*s)'), n=-0.518739, w0=(711,'kJ/mol'), E0=(212.93,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 81,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.18878,'m^3/(mol*s)'), n=1.76475, w0=(657,'kJ/mol'), E0=(181.27,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 82,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.215895,'m^3/(mol*s)'), n=1.97486, w0=(657,'kJ/mol'), E0=(231.46,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15132288918991663, var=27.931227026710847, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C
    Total Standard Deviation in ln(k): 10.97523353271578"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.97523353271578""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C
Total Standard Deviation in ln(k): 10.97523353271578
""",
)

entry(
    index = 83,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(40.7026,'m^3/(mol*s)'), n=1.65435, w0=(699.5,'kJ/mol'), E0=(224.765,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3CtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_3CtO2d->O2d",
    kinetics = ArrheniusBM(A=(1.09358e-06,'m^3/(mol*s)'), n=3.74071, w0=(827.5,'kJ/mol'), E0=(116.096,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_3CtO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_3CtO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 85,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->O2d",
    kinetics = ArrheniusBM(A=(1.62705,'m^3/(mol*s)'), n=1.85266, w0=(699.5,'kJ/mol'), E0=(214.967,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->O2d',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->O2d
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_N-3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-4COCdCddCtO2d-R_N-3CtO2d->O2d
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 86,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(1.62324e-22,'m^3/(mol*s)'), n=7.83496, Ea=(133.074,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 87,
    label = "Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(1.13304e-22,'m^3/(mol*s)'), n=7.82383, Ea=(109.166,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sH->H_N-1Br1sCl1sF1sH->H_N-3COCdCddCtO2d->Cd_Ext-3CO-R_Ext-3CO-R_5R!H->C_Ext-5C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 88,
    label = "Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(22.8223,'m^3/(mol*s)'), n=1.20947, w0=(858.5,'kJ/mol'), E0=(204.182,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s_Ext-3COCdCddCtO2d-R_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R_N-7R!H->C_7BrClFINOPSSi->F_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(25761.4,'m^3/(mol*s)'), n=0.211093, w0=(711,'kJ/mol'), E0=(206.552,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1695122657444783, var=13.236967877631287, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
    Total Standard Deviation in ln(k): 7.7196664881336865"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
Total Standard Deviation in ln(k): 7.7196664881336865""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R
Total Standard Deviation in ln(k): 7.7196664881336865
""",
)

entry(
    index = 90,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(5.59096e+06,'m^3/(mol*s)'), n=-0.339093, w0=(711,'kJ/mol'), E0=(221.524,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 91,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.825331,'m^3/(mol*s)'), n=1.69758, w0=(657,'kJ/mol'), E0=(221.393,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 92,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R",
    kinetics = ArrheniusBM(A=(3.63667,'m^3/(mol*s)'), n=1.59996, w0=(657,'kJ/mol'), E0=(251.549,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_N-2Br1sCl1s->Cl1s_Ext-3Cd-R_N-5R!H->C_Ext-3Cd-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 93,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(4061.22,'m^3/(mol*s)'), n=0.468604, w0=(711,'kJ/mol'), E0=(200.462,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18985986566819002, var=36.55501394603909, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 12.597811986024835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.597811986024835""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 12.597811986024835
""",
)

entry(
    index = 94,
    label = "Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R",
    kinetics = ArrheniusBM(A=(0.0823032,'m^3/(mol*s)'), n=1.92336, w0=(711,'kJ/mol'), E0=(212.188,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-1Br1sCl1sF1sH->Cl1s_3COCdCddCtO2d->Cd_2Br1sCl1s->Cl1s_Ext-3Cd-R_5R!H->Cl_Ext-3Cd-R_Ext-4COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

