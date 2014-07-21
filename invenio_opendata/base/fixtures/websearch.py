# -*- coding: utf-8 -*-
#
## This file is part of Invenio.
## Copyright (C) 2012, 2013 CERN.
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

from invenio.config import CFG_SITE_NAME
from fixture import DataSet
from invenio.modules.search.fixtures import FormatData, FieldData


class ExternalcollectionData(DataSet):

    class amazon:
        id = 1
        name = 'Amazon'

    class CERNEDMS:
        id = 2
        name = 'CERN EDMS'

    class CERNIndico:
        id = 3
        name = 'CERN Indico'

    class CERNIntranet:
        id = 4
        name = 'CERN Intranet'

    class citeSeer:
        id = 5
        name = 'CiteSeer'

    class googleBooks:
        id = 6
        name = 'Google Books'

    class googleScholar:
        id = 7
        name = 'Google Scholar'

    class googleWeb:
        id = 8
        name = 'Google Web'

    class IEC:
        id = 9
        name = 'IEC'

    class IHS:
        id = 10
        name = 'IHS'

    class INSPEC:
        id = 11
        name = 'INSPEC'

    class ISO:
        id = 12
        name = 'ISO'

    class KISSBooksJournals:
        id = 13
        name = 'KISS Books/Journals'

    class KISSPreprints:
        id = 14
        name = 'KISS Preprints'

    class NEBIS:
        id = 15
        name = 'NEBIS'

    class SLACLibraryCatalog:
        id = 16
        name = 'SLAC Library Catalog'

    class INSPIRE:
        id = 17
        name = 'INSPIRE'

    class scirus:
        id = 18
        name = 'Scirus'

    class atlantisInstituteBooks:
        id = 19
        name = 'Atlantis Institute Books'

    class atlantisInstituteArticles:
        id = 20
        name = 'Atlantis Institute Articles'


