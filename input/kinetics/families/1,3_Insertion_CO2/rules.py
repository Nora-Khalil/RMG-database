#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_CO2/rules"
shortDesc = ""
longDesc = """
572 - 575 Some of the tortional motions in the alkyl part of the 
transition states are treated as free rotations as they are relatively loose TSs. 

The dictionary defines CO2 in two ways, allowing the R-R' to insert either way
around. However, there are only rates for one of these ways. The other is
presumably matching the top level node.
"""
entry(
    index = 1,
    label = "Root",
    kinetics = Arrhenius(A=(1.08206e-33,'m^3/(mol*s)'), n=11.4802, Ea=(238.724,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.3276385263403874, var=74.56407789521812, Tref=1000.0, N=20, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 20 training reactions at node Root
    Total Standard Deviation in ln(k): 20.646761590555478"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root
Total Standard Deviation in ln(k): 20.646761590555478""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root
Total Standard Deviation in ln(k): 20.646761590555478
""",
)

entry(
    index = 2,
    label = "Root_5R->C",
    kinetics = ArrheniusBM(A=(7.3e-05,'m^3/(mol*s)'), n=3.13, w0=(745.5,'kJ/mol'), E0=(460.067,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_5R->C',), comment="""BM rule fitted to 1 training reactions at node Root_5R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_5R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_5R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-5R->C",
    kinetics = Arrhenius(A=(3.28799e-35,'m^3/(mol*s)'), n=11.9197, Ea=(225.304,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-0.11888428029201034, var=74.7974663912732, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-5R->C',), comment="""BM rule fitted to 19 training reactions at node Root_N-5R->C
    Total Standard Deviation in ln(k): 17.636761488007515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-5R->C
Total Standard Deviation in ln(k): 17.636761488007515""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-5R->C
Total Standard Deviation in ln(k): 17.636761488007515
""",
)

entry(
    index = 4,
    label = "Root_N-5R->C_4R->F",
    kinetics = ArrheniusBM(A=(2.45635e-08,'m^3/(mol*s)'), n=4.04584, w0=(975,'kJ/mol'), E0=(140.047,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_4R->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_4R->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_4R->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_4R->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_N-5R->C_N-4R->F",
    kinetics = Arrhenius(A=(1.05673e-36,'m^3/(mol*s)'), n=12.3572, Ea=(228.482,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.06659087267927644, var=62.9528851423078, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F',), comment="""BM rule fitted to 18 training reactions at node Root_N-5R->C_N-4R->F
    Total Standard Deviation in ln(k): 16.07345404803841"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-5R->C_N-4R->F
Total Standard Deviation in ln(k): 16.07345404803841""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-5R->C_N-4R->F
Total Standard Deviation in ln(k): 16.07345404803841
""",
)

entry(
    index = 6,
    label = "Root_N-5R->C_N-4R->F_4CH->H",
    kinetics = Arrhenius(A=(2.62182e-27,'m^3/(mol*s)'), n=9.78395, Ea=(233.686,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.5145321975659304, var=1.0097468686677356, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_4CH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_4CH->H
    Total Standard Deviation in ln(k): 3.307275797122445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_4CH->H
Total Standard Deviation in ln(k): 3.307275797122445""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_4CH->H
Total Standard Deviation in ln(k): 3.307275797122445
""",
)

entry(
    index = 7,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H",
    kinetics = Arrhenius(A=(7.07353e-38,'m^3/(mol*s)'), n=12.6788, Ea=(227.832,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-0.0849811662779958, var=68.7850923978987, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H',), comment="""BM rule fitted to 16 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H
    Total Standard Deviation in ln(k): 16.840147439088017"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H
Total Standard Deviation in ln(k): 16.840147439088017""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H
Total Standard Deviation in ln(k): 16.840147439088017
""",
)

entry(
    index = 8,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R",
    kinetics = Arrhenius(A=(2.64527e-39,'m^3/(mol*s)'), n=13.0624, Ea=(221.69,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-0.08386231719423337, var=77.17879014112562, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R',), comment="""BM rule fitted to 14 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R
    Total Standard Deviation in ln(k): 17.82259967448125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R
Total Standard Deviation in ln(k): 17.82259967448125""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R
Total Standard Deviation in ln(k): 17.82259967448125
""",
)

entry(
    index = 9,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1",
    kinetics = Arrhenius(A=(1.55746e-13,'m^3/(mol*s)'), n=5.13251, Ea=(125.014,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-8.997534477772192e-16, var=13.395418602564067, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1
    Total Standard Deviation in ln(k): 7.337280703613096"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1
Total Standard Deviation in ln(k): 7.337280703613096""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1
Total Standard Deviation in ln(k): 7.337280703613096
""",
)

entry(
    index = 10,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1",
    kinetics = Arrhenius(A=(1.34115e-43,'m^3/(mol*s)'), n=14.3841, Ea=(237.803,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.3776915498495792, var=16.78636682881237, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1',), comment="""BM rule fitted to 12 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1
    Total Standard Deviation in ln(k): 9.162607693431008"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1
Total Standard Deviation in ln(k): 9.162607693431008""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1
Total Standard Deviation in ln(k): 9.162607693431008
""",
)

entry(
    index = 11,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1_Ext-4C-R",
    kinetics = Arrhenius(A=(2.10377e-14,'m^3/(mol*s)'), n=5.39092, Ea=(133.97,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_6R!H-u1_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 12,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O",
    kinetics = Arrhenius(A=(4.26379e-45,'m^3/(mol*s)'), n=14.8582, Ea=(211.01,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-8.817583788216747e-15, var=2.91877459742804, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O',), comment="""BM rule fitted to 5 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O
    Total Standard Deviation in ln(k): 3.4249739160896073"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O
Total Standard Deviation in ln(k): 3.4249739160896073""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O
Total Standard Deviation in ln(k): 3.4249739160896073
""",
)

entry(
    index = 13,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O",
    kinetics = Arrhenius(A=(1.5749e-42,'m^3/(mol*s)'), n=14.0455, Ea=(256.941,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=1.5858251118155706, var=3.9145883324409856, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O
    Total Standard Deviation in ln(k): 7.950917432829113"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O
Total Standard Deviation in ln(k): 7.950917432829113""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O
Total Standard Deviation in ln(k): 7.950917432829113
""",
)

entry(
    index = 14,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R",
    kinetics = Arrhenius(A=(1.49948e-42,'m^3/(mol*s)'), n=14.2116, Ea=(214.667,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-1.2371609906936764e-14, var=0.6586218024280696, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 1.626953127006413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 1.626953127006413""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 1.626953127006413
""",
)

entry(
    index = 15,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-7R!H-R",
    kinetics = Arrhenius(A=(2.17633e-48,'m^3/(mol*s)'), n=15.6938, Ea=(206.967,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 16,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F",
    kinetics = Arrhenius(A=(1.15773e-58,'m^3/(mol*s)'), n=18.7257, Ea=(231.184,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=8.367707064328138e-15, var=0.6186619570347205, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F
    Total Standard Deviation in ln(k): 1.5768257190070567"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F
Total Standard Deviation in ln(k): 1.5768257190070567""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F
Total Standard Deviation in ln(k): 1.5768257190070567
""",
)

entry(
    index = 17,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F",
    kinetics = ArrheniusBM(A=(0.035263,'m^3/(mol*s)'), n=2.34043, w0=(828.5,'kJ/mol'), E0=(309.89,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3856711069752406, var=3.34163557678022, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F
    Total Standard Deviation in ln(k): 4.633706884883308"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F
Total Standard Deviation in ln(k): 4.633706884883308""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F
Total Standard Deviation in ln(k): 4.633706884883308
""",
)

entry(
    index = 18,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C",
    kinetics = Arrhenius(A=(7.08572e-41,'m^3/(mol*s)'), n=13.6708, Ea=(213.252,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-6.1576876582253435e-15, var=0.3235071920522639, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C
    Total Standard Deviation in ln(k): 1.1402470556497566"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C
Total Standard Deviation in ln(k): 1.1402470556497566""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C
Total Standard Deviation in ln(k): 1.1402470556497566
""",
)

entry(
    index = 19,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-10R!H->C",
    kinetics = Arrhenius(A=(6.7151e-46,'m^3/(mol*s)'), n=15.2932, Ea=(217.498,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-10R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-10R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_N-10R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C",
    kinetics = Arrhenius(A=(4.84072e-58,'m^3/(mol*s)'), n=18.5395, Ea=(230.527,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-7.479200534648135e-15, var=0.3465964562706064, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C
    Total Standard Deviation in ln(k): 1.1802365187905897"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 1.1802365187905897""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C
Total Standard Deviation in ln(k): 1.1802365187905897
""",
)

entry(
    index = 21,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_N-7R!H->C",
    kinetics = Arrhenius(A=(3.78787e-61,'m^3/(mol*s)'), n=19.4705, Ea=(233.815,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_N-7R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_N-7R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_N-7R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F_Ext-4C-R",
    kinetics = ArrheniusBM(A=(0.106,'m^3/(mol*s)'), n=2.13, w0=(828.5,'kJ/mol'), E0=(312.366,'kJ/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_N-6CF->F_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C",
    kinetics = Arrhenius(A=(1.23235e-39,'m^3/(mol*s)'), n=13.3058, Ea=(214.361,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 24,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C",
    kinetics = Arrhenius(A=(4.0741e-42,'m^3/(mol*s)'), n=14.0358, Ea=(212.142,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_6R!H->O_Ext-6O-R_Ext-4C-R_Ext-4C-R_Ext-8R!H-R_Ext-8R!H-R_Ext-7R!H-R_Ext-9R!H-R_10R!H->C_Ext-10C-R_N-11R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C",
    kinetics = Arrhenius(A=(4.56689e-58,'m^3/(mol*s)'), n=18.5284, Ea=(229.95,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-8.510168026892864e-15, var=0.6011000764726775, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
    Total Standard Deviation in ln(k): 1.5542840167309107"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 1.5542840167309107""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C
Total Standard Deviation in ln(k): 1.5542840167309107
""",
)

entry(
    index = 26,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C",
    kinetics = Arrhenius(A=(5.76471e-58,'m^3/(mol*s)'), n=18.5725, Ea=(232.258,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_N-8R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C",
    kinetics = Arrhenius(A=(3.90079e-58,'m^3/(mol*s)'), n=18.5063, Ea=(231.893,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_9R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C",
    kinetics = Arrhenius(A=(4.94145e-58,'m^3/(mol*s)'), n=18.5395, Ea=(228.978,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=-2.0806798479848195e-15, var=0.36141116752151736, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
    Total Standard Deviation in ln(k): 1.2051962548348458"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 1.2051962548348458""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C
Total Standard Deviation in ln(k): 1.2051962548348458
""",
)

entry(
    index = 29,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_8C-u0",
    kinetics = Arrhenius(A=(3.23183e-56,'m^3/(mol*s)'), n=18.045, Ea=(233.567,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_8C-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_8C-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_8C-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_8C-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_N-8C-u0",
    kinetics = Arrhenius(A=(7.55543e-60,'m^3/(mol*s)'), n=19.034, Ea=(224.389,'kJ/mol'), T0=(1,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_N-8C-u0',), comment="""BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_N-8C-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_N-8C-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-5R->C_N-4R->F_N-4CH->H_Ext-4C-R_N-6R!H-u1_N-6R!H->O_6CF->F_Ext-4C-R_7R!H->C_Ext-7C-R_8R!H->C_Ext-8C-R_N-9R!H->C_N-8C-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

