#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_CO/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(8.38607e-06,'m^3/(mol*s)'), n=3.65708, w0=(722933,'J/mol'), E0=(304453,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.021463353765412144, var=104.40231708744368, Tref=1000.0, N=15, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 15 training reactions at node Root
    Total Standard Deviation in ln(k): 20.537800250164782"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root
Total Standard Deviation in ln(k): 20.537800250164782""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root
Total Standard Deviation in ln(k): 20.537800250164782
""",
)

entry(
    index = 2,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(0.000199898,'m^3/(mol*s)'), n=3.37363, w0=(707800,'J/mol'), E0=(355308,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0007752095240496672, var=25.93198997196265, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs',), comment="""BM rule fitted to 10 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs
    Total Standard Deviation in ln(k): 10.21075284578118"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs
Total Standard Deviation in ln(k): 10.21075284578118""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs
Total Standard Deviation in ln(k): 10.21075284578118
""",
)

entry(
    index = 3,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(7.71351e-07,'m^3/(mol*s)'), n=3.73262, w0=(753200,'J/mol'), E0=(207085,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.01481451426525692, var=140.21852362954718, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs',), comment="""BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs
    Total Standard Deviation in ln(k): 23.776072845761064"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs
Total Standard Deviation in ln(k): 23.776072845761064""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs
Total Standard Deviation in ln(k): 23.776072845761064
""",
)

entry(
    index = 4,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs",
    kinetics = ArrheniusBM(A=(0.000538,'m^3/(mol*s)'), n=3.29, w0=(655500,'J/mol'), E0=(448319,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 14.683542115987143""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 14.683542115987143
""",
)