class CollectionData(DataSet):

    class siteCollection:
        id = 1
        name = CFG_SITE_NAME
        dbquery = None
        externalcollections_0 = [
            ExternalcollectionData.atlantisInstituteBooks,
            ExternalcollectionData.atlantisInstituteArticles
        ]
        externalcollections_1 = [
            ExternalcollectionData.amazon,
            ExternalcollectionData.CERNEDMS,
            ExternalcollectionData.CERNIndico,
            ExternalcollectionData.CERNIntranet,
            ExternalcollectionData.citeSeer,
            ExternalcollectionData.googleBooks,
            ExternalcollectionData.googleScholar,
            ExternalcollectionData.googleWeb,
            ExternalcollectionData.IEC,
            ExternalcollectionData.IHS,
            ExternalcollectionData.INSPEC,
            ExternalcollectionData.ISO,
            ExternalcollectionData.KISSBooksJournals,
            ExternalcollectionData.KISSPreprints,
            ExternalcollectionData.NEBIS,
            ExternalcollectionData.SLACLibraryCatalog,
            ExternalcollectionData.INSPIRE,
            ExternalcollectionData.scirus
        ]

    class preprints:
        id = 2
        name = 'Preprints'
        dbquery = '980:"PREPRINT"'
        names = {
            ('en', 'ln'): u'Preprints',
            ('fr', 'ln'): u'Prétirages',
            ('de', 'ln'): u'Preprints',
            ('es', 'ln'): u'Preprints',
            ('ca', 'ln'): u'Preprints',
            ('pl', 'ln'): u'Preprinty',
            ('pt', 'ln'): u'Preprints',
            ('it', 'ln'): u'Preprint',
            ('ru', 'ln'): u'Препринты',
            ('sk', 'ln'): u'Preprinty',
            ('cs', 'ln'): u'Preprinty',
            ('no', 'ln'): u'Førtrykk',
            ('sv', 'ln'): u'Preprints',
            ('el', 'ln'): u'Προδημοσιεύσεις',
            ('uk', 'ln'): u'Препринти',
            ('ja', 'ln'): u'プレプリント',
            ('bg', 'ln'): u'Препринти',
            ('hr', 'ln'): u'Preprinti',
            ('zh_CN', 'ln'): u'预印',
            ('zh_TW', 'ln'): u'預印',
            ('hu', 'ln'): u'Preprintek',
            ('af', 'ln'): u'Pre-drukke',
            ('gl', 'ln'): u'Preprints',
            ('ro', 'ln'): u'Preprinturi',
            ('rw', 'ln'): u'Preprints',
            ('ka', 'ln'): u'პრეპრინტები',
            ('lt', 'ln'): u'Rankraščiai',
            ('ar', 'ln'): u'مسودات'
        }
        externalcollections_0 = [
            ExternalcollectionData.atlantisInstituteBooks,
            ExternalcollectionData.atlantisInstituteArticles
        ]
        externalcollections_1 = [
            ExternalcollectionData.amazon,
            ExternalcollectionData.CERNEDMS,
            ExternalcollectionData.CERNIntranet,
            ExternalcollectionData.googleBooks,
            ExternalcollectionData.googleScholar,
            ExternalcollectionData.googleWeb,
            ExternalcollectionData.IEC,
            ExternalcollectionData.IHS,
            ExternalcollectionData.INSPEC,
            ExternalcollectionData.ISO,
            ExternalcollectionData.NEBIS,
            ExternalcollectionData.SLACLibraryCatalog
        ]
        externalcollections_2 = [
            ExternalcollectionData.CERNIndico,
            ExternalcollectionData.citeSeer,
            ExternalcollectionData.KISSBooksJournals,
            ExternalcollectionData.KISSPreprints,
            ExternalcollectionData.INSPIRE,
            ExternalcollectionData.scirus
        ]

    class books(siteCollection):
        id = 3
        name = 'Books'
        dbquery = '980:"BOOK"'
        names = {
            ('en', 'ln'): u'Books',
            ('fr', 'ln'): u'Livres',
            ('de', 'ln'): u'Bücher',
            ('es', 'ln'): u'Libros',
            ('ca', 'ln'): u'Llibres',
            ('pl', 'ln'): u'Książki',
            ('pt', 'ln'): u'Livros',
            ('it', 'ln'): u'Libri',
            ('ru', 'ln'): u'Книги',
            ('sk', 'ln'): u'Knihy',
            ('cs', 'ln'): u'Knihy',
            ('no', 'ln'): u'Bøker',
            ('sv', 'ln'): u'',
            ('el', 'ln'): u'Βιβλία',
            ('uk', 'ln'): u'Книги',
            ('ja', 'ln'): u'本',
            ('bg', 'ln'): u'Книги',
            ('hr', 'ln'): u'Knjige',
            ('zh_CN', 'ln'): u'书本',
            ('zh_TW', 'ln'): u'書本',
            ('hu', 'ln'): u'Könyvek',
            ('af', 'ln'): u'Boeke',
            ('gl', 'ln'): u'Libros',
            ('ro', 'ln'): u'Cărţi',
            ('rw', 'ln'): u'Ibitabo',
            ('ka', 'ln'): u'წიგნები',
            ('lt', 'ln'): u'Knygos',
            ('ar', 'ln'): u'كتب',
        }




    class theses(siteCollection):
        id = 4
        name = 'Theses'
        dbquery = '980:"THESIS"'
        names = {
            ('en', 'ln'): u'Theses',
            ('fr', 'ln'): u'Thèses',
            ('de', 'ln'): u'Dissertationen',
            ('es', 'ln'): u'Tesis',
            ('ca', 'ln'): u'Tesis',
            ('pl', 'ln'): u'Prace naukowe',
            ('pt', 'ln'): u'Teses',
            ('it', 'ln'): u'Tesi',
            ('ru', 'ln'): u'Диссертации',
            ('sk', 'ln'): u'Dizertácie',
            ('cs', 'ln'): u'Disertace',
            ('no', 'ln'): u'Avhandlinger',
            ('sv', 'ln'): u'',
            ('el', 'ln'): u'Διατριβές',
            ('uk', 'ln'): u'Дисертації',
            ('ja', 'ln'): u'説',
            ('bg', 'ln'): u'Дисертации',
            ('hr', 'ln'): u'Disertacije',
            ('zh_CN', 'ln'): u'论文',
            ('zh_TW', 'ln'): u'論文',
            ('hu', 'ln'): u'Disszertációk',
            ('af', 'ln'): u'Tesise',
            ('gl', 'ln'): u'Teses',
            ('ro', 'ln'): u'Teze',
            ('rw', 'ln'): u'Igitabo ky\'ubushakashatsi',
            ('ka', 'ln'): u'თეზისები',
            ('lt', 'ln'): u'Disertacijos',
            ('ar', 'ln'): u'أطروحات',
        }

    class reports(siteCollection):
        id = 5
        name = 'Reports'
        dbquery = '980:"REPORT"'
        names = {
            ('en', 'ln'): u'Reports',
            ('fr', 'ln'): u'Rapports',
            ('de', 'ln'): u'Reports',
            ('es', 'ln'): u'Informes',
            ('ca', 'ln'): u'Informes',
            ('pl', 'ln'): u'Raporty',
            ('pt', 'ln'): u'Relatórios',
            ('it', 'ln'): u'Rapporti',
            ('ru', 'ln'): u'Рапорты',
            ('sk', 'ln'): u'Správy',
            ('cs', 'ln'): u'Zprávy',
            ('no', 'ln'): u'Rapporter',
            ('sv', 'ln'): u'',
            ('el', 'ln'): u'Αναφορές',
            ('uk', 'ln'): u'Звіти',
            ('ja', 'ln'): u'レポート',
            ('bg', 'ln'): u'Доклади',
            ('hr', 'ln'): u'Izvještaji',
            ('zh_CN', 'ln'): u'报告',
            ('zh_TW', 'ln'): u'報告',
            ('hu', 'ln'): u'Tanulmányok',
            ('af', 'ln'): u'Verslae',
            ('gl', 'ln'): u'Informes',
            ('ro', 'ln'): u'Rapoarte',
            ('rw', 'ln'): u'Raporo',
            ('ka', 'ln'): u'რეპორტები',
            ('lt', 'ln'): u'Pranešimai',
            ('ar', 'ln'): u'تقارير',
        }

    class articles(preprints):
        id = 6
        name = 'Articles'
        dbquery = '980:"ARTICLE"'
        names = {
            ('en', 'ln'): u'Articles',
            ('fr', 'ln'): u'Articles',
            ('de', 'ln'): u'Artikel',
            ('es', 'ln'): u'Articulos',
            ('ca', 'ln'): u'Articles',
            ('pl', 'ln'): u'Artykuły',
            ('pt', 'ln'): u'Artigos',
            ('it', 'ln'): u'Articoli',
            ('ru', 'ln'): u'Статьи',
            ('sk', 'ln'): u'Články',
            ('cs', 'ln'): u'Články',
            ('no', 'ln'): u'Artikler',
            ('sv', 'ln'): u'',
            ('el', 'ln'): u"Άρθρα",
            ('uk', 'ln'): u'Статті',
            ('ja', 'ln'): u'記事',
            ('bg', 'ln'): u'Статии',
            ('hr', 'ln'): u'Članci',
            ('zh_CN', 'ln'): u'文章',
            ('zh_TW', 'ln'): u'文章',
            ('hu', 'ln'): u'Cikkek',
            ('af', 'ln'): u'Artikels',
            ('gl', 'ln'): u'Artigos',
            ('ro', 'ln'): u'Articole',
            ('rw', 'ln'): u'Ikinyamakuru ky\'ubushakashatsi',
            ('ka', 'ln'): u'სტატიები',
            ('lt', 'ln'): u'Straipsniai',
            ('ar', 'ln'): u'مقالات',
        }

    class pictures(siteCollection):
        id = 8
        name = 'Pictures'
        dbquery = '980:"PICTURE"'
        names = {
            ('en', 'ln'): u'Pictures',
            ('fr', 'ln'): u'Photos',
            ('de', 'ln'): u'Fotos',
            ('es', 'ln'): u'Imagenes',
            ('ca', 'ln'): u'Imatges',
            ('pl', 'ln'): u'Obrazy',
            ('pt', 'ln'): u'Fotografias',
            ('it', 'ln'): u'Foto',
            ('ru', 'ln'): u'Фотографии',
            ('sk', 'ln'): u'Fotografie',
            ('cs', 'ln'): u'Fotografie',
            ('no', 'ln'): u'Fotografier',
            ('sv', 'ln'): u'',
            ('el', 'ln'): u'Εικόνες',
            ('uk', 'ln'): u'Зображення',
            ('ja', 'ln'): u'映像',
            ('bg', 'ln'): u'Снимки',
            ('hr', 'ln'): u'Slike',
            ('zh_CN', 'ln'): u'图片',
            ('zh_TW', 'ln'): u'圖片',
            ('hu', 'ln'): u'Képek',
            ('af', 'ln'): u'Prente',
            ('gl', 'ln'): u'Imaxes',
            ('ro', 'ln'): u'Poze',
            ('rw', 'ln'): u'Ifoto',
            ('ka', 'ln'): u'სურათები',
            ('lt', 'ln'): u'Paveikslėliai',
            ('ar', 'ln'): u'صور',
        }

    class CERNDivisions(siteCollection):
        id = 9
        name = 'CERN Divisions'
        dbquery = None
        names = {
            ('en', 'ln'): u'CERN Divisions',
            ('fr', 'ln'): u'Divisions du CERN',
            ('de', 'ln'): u'Abteilungen des CERN',
            ('es', 'ln'): u'Divisiones del CERN',
            ('ca', 'ln'): u'Divisions del CERN',
            ('pl', 'ln'): u'Działy CERN',
            ('pt', 'ln'): u'Divisões do CERN',
            ('it', 'ln'): u'Divisioni del CERN',
            ('ru', 'ln'): u'Разделения CERNа',
            ('sk', 'ln'): u'Oddelenia CERNu',
            ('cs', 'ln'): u'Oddělení CERNu',
            ('no', 'ln'): u'Divisjoner ved CERN',
            ('sv', 'ln'): u'',
            ('el', 'ln'): u'Τομείς του CERN',
            ('uk', 'ln'): u'Підрозділи CERN',
            ('ja', 'ln'): u'CERN 部',
            ('bg', 'ln'): u'Отдели в CERN',
            ('hr', 'ln'): u'Odjeli CERN-a',
            ('zh_CN', 'ln'): u'CERN 分类',
            ('zh_TW', 'ln'): u'CERN 分類',
            ('hu', 'ln'): u'CERN részlegek',
            ('af', 'ln'): u'CERN Afdelings',
        }

    class CERNExperiments(siteCollection):
        id = 10
        name = 'CERN Experiments'
        dbquery = None
        names = {
            ('gl', 'ln'): u'Divisións do CERN',
            ('ro', 'ln'): u'Divizii CERN',
            ('rw', 'ln'): u'Ishami ya CERN',
            ('ka', 'ln'): u'ცერნის განყოფილებები',
            ('lt', 'ln'): u'CERN Padaliniai',
            ('ar', 'ln'): u'أقسام المنظمة الأوربية للبحوث النووية',
            ('en', 'ln'): u'CERN Experiments',
            ('fr', 'ln'): u'Expériences du CERN',
            ('de', 'ln'): u'Experimente des CERN',
            ('es', 'ln'): u'Experimentos del CERN',
            ('ca', 'ln'): u'Experiments del CERN',
            ('pl', 'ln'): u'Eksperymenty CERN',
            ('pt', 'ln'): u'Experimentos do CERN',
            ('it', 'ln'): u'Esperimenti del CERN',
            ('ru', 'ln'): u'Эксперименты CERNа',
            ('sk', 'ln'): u'Experimenty CERNu',
            ('cs', 'ln'): u'Experimenty CERNu',
            ('no', 'ln'): u'Eksperimenter ved CERN',
            ('sv', 'ln'): u'',
            ('el', 'ln'): u'Πειράματα του CERN',
            ('uk', 'ln'): u'Експерименти CERN',
            ('ja', 'ln'): u'CERN の実験',
            ('bg', 'ln'): u'Експерименти в CERN',
            ('hr', 'ln'): u'Eksperimenti CERN-a',
            ('zh_CN', 'ln'): u'CERN 实验',
            ('zh_TW', 'ln'): u'CERN 實驗',
            ('hu', 'ln'): u'CERN kísérletek',
            ('af', 'ln'): u'CERN Experimente',
            ('gl', 'ln'): u'Experimentos do CERN',
            ('ro', 'ln'): u'Experimente CERN',
            ('rw', 'ln'): u'Ubushakashatsi bwa CERN',
            ('ka', 'ln'): u'ცერნის ექსპერემენტები',
            ('lt', 'ln'): u'CERN Eksperimentai',
            ('ar', 'ln'): u'تجارب المنظمة الأوربية للبحوث النووية',
        }

    class theoreticalPhysics(siteCollection):
        id = 11
        name = 'Theoretical Physics (TH)'
        dbquery = 'division:TH'
        names = {
            ('en', 'ln'): u'Theoretical Physics (TH)',
            ('fr', 'ln'): u'Physique Théorique (TH)',
            ('de', 'ln'): u'Theoretische Physik (TH)',
            ('es', 'ln'): u'Física teórica (TH)',
            ('ca', 'ln'): u'Física teòrica (TH)',
            ('pl', 'ln'): u'Fizyka Teoretyczna (TH)',
            ('pt', 'ln'): u'Física Teórica (TH)',
            ('it', 'ln'): u'Fisica Teorica (TH)',
            ('ru', 'ln'): u'Теоретическая физика (TH)',
            ('sk', 'ln'): u'Teoretická fyzika (TH)',
            ('cs', 'ln'): u'Teoretická fyzika (TH)',
            ('no', 'ln'): u'Teoretisk fysikk (TH)',
            ('sv', 'ln'): u'',
            ('el', 'ln'): u'Θεωρητική Φυσική (TH)',
            ('uk', 'ln'): u'Теоретична фізика (TH)',
            ('ja', 'ln'): u'理論的な物理学 (TH)',
            ('bg', 'ln'): u'Теоретична физика (TH)',
            ('hr', 'ln'): u'Teorijska fizika (TH)',
            ('zh_CN', 'ln'): u'理论物理 (TH)',
            ('zh_TW', 'ln'): u'理論物理 (TH)',
            ('hu', 'ln'): u'Elméleti fizika (TH)',
            ('af', 'ln'): u'Teoretiese Fisika (TH)',
            ('gl', 'ln'): u'Física Teórica (TH)',
            ('ro', 'ln'): u'Fizică Teoretică (TH)',
            ('rw', 'ln'): u'Theoretical Physics (TH)',
            ('ka', 'ln'): u'თეორიული ფიზიკა (თფ)',
            ('lt', 'ln'): u'Teorinė fizika (TH)',
            ('ar', 'ln'): u'الفيزياء النظرية',
        }

    class experimentalPhysics(siteCollection):
        id = 12
        name = 'Experimental Physics (EP)'
        dbquery = 'division:EP'
        names = {
            ('en', 'ln'): u'Experimental Physics (EP)',
            ('fr', 'ln'): u'Physique Expérimentale (EP)',
            ('de', 'ln'): u'Experimentelle Physik (EP)',
            ('es', 'ln'): u'Física experimental (FE)',
            ('ca', 'ln'): u'Física experimental (EP)',
            ('pl', 'ln'): u'Fizyka Doświadczalna (EP)',
            ('pt', 'ln'): u'Física Experimental (EP)',
            ('it', 'ln'): u'Fisica Sperimentale (EP)',
            ('ru', 'ln'): u'Экспериментальная Физика (EP)',
            ('sk', 'ln'): u'Experimentálna fyzika (EP)',
            ('cs', 'ln'): u'Experimentální fyzika (EP)',
            ('no', 'ln'): u'Eksperimentell fysikk (EP)',
            ('sv', 'ln'): u'',
            ('el', 'ln'): u'Πειραματική Φυσική (EP)',
            ('uk', 'ln'): u'Експериментальна фізика (EP)',
            ('ja', 'ln'): u'実験物理学 (EP)',
            ('bg', 'ln'): u'Експериментална физика (EP)',
            ('hr', 'ln'): u'Eksperimentalna fizika (EP)',
            ('zh_CN', 'ln'): u'实验物理 (EP)',
            ('zh_TW', 'ln'): u'實驗物理 (EP)',
            ('hu', 'ln'): u'Kísérleti fizika (EP)',
            ('af', 'ln'): u'Eksperimentele Fisika (EP)',
            ('gl', 'ln'): u'Física Experimental (EP)',
            ('ro', 'ln'): u'Fizică Experimentală (EP)',
            ('rw', 'ln'): u'Experimental Physics (EP)',
            ('ka', 'ln'): u'ექსპერიმენტული ფიზიკა (ეფ)',
            ('lt', 'ln'): u'Eksperimentinė fizika (EP)',
            ('ar', 'ln'): u'الفيزياء التجريبية',
        }

    class ISOLDE(siteCollection):
        id = 13
        name = 'ISOLDE'
        dbquery = 'experiment:ISOLDE'
        names = {
            ('en', 'ln'): u'ISOLDE',
            ('fr', 'ln'): u'ISOLDE',
            ('de', 'ln'): u'ISOLDE',
            ('es', 'ln'): u'ISOLDE',
            ('ca', 'ln'): u'ISOLDE',
            ('pl', 'ln'): u'ISOLDE',
            ('pt', 'ln'): u'ISOLDE',
            ('it', 'ln'): u'ISOLDE',
            ('ru', 'ln'): u'ISOLDE',
            ('sk', 'ln'): u'ISOLDE',
            ('cs', 'ln'): u'ISOLDE',
            ('no', 'ln'): u'ISOLDE',
            ('sv', 'ln'): u'ISOLDE',
            ('el', 'ln'): u'ISOLDE',
            ('uk', 'ln'): u'ISOLDE',
            ('ja', 'ln'): u'ISOLDE',
            ('bg', 'ln'): u'ISOLDE',
            ('hr', 'ln'): u'ISOLDE',
            ('zh_CN', 'ln'): u'ISOLDE',
            ('zh_TW', 'ln'): u'ISOLDE',
            ('hu', 'ln'): u'ISOLDE',
            ('af', 'ln'): u'ISOLDE',
            ('gl', 'ln'): u'ISOLDE',
            ('ro', 'ln'): u'ISOLDE',
            ('rw', 'ln'): u'ISOLDE',
            ('ka', 'ln'): u'ISOLDE',
            ('lt', 'ln'): u'ISOLDE',
            ('ar', 'ln'): u'ISOLDE',
        }

    class ALEPH(siteCollection):
        id = 14
        name = 'ALEPH'
        dbquery = 'experiment:ALEPH'
        names = {
            ('en', 'ln'): u'ALEPH',
            ('fr', 'ln'): u'ALEPH',
            ('de', 'ln'): u'ALEPH',
            ('es', 'ln'): u'ALEPH',
            ('ca', 'ln'): u'ALEPH',
            ('pl', 'ln'): u'ALEPH',
            ('pt', 'ln'): u'ALEPH',
            ('it', 'ln'): u'ALEPH',
            ('ru', 'ln'): u'ALEPH',
            ('sk', 'ln'): u'ALEPH',
            ('cs', 'ln'): u'ALEPH',
            ('no', 'ln'): u'ALEPH',
            ('sv', 'ln'): u'ALEPH',
            ('el', 'ln'): u'ALEPH',
            ('uk', 'ln'): u'ALEPH',
            ('ja', 'ln'): u'ALEPH',
            ('bg', 'ln'): u'ALEPH',
            ('hr', 'ln'): u'ALEPH',
            ('zh_CN', 'ln'): u'ALEPH',
            ('zh_TW', 'ln'): u'ALEPH',
            ('hu', 'ln'): u'ALEPH',
            ('af', 'ln'): u'ALEPH',
            ('gl', 'ln'): u'ALEPH',
            ('ro', 'ln'): u'ALEPH',
            ('rw', 'ln'): u'ALEPH',
            ('ka', 'ln'): u'ALEPH',
            ('lt', 'ln'): u'ALEPH',
            ('ar', 'ln'): u'ALEPH',
        }

    class articlesPreprints(preprints):
        id = 15
        name = 'Articles & Preprints'
        dbquery = None
        names = {
            ('en', 'ln'): u'Articles & Preprints',
            ('fr', 'ln'): u'Articles et Prétirages',
            ('de', 'ln'): u'Artikel & Preprints',
            ('es', 'ln'): u'Articulos y preprints',
            ('ca', 'ln'): u'Articles i preprints',
            ('pl', 'ln'): u'Artykuły i Preprinty',
            ('pt', 'ln'): u'Artigos e Preprints',
            ('it', 'ln'): u'Articoli e Preprint',
            ('ru', 'ln'): u'Статьи и Препринты',
            ('sk', 'ln'): u'Články a Preprinty',
            ('cs', 'ln'): u'Články a Preprinty',
            ('no', 'ln'): u'Artikler og Førtrykk',
            ('sv', 'ln'): u'',
            ('el', 'ln'): u"Άρθρα & Προδημοσιεύσεις",
            ('uk', 'ln'): u'Статті та Препринти',
            ('ja', 'ln'): u'記事及びプレプリント',
            ('bg', 'ln'): u'Статии и Препринти',
            ('hr', 'ln'): u'Članci i Preprinti',
            ('zh_CN', 'ln'): u'文章和预印',
            ('zh_TW', 'ln'): u'文章和預印',
            ('hu', 'ln'): u'Cikkek és Preprintek',
            ('af', 'ln'): u'Artikels & Pre-drukke',
            ('gl', 'ln'): u'Artigos e Preprints',
            ('ro', 'ln'): u'Articole şi Preprinturi',
            ('rw', 'ln'): u'Ibinyamakuru',
            ('ka', 'ln'): u'სტატიები და პრეპრინტები',
            ('lt', 'ln'): u'Straipsniai ir Rankraščiai',
            ('ar', 'ln'): u'مقالات & مسودات',
        }

    class booksReports(siteCollection):
        id = 16
        name = 'Books & Reports'
        dbquery = None
        names = {
            ('en', 'ln'): u'Books & Reports',
            ('fr', 'ln'): u'Livres et Rapports',
            ('de', 'ln'): u'Monographien & Reports',
            ('es', 'ln'): u'Libros e informes',
            ('ca', 'ln'): u'Llibres i informes',
            ('pl', 'ln'): u'Książki i Raporty',
            ('pt', 'ln'): u'Livros e Relatórios',
            ('it', 'ln'): u'Libri e Rapporti',
            ('ru', 'ln'): u'Книги и Рапорты',
            ('sk', 'ln'): u'Knihy a Správy',
            ('cs', 'ln'): u'Knihy a Zprávy',
            ('no', 'ln'): u'Bøker og Rapporter',
            ('sv', 'ln'): u'',
            ('el', 'ln'): u'Βιβλία & Αναφορές',
            ('uk', 'ln'): u'Книги та Звіти',
            ('ja', 'ln'): u'本及びレポート',
            ('bg', 'ln'): u'Книги и Доклади',
            ('hr', 'ln'): u'Knjige i Izvještaji',
            ('zh_CN', 'ln'): u'书本和报告',
            ('zh_TW', 'ln'): u'書本和報告',
            ('hu', 'ln'): u'Könyvek és tanulmányok',
            ('af', 'ln'): u'Boeke & Verslae',
            ('gl', 'ln'): u'Libros e Informes',
            ('ro', 'ln'): u'Cărţi şi Rapoarte',
            ('rw', 'ln'): u'Ibitabo & Raporo',
            ('ka', 'ln'): u'წიგნები და მოხსენებები',
            ('lt', 'ln'): u'Knygos ir Pranešimai',
            ('ar', 'ln'): u'كتب & تقارير',
        }

    class multimediaArts(siteCollection):
        id = 17
        name = 'Multimedia & Arts'
        dbquery = None
        names = {
            ('en', 'ln'): u'Multimedia & Arts',
            ('fr', 'ln'): u'Multimédia et Arts',
            ('de', 'ln'): u'Multimedia & Kunst',
            ('es', 'ln'): u'Multimedia y artes',
            ('ca', 'ln'): u'Multimèdia i arts',
            ('pl', 'ln'): u'Multimedia i Sztuka',
            ('pt', 'ln'): u'Multimédia e Artes',
            ('it', 'ln'): u'Multimedia e Arti',
            ('ru', 'ln'): u'Мультимедиа и Исскуство',
            ('sk', 'ln'): u'Multimédia a Umenie',
            ('cs', 'ln'): u'Multimédia a Umění',
            ('no', 'ln'): u'Multimedia og Grafikk',
            ('sv', 'ln'): u'',
            ('el', 'ln'): u'Πολυμέσα & Τέχνες',
            ('uk', 'ln'): u'Мультимедіа та Мистецтво',
            ('ja', 'ln'): u'マルチメディア及び芸術',
            ('bg', 'ln'): u'Мултимедия и Изкуства',
            ('hr', 'ln'): u'Multimedija i Umjetnost',
            ('zh_CN', 'ln'): u'多媒体和艺术',
            ('zh_TW', 'ln'): u'多媒體和藝術',
            ('hu', 'ln'): u'Multimédia és képzőművészet',
            ('af', 'ln'): u'Multimedia & Kunste',
            ('gl', 'ln'): u'Multimedia e Arte',
            ('ro', 'ln'): u'Multimedia şi Arte',
            ('rw', 'ln'): u'Multimedia & Arts',
            ('ka', 'ln'): u'მულტიმედია და ხელოვნება',
            ('lt', 'ln'): u'Multimedija ir Menas',
            ('ar', 'ln'): u'وسائط متعددة & فنون',
        }

    class poetry(siteCollection):
        id = 18
        name = 'Poetry'
        dbquery = '980:"POETRY"'
        names = {
            ('en', 'ln'): u'Poetry',
            ('fr', 'ln'): u'Poésie',
            ('de', 'ln'): u'Poesie',
            ('es', 'ln'): u'Poesía',
            ('ca', 'ln'): u'Poesia',
            ('pl', 'ln'): u'Poezja',
            ('pt', 'ln'): u'Poesia',
            ('it', 'ln'): u'Poesia',
            ('ru', 'ln'): u'Поэзия',
            ('sk', 'ln'): u'Poézia',
            ('cs', 'ln'): u'Poezie',
            ('no', 'ln'): u'Poesi',
            ('sv', 'ln'): u'',
            ('el', 'ln'): u'Ποίηση',
            ('uk', 'ln'): u'Поезія',
            ('ja', 'ln'): u'詩歌',
            ('bg', 'ln'): u'Поезия',
            ('hr', 'ln'): u'Poezija',
            ('zh_CN', 'ln'): u'诗歌',
            ('zh_TW', 'ln'): u'詩歌',
            ('hu', 'ln'): u'Költészet',
            ('af', 'ln'): u'Poësie',
            ('gl', 'ln'): u'Poesía',
            ('ro', 'ln'): u'Poezie',
            ('rw', 'ln'): u'Umuvugo',
            ('ka', 'ln'): u'პოეზია',
            ('lt', 'ln'): u'Poezija',
            ('ar', 'ln'): u'شعر',
        }

    class atlantisTimesNews:
        id = 19
        name = 'Atlantis Times News'
        dbquery = '980:"ATLANTISTIMESNEWS"'
        names = {
            ('en', 'ln'): u'Atlantis Times News',
            ('fr', 'ln'): u'Atlantis Times Actualités',
        }

    class atlantisTimesArts:
        id = 20
        name = 'Atlantis Times Arts'
        dbquery = '980:"ATLANTISTIMESARTS"'
        names = {
            ('en', 'ln'): u'Atlantis Times Arts',
            ('fr', 'ln'): u'Atlantis Times Arts',
        }

    class atlantisTimesScience:
        id = 21
        name = 'Atlantis Times Science'
        dbquery = '980:"ATLANTISTIMESSCIENCE"'
        names = {
            ('en', 'ln'): u'Atlantis Times Science',
            ('fr', 'ln'): u'Atlantis Times Science',
        }

    class atlantisTimes:
        id = 22
        name = 'Atlantis Times'
        dbquery = None
        names = {
            ('en', 'ln'): u'Atlantis Times',
            ('fr', 'ln'): u'Atlantis Times',
        }

    class atlantisInstituteBooks:
        id = 23
        name = 'Atlantis Institute Books'
        dbquery = 'hostedcollection:'
        names = {
            ('en', 'ln'): u'Atlantis Institute Books',
            ('fr', 'ln'): u'Atlantis Institute Books',
        }

    class atlantisInstituteArticles:
        id = 24
        name = 'Atlantis Institute Articles'
        dbquery = 'hostedcollection:'
        names = {
            ('en', 'ln'): u'Atlantis Institute Articles',
            ('fr', 'ln'): u'Atlantis Institute Articles',
        }

    class atlantisTimesDrafts:
        id = 25
        name = 'Atlantis Times Drafts'
        dbquery = '980:"ATLANTISTIMESSCIENCEDRAFT" or 980:"ATLANTISTIMESARTSDRAFT" or 980:"ATLANTISTIMESNEWSDRAFT"'
        names = {
            ('en', 'ln'): u'Atlantis Times Drafts',
            ('fr', 'ln'): u'Atlantis Times Ébauches',
        }

    class notes:
        id = 26
        dbquery = u'980:"NOTE"'
        names = {
            ('en', 'ln'): u'Notes',
        }
        name = u'Notes'

    class ALEPHPapers:
        id = 27
        dbquery = u'980:"ALEPHPAPER"'
        names = {
            ('en', 'ln'): u'ALEPH Papers',
        }
        name = u'ALEPH Papers'

    class ALEPHInternalNotes:
        id = 28
        dbquery = u'980:"ALEPHNOTE"'
        names = {
            ('en', 'ln'): u'ALEPH Internal Notes',
        }
        name = u'ALEPH Internal Notes'

    class ALEPHTheses:
        id = 29
        dbquery = u'980:"ALEPHTHESIS"'
        names = {
            ('en', 'ln'): u'ALEPH Theses',
        }
        name = u'ALEPH Theses'

    class ISOLDEPapers:
        id = 30
        dbquery = u'980:"ISOLDEPAPER"'
        names = {
            ('en', 'ln'): u'ISOLDE Papers',
        }
        name = u'ISOLDE Papers'

    class ISOLDEInternalNotes:
        id = 31
        dbquery = u'980:"ISOLDENOTE"'
        names = {
            ('en', 'ln'): u'ISOLDE Internal Notes',
        }
        name = u'ISOLDE Internal Notes'

    class drafts:
        id = 32
        dbquery = u'980:"DRAFT"'
        names = {
            ('en', 'ln'): u'Drafts',
        }
        name = u'Drafts'

    class videos:
        id = 33
        dbquery = u'980:"VIDEO"'
        names = {
            ('en', 'ln'): u'Videos',
            ('fr', 'ln'): u'Vidéos',
            ('it', 'ln'): u'Filmati',
        }
        name = u'Videos'

    class Collection_34:
        id = 34
        dbquery = u'collection:AUTHORITY'
        names = {
            ('en','ln'): u'Authority Records',
            ('fr','ln'): u'Notices d\'autorité',
            ('pl','ln'): u'Rekordy kontrolne',
        }
        name = u'Authority Records'

    class Collection_35:
        id = 35
        dbquery = u'collection:AUTHOR'
        names = {
            ('en','ln'): u'Authors',
            ('fr','ln'): u'Auteurs',
            ('pl','ln'): u'Autorzy',
        }
        name = u'Authority Author'

    class Collection_36:
        id = 36
        dbquery = u'collection:INSTITUTION'
        names = {
            ('en','ln'): u'Institutions',
            ('fr','ln'): u'Institutions',
            ('pl','ln'): u'Instytucje',
        }
        name = u'Authority Institution'

    class Collection_37:
        id = 37
        dbquery = u'collection:JOURNAL'
        names = {
            ('en','ln'): u'Journals',
            ('fr','ln'): u'Journals',
            ('pl','ln'): u'Czasopisma',
        }
        name = u'Authority Journal'

    class Collection_38:
        id = 38
        dbquery = u'collection:SUBJECT'
        names = {
            ('en','ln'): u'Subjects',
            ('fr','ln'): u'Sujets',
            ('pl','ln'): u'Tematy',
        }
        name = u'Authority Subject'

    class CMS(siteCollection):
        id = 39
        name = u'CMS'
        dbquery = '980:"CMS"'
        names = {
            ('en', 'ln'): u'CMS'
            }
        }


