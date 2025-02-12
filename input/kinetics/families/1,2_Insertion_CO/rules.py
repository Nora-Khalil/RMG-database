#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_CO/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(8.6244e-09,'m^3/(mol*s)'), n=4.14746, w0=(718.364,'kJ/mol'), E0=(395.4,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15325066778616647, var=63.474890211697094, Tref=1000.0, N=33, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 33 training reactions at node Root
    Total Standard Deviation in ln(k): 16.357002908423972"""),
    rank = 11,
    shortDesc = """BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 16.357002908423972""",
    longDesc = 
"""
BM rule fitted to 33 training reactions at node Root
Total Standard Deviation in ln(k): 16.357002908423972
""",
)

entry(
    index = 2,
    label = "Root_1COCbCdCsCtHNOSSidSis->H",
    kinetics = ArrheniusBM(A=(0.199833,'m^3/(mol*s)'), n=2.2417, w0=(753.875,'kJ/mol'), E0=(242.116,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=3.182009315440503, var=322.9459769094626, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H',), comment="""BM rule fitted to 4 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H
    Total Standard Deviation in ln(k): 44.021486384938356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 44.021486384938356""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 44.021486384938356
""",
)

entry(
    index = 3,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H",
    kinetics = ArrheniusBM(A=(9.00716e-09,'m^3/(mol*s)'), n=4.13837, w0=(713.466,'kJ/mol'), E0=(398.546,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.17449195599068548, var=53.714345727863936, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H',), comment="""BM rule fitted to 29 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H
    Total Standard Deviation in ln(k): 15.131139705538365"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 15.131139705538365""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 15.131139705538365
""",
)

entry(
    index = 4,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(2890,'m^3/(mol*s)'), n=1.16, w0=(763.5,'kJ/mol'), E0=(342.758,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(2.97506e-05,'m^3/(mol*s)'), n=3.24415, w0=(750.667,'kJ/mol'), E0=(155.524,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.09875956426873611, var=43.22038047200727, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 13.427710858058727"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 13.427710858058727""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 13.427710858058727
""",
)