entry(
    index = 5,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs",
    kinetics = ArrheniusBM(A=(0.000147143,'m^3/(mol*s)'), n=3.40205, w0=(713611,'J/mol'), E0=(344478,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.006666109276590875, var=9.528414751844478, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs',), comment="""BM rule fitted to 9 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs
    Total Standard Deviation in ln(k): 6.204991399503731"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 6.204991399503731""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs
Total Standard Deviation in ln(k): 6.204991399503731
""",
)

entry(
    index = 6,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(0.000123216,'m^3/(mol*s)'), n=3.10804, w0=(757000,'J/mol'), E0=(292228,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.009698636387084951, var=75.52943254762172, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 17.447054060421397"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 17.447054060421397""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 17.447054060421397
""",
)

entry(
    index = 7,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(4.63215e-07,'m^3/(mol*s)'), n=3.79306, w0=(750667,'J/mol'), E0=(153506,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0033101079901278864, var=44.77575248961514, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 13.422938745578376"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 13.422938745578376""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 13.422938745578376
""",
)

entry(
    index = 8,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(6.59302e-05,'m^3/(mol*s)'), n=3.43279, w0=(735300,'J/mol'), E0=(346213,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0018996793658226105, var=11.392479574397608, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R',), comment="""BM rule fitted to 5 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R
    Total Standard Deviation in ln(k): 6.771304732016401"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R
Total Standard Deviation in ln(k): 6.771304732016401""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R
Total Standard Deviation in ln(k): 6.771304732016401
""",
)

entry(
    index = 9,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(0.0164,'m^3/(mol*s)'), n=2.86, w0=(720500,'J/mol'), E0=(353457,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 3.0973971792876913""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 3.0973971792876913
""",
)

entry(
    index = 10,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(4.72211e-05,'m^3/(mol*s)'), n=3.62605, w0=(675167,'J/mol'), E0=(336695,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.029131322726712552, var=25.066532298396353, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H',), comment="""BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 10.110198766151091"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 10.110198766151091""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 10.110198766151091
""",
)

entry(
    index = 11,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCtHNOSSidSis->O",
    kinetics = ArrheniusBM(A=(1.27e-07,'m^3/(mol*s)'), n=3.7, w0=(750500,'J/mol'), E0=(243508,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCtHNOSSidSis->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCtHNOSSidSis->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCtHNOSSidSis->O",
    kinetics = ArrheniusBM(A=(2890,'m^3/(mol*s)'), n=1.16, w0=(763500,'J/mol'), E0=(347090,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCtHNOSSidSis->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCtHNOSSidSis->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R
Total Standard Deviation in ln(k): 13.475162208492629""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R
Total Standard Deviation in ln(k): 13.475162208492629
""",
)

entry(
    index = 13,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s",
    kinetics = ArrheniusBM(A=(5.66811e-11,'m^3/(mol*s)'), n=4.88105, w0=(867000,'J/mol'), E0=(182718,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 14,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s",
    kinetics = ArrheniusBM(A=(0.000274925,'m^3/(mol*s)'), n=2.99988, w0=(692500,'J/mol'), E0=(140312,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0001260566361784852, var=9.332730823581484, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s
    Total Standard Deviation in ln(k): 6.124685864489913"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 6.124685864489913""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s
Total Standard Deviation in ln(k): 6.124685864489913
""",
)

entry(
    index = 15,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(4.06559e-05,'m^3/(mol*s)'), n=3.48903, w0=(720500,'J/mol'), E0=(336042,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.0017449027319432118, var=2.206248633025942, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H',), comment="""BM rule fitted to 4 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 2.9821066346347878"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 2.9821066346347878""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 2.9821066346347878
""",
)

entry(
    index = 16,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->H",
    kinetics = ArrheniusBM(A=(0.0026956,'m^3/(mol*s)'), n=2.93313, w0=(794500,'J/mol'), E0=(385875,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_N-2Br1sCl1sF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(0.000614234,'m^3/(mol*s)'), n=3.16963, w0=(794500,'J/mol'), E0=(361999,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s",
    kinetics = ArrheniusBM(A=(0.00260177,'m^3/(mol*s)'), n=3.17132, w0=(615500,'J/mol'), E0=(328365,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.00022826452100923147, var=7.965319250047673, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s
    Total Standard Deviation in ln(k): 5.658516724380591"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 5.658516724380591""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s
Total Standard Deviation in ln(k): 5.658516724380591
""",
)

entry(
    index = 19,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.006108,'m^3/(mol*s)'), n=2.57909, w0=(719500,'J/mol'), E0=(150891,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.0152384,'m^3/(mol*s)'), n=2.47236, w0=(665500,'J/mol'), E0=(134387,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O_Ext-5O-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O_Ext-5O-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O_Ext-5O-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(0.000319223,'m^3/(mol*s)'), n=2.55831, w0=(794.5,'kJ/mol'), E0=(258.363,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O_Ext-5O-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O_Ext-5O-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O_Ext-5O-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->O_Ext-5O-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(2.36028e-06,'m^3/(mol*s)'), n=3.37858, w0=(794.5,'kJ/mol'), E0=(358.342,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2564347683255395, var=44.64889667491692, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 14.03991414917353"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 14.03991414917353""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 14.03991414917353
""",
)

entry(
    index = 33,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_N-5BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(0.0023437,'m^3/(mol*s)'), n=2.91659, w0=(794.5,'kJ/mol'), E0=(386.506,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.11053150447395992, var=0.23751621675645537, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_N-5BrCClFINPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_N-5BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 1.254737727978971"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 1.254737727978971""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_N-5BrCClFINPSSi->C
Total Standard Deviation in ln(k): 1.254737727978971
""",
)

entry(
    index = 34,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(0.0272095,'m^3/(mol*s)'), n=2.58218, w0=(720.5,'kJ/mol'), E0=(339.675,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.18781295013985375, var=3.3730633191276174, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R
    Total Standard Deviation in ln(k): 4.15376849830483"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R
Total Standard Deviation in ln(k): 4.15376849830483""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R
Total Standard Deviation in ln(k): 4.15376849830483
""",
)

entry(
    index = 35,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.00734196,'m^3/(mol*s)'), n=2.97843, w0=(636.5,'kJ/mol'), E0=(335.591,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.0163189,'m^3/(mol*s)'), n=2.90186, w0=(594.5,'kJ/mol'), E0=(321.146,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_N-2Br1sCl1sH->H_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_6R!H->O",
    kinetics = ArrheniusBM(A=(2.23296e-06,'m^3/(mol*s)'), n=3.43153, w0=(794.5,'kJ/mol'), E0=(357.088,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_6R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_6R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_6R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O",
    kinetics = ArrheniusBM(A=(2.56232e-06,'m^3/(mol*s)'), n=3.35301, w0=(794.5,'kJ/mol'), E0=(358.828,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24891436526674468, var=84.66327378824407, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O
    Total Standard Deviation in ln(k): 19.071511264686446"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 19.071511264686446""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O
Total Standard Deviation in ln(k): 19.071511264686446
""",
)

entry(
    index = 39,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.83428,'m^3/(mol*s)'), n=2.03702, w0=(720.5,'kJ/mol'), E0=(343.691,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1874020864537245, var=4.5825242706269895, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C
    Total Standard Deviation in ln(k): 4.76236207753982"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C
Total Standard Deviation in ln(k): 4.76236207753982""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C
Total Standard Deviation in ln(k): 4.76236207753982
""",
)

entry(
    index = 40,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.81927e-16,'m^3/(mol*s)'), n=6.80628, w0=(720.5,'kJ/mol'), E0=(308.481,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(3.28726e-06,'m^3/(mol*s)'), n=3.34441, w0=(794.5,'kJ/mol'), E0=(346.458,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.2489524811015141, var=236.4437147670073, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 31.45177153518189"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 31.45177153518189""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 31.45177153518189
""",
)

entry(
    index = 42,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C",
    kinetics = ArrheniusBM(A=(5.43885e-06,'m^3/(mol*s)'), n=3.21456, w0=(794.5,'kJ/mol'), E0=(384.924,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_N-6BrCClFINPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(8.26069,'m^3/(mol*s)'), n=1.78987, w0=(720.5,'kJ/mol'), E0=(338.164,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.229798356330123, var=10.40246183297155, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R
    Total Standard Deviation in ln(k): 7.043224313309215"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R
Total Standard Deviation in ln(k): 7.043224313309215""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R
Total Standard Deviation in ln(k): 7.043224313309215
""",
)

entry(
    index = 44,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->O",
    kinetics = ArrheniusBM(A=(8.43453e-06,'m^3/(mol*s)'), n=3.52638, w0=(794.5,'kJ/mol'), E0=(319.086,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(5.69856e-08,'m^3/(mol*s)'), n=3.54975, w0=(794.5,'kJ/mol'), E0=(370.463,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_2Br1sCl1sF1sH->F1s_Ext-1COCbCdCsCtNOSSidSis-R_N-5R!H->O_5BrCClFINPSSi->C_Ext-5C-R_N-6R!H->O_6BrCClFINPSSi->C_Ext-6C-R_N-7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(88.9,'m^3/(mol*s)'), n=1.51, w0=(720.5,'kJ/mol'), E0=(332.524,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R_Ext-1Cs-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R_Ext-1Cs-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->F1s_1COCbCdCsCtNOSSidSis->Cs_2Br1sCl1sH->H_Ext-1Cs-R_5R!H->C_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_5R!H->C",
    kinetics = ArrheniusBM(A=(0.276494,'m^3/(mol*s)'), n=2.3475, w0=(720500,'J/mol'), E0=(344340,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.004190297371957585, var=4.145886677586163, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_5R!H->C
    Total Standard Deviation in ln(k): 4.0924597961275815"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_5R!H->C
Total Standard Deviation in ln(k): 4.0924597961275815""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_5R!H->C
Total Standard Deviation in ln(k): 4.0924597961275815
""",
)

entry(
    index = 22,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.81927e-16,'m^3/(mol*s)'), n=6.80628, w0=(720500,'J/mol'), E0=(307835,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.00734196,'m^3/(mol*s)'), n=2.97843, w0=(636500,'J/mol'), E0=(334210,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.0163189,'m^3/(mol*s)'), n=2.90186, w0=(594500,'J/mol'), E0=(319847,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_N-2Br1sCl1sF1sH->H_N-2Br1sCl1sF1s->F1s_N-2Br1sCl1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_5R!H->C_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(1.40137,'m^3/(mol*s)'), n=2.0958, w0=(720500,'J/mol'), E0=(339329,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-1.0306105576327384e-05, var=9.046558139596009, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_5R!H->C_Ext-1Cs-R',), comment="""BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_5R!H->C_Ext-1Cs-R
    Total Standard Deviation in ln(k): 6.029767182939766"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_5R!H->C_Ext-1Cs-R
Total Standard Deviation in ln(k): 6.029767182939766""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_5R!H->C_Ext-1Cs-R
Total Standard Deviation in ln(k): 6.029767182939766
""",
)

entry(
    index = 26,
    label = "Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_5R!H->C_Ext-1Cs-R_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(88.9,'m^3/(mol*s)'), n=1.51, w0=(720500,'J/mol'), E0=(331301,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_5R!H->C_Ext-1Cs-R_Ext-1Cs-R',), comment="""BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_5R!H->C_Ext-1Cs-R_Ext-1Cs-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_5R!H->C_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cs_Ext-1Cs-R_2Br1sCl1sF1sH->H_5R!H->C_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