class CollectionCollectionData(DataSet):

    class siteCollection_articlesPreprints:
        dad = CollectionData.siteCollection
        son = CollectionData.articlesPreprints
        score = 0
        type = 'r'

    class siteCollection_booksReports:
        dad = CollectionData.siteCollection
        son = CollectionData.booksReports
        score = 1
        type = 'r'

    class siteCollection_multimediaArts:
        dad = CollectionData.siteCollection
        son = CollectionData.multimediaArts
        score = 2
        type = 'r'

    class siteCollection_CERNDivisions:
        dad = CollectionData.siteCollection
        son = CollectionData.CERNDivisions
        score = 0
        type = 'v'

    class siteCollection_CERNExperiments:
        dad = CollectionData.siteCollection
        son = CollectionData.CERNExperiments
        score = 1
        type = 'v'

    class CERNExperiments_ISOLDE:
        dad = CollectionData.CERNExperiments
        son = CollectionData.ISOLDE
        score = 0
        type = 'r'

    class CERNExperiments_ALEPH:
        dad = CollectionData.CERNExperiments
        son = CollectionData.ALEPH
        score = 1
        type = 'r'

    class articlesPreprints_preprints:
        dad = CollectionData.articlesPreprints
        son = CollectionData.preprints
        score = 0
        type = 'r'

    class articlesPreprints_articles:
        dad = CollectionData.articlesPreprints
        son = CollectionData.articles
        score = 1
        type = 'r'

    class booksReports_books:
        dad = CollectionData.booksReports
        son = CollectionData.books
        score = 0
        type = 'r'

    class booksReports_theses:
        dad = CollectionData.booksReports
        son = CollectionData.theses
        score = 1
        type = 'r'

    class booksReports_reports:
        dad = CollectionData.booksReports
        son = CollectionData.reports
        score = 2
        type = 'r'

    class multimediaArts_pictures:
        dad = CollectionData.multimediaArts
        son = CollectionData.pictures
        score = 0
        type = 'r'

    class multimediaArts_poetry:
        dad = CollectionData.multimediaArts
        son = CollectionData.poetry
        score = 1
        type = 'r'

    class multimediaArts_videos:
        dad = CollectionData.multimediaArts
        son = CollectionData.videos
        score = 2
        type = 'r'

    class multimediaArts_atlantisTimes:
        dad = CollectionData.multimediaArts
        son = CollectionData.atlantisTimes
        score = 2
        type = 'r'

    class atlantisTimes_atlantisTimesNews:
        dad = CollectionData.atlantisTimes
        son = CollectionData.atlantisTimesNews
        score = 0
        type = 'r'

    class atlantisTimes_atlantisTimesArts:
        dad = CollectionData.atlantisTimes
        son = CollectionData.atlantisTimesArts
        score = 1
        type = 'r'

    class atlantisTimes_atlantisTimesScience:
        dad = CollectionData.atlantisTimes
        son = CollectionData.atlantisTimesScience
        score = 2
        type = 'r'

    class CERNDivisions_theoreticalPhysics:
        dad = CollectionData.CERNDivisions
        son = CollectionData.theoreticalPhysics
        score = 0
        type = 'r'

    class CERNDivisions_experimentalPhysics:
        dad = CollectionData.CERNDivisions
        son = CollectionData.experimentalPhysics
        score = 1
        type = 'r'


class CollectiondetailedrecordpagetabsData(DataSet):

    class Collectiondetailedrecordpagetabs_8:
        tabs = u'usage;comments;metadata'
        id_collection = CollectionData.pictures.ref('id')

    class Collectiondetailedrecordpagetabs_17:
        tabs = u'usage;comments;metadata'
        id_collection = CollectionData.multimediaArts.ref('id')

    class Collectiondetailedrecordpagetabs_18:
        tabs = u'usage;comments;metadata'
        id_collection = CollectionData.poetry.ref('id')

    class Collectiondetailedrecordpagetabs_19:
        tabs = u'usage;comments;metadata'
        id_collection = CollectionData.atlantisTimesNews.ref('id')

    class Collectiondetailedrecordpagetabs_33:
        tabs = u''
        id_collection = CollectionData.videos.ref('id')


