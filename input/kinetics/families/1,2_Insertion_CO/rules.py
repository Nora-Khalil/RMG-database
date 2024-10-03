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
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 15.678025212269217""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 15.678025212269217
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
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->Br1s
Total Standard Deviation in ln(k): 11.540182761524994
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
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.822981074071763""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.822981074071763
""",
)

entry(
    index = 12,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCtHNOSSidSis->O",
    kinetics = ArrheniusBM(A=(2890,'m^3/(mol*s)'), n=1.16, w0=(763500,'J/mol'), E0=(347090,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCtHNOSSidSis->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCtHNOSSidSis->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R
Total Standard Deviation in ln(k): 6.611042739432919""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R
Total Standard Deviation in ln(k): 6.611042739432919
""",
)

entry(
    index = 13,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s",
    kinetics = ArrheniusBM(A=(5.66811e-11,'m^3/(mol*s)'), n=4.88105, w0=(867000,'J/mol'), E0=(182718,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_2Br1sCl1sCsF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_N-2CsF1s->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_N-2CsF1s->Cs
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
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.0152384,'m^3/(mol*s)'), n=2.47236, w0=(665500,'J/mol'), E0=(134387,'J/mol'), Tmin=(298,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->Cs_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->F1s_N-2Br1sCl1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 31,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(3.29107e-06,'m^3/(mol*s)'), n=3.47243, w0=(772.445,'kJ/mol'), E0=(404.497,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.32885467589370915, var=14.072233730243552, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 8.346625926767244"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 8.346625926767244""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 8.346625926767244
""",
)

entry(
    index = 32,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(88.9,'m^3/(mol*s)'), n=1.51, w0=(720.5,'kJ/mol'), E0=(332.524,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtNOSSidSis->Cs_Ext-1Cs-R_Ext-1Cs-R_5R!H->C_Ext-1Cs-R
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
    index = 33,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R",
    kinetics = ArrheniusBM(A=(0.000646288,'m^3/(mol*s)'), n=2.4917, w0=(716.923,'kJ/mol'), E0=(367.722,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.15699964691804363, var=2.2252347933374517, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R
    Total Standard Deviation in ln(k): 3.384979073908383"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R
Total Standard Deviation in ln(k): 3.384979073908383""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R
Total Standard Deviation in ln(k): 3.384979073908383
""",
)

entry(
    index = 34,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(3.99883e-09,'m^3/(mol*s)'), n=4.23832, w0=(752.167,'kJ/mol'), E0=(349.79,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24336671816327302, var=42.80731917162696, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C
    Total Standard Deviation in ln(k): 13.727915007598067"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 13.727915007598067""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C
Total Standard Deviation in ln(k): 13.727915007598067
""",
)

entry(
    index = 35,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3.97532e-05,'m^3/(mol*s)'), n=3.22544, w0=(794.5,'kJ/mol'), E0=(362.283,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.22783205549101904, var=5.1887513664573435, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 5.138994480895391"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 5.138994480895391""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C
Total Standard Deviation in ln(k): 5.138994480895391
""",
)

entry(
    index = 36,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R",
    kinetics = ArrheniusBM(A=(2.6164e-06,'m^3/(mol*s)'), n=3.49588, w0=(779.839,'kJ/mol'), E0=(405.724,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.34271609905446115, var=18.596958023435917, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R
    Total Standard Deviation in ln(k): 9.506353455074818"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R
Total Standard Deviation in ln(k): 9.506353455074818""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R
Total Standard Deviation in ln(k): 9.506353455074818
""",
)

entry(
    index = 37,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_8R!H->C",
    kinetics = ArrheniusBM(A=(0.000100447,'m^3/(mol*s)'), n=2.73849, w0=(723.98,'kJ/mol'), E0=(371.249,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_N-8R!H->C",
    kinetics = ArrheniusBM(A=(0.0041564,'m^3/(mol*s)'), n=2.24495, w0=(709.866,'kJ/mol'), E0=(364.194,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-2CsF1s-R_Ext-5C-R_Ext-7R!H-R_Ext-5C-R_Ext-8R!H-R_Ext-5C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(9.64243e-06,'m^3/(mol*s)'), n=3.35746, w0=(794.5,'kJ/mol'), E0=(344.138,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.1886217895610347, var=22.420877291018996, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 9.966482770437088"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 9.966482770437088""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 9.966482770437088
""",
)

entry(
    index = 40,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_N-1COCbCdCsCtNOSSidSis->Cs",
    kinetics = ArrheniusBM(A=(4.23497e-07,'m^3/(mol*s)'), n=3.48174, w0=(712.908,'kJ/mol'), E0=(383.101,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_N-1COCbCdCsCtNOSSidSis->Cs',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_N-1COCbCdCsCtNOSSidSis->Cs
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_N-1COCbCdCsCtNOSSidSis->Cs
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 41,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_6BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(2.23296e-06,'m^3/(mol*s)'), n=3.43153, w0=(794.5,'kJ/mol'), E0=(357.088,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_6BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_6BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_N-6BrClFINOPSSi->O",
    kinetics = ArrheniusBM(A=(0.000729731,'m^3/(mol*s)'), n=3.01554, w0=(794.5,'kJ/mol'), E0=(367.51,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_N-6BrClFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_N-6BrClFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_N-6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_N-6R!H->C_N-6BrClFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.54927e-07,'m^3/(mol*s)'), n=3.84834, w0=(757.106,'kJ/mol'), E0=(395.202,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3806611735200859, var=4.918682127323757, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C
    Total Standard Deviation in ln(k): 5.402557032220877"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C
Total Standard Deviation in ln(k): 5.402557032220877""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C
Total Standard Deviation in ln(k): 5.402557032220877
""",
)

entry(
    index = 44,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(9.63848e-07,'m^3/(mol*s)'), n=3.3693, w0=(870.772,'kJ/mol'), E0=(436.664,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_7R!H->O",
    kinetics = ArrheniusBM(A=(6.28645e-08,'m^3/(mol*s)'), n=3.72541, w0=(794.5,'kJ/mol'), E0=(337.378,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_N-7R!H->O",
    kinetics = ArrheniusBM(A=(0.00121549,'m^3/(mol*s)'), n=3.01393, w0=(794.5,'kJ/mol'), E0=(350.69,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_N-7R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_N-7R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_N-7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_Ext-1COCbCdCsCtNOSSidSis-R_5R!H->C_Ext-5C-R_6R!H->C_1COCbCdCsCtNOSSidSis->Cs_Ext-6C-R_N-7R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R",
    kinetics = ArrheniusBM(A=(7.42676e-06,'m^3/(mol*s)'), n=3.65749, w0=(784.665,'kJ/mol'), E0=(403.794,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.41957717132397787, var=15.806124086847793, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R
    Total Standard Deviation in ln(k): 9.024422503682247"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R
Total Standard Deviation in ln(k): 9.024422503682247""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R
Total Standard Deviation in ln(k): 9.024422503682247
""",
)

entry(
    index = 48,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(7.9377e-09,'m^3/(mol*s)'), n=4.0356, w0=(723.557,'kJ/mol'), E0=(386.084,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_7R!H->C",
    kinetics = ArrheniusBM(A=(3.85608e-06,'m^3/(mol*s)'), n=3.87966, w0=(773.341,'kJ/mol'), E0=(399.503,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_N-7R!H->C",
    kinetics = ArrheniusBM(A=(8.7634e-06,'m^3/(mol*s)'), n=3.4963, w0=(795.99,'kJ/mol'), E0=(407.559,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1COCbCdCsCtHNOSSidSis->H_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-2Br1sCl1sCsF1s->Br1s_N-2Cl1sCsF1s->Cl1s_2CsF1s->Cs_N-1COCbCdCsCtNOSSidSis->Cs_Ext-2Cs-R_5R!H->C_Ext-2Cs-R_Ext-5C-R_N-7R!H->C
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

