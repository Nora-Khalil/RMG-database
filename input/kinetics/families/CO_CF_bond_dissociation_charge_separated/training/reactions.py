#!/usr/bin/env python
# encoding: utf-8

name = "CO_CF_bond_dissociation_charge_separated/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C3F6O-2 <=> CF2O + C2F4-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(2.43e+08,'s^-1'), n=1.22, Ea=(48702.3,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation_charge_separated/
Original entry: CF3OCCF3 <=> CF3CF+CF2O
""",
)

entry(
    index = 1,
    label = "C4F8O-2 <=> C2F4O-2 + C2F4-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.53e+09,'s^-1'), n=0.9, Ea=(52188.2,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation_charge_separated/
Original entry: C2F5OCCF3 <=> CF3CFO+CF3CF
""",
)

entry(
    index = 2,
    label = "C5F10O-2 <=> C3F6O-3 + C2F4-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.26e+08,'s^-1'), n=1.07, Ea=(51125.8,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation_charge_separated/
Original entry: C3F7OCCF3 <=> C2F5CFO+CF3CF
""",
)

entry(
    index = 3,
    label = "C4H8O-2 <=> C2H4O + C2H4-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.11e+06,'s^-1'), n=1.75, Ea=(44653.7,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation_charge_separated/
Original entry: C2H5OCCH3 <=> CH3CHO+CH3CH
""",
)

entry(
    index = 4,
    label = "C5H10O <=> C3H6O-2 + C2H4-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.12e+06,'s^-1'), n=1.87, Ea=(44732.4,'cal/mol'), T0=(1,'K')),
    rank = 3,
    longDesc = 
"""
Training reaction from kinetics library: PFAS_HPL_Test/CO_CF_bond_dissociation_charge_separated/
Original entry: C3H7OCCH3 <=> C2H5CHO+CH3CH
""",
)