class PortalboxData(DataSet):

    class Portalbox_1:
        body = u'Welcome to the demo site of the Invenio, a free document server software coming from CERN.  Please feel free to explore all the features of this demo site to the full.'
        id = 1
        title = u'ABOUT THIS SITE'

    class Portalbox_2:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 2
        title = u'SEE ALSO'

    class Portalbox_3:
        body = u'The Articles collection contains all the papers published in scientific journals by our staff.  The collection starts from 1998.'
        id = 3
        title = u'ABOUT ARTICLES'

    class Portalbox_4:
        body = u'<a href="http://arXiv.org/">arXiv.org</a><br /><a href="http://cds.cern.ch/">CDS</a><br /><a href="www.chemweb.com">ChemWeb</a><br /><a href="http://www.ams.org/mathscinet">MathSciNet</a>'
        id = 4
        title = u'SEE ALSO'

    class Portalbox_5:
        body = u'The Preprints collection contains not-yet-published papers and research results obtained at the institute.  The collection starts from 2001.'
        id = 5
        title = u'ABOUT PREPRINTS'

    class Portalbox_6:
        body = u'<a href="http://arXiv.org/">arXiv.org</a><br /><a href="http://cds.cern.ch/">CDS</a>'
        id = 6
        title = u'SEE ALSO'

    class Portalbox_7:
        body = u'The Books collection contains monographs published by institute staff as well as pointers to interesting online e-books available in fulltext.'
        id = 7
        title = u'ABOUT BOOKS'

    class Portalbox_8:
        body = u'<a href="http://etext.lib.virginia.edu/ebooks/ebooklist.html">UV e-Books</a><br /><a href="http://www.gutenberg.org/">Project Gutenberg</a>'
        id = 8
        title = u'SEE ALSO'

    class Portalbox_9:
        body = u"The Theses collection contains all students' theses defended at the institute.  The collection starts from 1950."
        id = 9
        title = u'ABOUT THESES'

    class Portalbox_10:
        body = u'<a href="http://www.theses.org/">NDLTD Theses</a><br /><a href="http://www.thesis.de/">Thesis.DE</a>'
        id = 10
        title = u'SEE ALSO'

    class Portalbox_11:
        body = u'The Reports collection contains miscellaneous technical reports, unpublished elsewhere.  The collection starts from 1950.'
        id = 11
        title = u'ABOUT REPORTS'

    class Portalbox_12:
        body = u'this is a test portal box'
        id = 12
        title = u'TEST portal box'

    class Portalbox_13:
        body = u'this is a test portal box'
        id = 13
        title = u'test'

    class Portalbox_14:
        body = u'The Pictures collection contains selected photographs and illustrations.  Please note that photographs are copyrighted.  The collection includes historical archive that starts from 1950.'
        id = 14
        title = u'ABOUT PICTURES'

    class Portalbox_15:
        body = u'These virtual collections present a specific point of view on the database content from CERN Divisions persective.'
        id = 15
        title = u'ABOUT CERN DIVISIONS'

    class Portalbox_16:
        body = u'These virtual collections present a specific point of view on the database content from CERN Experiments persective.'
        id = 16
        title = u'ABOUT CERN EXPERIMENTS'

    class Portalbox_17:
        body = u'This virtual collection groups together all the documents written by authors from CERN TH Division.'
        id = 17
        title = u'ABOUT TH'

    class Portalbox_18:
        body = u'This virtual collection groups together all the documents written by authors from CERN EP Division.'
        id = 18
        title = u'ABOUT EP'

    class Portalbox_19:
        body = u'This virtual collection groups together all the documents about ISOLDE CERN experiment.'
        id = 19
        title = u'ABOUT ISOLDE'

    class Portalbox_20:
        body = u'This virtual collection groups together all the documents about ALEPH CERN experiment.'
        id = 20
        title = u'ABOUT ALEPH'

    class Portalbox_21:
        body = u'This collection groups together all published and non-published articles, many of which in electronic fulltext form.'
        id = 21
        title = u'ABOUT ARTICLES AND PREPRINTS'

    class Portalbox_22:
        body = u'This collection groups together all monograph-like publications, be they books, theses, reports, book chapters, proceedings, and so on.'
        id = 22
        title = u'ABOUT BOOKS AND REPORTS'

    class Portalbox_23:
        body = u'This collection groups together all multimedia- and outreach- oriented material.'
        id = 23
        title = u'ABOUT MULTIMEDIA & OUTREACH'

    class Portalbox_24:
        body = u'This collection presents poetry excerpts, mainly to demonstrate and test the treatment of various languages.<p>Vitrum edere possum; mihi non nocet.<br />\u039c\u03c0\u03bf\u03c1\u03ce \u03bd\u03b1 \u03c6\u03ac\u03c9 \u03c3\u03c0\u03b1\u03c3\u03bc\u03ad\u03bd\u03b1 \u03b3\u03c5\u03b1\u03bb\u03b9\u03ac \u03c7\u03c9\u03c1\u03af\u03c2 \u03bd\u03b1 \u03c0\u03ac\u03b8\u03c9 \u03c4\u03af\u03c0\u03bf\u03c4\u03b1.<br />P\xf2di manjar de veire, me nafrari\xe1 pas.<br />\xc9g get eti\xf0 gler \xe1n \xfeess a\xf0 mei\xf0a mig.<br />Ic m\xe6g gl\xe6s eotan ond hit ne hearmia\xf0 me.<br />\u16c1\u16b3\u16eb\u16d7\u16a8\u16b7\u16eb\u16b7\u16da\u16a8\u16cb\u16eb\u16d6\u16a9\u16cf\u16aa\u16be\u16eb\u16a9\u16be\u16de\u16eb\u16bb\u16c1\u16cf\u16eb\u16be\u16d6\u16eb\u16bb\u16d6\u16aa\u16b1\u16d7\u16c1\u16aa\u16a7\u16eb\u16d7\u16d6\u16ec<br />\u280a\u2800\u2809\u2801\u281d\u2800\u2811\u2801\u281e\u2800\u281b\u2807\u2801\u280e\u280e\u2800\u2801\u281d\u2819\u2800\u280a\u281e\u2800\u2819\u2815\u2811\u280e\u281d\u281e\u2800\u2813\u2825\u2817\u281e\u2800\u280d\u2811<br />Pot s\u0103 m\u0103n\xe2nc sticl\u0103 \u0219i ea nu m\u0103 r\u0103ne\u0219te.<br />Meg tudom enni az \xfcveget, nem lesz t\u0151le bajom.<br />M\xf4\u017eem jes\u0165 sklo. Nezran\xed ma.<br /><span dir="rtl" lang="he">\u05d0\u05e0\u05d9 \u05d9\u05db\u05d5\u05dc \u05dc\u05d0\u05db\u05d5\u05dc \u05d6\u05db\u05d5\u05db\u05d9\u05ea \u05d5\u05d6\u05d4 \u05dc\u05d0 \u05de\u05d6\u05d9\u05e7 \u05dc\u05d9.</span><br /><span dir="rtl" lang="ji">\u05d0\u05d9\u05da \u05e7\u05e2\u05df \u05e2\u05e1\u05df \u05d2\u05dc\u05d0\u05b8\u05d6 \u05d0\u05d5\u05df \u05e2\u05e1 \u05d8\u05d5\u05d8 \u05de\u05d9\u05e8 \u05e0\u05d9\u05e9\u05d8 \u05f0\u05f2.</span><br /><span dir="RTL" lang=AR>\u0623\u0646\u0627 \u0642\u0627\u062f\u0631 \u0639\u0644\u0649 \u0623\u0643\u0644 \u0627\u0644\u0632\u062c\u0627\u062c \u0648 \u0647\u0630\u0627 \u0644\u0627 \u064a\u0624\u0644\u0645\u0646\u064a.</span><br />\u042f \u043c\u043e\u0433\u0443 \u0435\u0441\u0442\u044c \u0441\u0442\u0435\u043a\u043b\u043e, \u043e\u043d\u043e \u043c\u043d\u0435 \u043d\u0435 \u0432\u0440\u0435\u0434\u0438\u0442.<br />\u10db\u10d8\u10dc\u10d0\u10e1 \u10d5\u10ed\u10d0\u10db \u10d3\u10d0 \u10d0\u10e0\u10d0 \u10db\u10e2\u10d9\u10d8\u10d5\u10d0.<br />\u053f\u0580\u0576\u0561\u0574 \u0561\u057a\u0561\u056f\u056b \u0578\u0582\u057f\u0565\u056c \u0587 \u056b\u0576\u056e\u056b \u0561\u0576\u0570\u0561\u0576\u0563\u056b\u057d\u057f \u0579\u0568\u0576\u0565\u0580\u0589<br />\u092e\u0948\u0902 \u0915\u093e\u0901\u091a \u0916\u093e \u0938\u0915\u0924\u093e \u0939\u0942\u0901, \u092e\u0941\u091d\u0947 \u0909\u0938 \u0938\u0947 \u0915\u094b\u0908 \u092a\u0940\u0921\u093e \u0928\u0939\u0940\u0902 \u0939\u094b\u0924\u0940.<br />\u0915\u093e\u091a\u0902 \u0936\u0915\u094d\u0928\u094b\u092e\u094d\u092f\u0924\u094d\u0924\u0941\u092e\u094d \u0964 \u0928\u094b\u092a\u0939\u093f\u0928\u0938\u094d\u0924\u093f \u092e\u093e\u092e\u094d \u0965<br />\u0e09\u0e31\u0e19\u0e01\u0e34\u0e19\u0e01\u0e23\u0e30\u0e08\u0e01\u0e44\u0e14\u0e49 \u0e41\u0e15\u0e48\u0e21\u0e31\u0e19\u0e44\u0e21\u0e48\u0e17\u0e33\u0e43\u0e2b\u0e49\u0e09\u0e31\u0e19\u0e40\u0e08\u0e47\u0e1a<br />T\xf4i c\xf3 th\u1ec3 \u0103n th\u1ee7y tinh m\xe0 kh\xf4ng h\u1ea1i g\xec.<br /><span lang="zh">\u6211\u80fd\u541e\u4e0b\u73bb\u7483\u800c\u4e0d\u4f24\u8eab\u4f53\u3002</span><br /><span lang=ja>\u79c1\u306f\u30ac\u30e9\u30b9\u3092\u98df\u3079\u3089\u308c\u307e\u3059\u3002\u305d\u308c\u306f\u79c1\u3092\u50b7\u3064\u3051\u307e\u305b\u3093\u3002</span><br /><span lang=ko>\ub098\ub294 \uc720\ub9ac\ub97c \uba39\uc744 \uc218 \uc788\uc5b4\uc694. \uadf8\ub798\ub3c4 \uc544\ud504\uc9c0 \uc54a\uc544\uc694</span><br />(<a href="http://www.columbia.edu/kermit/utf8.html">http://www.columbia.edu/kermit/utf8.html</a>)'
        id = 24
        title = u'ABOUT POETRY'

    class Portalbox_25:
        body = u'Bienvenue sur le site de d\xe9monstration de Invenio, un logiciel libre pour des serveurs des documents, venant du CERN.  Veuillez explorer les possibilit\xe9s de ce site de d\xe9monstration de tous ses c\xf4t\xe9s.'
        id = 25
        title = u'\xc0 PROPOS DE CE SITE'

    class Portalbox_26:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 26
        title = u'VOIR AUSSI'

    class Portalbox_27:
        body = u'Vitajte na demon\u0161tra\u010dn\xfdch str\xe1nkach Invenio, vo\u013ene dostupn\xe9ho softwaru pre dokumentov\xe9 servery, poch\xe1dzaj\xfaceho z CERNu.  Prehliadnite si mo\u017enosti na\u0161eho demon\u0161tra\u010dn\xe9ho serveru podla \u013eubov\xf4le.'
        id = 27
        title = u'O T\xddCHTO STR\xc1NKACH'

    class Portalbox_28:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 28
        title = u'VI\u010e TIE\u017d'

    class Portalbox_29:
        body = u'V\xedtejte na demonstra\u010dn\xedch str\xe1nk\xe1ch Invenio, voln\u011b dostupn\xe9ho softwaru pro dokumentov\xe9 servery, poch\xe1zej\xedc\xedho z CERNu.  Prohl\xe9dn\u011bte si mo\u017enosti na\u0161eho demonstra\u010dn\xedho serveru podle libosti.'
        id = 29
        title = u'O T\u011aCHTO STR\xc1NK\xc1CH'

    class Portalbox_30:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 30
        title = u'VIZ T\xc9\u017d'

    class Portalbox_31:
        body = u'Willkommen Sie bei der Demo-Seite des Invenio, des Dokument Management Systems Software aus CERN. Hier k\xf6nnen Sie den System gleich und frei ausprobieren.'
        id = 31
        title = u'\xdcBER DIESEN SEITEN'

    class Portalbox_32:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 32
        title = u'SEHEN SIE AUCH'

    class Portalbox_33:
        body = u'Bienvenidos a las p\xe1ginas de demostraci\xf3n de Invenio, un software gratuito desarrollado por el CERN que permite crear un servidor de documentos. Le invitamos a explorar a fondo todas las funcionalidades ofrecidas por estas p\xe1ginas de demostraci\xf3n.'
        id = 33
        title = u'ACERCA DE ESTAS P\xc1GINAS'

    class Portalbox_34:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 34
        title = u'VEA TAMBI\xc9N'

    class Portalbox_35:
        body = u'Benvenuti nel sito demo di Invenio, un software libero per server di documenti sviluppato al CERN. Vi invitiamo ad esplorare a fondo tutte le caratteristiche di questo sito demo.'
        id = 35
        title = u'A PROPOSITO DI QUESTO SITO'

    class Portalbox_36:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 36
        title = u'VEDI ANCHE'

    class Portalbox_37:
        body = u'Velkommen til demosiden for Invenio, en gratis dokumentserver fra CERN. Vennligst f\xf8l deg fri til \xe5 utforske alle mulighetene i denne demoen til det fulle.'
        id = 37
        title = u'OM DENNE SIDEN'

    class Portalbox_38:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 38
        title = u'SE OGS\xc5'

    class Portalbox_39:
        body = u'Bem vindo ao site de demonstra\xe7\xe3o do Invenio, um servidor de documentos livre desenvolvido pelo CERN. Sinta-se \xe0 vontade para explorar plenamente todos os recursos deste site demonstra\xe7\xe3o.'
        id = 39
        title = u'SOBRE ESTE SITE'

    class Portalbox_40:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 40
        title = u'VEJA TAMB\xc9M'

    class Portalbox_41:
        body = u'\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u043d\u0430 \u043d\u0430\u0448 \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0441\u0430\u0439\u0442 Invenio. Invenio -- \u0441\u0432\u043e\u0431\u043e\u0434\u043d\u0430\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u0434\u043b\u044f \u0441\u0435\u0440\u0432\u0435\u0440\u043e\u0432 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432, \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0430\u043d\u043d\u0430\u044f \u0432 CERN\u0435.  \u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430 \u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435\u0441\u044c \u0441\u0432\u043e\u0431\u043e\u0434\u043d\u043e \u044d\u0442\u0438\u043c \u0441\u0430\u0439\u0442\u043e\u043c.'
        id = 41
        title = u'\u041e\u0411 \u042d\u0422\u041e\u041c \u0421\u0410\u0419\u0422\u0415'

    class Portalbox_42:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 42
        title = u'\u0421\u041c\u041e\u0422\u0420\u0418\u0422\u0415 \u0422\u0410\u041a\u0416\u0415'

    class Portalbox_43:
        body = u'V\xe4lkommen till demoinstallationen av Invenio, en fri programvara f\xf6r hantering av dokument, fr\xe5n CERN. V\xe4lkommen att unders\xf6ka alla funktioner i denna installation.'
        id = 43
        title = u'OM DENNA WEBBPLATS'

    class Portalbox_44:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 44
        title = u'SE \xc4VEN'

    class Portalbox_45:
        body = u'<a href="/submit?doctype=TEXT">Submit a new preprint</a>'
        id = 45
        title = u'SUBMIT PREPRINT'

    class Portalbox_46:
        body = u'<a href="/submit?doctype=TEXT">Submit a new book</a>'
        id = 46
        title = u'SUBMIT BOOK'

    class Portalbox_47:
        body = u'<a href="/submit?doctype=TEXT">Submit a new thesis</a>'
        id = 47
        title = u'SUBMIT THESIS'

    class Portalbox_48:
        body = u'<a href="/submit?doctype=TEXT">Submit a new report</a>'
        id = 48
        title = u'SUBMIT REPORT'

    class Portalbox_49:
        body = u'<a href="/submit?doctype=TEXT">Submit a new article</a>'
        id = 49
        title = u'SUBMIT ARTICLE'

    class Portalbox_50:
        body = u'<a href="/submit?doctype=DEMOPIC">Submit a new picture</a>'
        id = 50
        title = u'SUBMIT PICTURE'

    class Portalbox_51:
        body = u'<a href="/submit?doctype=TEXT">Submit a new article</a><br /><a href="/submit?doctype=TEXT">Submit a new preprint</a>'
        id = 51
        title = u'SUBMIT NEW DOCUMENT'

    class Portalbox_52:
        body = u'<a href="/submit?doctype=TEXT">Submit a new book</a><br /><a href="/submit?doctype=TEXT">Submit a new thesis</a><br /><a href="/submit?doctype=TEXT">Submit a new report</a>'
        id = 52
        title = u'SUBMIT NEW DOCUMENT'

    class Portalbox_53:
        body = u'<a href="/submit?doctype=DEMOPIC">Submit a new picture</a>'
        id = 53
        title = u'SUBMIT NEW DOCUMENT'

    class Portalbox_54:
        body = u'\u039a\u03b1\u03bb\u03c9\u03c2 \u03ae\u03bb\u03b8\u03b1\u03c4\u03b5 \u03c3\u03c4\u03bf\u03bd \u03b4\u03b9\u03ba\u03c4\u03c5\u03b1\u03ba\u03cc \u03c4\u03cc\u03c0\u03bf \u03c4\u03bf\u03c5 Invenio, \u03b5\u03bd\u03cc\u03c2 \u03b4\u03c9\u03c1\u03b5\u03ac\u03bd \u03b5\u03be\u03c5\u03c0\u03b7\u03c1\u03b5\u03c4\u03b7\u03c4\u03ae \u03b3\u03b9\u03b1 \u03ad\u03b3\u03b3\u03c1\u03b1\u03c6\u03b1 \u03c0\u03c1\u03bf\u03b5\u03c1\u03c7\u03cc\u03bc\u03b5\u03bd\u03bf \u03b1\u03c0\u03bf \u03c4\u03bf CERN. \u0395\u03af\u03c3\u03c4\u03b5 \u03b5\u03c5\u03c0\u03c1\u03cc\u03c3\u03b4\u03b5\u03ba\u03c4\u03bf\u03b9 \u03bd\u03b1 \u03b5\u03be\u03b5\u03c1\u03b5\u03c5\u03bd\u03ae\u03c3\u03b5\u03c4\u03b5 \u03c3\u03b5 \u03b2\u03ac\u03b8\u03bf\u03c2 \u03c4\u03b9\u03c2 \u03b4\u03c5\u03bd\u03b1\u03c4\u03cc\u03c4\u03b7\u03c4\u03b5\u03c2 \u03c0\u03bf\u03c5 \u03c3\u03b1\u03c2 \u03c0\u03b1\u03c1\u03ad\u03c7\u03b5\u03b9 \u03bf \u03b4\u03b9\u03ba\u03c4\u03c5\u03b1\u03ba\u03cc\u03c2 \u03b1\u03c5\u03c4\u03cc\u03c2 \u03c4\u03cc\u03c0\u03bf\u03c2.'
        id = 54
        title = u'\u03a3\u03a7\u0395\u03a4\u0399\u039a\u0391 \u039c\u0395 \u03a4\u0397\u039d \u03a3\u0395\u039b\u0399\u0394\u0391'

    class Portalbox_55:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 55
        title = u'\u0394\u0395\u0399\u03a4\u0395 \u0395\u03a0\u0399\u03a3\u0397\u03a3'

    class Portalbox_56:
        body = u'\u041b\u0430\u0441\u043a\u0430\u0432\u043e \u043f\u0440\u043e\u0441\u0438\u043c\u043e \u0434\u043e \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0456\u0439\u043d\u043e\u0433\u043e \u0441\u0430\u0439\u0442\u0443 Invenio, \u0432\u0456\u043b\u044c\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043d\u043e\u0433\u043e \u0437\u0430\u0431\u0435\u0437\u043f\u0435\u0447\u0435\u043d\u043d\u044f, \u0440\u043e\u0437\u0440\u043e\u0431\u043b\u0435\u043d\u043e\u0433\u043e CERN. \u0412\u0438\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u0432\u0441\u0456 \u043c\u043e\u0436\u043b\u0438\u0432\u043e\u0441\u0442\u0456 \u0446\u044c\u043e\u0433\u043e \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0456\u0439\u043d\u043e\u0433\u043e \u0441\u0430\u0439\u0442\u0443 \u0432 \u043f\u043e\u0432\u043d\u043e\u043c\u0443 \u043e\u0431\u0441\u044f\u0437\u0456.'
        id = 56
        title = u'\u041f\u0420\u041e \u0426\u0415\u0419 \u0421\u0410\u0419\u0422'

    class Portalbox_57:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 57
        title = u'\u0414\u0418\u0412\u0418\u0421\u042c \u0422\u0410\u041a\u041e\u0416'

    class Portalbox_58:
        body = u'Benvinguts al lloc de demo de Invenio, un servidor de documents lliure originat al CERN. Us convidem a explorar a fons totes les funcionalitats ofertes en aquestes p\xe0gines de demostraci\xf3.'
        id = 58
        title = u'SOBRE AQUEST LLOC'

    class Portalbox_59:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 59
        title = u'VEGEU TAMB\xc9'

    class Portalbox_60:
        body = u'Invenio\u30c7\u30e2\u30f3\u30b9\u30c8\u30ec\u30fc\u30b7\u30e7\u30f3\u306e\u5834\u6240\u3078\u306e\u6b53\u8fce, CERN \u304b\u3089\u6765\u308b\u81ea\u7531\u306a\u6587\u66f8\u306e\u30b5\u30fc\u30d0\u30fc\u30bd\u30d5\u30c8\u30a6\u30a7\u30a2,    \u3053\u306e\u30c7\u30e2\u30f3\u30b9\u30c8\u30ec\u30fc\u30b7\u30e7\u30f3\u306e\u5834\u6240\u306e\u7279\u5fb4\u3059\u3079\u3066\u3092\u63a2\u691c\u3059\u308b\u81ea\u7531\u306e\u611f\u3058'
        id = 60
        title = u'\u3053\u306e\u5834\u6240\u306b\u3064\u3044\u3066'

    class Portalbox_61:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 61
        title = u'\u307e\u305f\u898b\u306a\u3055\u3044'

    class Portalbox_62:
        body = u'Witamy w wersji demo systemu Invenio, darmowego oprogramowania do obs\u0142ugi serwera dokument\xf3w, stworzonego w CERN. Zach\u0119camy do odkrywania wszelkich funkcjonalno\u015bci oferowanych przez t\u0119 stron\u0119.'
        id = 62
        title = u'O TEJ STRONIE'

    class Portalbox_63:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 63
        title = u'ZOBACZ TAK\u017bE'

    class Portalbox_64:
        body = u'\u0414\u043e\u0431\u0440\u0435 \u0434\u043e\u0448\u043b\u0438 \u043d\u0430 \u0434\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u0438\u044f \u0441\u0430\u0439\u0442 \u043d\u0430 Invenio, \u0441\u0432\u043e\u0431\u043e\u0434\u0435\u043d \u0441\u043e\u0444\u0442\u0443\u0435\u0440 \u0437\u0430 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043d\u0438 \u0441\u044a\u0440\u0432\u044a\u0440\u0438 \u0438\u0437\u0440\u0430\u0431\u043e\u0442\u0435\u043d \u0432 \u0426\u0415\u0420\u041d. \u0427\u0443\u0432\u0441\u0442\u0432\u0430\u0439\u0442\u0435 \u0441\u0435 \u0441\u0432\u043e\u0431\u043e\u0434\u043d\u0438 \u0434\u0430 \u0438\u0437\u0441\u043b\u0435\u0434\u0432\u0430\u0442\u0435 \u0432\u0441\u044f\u043a\u0430 \u0435\u0434\u043d\u0430 \u043e\u0442 \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438\u0442\u0435 \u043d\u0430 \u0441\u0430\u0439\u0442\u0430.'
        id = 64
        title = u'\u0417\u0410 \u0421\u0410\u0419\u0422\u0410'

    class Portalbox_65:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 65
        title = u'\u0412\u0418\u0416 \u0421\u042a\u0429\u041e'

    class Portalbox_66:
        body = u'Dobrodo\u0161li na Invenio demo site. Invenio je slobodno dostupan poslu\u017eitelj dokumenata razvijen na CERN-u. Slobodno istra\u017eite sve mogu\u0107nosti ove aplikacije.'
        id = 66
        title = u'O OVOM SITE-u'

    class Portalbox_67:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 67
        title = u'TAKO\u0110ER POGLEDAJTE'

    class Portalbox_68:
        body = u'\u6b22\u8fce\u6765\u5230Invenio \u7684\u793a\u8303\u7f51\u7ad9\uff01Invenio\u662f\u4e00\u4e2a\u7531CERN\u5f00\u53d1\u7684\u514d\u8d39\u6587\u4ef6\u670d\u52a1\u5668\u8f6f\u4ef6\u3002 \u8981\u4e86\u89e3\u8fd9\u7f51\u7ad9\u6240\u63d0\u4f9b\u7684\u5404\u9879\u7279\u70b9, \u8bf7\u7acb\u523b\u884c\u52a8\uff0c\u5c3d\u60c5\u63a2\u7d22\u3002'
        id = 68
        title = u'\u5173\u4e8e\u8fd9\u4e2a\u7f51\u7ad9'

    class Portalbox_69:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 69
        title = u'\u53c2\u89c1'

    class Portalbox_70:
        body = u'\u6b61\u8fce\u4f86\u5230Invenio \u7684\u793a\u7bc4\u7db2\u7ad9\uff01Invenio\u662f\u4e00\u500b\u7531CERN\u958b\u767c\u7684\u514d\u8cbb\u6587\u4ef6\u4f3a\u670d\u5668\u8edf\u9ad4\u3002 \u8981\u77ad\u89e3\u9019\u7db2\u7ad9\u6240\u63d0\u4f9b\u7684\u5404\u9805\u7279\u9ede, \u8acb\u7acb\u523b\u884c\u52d5\uff0c\u76e1\u60c5\u63a2\u7d22\u3002'
        id = 70
        title = u'\u95dc\u65bc\u9019\u500b\u7db2\u7ad9'

    class Portalbox_71:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 71
        title = u'\u53c3\u898b'

    class Portalbox_72:
        body = u'\xdcdv\xf6z\xf6lj\xfck a Invenio bemutat\xf3oldalain! Ezt a szabad dokumentumkezel\u0151 szoftvert a CERN-ben fejlesztett\xe9k. Fedezze fel b\xe1tran a tesztrendszer ny\xfajtotta szolg\xe1ltat\xe1sokat!'
        id = 72
        title = u'IMPRESSZUM'

    class Portalbox_73:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 73
        title = u'L\xc1SD M\xc9G'

    class Portalbox_74:
        body = u'Welkom by die demo tuiste van Invenio, gratis dokument bediener sagteware wat deur CERN geskryf is. Voel vry om al die eienskappe van die demo te deursoek.'
        id = 74
        title = u'OMTRENT HIERDIE TUISTE'

    class Portalbox_75:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 75
        title = u'SIEN OOK'

    class Portalbox_76:
        body = u'Benvido \xf3 sitio de demostraci\xf3n do Invenio, un software de servidor de documentos do CERN. Por favor s\xedntete libre de explorar todas as caracter\xedsticas deste sitio de demostraci\xf3n.'
        id = 76
        title = u'ACERCA DESTE SITIO'

    class Portalbox_77:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 77
        title = u'VEXA TAM\xc9N'

    class Portalbox_78:
        body = u'The "Atlantis Times" collections contain the articles from the <a href="/journal/atlantistimes/">Atlantis Times</a> journal.'
        id = 78
        title = u'ABOUT ATLANTIS TIMES'

    class Portalbox_79:
        body = u'Bine a\u0163i venit pe site-ul demo al Invenio, un software gratuit pentru servere de documente, creat de CERN. Nu ezita\u0163i s\u0103 explora\u0163i din plin toate caracteristicile acestui site demo.'
        id = 79
        title = u'DESPRE ACEST SITE'

    class Portalbox_80:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 80
        title = u'ALTE RESURSE'

    class Portalbox_81:
        body = u"Murakzaneza kuri web ya Invenio, iyi ni koranabuhanga y'ubuntu ya kozwe na CERN. Bitimuntu afite uburenganzira bwo kuyigerageza no kuyikoresha."
        id = 81
        title = u"IBYEREKERANYE N'IYI WEB"

    class Portalbox_82:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 82
        title = u"REBA N'IBI"

    class Portalbox_83:
        body = u'\u10d9\u10d4\u10d7\u10d8\u10da\u10d8 \u10d8\u10e7\u10dd\u10e1 \u10d7\u10e5\u10d5\u10d4\u10dc\u10d8 \u10db\u10dd\u10d1\u10e0\u10eb\u10d0\u10dc\u10d4\u10d1\u10d0 Invenio -\u10d8\u10e1 \u10e1\u10d0\u10d3\u10d4\u10db\u10dd\u10dc\u10e1\u10e2\u10e0\u10d0\u10ea\u10d8\u10dd \u10e1\u10d0\u10d8\u10e2\u10d6\u10d4, \u10d7\u10d0\u10d5\u10d8\u10e1\u10e3\u10e4\u10d0\u10da\u10d8 \u10d3\u10dd\u10d9\u10e3\u10db\u10d4\u10dc\u10e2\u10d4\u10d1\u10d8\u10e1 \u10e1\u10d4\u10e0\u10d5\u10d4\u10e0\u10d8 CERN -\u10d8\u10e1\u10d0\u10d2\u10d0\u10dc. \u10d2\u10d7\u10ee\u10dd\u10d5\u10d7 \u10e1\u10e0\u10e3\u10da\u10d0\u10d3 \u10e8\u10d4\u10d8\u10e1\u10ec\u10d0\u10d5\u10da\u10dd\u10d7 \u10e1\u10d0\u10d3\u10d4\u10db\u10dd\u10dc\u10e1\u10e2\u10e0\u10d0\u10ea\u10d8\u10dd \u10e1\u10d0\u10d8\u10e2\u10d8\u10e1 \u10e8\u10d4\u10e1\u10d0\u10eb\u10da\u10d4\u10d1\u10da\u10dd\u10d1\u10d4\u10d1\u10d8.'
        id = 83
        title = u'\u10e1\u10d0\u10d8\u10e2\u10d8\u10e1 \u10e8\u10d4\u10e1\u10d0\u10ee\u10d4\u10d1'

    class Portalbox_84:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 84
        title = u'\u10d0\u10e1\u10d4\u10d5\u10d4 \u10d8\u10ee\u10d8\u10da\u10d4\u10d7'

    class Portalbox_85:
        body = u'Sveiki atvyk\u0119 \u012f Invenio bandom\u0105j\u012f tinklap\u012f. Invenio yra nemokama programin\u0117 \u012franga dokument\u0173 serveriams, sukurta CERN. Kvie\u010diame i\u0161bandyti visas tinklapio galimybes ir funkcijas.'
        id = 85
        title = u'APIE PUSLAP\u012e'

    class Portalbox_86:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 86
        title = u'TAIP PAT \u017dI\u016aR\u0116KITE'

    class Portalbox_87:
        body = u'\u0645\u0631\u062d\u0628\u0627 \u0628\u0643\u0645 \u0641\u064a \u0627\u0644\u0645\u0648\u0642\u0639 \u0627\u0644\u062a\u062c\u0631\u064a\u0628\u064a \u0644\u0625\u0646\u0641\u064a\u0646\u064a\u0648\u060c \u0627\u0644\u0645\u062d\u0637\u0629 \u0627\u0644\u062e\u0627\u062f\u0645\u0629 (\u0627\u0644\u062d\u0631\u0629) \u0627\u0644\u0645\u0628\u0631\u0645\u062c\u0629 \u0645\u0646 \u0637\u0631\u0641 \u0627\u0644\u0645\u0646\u0638\u0645\u0629 \u0627\u0644\u0623\u0648\u0631\u0628\u064a\u0629 \u0644\u0644\u0628\u062d\u0648\u062b \u0627\u0644\u0646\u0648\u0648\u064a\u0629. \u0627\u0644\u0631\u062c\u0627\u0621 \u0639\u062f\u0645 \u0627\u0644\u062a\u0631\u062f\u062f \u0644\u0644\u0625\u0637\u0644\u0627\u0639 \u0639\u0644\u0649 \u062c\u0645\u064a\u0639 \u0635\u0641\u062d\u0627\u062a \u0647\u0630\u0627 \u0627\u0644\u0645\u0648\u0642\u0639 \u0627\u0644\u062a\u062c\u0631\u064a\u0628\u064a'
        id = 87
        title = u'\u062d\u0648\u0644 \u0647\u0630\u0627 \u0627\u0644\u0645\u0648\u0642\u0639'

    class Portalbox_88:
        body = u'<a href="http://invenio-software.org/">Invenio</a><br /><a href="http://www.cern.ch/">CERN</a>'
        id = 88
        title = u'\u0632\u0648\u0631\u0648\u0627 \u0623\u064a\u0636\u0627'

    class Portalbox_89:
        body = u'The Notes collection is a temporary collection that is being used for testing.'
        id = 89
        title = u'ABOUT Notes'

    class Portalbox_90:
        body = u'The ALEPH Papers collection is a temporary collection that is being used for testing.'
        id = 90
        title = u'ABOUT ALEPH Papers'

    class Portalbox_91:
        body = u'The ALEPH Internal Notes collection is a temporary restricted collection that is being used for testing.'
        id = 91
        title = u'ABOUT ALEPH Internal Notes'

    class Portalbox_92:
        body = u'The ALEPH Theses collection is a temporary restricted collection that is being used for testing.'
        id = 92
        title = u'ABOUT ALEPH Theses'

    class Portalbox_93:
        body = u'The ISOLDE Papers collection is a temporary collection that is being used for testing.'
        id = 93
        title = u'ABOUT ISOLDE Papers'

    class Portalbox_94:
        body = u'The ISOLDE Internal Notes collection is a temporary restricted and hidden collection that is being used for testing.'
        id = 94
        title = u'ABOUT ISOLDE Internal Notes'

    class Portalbox_95:
        body = u'The Drafts collection is a temporary restricted collection that is being used for testing.'
        id = 95
        title = u'ABOUT Drafts'


