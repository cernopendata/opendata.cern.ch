# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2021 CERN.
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

from unittest.mock import patch

import pytest

from cernopendata.config import RECORDS_REST_FACETS
from cernopendata.views import translate_search_url


# This is usually fetched from OpenSearch. For the tests, let's assume that we have this values
def mock_data():
    return {
        "keywords": {
            "datascience": {},
            "education": {},
            "external resource": {},
            "heavy-ion physics": {},
            "masterclass": {},
            "teaching": {},
        },
        "signature": {
            "H": {},
            "Jpsi": {},
            "W": {},
            "Y": {},
            "Z": {},
            "electron": {},
            "missing transverse energy": {},
            "muon": {},
            "photon": {},
        },
        "collision_energy": {
            "0.9TeV": {},
            "0TeV": {},
            "13TeV": {},
            "2.76TeV": {},
            "5.02TeV": {},
            "7TeV": {},
            "8TeV": {},
        },
        "year": {
            "2008": {},
            "2009": {},
            "2010": {},
            "2011": {},
            "2012": {},
            "2013": {},
            "2015": {},
            "2016": {},
            "2018": {},
            "2019": {},
            "2020": {},
        },
        "stripping_version": {
            "stripping21": {},
            "stripping21r0p1": {},
            "stripping21r0p2": {},
            "stripping21r1": {},
            "stripping21r1p1": {},
            "stripping21r1p2": {},
        },
        "type": {
            "Dataset": {"subtype": {"Collision", "Simulated", "Derived"}},
            "Documentation": {
                "subtype": {
                    "Policy",
                    "Authors",
                    "Report",
                    "Help",
                    "Activities",
                    "Stripping",
                    "Guide",
                    "About",
                }
            },
            "Environment": {"subtype": {"Condition", "VM", "Validation"}},
            "Glossary": {"subtype": set()},
            "News": {"subtype": set()},
            "Software": {
                "subtype": {"Validation", "Workflow", "Tool", "Framework", "Analysis"}
            },
            "Supplementaries": {
                "subtype": {
                    "Configuration LHE",
                    "Configuration RECO",
                    "Configuration",
                    "Trigger",
                    "Configuration SIM",
                    "Configuration HLT",
                    "Luminosity",
                }
            },
        },
        "collision_type": {"Interfill": {}, "PbPb": {}, "pPb": {}, "pp": {}},
        "experiment": {
            "": {},
            "ALICE": {},
            "ATLAS": {},
            "CMS": {},
            "LHCb": {},
            "OPERA": {},
            "PHENIX": {},
        },
        "stripping_stream": {
            "COMMONPARTICLES": {},
            "EW": {},
            "LEPTONIC": {},
            "RADIATIVE": {},
        },
        "file_type": {
            "C": {},
            "DST": {},
            "MDST": {},
            "aod": {},
            "aodsim": {},
            "cc": {},
            "csv": {},
            "db": {},
            "docx": {},
            "fevtdebughlt": {},
            "gen-sim": {},
            "gen-sim-digi-raw": {},
            "gen-sim-reco": {},
            "gz": {},
            "h5": {},
            "html": {},
            "ig": {},
            "ipynb": {},
            "jpg": {},
            "json": {},
            "m4v": {},
            "miniaod": {},
            "miniaodsim": {},
            "nanoaod": {},
            "ova": {},
            "pdf": {},
            "png": {},
            "py": {},
            "raw": {},
            "reco": {},
            "root": {},
            "tar": {},
            "tar.gz": {},
            "tgz": {},
            "txt": {},
            "xls": {},
            "xml": {},
            "zip": {},
        },
        "category": {
            " Heavy-Ion Physics": {"subcategory": set()},
            "B physics and Quarkonia": {"subcategory": set()},
            "Beyond 2 Generations": {"subcategory": set()},
            "Exotica": {
                "subcategory": {
                    "Gravitons",
                    "Heavy Fermions, Heavy Righ-Handed Neutrinos",
                    "Heavy Gauge Bosons",
                    "Leptoquarks",
                    "Contact Interaction",
                    "Extra Dimensions",
                    "Miscellaneous",
                    "Excited Fermions",
                    "Dark Matter",
                }
            },
            "Heavy-Ion Physics": {"subcategory": set()},
            "Higgs Physics": {
                "subcategory": {"Standard Model", "Beyond Standard Model"}
            },
            "Physics Modelling": {"subcategory": set()},
            "Standard Model Physics": {
                "subcategory": {
                    "ElectroWeak",
                    "Top physics",
                    "Minimum Bias",
                    "QCD",
                    "Forward and Small-x QCD Physics",
                    "Drell-Yan",
                }
            },
            "Supersymmetry": {"subcategory": set()},
        },
        "number_of_events": {
            "0 -- 999 ": {},
            "1000 -- 9999": {},
            "10000 -- 99999": {},
            "100000 -- 999999": {},
            "1000000 -- 9999999": {},
            " 10000000 --": {},
        },
        "magnet_polarity": {"MagDown": {}, "MagUp": {}},
    }


@patch("cernopendata.views.initialize_facet_hierarchy", mock_data)
@pytest.mark.parametrize(
    "old_qs_args,new_qs_args",
    [
        ({"type": ["Documentation"]}, {"f": ["type:Documentation"]}),
        (
            {"type": ["Environment"], "category": ["Exotica"]},
            {"f": ["type:Environment", "category:Exotica"]},
        ),
        (
            {"type": ["Dataset"], "subtype": ["Derived"]},
            {"f": ["type:Dataset+subtype:Derived"]},
        ),
        (
            {"type": ["Dataset", "Documentation"], "subtype": ["Simulated", "Guide"]},
            {
                "f": [
                    "type:Dataset+subtype:Simulated",
                    "type:Documentation+subtype:Guide",
                ]
            },
        ),
        (
            {
                "type": ["Dataset", "Documentation"],
                "subtype": ["Help", "Simulated", "Guide"],
            },
            {
                "f": [
                    "type:Dataset+subtype:Simulated",
                    "type:Documentation+subtype:Guide",
                    "type:Documentation+subtype:Help",
                ]
            },
        ),
        (
            {"type": ["Dataset", "Documentation"], "subtype": ["Help", "Guide"]},
            {
                "f": [
                    "type:Dataset",
                    "type:Documentation+subtype:Guide",
                    "type:Documentation+subtype:Help",
                ]
            },
        ),
        (
            {"type": ["Environment"], "subtype": ["VM"], "experiment": ["CMS"]},
            {"f": ["type:Environment+subtype:VM", "experiment:CMS"]},
        ),
        (
            {"experiment": ["CMS", "ATLAS"]},
            {"f": ["experiment:CMS", "experiment:ATLAS"]},
        ),
        ({"q": ["foo"]}, {"q": ["foo"], "f": []}),
        ({"foo": ["bar", "baz"]}, {"foo": ["bar", "baz"], "f": []}),
        ({"q": ["foo"], "type": ["Software"]}, {"q": ["foo"], "f": ["type:Software"]}),
    ],
)
def test_old_search_qs(old_qs_args, new_qs_args):
    """Test translation from old search querystring args to new ones."""
    translated_qs = translate_search_url(old_qs_args, RECORDS_REST_FACETS)
    # compare facets no matter the order
    assert set(translated_qs.pop("f")) == set(new_qs_args.pop("f"))
    # compare rest of query params
    assert translated_qs == new_qs_args
