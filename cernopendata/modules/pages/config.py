# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2017 CERN.
#
# CERN Open Data Portal is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# CERN Open Data Portal is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CERN Open Data Portal; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Configuration for CERN Open Data pages."""

#: Information on homepage.
OPENDATA_EXPERIMENTS = [
    "CMS",
    "ALICE",
    "ATLAS",
    "LHCb",
    "OPERA",
]

OPENDATA_EDUCATION = [
    (
        "CMS",
        "The CMS (Compact Muon Solenoid) experiment is one of two large "
        "general-purpose particle physics detectors built on the Large Hadron "
        "Collider (LHC) at CERN in Switzerland and France. The goal of CMS is "
        "to investigate a wide range of physics, including properties of the "
        "recently discovered Higgs boson as well as searches for extra "
        "dimensions and particles that could make up dark matter.",
        True,
    ),
    (
        "ALICE",
        '<a href="http://aliceinfo.cern.ch/Public/Welcome.html">'
        '<span class="external-link-l"></span>ALICE</a> '
        "(A Large Ion Collider Experiment) is a heavy-ion "
        '<a href="http://home.web.cern.ch/about/how-detector-works">'
        '<span class="external-link-l"></span>detector</a> designed to study '
        "the physics of strongly interacting matter at extreme energy densities, "
        'where a phase of matter called <a href="http://home.web.cern.ch'
        '/about/physics/heavy-ions-and-quark-gluon-plasma">'
        '<span class="external-link-l"></span>quark-gluon plasma</a> forms.<br/>'
        "The ALICE collaboration uses the 10,000-tonne ALICE detector - 26 m "
        "long, 16 m high, and 16 m wide - to study quark-gluon plasma. "
        "The detector sits in a vast cavern 56 m below ground close to the "
        "village of Saint Genis-Pouilly in France, receiving beams from the LHC. "
        "More than 1000 scientists are part of the collaboration.",
        True,
    ),
    (
        "ATLAS",
        "The ATLAS (A Toroidal LHC ApparatuS) experiment is a general-purpose "
        "detector exploring topics like the properties of the Higgs-like "
        "particle, extra dimensions of space, unification of fundamental "
        "forces and evidence for dark matter candidates in the Universe.",
        True,
    ),
    (
        "LHCb",
        "The LHCb (Large Hadron Collider beauty) experiment aims to record "
        "the decay of particles containing b and anti-b quarks, known as "
        "B mesons. The detector is designed to gather information about the "
        "identity, trajectory, momentum and energy of each particle.",
        True,
    ),
    (
        "OPERA",
        "The Oscillation Project with Emulsion-tRacking Apparatus (OPERA) is a "
        "scientific experiment for detecting tau neutrinos from muon "
        "neutrino oscillations. The experiment is a collaboration between "
        "CERN in Geneva, Switzerland, and the Laboratori Nazionali del "
        "Gran Sasso (LNGS) in Gran Sasso, Italy.",
        True,
    ),
]

OPENDATA_RESEARCH = [
    (
        "CMS",
        "To analyse CMS data, a Virtual Machine with the CMS analysis "
        "environment is provided. The data can be accessed directly "
        "through the VM. In the primary datasets, no selection nor "
        "identification criteria have been applied. The 2011 data release "
        "includes simulated Monte Carlo datasets, but no simulated "
        "datasets are provided for the 2010 release.",
        True,
    ),
    (
        "ALICE",
        "According to the ALICE data preservation strategy, reconstructed "
        "data and Monte Carlo data as well as the analysis software and "
        "documentation needed to process them will be made available on "
        "a time scale of 5 years (for 10% of the data). Thus, the first "
        "release of ALICE research data will happen in 2018.",
        False,
    ),
    (
        "ATLAS",
        "According to the ATLAS Data Access Policy, reconstructed data and "
        "accompanying tools will be released after reasonable embargo periods.",
        False,
    ),
    (
        "OPERA",
        "The Oscillation Project with Emulsion-tRacking Apparatus (OPERA) is a "
        "scientific experiment for detecting tau neutrinos from muon "
        "neutrino oscillations. The experiment is a collaboration between "
        "CERN in Geneva, Switzerland, and the Laboratori Nazionali del "
        "Gran Sasso (LNGS) in Gran Sasso, Italy.",
        False,
    ),
]