class ExampleData(DataSet):

    class Example_1:
        body = u'author:"Ellis, J"'
        type = u'author search'
        id = 1

    class Example_2:
        body = u'quantum'
        type = u'word search'
        id = 2

    class Example_3:
        body = u'quant*'
        type = u'wildcard word search'
        id = 3

    class Example_4:
        body = u"title:'standard model'"
        type = u'phrase search'
        id = 4

    class Example_5:
        body = u'quark -sigma +dense'
        type = u'boolean search'
        id = 5

    class Example_6:
        body = u'author:draper title:electrical'
        type = u'complex boolean search'
        id = 6

    class Example_7:
        body = u"author:ellis -muon* +abstract:'dense quark matter'"
        type = u'complex boolean search'
        id = 7

    class Example_8:
        body = u'ellis muon*'
        type = u'boolean search'
        id = 8

    class Example_13:
        body = u'references:"Theor. Math. Phys. 2 (1998) 231"'
        type = u'reference search'
        id = 13

    class Example_14:
        body = u"abstract:'Higgs boson'"
        type = u'phrase search'
        id = 14

    class Example_15:
        body = u'cal*'
        type = u'wildcard word search'
        id = 15

    class Example_16:
        body = u'keyword:Nobel'
        type = u'keyword search'
        id = 16

    class Example_17:
        body = u'author:Cole'
        type = u'author search'
        id = 17

    class Example_18:
        body = u"title:'nuclear electronics'"
        type = u'phrase search'
        id = 18

    class Example_19:
        body = u'supergravity and author:"Ellis, J" and year:1980->1990'
        type = u'combined search'
        id = 19


