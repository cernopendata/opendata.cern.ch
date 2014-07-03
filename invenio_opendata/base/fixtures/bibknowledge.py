# -*- coding: utf-8 -*-
#
## This file is part of Invenio.
## Copyright (C) 2013 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

from fixture import DataSet


class KnwKBData(DataSet):

    class KnwKB_1:
        name = u'DBCOLLID2COLL'
        description = u'DbCollID to Coll name correspondance.'
        kbtype = None
        id = 1

    class KnwKB_2:
        name = u'EJOURNALS'
        description = u'Knowledge base of all known electronic journals.  Useful for reference linking.'
        kbtype = None
        id = 2

    class KnwKB_3:
        name = u'DBCOLLID2BIBTEX'
        description = u'Mapping between the 980 field and BibTeX entry types.'
        kbtype = None
        id = 3

    class KnwKB_4:
        name = u'SEARCH-SYNONYM-JOURNAL'
        description = u'Knowledge base of journal title synonyms.  Used during search time.'
        kbtype = None
        id = 4

    class KnwKB_5:
        name = u'INDEX-SYNONYM-TITLE'
        description = u'Knowledge base of title word synonyms.  Used during indexing time.'
        kbtype = None
        id = 5

    class KnwKB_6:
        name = u'DBCOLLID2OPENGRAPHTYPE'
        description = u'Maps collection 980 field to an Open Graph Type'
        kbtype = None
        id = 6

    class KnwKB_7:
        name = u'LICENSE2URL'
        description = u'Map a license name to its URL'
        kbtype = None
        id = 7