entry(
    index = 6,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = Arrhenius(A=(7.31428e-12,'m^3/(mol*s)'), n=5.23142, Ea=(379.471,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=11.084833012051705, var=131.95842148625496, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 10 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 50.88036391106684"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 50.88036391106684""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 50.88036391106684
""",
)

entry(
    index = 7,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(2.39609e-06,'m^3/(mol*s)'), n=3.40218, w0=(708.184,'kJ/mol'), E0=(384.32,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2419157737874088, var=18.728711394253086, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 19 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 9.283656669499548"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 9.283656669499548""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 9.283656669499548
""",
)

entry(
    index = 8,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s",
    kinetics = ArrheniusBM(A=(5.66811e-11,'m^3/(mol*s)'), n=4.88105, w0=(867,'kJ/mol'), E0=(180.452,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s",
    kinetics = ArrheniusBM(A=(0.00925504,'m^3/(mol*s)'), n=2.53089, w0=(692.5,'kJ/mol'), E0=(142.143,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05412795233083692, var=9.232006363555131, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s
    Total Standard Deviation in ln(k): 6.227230421193259"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 6.227230421193259""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 6.227230421193259
""",
)

entry(
    index = 10,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs",
    kinetics = Arrhenius(A=(2.4723e-12,'m^3/(mol*s)'), n=5.40158, Ea=(396.829,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=10.046726283133394, var=99.04873971056898, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 45.194802547966646"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 45.194802547966646""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 45.194802547966646
""",
)

entry(
    index = 11,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(1.27e-07,'m^3/(mol*s)'), n=3.7, w0=(750.5,'kJ/mol'), E0=(246.144,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R",
    kinetics = ArrheniusBM(A=(5.11526e-06,'m^3/(mol*s)'), n=3.32781, w0=(752.167,'kJ/mol'), E0=(365.036,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.20864420989947058, var=5.027100087570713, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R
    Total Standard Deviation in ln(k): 5.019087397713436"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R
Total Standard Deviation in ln(k): 5.019087397713436""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R
Total Standard Deviation in ln(k): 5.019087397713436
""",
)

entry(
    index = 13,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs",
    kinetics = ArrheniusBM(A=(4.83947e-05,'m^3/(mol*s)'), n=2.98548, w0=(665.786,'kJ/mol'), E0=(415.534,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.25444983736305143, var=11.386006407218195, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs',), comment="""BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs
    Total Standard Deviation in ln(k): 7.403930234687958"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs
Total Standard Deviation in ln(k): 7.403930234687958""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs
Total Standard Deviation in ln(k): 7.403930234687958
""",
)

entry(
    index = 14,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs",
    kinetics = ArrheniusBM(A=(0.00017035,'m^3/(mol*s)'), n=3.41516, w0=(675.167,'kJ/mol'), E0=(336.837,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.21424198572096528, var=25.20771870518315, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs
    Total Standard Deviation in ln(k): 10.603527790022808"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs
Total Standard Deviation in ln(k): 10.603527790022808""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs
Total Standard Deviation in ln(k): 10.603527790022808
""",
)

entry(
    index = 15,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.006108,'m^3/(mol*s)'), n=2.57909, w0=(719.5,'kJ/mol'), E0=(150.342,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.0152384,'m^3/(mol*s)'), n=2.47236, w0=(665.5,'kJ/mol'), E0=(134.033,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R",
    kinetics = Arrhenius(A=(1.59757e-11,'m^3/(mol*s)'), n=5.10963, Ea=(392.063,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=10.844238902648481, var=121.40465731012806, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R
    Total Standard Deviation in ln(k): 49.3357606100702"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R
Total Standard Deviation in ln(k): 49.3357606100702""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R
Total Standard Deviation in ln(k): 49.3357606100702
""",
)

entry(
    index = 18,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.06029e-06,'m^3/(mol*s)'), n=3.38706, w0=(740.071,'kJ/mol'), E0=(361.82,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2112969102517167, var=6.034106433395716, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C
    Total Standard Deviation in ln(k): 5.45541184904648"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C
Total Standard Deviation in ln(k): 5.45541184904648""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C
Total Standard Deviation in ln(k): 5.45541184904648
""",
)

entry(
    index = 19,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(0.0021256,'m^3/(mol*s)'), n=2.9327, w0=(794.5,'kJ/mol'), E0=(386.248,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.03804014467098987, var=0.14344916898309892, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C
    Total Standard Deviation in ln(k): 0.8548653290005201"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.8548653290005201""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.8548653290005201
""",
)

entry(
    index = 20,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(0.000538,'m^3/(mol*s)'), n=3.29, w0=(655.5,'kJ/mol'), E0=(448.925,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(4.591e-05,'m^3/(mol*s)'), n=2.97593, w0=(667.5,'kJ/mol'), E0=(414.65,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2625547048188877, var=11.92585683908382, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 7.582804005829836"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 7.582804005829836""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 7.582804005829836
""",
)

entry(
    index = 22,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(0.000614234,'m^3/(mol*s)'), n=3.16963, w0=(794.5,'kJ/mol'), E0=(363.717,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(0.00962611,'m^3/(mol*s)'), n=2.95613, w0=(615.5,'kJ/mol'), E0=(328.448,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18731351736346022, var=8.005119587844945, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 6.1426980919536565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.1426980919536565""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 6.1426980919536565
""",
)

entry(
    index = 24,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(0.0160071,'m^3/(mol*s)'), n=2.60695, w0=(720.5,'kJ/mol'), E0=(333.568,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.25177113105531246, var=5.184316312875414, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R
    Total Standard Deviation in ln(k): 5.197190878460104"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 5.197190878460104""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 5.197190878460104
""",
)

entry(
    index = 25,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R",
    kinetics = Arrhenius(A=(3.53407e-23,'m^3/(mol*s)'), n=8.19081, Ea=(458.46,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=1.6870377145822858e-15, var=1.6389656920711897, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 2.5665038540899876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.5665038540899876""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 2.5665038540899876
""",
)

entry(
    index = 26,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(2.93197e-05,'m^3/(mol*s)'), n=3.07297, w0=(752.167,'kJ/mol'), E0=(360.904,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.19178919687277432, var=3.6166923960422124, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R
    Total Standard Deviation in ln(k): 4.294408069362602"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 4.294408069362602""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 4.294408069362602
""",
)

entry(
    index = 27,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R",
    kinetics = ArrheniusBM(A=(1.49699e-05,'m^3/(mol*s)'), n=3.07572, w0=(667.5,'kJ/mol'), E0=(416.375,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2790100330224709, var=11.650589388804836, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R
    Total Standard Deviation in ln(k): 7.543784397244557"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R
Total Standard Deviation in ln(k): 7.543784397244557""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R
Total Standard Deviation in ln(k): 7.543784397244557
""",
)

entry(
    index = 28,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.00734196,'m^3/(mol*s)'), n=2.97843, w0=(636.5,'kJ/mol'), E0=(335.809,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.0163189,'m^3/(mol*s)'), n=2.90186, w0=(594.5,'kJ/mol'), E0=(321.364,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Cs_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C",
    kinetics = ArrheniusBM(A=(8.26432,'m^3/(mol*s)'), n=1.78982, w0=(720.5,'kJ/mol'), E0=(338.391,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2344182405761059, var=10.402855165970264, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C
    Total Standard Deviation in ln(k): 7.054954303195877"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C
Total Standard Deviation in ln(k): 7.054954303195877""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C
Total Standard Deviation in ln(k): 7.054954303195877
""",
)

entry(
    index = 31,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C",
    kinetics = Arrhenius(A=(1.81927e-16,'m^3/(mol*s)'), n=6.80628, Ea=(325.917,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_6R!H->C",
    kinetics = Arrhenius(A=(1.76125e-25,'m^3/(mol*s)'), n=8.86865, Ea=(457.075,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C",
    kinetics = Arrhenius(A=(7.09132e-21,'m^3/(mol*s)'), n=7.51297, Ea=(459.846,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.00883e-05,'m^3/(mol*s)'), n=2.97247, w0=(731,'kJ/mol'), E0=(360.496,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16991008426787743, var=3.818391389164475, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 4.344303367932451"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 4.344303367932451""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 4.344303367932451
""",
)

entry(
    index = 35,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.57254e-05,'m^3/(mol*s)'), n=3.24294, w0=(794.5,'kJ/mol'), E0=(361.988,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.23244300669039758, var=5.185214704805579, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 5.149023235331049"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 5.149023235331049""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 5.149023235331049
""",
)

entry(
    index = 36,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R",
    kinetics = ArrheniusBM(A=(5.2597e-07,'m^3/(mol*s)'), n=3.46483, w0=(667.5,'kJ/mol'), E0=(427.258,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.324942503029567, var=2.2347856186302955, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R
    Total Standard Deviation in ln(k): 3.8133568858185076"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R
Total Standard Deviation in ln(k): 3.8133568858185076""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R
Total Standard Deviation in ln(k): 3.8133568858185076
""",
)

entry(
    index = 37,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(7.15522e-09,'m^3/(mol*s)'), n=4.05272, w0=(667.5,'kJ/mol'), E0=(385.857,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(88.9,'m^3/(mol*s)'), n=1.51, w0=(720.5,'kJ/mol'), E0=(332.75,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_8R!H->O",
    kinetics = ArrheniusBM(A=(5.66674e-08,'m^3/(mol*s)'), n=3.74252, w0=(794.5,'kJ/mol'), E0=(337.084,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_8R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_8R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_8R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O",
    kinetics = ArrheniusBM(A=(0.000303824,'m^3/(mol*s)'), n=2.68832, w0=(709.833,'kJ/mol'), E0=(368.544,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.157434887137511, var=1.963405764246412, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O
    Total Standard Deviation in ln(k): 3.204631541279232"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O
Total Standard Deviation in ln(k): 3.204631541279232""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O
Total Standard Deviation in ln(k): 3.204631541279232
""",
)

entry(
    index = 41,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(0.000657796,'m^3/(mol*s)'), n=3.03266, w0=(794.5,'kJ/mol'), E0=(367.221,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_N-6R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C",
    kinetics = ArrheniusBM(A=(4.06388e-07,'m^3/(mol*s)'), n=3.50491, w0=(667.5,'kJ/mol'), E0=(422.694,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3342610586865197, var=0.033718338013159196, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C
    Total Standard Deviation in ln(k): 1.2079724623299843"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C
Total Standard Deviation in ln(k): 1.2079724623299843""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C
Total Standard Deviation in ln(k): 1.2079724623299843
""",
)

entry(
    index = 43,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(8.68834e-07,'m^3/(mol*s)'), n=3.38642, w0=(667.5,'kJ/mol'), E0=(436.372,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(0.000113417,'m^3/(mol*s)'), n=3.00792, w0=(794.5,'kJ/mol'), E0=(371.12,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(0.000582584,'m^3/(mol*s)'), n=2.50881, w0=(667.5,'kJ/mol'), E0=(367.432,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.16163968774428036, var=2.225082732425544, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 3.3965352883712696"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 3.3965352883712696""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 3.3965352883712696
""",
)

entry(
    index = 46,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(1.17091e-07,'m^3/(mol*s)'), n=3.66153, w0=(667.5,'kJ/mol'), E0=(421.836,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(1.41072e-06,'m^3/(mol*s)'), n=3.34827, w0=(667.5,'kJ/mol'), E0=(423.552,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_8BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(9.05456e-05,'m^3/(mol*s)'), n=2.75561, w0=(667.5,'kJ/mol'), E0=(370.96,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_8BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_8BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_8BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_8BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_N-8BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(0.00374667,'m^3/(mol*s)'), n=2.26207, w0=(667.5,'kJ/mol'), E0=(363.903,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_N-8BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_N-8BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_N-8BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_Ext-5C-R_6R!H->C_Ext-6C-R_N-8R!H->O_N-1COCbCdCsCtNOSSidSis->Cs_N-8BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