class CollectionExampleData(DataSet):

    #class CollectionExample_15_0:
    #    id_example = None
    #    score = 27
    #    id_collection = CollectionData.articlesPreprints.ref('id')

    class CollectionExample_15_1:
        id_example = ExampleData.Example_1.ref('id')
        score = 1
        id_collection = CollectionData.articlesPreprints.ref('id')

    class CollectionExample_15_19:
        id_example = ExampleData.Example_19.ref('id')
        score = 0
        id_collection = CollectionData.articlesPreprints.ref('id')

    class CollectionExample_15_2:
        id_example = ExampleData.Example_2.ref('id')
        score = 8
        id_collection = CollectionData.articlesPreprints.ref('id')

    class CollectionExample_15_3:
        id_example = ExampleData.Example_3.ref('id')
        score = 60
        id_collection = CollectionData.articlesPreprints.ref('id')

    class CollectionExample_15_4:
        id_example = ExampleData.Example_4.ref('id')
        score = 40
        id_collection = CollectionData.articlesPreprints.ref('id')

    class CollectionExample_15_5:
        id_example = ExampleData.Example_5.ref('id')
        score = 2
        id_collection = CollectionData.articlesPreprints.ref('id')

    class CollectionExample_15_6:
        id_example = ExampleData.Example_6.ref('id')
        score = 4
        id_collection = CollectionData.articlesPreprints.ref('id')

    class CollectionExample_15_7:
        id_example = ExampleData.Example_7.ref('id')
        score = 5
        id_collection = CollectionData.articlesPreprints.ref('id')

    class CollectionExample_15_8:
        id_example = ExampleData.Example_8.ref('id')
        score = 3
        id_collection = CollectionData.articlesPreprints.ref('id')

    class CollectionExample_16_1:
        id_example = ExampleData.Example_1.ref('id')
        score = 1
        id_collection = CollectionData.booksReports.ref('id')

    class CollectionExample_16_19:
        id_example = ExampleData.Example_19.ref('id')
        score = 0
        id_collection = CollectionData.booksReports.ref('id')

    class CollectionExample_16_2:
        id_example = ExampleData.Example_2.ref('id')
        score = 8
        id_collection = CollectionData.booksReports.ref('id')

    class CollectionExample_16_3:
        id_example = ExampleData.Example_3.ref('id')
        score = 7
        id_collection = CollectionData.booksReports.ref('id')

    class CollectionExample_16_4:
        id_example = ExampleData.Example_4.ref('id')
        score = 6
        id_collection = CollectionData.booksReports.ref('id')

    class CollectionExample_16_5:
        id_example = ExampleData.Example_5.ref('id')
        score = 2
        id_collection = CollectionData.booksReports.ref('id')

    class CollectionExample_16_6:
        id_example = ExampleData.Example_6.ref('id')
        score = 4
        id_collection = CollectionData.booksReports.ref('id')

    class CollectionExample_16_7:
        id_example = ExampleData.Example_7.ref('id')
        score = 5
        id_collection = CollectionData.booksReports.ref('id')

    class CollectionExample_16_8:
        id_example = ExampleData.Example_8.ref('id')
        score = 3
        id_collection = CollectionData.booksReports.ref('id')

    class CollectionExample_17_14:
        id_example = ExampleData.Example_14.ref('id')
        score = 10
        id_collection = CollectionData.multimediaArts.ref('id')

    class CollectionExample_17_15:
        id_example = ExampleData.Example_15.ref('id')
        score = 20
        id_collection = CollectionData.multimediaArts.ref('id')

    class CollectionExample_17_16:
        id_example = ExampleData.Example_16.ref('id')
        score = 30
        id_collection = CollectionData.multimediaArts.ref('id')

    class CollectionExample_1_1:
        id_example = ExampleData.Example_1.ref('id')
        score = 1
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionExample_1_13:
        id_example = ExampleData.Example_13.ref('id')
        score = 50
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionExample_1_19:
        id_example = ExampleData.Example_19.ref('id')
        score = 0
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionExample_1_2:
        id_example = ExampleData.Example_2.ref('id')
        score = 8
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionExample_1_3:
        id_example = ExampleData.Example_3.ref('id')
        score = 7
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionExample_1_4:
        id_example = ExampleData.Example_4.ref('id')
        score = 6
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionExample_1_5:
        id_example = ExampleData.Example_5.ref('id')
        score = 2
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionExample_1_6:
        id_example = ExampleData.Example_6.ref('id')
        score = 4
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionExample_1_7:
        id_example = ExampleData.Example_7.ref('id')
        score = 5
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionExample_1_8:
        id_example = ExampleData.Example_8.ref('id')
        score = 3
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionExample_2_1:
        id_example = ExampleData.Example_1.ref('id')
        score = 1
        id_collection = CollectionData.preprints.ref('id')

    class CollectionExample_2_2:
        id_example = ExampleData.Example_2.ref('id')
        score = 8
        id_collection = CollectionData.preprints.ref('id')

    class CollectionExample_2_3:
        id_example = ExampleData.Example_3.ref('id')
        score = 7
        id_collection = CollectionData.preprints.ref('id')

    class CollectionExample_2_4:
        id_example = ExampleData.Example_4.ref('id')
        score = 6
        id_collection = CollectionData.preprints.ref('id')

    class CollectionExample_2_5:
        id_example = ExampleData.Example_5.ref('id')
        score = 2
        id_collection = CollectionData.preprints.ref('id')

    class CollectionExample_2_6:
        id_example = ExampleData.Example_6.ref('id')
        score = 4
        id_collection = CollectionData.preprints.ref('id')

    class CollectionExample_2_7:
        id_example = ExampleData.Example_7.ref('id')
        score = 5
        id_collection = CollectionData.preprints.ref('id')

    class CollectionExample_2_8:
        id_example = ExampleData.Example_8.ref('id')
        score = 3
        id_collection = CollectionData.preprints.ref('id')

    class CollectionExample_3_17:
        id_example = ExampleData.Example_17.ref('id')
        score = 10
        id_collection = CollectionData.books.ref('id')

    class CollectionExample_3_18:
        id_example = ExampleData.Example_18.ref('id')
        score = 20
        id_collection = CollectionData.books.ref('id')

    class CollectionExample_3_6:
        id_example = ExampleData.Example_6.ref('id')
        score = 30
        id_collection = CollectionData.books.ref('id')

    class CollectionExample_4_1:
        id_example = ExampleData.Example_1.ref('id')
        score = 1
        id_collection = CollectionData.theses.ref('id')

    class CollectionExample_4_2:
        id_example = ExampleData.Example_2.ref('id')
        score = 8
        id_collection = CollectionData.theses.ref('id')

    class CollectionExample_4_3:
        id_example = ExampleData.Example_3.ref('id')
        score = 7
        id_collection = CollectionData.theses.ref('id')

    class CollectionExample_4_4:
        id_example = ExampleData.Example_4.ref('id')
        score = 6
        id_collection = CollectionData.theses.ref('id')

    class CollectionExample_4_5:
        id_example = ExampleData.Example_5.ref('id')
        score = 2
        id_collection = CollectionData.theses.ref('id')

    class CollectionExample_4_6:
        id_example = ExampleData.Example_6.ref('id')
        score = 4
        id_collection = CollectionData.theses.ref('id')

    class CollectionExample_4_7:
        id_example = ExampleData.Example_7.ref('id')
        score = 5
        id_collection = CollectionData.theses.ref('id')

    class CollectionExample_4_8:
        id_example = ExampleData.Example_8.ref('id')
        score = 3
        id_collection = CollectionData.theses.ref('id')

    class CollectionExample_5_1:
        id_example = ExampleData.Example_1.ref('id')
        score = 1
        id_collection = CollectionData.reports.ref('id')

    class CollectionExample_5_2:
        id_example = ExampleData.Example_2.ref('id')
        score = 8
        id_collection = CollectionData.reports.ref('id')

    class CollectionExample_5_3:
        id_example = ExampleData.Example_3.ref('id')
        score = 7
        id_collection = CollectionData.reports.ref('id')

    class CollectionExample_5_4:
        id_example = ExampleData.Example_4.ref('id')
        score = 6
        id_collection = CollectionData.reports.ref('id')

    class CollectionExample_5_5:
        id_example = ExampleData.Example_5.ref('id')
        score = 2
        id_collection = CollectionData.reports.ref('id')

    class CollectionExample_5_6:
        id_example = ExampleData.Example_6.ref('id')
        score = 4
        id_collection = CollectionData.reports.ref('id')

    class CollectionExample_5_7:
        id_example = ExampleData.Example_7.ref('id')
        score = 5
        id_collection = CollectionData.reports.ref('id')

    class CollectionExample_5_8:
        id_example = ExampleData.Example_8.ref('id')
        score = 3
        id_collection = CollectionData.reports.ref('id')

    #class CollectionExample_6_0:
    #    id_example = None
    #    score = 27
    #    id_collection = CollectionData.articles.ref('id')

    class CollectionExample_6_1:
        id_example = ExampleData.Example_1.ref('id')
        score = 10
        id_collection = CollectionData.articles.ref('id')

    class CollectionExample_6_2:
        id_example = ExampleData.Example_2.ref('id')
        score = 80
        id_collection = CollectionData.articles.ref('id')

    class CollectionExample_6_3:
        id_example = ExampleData.Example_3.ref('id')
        score = 60
        id_collection = CollectionData.articles.ref('id')

    class CollectionExample_6_4:
        id_example = ExampleData.Example_4.ref('id')
        score = 40
        id_collection = CollectionData.articles.ref('id')

    class CollectionExample_6_5:
        id_example = ExampleData.Example_5.ref('id')
        score = 20
        id_collection = CollectionData.articles.ref('id')

    class CollectionExample_6_8:
        id_example = ExampleData.Example_8.ref('id')
        score = 30
        id_collection = CollectionData.articles.ref('id')

    class CollectionExample_8_14:
        id_example = ExampleData.Example_14.ref('id')
        score = 10
        id_collection = CollectionData.pictures.ref('id')

    class CollectionExample_8_15:
        id_example = ExampleData.Example_15.ref('id')
        score = 20
        id_collection = CollectionData.pictures.ref('id')

    class CollectionExample_8_16:
        id_example = ExampleData.Example_16.ref('id')
        score = 30
        id_collection = CollectionData.pictures.ref('id')