class KnwKBRVALData(DataSet):

    class KnwKBRVAL_1:
        m_key = u'ARTICLE'
        m_value = u'Published Article'
        id = 1
        id_knwKB = KnwKBData.KnwKB_1.ref('id')

    class KnwKBRVAL_2:
        m_key = u'PREPRINT'
        m_value = u'Preprint'
        id = 2
        id_knwKB = KnwKBData.KnwKB_1.ref('id')

    class KnwKBRVAL_3:
        m_key = u'THESIS'
        m_value = u'Thesis'
        id = 3
        id_knwKB = KnwKBData.KnwKB_1.ref('id')

    class KnwKBRVAL_4:
        m_key = u'BOOK'
        m_value = u'Book'
        id = 4
        id_knwKB = KnwKBData.KnwKB_1.ref('id')

    class KnwKBRVAL_5:
        m_key = u'REPORT'
        m_value = u'Report'
        id = 5
        id_knwKB = KnwKBData.KnwKB_1.ref('id')

    class KnwKBRVAL_6:
        m_key = u'PICTURE'
        m_value = u'Pictures'
        id = 6
        id_knwKB = KnwKBData.KnwKB_1.ref('id')

    class KnwKBRVAL_7:
        m_key = u'AAS Photo Bull.'
        m_value = u'AAS Photo Bull.'
        id = 7
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_8:
        m_key = u'Accredit. Qual. Assur.'
        m_value = u'Accredit. Qual. Assur.'
        id = 8
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_9:
        m_key = u'Acoust. Phys.'
        m_value = u'Acoust. Phys.'
        id = 9
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_10:
        m_key = u'Acoust. Res. Lett.'
        m_value = u'Acoust. Res. Lett.'
        id = 10
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_11:
        m_key = u'Acta Astron.'
        m_value = u'Acta Astron.'
        id = 11
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_12:
        m_key = u'Adv. Comput. Math.'
        m_value = u'Adv. Comput. Math.'
        id = 12
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_13:
        m_key = u'Aequ. Math.'
        m_value = u'Aequ. Math.'
        id = 13
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_14:
        m_key = u'Afr. Skies'
        m_value = u'Afr. Skies'
        id = 14
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_15:
        m_key = u'Algorithmica'
        m_value = u'Algorithmica'
        id = 15
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_16:
        m_key = u'Am. J. Phys.'
        m_value = u'Am. J. Phys.'
        id = 16
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_17:
        m_key = u'Ann. Phys.'
        m_value = u'Ann. Phys.'
        id = 17
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_18:
        m_key = u'Annu. Rev. Astron. Astrophys.'
        m_value = u'Annu. Rev. Astron. Astrophys.'
        id = 18
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_19:
        m_key = u'Annu. Rev. Earth Planet. Sci.'
        m_value = u'Annu. Rev. Earth Planet. Sci.'
        id = 19
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_20:
        m_key = u'Appl. Phys. Lett.'
        m_value = u'Appl. Phys. Lett.'
        id = 20
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_21:
        m_key = u'Appl. Phys., A'
        m_value = u'Appl. Phys., A'
        id = 21
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_22:
        m_key = u'Appl. Phys., B'
        m_value = u'Appl. Phys., B'
        id = 22
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_23:
        m_key = u'Appl. Radiat. Isot.'
        m_value = u'Appl. Radiat. Isot.'
        id = 23
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_24:
        m_key = u'Appl. Surf. Sci.'
        m_value = u'Appl. Surf. Sci.'
        id = 24
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_25:
        m_key = u'Arch. Appl. Mech.'
        m_value = u'Arch. Appl. Mech.'
        id = 25
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_26:
        m_key = u'Arch. Envir. Contam. Toxicol.'
        m_value = u'Arch. Envir. Contam. Toxicol.'
        id = 26
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_27:
        m_key = u'Arch. Rational Mech. Analys.'
        m_value = u'Arch. Rational Mech. Analys.'
        id = 27
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_28:
        m_key = u'Astron. Astrophys. Rev.'
        m_value = u'Astron. Astrophys. Rev.'
        id = 28
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_29:
        m_key = u'Astron. Astrophys.'
        m_value = u'Astron. Astrophys.'
        id = 29
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_30:
        m_key = u'Astron. Astrophys., Suppl.'
        m_value = u'Astron. Astrophys., Suppl.'
        id = 30
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_31:
        m_key = u'Astron. J.'
        m_value = u'Astron. J.'
        id = 31
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_32:
        m_key = u'Astron. Lett.'
        m_value = u'Astron. Lett.'
        id = 32
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_33:
        m_key = u'Astron. Nachr.'
        m_value = u'Astron. Nachr.'
        id = 33
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_34:
        m_key = u'Astron. Rep.'
        m_value = u'Astron. Rep.'
        id = 34
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_35:
        m_key = u'Astropart. Phys.'
        m_value = u'Astropart. Phys.'
        id = 35
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_36:
        m_key = u'Astrophys. J.'
        m_value = u'Astrophys. J.'
        id = 36
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_37:
        m_key = u'Astrophys. Norvegica'
        m_value = u'Astrophys. Norvegica'
        id = 37
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_38:
        m_key = u'Balt. Astron.'
        m_value = u'Balt. Astron.'
        id = 38
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_39:
        m_key = u'Bioimaging'
        m_value = u'Bioimaging'
        id = 39
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_40:
        m_key = u'Biol. Cybern.'
        m_value = u'Biol. Cybern.'
        id = 40
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_41:
        m_key = u'Bull. Astron. Belgrade'
        m_value = u'Bull. Astron. Belgrade'
        id = 41
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_42:
        m_key = u'Bull. Astron. Inst. Czech.'
        m_value = u'Bull. Astron. Inst. Czech.'
        id = 42
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_43:
        m_key = u'Bull. Astron. Soc. India'
        m_value = u'Bull. Astron. Soc. India'
        id = 43
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_44:
        m_key = u'Bull. Eng. Geol. Environ.'
        m_value = u'Bull. Eng. Geol. Environ.'
        id = 44
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_45:
        m_key = u'Bull. Environ. Contam. Toxicol.'
        m_value = u'Bull. Environ. Contam. Toxicol.'
        id = 45
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_46:
        m_key = u'Calc. Var. Partial Differ. Equ.'
        m_value = u'Calc. Var. Partial Differ. Equ.'
        id = 46
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_47:
        m_key = u'Chaos'
        m_value = u'Chaos'
        id = 47
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_48:
        m_key = u'Chaos Solitons Fractals'
        m_value = u'Chaos Solitons Fractals'
        id = 48
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_49:
        m_key = u'Chem. Phys.'
        m_value = u'Chem. Phys.'
        id = 49
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_50:
        m_key = u'Chem. Phys. Lett.'
        m_value = u'Chem. Phys. Lett.'
        id = 50
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_51:
        m_key = u'Chin. Astron. Astrophys.'
        m_value = u'Chin. Astron. Astrophys.'
        id = 51
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_52:
        m_key = u'Chin. J. Astron. Astrophys.'
        m_value = u'Chin. J. Astron. Astrophys.'
        id = 52
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_53:
        m_key = u'Class. Quantum Gravity'
        m_value = u'Class. Quantum Gravity'
        id = 53
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_54:
        m_key = u'Clim. Dyn.'
        m_value = u'Clim. Dyn.'
        id = 54
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_55:
        m_key = u'Colloid Polym. Sci.'
        m_value = u'Colloid Polym. Sci.'
        id = 55
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_56:
        m_key = u'Combinatorica'
        m_value = u'Combinatorica'
        id = 56
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_57:
        m_key = u'Combust. Theory Model.'
        m_value = u'Combust. Theory Model.'
        id = 57
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_58:
        m_key = u'Commun. Math. Phys.'
        m_value = u'Commun. Math. Phys.'
        id = 58
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_59:
        m_key = u'Comment. Math. Helv.'
        m_value = u'Comment. Math. Helv.'
        id = 59
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_60:
        m_key = u'Comput. Mech.'
        m_value = u'Comput. Mech.'
        id = 60
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_61:
        m_key = u'Comput. Phys.'
        m_value = u'Comput. Phys.'
        id = 61
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_62:
        m_key = u'Comput. Phys. Commun.'
        m_value = u'Comput. Phys. Commun.'
        id = 62
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_63:
        m_key = u'Comput. Sci. Eng.'
        m_value = u'Comput. Sci. Eng.'
        id = 63
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_64:
        m_key = u'Comput. Vis. Sci.'
        m_value = u'Comput. Vis. Sci.'
        id = 64
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_65:
        m_key = u'Computing'
        m_value = u'Computing'
        id = 65
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_66:
        m_key = u'Constr. Approx.'
        m_value = u'Constr. Approx.'
        id = 66
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_67:
        m_key = u'Contin. Mech. Thermodyn.'
        m_value = u'Contin. Mech. Thermodyn.'
        id = 67
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_68:
        m_key = u'Contrib. Astron. Obs. Skaln. Pleso'
        m_value = u'Contrib. Astron. Obs. Skaln. Pleso'
        id = 68
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_69:
        m_key = u'Contrib. Astron. Obs. Skaln. Pleso Suppl.'
        m_value = u'Contrib. Astron. Obs. Skaln. Pleso Suppl.'
        id = 69
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_70:
        m_key = u'Cryogenics'
        m_value = u'Cryogenics'
        id = 70
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_71:
        m_key = u'Crystallogr. Rep.'
        m_value = u'Crystallogr. Rep.'
        id = 71
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_72:
        m_key = u'Curr. Appl. Phys.'
        m_value = u'Curr. Appl. Phys.'
        id = 72
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_73:
        m_key = u'Curr. Opin. Solid State Mater. Sci.'
        m_value = u'Curr. Opin. Solid State Mater. Sci.'
        id = 73
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_74:
        m_key = u'Discret. Comput. Geom.'
        m_value = u'Discret. Comput. Geom.'
        id = 74
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_75:
        m_key = u'Displays'
        m_value = u'Displays'
        id = 75
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_76:
        m_key = u'Distrib. Comput.'
        m_value = u'Distrib. Comput.'
        id = 76
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_77:
        m_key = u'Distrib. Syst. Eng.'
        m_value = u'Distrib. Syst. Eng.'
        id = 77
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_78:
        m_key = u'Dokl. Phys.'
        m_value = u'Dokl. Phys.'
        id = 78
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_79:
        m_key = u'Electrochem. Solid State Lett.'
        m_value = u'Electrochem. Solid State Lett.'
        id = 79
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_80:
        m_key = u'Electron. Lett.'
        m_value = u'Electron. Lett.'
        id = 80
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_81:
        m_key = u'Elem. Math.'
        m_value = u'Elem. Math.'
        id = 81
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_82:
        m_key = u'Environ. Geol.'
        m_value = u'Environ. Geol.'
        id = 82
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_83:
        m_key = u'Environ. Manage.'
        m_value = u'Environ. Manage.'
        id = 83
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_84:
        m_key = u'Eur. Biophys. J. Biophys. Lett.'
        m_value = u'Eur. Biophys. J. Biophys. Lett.'
        id = 84
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_85:
        m_key = u'Eur. J. Phys.'
        m_value = u'Eur. J. Phys.'
        id = 85
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_86:
        m_key = u'Eur. Phys. J., A'
        m_value = u'Eur. Phys. J., A'
        id = 86
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_87:
        m_key = u'Eur. Phys. J., Appl. Phys.'
        m_value = u'Eur. Phys. J., Appl. Phys.'
        id = 87
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_88:
        m_key = u'Eur. Phys. J., B'
        m_value = u'Eur. Phys. J., B'
        id = 88
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_89:
        m_key = u'Eur. Phys. J., C'
        m_value = u'Eur. Phys. J., C'
        id = 89
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_90:
        m_key = u'Eur. Phys. J., D'
        m_value = u'Eur. Phys. J., D'
        id = 90
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_91:
        m_key = u'Eur. Phys. J., E'
        m_value = u'Eur. Phys. J., E'
        id = 91
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_92:
        m_key = u'Europhys. Lett.'
        m_value = u'Europhys. Lett.'
        id = 92
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_93:
        m_key = u'Europhys. News'
        m_value = u'Europhys. News'
        id = 93
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_94:
        m_key = u'Exp. Fluids'
        m_value = u'Exp. Fluids'
        id = 94
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_95:
        m_key = u'Few-Body Syst.'
        m_value = u'Few-Body Syst.'
        id = 95
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_96:
        m_key = u'Finan. Stoch.'
        m_value = u'Finan. Stoch.'
        id = 96
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_97:
        m_key = u'Fluid Dyn. Res.'
        m_value = u'Fluid Dyn. Res.'
        id = 97
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_98:
        m_key = u'Geom. Funct. Anal.'
        m_value = u'Geom. Funct. Anal.'
        id = 98
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_99:
        m_key = u'Heat Mass Transf.'
        m_value = u'Heat Mass Transf.'
        id = 99
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_100:
        m_key = u'High Energy Phys. Libr. Webzine'
        m_value = u'High Energy Phys. Libr. Webzine'
        id = 100
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_101:
        m_key = u'High Perform. Polym.'
        m_value = u'High Perform. Polym.'
        id = 101
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_102:
        m_key = u'IEE Proc., Circ. Devices Syst.'
        m_value = u'IEE Proc., Circ. Devices Syst.'
        id = 102
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_103:
        m_key = u'IEE Proc., Commun.'
        m_value = u'IEE Proc., Commun.'
        id = 103
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_104:
        m_key = u'IEE Proc., Comput. Digit. Tech.'
        m_value = u'IEE Proc., Comput. Digit. Tech.'
        id = 104
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_105:
        m_key = u'IEE Proc., Control Theory Appl.'
        m_value = u'IEE Proc., Control Theory Appl.'
        id = 105
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_106:
        m_key = u'IEE Proc., Electr. Power Appl.'
        m_value = u'IEE Proc., Electr. Power Appl.'
        id = 106
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_107:
        m_key = u'IEE Proc., Gener. Transm. Distrib.'
        m_value = u'IEE Proc., Gener. Transm. Distrib.'
        id = 107
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_108:
        m_key = u'IEE Proc., Microw. Antennas Propag.'
        m_value = u'IEE Proc., Microw. Antennas Propag.'
        id = 108
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_109:
        m_key = u'IEE Proc., Optoelectron.'
        m_value = u'IEE Proc., Optoelectron.'
        id = 109
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_110:
        m_key = u'IEE Proc., Radar, Sonar Navig.'
        m_value = u'IEE Proc., Radar, Sonar Navig.'
        id = 110
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_111:
        m_key = u'IEE Proc., Sci. Meas. Technol.'
        m_value = u'IEE Proc., Sci. Meas. Technol.'
        id = 111
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_112:
        m_key = u'IEE Proc., Softw. Eng.'
        m_value = u'IEE Proc., Softw. Eng.'
        id = 112
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_113:
        m_key = u'IEE Proc., Vis. Image Signal Process.'
        m_value = u'IEE Proc., Vis. Image Signal Process.'
        id = 113
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_114:
        m_key = u'Image Vis. Comput.'
        m_value = u'Image Vis. Comput.'
        id = 114
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_115:
        m_key = u'Inform. Forsch. Entwickl.'
        m_value = u'Inform. Forsch. Entwickl.'
        id = 115
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_116:
        m_key = u'Inform. Spektr.'
        m_value = u'Inform. Spektr.'
        id = 116
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_117:
        m_key = u'Infrared Phys. Technol.'
        m_value = u'Infrared Phys. Technol.'
        id = 117
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_118:
        m_key = u'Int. J. Digit. Libr.'
        m_value = u'Int. J. Digit. Libr.'
        id = 118
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_119:
        m_key = u'Int. J. Doc. Anal. Recogn.'
        m_value = u'Int. J. Doc. Anal. Recogn.'
        id = 119
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_120:
        m_key = u'Int. J. Nonlinear Mech.'
        m_value = u'Int. J. Nonlinear Mech.'
        id = 120
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_121:
        m_key = u'Int. J. Softw. Tools Technol. Transf.'
        m_value = u'Int. J. Softw. Tools Technol. Transf.'
        id = 121
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_122:
        m_key = u'Invent. Math.'
        m_value = u'Invent. Math.'
        id = 122
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_123:
        m_key = u'Inverse Probl.'
        m_value = u'Inverse Probl.'
        id = 123
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_124:
        m_key = u'J. Acoust. Soc. Am.'
        m_value = u'J. Acoust. Soc. Am.'
        id = 124
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_125:
        m_key = u'J. Aerosp. Eng.'
        m_value = u'J. Aerosp. Eng.'
        id = 125
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_126:
        m_key = u'J. Alloys. Compounds'
        m_value = u'J. Alloys. Compounds'
        id = 126
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_127:
        m_key = u'J. Am. Assoc. Var. Star Obs.'
        m_value = u'J. Am. Assoc. Var. Star Obs.'
        id = 127
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_128:
        m_key = u'J. Appl. Mech.'
        m_value = u'J. Appl. Mech.'
        id = 128
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_129:
        m_key = u'J. Appl. Phys.'
        m_value = u'J. Appl. Phys.'
        id = 129
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_130:
        m_key = u'J. Atmos. Solar Terrest. Phys.'
        m_value = u'J. Atmos. Solar Terrest. Phys.'
        id = 130
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_131:
        m_key = u'J. Br. Astron. Assoc.'
        m_value = u'J. Br. Astron. Assoc.'
        id = 131
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_132:
        m_key = u'J. Chem. Phys.'
        m_value = u'J. Chem. Phys.'
        id = 132
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_133:
        m_key = u'J. Classif.'
        m_value = u'J. Classif.'
        id = 133
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_134:
        m_key = u'J. Comput. Inf. Sci. Eng.'
        m_value = u'J. Comput. Inf. Sci. Eng.'
        id = 134
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_135:
        m_key = u'J. Constr. Eng. Manage.'
        m_value = u'J. Constr. Eng. Manage.'
        id = 135
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_136:
        m_key = u'J. Cryptol.'
        m_value = u'J. Cryptol.'
        id = 136
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_137:
        m_key = u'J. Cryst. Growth'
        m_value = u'J. Cryst. Growth'
        id = 137
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_138:
        m_key = u'J. Dyn. Syst. Meas. Control'
        m_value = u'J. Dyn. Syst. Meas. Control'
        id = 138
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_139:
        m_key = u'J. Electrochem. Soc.'
        m_value = u'J. Electrochem. Soc.'
        id = 139
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_140:
        m_key = u'J. Electron Spectrosc. Relat. Phen.'
        m_value = u'J. Electron Spectrosc. Relat. Phen.'
        id = 140
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_141:
        m_key = u'J. Electron. Imaging'
        m_value = u'J. Electron. Imaging'
        id = 141
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_142:
        m_key = u'J. Electron. Packag.'
        m_value = u'J. Electron. Packag.'
        id = 142
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_143:
        m_key = u'J. Energy Eng.'
        m_value = u'J. Energy Eng.'
        id = 143
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_144:
        m_key = u'J. Energy Resour. Technol.'
        m_value = u'J. Energy Resour. Technol.'
        id = 144
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_145:
        m_key = u'J. Eng. Mater. Technol.'
        m_value = u'J. Eng. Mater. Technol.'
        id = 145
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_146:
        m_key = u'J. Eng. Mech.'
        m_value = u'J. Eng. Mech.'
        id = 146
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_147:
        m_key = u'J. Environ. Eng.'
        m_value = u'J. Environ. Eng.'
        id = 147
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_148:
        m_key = u'J. Exp. Theor. Phys., JETP'
        m_value = u'J. Exp. Theor. Phys., JETP'
        id = 148
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_149:
        m_key = u'J. Fluids Eng.'
        m_value = u'J. Fluids Eng.'
        id = 149
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_150:
        m_key = u'J. Geom. Phys.'
        m_value = u'J. Geom. Phys.'
        id = 150
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_151:
        m_key = u'J. Heat Transf.'
        m_value = u'J. Heat Transf.'
        id = 151
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_152:
        m_key = u'J. High Energy Phys.'
        m_value = u'J. High Energy Phys.'
        id = 152
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_153:
        m_key = u'J. Korean Astron. Soc.'
        m_value = u'J. Korean Astron. Soc.'
        id = 153
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_154:
        m_key = u'J. Lumin.'
        m_value = u'J. Lumin.'
        id = 154
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_155:
        m_key = u'J. Magn. Magn. Mater.'
        m_value = u'J. Magn. Magn. Mater.'
        id = 155
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_156:
        m_key = u'J. Manage. Eng.'
        m_value = u'J. Manage. Eng.'
        id = 156
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_157:
        m_key = u'J. Manuf. Sci. Eng.'
        m_value = u'J. Manuf. Sci. Eng.'
        id = 157
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_158:
        m_key = u'J. Mater. Civ. Eng.'
        m_value = u'J. Mater. Civ. Eng.'
        id = 158
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_159:
        m_key = u'J. Math. Biol.'
        m_value = u'J. Math. Biol.'
        id = 159
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_160:
        m_key = u'J. Math. Phys.'
        m_value = u'J. Math. Phys.'
        id = 160
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_161:
        m_key = u'J. Mech. Des.'
        m_value = u'J. Mech. Des.'
        id = 161
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_162:
        m_key = u'J. Micromech. Microeng.'
        m_value = u'J. Micromech. Microeng.'
        id = 162
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_163:
        m_key = u'J. Opt.'
        m_value = u'J. Opt.'
        id = 163
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_164:
        m_key = u'J. Phys., A'
        m_value = u'J. Phys., A'
        id = 164
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_165:
        m_key = u'J. Phys., B'
        m_value = u'J. Phys., B'
        id = 165
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_166:
        m_key = u'J. Phys., Condens. Matter'
        m_value = u'J. Phys., Condens. Matter'
        id = 166
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_167:
        m_key = u'J. Phys., D'
        m_value = u'J. Phys., D'
        id = 167
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_168:
        m_key = u'J. Phys., G'
        m_value = u'J. Phys., G'
        id = 168
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_169:
        m_key = u'J. Phys. I'
        m_value = u'J. Phys. I'
        id = 169
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_170:
        m_key = u'J. Phys. II'
        m_value = u'J. Phys. II'
        id = 170
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_171:
        m_key = u'J. Phys. III'
        m_value = u'J. Phys. III'
        id = 171
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_172:
        m_key = u'J. Phys. Chem. Ref. Data'
        m_value = u'J. Phys. Chem. Ref. Data'
        id = 172
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_173:
        m_key = u'J. Phys. Chem. Solids'
        m_value = u'J. Phys. Chem. Solids'
        id = 173
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_174:
        m_key = u'J. Quant. Spectrosc. Radiat. Transf.'
        m_value = u'J. Quant. Spectrosc. Radiat. Transf.'
        id = 174
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_175:
        m_key = u'J. R. Astron. Soc. Can.'
        m_value = u'J. R. Astron. Soc. Can.'
        id = 175
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_176:
        m_key = u'J. Radio. Prot.'
        m_value = u'J. Radio. Prot.'
        id = 176
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_177:
        m_key = u'J. Rheol.'
        m_value = u'J. Rheol.'
        id = 177
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_178:
        m_key = u'J. Solar Energy Eng.'
        m_value = u'J. Solar Energy Eng.'
        id = 178
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_179:
        m_key = u'J. Solid State Electrochem.'
        m_value = u'J. Solid State Electrochem.'
        id = 179
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_180:
        m_key = u'J. Struct. Eng.'
        m_value = u'J. Struct. Eng.'
        id = 180
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_181:
        m_key = u'J. Surv. Eng.'
        m_value = u'J. Surv. Eng.'
        id = 181
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_182:
        m_key = u'J. Tribol.'
        m_value = u'J. Tribol.'
        id = 182
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_183:
        m_key = u'J. Turbomach.'
        m_value = u'J. Turbomach.'
        id = 183
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_184:
        m_key = u'J. Vac. Sci. Technol.'
        m_value = u'J. Vac. Sci. Technol.'
        id = 184
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_185:
        m_key = u'J. Vac. Sci. Technol., A'
        m_value = u'J. Vac. Sci. Technol., A'
        id = 185
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_186:
        m_key = u'J. Vac. Sci. Technol., B'
        m_value = u'J. Vac. Sci. Technol., B'
        id = 186
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_187:
        m_key = u'J. Vib. Acoust.'
        m_value = u'J. Vib. Acoust.'
        id = 187
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_188:
        m_key = u'JETP'
        m_value = u'JETP'
        id = 188
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_189:
        m_key = u'JETP Lett.'
        m_value = u'JETP Lett.'
        id = 189
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_190:
        m_key = u'Low Temp. Phys.'
        m_value = u'Low Temp. Phys.'
        id = 190
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_191:
        m_key = u'Mach. Vis. Appl.'
        m_value = u'Mach. Vis. Appl.'
        id = 191
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_192:
        m_key = u'Mater. Res. Innov.'
        m_value = u'Mater. Res. Innov.'
        id = 192
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_193:
        m_key = u'Mater. Sci. Eng., B'
        m_value = u'Mater. Sci. Eng., B'
        id = 193
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_194:
        m_key = u'Math. Ann.'
        m_value = u'Math. Ann.'
        id = 194
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_195:
        m_key = u'Math. Model. Numer. Anal.'
        m_value = u'Math. Model. Numer. Anal.'
        id = 195
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_196:
        m_key = u'Math. Program.'
        m_value = u'Math. Program.'
        id = 196
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_197:
        m_key = u'Math. Z.'
        m_value = u'Math. Z.'
        id = 197
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_198:
        m_key = u'Meas. Sci. Technol.'
        m_value = u'Meas. Sci. Technol.'
        id = 198
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_199:
        m_key = u'Med. Phys.'
        m_value = u'Med. Phys.'
        id = 199
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_200:
        m_key = u'Meteorit. Planet. Sci.'
        m_value = u'Meteorit. Planet. Sci.'
        id = 200
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_201:
        m_key = u'Microelectron. Eng.'
        m_value = u'Microelectron. Eng.'
        id = 201
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_202:
        m_key = u'Micron'
        m_value = u'Micron'
        id = 202
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_203:
        m_key = u'Microsc. Microanal.'
        m_value = u'Microsc. Microanal.'
        id = 203
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_204:
        m_key = u'Microsyst. Technol.'
        m_value = u'Microsyst. Technol.'
        id = 204
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_205:
        m_key = u'Mon. Not. R. Astron. Soc.'
        m_value = u'Mon. Not. R. Astron. Soc.'
        id = 205
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_206:
        m_key = u'Multim. Syst.'
        m_value = u'Multim. Syst.'
        id = 206
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_207:
        m_key = u'Nanotech.'
        m_value = u'Nanotech.'
        id = 207
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_208:
        m_key = u'Naturwiss.'
        m_value = u'Naturwiss.'
        id = 208
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_209:
        m_key = u'Network'
        m_value = u'Network'
        id = 209
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_210:
        m_key = u'New Astron.'
        m_value = u'New Astron.'
        id = 210
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_211:
        m_key = u'New Astron. Rev.'
        m_value = u'New Astron. Rev.'
        id = 211
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_212:
        m_key = u'Nonlinearity'
        m_value = u'Nonlinearity'
        id = 212
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_213:
        m_key = u'Nucl. Instrum. Methods Phys. Res., A'
        m_value = u'Nucl. Instrum. Methods Phys. Res., A'
        id = 213
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_214:
        m_key = u'Nucl. Instrum. Methods Phys. Res., B'
        m_value = u'Nucl. Instrum. Methods Phys. Res., B'
        id = 214
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_215:
        m_key = u'Nucl. Phys. B, Proc. Suppl.'
        m_value = u'Nucl. Phys. B, Proc. Suppl.'
        id = 215
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_216:
        m_key = u'Nucl. Phys., A'
        m_value = u'Nucl. Phys., A'
        id = 216
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_217:
        m_key = u'Nucl. Phys., B'
        m_value = u'Nucl. Phys., B'
        id = 217
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_218:
        m_key = u'Num. Math.'
        m_value = u'Num. Math.'
        id = 218
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_219:
        m_key = u'Nuovo Cimento, A'
        m_value = u'Nuovo Cimento, A'
        id = 219
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_220:
        m_key = u'Nuovo Cimento, B'
        m_value = u'Nuovo Cimento, B'
        id = 220
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_221:
        m_key = u'Nuovo Cimento, C'
        m_value = u'Nuovo Cimento, C'
        id = 221
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_222:
        m_key = u'Nuovo Cimento, D'
        m_value = u'Nuovo Cimento, D'
        id = 222
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_223:
        m_key = u'Obs.'
        m_value = u'Obs.'
        id = 223
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_224:
        m_key = u'Opt. Commun.'
        m_value = u'Opt. Commun.'
        id = 224
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_225:
        m_key = u'Opt. Eng.'
        m_value = u'Opt. Eng.'
        id = 225
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_226:
        m_key = u'Opt. Lasers Eng.'
        m_value = u'Opt. Lasers Eng.'
        id = 226
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_227:
        m_key = u'Opt. Mater.'
        m_value = u'Opt. Mater.'
        id = 227
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_228:
        m_key = u'Opt. Spectrosc.'
        m_value = u'Opt. Spectrosc.'
        id = 228
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_229:
        m_key = u'Phys. At. Nucl.'
        m_value = u'Phys. At. Nucl.'
        id = 229
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_230:
        m_key = u'Phys. Chem. Miner.'
        m_value = u'Phys. Chem. Miner.'
        id = 230
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_231:
        m_key = u'Phys. Educ.'
        m_value = u'Phys. Educ.'
        id = 231
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_232:
        m_key = u'Phys. Fluids'
        m_value = u'Phys. Fluids'
        id = 232
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_233:
        m_key = u'Phys. Fluids, A'
        m_value = u'Phys. Fluids, A'
        id = 233
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_234:
        m_key = u'Phys. Fluids, B'
        m_value = u'Phys. Fluids, B'
        id = 234
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_235:
        m_key = u'Phys. Lett., A'
        m_value = u'Phys. Lett., A'
        id = 235
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_236:
        m_key = u'Phys. Lett., B'
        m_value = u'Phys. Lett., B'
        id = 236
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_237:
        m_key = u'Phys. Med. Biol.'
        m_value = u'Phys. Med. Biol.'
        id = 237
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_238:
        m_key = u'Phys. Part. Nucl.'
        m_value = u'Phys. Part. Nucl.'
        id = 238
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_239:
        m_key = u'Phys. Plasmas'
        m_value = u'Phys. Plasmas'
        id = 239
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_240:
        m_key = u'Phys. Rep.'
        m_value = u'Phys. Rep.'
        id = 240
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_241:
        m_key = u'Phys. Rev., A'
        m_value = u'Phys. Rev., A'
        id = 241
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_242:
        m_key = u'Phys. Rev., B'
        m_value = u'Phys. Rev., B'
        id = 242
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_243:
        m_key = u'Phys. Rev., C'
        m_value = u'Phys. Rev., C'
        id = 243
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_244:
        m_key = u'Phys. Rev., D'
        m_value = u'Phys. Rev., D'
        id = 244
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_245:
        m_key = u'Phys. Rev., E'
        m_value = u'Phys. Rev., E'
        id = 245
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_246:
        m_key = u'Phys. Rev., ser. 1'
        m_value = u'Phys. Rev., ser. 1'
        id = 246
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_247:
        m_key = u'Phys. Rev. Lett.'
        m_value = u'Phys. Rev. Lett.'
        id = 247
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_248:
        m_key = u'Phys. Rev. Spec. Top. Accel. Beams'
        m_value = u'Phys. Rev. Spec. Top. Accel. Beams'
        id = 248
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_249:
        m_key = u'Phys. Rev.'
        m_value = u'Phys. Rev.'
        id = 249
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_250:
        m_key = u'Phys. Solid State'
        m_value = u'Phys. Solid State'
        id = 250
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_251:
        m_key = u'Physica, A'
        m_value = u'Physica, A'
        id = 251
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_252:
        m_key = u'Physica, B'
        m_value = u'Physica, B'
        id = 252
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_253:
        m_key = u'Physica, C'
        m_value = u'Physica, C'
        id = 253
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_254:
        m_key = u'Physica, D'
        m_value = u'Physica, D'
        id = 254
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_255:
        m_key = u'Physica, E'
        m_value = u'Physica, E'
        id = 255
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_256:
        m_key = u'Physiol. Meas.'
        m_value = u'Physiol. Meas.'
        id = 256
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_257:
        m_key = u'Planet. Space Sci.'
        m_value = u'Planet. Space Sci.'
        id = 257
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_258:
        m_key = u'Plasma Phys. Control. Fusion'
        m_value = u'Plasma Phys. Control. Fusion'
        id = 258
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_259:
        m_key = u'Plasma Phys. Rep.'
        m_value = u'Plasma Phys. Rep.'
        id = 259
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_260:
        m_key = u'Plasma Sources Sci. Technol.'
        m_value = u'Plasma Sources Sci. Technol.'
        id = 260
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_261:
        m_key = u'Polym. Bull.'
        m_value = u'Polym. Bull.'
        id = 261
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_262:
        m_key = u'Powder Diffraction'
        m_value = u'Powder Diffraction'
        id = 262
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_263:
        m_key = u'Probab. Theory Relat. Fields'
        m_value = u'Probab. Theory Relat. Fields'
        id = 263
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_264:
        m_key = u'Proc. Astron. Soc. Aust.'
        m_value = u'Proc. Astron. Soc. Aust.'
        id = 264
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_265:
        m_key = u'Proc. Nat. Acad. Sci.'
        m_value = u'Proc. Nat. Acad. Sci.'
        id = 265
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_266:
        m_key = u'Prog. Cryst. Growth Charact. Mat.'
        m_value = u'Prog. Cryst. Growth Charact. Mat.'
        id = 266
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_267:
        m_key = u'Prog. Part. Nucl. Phys.'
        m_value = u'Prog. Part. Nucl. Phys.'
        id = 267
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_268:
        m_key = u'Prog. Quantum Electron.'
        m_value = u'Prog. Quantum Electron.'
        id = 268
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_269:
        m_key = u'Prog. Surf. Sci.'
        m_value = u'Prog. Surf. Sci.'
        id = 269
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_270:
        m_key = u'Program'
        m_value = u'Program'
        id = 270
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_271:
        m_key = u'Publ. Astron. Soc. Aust.'
        m_value = u'Publ. Astron. Soc. Aust.'
        id = 271
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_272:
        m_key = u'Publ. Astron. Soc. Jpn.'
        m_value = u'Publ. Astron. Soc. Jpn.'
        id = 272
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_273:
        m_key = u'Publ. Astron. Soc. Pac.'
        m_value = u'Publ. Astron. Soc. Pac.'
        id = 273
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_274:
        m_key = u'Publ. Underst. Sci.'
        m_value = u'Publ. Underst. Sci.'
        id = 274
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_275:
        m_key = u'Pure Appl. Opt.: J. Eur. Opt. Soc. P. A'
        m_value = u'Pure Appl. Opt.: J. Eur. Opt. Soc. P. A'
        id = 275
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_276:
        m_key = u'Quantum Semiclass. Opt.: J. Eur. Opt. Soc. P. B'
        m_value = u'Quantum Semiclass. Opt.: J. Eur. Opt. Soc. P. B'
        id = 276
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_277:
        m_key = u'Radiat. Environ. Biophys.'
        m_value = u'Radiat. Environ. Biophys.'
        id = 277
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_278:
        m_key = u'Radiat. Meas.'
        m_value = u'Radiat. Meas.'
        id = 278
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_279:
        m_key = u'Radiat. Phys. Chem.'
        m_value = u'Radiat. Phys. Chem.'
        id = 279
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_280:
        m_key = u'Radiologe'
        m_value = u'Radiologe'
        id = 280
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_281:
        m_key = u'Radioprotection'
        m_value = u'Radioprotection'
        id = 281
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_282:
        m_key = u'Rep. Math. Phys.'
        m_value = u'Rep. Math. Phys.'
        id = 282
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_283:
        m_key = u'Rep. Prog. Phys.'
        m_value = u'Rep. Prog. Phys.'
        id = 283
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_284:
        m_key = u'Res. Exp. Med.'
        m_value = u'Res. Exp. Med.'
        id = 284
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_285:
        m_key = u'Rev. Mex. Astron. Astrofis.'
        m_value = u'Rev. Mex. Astron. Astrofis.'
        id = 285
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_286:
        m_key = u'Rev. Mod. Phys.'
        m_value = u'Rev. Mod. Phys.'
        id = 286
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_287:
        m_key = u'Rev. Sci. Instrum.'
        m_value = u'Rev. Sci. Instrum.'
        id = 287
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_288:
        m_key = u'Sel. Math., New Ser.'
        m_value = u'Sel. Math., New Ser.'
        id = 288
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_289:
        m_key = u'Semicond.'
        m_value = u'Semicond.'
        id = 289
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_290:
        m_key = u'Semicond. Sci. Technol.'
        m_value = u'Semicond. Sci. Technol.'
        id = 290
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_291:
        m_key = u'Shock Waves'
        m_value = u'Shock Waves'
        id = 291
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_292:
        m_key = u'SIAM J. Appl. Math.'
        m_value = u'SIAM J. Appl. Math.'
        id = 292
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_293:
        m_key = u'SIAM J. Comput.'
        m_value = u'SIAM J. Comput.'
        id = 293
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_294:
        m_key = u'SIAM J. Math. Anal.'
        m_value = u'SIAM J. Math. Anal.'
        id = 294
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_295:
        m_key = u'SIAM J. Numer. Anal.'
        m_value = u'SIAM J. Numer. Anal.'
        id = 295
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_296:
        m_key = u'SIAM J. Optim.'
        m_value = u'SIAM J. Optim.'
        id = 296
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_297:
        m_key = u'SIAM Rev.'
        m_value = u'SIAM Rev.'
        id = 297
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_298:
        m_key = u'Smart Mat. Struct.'
        m_value = u'Smart Mat. Struct.'
        id = 298
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_299:
        m_key = u'Soft Comput.'
        m_value = u'Soft Comput.'
        id = 299
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_300:
        m_key = u'Softw. Concepts Tools'
        m_value = u'Softw. Concepts Tools'
        id = 300
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_301:
        m_key = u'Solar Phys.'
        m_value = u'Solar Phys.'
        id = 301
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_302:
        m_key = u'Solid State Commun.'
        m_value = u'Solid State Commun.'
        id = 302
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_303:
        m_key = u'Solid State Electron.'
        m_value = u'Solid State Electron.'
        id = 303
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_304:
        m_key = u'Solid State Ion.'
        m_value = u'Solid State Ion.'
        id = 304
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_305:
        m_key = u'Sov. Astron. Lett.'
        m_value = u'Sov. Astron. Lett.'
        id = 305
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_306:
        m_key = u'Superconductor Science and Technology'
        m_value = u'Superconductor Science and Technology'
        id = 306
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_307:
        m_key = u'Surf. Coatings Techn.'
        m_value = u'Surf. Coatings Techn.'
        id = 307
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_308:
        m_key = u'Surf. Sci.'
        m_value = u'Surf. Sci.'
        id = 308
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_309:
        m_key = u'Surf. Sci. Rep.'
        m_value = u'Surf. Sci. Rep.'
        id = 309
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_310:
        m_key = u'Surf. Sci. Spectra'
        m_value = u'Surf. Sci. Spectra'
        id = 310
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_311:
        m_key = u'Synth. Metals'
        m_value = u'Synth. Metals'
        id = 311
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_312:
        m_key = u'Syst. Fam.'
        m_value = u'Syst. Fam.'
        id = 312
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_313:
        m_key = u'Tech. Phys.'
        m_value = u'Tech. Phys.'
        id = 313
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_314:
        m_key = u'Tech. Phys. Lett.'
        m_value = u'Tech. Phys. Lett.'
        id = 314
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_315:
        m_key = u'Theor. Comput. Fluid Dyn.'
        m_value = u'Theor. Comput. Fluid Dyn.'
        id = 315
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_316:
        m_key = u'Theory Comput. Syst.'
        m_value = u'Theory Comput. Syst.'
        id = 316
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_317:
        m_key = u'Thin Solid Films'
        m_value = u'Thin Solid Films'
        id = 317
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_318:
        m_key = u'Tribol. Int.'
        m_value = u'Tribol. Int.'
        id = 318
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_319:
        m_key = u'Ultramicroscopy'
        m_value = u'Ultramicroscopy'
        id = 319
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_320:
        m_key = u'Vacuum'
        m_value = u'Vacuum'
        id = 320
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_321:
        m_key = u'VLDB J.'
        m_value = u'VLDB J.'
        id = 321
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_322:
        m_key = u'Virtual J. Nanoscale Sci. Technol.'
        m_value = u'Virtual J. Nanoscale Sci. Technol.'
        id = 322
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_323:
        m_key = u'Virtual J. Biol. Phys. Res.'
        m_value = u'Virtual J. Biol. Phys. Res.'
        id = 323
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_324:
        m_key = u'Vis. Comput.'
        m_value = u'Vis. Comput.'
        id = 324
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_325:
        m_key = u'Wave Motion'
        m_value = u'Wave Motion'
        id = 325
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_326:
        m_key = u'Waves Random Media'
        m_value = u'Waves Random Media'
        id = 326
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_327:
        m_key = u'Wear'
        m_value = u'Wear'
        id = 327
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_328:
        m_key = u'Z. Angew. Math. Phys.'
        m_value = u'Z. Angew. Math. Phys.'
        id = 328
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_329:
        m_key = u'Z. Phys., A'
        m_value = u'Z. Phys., A'
        id = 329
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_330:
        m_key = u'Z. Phys., B'
        m_value = u'Z. Phys., B'
        id = 330
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_331:
        m_key = u'Z. Phys., C'
        m_value = u'Z. Phys., C'
        id = 331
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_332:
        m_key = u'Zphys-e.C'
        m_value = u'Zphys-e.C'
        id = 332
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_333:
        m_key = u'ATLAS eNews'
        m_value = u'ATLAS eNews'
        id = 333
        id_knwKB = KnwKBData.KnwKB_2.ref('id')

    class KnwKBRVAL_334:
        m_key = u'PICTURE'
        m_value = u'unpublished'
        id = 334
        id_knwKB = KnwKBData.KnwKB_3.ref('id')

    class KnwKBRVAL_335:
        m_key = u'PREPRINT'
        m_value = u'techreport'
        id = 335
        id_knwKB = KnwKBData.KnwKB_3.ref('id')

    class KnwKBRVAL_336:
        m_key = u'ARTICLE'
        m_value = u'article'
        id = 336
        id_knwKB = KnwKBData.KnwKB_3.ref('id')

    class KnwKBRVAL_337:
        m_key = u'REPORT'
        m_value = u'techreport'
        id = 337
        id_knwKB = KnwKBData.KnwKB_3.ref('id')

    class KnwKBRVAL_338:
        m_key = u'BOOK'
        m_value = u'book'
        id = 338
        id_knwKB = KnwKBData.KnwKB_3.ref('id')

    class KnwKBRVAL_339:
        m_key = u'THESIS'
        m_value = u'phdthesis'
        id = 339
        id_knwKB = KnwKBData.KnwKB_3.ref('id')

    class KnwKBRVAL_340:
        m_key = u'POETRY'
        m_value = u'unpublished'
        id = 340
        id_knwKB = KnwKBData.KnwKB_3.ref('id')

    class KnwKBRVAL_341:
        m_key = u'PHRVD'
        m_value = u'Phys. Rev., D'
        id = 341
        id_knwKB = KnwKBData.KnwKB_4.ref('id')

    class KnwKBRVAL_342:
        m_key = u'Phys.Rev.D'
        m_value = u'Phys. Rev., D'
        id = 342
        id_knwKB = KnwKBData.KnwKB_4.ref('id')

    class KnwKBRVAL_343:
        m_key = u'beta'
        m_value = u'\u03b2'
        id = 343
        id_knwKB = KnwKBData.KnwKB_5.ref('id')

    class KnwKBRVAL_344:
        m_key = u'\u03b2'
        m_value = u'beta'
        id = 344
        id_knwKB = KnwKBData.KnwKB_5.ref('id')

    class KnwKBRVAL_345:
        m_key = u'ARTICLE'
        m_value = u'article'
        id = 345
        id_knwKB = KnwKBData.KnwKB_6.ref('id')

    class KnwKBRVAL_346:
        m_key = u'BOOK'
        m_value = u'book'
        id = 346
        id_knwKB = KnwKBData.KnwKB_6.ref('id')

    class KnwKBRVAL_347:
        m_key = u'VIDEO'
        m_value = u'video.other'
        id = 347
        id_knwKB = KnwKBData.KnwKB_6.ref('id')

    class KnwKBRVAL_348:
        m_key = u'CERN'
        m_value = u'http://copyright.cern.ch/'
        id = 348
        id_knwKB = KnwKBData.KnwKB_7.ref('id')

    class KnwKBRVAL_349:
        m_key = u'CC-BY-3.0'
        m_value = u'http://creativecommons.org/licenses/by/3.0/'
        id = 349
        id_knwKB = KnwKBData.KnwKB_7.ref('id')

    class KnwKBRVAL_350:
        m_key = u'CC-BY-SA-3.0'
        m_value = u'http://creativecommons.org/licenses/by-sa/3.0/'
        id = 350
        id_knwKB = KnwKBData.KnwKB_7.ref('id')

    class KnwKBRVAL_351:
        m_key = u'CC-BY-NC-3.0'
        m_value = u'http://creativecommons.org/licenses/by-nc/3.0/'
        id = 351
        id_knwKB = KnwKBData.KnwKB_7.ref('id')

    class KnwKBRVAL_352:
        m_key = u'CC-BY-ND-3.0'
        m_value = u'http://creativecommons.org/licenses/by-nd/3.0/'
        id = 352
        id_knwKB = KnwKBData.KnwKB_7.ref('id')

    class KnwKBRVAL_353:
        m_key = u'CC-BY-NC-SA-3.0'
        m_value = u'http://creativecommons.org/licenses/by-nc-sa/3.0/'
        id = 353
        id_knwKB = KnwKBData.KnwKB_7.ref('id')

    class KnwKBRVAL_354:
        m_key = u'CC-BY-NC-ND-3.0'
        m_value = u'http://creativecommons.org/licenses/by-nc-nd/3.0/'
        id = 354
        id_knwKB = KnwKBData.KnwKB_7.ref('id')
