# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2012, 2013, 2014, 2015, 2016 CERN.
#
# CERN Open Data Portal is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# CERN Open Data Portal is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Define fixtures."""

COLLECTIONS = [
    dict(
        name="CERN Open Data Portal",
        dbquery=None,
        children=[
            dict(
                name="CMS",
                dbquery=None,
                children=[
                    dict(
                        name="CMS-Primary-Datasets",
                        dbquery='collections.primary:"CMS-Primary-Datasets"',
                    ),
                    dict(
                        name="CMS-Derived-Datasets",
                        dbquery='collections.primary:"CMS-Derived-Datasets"',
                    ),
                    dict(
                        name="CMS-Tools",
                        dbquery='collections.primary:"CMS-Tools"',
                    ),
                    dict(
                        name="CMS-Validated-Runs",
                        dbquery='collections.primary:"CMS-Validated-Runs"',
                    ),
                    dict(
                        name="CMS-Learning-Resources",
                        dbquery='collections.primary:"CMS-Learning-Resources"',
                    ),
                    dict(
                        name="CMS-Open-Data-Instructions",
                        dbquery='collections.primary:"CMS-Open-Data-Instructions"',
                    ),
                ],
            ),
            dict(
                name="ALICE",
                dbquery=None,
                children=[
                    dict(
                        name="ALICE-Derived-Datasets",
                        dbquery='collections.primary:"ALICE-Derived-Datasets"',
                    ),
                    dict(
                        name="ALICE-Tools",
                        dbquery='collections.primary:"ALICE-Tools"',
                    ),
                    dict(
                        name="ALICE-Reconstructed-Data",
                        dbquery='collections.primary:"ALICE-Reconstructed-Data"',
                    ),
                    dict(
                        name="ALICE-Learning-Resources",
                        dbquery='collections.primary:"ALICE-Learning-Resources"',
                    ),
                ],
            ),
            dict(
                name="ATLAS",
                dbquery=None,
                children=[
                    dict(
                        name="ATLAS-Derived-Datasets",
                        dbquery='collections.primary:"ATLAS-Derived-Datasets"',
                    ),
                    dict(
                        name="ATLAS-Learning-Resources",
                        dbquery='collections.primary:"ATLAS-Learning-Resources"',
                    ),
                    dict(
                        name="ATLAS-Tools",
                        dbquery='collections.primary:"ATLAS-Tools"',
                    ),
                    dict(
                        name="ATLAS-Higgs-Challenge-2014",
                        dbquery='collections.primary:"ATLAS-Higgs-Challenge-2014"',
                    ),
                ],
            ),
            dict(
                name="LHCb",
                dbquery=None,
                children=[
                    dict(
                        name="LHCb-Derived-Datasets",
                        dbquery='collections.primary:"LHCb-Derived-Datasets"',
                    ),
                    dict(
                        name="LHCb-Tools",
                        dbquery='collections.primary:"LHCb-Tools"',
                    ),
                    dict(
                        name="LHCb-Learning-Resources",
                        dbquery='collections.primary:"LHCb-Learning-Resources"',
                    ),
                ],
            ),
            dict(
                name="Author-Lists",
                dbquery='collections.primary:"Author-Lists"',
            ),
            dict(
                name="Data-Policies",
                dbquery='collections.primary:"Data-Policies"',
            ),
        ],
    ),
]