class FieldvalueData(DataSet):

    class Fieldvalue_1:
        id = 1
        value = u'Particle Physics'
        name = u'Particle Physics'

    class Fieldvalue_2:
        id = 2
        value = u'Particle Physics - Experimental Results'
        name = u'Particle Physics - Experimental Results'

    class Fieldvalue_3:
        id = 3
        value = u'Particle Physics - Phenomenology'
        name = u'Particle Physics - Phenomenology'

    class Fieldvalue_4:
        id = 4
        value = u'Particle Physics - Theory'
        name = u'Particle Physics - Theory'

    class Fieldvalue_5:
        id = 5
        value = u'Particle Physics - Lattice'
        name = u'Particle Physics - Lattice'

    class Fieldvalue_6:
        id = 6
        value = u'Nuclear Physics'
        name = u'Nuclear Physics'

    class Fieldvalue_7:
        id = 7
        value = u'General Relativity and Cosmology'
        name = u'General Relativity and Cosmology'

    class Fieldvalue_8:
        id = 8
        value = u'General Theoretical Physics'
        name = u'General Theoretical Physics'

    class Fieldvalue_9:
        id = 9
        value = u'Detectors and Experimental Techniques'
        name = u'Detectors and Experimental Techniques'

    class Fieldvalue_10:
        id = 10
        value = u'Accelerators and Storage Rings'
        name = u'Accelerators and Storage Rings'

    class Fieldvalue_11:
        id = 11
        value = u'Health Physics and Radiation Effects'
        name = u'Health Physics and Radiation Effects'

    class Fieldvalue_12:
        id = 12
        value = u'Computing and Computers'
        name = u'Computing and Computers'

    class Fieldvalue_13:
        id = 13
        value = u'Mathematical Physics and Mathematics'
        name = u'Mathematical Physics and Mathematics'

    class Fieldvalue_14:
        id = 14
        value = u'Astrophysics and Astronomy'
        name = u'Astrophysics and Astronomy'

    class Fieldvalue_15:
        id = 15
        value = u'Nonlinear Systems'
        name = u'Nonlinear Systems'

    class Fieldvalue_16:
        id = 16
        value = u'Condensed Matter'
        name = u'Condensed Matter'

    class Fieldvalue_17:
        id = 17
        value = u'Other Fields of Physics'
        name = u'Other Fields of Physics'

    class Fieldvalue_18:
        id = 18
        value = u'Chemical Physics and Chemistry'
        name = u'Chemical Physics and Chemistry'

    class Fieldvalue_19:
        id = 19
        value = u'Engineering'
        name = u'Engineering'

    class Fieldvalue_20:
        id = 20
        value = u'Information Transfer and Management'
        name = u'Information Transfer and Management'

    class Fieldvalue_21:
        id = 21
        value = u'Other Aspects of Science'
        name = u'Other Aspects of Science'

    class Fieldvalue_22:
        id = 22
        value = u'Commerce, Economics, Social Science'
        name = u'Commerce, Economics, Social Science'

    class Fieldvalue_23:
        id = 23
        value = u'Biography, Geography, History'
        name = u'Biography, Geography, History'

    class Fieldvalue_24:
        id = 24
        value = u'Other Subjects'
        name = u'Other Subjects'

    class Fieldvalue_25:
        id = 25
        value = u'TH'
        name = u'CERN TH'

    class Fieldvalue_26:
        id = 26
        value = u'PPE'
        name = u'CERN PPE'

    class Fieldvalue_27:
        id = 27
        value = u'Experiments and Tracks'
        name = u'Experiments and Tracks'

    class Fieldvalue_28:
        id = 28
        value = u'Personalities and History of CERN'
        name = u'Personalities and History of CERN'

    class Fieldvalue_29:
        id = 29
        value = u'Diagrams and Charts'
        name = u'Diagrams and Charts'

    class Fieldvalue_30:
        id = 30
        value = u'Life at CERN'
        name = u'Life at CERN'

    class Fieldvalue_31:
        id = 31
        value = u'ETT'
        name = u'CERN ETT'

    class Fieldvalue_32:
        id = 32
        value = u'EP'
        name = u'CERN EP'


class CollectionPortalboxData(DataSet):

    class CollectionPortalbox_10_16_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_16.ref('id')
        score = 100
        id_collection = CollectionData.CERNExperiments.ref('id')

    class CollectionPortalbox_11_17_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_17.ref('id')
        score = 100
        id_collection = CollectionData.theoreticalPhysics.ref('id')

    class CollectionPortalbox_12_18_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_18.ref('id')
        score = 100
        id_collection = CollectionData.experimentalPhysics.ref('id')

    class CollectionPortalbox_13_19_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_19.ref('id')
        score = 100
        id_collection = CollectionData.ISOLDE.ref('id')

    class CollectionPortalbox_14_20_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_20.ref('id')
        score = 100
        id_collection = CollectionData.ALEPH.ref('id')

    class CollectionPortalbox_15_21_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_21.ref('id')
        score = 100
        id_collection = CollectionData.articlesPreprints.ref('id')

    class CollectionPortalbox_15_51_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_51.ref('id')
        score = 95
        id_collection = CollectionData.articlesPreprints.ref('id')

    class CollectionPortalbox_16_22_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_22.ref('id')
        score = 100
        id_collection = CollectionData.booksReports.ref('id')

    class CollectionPortalbox_16_52_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_52.ref('id')
        score = 95
        id_collection = CollectionData.booksReports.ref('id')

    class CollectionPortalbox_17_23_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_23.ref('id')
        score = 100
        id_collection = CollectionData.multimediaArts.ref('id')

    class CollectionPortalbox_17_53_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_53.ref('id')
        score = 95
        id_collection = CollectionData.multimediaArts.ref('id')

    class CollectionPortalbox_18_24_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_24.ref('id')
        score = 100
        id_collection = CollectionData.poetry.ref('id')

    class CollectionPortalbox_19_78_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_78.ref('id')
        score = 100
        id_collection = CollectionData.atlantisTimesNews.ref('id')

    class CollectionPortalbox_1_1_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_1.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_25_fr:
        ln = u'fr'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_25.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_26_fr:
        ln = u'fr'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_26.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_27_sk:
        ln = u'sk'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_27.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_28_sk:
        ln = u'sk'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_28.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_29_cs:
        ln = u'cs'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_29.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_2_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_2.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_30_cs:
        ln = u'cs'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_30.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_31_de:
        ln = u'de'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_31.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_32_de:
        ln = u'de'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_32.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_33_es:
        ln = u'es'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_33.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_34_es:
        ln = u'es'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_34.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_35_it:
        ln = u'it'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_35.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_36_it:
        ln = u'it'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_36.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_37_no:
        ln = u'no'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_37.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_38_no:
        ln = u'no'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_38.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_39_pt:
        ln = u'pt'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_39.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_40_pt:
        ln = u'pt'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_40.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_41_ru:
        ln = u'ru'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_41.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_42_ru:
        ln = u'ru'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_42.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_43_sv:
        ln = u'sv'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_43.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_44_sv:
        ln = u'sv'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_44.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_54_el:
        ln = u'el'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_54.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_55_el:
        ln = u'el'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_55.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_56_uk:
        ln = u'uk'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_56.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_57_uk:
        ln = u'uk'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_57.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_58_ca:
        ln = u'ca'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_58.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_59_ca:
        ln = u'ca'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_59.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_60_ja:
        ln = u'ja'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_60.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_61_ja:
        ln = u'ja'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_61.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_62_pl:
        ln = u'pl'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_62.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_63_pl:
        ln = u'pl'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_63.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_64_bg:
        ln = u'bg'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_64.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_65_bg:
        ln = u'bg'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_65.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_66_hr:
        ln = u'hr'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_66.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_67_hr:
        ln = u'hr'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_67.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_68_zhCN:
        ln = u'zh_CN'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_68.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_69_zhCN:
        ln = u'zh_CN'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_69.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_70_zhTW:
        ln = u'zh_TW'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_70.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_71_zhTW:
        ln = u'zh_TW'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_71.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_72_hu:
        ln = u'hu'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_72.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_73_hu:
        ln = u'hu'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_73.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_74_af:
        ln = u'af'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_74.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_75_af:
        ln = u'af'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_75.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_76_gl:
        ln = u'gl'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_76.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_77_gl:
        ln = u'gl'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_77.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_79_ro:
        ln = u'ro'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_79.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_80_ro:
        ln = u'ro'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_80.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_81_rw:
        ln = u'rw'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_81.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_82_rw:
        ln = u'rw'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_82.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_83_ka:
        ln = u'ka'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_83.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_84_ka:
        ln = u'ka'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_84.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_85_lt:
        ln = u'lt'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_85.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_86_lt:
        ln = u'lt'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_86.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_87_ar:
        ln = u'ar'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_87.ref('id')
        score = 100
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_1_88_ar:
        ln = u'ar'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_88.ref('id')
        score = 90
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionPortalbox_20_78_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_78.ref('id')
        score = 100
        id_collection = CollectionData.atlantisTimesArts.ref('id')

    class CollectionPortalbox_21_78_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_78.ref('id')
        score = 100
        id_collection = CollectionData.atlantisTimesScience.ref('id')

    class CollectionPortalbox_22_78_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_78.ref('id')
        score = 100
        id_collection = CollectionData.atlantisTimes.ref('id')

    class CollectionPortalbox_26_89_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_89.ref('id')
        score = 100
        id_collection = CollectionData.notes.ref('id')

    class CollectionPortalbox_27_90_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_90.ref('id')
        score = 100
        id_collection = CollectionData.ALEPHPapers.ref('id')

    class CollectionPortalbox_28_91_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_91.ref('id')
        score = 100
        id_collection = CollectionData.ALEPHInternalNotes.ref('id')

    class CollectionPortalbox_29_92_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_92.ref('id')
        score = 100
        id_collection = CollectionData.ALEPHTheses.ref('id')

    class CollectionPortalbox_2_45_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_45.ref('id')
        score = 95
        id_collection = CollectionData.preprints.ref('id')

    class CollectionPortalbox_2_5_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_5.ref('id')
        score = 100
        id_collection = CollectionData.preprints.ref('id')

    class CollectionPortalbox_2_6_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_6.ref('id')
        score = 90
        id_collection = CollectionData.preprints.ref('id')

    class CollectionPortalbox_30_93_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_93.ref('id')
        score = 100
        id_collection = CollectionData.ISOLDEPapers.ref('id')

    class CollectionPortalbox_31_94_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_94.ref('id')
        score = 100
        id_collection = CollectionData.ISOLDEInternalNotes.ref('id')

    class CollectionPortalbox_32_95_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_95.ref('id')
        score = 100
        id_collection = CollectionData.drafts.ref('id')

    class CollectionPortalbox_3_46_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_46.ref('id')
        score = 95
        id_collection = CollectionData.books.ref('id')

    class CollectionPortalbox_3_7_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_7.ref('id')
        score = 100
        id_collection = CollectionData.books.ref('id')

    class CollectionPortalbox_3_8_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_8.ref('id')
        score = 90
        id_collection = CollectionData.books.ref('id')

    class CollectionPortalbox_4_10_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_10.ref('id')
        score = 90
        id_collection = CollectionData.theses.ref('id')

    class CollectionPortalbox_4_47_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_47.ref('id')
        score = 95
        id_collection = CollectionData.theses.ref('id')

    class CollectionPortalbox_4_9_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_9.ref('id')
        score = 100
        id_collection = CollectionData.theses.ref('id')

    class CollectionPortalbox_5_11_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_11.ref('id')
        score = 100
        id_collection = CollectionData.reports.ref('id')

    class CollectionPortalbox_5_48_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_48.ref('id')
        score = 95
        id_collection = CollectionData.reports.ref('id')

    class CollectionPortalbox_6_3_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_3.ref('id')
        score = 100
        id_collection = CollectionData.articles.ref('id')

    class CollectionPortalbox_6_49_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_49.ref('id')
        score = 95
        id_collection = CollectionData.articles.ref('id')

    class CollectionPortalbox_6_4_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_4.ref('id')
        score = 90
        id_collection = CollectionData.articles.ref('id')

    class CollectionPortalbox_8_14_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_14.ref('id')
        score = 100
        id_collection = CollectionData.pictures.ref('id')

    class CollectionPortalbox_8_50_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_50.ref('id')
        score = 95
        id_collection = CollectionData.pictures.ref('id')

    class CollectionPortalbox_9_15_en:
        ln = u'en'
        position = u'rt'
        id_portalbox = PortalboxData.Portalbox_15.ref('id')
        score = 100
        id_collection = CollectionData.CERNDivisions.ref('id')


class CollectionFormatData(DataSet):

    class CollectionFormat_15_1:
        score = 100
        id_format = FormatData.Format_1.ref('id')
        id_collection = CollectionData.articlesPreprints.ref('id')

    class CollectionFormat_15_18:
        score = 85
        id_format = FormatData.Format_18.ref('id')
        id_collection = CollectionData.articlesPreprints.ref('id')

    class CollectionFormat_15_2:
        score = 90
        id_format = FormatData.Format_2.ref('id')
        id_collection = CollectionData.articlesPreprints.ref('id')

    class CollectionFormat_15_3:
        score = 80
        id_format = FormatData.Format_3.ref('id')
        id_collection = CollectionData.articlesPreprints.ref('id')

    class CollectionFormat_15_4:
        score = 70
        id_format = FormatData.Format_4.ref('id')
        id_collection = CollectionData.articlesPreprints.ref('id')

    class CollectionFormat_15_5:
        score = 60
        id_format = FormatData.Format_5.ref('id')
        id_collection = CollectionData.articlesPreprints.ref('id')

    class CollectionFormat_1_1:
        score = 100
        id_format = FormatData.Format_1.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_2:
        score = 90
        id_format = FormatData.Format_2.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_3:
        score = 80
        id_format = FormatData.Format_3.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_4:
        score = 70
        id_format = FormatData.Format_4.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_5:
        score = 60
        id_format = FormatData.Format_5.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_2_1:
        score = 100
        id_format = FormatData.Format_1.ref('id')
        id_collection = CollectionData.preprints.ref('id')

    class CollectionFormat_2_2:
        score = 90
        id_format = FormatData.Format_2.ref('id')
        id_collection = CollectionData.preprints.ref('id')

    class CollectionFormat_2_3:
        score = 80
        id_format = FormatData.Format_3.ref('id')
        id_collection = CollectionData.preprints.ref('id')

    class CollectionFormat_2_4:
        score = 70
        id_format = FormatData.Format_4.ref('id')
        id_collection = CollectionData.preprints.ref('id')

    class CollectionFormat_2_5:
        score = 60
        id_format = FormatData.Format_5.ref('id')
        id_collection = CollectionData.preprints.ref('id')

    class CollectionFormat_3_1:
        score = 100
        id_format = FormatData.Format_1.ref('id')
        id_collection = CollectionData.books.ref('id')

    class CollectionFormat_3_2:
        score = 90
        id_format = FormatData.Format_2.ref('id')
        id_collection = CollectionData.books.ref('id')

    class CollectionFormat_3_3:
        score = 80
        id_format = FormatData.Format_3.ref('id')
        id_collection = CollectionData.books.ref('id')

    class CollectionFormat_3_4:
        score = 70
        id_format = FormatData.Format_4.ref('id')
        id_collection = CollectionData.books.ref('id')

    class CollectionFormat_3_5:
        score = 60
        id_format = FormatData.Format_5.ref('id')
        id_collection = CollectionData.books.ref('id')

    class CollectionFormat_4_1:
        score = 100
        id_format = FormatData.Format_1.ref('id')
        id_collection = CollectionData.theses.ref('id')

    class CollectionFormat_4_2:
        score = 90
        id_format = FormatData.Format_2.ref('id')
        id_collection = CollectionData.theses.ref('id')

    class CollectionFormat_4_3:
        score = 80
        id_format = FormatData.Format_3.ref('id')
        id_collection = CollectionData.theses.ref('id')

    class CollectionFormat_4_4:
        score = 70
        id_format = FormatData.Format_4.ref('id')
        id_collection = CollectionData.theses.ref('id')

    class CollectionFormat_4_5:
        score = 60
        id_format = FormatData.Format_5.ref('id')
        id_collection = CollectionData.theses.ref('id')

    class CollectionFormat_5_1:
        score = 100
        id_format = FormatData.Format_1.ref('id')
        id_collection = CollectionData.reports.ref('id')

    class CollectionFormat_5_2:
        score = 90
        id_format = FormatData.Format_2.ref('id')
        id_collection = CollectionData.reports.ref('id')

    class CollectionFormat_5_3:
        score = 80
        id_format = FormatData.Format_3.ref('id')
        id_collection = CollectionData.reports.ref('id')

    class CollectionFormat_5_4:
        score = 70
        id_format = FormatData.Format_4.ref('id')
        id_collection = CollectionData.reports.ref('id')

    class CollectionFormat_5_5:
        score = 60
        id_format = FormatData.Format_5.ref('id')
        id_collection = CollectionData.reports.ref('id')

    class CollectionFormat_6_1:
        score = 100
        id_format = FormatData.Format_1.ref('id')
        id_collection = CollectionData.articles.ref('id')

    class CollectionFormat_6_2:
        score = 90
        id_format = FormatData.Format_2.ref('id')
        id_collection = CollectionData.articles.ref('id')

    class CollectionFormat_6_3:
        score = 80
        id_format = FormatData.Format_3.ref('id')
        id_collection = CollectionData.articles.ref('id')

    class CollectionFormat_6_4:
        score = 70
        id_format = FormatData.Format_4.ref('id')
        id_collection = CollectionData.articles.ref('id')

    class CollectionFormat_6_5:
        score = 60
        id_format = FormatData.Format_5.ref('id')
        id_collection = CollectionData.articles.ref('id')

    class CollectionFormat_8_1:
        score = 100
        id_format = FormatData.Format_1.ref('id')
        id_collection = CollectionData.pictures.ref('id')

    class CollectionFormat_8_2:
        score = 90
        id_format = FormatData.Format_2.ref('id')
        id_collection = CollectionData.pictures.ref('id')

    class CollectionFormat_8_3:
        score = 80
        id_format = FormatData.Format_3.ref('id')
        id_collection = CollectionData.pictures.ref('id')

    class CollectionFormat_8_4:
        score = 70
        id_format = FormatData.Format_4.ref('id')
        id_collection = CollectionData.pictures.ref('id')

    class CollectionFormat_8_5:
        score = 60
        id_format = FormatData.Format_5.ref('id')
        id_collection = CollectionData.pictures.ref('id')

    class CollectionFormat_8_6:
        score = 96
        id_format = FormatData.Format_6.ref('id')
        id_collection = CollectionData.pictures.ref('id')

    class CollectionFormat_8_7:
        score = 93
        id_format = FormatData.Format_7.ref('id')
        id_collection = CollectionData.pictures.ref('id')


class CollectionFieldFieldvalueData(DataSet):
    class CollectionFieldFieldvalue_2_7_7:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_7.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 18

    class CollectionFieldFieldvalue_2_7_6:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_6.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 19

    class CollectionFieldFieldvalue_2_7_5:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_5.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 20

    class CollectionFieldFieldvalue_2_7_4:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_4.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 21

    class CollectionFieldFieldvalue_6_7_1:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_1.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 24

    class CollectionFieldFieldvalue_6_7_2:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_2.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 23

    class CollectionFieldFieldvalue_6_7_3:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_3.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 22

    class CollectionFieldFieldvalue_6_7_4:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_4.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 21

    class CollectionFieldFieldvalue_6_7_5:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_5.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 20

    class CollectionFieldFieldvalue_6_7_6:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_6.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 19

    class CollectionFieldFieldvalue_6_7_7:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_7.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 18

    class CollectionFieldFieldvalue_6_7_8:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_8.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 17

    class CollectionFieldFieldvalue_6_7_9:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_9.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 16

    class CollectionFieldFieldvalue_6_7_10:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_10.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 15

    class CollectionFieldFieldvalue_6_7_11:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_11.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 14

    class CollectionFieldFieldvalue_6_7_12:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_12.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 13

    class CollectionFieldFieldvalue_6_7_13:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_13.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 12

    class CollectionFieldFieldvalue_6_7_14:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_14.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 11

    class CollectionFieldFieldvalue_6_7_15:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_15.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 10

    class CollectionFieldFieldvalue_6_7_16:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_16.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 9

    class CollectionFieldFieldvalue_6_7_17:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_17.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 8

    class CollectionFieldFieldvalue_6_7_18:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_18.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 7

    class CollectionFieldFieldvalue_6_7_19:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_19.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 6

    class CollectionFieldFieldvalue_6_7_20:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_20.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 5

    class CollectionFieldFieldvalue_6_7_21:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_21.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 4

    class CollectionFieldFieldvalue_6_7_22:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_22.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 3

    class CollectionFieldFieldvalue_6_7_23:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_23.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 2

    class CollectionFieldFieldvalue_6_7_24:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_24.ref('id')
        type = 'seo'
        score = 2
        score_fieldvalue = 1

    class CollectionFieldFieldvalue_2_7_3:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_3.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 22

    class CollectionFieldFieldvalue_2_7_2:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_2.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 23

    class CollectionFieldFieldvalue_6_8_None:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_8.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 2
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_2_7_1:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_1.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 24

    class CollectionFieldFieldvalue_6_4_None:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_4.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 4
        score_fieldvalue = 70

    class CollectionFieldFieldvalue_6_2_None:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_2.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 3
        score_fieldvalue = 70

    class CollectionFieldFieldvalue_6_19_None:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_19.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 3
        score_fieldvalue = 65

    class CollectionFieldFieldvalue_6_5_None:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_5.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 1
        score_fieldvalue = 70

    class CollectionFieldFieldvalue_6_11_25:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_11.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_25.ref('id')
        type = 'seo'
        score = 1
        score_fieldvalue = 1

    class CollectionFieldFieldvalue_6_11_26:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_11.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_26.ref('id')
        type = 'seo'
        score = 1
        score_fieldvalue = 2

    class CollectionFieldFieldvalue_8_7_27:
        id_collection = CollectionData.pictures.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_27.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 3

    class CollectionFieldFieldvalue_8_7_28:
        id_collection = CollectionData.pictures.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_28.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 1

    class CollectionFieldFieldvalue_8_7_29:
        id_collection = CollectionData.pictures.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_29.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 4

    class CollectionFieldFieldvalue_8_7_30:
        id_collection = CollectionData.pictures.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_30.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 2

    class CollectionFieldFieldvalue_6_3_None:
        id_collection = CollectionData.articles.ref('id')
        id_field = FieldData.Field_3.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 5
        score_fieldvalue = 70

    class CollectionFieldFieldvalue_2_7_8:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_8.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 17

    class CollectionFieldFieldvalue_2_7_9:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_9.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 16

    class CollectionFieldFieldvalue_2_7_10:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_10.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 15

    class CollectionFieldFieldvalue_2_7_11:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_11.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 14

    class CollectionFieldFieldvalue_2_7_12:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_12.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 13

    class CollectionFieldFieldvalue_2_7_13:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_13.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 12

    class CollectionFieldFieldvalue_2_7_14:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_14.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 11

    class CollectionFieldFieldvalue_2_7_15:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_15.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 10

    class CollectionFieldFieldvalue_2_7_16:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_16.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 9

    class CollectionFieldFieldvalue_2_7_17:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_17.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 8

    class CollectionFieldFieldvalue_2_7_18:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_18.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 7

    class CollectionFieldFieldvalue_2_7_19:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_19.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 6

    class CollectionFieldFieldvalue_2_7_20:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_20.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 5

    class CollectionFieldFieldvalue_2_7_21:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_21.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 4

    class CollectionFieldFieldvalue_2_7_22:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_22.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 3

    class CollectionFieldFieldvalue_2_7_23:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_23.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 2

    class CollectionFieldFieldvalue_2_7_24:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_24.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 1

    class CollectionFieldFieldvalue_2_8_None:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_8.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 20
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_2_4_None:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_4.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 40
        score_fieldvalue = 70

    class CollectionFieldFieldvalue_2_2_None:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_2.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 60
        score_fieldvalue = 70

    class CollectionFieldFieldvalue_2_5_None:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_5.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 30
        score_fieldvalue = 70

    class CollectionFieldFieldvalue_2_11_26:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_11.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_26.ref('id')
        type = 'seo'
        score = 5
        score_fieldvalue = 1

    class CollectionFieldFieldvalue_2_3_None:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_3.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 50
        score_fieldvalue = 70

    class CollectionFieldFieldvalue_2_11_25:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_11.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_25.ref('id')
        type = 'seo'
        score = 5
        score_fieldvalue = 2

    class CollectionFieldFieldvalue_2_11_32:
        id_collection = CollectionData.preprints.ref('id')
        id_field = FieldData.Field_11.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_32.ref('id')
        type = 'seo'
        score = 5
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_3_2_None:
        id_collection = CollectionData.books.ref('id')
        id_field = FieldData.Field_2.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 10
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_3_3_None:
        id_collection = CollectionData.books.ref('id')
        id_field = FieldData.Field_3.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 20
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_3_12_None:
        id_collection = CollectionData.books.ref('id')
        id_field = FieldData.Field_12.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 30
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_4_4_None:
        id_collection = CollectionData.theses.ref('id')
        id_field = FieldData.Field_4.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 30
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_4_3_None:
        id_collection = CollectionData.theses.ref('id')
        id_field = FieldData.Field_3.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 40
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_4_12_None:
        id_collection = CollectionData.theses.ref('id')
        id_field = FieldData.Field_12.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 10
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_4_2_None:
        id_collection = CollectionData.theses.ref('id')
        id_field = FieldData.Field_2.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 50
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_4_6_None:
        id_collection = CollectionData.theses.ref('id')
        id_field = FieldData.Field_6.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 20
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_4_7_None:
        id_collection = CollectionData.theses.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = 0
        type = 'seo'
        score = 10
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_4_7_12:
        id_collection = CollectionData.theses.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_12.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 2

    class CollectionFieldFieldvalue_4_7_8:
        id_collection = CollectionData.theses.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_8.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 3

    class CollectionFieldFieldvalue_4_7_10:
        id_collection = CollectionData.theses.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_10.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 1

    class CollectionFieldFieldvalue_5_6_None:
        id_collection = CollectionData.reports.ref('id')
        id_field = FieldData.Field_6.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 20
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_5_12_None:
        id_collection = CollectionData.reports.ref('id')
        id_field = FieldData.Field_12.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 10
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_5_4_None:
        id_collection = CollectionData.reports.ref('id')
        id_field = FieldData.Field_4.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 30
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_5_3_None:
        id_collection = CollectionData.reports.ref('id')
        id_field = FieldData.Field_3.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 40
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_5_2_None:
        id_collection = CollectionData.reports.ref('id')
        id_field = FieldData.Field_2.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 50
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_5_7_None:
        id_collection = CollectionData.reports.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = 0
        type = 'seo'
        score = 10
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_5_7_9:
        id_collection = CollectionData.reports.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_9.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 3

    class CollectionFieldFieldvalue_5_7_12:
        id_collection = CollectionData.reports.ref('id')
        id_field = FieldData.Field_7.ref('id')
        id_fieldvalue = FieldvalueData.Fieldvalue_12.ref('id')
        type = 'seo'
        score = 10
        score_fieldvalue = 2

    class CollectionFieldFieldvalue_8_6_None:
        id_collection = CollectionData.pictures.ref('id')
        id_field = FieldData.Field_6.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 10
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_8_2_None:
        id_collection = CollectionData.pictures.ref('id')
        id_field = FieldData.Field_2.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 50
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_8_3_None:
        id_collection = CollectionData.pictures.ref('id')
        id_field = FieldData.Field_3.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 40
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_8_5_None:
        id_collection = CollectionData.pictures.ref('id')
        id_field = FieldData.Field_5.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 20
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_8_4_None:
        id_collection = CollectionData.pictures.ref('id')
        id_field = FieldData.Field_4.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 30
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_1_2_None:
        id_collection = CollectionData.siteCollection.ref('id')
        id_field = FieldData.Field_2.ref('id')
        id_fieldvalue = 0
        type = 'soo'
        score = 40
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_1_3_None:
        id_collection = CollectionData.siteCollection.ref('id')
        id_field = FieldData.Field_3.ref('id')
        id_fieldvalue = 0
        type = 'soo'
        score = 30
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_1_6_None:
        id_collection = CollectionData.siteCollection.ref('id')
        id_field = FieldData.Field_6.ref('id')
        id_fieldvalue = 0
        type = 'soo'
        score = 20
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_1_12_None:
        id_collection = CollectionData.siteCollection.ref('id')
        id_field = FieldData.Field_12.ref('id')
        id_fieldvalue = 0
        type = 'soo'
        score = 10
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_3_15_None:
        id_collection = CollectionData.books.ref('id')
        id_field = FieldData.Field_15.ref('id')
        id_fieldvalue = 0
        type = 'soo'
        score = 20
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_34_33_None:
        id_collection = CollectionData.Collection_34.ref('id')
        id_field = FieldData.Field_33.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 4
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_34_34_None:
        id_collection = CollectionData.Collection_34.ref('id')
        id_field = FieldData.Field_34.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 3
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_34_35_None:
        id_collection = CollectionData.Collection_34.ref('id')
        id_field = FieldData.Field_35.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 2
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_34_36_None:
        id_collection = CollectionData.Collection_34.ref('id')
        id_field = FieldData.Field_36.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 1
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_35_33_None:
        id_collection = CollectionData.Collection_35.ref('id')
        id_field = FieldData.Field_33.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 1
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_36_34_None:
        id_collection = CollectionData.Collection_36.ref('id')
        id_field = FieldData.Field_34.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 1
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_37_35_None:
        id_collection = CollectionData.Collection_37.ref('id')
        id_field = FieldData.Field_35.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 1
        score_fieldvalue = 0

    class CollectionFieldFieldvalue_38_36_None:
        id_collection = CollectionData.Collection_38.ref('id')
        id_field = FieldData.Field_36.ref('id')
        id_fieldvalue = 0
        type = 'sew'
        score = 1
        score_fieldvalue = 0
