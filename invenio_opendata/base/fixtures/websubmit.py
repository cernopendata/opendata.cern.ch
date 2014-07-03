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

import datetime
from fixture import DataSet


class SbmCOLLECTIONData(DataSet):

    class SbmCOLLECTION_36:
        id = 36L
        name = u'Document Types'


class SbmCOLLECTIONSbmCOLLECTIONData(DataSet):

    class SbmCOLLECTIONSbmCOLLECTION_0_36:
        id_son = SbmCOLLECTIONData.SbmCOLLECTION_36.ref('id')
        catalogue_order = 1L
        id_father = None


class SbmDOCTYPEData(DataSet):

    class SbmDOCTYPE_DEMOART:
        md = datetime.date(2008, 3, 6)
        ldocname = u'Demo Article Submission'
        description = u'<br /><br />The Demo Article submission demonstrates a more complex submission type.<br /><br />\r\nThe submission gives a document a category. This category is used in the document\'s reference number and also serves as a means to classify it into a specific ATLANTIS collection. Documents submitted into the "Article" category are inserted into the ATLANTIS "Articles" collection, documents categorized as "Preprint" are inserted into the ATLANTIS "Preprints" collection, and a document categorized as a "Report" is inserted into the ATLANTIS "Reports" collection.<br /><br />\r\n'
        sdocname = u'DEMOART'
        cd = datetime.date(2008, 3, 6)

    class SbmDOCTYPE_DEMOBOO:
        md = datetime.date(2008, 3, 6)
        ldocname = u'Demo Book Submission (Refereed)'
        description = u'<br /><br />The Demo Book submission demonstrates a refereed submission.<br /><br />\r\nWhen the details of a book are submitted by a user, they must be approved by a referee before the record is integrated into the ATLANTIS repository.<br />\r\nApproved books are integrated into the ATLANTIS "Books" collection.<br />\r\n'
        sdocname = u'DEMOBOO'
        cd = datetime.date(2008, 3, 6)

    class SbmDOCTYPE_DEMOJRN:
        md = datetime.date(2008, 9, 18)
        ldocname = u'Demo Journal Submission'
        description = u'The Demo Journal submission submits records that will be integrated into the demo "Atlantis Times" journal.<br />\r\n Makes use of CKEditor to provide WYSIWYG HTML edition of the articles. Install it with <code>make install-ckeditor-plugin</code>.'
        sdocname = u'DEMOJRN'
        cd = datetime.date(2008, 9, 18)

    class SbmDOCTYPE_DEMOPIC:
        md = datetime.date(2007, 10, 17)
        ldocname = u'Demo Picture Submission'
        description = u'<br /><br />\r\nThe Demo Picture submission demonstrates a slightly more detailed submission type.<br />\r\nIt makes use of different categories (which in this case are used in the picture\'s reference number to better describe it) and creates icons for the submitted picture files. Records created with this submission are inserted into the ATLANTIS "Pictures" collection.\r\n<br /><br />\r\n'
        sdocname = u'DEMOPIC'
        cd = datetime.date(2007, 9, 13)

    class SbmDOCTYPE_DEMOPOE:
        md = datetime.date(2008, 3, 12)
        ldocname = u'Demo Poetry Submission'
        description = u'<br /><br />\r\nThe Demo Poetry submission demonstrates a simple submission type with a submission form split over two pages.<br />\r\nIt does not use categories. Records created with this submission are inserted into the ATLANTIS "Poetry" collection.\r\n<br /><br />'
        sdocname = u'DEMOPOE'
        cd = datetime.date(2008, 3, 12)

    class SbmDOCTYPE_DEMOTHE:
        md = datetime.date(2008, 3, 5)
        ldocname = u'Demo Thesis Submission'
        description = u'<br />\r\n<br />\r\nThe Demo Thesis submission demonstrates a very simple submission type.<br />\r\nIt has no categories, submits directly into the ATLANTIS "Theses" collection and also stamps full-text files.\r\n<br /><br />\r\n'
        sdocname = u'DEMOTHE'
        cd = datetime.date(2008, 3, 2)

    class SbmDOCTYPE_DEMOVID:
        md = datetime.date(2012, 2, 16)
        ldocname = u'Demo Video Submission'
        description = u'This is a prototype implementation of a video submission workflow. It will generate all necessary files and video formats from one file uploaded to the system.'
        sdocname = u'DEMOVID'
        cd = datetime.date(2012, 2, 16)


class SbmCOLLECTIONSbmDOCTYPEData(DataSet):

    class SbmCOLLECTIONSbmDOCTYPE_36_DEMOART:
        id_son = SbmDOCTYPEData.SbmDOCTYPE_DEMOART.ref('sdocname')
        catalogue_order = 4L
        id_father = SbmCOLLECTIONData.SbmCOLLECTION_36.ref('id')

    class SbmCOLLECTIONSbmDOCTYPE_36_DEMOBOO:
        id_son = SbmDOCTYPEData.SbmDOCTYPE_DEMOBOO.ref('sdocname')
        catalogue_order = 5L
        id_father = SbmCOLLECTIONData.SbmCOLLECTION_36.ref('id')

    class SbmCOLLECTIONSbmDOCTYPE_36_DEMOJRN:
        id_son = SbmDOCTYPEData.SbmDOCTYPE_DEMOJRN.ref('sdocname')
        catalogue_order = 6L
        id_father = SbmCOLLECTIONData.SbmCOLLECTION_36.ref('id')

    class SbmCOLLECTIONSbmDOCTYPE_36_DEMOPIC:
        id_son = SbmDOCTYPEData.SbmDOCTYPE_DEMOPIC.ref('sdocname')
        catalogue_order = 3L
        id_father = SbmCOLLECTIONData.SbmCOLLECTION_36.ref('id')

    class SbmCOLLECTIONSbmDOCTYPE_36_DEMOPOE:
        id_son = SbmDOCTYPEData.SbmDOCTYPE_DEMOPOE.ref('sdocname')
        catalogue_order = 2L
        id_father = SbmCOLLECTIONData.SbmCOLLECTION_36.ref('id')

    class SbmCOLLECTIONSbmDOCTYPE_36_DEMOTHE:
        id_son = SbmDOCTYPEData.SbmDOCTYPE_DEMOTHE.ref('sdocname')
        catalogue_order = 1L
        id_father = SbmCOLLECTIONData.SbmCOLLECTION_36.ref('id')

    class SbmCOLLECTIONSbmDOCTYPE_36_DEMOVID:
        id_son = SbmDOCTYPEData.SbmDOCTYPE_DEMOVID.ref('sdocname')
        catalogue_order = 7L
        id_father = SbmCOLLECTIONData.SbmCOLLECTION_36.ref('id')


class SbmCATEGORIESData(DataSet):

    class SbmCATEGORIES_DEMOART_ARTICLE:
        lname = u'Article'
        score = 1
        doctype = u'DEMOART'
        sname = u'ARTICLE'

    class SbmCATEGORIES_DEMOART_PREPRINT:
        lname = u'Preprint'
        score = 2
        doctype = u'DEMOART'
        sname = u'PREPRINT'

    class SbmCATEGORIES_DEMOART_REPORT:
        lname = u'Report'
        score = 3
        doctype = u'DEMOART'
        sname = u'REPORT'

    class SbmCATEGORIES_DEMOJRN_ARTS:
        lname = u'Arts'
        score = 1
        doctype = u'DEMOJRN'
        sname = u'ARTS'

    class SbmCATEGORIES_DEMOJRN_NEWS:
        lname = u'News'
        score = 2
        doctype = u'DEMOJRN'
        sname = u'NEWS'

    class SbmCATEGORIES_DEMOJRN_SCIENCE:
        lname = u'Science'
        score = 4
        doctype = u'DEMOJRN'
        sname = u'SCIENCE'

    class SbmCATEGORIES_DEMOPIC_EXP:
        lname = u'Experiments'
        score = 1
        doctype = u'DEMOPIC'
        sname = u'EXP'

    class SbmCATEGORIES_DEMOPIC_HIST:
        lname = u'Personalities and History of CERN'
        score = 2
        doctype = u'DEMOPIC'
        sname = u'HIST'

    class SbmCATEGORIES_DEMOPIC_LIFE:
        lname = u'Life at CERN'
        score = 3
        doctype = u'DEMOPIC'
        sname = u'LIFE'


class SbmFIELDData(DataSet):

    class SbmFIELD_APPDEMOBOO_1_DEMOBOOCOMNT:
        fitext = u'<br /><br />Comments on Decision:<br />\r\n'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u"Referee's Comments"
        level = u'O'
        fieldnb = 3L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOBOO_COMNT'
        fiefi2 = None
        subname = u'APPDEMOBOO'

    class SbmFIELD_APPDEMOBOO_1_DEMOBOODECSN:
        fitext = u'<br /><br /><span style="color: red;">*</span>Decision:<br />\r\n'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Decision'
        level = u'M'
        fieldnb = 2L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOBOO_DECSN'
        fiefi2 = None
        subname = u'APPDEMOBOO'

    class SbmFIELD_APPDEMOBOO_1_DEMOBOOREGB:
        fitext = u'<br /><br /></td></tr></table>'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u''
        level = u'O'
        fieldnb = 4L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOBOO_REGB'
        fiefi2 = None
        subname = u'APPDEMOBOO'

    class SbmFIELD_APPDEMOBOO_1_DEMOBOORN:
        fitext = u'<table width="100%" bgcolor="#D3E3E2" align="center" cellspacing="2" cellpadding="2" border="1"><tr><td align="left"><br /><b>Approve or reject an ATLANTIS book:</b><br /><br /><span style=\'color: red;\'>*</span>Book Reference Number:&nbsp;&nbsp;'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Reference Number'
        level = u'M'
        fieldnb = 1L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOBOO_RN'
        fiefi2 = None
        subname = u'APPDEMOBOO'

    class SbmFIELD_MBIDEMOART_1_DEMOARTCHANGE:
        fitext = u'<br /><br /><span style="color: red;">*</span>Choose the fields to be modified:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Fields to Modify'
        level = u'M'
        fieldnb = 2L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOART_CHANGE'
        fiefi2 = None
        subname = u'MBIDEMOART'

    class SbmFIELD_MBIDEMOART_1_DEMOARTCONT:
        fitext = u'<br /><br /></td></tr></table>'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u''
        level = u'O'
        fieldnb = 3L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOART_CONT'
        fiefi2 = None
        subname = u'MBIDEMOART'

    class SbmFIELD_MBIDEMOART_1_DEMOARTRN:
        fitext = u'<table width="100%" bgcolor="#D3E3E2" align="center" cellspacing="2" cellpadding="2" border="1"><tr><td align="left"><br /><b>Modify an article\'s bibliographic information:</b><br /><br /><span style=\'color: red;\'>*</span>Document Reference Number:&nbsp;&nbsp;'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Reference Number'
        level = u'M'
        fieldnb = 1L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOART_RN'
        fiefi2 = None
        subname = u'MBIDEMOART'

    class SbmFIELD_MBIDEMOBOO_1_DEMOBOOCHANGE:
        fitext = u'<br /><br /><span style="color: red;">*</span>Choose the fields to be modified:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Fields to Modify'
        level = u'M'
        fieldnb = 2L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOBOO_CHANGE'
        fiefi2 = None
        subname = u'MBIDEMOBOO'

    class SbmFIELD_MBIDEMOBOO_1_DEMOBOOCONT:
        fitext = u'<br /><br /></td></tr></table>'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u''
        level = u'O'
        fieldnb = 3L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOBOO_CONT'
        fiefi2 = None
        subname = u'MBIDEMOBOO'

    class SbmFIELD_MBIDEMOBOO_1_DEMOBOORN:
        fitext = u'<table width="100%" bgcolor="#D3E3E2" align="center" cellspacing="2" cellpadding="2" border="1"><tr><td align="left"><br /><b>Modify a book\'s bibliographic information:</b><br /><br /><span style=\'color: red;\'>*</span>Book Reference Number:&nbsp;&nbsp;'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Reference Number'
        level = u'M'
        fieldnb = 1L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOBOO_RN'
        fiefi2 = None
        subname = u'MBIDEMOBOO'

    class SbmFIELD_MBIDEMOJRN_1_DEMOJRNCHANGE:
        fitext = u''
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2009, 1, 9)
        sdesc = u''
        level = u'O'
        fieldnb = 2L
        cd = datetime.date(2009, 1, 9)
        fidesc = u'DEMOJRN_CHANGE'
        fiefi2 = None
        subname = u'MBIDEMOJRN'

    class SbmFIELD_MBIDEMOJRN_1_DEMOJRNCONT:
        fitext = u'<br /><br /></td></tr></table>'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2009, 1, 9)
        sdesc = u''
        level = u'O'
        fieldnb = 3L
        cd = datetime.date(2008, 10, 6)
        fidesc = u'DEMOJRN_CONT'
        fiefi2 = None
        subname = u'MBIDEMOJRN'

    class SbmFIELD_MBIDEMOJRN_1_DEMOJRNRN:
        fitext = u'<table width="100%" bgcolor="#D3E3E2" align="center" cellspacing="2" cellpadding="2" border="1"><tr><td align="left"><br /><b>Update a journal article:</b><br /><br /><span style=\'color: red;\'>*</span>Document Reference Number:&nbsp;&nbsp;'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 10, 6)
        sdesc = u''
        level = u'M'
        fieldnb = 1L
        cd = datetime.date(2008, 10, 6)
        fidesc = u'DEMOJRN_RN'
        fiefi2 = None
        subname = u'MBIDEMOJRN'

    class SbmFIELD_MBIDEMOPIC_1_DEMOPICCHANGE:
        fitext = u'<br /><br /><span style="color: red;">*</span>Choose the fields to be modified:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2007, 10, 4)
        sdesc = u'Fields to Modify'
        level = u'M'
        fieldnb = 2L
        cd = datetime.date(2007, 10, 4)
        fidesc = u'DEMOPIC_CHANGE'
        fiefi2 = None
        subname = u'MBIDEMOPIC'

    class SbmFIELD_MBIDEMOPIC_1_DEMOPICCONT:
        fitext = u'<br /><br /></td></tr></table>'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2007, 10, 4)
        sdesc = u''
        level = u'O'
        fieldnb = 3L
        cd = datetime.date(2007, 10, 4)
        fidesc = u'DEMOPIC_CONT'
        fiefi2 = None
        subname = u'MBIDEMOPIC'

    class SbmFIELD_MBIDEMOPIC_1_DEMOPICRN:
        fitext = u'<table width="100%" bgcolor="#D3E3E2" align="center" cellspacing="2" cellpadding="2" border="1"><tr><td align="left"><br /><b>Modify a picture\'s bibliographic information:</b><br /><br /><span style=\'color: red;\'>*</span>Picture Reference Number:&nbsp;&nbsp;'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2007, 10, 4)
        sdesc = u'Reference Number'
        level = u'M'
        fieldnb = 1L
        cd = datetime.date(2007, 10, 4)
        fidesc = u'DEMOPIC_RN'
        fiefi2 = None
        subname = u'MBIDEMOPIC'

    class SbmFIELD_MBIDEMOPOE_1_DEMOPOECHANGE:
        fitext = u'<br /><br /><span style="color: red;">*</span>Choose the fields to be modified:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 12)
        sdesc = u'Fields to Modify'
        level = u'M'
        fieldnb = 2L
        cd = datetime.date(2008, 3, 12)
        fidesc = u'DEMOPOE_CHANGE'
        fiefi2 = None
        subname = u'MBIDEMOPOE'

    class SbmFIELD_MBIDEMOPOE_1_DEMOPOECONT:
        fitext = u'<br /><br /></td></tr></table>'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 12)
        sdesc = u''
        level = u'O'
        fieldnb = 3L
        cd = datetime.date(2008, 3, 12)
        fidesc = u'DEMOPOE_CONT'
        fiefi2 = None
        subname = u'MBIDEMOPOE'

    class SbmFIELD_MBIDEMOPOE_1_DEMOPOERN:
        fitext = u'<table width="100%" bgcolor="#D3E3E2" align="center" cellspacing="2" cellpadding="2" border="1"><tr><td align="left"><br /><b>Modify a poem\'s bibliographic information:</b><br /><br /><span style=\'color: red;\'>*</span>Poem Reference Number:&nbsp;&nbsp;'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 12)
        sdesc = u'Reference Number'
        level = u'M'
        fieldnb = 1L
        cd = datetime.date(2008, 3, 12)
        fidesc = u'DEMOPOE_RN'
        fiefi2 = None
        subname = u'MBIDEMOPOE'

    class SbmFIELD_MBIDEMOTHE_1_DEMOTHECHANGE:
        fitext = u'<br /><br /><span style="color: red;">*</span>Choose the fields to be modified:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 5)
        sdesc = u'Fields to Modify'
        level = u'M'
        fieldnb = 2L
        cd = datetime.date(2008, 3, 5)
        fidesc = u'DEMOTHE_CHANGE'
        fiefi2 = None
        subname = u'MBIDEMOTHE'

    class SbmFIELD_MBIDEMOTHE_1_DEMOTHECONT:
        fitext = u'<br /><br /></td></tr></table>'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 5)
        sdesc = u''
        level = u'O'
        fieldnb = 3L
        cd = datetime.date(2008, 3, 5)
        fidesc = u'DEMOTHE_CONT'
        fiefi2 = None
        subname = u'MBIDEMOTHE'

    class SbmFIELD_MBIDEMOTHE_1_DEMOTHERN:
        fitext = u'<table width="100%" bgcolor="#D3E3E2" align="center" cellspacing="2" cellpadding="2" border="1"><tr><td align="left"><br /><b>Modify a thesis\' bibliographic information:</b><br /><br /><span style=\'color: red;\'>*</span>Thesis Reference Number:&nbsp;&nbsp;'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 5)
        sdesc = u'Reference Number'
        level = u'M'
        fieldnb = 1L
        cd = datetime.date(2008, 3, 5)
        fidesc = u'DEMOTHE_RN'
        fiefi2 = None
        subname = u'MBIDEMOTHE'

    class SbmFIELD_SBIDEMOART_1_DEMOARTABS:
        fitext = u'</td></tr></table><br /><span style="color: red;">*</span>Abstract:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Abstract'
        level = u'M'
        fieldnb = 4L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOART_ABS'
        fiefi2 = None
        subname = u'SBIDEMOART'

    class SbmFIELD_SBIDEMOART_1_DEMOARTAU:
        fitext = u'<br /><br /><table width="100%"><tr><td valign="top"><span style="color: red;">*</span>Author of the Document: <i>(one per line)</i><br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Author(s)'
        level = u'M'
        fieldnb = 3L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOART_AU'
        fiefi2 = None
        subname = u'SBIDEMOART'

    class SbmFIELD_SBIDEMOART_1_DEMOARTDATE:
        fitext = u'<br /><br /><span style="color: red;">*</span>Date of Document: <i>(dd/mm/yyyy)</i>&nbsp;'
        checkn = u'DatCheckNew'
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Date of Document'
        level = u'M'
        fieldnb = 7L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOART_DATE'
        fiefi2 = None
        subname = u'SBIDEMOART'

    class SbmFIELD_SBIDEMOART_1_DEMOARTEND:
        fitext = u'<br /><br /></td></tr></table><br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u''
        level = u'O'
        fieldnb = 11L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOART_END'
        fiefi2 = None
        subname = u'SBIDEMOART'

    class SbmFIELD_SBIDEMOART_1_DEMOARTFILE:
        fitext = u'<br><br><span style="color: red;">*</span>Enter the full path to the source file to upload:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Source File'
        level = u'M'
        fieldnb = 10L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOART_FILE'
        fiefi2 = None
        subname = u'SBIDEMOART'

    class SbmFIELD_SBIDEMOART_1_DEMOARTKW:
        fitext = u'<br /><br />Keywords/Key-phrases: <i>(one per line)</i><br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Keywords/Key-phrases'
        level = u'O'
        fieldnb = 8L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOART_KW'
        fiefi2 = None
        subname = u'SBIDEMOART'

    class SbmFIELD_SBIDEMOART_1_DEMOARTLANG:
        fitext = u'<br /><br /><span style="color: red;">*</span>Language:&nbsp;'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Language'
        level = u'O'
        fieldnb = 6L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOART_LANG'
        fiefi2 = None
        subname = u'SBIDEMOART'

    class SbmFIELD_SBIDEMOART_1_DEMOARTNOTE:
        fitext = u'<br /><br />Additional Notes or Comments:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Notes/Comments'
        level = u'O'
        fieldnb = 9L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOART_NOTE'
        fiefi2 = None
        subname = u'SBIDEMOART'

    class SbmFIELD_SBIDEMOART_1_DEMOARTNUMP:
        fitext = u'<br /><br />Number of Pages:&nbsp;'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Number of Pages'
        level = u'O'
        fieldnb = 5L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOART_NUMP'
        fiefi2 = None
        subname = u'SBIDEMOART'

    class SbmFIELD_SBIDEMOART_1_DEMOARTREP:
        fitext = u'<TABLE WIDTH="100%" BGCOLOR="#D3E3E2" ALIGN="center" CELLSPACING="2" CELLPADDING="2" BORDER="1"><TR><TD ALIGN="left"><br /><b>Submit an ATLANTIS Article:</b><br /><br />Your document will be given a reference number automatically.<br /> However, if it has other reference numbers, please enter them here:<br /><i>(one per line)</i><br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Other Report Numbers'
        level = u'O'
        fieldnb = 1L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOART_REP'
        fiefi2 = None
        subname = u'SBIDEMOART'

    class SbmFIELD_SBIDEMOART_1_DEMOARTTITLE:
        fitext = u'<br /><br /><span style="color: red;">*</span>Document Title:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Title'
        level = u'M'
        fieldnb = 2L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOART_TITLE'
        fiefi2 = None
        subname = u'SBIDEMOART'

    class SbmFIELD_SBIDEMOBOO_1_DEMOBOOABS:
        fitext = u'</td></tr></table><br /><span style="color: red;">*</span>Abstract:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Abstract'
        level = u'M'
        fieldnb = 4L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOBOO_ABS'
        fiefi2 = None
        subname = u'SBIDEMOBOO'

    class SbmFIELD_SBIDEMOBOO_1_DEMOBOOAU:
        fitext = u'<br /><br /><table width="100%"><tr><td valign="top"><span style="color: red;">*</span>Author of the Book: <i>(one per line)</i><br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Author(s)'
        level = u'M'
        fieldnb = 3L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOBOO_AU'
        fiefi2 = None
        subname = u'SBIDEMOBOO'

    class SbmFIELD_SBIDEMOBOO_1_DEMOBOODATE:
        fitext = u'<br /><br /><span style="color: red;">*</span>Date of the Book: <i>(dd/mm/yyyy)</i>&nbsp;'
        checkn = u'DatCheckNew'
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Date of Document'
        level = u'M'
        fieldnb = 7L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOBOO_DATE'
        fiefi2 = None
        subname = u'SBIDEMOBOO'

    class SbmFIELD_SBIDEMOBOO_1_DEMOBOOEND:
        fitext = u'<br /><br /></td></tr></table><br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u''
        level = u'O'
        fieldnb = 11L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOBOO_END'
        fiefi2 = None
        subname = u'SBIDEMOBOO'

    class SbmFIELD_SBIDEMOBOO_1_DEMOBOOFILE:
        fitext = u'<br><br>Enter the full path to the source file to upload:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Source File'
        level = u'O'
        fieldnb = 10L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOBOO_FILE'
        fiefi2 = None
        subname = u'SBIDEMOBOO'

    class SbmFIELD_SBIDEMOBOO_1_DEMOBOOKW:
        fitext = u'<br /><br />Keywords/Key-phrases: <i>(one per line)</i><br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Keywords/Key-phrases'
        level = u'O'
        fieldnb = 8L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOBOO_KW'
        fiefi2 = None
        subname = u'SBIDEMOBOO'

    class SbmFIELD_SBIDEMOBOO_1_DEMOBOOLANG:
        fitext = u'<br /><br /><span style="color: red;">*</span>Language:&nbsp;'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Language'
        level = u'O'
        fieldnb = 6L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOBOO_LANG'
        fiefi2 = None
        subname = u'SBIDEMOBOO'

    class SbmFIELD_SBIDEMOBOO_1_DEMOBOONOTE:
        fitext = u'<br /><br />Additional Notes or Comments:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Notes/Comments'
        level = u'O'
        fieldnb = 9L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOBOO_NOTE'
        fiefi2 = None
        subname = u'SBIDEMOBOO'

    class SbmFIELD_SBIDEMOBOO_1_DEMOBOONUMP:
        fitext = u'<br /><br />Number of Pages:&nbsp;'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Number of Pages'
        level = u'O'
        fieldnb = 5L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOBOO_NUMP'
        fiefi2 = None
        subname = u'SBIDEMOBOO'

    class SbmFIELD_SBIDEMOBOO_1_DEMOBOOREP:
        fitext = u'<TABLE WIDTH="100%" BGCOLOR="#D3E3E2" ALIGN="center" CELLSPACING="2" CELLPADDING="2" BORDER="1"><TR><TD ALIGN="left"><br /><b>Submit an ATLANTIS Book:</b><br /><br />Your book will be given a reference number automatically.<br /> However, if it has other reference numbers, please enter them here:<br /><i>(one per line)</i><br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Other Report Numbers'
        level = u'O'
        fieldnb = 1L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOBOO_REP'
        fiefi2 = None
        subname = u'SBIDEMOBOO'

    class SbmFIELD_SBIDEMOBOO_1_DEMOBOOTITLE:
        fitext = u'<br /><br /><span style="color: red;">*</span>Book Title:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 7)
        sdesc = u'Title'
        level = u'M'
        fieldnb = 2L
        cd = datetime.date(2008, 3, 7)
        fidesc = u'DEMOBOO_TITLE'
        fiefi2 = None
        subname = u'SBIDEMOBOO'

    class SbmFIELD_SBIDEMOJRN_1_DEMOJRNABSE:
        fitext = u'</td></tr><tr><td><br />English article:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2009, 1, 9)
        sdesc = u'English article:'
        level = u'O'
        fieldnb = 8L
        cd = datetime.date(2008, 11, 4)
        fidesc = u'DEMOJRN_ABSE'
        fiefi2 = None
        subname = u'SBIDEMOJRN'

    class SbmFIELD_SBIDEMOJRN_1_DEMOJRNABSF:
        fitext = u'</td><td><br />French article:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2009, 1, 9)
        sdesc = u'French article:'
        level = u'O'
        fieldnb = 9L
        cd = datetime.date(2008, 9, 26)
        fidesc = u'DEMOJRN_ABSF'
        fiefi2 = None
        subname = u'SBIDEMOJRN'

    class SbmFIELD_SBIDEMOJRN_1_DEMOJRNAU:
        fitext = u'</td></TR><TR><TD><br /><br />Author(s): <i>(one per line)</i><br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2009, 2, 20)
        sdesc = u'Author(s)'
        level = u'O'
        fieldnb = 4L
        cd = datetime.date(2008, 9, 26)
        fidesc = u'DEMOJRN_AU'
        fiefi2 = None
        subname = u'SBIDEMOJRN'

    class SbmFIELD_SBIDEMOJRN_1_DEMOJRNCATEG:
        fitext = u''
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2009, 10, 15)
        sdesc = u'comboDEMOJRN-like for MBI'
        level = u'O'
        fieldnb = 14L
        cd = datetime.date(2009, 10, 15)
        fidesc = u'DEMOJRN_CATEG'
        fiefi2 = None
        subname = u'SBIDEMOJRN'

    class SbmFIELD_SBIDEMOJRN_1_DEMOJRNEMAIL:
        fitext = u'</TD><TD><br /><br />E-mail(s) of the author(s): <i>(one per line)</i><br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2009, 1, 9)
        sdesc = u'E-mail of the author(s): <i>(one per line)</i>'
        level = u'O'
        fieldnb = 5L
        cd = datetime.date(2008, 9, 26)
        fidesc = u'DEMOJRN_EMAIL'
        fiefi2 = None
        subname = u'SBIDEMOJRN'

    class SbmFIELD_SBIDEMOJRN_1_DEMOJRNEND:
        fitext = u'</td></tr><tr><td colspan="2">'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2009, 2, 20)
        sdesc = u''
        level = u'O'
        fieldnb = 12L
        cd = datetime.date(2008, 9, 26)
        fidesc = u'DEMOJRN_END'
        fiefi2 = None
        subname = u'SBIDEMOJRN'

    class SbmFIELD_SBIDEMOJRN_1_DEMOJRNENDING:
        fitext = u'</td></tr></table>'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2009, 2, 20)
        sdesc = u''
        level = u'O'
        fieldnb = 13L
        cd = datetime.date(2009, 2, 20)
        fidesc = u'DEMOJRN_ENDING'
        fiefi2 = None
        subname = u'SBIDEMOJRN'

    class SbmFIELD_SBIDEMOJRN_1_DEMOJRNIN:
        fitext = u''
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2009, 2, 6)
        sdesc = u'Journal Name'
        level = u'O'
        fieldnb = 10L
        cd = datetime.date(2008, 9, 26)
        fidesc = u'DEMOJRN_IN'
        fiefi2 = None
        subname = u'SBIDEMOJRN'

    class SbmFIELD_SBIDEMOJRN_1_DEMOJRNISSUES:
        fitext = u'</TD><TD align="center"><span style="color: red;">*</span>Order(s) <small><i>(digit)</i></small> and issue(s) <small><i>(xx/YYYY)</i></small> of the article:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2009, 2, 20)
        sdesc = u'Order and issue numbers'
        level = u'O'
        fieldnb = 3L
        cd = datetime.date(2009, 2, 20)
        fidesc = u'DEMOJRN_ISSUES'
        fiefi2 = None
        subname = u'SBIDEMOJRN'

    class SbmFIELD_SBIDEMOJRN_1_DEMOJRNTITLEE:
        fitext = u'</TD></TR><TR><TD><br /><br />English title:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2009, 1, 9)
        sdesc = u'English title:'
        level = u'O'
        fieldnb = 6L
        cd = datetime.date(2008, 9, 26)
        fidesc = u'DEMOJRN_TITLEE'
        fiefi2 = None
        subname = u'SBIDEMOJRN'

    class SbmFIELD_SBIDEMOJRN_1_DEMOJRNTITLEF:
        fitext = u'</TD><TD><br /><br />French title:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2009, 1, 9)
        sdesc = u'French title:'
        level = u'O'
        fieldnb = 7L
        cd = datetime.date(2008, 9, 26)
        fidesc = u'DEMOJRN_TITLEF'
        fiefi2 = None
        subname = u'SBIDEMOJRN'

    class SbmFIELD_SBIDEMOJRN_1_DEMOJRNTYPE:
        fitext = u'<TABLE WIDTH="100%" BGCOLOR="#D3E3E2" ALIGN="center" CELLSPACING="2" CELLPADDING="2" BORDER="1"><TR><TD ALIGN="left" colspan="2"><br /><b>Submit an Atlantis Times article:</b></TD></TR><TR><TD align="center"><span style="color: red;">*</span>Status:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2009, 2, 20)
        sdesc = u'Status:'
        level = u'O'
        fieldnb = 2L
        cd = datetime.date(2009, 2, 20)
        fidesc = u'DEMOJRN_TYPE'
        fiefi2 = None
        subname = u'SBIDEMOJRN'

    class SbmFIELD_SBIDEMOPIC_1_DEMOPICADDRN:
        fitext = u'<br /><br />Your picture will be given a reference number automatically.<br /> However, if the picture has other reference numbers, please enter them here:<br /><i>(one per line)</i><br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2007, 9, 13)
        sdesc = u'Additional Reference Numbers'
        level = u'O'
        fieldnb = 6L
        cd = datetime.date(2007, 9, 13)
        fidesc = u'DEMOPIC_ADD_RN'
        fiefi2 = None
        subname = u'SBIDEMOPIC'

    class SbmFIELD_SBIDEMOPIC_1_DEMOPICDATE:
        fitext = u'<br /><br /><span style="color: red;">*</span>Picture Date: <i>(dd/mm/yyyy)</i>&nbsp;'
        checkn = u'DatCheckNew'
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2007, 10, 4)
        sdesc = u'Picture Date'
        level = u'M'
        fieldnb = 3L
        cd = datetime.date(2007, 9, 13)
        fidesc = u'DEMOPIC_DATE'
        fiefi2 = None
        subname = u'SBIDEMOPIC'

    class SbmFIELD_SBIDEMOPIC_1_DEMOPICDESCR:
        fitext = u'<br /><br />Picture Description:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2007, 9, 13)
        sdesc = u'Picture Description'
        level = u'O'
        fieldnb = 5L
        cd = datetime.date(2007, 9, 13)
        fidesc = u'DEMOPIC_DESCR'
        fiefi2 = None
        subname = u'SBIDEMOPIC'

    class SbmFIELD_SBIDEMOPIC_1_DEMOPICFINISH:
        fitext = u'<br /><br /></td></tr></table>'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2007, 9, 13)
        sdesc = u''
        level = u'O'
        fieldnb = 9L
        cd = datetime.date(2007, 9, 13)
        fidesc = u'DEMOPIC_FINISH'
        fiefi2 = None
        subname = u'SBIDEMOPIC'

    class SbmFIELD_SBIDEMOPIC_1_DEMOPICKW:
        fitext = u'<br /><br />Keywords:<br /><i>(one keyword/key-phrase per line)</i><br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2007, 9, 13)
        sdesc = u'Picture Keywords'
        level = u'O'
        fieldnb = 4L
        cd = datetime.date(2007, 9, 13)
        fidesc = u'DEMOPIC_KW'
        fiefi2 = None
        subname = u'SBIDEMOPIC'

    class SbmFIELD_SBIDEMOPIC_1_DEMOPICNOTE:
        fitext = u'<br /><br />Additional Comments or Notes about the Picture:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2007, 9, 13)
        sdesc = u'Picture Notes or Comments'
        level = u'O'
        fieldnb = 7L
        cd = datetime.date(2007, 9, 13)
        fidesc = u'DEMOPIC_NOTE'
        fiefi2 = None
        subname = u'SBIDEMOPIC'

    class SbmFIELD_SBIDEMOPIC_1_DEMOPICPHOTOG:
        fitext = u'<br /><br />Picture Author(s) or Photographers(s): <i>(one per line)</i><br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2007, 9, 13)
        sdesc = u'Photographer(s)'
        level = u'O'
        fieldnb = 2L
        cd = datetime.date(2007, 9, 13)
        fidesc = u'DEMOPIC_PHOTOG'
        fiefi2 = None
        subname = u'SBIDEMOPIC'

    class SbmFIELD_SBIDEMOPIC_1_DEMOPICTITLE:
        fitext = u'<table width="100%" bgcolor="#D3E3E2" align="center" cellspacing="2" cellpadding="2" border="1"><tr><td align="left"><br /><b>Submit an ATLANTIS picture:</b><br /><br /><span style="color: red;">*</span>Picture Title:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2007, 10, 4)
        sdesc = u'Picture Title'
        level = u'M'
        fieldnb = 1L
        cd = datetime.date(2007, 9, 13)
        fidesc = u'DEMOPIC_TITLE'
        fiefi2 = None
        subname = u'SBIDEMOPIC'

    class SbmFIELD_SBIDEMOPIC_1_UploadPhotos:
        fitext = u'<br /><br />Select the photo(s) to upload:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2007, 9, 13)
        sdesc = u'Picture File'
        level = u'O'
        fieldnb = 8L
        cd = datetime.date(2007, 9, 13)
        fidesc = u'Upload_Photos'
        fiefi2 = None
        subname = u'SBIDEMOPIC'

    class SbmFIELD_SBIDEMOPOE_1_DEMOPOEAU:
        fitext = u'<br /><br /><span style="color: red;">*</span>Author(s) of the Poem: <i>(one per line)</i><br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 12)
        sdesc = u'Author(s)'
        level = u'M'
        fieldnb = 2L
        cd = datetime.date(2008, 3, 12)
        fidesc = u'DEMOPOE_AU'
        fiefi2 = None
        subname = u'SBIDEMOPOE'

    class SbmFIELD_SBIDEMOPOE_1_DEMOPOEDUMMY:
        fitext = u''
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 12)
        sdesc = u''
        level = u'O'
        fieldnb = 5L
        cd = datetime.date(2008, 3, 12)
        fidesc = u'DEMOPOE_DUMMY'
        fiefi2 = None
        subname = u'SBIDEMOPOE'

    class SbmFIELD_SBIDEMOPOE_1_DEMOPOELANG:
        fitext = u'<br /><br /><table width="100%"><tr><td valign="top"><span style="color: red;">*</span>Poem Language:&nbsp;'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 12)
        sdesc = u'Language'
        level = u'M'
        fieldnb = 3L
        cd = datetime.date(2008, 3, 12)
        fidesc = u'DEMOPOE_LANG'
        fiefi2 = None
        subname = u'SBIDEMOPOE'

    class SbmFIELD_SBIDEMOPOE_1_DEMOPOETITLE:
        fitext = u'<TABLE WIDTH="100%" BGCOLOR="#D3E3E2" ALIGN="center" CELLSPACING="2" CELLPADDING="2" BORDER="1"><TR><TD ALIGN="left"><br /><b>Submit an ATLANTIS Poem:</b><br /><br /><span style="color: red;">*</span>Poem Title:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 12)
        sdesc = u'>Title'
        level = u'M'
        fieldnb = 1L
        cd = datetime.date(2008, 3, 12)
        fidesc = u'DEMOPOE_TITLE'
        fiefi2 = None
        subname = u'SBIDEMOPOE'

    class SbmFIELD_SBIDEMOPOE_1_DEMOPOEYEAR:
        fitext = u'</td><td><span style="color: red;">*</span>Year of the Poem:&nbsp;'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 12)
        sdesc = u'Poem Year'
        level = u'M'
        fieldnb = 4L
        cd = datetime.date(2008, 3, 12)
        fidesc = u'DEMOPOE_YEAR'
        fiefi2 = None
        subname = u'SBIDEMOPOE'

    class SbmFIELD_SBIDEMOPOE_2_DEMOPOEABS:
        fitext = u'<TABLE WIDTH="100%" BGCOLOR="#D3E3E2" ALIGN="center" CELLSPACING="2" CELLPADDING="2" BORDER="1"><TR><TD ALIGN="left"><br /><br /><span style="color: red;">*</span>Poem Text:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 2L
        md = datetime.date(2008, 3, 12)
        sdesc = u'Abstract'
        level = u'M'
        fieldnb = 1L
        cd = datetime.date(2008, 3, 12)
        fidesc = u'DEMOPOE_ABS'
        fiefi2 = None
        subname = u'SBIDEMOPOE'

    class SbmFIELD_SBIDEMOPOE_2_DEMOPOEEND:
        fitext = u'<br /><br /></td></tr></table><br />'
        checkn = u''
        fiefi1 = None
        pagenb = 2L
        md = datetime.date(2008, 3, 12)
        sdesc = u''
        level = u'O'
        fieldnb = 2L
        cd = datetime.date(2008, 3, 12)
        fidesc = u'DEMOPOE_END'
        fiefi2 = None
        subname = u'SBIDEMOPOE'

    class SbmFIELD_SBIDEMOTHE_1_DEMOTHEABS:
        fitext = u'</td></tr></table><br /><span style="color: red;">*</span>Abstract:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 6)
        sdesc = u'Abstract'
        level = u'M'
        fieldnb = 6L
        cd = datetime.date(2008, 3, 2)
        fidesc = u'DEMOTHE_ABS'
        fiefi2 = None
        subname = u'SBIDEMOTHE'

    class SbmFIELD_SBIDEMOTHE_1_DEMOTHEAU:
        fitext = u'<br /><br /><table width="100%"><tr><td valign="top"><span style="color: red;">*</span>Author of the Thesis: <i>(one per line)</i><br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 6)
        sdesc = u'Author(s)'
        level = u'M'
        fieldnb = 4L
        cd = datetime.date(2008, 3, 2)
        fidesc = u'DEMOTHE_AU'
        fiefi2 = None
        subname = u'SBIDEMOTHE'

    class SbmFIELD_SBIDEMOTHE_1_DEMOTHEDATE:
        fitext = u'<br /><br /><span style="color: red;">*</span>Thesis Defence date <i>(dd/mm/yyyy)</i>:&nbsp;'
        checkn = u'DatCheckNew'
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 6)
        sdesc = u'Date of Thesis Defence'
        level = u'M'
        fieldnb = 12L
        cd = datetime.date(2008, 3, 2)
        fidesc = u'DEMOTHE_DATE'
        fiefi2 = None
        subname = u'SBIDEMOTHE'

    class SbmFIELD_SBIDEMOTHE_1_DEMOTHEDIPL:
        fitext = u'<br /><br /><span style="color: red;">*</span>Diploma Awarded:&nbsp;'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 6)
        sdesc = u'Diploma Awarded'
        level = u'M'
        fieldnb = 11L
        cd = datetime.date(2008, 3, 2)
        fidesc = u'DEMOTHE_DIPL'
        fiefi2 = None
        subname = u'SBIDEMOTHE'

    class SbmFIELD_SBIDEMOTHE_1_DEMOTHEEND:
        fitext = u'<br /><br /></td></tr></table><br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 2)
        sdesc = u''
        level = u'O'
        fieldnb = 16L
        cd = datetime.date(2008, 3, 2)
        fidesc = u'DEMOTHE_END'
        fiefi2 = None
        subname = u'SBIDEMOTHE'

    class SbmFIELD_SBIDEMOTHE_1_DEMOTHEFILE:
        fitext = u'<br><br><span style="color: red;">*</span>Enter the full path to the source file to upload:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 6)
        sdesc = u'Source File'
        level = u'M'
        fieldnb = 15L
        cd = datetime.date(2008, 3, 2)
        fidesc = u'DEMOTHE_FILE'
        fiefi2 = None
        subname = u'SBIDEMOTHE'

    class SbmFIELD_SBIDEMOTHE_1_DEMOTHELANG:
        fitext = u'<br><br><span style="color: red;">*</span>Language: '
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 6)
        sdesc = u'Thesis Language'
        level = u'M'
        fieldnb = 8L
        cd = datetime.date(2008, 3, 2)
        fidesc = u'DEMOTHE_LANG'
        fiefi2 = None
        subname = u'SBIDEMOTHE'

    class SbmFIELD_SBIDEMOTHE_1_DEMOTHENUMP:
        fitext = u'<br /><br />Number of Pages: '
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 6)
        sdesc = u'Number of Pages'
        level = u'O'
        fieldnb = 7L
        cd = datetime.date(2008, 3, 2)
        fidesc = u'DEMOTHE_NUMP'
        fiefi2 = None
        subname = u'SBIDEMOTHE'

    class SbmFIELD_SBIDEMOTHE_1_DEMOTHEPLACE:
        fitext = u'&nbsp;at <span style="color: red;">*</span>Place/Town:&nbsp;'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 6)
        sdesc = u'Awarding University town'
        level = u'M'
        fieldnb = 14L
        cd = datetime.date(2008, 3, 2)
        fidesc = u'DEMOTHE_PLACE'
        fiefi2 = None
        subname = u'SBIDEMOTHE'

    class SbmFIELD_SBIDEMOTHE_1_DEMOTHEPLDEF:
        fitext = u'&nbsp;at <span style="color: red;">*</span>Place/Town:&nbsp;'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 6)
        sdesc = u'Place of Thesis Defence'
        level = u'M'
        fieldnb = 10L
        cd = datetime.date(2008, 3, 2)
        fidesc = u'DEMOTHE_PLDEF'
        fiefi2 = None
        subname = u'SBIDEMOTHE'

    class SbmFIELD_SBIDEMOTHE_1_DEMOTHEPUBL:
        fitext = u'<br /><br /><span style="color: red;">*</span>Thesis Publisher (or Institute):&nbsp;'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 6)
        sdesc = u'Thesis Publisher/University'
        level = u'M'
        fieldnb = 9L
        cd = datetime.date(2008, 3, 2)
        fidesc = u'DEMOTHE_PUBL'
        fiefi2 = None
        subname = u'SBIDEMOTHE'

    class SbmFIELD_SBIDEMOTHE_1_DEMOTHEREP:
        fitext = u'<TABLE WIDTH="100%" BGCOLOR="#D3E3E2" ALIGN="center" CELLSPACING="2" CELLPADDING="2" BORDER="1"><TR><TD ALIGN="left"><br /><b>Submit an ATLANTIS Thesis:</b><br /><br />Your thesis will be given a reference number automatically.<br /> However, if it has other reference numbers, please enter them here:<br /><i>(one per line)</i><br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 6)
        sdesc = u'Other Report Numbers'
        level = u'O'
        fieldnb = 1L
        cd = datetime.date(2008, 3, 2)
        fidesc = u'DEMOTHE_REP'
        fiefi2 = None
        subname = u'SBIDEMOTHE'

    class SbmFIELD_SBIDEMOTHE_1_DEMOTHESUBTTL:
        fitext = u'<br /><br />Thesis Subtitle <i>(if any)</i>:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 6)
        sdesc = u'Subtitle'
        level = u'O'
        fieldnb = 3L
        cd = datetime.date(2008, 3, 2)
        fidesc = u'DEMOTHE_SUBTTL'
        fiefi2 = None
        subname = u'SBIDEMOTHE'

    class SbmFIELD_SBIDEMOTHE_1_DEMOTHESUPERV:
        fitext = u'</td></tr><tr><td valign="top"><br>Thesis Supervisor(s): <i>(one per line)</i><br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 6)
        sdesc = u'Thesis Supervisor(s)'
        level = u'O'
        fieldnb = 5L
        cd = datetime.date(2008, 3, 2)
        fidesc = u'DEMOTHE_SUPERV'
        fiefi2 = None
        subname = u'SBIDEMOTHE'

    class SbmFIELD_SBIDEMOTHE_1_DEMOTHETITLE:
        fitext = u'<br /><br /><span style="color: red;">*</span>Thesis Title:<br />'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 6)
        sdesc = u'Title'
        level = u'M'
        fieldnb = 2L
        cd = datetime.date(2008, 3, 2)
        fidesc = u'DEMOTHE_TITLE'
        fiefi2 = None
        subname = u'SBIDEMOTHE'

    class SbmFIELD_SBIDEMOTHE_1_DEMOTHEUNIV:
        fitext = u'<br /><span style="color: red;">*</span>Awarding University:&nbsp;'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2008, 3, 6)
        sdesc = u'Awarding University'
        level = u'M'
        fieldnb = 13L
        cd = datetime.date(2008, 3, 2)
        fidesc = u'DEMOTHE_UNIV'
        fiefi2 = None
        subname = u'SBIDEMOTHE'

    class SbmFIELD_SBIDEMOVID_1_DEMOVIDSINGLE:
        fitext = u''
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2012, 2, 16)
        sdesc = u''
        level = u'O'
        fieldnb = 1L
        cd = datetime.date(2012, 2, 16)
        fidesc = u'DEMOVID_SINGLE'
        fiefi2 = None
        subname = u'SBIDEMOVID'

    class SbmFIELD_SBIDEMOVID_1_DEMOVIDSUBMIT:
        fitext = u''
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2012, 2, 16)
        sdesc = u''
        level = u'O'
        fieldnb = 2L
        cd = datetime.date(2012, 2, 16)
        fidesc = u'DEMOVID_SUBMIT'
        fiefi2 = None
        subname = u'SBIDEMOVID'

    class SbmFIELD_SRVDEMOPIC_1_DEMOPICCONT:
        fitext = u'<br /><br /></td></tr></table>'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2009, 4, 9)
        sdesc = u''
        level = u'O'
        fieldnb = 2L
        cd = datetime.date(2009, 4, 9)
        fidesc = u'DEMOPIC_CONT'
        fiefi2 = None
        subname = u'SRVDEMOPIC'

    class SbmFIELD_SRVDEMOPIC_1_DEMOPICRN:
        fitext = u'<table width="100%" bgcolor="#D3E3E2" align="center" cellspacing="2" cellpadding="2" border="1"><tr><td align="left"><br /><b> Revise/add pictures:</b><br /><br /><span style=\'color: red;\'>*</span>Picture Reference Number:&nbsp;&nbsp;'
        checkn = u''
        fiefi1 = None
        pagenb = 1L
        md = datetime.date(2009, 4, 9)
        sdesc = u'Reference Number'
        level = u'M'
        fieldnb = 1L
        cd = datetime.date(2009, 4, 9)
        fidesc = u'DEMOPIC_RN'
        fiefi2 = None
        subname = u'SRVDEMOPIC'


class SbmFIELDDESCData(DataSet):

    class SbmFIELDDESC_DEMOARTABS:
        md = datetime.date(2008, 3, 7)
        rows = 12L
        name = u'DEMOART_ABS'
        val = None
        marccode = u'520__a'
        fddfi2 = None
        cols = 80L
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br />Abstract:<br />'

    class SbmFIELDDESC_DEMOARTAU:
        md = datetime.date(2008, 3, 7)
        rows = 6L
        name = u'DEMOART_AU'
        val = None
        marccode = u'100__a'
        fddfi2 = None
        cols = 60L
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br />Authors: <i>(one per line)</i><br />'

    class SbmFIELDDESC_DEMOARTCHANGE:
        md = datetime.date(2008, 3, 7)
        rows = None
        name = u'DEMOART_CHANGE'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 7)
        fidesc = u'<select name="DEMOART_CHANGE[]" size="8" multiple>\r\n <option value="Select:">Select:</option>\r\n <option value="DEMOART_REP">Other Report Numbers</option>\r\n <option value="DEMOART_TITLE">Title</option>\r\n <option value="DEMOART_AU">Author(s)</option>\r\n <option value="DEMOART_LANG">Language</option>\r\n <option value="DEMOART_KW">Keywords</option>\r\n <option value="DEMOART_ABS">Abstract</option>\r\n <option value="DEMOART_NUMP">Number of Pages</option>\r\n</select>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'S'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOARTCONT:
        md = datetime.date(2008, 3, 7)
        rows = None
        name = u'DEMOART_CONT'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 7)
        fidesc = u'<div align="center">\r\n<input type="button" class="adminbutton" width="400" height="50" name="endS" value="Continue" onclick="finish();" />\r\n</div>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'D'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOARTDATE:
        md = datetime.date(2008, 3, 7)
        rows = None
        name = u'DEMOART_DATE'
        val = None
        marccode = u'269__c'
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 10L
        type = u'I'
        alephcode = None
        modifytext = u'<br />Date:&nbsp;'

    class SbmFIELDDESC_DEMOARTEND:
        md = datetime.date(2008, 3, 7)
        rows = None
        name = u'DEMOART_END'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 7)
        fidesc = u'<div align="center">\r\n<INPUT TYPE="button" class="adminbutton" name="endS" width="400" height="50" value="Finish Submission" onclick="finish();">\r\n</div>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'D'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOARTFILE:
        md = datetime.date(2008, 3, 7)
        rows = None
        name = u'DEMOART_FILE'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 60L
        type = u'F'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOARTKW:
        md = datetime.date(2008, 3, 7)
        rows = 4L
        name = u'DEMOART_KW'
        val = None
        marccode = u'6531_a'
        fddfi2 = None
        cols = 50L
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br /><br />Keywords:<br /><i>(one keyword/key-phrase per line)</i><br />'

    class SbmFIELDDESC_DEMOARTLANG:
        md = datetime.date(2008, 3, 7)
        rows = None
        name = u'DEMOART_LANG'
        val = None
        marccode = u'041__a'
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 7)
        fidesc = u'<SELECT name="DEMOART_LANG">\r\n        <option value="Select:">Select:</option>\r\n        <option value="eng">English</option>\r\n        <option value="fre">French</option>\r\n        <option value="ger">German</option>\r\n        <option value="dut">Dutch</option>\r\n        <option value="ita">Italian</option>\r\n        <option value="spa">Spanish</option>\r\n        <option value="por">Portuguese</option>\r\n        <option value="gre">Greek</option>\r\n        <option value="slo">Slovak</option>\r\n        <option value="cze">Czech</option>\r\n        <option value="hun">Hungarian</option>\r\n        <option value="pol">Polish</option>\r\n        <option value="nor">Norwegian</option>\r\n        <option value="swe">Swedish</option>\r\n        <option value="fin">Finnish</option>\r\n        <option value="rus">Russian</option>\r\n</SELECT>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'S'
        alephcode = None
        modifytext = u'<br /><br />Select the Language:&nbsp;'

    class SbmFIELDDESC_DEMOARTNOTE:
        md = datetime.date(2008, 3, 7)
        rows = 6L
        name = u'DEMOART_NOTE'
        val = None
        marccode = u'500__a'
        fddfi2 = None
        cols = 60L
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br /><br />Additional Comments or Notes:<br />'

    class SbmFIELDDESC_DEMOARTNUMP:
        md = datetime.date(2008, 3, 7)
        rows = None
        name = u'DEMOART_NUMP'
        val = None
        marccode = u'300__a'
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 5L
        type = u'I'
        alephcode = None
        modifytext = u'<br />Number of Pages:&nbsp;'

    class SbmFIELDDESC_DEMOARTREP:
        md = datetime.date(2008, 3, 7)
        rows = 4L
        name = u'DEMOART_REP'
        val = None
        marccode = u'088__a'
        fddfi2 = None
        cols = 30L
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br />Other Report Numbers <i>(one per line)</i>:'

    class SbmFIELDDESC_DEMOARTRN:
        md = datetime.date(2008, 3, 7)
        rows = None
        name = u'DEMOART_RN'
        val = u'DEMO-<COMBO>-<YYYY>-???'
        marccode = u'037__a'
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 35L
        type = u'I'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOARTTITLE:
        md = datetime.date(2008, 3, 7)
        rows = 5L
        name = u'DEMOART_TITLE'
        val = None
        marccode = u'245__a'
        fddfi2 = None
        cols = 60L
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br />Title:<br />'

    class SbmFIELDDESC_DEMOBOOABS:
        md = datetime.date(2008, 3, 7)
        rows = 12L
        name = u'DEMOBOO_ABS'
        val = None
        marccode = u'520__a'
        fddfi2 = None
        cols = 80L
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br />Abstract:<br />'

    class SbmFIELDDESC_DEMOBOOAU:
        md = datetime.date(2008, 3, 7)
        rows = 6L
        name = u'DEMOBOO_AU'
        val = None
        marccode = u'100__a'
        fddfi2 = None
        cols = 60L
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br />Authors: <i>(one per line)</i><br />'

    class SbmFIELDDESC_DEMOBOOCHANGE:
        md = datetime.date(2008, 3, 7)
        rows = None
        name = u'DEMOBOO_CHANGE'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 7)
        fidesc = u'<select name="DEMOBOO_CHANGE[]" size="9" multiple>\r\n <option value="Select:">Select:</option>\r\n <option value="DEMOBOO_REP">Other Report Numbers</option>\r\n <option value="DEMOBOO_TITLE">Title</option>\r\n <option value="DEMOBOO_AU">Author(s)</option>\r\n <option value="DEMOBOO_LANG">Language</option>\r\n <option value="DEMOBOO_KW">Keywords</option>\r\n <option value="DEMOBOO_ABS">Abstract</option>\r\n <option value="DEMOBOO_NUMP">Number of Pages</option>\r\n <option value="DEMOBOO_FILE">File</option>\r\n</select>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'S'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOBOOCOMNT:
        md = datetime.date(2008, 3, 7)
        rows = 6L
        name = u'DEMOBOO_COMNT'
        val = None
        marccode = u''
        fddfi2 = None
        cols = 60L
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOBOOCONT:
        md = datetime.date(2008, 3, 7)
        rows = None
        name = u'DEMOBOO_CONT'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 7)
        fidesc = u'<div align="center">\r\n<input type="button" class="adminbutton" width="400" height="50" name="endS" value="Continue" onclick="finish();" />\r\n</div>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'D'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOBOODATE:
        md = datetime.date(2008, 3, 7)
        rows = None
        name = u'DEMOBOO_DATE'
        val = None
        marccode = u'269__c'
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 10L
        type = u'I'
        alephcode = None
        modifytext = u'<br />Date:&nbsp;'

    class SbmFIELDDESC_DEMOBOODECSN:
        md = datetime.date(2008, 3, 7)
        rows = None
        name = u'DEMOBOO_DECSN'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 7)
        fidesc = u'<select name="DEMOBOO_DECSN">\r\n<option value="Select:">Select:</option>\r\n<option value="approve">Approve</option>\r\n<option value="reject">Reject</option>\r\n</select>\r\n'
        cookie = 0L
        maxlength = None
        size = None
        type = u'S'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOBOOEND:
        md = datetime.date(2008, 3, 7)
        rows = None
        name = u'DEMOBOO_END'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 7)
        fidesc = u'<div align="center">\r\n<INPUT TYPE="button" class="adminbutton" name="endS" width="400" height="50" value="Finish Submission" onclick="finish();">\r\n</div>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'D'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOBOOFILE:
        md = datetime.date(2008, 3, 7)
        rows = None
        name = u'DEMOBOO_FILE'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 60L
        type = u'F'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOBOOKW:
        md = datetime.date(2008, 3, 7)
        rows = 4L
        name = u'DEMOBOO_KW'
        val = None
        marccode = u'6531_a'
        fddfi2 = None
        cols = 50L
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br /><br />Keywords:<br /><i>(one keyword/key-phrase per line)</i><br />'

    class SbmFIELDDESC_DEMOBOOLANG:
        md = datetime.date(2008, 3, 7)
        rows = None
        name = u'DEMOBOO_LANG'
        val = None
        marccode = u'041__a'
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 7)
        fidesc = u'<SELECT name="DEMOBOO_LANG">\r\n        <option value="Select:">Select:</option>\r\n        <option value="eng">English</option>\r\n        <option value="fre">French</option>\r\n        <option value="ger">German</option>\r\n        <option value="dut">Dutch</option>\r\n        <option value="ita">Italian</option>\r\n        <option value="spa">Spanish</option>\r\n        <option value="por">Portuguese</option>\r\n        <option value="gre">Greek</option>\r\n        <option value="slo">Slovak</option>\r\n        <option value="cze">Czech</option>\r\n        <option value="hun">Hungarian</option>\r\n        <option value="pol">Polish</option>\r\n        <option value="nor">Norwegian</option>\r\n        <option value="swe">Swedish</option>\r\n        <option value="fin">Finnish</option>\r\n        <option value="rus">Russian</option>\r\n</SELECT>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'S'
        alephcode = None
        modifytext = u'<br /><br />Select the Language:&nbsp;'

    class SbmFIELDDESC_DEMOBOONOTE:
        md = datetime.date(2008, 3, 7)
        rows = 6L
        name = u'DEMOBOO_NOTE'
        val = None
        marccode = u'500__a'
        fddfi2 = None
        cols = 60L
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br /><br />Additional Comments or Notes:<br />'

    class SbmFIELDDESC_DEMOBOONUMP:
        md = datetime.date(2008, 3, 7)
        rows = None
        name = u'DEMOBOO_NUMP'
        val = None
        marccode = u'300__a'
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 5L
        type = u'I'
        alephcode = None
        modifytext = u'<br />Number of Pages:&nbsp;'

    class SbmFIELDDESC_DEMOBOOREGB:
        md = datetime.date(2008, 3, 7)
        rows = None
        name = u'DEMOBOO_REGB'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 7)
        fidesc = u'<div align="center">\r\n<INPUT TYPE="button" class="adminbutton" name="endS" width="400" height="50" value="Register Decision" onclick="finish();">\r\n</div>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'D'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOBOOREP:
        md = datetime.date(2008, 3, 7)
        rows = 4L
        name = u'DEMOBOO_REP'
        val = None
        marccode = u'088__a'
        fddfi2 = None
        cols = 30L
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br />Other Report Numbers <i>(one per line)</i>:'

    class SbmFIELDDESC_DEMOBOORN:
        md = datetime.date(2008, 3, 7)
        rows = None
        name = u'DEMOBOO_RN'
        val = u'DEMO-BOOK-<YYYY>-???'
        marccode = u'037__a'
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 35L
        type = u'I'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOBOOTITLE:
        md = datetime.date(2008, 3, 7)
        rows = 5L
        name = u'DEMOBOO_TITLE'
        val = None
        marccode = u'245__a'
        fddfi2 = None
        cols = 60L
        cd = datetime.date(2008, 3, 7)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br />Title:<br />'

    class SbmFIELDDESC_DEMOJRNABSE:
        md = datetime.date(2009, 2, 23)
        rows = 100L
        name = u'DEMOJRN_ABSE'
        val = None
        marccode = u'520__b'
        fddfi2 = None
        cols = 90L
        cd = datetime.date(2008, 9, 22)
        fidesc = u'from invenio.utils.html import get_html_text_editor\r\nfrom invenio.config import CFG_SITE_URL\r\nfrom invenio.legacy.bibrecord import get_fieldvalues\r\nimport os\r\n\r\n\r\nif (\'modify\' in curdir) and not os.path.exists("%s/DEMOJRN_ABSE" % curdir):\r\n    try:\r\n        content = get_fieldvalues(int(sysno), \'520__b\')[0]\r\n    except:\r\n        content = \'\'\r\nelif os.path.exists("%s/DEMOJRN_ABSE" % curdir):\r\n    content = file("%s/DEMOJRN_ABSE" % curdir).read()\r\nelse:\r\n    content = \'\'\r\n\r\ntext = get_html_text_editor("DEMOJRN_ABSE",id="BulletinCKEditor2", content=content, toolbar_set="WebJournal", width=\'522px\', height=\'700px\', file_upload_url=CFG_SITE_URL + \'/submit/attachfile\', custom_configurations_path=\'/ckeditor/journal-editor-config.js\')\r\n\r\n'
        cookie = 0L
        maxlength = None
        size = None
        type = u'R'
        alephcode = None
        modifytext = u'</td></tr><tr><td><br />English Article:<br />'

    class SbmFIELDDESC_DEMOJRNABSF:
        md = datetime.date(2009, 2, 23)
        rows = 100L
        name = u'DEMOJRN_ABSF'
        val = None
        marccode = u'590__b'
        fddfi2 = None
        cols = 90L
        cd = datetime.date(2008, 9, 23)
        fidesc = u'from invenio.utils.html import get_html_text_editor\r\nfrom invenio.config import CFG_SITE_URL\r\nfrom invenio.legacy.bibrecord import get_fieldvalues\r\nimport os\r\n\r\nif (\'modify\' in curdir) and not os.path.exists("%s/DEMOJRN_ABSF" % curdir):\r\n    try:\r\n        content = get_fieldvalues(int(sysno), \'590__b\')[0]\r\n    except:\r\n        content = \'\'\r\nelif os.path.exists("%s/DEMOJRN_ABSE" % curdir):\r\n    content = file("%s/DEMOJRN_ABSE" % curdir).read()\r\nelse:\r\n    content = \'\'\r\n\r\ntext = get_html_text_editor("DEMOJRN_ABSF", id="BulletinCKEditor1", content=content, toolbar_set="WebJournal", width=\'522px\', height=\'700px\', file_upload_url=CFG_SITE_URL + \'/submit/attachfile\', custom_configurations_path=\'/ckeditor/journal-editor-config.js\')'
        cookie = 0L
        maxlength = None
        size = None
        type = u'R'
        alephcode = None
        modifytext = u'</td><td><br />French Article:<br />'

    class SbmFIELDDESC_DEMOJRNAU:
        md = datetime.date(2009, 2, 20)
        rows = 4L
        name = u'DEMOJRN_AU'
        val = None
        marccode = u'100__a'
        fddfi2 = None
        cols = 60L
        cd = datetime.date(2008, 9, 23)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'</TD></TR><TR><TD><br /><br />Author(s): <i>(one per line)</i><br />'

    class SbmFIELDDESC_DEMOJRNCATEG:
        md = datetime.date(2009, 10, 15)
        rows = None
        name = u'DEMOJRN_CATEG'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2009, 10, 15)
        fidesc = u'# Solve usual problem with submit/direct?.. links that bypass \r\n# the comboXXX (category selection) of the submission. Retrieve \r\n# the value, and set it (only in the case of MBI)\r\n\r\nfrom invenio.legacy.bibrecord import get_fieldvalues\r\n\r\nif "modify" in curdir:\r\n    try:\r\n        comboDEMOJRNfile = file("%s/%s" % (curdir,\'comboDEMOJRN\'), \'w\')\r\n        report_number = get_fieldvalues(int(sysno), \'037__a\')[0]\r\n        category = report_number.split(\'-\')[1]\r\n        comboDEMOJRNfile.write(category)\r\n        comboDEMOJRNfile.close()\r\n    except:\r\n        text = \'\''
        cookie = 0L
        maxlength = None
        size = None
        type = u'R'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOJRNCHANGE:
        md = datetime.date(2009, 2, 20)
        rows = None
        name = u'DEMOJRN_CHANGE'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2009, 1, 9)
        fidesc = u'<div id="1" STYLE="position:relative;visibility:hidden;">\r\n<select name="DEMOJRN_CHANGE[]" size="2" multiple>\r\n <option selected value="DEMOJRN_TYPE">3</option>\r\n <option selected value="DEMOJRN_ISSUES">4</option>\r\n <option selected value="DEMOJRN_AU">12</option>\r\n <option selected value="DEMOJRN_EMAIL">13</option>\r\n <option selected value="DEMOJRN_TITLEE">14</option>\r\n <option selected value="DEMOJRN_TITLEF">15</option>\r\n <option selected value="DEMOJRN_ABSE">16</option>\r\n <option selected value="DEMOJRN_ABSF">17</option>\r\n <option selected value="DEMOJRN_IN">18</option>\r\n <option selected value="DEMOJRN_ENDING">19</option>\r\n</select>\r\n <option selected value="DEMOJRN_CATEG">20</option>\r\n</select>\r\n</div>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'S'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOJRNCONT:
        md = datetime.date(2008, 10, 6)
        rows = None
        name = u'DEMOJRN_CONT'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 10, 6)
        fidesc = u'<div align="center">\r\n<input type="button" class="adminbutton" width="400" height="50" name="endS" value="Continue" onclick="finish();" />\r\n</div>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'D'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOJRNEMAIL:
        md = datetime.date(2009, 2, 20)
        rows = 4L
        name = u'DEMOJRN_EMAIL'
        val = None
        marccode = u'859__a'
        fddfi2 = None
        cols = 60L
        cd = datetime.date(2008, 9, 23)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'</TD><TD><br /><br />E-mail(s) of the author(s): <i>(one per line)</i><br />'

    class SbmFIELDDESC_DEMOJRNEND:
        md = datetime.date(2009, 2, 20)
        rows = None
        name = u'DEMOJRN_END'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 9, 23)
        fidesc = u'<div align="center">\r\n<INPUT TYPE="button" class="adminbutton" name="endS" width="400" height="50" value="Finish Submission" onclick="finish();">\r\n</div>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'D'
        alephcode = None
        modifytext = u'</td></tr><tr><td colspan="2">'

    class SbmFIELDDESC_DEMOJRNENDING:
        md = datetime.date(2009, 2, 20)
        rows = None
        name = u'DEMOJRN_ENDING'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2009, 2, 6)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'H'
        alephcode = None
        modifytext = u'</td></tr></table>'

    class SbmFIELDDESC_DEMOJRNIN:
        md = datetime.date(2009, 2, 20)
        rows = None
        name = u'DEMOJRN_IN'
        val = u'Atlantis Times'
        marccode = u'595__a'
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 9, 23)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'H'
        alephcode = None
        modifytext = u' '

    class SbmFIELDDESC_DEMOJRNISSUES:
        md = datetime.date(2009, 2, 23)
        rows = None
        name = u'DEMOJRN_ISSUES'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2009, 2, 20)
        fidesc = u'from invenio.legacy.bibrecord import get_fieldvalues\r\nfrom invenio.legacy.webjournal.utils import get_next_journal_issues, get_current_issue, get_journal_issue_grouping\r\nimport os\r\n\r\norders_and_issues = [(\'\',\'\')]*4\r\n\r\nif (\'modify\' in curdir) and not os.path.exists("%s/DEMOJRN_ISSUE1" % curdir):\r\n    try:\r\n        orders = get_fieldvalues(int(sysno), \'773__c\')\r\n        issues = get_fieldvalues(int(sysno), \'773__n\')\r\n        orders_and_issues = zip(orders, issues) + orders_and_issues\r\n    except:\r\n        pass\r\nelif (\'running\' in curdir) and not os.path.exists("%s/DEMOJRN_ISSUE1" % curdir):\r\n    try:\r\n        journal_name = \'AtlantisTimes\'\r\n        current_issue = get_current_issue(\'en\', journal_name)\r\n        nb_issues = get_journal_issue_grouping(journal_name)\r\n        next_issue_numbers = get_next_journal_issues(current_issue, journal_name, nb_issues)\r\n        orders_and_issues = zip([\'\']*4, next_issue_numbers) + orders_and_issues\r\n    except:\r\n        pass\r\nissues_fields = []\r\nsingle_issue_and_order_tmpl = \'\'\'\r\n<input type="text" name="DEMOJRN_ORDER%i" size="2" value="%s"  />\r\n<input type="text" name="DEMOJRN_ISSUE%i" size="7" value="%s"  />\'\'\'\r\ni = 1\r\nfor order_and_issue in orders_and_issues[:4]:\r\n    order = order_and_issue[0]\r\n    issue = order_and_issue[1]\r\n    issues_fields.append(single_issue_and_order_tmpl % (i, order, i, issue))\r\n    i += 1\r\n\r\ntext = \'<br/>\'.join(issues_fields)\r\n'
        cookie = 0L
        maxlength = None
        size = None
        type = u'R'
        alephcode = None
        modifytext = u'</TD><TD align="center"><span style="color: red;">*</span>Order(s) <small><i>(digit)</i></small> and issue(s) <small><i>(xx/YYYY)</i></small> of the article:<br />'

    class SbmFIELDDESC_DEMOJRNRN:
        md = datetime.date(2009, 2, 20)
        rows = None
        name = u'DEMOJRN_RN'
        val = u'BUL-<COMBO>-<YYYY>-???'
        marccode = u'037__a'
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 10, 6)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 35L
        type = u'I'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOJRNTITLEE:
        md = datetime.date(2009, 2, 20)
        rows = 5L
        name = u'DEMOJRN_TITLEE'
        val = None
        marccode = u'245__a'
        fddfi2 = None
        cols = 60L
        cd = datetime.date(2008, 9, 23)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'</TD></TR><TR><TD><br /><br />English title:<br />'

    class SbmFIELDDESC_DEMOJRNTITLEF:
        md = datetime.date(2009, 2, 20)
        rows = 5L
        name = u'DEMOJRN_TITLEF'
        val = None
        marccode = u'246_1a'
        fddfi2 = None
        cols = 60L
        cd = datetime.date(2008, 9, 23)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'</TD><TD><br /><br />French title:<br />'

    class SbmFIELDDESC_DEMOJRNTYPE:
        md = datetime.date(2009, 2, 20)
        rows = None
        name = u'DEMOJRN_TYPE'
        val = None
        marccode = u'691__a'
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 12, 4)
        fidesc = u'<select name="DEMOJRN_TYPE">\r\n<option value="Select:">Select:</option>\r\n\r\n<option value="DRAFT">Offline</option>\r\n<option value="ONLINE">Online</option>\r\n</select><small>[<a target="_blank" href="/help/admin/webjournal-editor-guide#offlineVsOnline">?</a>]</small>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'S'
        alephcode = None
        modifytext = u'<TABLE WIDTH="100%" BGCOLOR="#D3E3E2" ALIGN="center" CELLSPACING="2" CELLPADDING="2" BORDER="1"><TR><TD ALIGN="left" colspan="2"><br /><b>Update an Atlantis Times article:</b></TD></TR><TR><TD align="center"><span style="color: red;">*</span>Status:<br />'

    class SbmFIELDDESC_DEMOPICADDRN:
        md = datetime.date(2007, 9, 13)
        rows = 4L
        name = u'DEMOPIC_ADD_RN'
        val = None
        marccode = u'088__a'
        fddfi2 = None
        cols = 30L
        cd = datetime.date(2007, 9, 13)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br /><br />Additional Reference Numbers:<br />'

    class SbmFIELDDESC_DEMOPICCHANGE:
        md = datetime.date(2007, 10, 4)
        rows = None
        name = u'DEMOPIC_CHANGE'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2007, 10, 4)
        fidesc = u'<select name="DEMOPIC_CHANGE[]" size="8" multiple>\r\n <option value="Select:">Select:</option>\r\n <option value="DEMOPIC_TITLE">Title</option>\r\n <option value="DEMOPIC_PHOTOG">Photographer(s)</option>\r\n <option value="DEMOPIC_DATE">Picture Date</option>\r\n <option value="DEMOPIC_KW">Keywords</option>\r\n <option value="DEMOPIC_DESCR">Picture Description</option>\r\n <option value="DEMOPIC_ADD_RN">Picture Reference Numbers</option>\r\n <option value="DEMOPIC_NOTE">Notes or Comments</option>\r\n <option value="Upload_Photos">Pictures</option>\r\n</select>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'S'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOPICCONT:
        md = datetime.date(2007, 10, 4)
        rows = None
        name = u'DEMOPIC_CONT'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2007, 10, 4)
        fidesc = u'<div align="center">\r\n<input type="button" class="adminbutton" width="400" height="50" name="endS" value="Continue" onclick="finish();" />\r\n</div>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'D'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOPICDATE:
        md = datetime.date(2007, 9, 19)
        rows = None
        name = u'DEMOPIC_DATE'
        val = None
        marccode = u'260__c'
        fddfi2 = None
        cols = None
        cd = datetime.date(2007, 9, 13)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 10L
        type = u'I'
        alephcode = None
        modifytext = u'<br /><br />Date of the picture (dd/mm/yyyy):&nbsp;'

    class SbmFIELDDESC_DEMOPICDESCR:
        md = datetime.date(2007, 9, 13)
        rows = 12L
        name = u'DEMOPIC_DESCR'
        val = None
        marccode = u'520__a'
        fddfi2 = None
        cols = 80L
        cd = datetime.date(2007, 9, 13)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br /><br />Picture Description:<br />'

    class SbmFIELDDESC_DEMOPICFILE:
        md = datetime.date(2007, 9, 13)
        rows = None
        name = u'DEMOPIC_FILE'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2007, 9, 13)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 40L
        type = u'F'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOPICFINISH:
        md = datetime.date(2007, 9, 13)
        rows = None
        name = u'DEMOPIC_FINISH'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2007, 9, 13)
        fidesc = u'<div align="center">\r\n<input type="button" class="adminbutton" width="400" height="50" name="endS" value="finish submission" onclick="finish();" />\r\n</div>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'D'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOPICKW:
        md = datetime.date(2007, 9, 13)
        rows = 2L
        name = u'DEMOPIC_KW'
        val = None
        marccode = u'6531_a'
        fddfi2 = None
        cols = 50L
        cd = datetime.date(2007, 9, 13)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br /><br />Keywords<br /><i>(Optional, <b>one keyword/key-phrase per line</b>)</i>:<br />'

    class SbmFIELDDESC_DEMOPICNOTE:
        md = datetime.date(2007, 9, 13)
        rows = 6L
        name = u'DEMOPIC_NOTE'
        val = None
        marccode = u'500__a'
        fddfi2 = None
        cols = 60L
        cd = datetime.date(2007, 9, 13)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br /><br />Additional Comments or Notes about the Picture:<br />'

    class SbmFIELDDESC_DEMOPICPHOTOG:
        md = datetime.date(2007, 9, 19)
        rows = 6L
        name = u'DEMOPIC_PHOTOG'
        val = None
        marccode = u'100__a'
        fddfi2 = None
        cols = 30L
        cd = datetime.date(2007, 9, 13)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br /><br />Picture Author(s) or Photographers(s)<br /><i>(optional)(<B>one per line</B>)</i>:<br />'

    class SbmFIELDDESC_DEMOPICRN:
        md = datetime.date(2007, 10, 4)
        rows = None
        name = u'DEMOPIC_RN'
        val = u'DEMO-PICTURE-<COMBO>-<YYYY>-???'
        marccode = u'037__a'
        fddfi2 = None
        cols = None
        cd = datetime.date(2007, 10, 4)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 30L
        type = u'I'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOPICTITLE:
        md = datetime.date(2007, 9, 13)
        rows = 5L
        name = u'DEMOPIC_TITLE'
        val = None
        marccode = u'245__a'
        fddfi2 = None
        cols = 60L
        cd = datetime.date(2007, 9, 13)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOPOEABS:
        md = datetime.date(2008, 3, 12)
        rows = 20L
        name = u'DEMOPOE_ABS'
        val = None
        marccode = u'520__a'
        fddfi2 = None
        cols = 80L
        cd = datetime.date(2008, 3, 12)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br />Abstract:<br />'

    class SbmFIELDDESC_DEMOPOEAU:
        md = datetime.date(2008, 3, 12)
        rows = 6L
        name = u'DEMOPOE_AU'
        val = None
        marccode = u'100__a'
        fddfi2 = None
        cols = 60L
        cd = datetime.date(2008, 3, 12)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br />Authors: <i>(one per line)</i><br />'

    class SbmFIELDDESC_DEMOPOECHANGE:
        md = datetime.date(2008, 3, 12)
        rows = None
        name = u'DEMOPOE_CHANGE'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 12)
        fidesc = u'<select name="DEMOPOE_CHANGE[]" size="6" multiple>\r\n <option value="Select:">Select:</option>\r\n <option value="DEMOPOE_TITLE">Title</option>\r\n <option value="DEMOPOE_AU">Author(s)</option>\r\n <option value="DEMOPOE_LANG">Language</option>\r\n <option value="DEMOPOE_YEAR">Year</option>\r\n <option value="DEMOPOE_ABS">Poem Text</option>\r\n</select>\r\n'
        cookie = 0L
        maxlength = None
        size = None
        type = u'S'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOPOECONT:
        md = datetime.date(2008, 3, 12)
        rows = None
        name = u'DEMOPOE_CONT'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 12)
        fidesc = u'<div align="center">\r\n<input type="button" class="adminbutton" width="400" height="50" name="endS" value="Continue" onclick="finish();" />\r\n</div>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'D'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOPOEDUMMY:
        md = datetime.date(2008, 3, 12)
        rows = None
        name = u'DEMOPOE_DUMMY'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 12)
        fidesc = u'</td></tr></table><br /><br /></td></tr></table>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'D'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOPOEEND:
        md = datetime.date(2008, 3, 12)
        rows = None
        name = u'DEMOPOE_END'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 12)
        fidesc = u'<div align="center">\r\n<INPUT TYPE="button" class="adminbutton" name="endS" width="400" height="50" value="Finish Submission" onclick="finish();">\r\n</div>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'D'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOPOELANG:
        md = datetime.date(2008, 3, 12)
        rows = None
        name = u'DEMOPOE_LANG'
        val = None
        marccode = u'041__a'
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 12)
        fidesc = u'<SELECT name="DEMOPOE_LANG">\r\n        <option value="Select:">Select:</option>\r\n        <option value="eng">English</option>\r\n        <option value="fre">French</option>\r\n        <option value="ger">German</option>\r\n        <option value="dut">Dutch</option>\r\n        <option value="ita">Italian</option>\r\n        <option value="spa">Spanish</option>\r\n        <option value="por">Portuguese</option>\r\n        <option value="gre">Greek</option>\r\n        <option value="slo">Slovak</option>\r\n        <option value="cze">Czech</option>\r\n        <option value="hun">Hungarian</option>\r\n        <option value="pol">Polish</option>\r\n        <option value="nor">Norwegian</option>\r\n        <option value="swe">Swedish</option>\r\n        <option value="fin">Finnish</option>\r\n        <option value="rus">Russian</option>\r\n</SELECT>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'S'
        alephcode = None
        modifytext = u'<br /><br />Select the Language:&nbsp;'

    class SbmFIELDDESC_DEMOPOERN:
        md = datetime.date(2008, 3, 12)
        rows = None
        name = u'DEMOPOE_RN'
        val = u'DEMO-POETRY-<YYYY>-???'
        marccode = u'037__a'
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 12)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 35L
        type = u'I'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOPOETITLE:
        md = datetime.date(2008, 3, 12)
        rows = 5L
        name = u'DEMOPOE_TITLE'
        val = None
        marccode = u'245__a'
        fddfi2 = None
        cols = 60L
        cd = datetime.date(2008, 3, 12)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br />Title:<br />'

    class SbmFIELDDESC_DEMOPOEYEAR:
        md = datetime.date(2008, 3, 12)
        rows = None
        name = u'DEMOPOE_YEAR'
        val = None
        marccode = u'909C0y'
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 12)
        fidesc = None
        cookie = 0L
        maxlength = 4L
        size = 4L
        type = u'I'
        alephcode = None
        modifytext = u'<br /><br />Year:&nbsp;'

    class SbmFIELDDESC_DEMOTHEABS:
        md = datetime.date(2008, 3, 2)
        rows = 12L
        name = u'DEMOTHE_ABS'
        val = None
        marccode = u'520__a'
        fddfi2 = None
        cols = 80L
        cd = datetime.date(2008, 3, 2)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br />Abstract:<br />'

    class SbmFIELDDESC_DEMOTHEAU:
        md = datetime.date(2008, 3, 2)
        rows = 6L
        name = u'DEMOTHE_AU'
        val = None
        marccode = u'100__a'
        fddfi2 = None
        cols = 60L
        cd = datetime.date(2008, 3, 2)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br />Authors:<br />(one per line):<br />'

    class SbmFIELDDESC_DEMOTHECHANGE:
        md = datetime.date(2008, 3, 6)
        rows = None
        name = u'DEMOTHE_CHANGE'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 5)
        fidesc = u'<select name="DEMOTHE_CHANGE[]" size="9" multiple>\r\n <option value="Select:">Select:</option>\r\n <option value="DEMOTHE_REP">Other Report Numbers</option>\r\n <option value="DEMOTHE_TITLE">Title</option>\r\n <option value="DEMOTHE_SUBTITLE">Subtitle</option>\r\n <option value="DEMOTHE_AU">Author(s)</option>\r\n <option value="DEMOTHE_SUPERV">Supervisor(s)</option>\r\n <option value="DEMOTHE_ABS">Abstract</option>\r\n <option value="DEMOTHE_NUMP">Number of Pages</option>\r\n <option value="DEMOTHE_LANG">Language</option>\r\n</select>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'S'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOTHECONT:
        md = datetime.date(2008, 3, 5)
        rows = None
        name = u'DEMOTHE_CONT'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 5)
        fidesc = u'<div align="center">\r\n<input type="button" class="adminbutton" width="400" height="50" name="endS" value="Continue" onclick="finish();" />\r\n</div>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'D'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOTHEDATE:
        md = datetime.date(2008, 3, 2)
        rows = None
        name = u'DEMOTHE_DATE'
        val = None
        marccode = u'269__c'
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 2)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 10L
        type = u'I'
        alephcode = None
        modifytext = u'<br />Date:&nbsp;'

    class SbmFIELDDESC_DEMOTHEDIPL:
        md = datetime.date(2008, 3, 2)
        rows = None
        name = u'DEMOTHE_DIPL'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 2)
        fidesc = u'<select name="DEMOTHE_DIPL">\r\n <option value="">Select:</option>\r\n <option value="Diploma">Diploma</option>\r\n <option value="MSc">MSc</option>\r\n <option value="PhD">PhD</option>\r\n</select>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'S'
        alephcode = None
        modifytext = u'<br /><br />Diploma Awarded:<br />'

    class SbmFIELDDESC_DEMOTHEEND:
        md = datetime.date(2008, 3, 2)
        rows = None
        name = u'DEMOTHE_END'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 2)
        fidesc = u'<div align="center">\r\n<INPUT TYPE="button" class="adminbutton" name="endS" width="400" height="50" value="Finish Submission" onclick="finish();">\r\n</div>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'D'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOTHEFILE:
        md = datetime.date(2008, 3, 2)
        rows = None
        name = u'DEMOTHE_FILE'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 2)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 60L
        type = u'F'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOTHELANG:
        md = datetime.date(2008, 3, 2)
        rows = None
        name = u'DEMOTHE_LANG'
        val = None
        marccode = u'041__a'
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 2)
        fidesc = u'<SELECT name="DEMOTHE_LANG">\r\n        <option value="Select:">Select:</option>\r\n        <option value="eng">English</option>\r\n        <option value="fre">French</option>\r\n        <option value="ger">German</option>\r\n        <option value="dut">Dutch</option>\r\n        <option value="ita">Italian</option>\r\n        <option value="spa">Spanish</option>\r\n        <option value="por">Portuguese</option>\r\n        <option value="gre">Greek</option>\r\n        <option value="slo">Slovak</option>\r\n        <option value="cze">Czech</option>\r\n        <option value="hun">Hungarian</option>\r\n        <option value="pol">Polish</option>\r\n        <option value="nor">Norwegian</option>\r\n        <option value="swe">Swedish</option>\r\n        <option value="fin">Finnish</option>\r\n        <option value="rus">Russian</option>\r\n</SELECT>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'S'
        alephcode = None
        modifytext = u'<br /><br />Select the Language:&nbsp;'

    class SbmFIELDDESC_DEMOTHENUMP:
        md = datetime.date(2008, 3, 6)
        rows = None
        name = u'DEMOTHE_NUMP'
        val = None
        marccode = u'300__a'
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 2)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 5L
        type = u'I'
        alephcode = None
        modifytext = u'<br />Number of Pages:&nbsp;'

    class SbmFIELDDESC_DEMOTHEPLACE:
        md = datetime.date(2008, 3, 2)
        rows = None
        name = u'DEMOTHE_PLACE'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 2)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 20L
        type = u'I'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOTHEPLDEF:
        md = datetime.date(2008, 3, 2)
        rows = None
        name = u'DEMOTHE_PLDEF'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 2)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 20L
        type = u'I'
        alephcode = None
        modifytext = u'<br /><br />Place of Thesis Defence:<br />'

    class SbmFIELDDESC_DEMOTHEPUBL:
        md = datetime.date(2008, 3, 2)
        rows = None
        name = u'DEMOTHE_PUBL'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 2)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 35L
        type = u'I'
        alephcode = None
        modifytext = u'<br />Thesis Publisher (or University):&nbsp;'

    class SbmFIELDDESC_DEMOTHEREP:
        md = datetime.date(2008, 3, 2)
        rows = 4L
        name = u'DEMOTHE_REP'
        val = None
        marccode = u'088__a'
        fddfi2 = None
        cols = 30L
        cd = datetime.date(2008, 3, 2)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br />Other Report Numbers (one per line):'

    class SbmFIELDDESC_DEMOTHERN:
        md = datetime.date(2008, 3, 5)
        rows = None
        name = u'DEMOTHE_RN'
        val = u'DEMO-THESIS-<YYYY>-???'
        marccode = u'037__a'
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 5)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 30L
        type = u'I'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOTHESUBTTL:
        md = datetime.date(2008, 3, 2)
        rows = 3L
        name = u'DEMOTHE_SUBTTL'
        val = None
        marccode = u'245__b'
        fddfi2 = None
        cols = 60L
        cd = datetime.date(2008, 3, 2)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br /><br />Thesis Subtitle (if any):<br />'

    class SbmFIELDDESC_DEMOTHESUPERV:
        md = datetime.date(2008, 3, 2)
        rows = 6L
        name = u'DEMOTHE_SUPERV'
        val = None
        marccode = u''
        fddfi2 = None
        cols = 60L
        cd = datetime.date(2008, 3, 2)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br />Thesis Supervisor(s)<br />(one per line):<br />'

    class SbmFIELDDESC_DEMOTHETITLE:
        md = datetime.date(2008, 3, 2)
        rows = 5L
        name = u'DEMOTHE_TITLE'
        val = None
        marccode = u'245__a'
        fddfi2 = None
        cols = 60L
        cd = datetime.date(2008, 3, 2)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = u'<br />Title:<br />'

    class SbmFIELDDESC_DEMOTHEUNIV:
        md = datetime.date(2008, 3, 2)
        rows = None
        name = u'DEMOTHE_UNIV'
        val = None
        marccode = u'502__b'
        fddfi2 = None
        cols = None
        cd = datetime.date(2008, 3, 2)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = 30L
        type = u'I'
        alephcode = None
        modifytext = u'<br />Awarding University:<br />'

    class SbmFIELDDESC_DEMOVIDASPECT:
        md = datetime.date(2012, 2, 16)
        rows = None
        name = u'DEMOVID_ASPECT'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2012, 2, 16)
        fidesc = u'from invenio.modules.encoder.websubmit import websumbit_aspect_ratio_form_element\r\n\r\ntext = websumbit_aspect_ratio_form_element(curdir, doctype, uid, access)'
        cookie = 0L
        maxlength = None
        size = None
        type = u'R'
        alephcode = None
        modifytext = u'Aspect Ratio'

    class SbmFIELDDESC_DEMOVIDAU:
        md = datetime.date(2012, 2, 16)
        rows = 6L
        name = u'DEMOVID_AU'
        val = None
        marccode = u'100__a'
        fddfi2 = None
        cols = 80L
        cd = datetime.date(2012, 2, 16)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOVIDDESCR:
        md = datetime.date(2012, 2, 16)
        rows = 12L
        name = u'DEMOVID_DESCR'
        val = None
        marccode = u'520__a'
        fddfi2 = None
        cols = 80L
        cd = datetime.date(2012, 2, 16)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'T'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOVIDFILE:
        md = datetime.date(2012, 2, 16)
        rows = None
        name = u'DEMOVID_FILE'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2012, 2, 16)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'F'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOVIDSINGLE:
        md = datetime.date(2012, 2, 16)
        rows = None
        name = u'DEMOVID_SINGLE'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2012, 2, 16)
        fidesc = u'from invenio.modules.encoder.websubmit import (get_session_id, websubmit_singlepage)\r\n\r\n# Retrieve session id\r\ntry:\r\n    # User info is defined only in MBI/MPI actions...\r\n    session_id = get_session_id(None, uid, user_info) \r\nexcept:\r\n    session_id = get_session_id(req, uid, {})\r\n\r\ntext = websubmit_singlepage(curdir, doctype, uid, access, session_id)'
        cookie = 0L
        maxlength = None
        size = None
        type = u'R'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOVIDSUBMIT:
        md = datetime.date(2012, 2, 16)
        rows = None
        name = u'DEMOVID_SUBMIT'
        val = None
        marccode = u''
        fddfi2 = None
        cols = None
        cd = datetime.date(2012, 2, 16)
        fidesc = u'<div align="center">\r\n<input type="button" class="adminbutton" width="400" height="50" name="endS" value="finish submission" onclick="finish();" />\r\n</div>'
        cookie = 0L
        maxlength = None
        size = None
        type = u'D'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOVIDTITLE:
        md = datetime.date(2012, 2, 16)
        rows = None
        name = u'DEMOVID_TITLE'
        val = None
        marccode = u'245__a'
        fddfi2 = None
        cols = None
        cd = datetime.date(2012, 2, 16)
        fidesc = None
        cookie = 0L
        maxlength = None
        size = None
        type = u'I'
        alephcode = None
        modifytext = None

    class SbmFIELDDESC_DEMOVIDYEAR:
        md = datetime.date(2012, 2, 16)
        rows = None
        name = u'DEMOVID_YEAR'
        val = None
        marccode = u'909C0y'
        fddfi2 = None
        cols = None
        cd = datetime.date(2012, 2, 16)
        fidesc = None
        cookie = 0L
        maxlength = 4L
        size = 4L
        type = u'I'
        alephcode = None
        modifytext = None


class SbmFUNCTIONSData(DataSet):

    class SbmFUNCTIONS_APP_DEMOBOO_CaseEDS_40_1:
        action = u'APP'
        function = u'CaseEDS'
        step = 1
        score = 40L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_GetInfo_40_2:
        action = u'APP'
        function = u'Get_Info'
        step = 2
        score = 40L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_GetInfo_40_3:
        action = u'APP'
        function = u'Get_Info'
        step = 3
        score = 40L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_GetRecid_30_2:
        action = u'APP'
        function = u'Get_Recid'
        step = 2
        score = 30L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_GetRecid_30_3:
        action = u'APP'
        function = u'Get_Recid'
        step = 3
        score = 30L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_GetReportNumber_10_1:
        action = u'APP'
        function = u'Get_Report_Number'
        step = 1
        score = 10L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_GetReportNumber_10_2:
        action = u'APP'
        function = u'Get_Report_Number'
        step = 2
        score = 10L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_GetReportNumber_10_3:
        action = u'APP'
        function = u'Get_Report_Number'
        step = 3
        score = 10L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_InsertRecord_60_2:
        action = u'APP'
        function = u'Insert_Record'
        step = 2
        score = 60L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_IsReferee_30_1:
        action = u'APP'
        function = u'Is_Referee'
        step = 1
        score = 30L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_MakeRecord_50_2:
        action = u'APP'
        function = u'Make_Record'
        step = 2
        score = 50L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_MoveFromPending_20_2:
        action = u'APP'
        function = u'Move_From_Pending'
        step = 2
        score = 20L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_MoveFromPending_20_3:
        action = u'APP'
        function = u'Move_From_Pending'
        step = 3
        score = 20L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_MovetoDone_100_2:
        action = u'APP'
        function = u'Move_to_Done'
        step = 2
        score = 100L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_MovetoDone_80_3:
        action = u'APP'
        function = u'Move_to_Done'
        step = 3
        score = 80L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_PrintSuccessAPP_60_3:
        action = u'APP'
        function = u'Print_Success_APP'
        step = 3
        score = 60L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_PrintSuccessAPP_80_2:
        action = u'APP'
        function = u'Print_Success_APP'
        step = 2
        score = 80L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_SendAPPMail_70_3:
        action = u'APP'
        function = u'Send_APP_Mail'
        step = 3
        score = 70L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_SendAPPMail_90_2:
        action = u'APP'
        function = u'Send_APP_Mail'
        step = 2
        score = 90L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_TestStatus_20_1:
        action = u'APP'
        function = u'Test_Status'
        step = 1
        score = 20L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_UpdateApprovalDB_50_3:
        action = u'APP'
        function = u'Update_Approval_DB'
        step = 3
        score = 50L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_APP_DEMOBOO_UpdateApprovalDB_70_2:
        action = u'APP'
        function = u'Update_Approval_DB'
        step = 2
        score = 70L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_MBI_DEMOART_CreateModifyInterface_40_1:
        action = u'MBI'
        function = u'Create_Modify_Interface'
        step = 1
        score = 40L
        doctype = u'DEMOART'

    class SbmFUNCTIONS_MBI_DEMOART_GetRecid_20_1:
        action = u'MBI'
        function = u'Get_Recid'
        step = 1
        score = 20L
        doctype = u'DEMOART'

    class SbmFUNCTIONS_MBI_DEMOART_GetRecid_20_2:
        action = u'MBI'
        function = u'Get_Recid'
        step = 2
        score = 20L
        doctype = u'DEMOART'

    class SbmFUNCTIONS_MBI_DEMOART_GetReportNumber_10_1:
        action = u'MBI'
        function = u'Get_Report_Number'
        step = 1
        score = 10L
        doctype = u'DEMOART'

    class SbmFUNCTIONS_MBI_DEMOART_GetReportNumber_10_2:
        action = u'MBI'
        function = u'Get_Report_Number'
        step = 2
        score = 10L
        doctype = u'DEMOART'

    class SbmFUNCTIONS_MBI_DEMOART_InsertModifyRecord_50_2:
        action = u'MBI'
        function = u'Insert_Modify_Record'
        step = 2
        score = 50L
        doctype = u'DEMOART'

    class SbmFUNCTIONS_MBI_DEMOART_IsOriginalSubmitter_30_1:
        action = u'MBI'
        function = u'Is_Original_Submitter'
        step = 1
        score = 30L
        doctype = u'DEMOART'

    class SbmFUNCTIONS_MBI_DEMOART_IsOriginalSubmitter_30_2:
        action = u'MBI'
        function = u'Is_Original_Submitter'
        step = 2
        score = 30L
        doctype = u'DEMOART'

    class SbmFUNCTIONS_MBI_DEMOART_MakeModifyRecord_40_2:
        action = u'MBI'
        function = u'Make_Modify_Record'
        step = 2
        score = 40L
        doctype = u'DEMOART'

    class SbmFUNCTIONS_MBI_DEMOART_MovetoDone_80_2:
        action = u'MBI'
        function = u'Move_to_Done'
        step = 2
        score = 80L
        doctype = u'DEMOART'

    class SbmFUNCTIONS_MBI_DEMOART_PrintSuccessMBI_60_2:
        action = u'MBI'
        function = u'Print_Success_MBI'
        step = 2
        score = 60L
        doctype = u'DEMOART'

    class SbmFUNCTIONS_MBI_DEMOART_SendModifyMail_70_2:
        action = u'MBI'
        function = u'Send_Modify_Mail'
        step = 2
        score = 70L
        doctype = u'DEMOART'

    class SbmFUNCTIONS_MBI_DEMOBOO_CreateModifyInterface_40_1:
        action = u'MBI'
        function = u'Create_Modify_Interface'
        step = 1
        score = 40L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_MBI_DEMOBOO_GetRecid_20_1:
        action = u'MBI'
        function = u'Get_Recid'
        step = 1
        score = 20L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_MBI_DEMOBOO_GetRecid_20_2:
        action = u'MBI'
        function = u'Get_Recid'
        step = 2
        score = 20L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_MBI_DEMOBOO_GetReportNumber_10_1:
        action = u'MBI'
        function = u'Get_Report_Number'
        step = 1
        score = 10L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_MBI_DEMOBOO_GetReportNumber_10_2:
        action = u'MBI'
        function = u'Get_Report_Number'
        step = 2
        score = 10L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_MBI_DEMOBOO_InsertModifyRecord_50_2:
        action = u'MBI'
        function = u'Insert_Modify_Record'
        step = 2
        score = 50L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_MBI_DEMOBOO_IsOriginalSubmitter_30_1:
        action = u'MBI'
        function = u'Is_Original_Submitter'
        step = 1
        score = 30L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_MBI_DEMOBOO_IsOriginalSubmitter_30_2:
        action = u'MBI'
        function = u'Is_Original_Submitter'
        step = 2
        score = 30L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_MBI_DEMOBOO_MakeModifyRecord_40_2:
        action = u'MBI'
        function = u'Make_Modify_Record'
        step = 2
        score = 40L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_MBI_DEMOBOO_MoveUploadedFilestoStorage_60_2:
        action = u'MBI'
        function = u'Move_Uploaded_Files_to_Storage'
        step = 2
        score = 60L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_MBI_DEMOBOO_MovetoDone_90_2:
        action = u'MBI'
        function = u'Move_to_Done'
        step = 2
        score = 90L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_MBI_DEMOBOO_PrintSuccessMBI_70_2:
        action = u'MBI'
        function = u'Print_Success_MBI'
        step = 2
        score = 70L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_MBI_DEMOBOO_SendModifyMail_80_2:
        action = u'MBI'
        function = u'Send_Modify_Mail'
        step = 2
        score = 80L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_MBI_DEMOJRN_CreateModifyInterface_30_1:
        action = u'MBI'
        function = u'Create_Modify_Interface'
        step = 1
        score = 30L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_MBI_DEMOJRN_GetRecid_20_1:
        action = u'MBI'
        function = u'Get_Recid'
        step = 1
        score = 20L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_MBI_DEMOJRN_GetRecid_20_2:
        action = u'MBI'
        function = u'Get_Recid'
        step = 2
        score = 20L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_MBI_DEMOJRN_GetReportNumber_10_1:
        action = u'MBI'
        function = u'Get_Report_Number'
        step = 1
        score = 10L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_MBI_DEMOJRN_GetReportNumber_10_2:
        action = u'MBI'
        function = u'Get_Report_Number'
        step = 2
        score = 10L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_MBI_DEMOJRN_InsertModifyRecord_50_2:
        action = u'MBI'
        function = u'Insert_Modify_Record'
        step = 2
        score = 50L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_MBI_DEMOJRN_MakeModifyRecord_40_2:
        action = u'MBI'
        function = u'Make_Modify_Record'
        step = 2
        score = 40L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_MBI_DEMOJRN_MoveCKEditorFilestoStorage_30_2:
        action = u'MBI'
        function = u'Move_CKEditor_Files_to_Storage'
        step = 2
        score = 30L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_MBI_DEMOJRN_MoveFilestoStorage_60_2:
        action = u'MBI'
        function = u'Move_Files_to_Storage'
        step = 2
        score = 60L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_MBI_DEMOJRN_MovetoDone_90_2:
        action = u'MBI'
        function = u'Move_to_Done'
        step = 2
        score = 90L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_MBI_DEMOJRN_PrintSuccessMBI_70_2:
        action = u'MBI'
        function = u'Print_Success_MBI'
        step = 2
        score = 70L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_MBI_DEMOJRN_SendModifyMail_80_2:
        action = u'MBI'
        function = u'Send_Modify_Mail'
        step = 2
        score = 80L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_MBI_DEMOPIC_CreateModifyInterface_40_1:
        action = u'MBI'
        function = u'Create_Modify_Interface'
        step = 1
        score = 40L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_MBI_DEMOPIC_GetRecid_20_1:
        action = u'MBI'
        function = u'Get_Recid'
        step = 1
        score = 20L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_MBI_DEMOPIC_GetRecid_20_2:
        action = u'MBI'
        function = u'Get_Recid'
        step = 2
        score = 20L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_MBI_DEMOPIC_GetReportNumber_10_1:
        action = u'MBI'
        function = u'Get_Report_Number'
        step = 1
        score = 10L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_MBI_DEMOPIC_GetReportNumber_10_2:
        action = u'MBI'
        function = u'Get_Report_Number'
        step = 2
        score = 10L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_MBI_DEMOPIC_InsertModifyRecord_50_2:
        action = u'MBI'
        function = u'Insert_Modify_Record'
        step = 2
        score = 50L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_MBI_DEMOPIC_IsOriginalSubmitter_30_1:
        action = u'MBI'
        function = u'Is_Original_Submitter'
        step = 1
        score = 30L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_MBI_DEMOPIC_IsOriginalSubmitter_30_2:
        action = u'MBI'
        function = u'Is_Original_Submitter'
        step = 2
        score = 30L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_MBI_DEMOPIC_MakeModifyRecord_40_2:
        action = u'MBI'
        function = u'Make_Modify_Record'
        step = 2
        score = 40L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_MBI_DEMOPIC_MovePhotostoStorage_60_2:
        action = u'MBI'
        function = u'Move_Photos_to_Storage'
        step = 2
        score = 60L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_MBI_DEMOPIC_MovetoDone_90_2:
        action = u'MBI'
        function = u'Move_to_Done'
        step = 2
        score = 90L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_MBI_DEMOPIC_PrintSuccessMBI_70_2:
        action = u'MBI'
        function = u'Print_Success_MBI'
        step = 2
        score = 70L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_MBI_DEMOPIC_SendModifyMail_80_2:
        action = u'MBI'
        function = u'Send_Modify_Mail'
        step = 2
        score = 80L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_MBI_DEMOPOE_CreateModifyInterface_40_1:
        action = u'MBI'
        function = u'Create_Modify_Interface'
        step = 1
        score = 40L
        doctype = u'DEMOPOE'

    class SbmFUNCTIONS_MBI_DEMOPOE_GetRecid_20_1:
        action = u'MBI'
        function = u'Get_Recid'
        step = 1
        score = 20L
        doctype = u'DEMOPOE'

    class SbmFUNCTIONS_MBI_DEMOPOE_GetRecid_20_2:
        action = u'MBI'
        function = u'Get_Recid'
        step = 2
        score = 20L
        doctype = u'DEMOPOE'

    class SbmFUNCTIONS_MBI_DEMOPOE_GetReportNumber_10_1:
        action = u'MBI'
        function = u'Get_Report_Number'
        step = 1
        score = 10L
        doctype = u'DEMOPOE'

    class SbmFUNCTIONS_MBI_DEMOPOE_GetReportNumber_10_2:
        action = u'MBI'
        function = u'Get_Report_Number'
        step = 2
        score = 10L
        doctype = u'DEMOPOE'

    class SbmFUNCTIONS_MBI_DEMOPOE_InsertModifyRecord_50_2:
        action = u'MBI'
        function = u'Insert_Modify_Record'
        step = 2
        score = 50L
        doctype = u'DEMOPOE'

    class SbmFUNCTIONS_MBI_DEMOPOE_IsOriginalSubmitter_30_1:
        action = u'MBI'
        function = u'Is_Original_Submitter'
        step = 1
        score = 30L
        doctype = u'DEMOPOE'

    class SbmFUNCTIONS_MBI_DEMOPOE_IsOriginalSubmitter_30_2:
        action = u'MBI'
        function = u'Is_Original_Submitter'
        step = 2
        score = 30L
        doctype = u'DEMOPOE'

    class SbmFUNCTIONS_MBI_DEMOPOE_MakeModifyRecord_40_2:
        action = u'MBI'
        function = u'Make_Modify_Record'
        step = 2
        score = 40L
        doctype = u'DEMOPOE'

    class SbmFUNCTIONS_MBI_DEMOPOE_MovetoDone_80_2:
        action = u'MBI'
        function = u'Move_to_Done'
        step = 2
        score = 80L
        doctype = u'DEMOPOE'

    class SbmFUNCTIONS_MBI_DEMOPOE_PrintSuccessMBI_60_2:
        action = u'MBI'
        function = u'Print_Success_MBI'
        step = 2
        score = 60L
        doctype = u'DEMOPOE'

    class SbmFUNCTIONS_MBI_DEMOTHE_CreateModifyInterface_40_1:
        action = u'MBI'
        function = u'Create_Modify_Interface'
        step = 1
        score = 40L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_MBI_DEMOTHE_GetRecid_20_1:
        action = u'MBI'
        function = u'Get_Recid'
        step = 1
        score = 20L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_MBI_DEMOTHE_GetRecid_20_2:
        action = u'MBI'
        function = u'Get_Recid'
        step = 2
        score = 20L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_MBI_DEMOTHE_GetReportNumber_10_1:
        action = u'MBI'
        function = u'Get_Report_Number'
        step = 1
        score = 10L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_MBI_DEMOTHE_GetReportNumber_10_2:
        action = u'MBI'
        function = u'Get_Report_Number'
        step = 2
        score = 10L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_MBI_DEMOTHE_InsertModifyRecord_50_2:
        action = u'MBI'
        function = u'Insert_Modify_Record'
        step = 2
        score = 50L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_MBI_DEMOTHE_IsOriginalSubmitter_30_1:
        action = u'MBI'
        function = u'Is_Original_Submitter'
        step = 1
        score = 30L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_MBI_DEMOTHE_IsOriginalSubmitter_30_2:
        action = u'MBI'
        function = u'Is_Original_Submitter'
        step = 2
        score = 30L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_MBI_DEMOTHE_MakeModifyRecord_40_2:
        action = u'MBI'
        function = u'Make_Modify_Record'
        step = 2
        score = 40L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_MBI_DEMOTHE_MovetoDone_80_2:
        action = u'MBI'
        function = u'Move_to_Done'
        step = 2
        score = 80L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_MBI_DEMOTHE_PrintSuccessMBI_60_2:
        action = u'MBI'
        function = u'Print_Success_MBI'
        step = 2
        score = 60L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_MBI_DEMOTHE_SendModifyMail_70_2:
        action = u'MBI'
        function = u'Send_Modify_Mail'
        step = 2
        score = 70L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_SBI_DEMOART_CreateRecid_10_1:
        action = u'SBI'
        function = u'Create_Recid'
        step = 1
        score = 10L
        doctype = u'DEMOART'

    class SbmFUNCTIONS_SBI_DEMOART_InsertRecord_40_1:
        action = u'SBI'
        function = u'Insert_Record'
        step = 1
        score = 40L
        doctype = u'DEMOART'

    class SbmFUNCTIONS_SBI_DEMOART_MailSubmitter_60_1:
        action = u'SBI'
        function = u'Mail_Submitter'
        step = 1
        score = 60L
        doctype = u'DEMOART'

    class SbmFUNCTIONS_SBI_DEMOART_MakeRecord_30_1:
        action = u'SBI'
        function = u'Make_Record'
        step = 1
        score = 30L
        doctype = u'DEMOART'

    class SbmFUNCTIONS_SBI_DEMOART_PrintSuccess_50_1:
        action = u'SBI'
        function = u'Print_Success'
        step = 1
        score = 50L
        doctype = u'DEMOART'

    class SbmFUNCTIONS_SBI_DEMOART_ReportNumberGeneration_20_1:
        action = u'SBI'
        function = u'Report_Number_Generation'
        step = 1
        score = 20L
        doctype = u'DEMOART'

    class SbmFUNCTIONS_SBI_DEMOBOO_CreateRecid_10_1:
        action = u'SBI'
        function = u'Create_Recid'
        step = 1
        score = 10L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_SBI_DEMOBOO_MailSubmitter_50_1:
        action = u'SBI'
        function = u'Mail_Submitter'
        step = 1
        score = 50L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_SBI_DEMOBOO_MakeDummyMARCXMLRecord_30_1:
        action = u'SBI'
        function = u'Make_Dummy_MARC_XML_Record'
        step = 1
        score = 30L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_SBI_DEMOBOO_MoveFilestoStorage_40_1:
        action = u'SBI'
        function = u'Move_Files_to_Storage'
        step = 1
        score = 40L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_SBI_DEMOBOO_MovetoPending_90_1:
        action = u'SBI'
        function = u'Move_to_Pending'
        step = 1
        score = 90L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_SBI_DEMOBOO_PrintSuccess_80_1:
        action = u'SBI'
        function = u'Print_Success'
        step = 1
        score = 80L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_SBI_DEMOBOO_ReportNumberGeneration_20_1:
        action = u'SBI'
        function = u'Report_Number_Generation'
        step = 1
        score = 20L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_SBI_DEMOBOO_SendApprovalRequest_70_1:
        action = u'SBI'
        function = u'Send_Approval_Request'
        step = 1
        score = 70L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_SBI_DEMOBOO_UpdateApprovalDB_60_1:
        action = u'SBI'
        function = u'Update_Approval_DB'
        step = 1
        score = 60L
        doctype = u'DEMOBOO'

    class SbmFUNCTIONS_SBI_DEMOJRN_CreateRecid_10_1:
        action = u'SBI'
        function = u'Create_Recid'
        step = 1
        score = 10L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_SBI_DEMOJRN_InsertRecord_50_1:
        action = u'SBI'
        function = u'Insert_Record'
        step = 1
        score = 50L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_SBI_DEMOJRN_MailSubmitter_70_1:
        action = u'SBI'
        function = u'Mail_Submitter'
        step = 1
        score = 70L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_SBI_DEMOJRN_MakeRecord_40_1:
        action = u'SBI'
        function = u'Make_Record'
        step = 1
        score = 40L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_SBI_DEMOJRN_MoveCKEditorFilestoStorage_30_1:
        action = u'SBI'
        function = u'Move_CKEditor_Files_to_Storage'
        step = 1
        score = 30L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_SBI_DEMOJRN_MovetoDone_80_1:
        action = u'SBI'
        function = u'Move_to_Done'
        step = 1
        score = 80L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_SBI_DEMOJRN_PrintSuccess_60_1:
        action = u'SBI'
        function = u'Print_Success'
        step = 1
        score = 60L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_SBI_DEMOJRN_ReportNumberGeneration_20_1:
        action = u'SBI'
        function = u'Report_Number_Generation'
        step = 1
        score = 20L
        doctype = u'DEMOJRN'

    class SbmFUNCTIONS_SBI_DEMOPIC_CreateRecid_10_1:
        action = u'SBI'
        function = u'Create_Recid'
        step = 1
        score = 10L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_SBI_DEMOPIC_InsertRecord_40_1:
        action = u'SBI'
        function = u'Insert_Record'
        step = 1
        score = 40L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_SBI_DEMOPIC_MailSubmitter_70_1:
        action = u'SBI'
        function = u'Mail_Submitter'
        step = 1
        score = 70L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_SBI_DEMOPIC_MakeRecord_30_1:
        action = u'SBI'
        function = u'Make_Record'
        step = 1
        score = 30L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_SBI_DEMOPIC_MovePhotostoStorage_50_1:
        action = u'SBI'
        function = u'Move_Photos_to_Storage'
        step = 1
        score = 50L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_SBI_DEMOPIC_MovetoDone_80_1:
        action = u'SBI'
        function = u'Move_to_Done'
        step = 1
        score = 80L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_SBI_DEMOPIC_PrintSuccess_60_1:
        action = u'SBI'
        function = u'Print_Success'
        step = 1
        score = 60L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_SBI_DEMOPIC_ReportNumberGeneration_20_1:
        action = u'SBI'
        function = u'Report_Number_Generation'
        step = 1
        score = 20L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_SBI_DEMOPOE_CreateRecid_10_1:
        action = u'SBI'
        function = u'Create_Recid'
        step = 1
        score = 10L
        doctype = u'DEMOPOE'

    class SbmFUNCTIONS_SBI_DEMOPOE_InsertRecord_40_1:
        action = u'SBI'
        function = u'Insert_Record'
        step = 1
        score = 40L
        doctype = u'DEMOPOE'

    class SbmFUNCTIONS_SBI_DEMOPOE_MailSubmitter_60_1:
        action = u'SBI'
        function = u'Mail_Submitter'
        step = 1
        score = 60L
        doctype = u'DEMOPOE'

    class SbmFUNCTIONS_SBI_DEMOPOE_MakeRecord_30_1:
        action = u'SBI'
        function = u'Make_Record'
        step = 1
        score = 30L
        doctype = u'DEMOPOE'

    class SbmFUNCTIONS_SBI_DEMOPOE_MovetoDone_70_1:
        action = u'SBI'
        function = u'Move_to_Done'
        step = 1
        score = 70L
        doctype = u'DEMOPOE'

    class SbmFUNCTIONS_SBI_DEMOPOE_PrintSuccess_50_1:
        action = u'SBI'
        function = u'Print_Success'
        step = 1
        score = 50L
        doctype = u'DEMOPOE'

    class SbmFUNCTIONS_SBI_DEMOPOE_ReportNumberGeneration_20_1:
        action = u'SBI'
        function = u'Report_Number_Generation'
        step = 1
        score = 20L
        doctype = u'DEMOPOE'

    class SbmFUNCTIONS_SBI_DEMOTHE_CreateRecid_10_1:
        action = u'SBI'
        function = u'Create_Recid'
        step = 1
        score = 10L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_SBI_DEMOTHE_InsertRecord_60_1:
        action = u'SBI'
        function = u'Insert_Record'
        step = 1
        score = 60L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_SBI_DEMOTHE_MailSubmitter_80_1:
        action = u'SBI'
        function = u'Mail_Submitter'
        step = 1
        score = 80L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_SBI_DEMOTHE_MakeRecord_50_1:
        action = u'SBI'
        function = u'Make_Record'
        step = 1
        score = 50L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_SBI_DEMOTHE_MoveFilestoStorage_40_1:
        action = u'SBI'
        function = u'Move_Files_to_Storage'
        step = 1
        score = 40L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_SBI_DEMOTHE_MovetoDone_90_1:
        action = u'SBI'
        function = u'Move_to_Done'
        step = 1
        score = 90L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_SBI_DEMOTHE_PrintSuccess_70_1:
        action = u'SBI'
        function = u'Print_Success'
        step = 1
        score = 70L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_SBI_DEMOTHE_ReportNumberGeneration_20_1:
        action = u'SBI'
        function = u'Report_Number_Generation'
        step = 1
        score = 20L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_SBI_DEMOTHE_StampUploadedFiles_30_1:
        action = u'SBI'
        function = u'Stamp_Uploaded_Files'
        step = 1
        score = 30L
        doctype = u'DEMOTHE'

    class SbmFUNCTIONS_SBI_DEMOVID_CreateRecid_10_1:
        action = u'SBI'
        function = u'Create_Recid'
        step = 1
        score = 10L
        doctype = u'DEMOVID'

    class SbmFUNCTIONS_SBI_DEMOVID_InsertRecord_40_1:
        action = u'SBI'
        function = u'Insert_Record'
        step = 1
        score = 40L
        doctype = u'DEMOVID'

    class SbmFUNCTIONS_SBI_DEMOVID_MailSubmitter_60_1:
        action = u'SBI'
        function = u'Mail_Submitter'
        step = 1
        score = 60L
        doctype = u'DEMOVID'

    class SbmFUNCTIONS_SBI_DEMOVID_MakeRecord_30_1:
        action = u'SBI'
        function = u'Make_Record'
        step = 1
        score = 30L
        doctype = u'DEMOVID'

    class SbmFUNCTIONS_SBI_DEMOVID_PrintSuccess_50_1:
        action = u'SBI'
        function = u'Print_Success'
        step = 1
        score = 50L
        doctype = u'DEMOVID'

    class SbmFUNCTIONS_SBI_DEMOVID_ReportNumberGeneration_20_1:
        action = u'SBI'
        function = u'Report_Number_Generation'
        step = 1
        score = 20L
        doctype = u'DEMOVID'

    class SbmFUNCTIONS_SBI_DEMOVID_VideoProcessing_70_1:
        action = u'SBI'
        function = u'Video_Processing'
        step = 1
        score = 70L
        doctype = u'DEMOVID'

    class SbmFUNCTIONS_SRV_DEMOPIC_CreateUploadFilesInterface_40_1:
        action = u'SRV'
        function = u'Create_Upload_Files_Interface'
        step = 1
        score = 40L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_SRV_DEMOPIC_GetRecid_10_2:
        action = u'SRV'
        function = u'Get_Recid'
        step = 2
        score = 10L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_SRV_DEMOPIC_GetRecid_20_1:
        action = u'SRV'
        function = u'Get_Recid'
        step = 1
        score = 20L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_SRV_DEMOPIC_GetReportNumber_10_1:
        action = u'SRV'
        function = u'Get_Report_Number'
        step = 1
        score = 10L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_SRV_DEMOPIC_IsOriginalSubmitter_20_2:
        action = u'SRV'
        function = u'Is_Original_Submitter'
        step = 2
        score = 20L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_SRV_DEMOPIC_IsOriginalSubmitter_30_1:
        action = u'SRV'
        function = u'Is_Original_Submitter'
        step = 1
        score = 30L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_SRV_DEMOPIC_MailSubmitter_40_2:
        action = u'SRV'
        function = u'Mail_Submitter'
        step = 2
        score = 40L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_SRV_DEMOPIC_MoveUploadedFilestoStorage_30_2:
        action = u'SRV'
        function = u'Move_Uploaded_Files_to_Storage'
        step = 2
        score = 30L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_SRV_DEMOPIC_MovetoDone_60_2:
        action = u'SRV'
        function = u'Move_to_Done'
        step = 2
        score = 60L
        doctype = u'DEMOPIC'

    class SbmFUNCTIONS_SRV_DEMOPIC_PrintSuccess_50_2:
        action = u'SRV'
        function = u'Print_Success'
        step = 2
        score = 50L
        doctype = u'DEMOPIC'


class SbmIMPLEMENTData(DataSet):

    class SbmIMPLEMENT_APPDEMOBOO_1:
        md = datetime.date(2002, 5, 28)
        stpage = 1L
        endtxt = u''
        level = u'0'
        statustext = u'0'
        nbpg = 1L
        displayed = u'Y'
        buttonorder = 3L
        score = 0L
        subname = u'APPDEMOBOO'
        docname = u'DEMOBOO'
        actname = u'APP'
        cd = datetime.date(2002, 5, 6)

    class SbmIMPLEMENT_MBIDEMOART_1:
        md = datetime.date(2008, 3, 7)
        stpage = 0L
        endtxt = u''
        level = u''
        statustext = u''
        nbpg = 1L
        displayed = u'Y'
        buttonorder = 2L
        score = 0L
        subname = u'MBIDEMOART'
        docname = u'DEMOART'
        actname = u'MBI'
        cd = datetime.date(2008, 3, 7)

    class SbmIMPLEMENT_MBIDEMOBOO_1:
        md = datetime.date(2008, 3, 7)
        stpage = 0L
        endtxt = u''
        level = u''
        statustext = u''
        nbpg = 1L
        displayed = u'Y'
        buttonorder = 2L
        score = 0L
        subname = u'MBIDEMOBOO'
        docname = u'DEMOBOO'
        actname = u'MBI'
        cd = datetime.date(2008, 3, 7)

    class SbmIMPLEMENT_MBIDEMOJRN_1:
        md = datetime.date(2009, 2, 23)
        stpage = 0L
        endtxt = u''
        level = u''
        statustext = u''
        nbpg = 1L
        displayed = u'Y'
        buttonorder = 2L
        score = 0L
        subname = u'MBIDEMOJRN'
        docname = u'DEMOJRN'
        actname = u'MBI'
        cd = datetime.date(2008, 9, 18)

    class SbmIMPLEMENT_MBIDEMOPIC_1:
        md = datetime.date(2007, 10, 4)
        stpage = 0L
        endtxt = u''
        level = u''
        statustext = u''
        nbpg = 1L
        displayed = u'Y'
        buttonorder = 2L
        score = 0L
        subname = u'MBIDEMOPIC'
        docname = u'DEMOPIC'
        actname = u'MBI'
        cd = datetime.date(2007, 10, 4)

    class SbmIMPLEMENT_MBIDEMOPOE_1:
        md = datetime.date(2008, 3, 12)
        stpage = 0L
        endtxt = u''
        level = u''
        statustext = u''
        nbpg = 1L
        displayed = u'Y'
        buttonorder = 2L
        score = 0L
        subname = u'MBIDEMOPOE'
        docname = u'DEMOPOE'
        actname = u'MBI'
        cd = datetime.date(2008, 3, 12)

    class SbmIMPLEMENT_MBIDEMOTHE_1:
        md = datetime.date(2008, 3, 5)
        stpage = 0L
        endtxt = u''
        level = u''
        statustext = u''
        nbpg = 1L
        displayed = u'Y'
        buttonorder = 2L
        score = 0L
        subname = u'MBIDEMOTHE'
        docname = u'DEMOTHE'
        actname = u'MBI'
        cd = datetime.date(2008, 3, 5)

    class SbmIMPLEMENT_SBIDEMOART_1:
        md = datetime.date(2008, 3, 7)
        stpage = 0L
        endtxt = u''
        level = u''
        statustext = u''
        nbpg = 1L
        displayed = u'Y'
        buttonorder = 1L
        score = 0L
        subname = u'SBIDEMOART'
        docname = u'DEMOART'
        actname = u'SBI'
        cd = datetime.date(2008, 3, 6)

    class SbmIMPLEMENT_SBIDEMOBOO_1:
        md = datetime.date(2008, 3, 7)
        stpage = 0L
        endtxt = u''
        level = u''
        statustext = u''
        nbpg = 1L
        displayed = u'Y'
        buttonorder = 1L
        score = 0L
        subname = u'SBIDEMOBOO'
        docname = u'DEMOBOO'
        actname = u'SBI'
        cd = datetime.date(2008, 3, 6)

    class SbmIMPLEMENT_SBIDEMOJRN_1:
        md = datetime.date(2009, 2, 23)
        stpage = 0L
        endtxt = u''
        level = u''
        statustext = u''
        nbpg = 1L
        displayed = u'Y'
        buttonorder = 1L
        score = 0L
        subname = u'SBIDEMOJRN'
        docname = u'DEMOJRN'
        actname = u'SBI'
        cd = datetime.date(2008, 9, 18)

    class SbmIMPLEMENT_SBIDEMOPIC_1:
        md = datetime.date(2007, 10, 4)
        stpage = 0L
        endtxt = u''
        level = u''
        statustext = u''
        nbpg = 1L
        displayed = u'Y'
        buttonorder = 1L
        score = 0L
        subname = u'SBIDEMOPIC'
        docname = u'DEMOPIC'
        actname = u'SBI'
        cd = datetime.date(2007, 9, 13)

    class SbmIMPLEMENT_SBIDEMOPOE_2:
        md = datetime.date(2008, 3, 12)
        stpage = 0L
        endtxt = u''
        level = u''
        statustext = u''
        nbpg = 2L
        displayed = u'Y'
        buttonorder = 1L
        score = 0L
        subname = u'SBIDEMOPOE'
        docname = u'DEMOPOE'
        actname = u'SBI'
        cd = datetime.date(2008, 3, 12)

    class SbmIMPLEMENT_SBIDEMOTHE_1:
        md = datetime.date(2008, 3, 5)
        stpage = 0L
        endtxt = u''
        level = u'1'
        statustext = u''
        nbpg = 1L
        displayed = u'Y'
        buttonorder = 1L
        score = 1L
        subname = u'SBIDEMOTHE'
        docname = u'DEMOTHE'
        actname = u'SBI'
        cd = datetime.date(2008, 3, 2)

    class SbmIMPLEMENT_SBIDEMOVID_1:
        md = datetime.date(2012, 2, 16)
        stpage = 0L
        endtxt = u''
        level = u''
        statustext = u''
        nbpg = 1L
        displayed = u'Y'
        buttonorder = 1L
        score = 0L
        subname = u'SBIDEMOVID'
        docname = u'DEMOVID'
        actname = u'SBI'
        cd = datetime.date(2012, 2, 16)

    class SbmIMPLEMENT_SRVDEMOPIC_1:
        md = datetime.date(2009, 4, 9)
        stpage = 0L
        endtxt = u''
        level = u''
        statustext = u''
        nbpg = 1L
        displayed = u'Y'
        buttonorder = 3L
        score = 0L
        subname = u'SRVDEMOPIC'
        docname = u'DEMOPIC'
        actname = u'SRV'
        cd = datetime.date(2009, 4, 9)


class SbmPARAMETERSData(DataSet):

    class SbmPARAMETERS_DEMOART_addressesMBI:
        doctype = u'DEMOART'
        value = u''
        name = u'addressesMBI'

    class SbmPARAMETERS_DEMOART_authorfile:
        doctype = u'DEMOART'
        value = u'DEMOART_AU'
        name = u'authorfile'

    class SbmPARAMETERS_DEMOART_autorngen:
        doctype = u'DEMOART'
        value = u'Y'
        name = u'autorngen'

    class SbmPARAMETERS_DEMOART_counterpath:
        doctype = u'DEMOART'
        value = u'lastid_DEMOART_<PA>categ</PA>_<PA>yy</PA>'
        name = u'counterpath'

    class SbmPARAMETERS_DEMOART_createTemplate:
        doctype = u'DEMOART'
        value = u'DEMOARTcreate.tpl'
        name = u'createTemplate'

    class SbmPARAMETERS_DEMOART_documenttype:
        doctype = u'DEMOART'
        value = u'fulltext'
        name = u'documenttype'

    class SbmPARAMETERS_DEMOART_edsrn:
        doctype = u'DEMOART'
        value = u'DEMOART_RN'
        name = u'edsrn'

    class SbmPARAMETERS_DEMOART_emailFile:
        doctype = u'DEMOART'
        value = u'SuE'
        name = u'emailFile'

    class SbmPARAMETERS_DEMOART_fieldnameMBI:
        doctype = u'DEMOART'
        value = u'DEMOART_CHANGE'
        name = u'fieldnameMBI'

    class SbmPARAMETERS_DEMOART_iconsize:
        doctype = u'DEMOART'
        value = u'180'
        name = u'iconsize'

    class SbmPARAMETERS_DEMOART_modifyTemplate:
        doctype = u'DEMOART'
        value = u'DEMOARTmodify.tpl'
        name = u'modifyTemplate'

    class SbmPARAMETERS_DEMOART_newrnin:
        doctype = u'DEMOART'
        value = u''
        name = u'newrnin'

    class SbmPARAMETERS_DEMOART_pathsandsuffixes:
        doctype = u'DEMOART'
        value = u'{"DEMOART_FILE":""}'
        name = u'paths_and_suffixes'

    class SbmPARAMETERS_DEMOART_rename:
        doctype = u'DEMOART'
        value = u'<PA>file:DEMOART_RN</PA>'
        name = u'rename'

    class SbmPARAMETERS_DEMOART_rnformat:
        doctype = u'DEMOART'
        value = u'DEMO-<PA>categ</PA>-<PA>yy</PA>'
        name = u'rnformat'

    class SbmPARAMETERS_DEMOART_rnin:
        doctype = u'DEMOART'
        value = u'comboDEMOART'
        name = u'rnin'

    class SbmPARAMETERS_DEMOART_sourceDoc:
        doctype = u'DEMOART'
        value = u'Textual Document'
        name = u'sourceDoc'

    class SbmPARAMETERS_DEMOART_sourceTemplate:
        doctype = u'DEMOART'
        value = u'DEMOART.tpl'
        name = u'sourceTemplate'

    class SbmPARAMETERS_DEMOART_status:
        doctype = u'DEMOART'
        value = u'ADDED'
        name = u'status'

    class SbmPARAMETERS_DEMOART_titleFile:
        doctype = u'DEMOART'
        value = u'DEMOART_TITLE'
        name = u'titleFile'

    class SbmPARAMETERS_DEMOART_yeargen:
        doctype = u'DEMOART'
        value = u'AUTO'
        name = u'yeargen'

    class SbmPARAMETERS_DEMOBOO_addressesAPP:
        doctype = u'DEMOBOO'
        value = u''
        name = u'addressesAPP'

    class SbmPARAMETERS_DEMOBOO_addressesDAM:
        doctype = u'DEMOBOO'
        value = u''
        name = u'addressesDAM'

    class SbmPARAMETERS_DEMOBOO_addressesMBI:
        doctype = u'DEMOBOO'
        value = u''
        name = u'addressesMBI'

    class SbmPARAMETERS_DEMOBOO_authorfile:
        doctype = u'DEMOBOO'
        value = u'DEMOBOO_AU'
        name = u'authorfile'

    class SbmPARAMETERS_DEMOBOO_autorngen:
        doctype = u'DEMOBOO'
        value = u'Y'
        name = u'autorngen'

    class SbmPARAMETERS_DEMOBOO_casedefault:
        doctype = u'DEMOBOO'
        value = u''
        name = u'casedefault'

    class SbmPARAMETERS_DEMOBOO_casesteps:
        doctype = u'DEMOBOO'
        value = u'2,3'
        name = u'casesteps'

    class SbmPARAMETERS_DEMOBOO_casevalues:
        doctype = u'DEMOBOO'
        value = u'approve,reject'
        name = u'casevalues'

    class SbmPARAMETERS_DEMOBOO_casevariable:
        doctype = u'DEMOBOO'
        value = u'DEMOBOO_DECSN'
        name = u'casevariable'

    class SbmPARAMETERS_DEMOBOO_categformatAPP:
        doctype = u'DEMOBOO'
        value = u''
        name = u'categformatAPP'

    class SbmPARAMETERS_DEMOBOO_categformatDAM:
        doctype = u'DEMOBOO'
        value = u''
        name = u'categformatDAM'

    class SbmPARAMETERS_DEMOBOO_commentsfile:
        doctype = u'DEMOBOO'
        value = u'DEMOBOO_COMNT'
        name = u'comments_file'

    class SbmPARAMETERS_DEMOBOO_counterpath:
        doctype = u'DEMOBOO'
        value = u'lastid_DEMOBOO_<PA>yy</PA>'
        name = u'counterpath'

    class SbmPARAMETERS_DEMOBOO_createTemplate:
        doctype = u'DEMOBOO'
        value = u'DEMOBOOcreate.tpl'
        name = u'createTemplate'

    class SbmPARAMETERS_DEMOBOO_decisionfile:
        doctype = u'DEMOBOO'
        value = u'DEMOBOO_DECSN'
        name = u'decision_file'

    class SbmPARAMETERS_DEMOBOO_directory:
        doctype = u'DEMOBOO'
        value = u'DEMOBOO'
        name = u'directory'

    class SbmPARAMETERS_DEMOBOO_documenttype:
        doctype = u'DEMOBOO'
        value = u'fulltext'
        name = u'documenttype'

    class SbmPARAMETERS_DEMOBOO_dummyreccreatetpl:
        doctype = u'DEMOBOO'
        value = u'DEMOBOOcreate.tpl'
        name = u'dummyrec_create_tpl'

    class SbmPARAMETERS_DEMOBOO_dummyrecsourcetpl:
        doctype = u'DEMOBOO'
        value = u'DEMOBOO.tpl'
        name = u'dummyrec_source_tpl'

    class SbmPARAMETERS_DEMOBOO_edsrn:
        doctype = u'DEMOBOO'
        value = u'DEMOBOO_RN'
        name = u'edsrn'

    class SbmPARAMETERS_DEMOBOO_elementNameToDoctype:
        doctype = u'DEMOBOO'
        value = u'DEMOBOO_FILE=DEMOBOO_FILE'
        name = u'elementNameToDoctype'

    class SbmPARAMETERS_DEMOBOO_emailFile:
        doctype = u'DEMOBOO'
        value = u'SuE'
        name = u'emailFile'

    class SbmPARAMETERS_DEMOBOO_fieldnameMBI:
        doctype = u'DEMOBOO'
        value = u'DEMOBOO_CHANGE'
        name = u'fieldnameMBI'

    class SbmPARAMETERS_DEMOBOO_iconsize:
        doctype = u'DEMOBOO'
        value = u'180>,700>'
        name = u'iconsize'

    class SbmPARAMETERS_DEMOBOO_modifyTemplate:
        doctype = u'DEMOBOO'
        value = u'DEMOBOOmodify.tpl'
        name = u'modifyTemplate'

    class SbmPARAMETERS_DEMOBOO_newrnin:
        doctype = u'DEMOBOO'
        value = u'NEWRN'
        name = u'newrnin'

    class SbmPARAMETERS_DEMOBOO_pathsandsuffixes:
        doctype = u'DEMOBOO'
        value = u'{"DEMOBOO_FILE":""}'
        name = u'paths_and_suffixes'

    class SbmPARAMETERS_DEMOBOO_rename:
        doctype = u'DEMOBOO'
        value = u'<PA>file:DEMOBOO_RN</PA>'
        name = u'rename'

    class SbmPARAMETERS_DEMOBOO_rnformat:
        doctype = u'DEMOBOO'
        value = u'DEMO-BOOK-<PA>yy</PA>'
        name = u'rnformat'

    class SbmPARAMETERS_DEMOBOO_rnin:
        doctype = u'DEMOBOO'
        value = u'comboDEMOBOO'
        name = u'rnin'

    class SbmPARAMETERS_DEMOBOO_sourceDoc:
        doctype = u'DEMOBOO'
        value = u'BOOK'
        name = u'sourceDoc'

    class SbmPARAMETERS_DEMOBOO_sourceTemplate:
        doctype = u'DEMOBOO'
        value = u'DEMOBOO.tpl'
        name = u'sourceTemplate'

    class SbmPARAMETERS_DEMOBOO_status:
        doctype = u'DEMOBOO'
        value = u'APPROVAL'
        name = u'status'

    class SbmPARAMETERS_DEMOBOO_titleFile:
        doctype = u'DEMOBOO'
        value = u'DEMOBOO_TITLE'
        name = u'titleFile'

    class SbmPARAMETERS_DEMOBOO_yeargen:
        doctype = u'DEMOBOO'
        value = u'AUTO'
        name = u'yeargen'

    class SbmPARAMETERS_DEMOJRN_addressesMBI:
        doctype = u'DEMOJRN'
        value = u''
        name = u'addressesMBI'

    class SbmPARAMETERS_DEMOJRN_authorfile:
        doctype = u'DEMOJRN'
        value = u'DEMOJRN_AU'
        name = u'authorfile'

    class SbmPARAMETERS_DEMOJRN_autorngen:
        doctype = u'DEMOJRN'
        value = u'Y'
        name = u'autorngen'

    class SbmPARAMETERS_DEMOJRN_counterpath:
        doctype = u'DEMOJRN'
        value = u'lastid_DEMOJRN_<PA>categ</PA>_<PA>yy</PA>'
        name = u'counterpath'

    class SbmPARAMETERS_DEMOJRN_createTemplate:
        doctype = u'DEMOJRN'
        value = u'DEMOJRNcreate.tpl'
        name = u'createTemplate'

    class SbmPARAMETERS_DEMOJRN_documenttype:
        doctype = u'DEMOJRN'
        value = u'picture'
        name = u'documenttype'

    class SbmPARAMETERS_DEMOJRN_edsrn:
        doctype = u'DEMOJRN'
        value = u'DEMOJRN_RN'
        name = u'edsrn'

    class SbmPARAMETERS_DEMOJRN_emailFile:
        doctype = u'DEMOJRN'
        value = u'SuE'
        name = u'emailFile'

    class SbmPARAMETERS_DEMOJRN_fieldnameMBI:
        doctype = u'DEMOJRN'
        value = u'DEMOJRN_CHANGE'
        name = u'fieldnameMBI'

    class SbmPARAMETERS_DEMOJRN_files:
        doctype = u'DEMOJRN'
        value = u'DEMOJRN_ABSE,DEMOJRN_ABSF'
        name = u'files'

    class SbmPARAMETERS_DEMOJRN_iconsize:
        doctype = u'DEMOJRN'
        value = u'300>'
        name = u'iconsize'

    class SbmPARAMETERS_DEMOJRN_inputfields:
        doctype = u'DEMOJRN'
        value = u'DEMOJRN_ABSE,DEMOJRN_ABSF'
        name = u'input_fields'

    class SbmPARAMETERS_DEMOJRN_modifyTemplate:
        doctype = u'DEMOJRN'
        value = u'DEMOJRNmodify.tpl'
        name = u'modifyTemplate'

    class SbmPARAMETERS_DEMOJRN_newrnin:
        doctype = u'DEMOJRN'
        value = u''
        name = u'newrnin'

    class SbmPARAMETERS_DEMOJRN_pathsandsuffixes:
        doctype = u'DEMOJRN'
        value = u'{\'image\':"image", \'file\':"file", \'flash\':"flash", \'media\':\'media\'}'
        name = u'paths_and_suffixes'

    class SbmPARAMETERS_DEMOJRN_recordsearchpattern:
        doctype = u'DEMOJRN'
        value = u'collection:ATLANTISTIMES*'
        name = u'record_search_pattern'

    class SbmPARAMETERS_DEMOJRN_rename:
        doctype = u'DEMOJRN'
        value = u''
        name = u'rename'

    class SbmPARAMETERS_DEMOJRN_rnformat:
        doctype = u'DEMOJRN'
        value = u'BUL-<PA>categ</PA>-<PA>yy</PA>'
        name = u'rnformat'

    class SbmPARAMETERS_DEMOJRN_rnin:
        doctype = u'DEMOJRN'
        value = u'comboDEMOJRN'
        name = u'rnin'

    class SbmPARAMETERS_DEMOJRN_sourceDoc:
        doctype = u'DEMOJRN'
        value = u'Textual Document'
        name = u'sourceDoc'

    class SbmPARAMETERS_DEMOJRN_sourceTemplate:
        doctype = u'DEMOJRN'
        value = u'DEMOJRN.tpl'
        name = u'sourceTemplate'

    class SbmPARAMETERS_DEMOJRN_status:
        doctype = u'DEMOJRN'
        value = u'ADDED'
        name = u'status'

    class SbmPARAMETERS_DEMOJRN_titleFile:
        doctype = u'DEMOJRN'
        value = u'DEMOJRN_TITLEE'
        name = u'titleFile'

    class SbmPARAMETERS_DEMOJRN_yeargen:
        doctype = u'DEMOJRN'
        value = u'AUTO'
        name = u'yeargen'

    class SbmPARAMETERS_DEMOPIC_addressesMBI:
        doctype = u'DEMOPIC'
        value = u''
        name = u'addressesMBI'

    class SbmPARAMETERS_DEMOPIC_authorfile:
        doctype = u'DEMOPIC'
        value = u'DEMOPIC_PHOTOG'
        name = u'authorfile'

    class SbmPARAMETERS_DEMOPIC_autorngen:
        doctype = u'DEMOPIC'
        value = u'Y'
        name = u'autorngen'

    class SbmPARAMETERS_DEMOPIC_canAddFormatDoctypes:
        doctype = u'DEMOPIC'
        value = u'DEMOPIC_FILE'
        name = u'canAddFormatDoctypes'

    class SbmPARAMETERS_DEMOPIC_canCommentDoctypes:
        doctype = u'DEMOPIC'
        value = u'*'
        name = u'canCommentDoctypes'

    class SbmPARAMETERS_DEMOPIC_canDeleteDoctypes:
        doctype = u'DEMOPIC'
        value = u'*'
        name = u'canDeleteDoctypes'

    class SbmPARAMETERS_DEMOPIC_canNameNewFiles:
        doctype = u'DEMOPIC'
        value = u'1'
        name = u'canNameNewFiles'

    class SbmPARAMETERS_DEMOPIC_canRenameDoctypes:
        doctype = u'DEMOPIC'
        value = u''
        name = u'canRenameDoctypes'

    class SbmPARAMETERS_DEMOPIC_canRestrictDoctypes:
        doctype = u'DEMOPIC'
        value = u'*'
        name = u'canRestrictDoctypes'

    class SbmPARAMETERS_DEMOPIC_canReviseDoctypes:
        doctype = u'DEMOPIC'
        value = u'*'
        name = u'canReviseDoctypes'

    class SbmPARAMETERS_DEMOPIC_counterpath:
        doctype = u'DEMOPIC'
        value = u'lastid_DEMOPIC_<PA>categ</PA>_<PA>yy</PA>'
        name = u'counterpath'

    class SbmPARAMETERS_DEMOPIC_createIconDoctypes:
        doctype = u'DEMOPIC'
        value = u'*'
        name = u'createIconDoctypes'

    class SbmPARAMETERS_DEMOPIC_createTemplate:
        doctype = u'DEMOPIC'
        value = u'DEMOPICcreate.tpl'
        name = u'createTemplate'

    class SbmPARAMETERS_DEMOPIC_doctypes:
        doctype = u'DEMOPIC'
        value = u'DEMOPIC_FILE=Picture|Additional=Additional Document'
        name = u'doctypes'

    class SbmPARAMETERS_DEMOPIC_documenttype:
        doctype = u'DEMOPIC'
        value = u'picture'
        name = u'documenttype'

    class SbmPARAMETERS_DEMOPIC_edsrn:
        doctype = u'DEMOPIC'
        value = u'DEMOPIC_RN'
        name = u'edsrn'

    class SbmPARAMETERS_DEMOPIC_emailFile:
        doctype = u'DEMOPIC'
        value = u'SuE'
        name = u'emailFile'

    class SbmPARAMETERS_DEMOPIC_fieldnameMBI:
        doctype = u'DEMOPIC'
        value = u'DEMOPIC_CHANGE'
        name = u'fieldnameMBI'

    class SbmPARAMETERS_DEMOPIC_forceFileRevision:
        doctype = u'DEMOPIC'
        value = u''
        name = u'forceFileRevision'

    class SbmPARAMETERS_DEMOPIC_iconsize:
        doctype = u'DEMOPIC'
        value = u'180>,700>'
        name = u'iconsize'

    class SbmPARAMETERS_DEMOPIC_keepDefault:
        doctype = u'DEMOPIC'
        value = u'1'
        name = u'keepDefault'

    class SbmPARAMETERS_DEMOPIC_maxFilesDoctypes:
        doctype = u'DEMOPIC'
        value = u'Additional=1'
        name = u'maxFilesDoctypes'

    class SbmPARAMETERS_DEMOPIC_modifyTemplate:
        doctype = u'DEMOPIC'
        value = u'DEMOPICmodify.tpl'
        name = u'modifyTemplate'

    class SbmPARAMETERS_DEMOPIC_newrnin:
        doctype = u'DEMOPIC'
        value = u'NEWRN'
        name = u'newrnin'

    class SbmPARAMETERS_DEMOPIC_pathsandsuffixes:
        doctype = u'DEMOPIC'
        value = u'{"DEMOPIC_FILE":""}'
        name = u'paths_and_suffixes'

    class SbmPARAMETERS_DEMOPIC_rename:
        doctype = u'DEMOPIC'
        value = u'<PA>file:DEMOPIC_RN</PA>'
        name = u'rename'

    class SbmPARAMETERS_DEMOPIC_restrictions:
        doctype = u'DEMOPIC'
        value = u'=Public|restricted_picture=Private'
        name = u'restrictions'

    class SbmPARAMETERS_DEMOPIC_rnformat:
        doctype = u'DEMOPIC'
        value = u'DEMO-PICTURE-<PA>categ</PA>-<PA>yy</PA>'
        name = u'rnformat'

    class SbmPARAMETERS_DEMOPIC_rnin:
        doctype = u'DEMOPIC'
        value = u'comboDEMOPIC'
        name = u'rnin'

    class SbmPARAMETERS_DEMOPIC_showLinks:
        doctype = u'DEMOPIC'
        value = u'1'
        name = u'showLinks'

    class SbmPARAMETERS_DEMOPIC_sourceDoc:
        doctype = u'DEMOPIC'
        value = u'photos'
        name = u'sourceDoc'

    class SbmPARAMETERS_DEMOPIC_sourceTemplate:
        doctype = u'DEMOPIC'
        value = u'DEMOPIC.tpl'
        name = u'sourceTemplate'

    class SbmPARAMETERS_DEMOPIC_status:
        doctype = u'DEMOPIC'
        value = u'ADDED'
        name = u'status'

    class SbmPARAMETERS_DEMOPIC_titleFile:
        doctype = u'DEMOPIC'
        value = u'DEMOPIC_TITLE'
        name = u'titleFile'

    class SbmPARAMETERS_DEMOPIC_yeargen:
        doctype = u'DEMOPIC'
        value = u'AUTO'
        name = u'yeargen'

    class SbmPARAMETERS_DEMOPOE_addressesMBI:
        doctype = u'DEMOPOE'
        value = u''
        name = u'addressesMBI'

    class SbmPARAMETERS_DEMOPOE_authorfile:
        doctype = u'DEMOPOE'
        value = u'DEMOPOE_AU'
        name = u'authorfile'

    class SbmPARAMETERS_DEMOPOE_autorngen:
        doctype = u'DEMOPOE'
        value = u'Y'
        name = u'autorngen'

    class SbmPARAMETERS_DEMOPOE_counterpath:
        doctype = u'DEMOPOE'
        value = u'lastid_DEMOPOE_<PA>yy</PA>'
        name = u'counterpath'

    class SbmPARAMETERS_DEMOPOE_createTemplate:
        doctype = u'DEMOPOE'
        value = u'DEMOPOEcreate.tpl'
        name = u'createTemplate'

    class SbmPARAMETERS_DEMOPOE_edsrn:
        doctype = u'DEMOPOE'
        value = u'DEMOPOE_RN'
        name = u'edsrn'

    class SbmPARAMETERS_DEMOPOE_emailFile:
        doctype = u'DEMOPOE'
        value = u'SuE'
        name = u'emailFile'

    class SbmPARAMETERS_DEMOPOE_fieldnameMBI:
        doctype = u'DEMOPOE'
        value = u'DEMOPOE_CHANGE'
        name = u'fieldnameMBI'

    class SbmPARAMETERS_DEMOPOE_modifyTemplate:
        doctype = u'DEMOPOE'
        value = u'DEMOPOEmodify.tpl'
        name = u'modifyTemplate'

    class SbmPARAMETERS_DEMOPOE_newrnin:
        doctype = u'DEMOPOE'
        value = u''
        name = u'newrnin'

    class SbmPARAMETERS_DEMOPOE_rnformat:
        doctype = u'DEMOPOE'
        value = u'DEMO-POETRY-<PA>yy</PA>'
        name = u'rnformat'

    class SbmPARAMETERS_DEMOPOE_rnin:
        doctype = u'DEMOPOE'
        value = u'comboDEMOPOE'
        name = u'rnin'

    class SbmPARAMETERS_DEMOPOE_sourceDoc:
        doctype = u'DEMOPOE'
        value = u'Poem'
        name = u'sourceDoc'

    class SbmPARAMETERS_DEMOPOE_sourceTemplate:
        doctype = u'DEMOPOE'
        value = u'DEMOPOE.tpl'
        name = u'sourceTemplate'

    class SbmPARAMETERS_DEMOPOE_status:
        doctype = u'DEMOPOE'
        value = u'ADDED'
        name = u'status'

    class SbmPARAMETERS_DEMOPOE_titleFile:
        doctype = u'DEMOPOE'
        value = u'DEMOPOE_TITLE'
        name = u'titleFile'

    class SbmPARAMETERS_DEMOPOE_yeargen:
        doctype = u'DEMOPOE'
        value = u'AUTO'
        name = u'yeargen'

    class SbmPARAMETERS_DEMOTHE_addressesMBI:
        doctype = u'DEMOTHE'
        value = u''
        name = u'addressesMBI'

    class SbmPARAMETERS_DEMOTHE_authorfile:
        doctype = u'DEMOTHE'
        value = u'DEMOTHE_AU'
        name = u'authorfile'

    class SbmPARAMETERS_DEMOTHE_autorngen:
        doctype = u'DEMOTHE'
        value = u'Y'
        name = u'autorngen'

    class SbmPARAMETERS_DEMOTHE_counterpath:
        doctype = u'DEMOTHE'
        value = u'lastid_DEMOTHE_<PA>yy</PA>'
        name = u'counterpath'

    class SbmPARAMETERS_DEMOTHE_createTemplate:
        doctype = u'DEMOTHE'
        value = u'DEMOTHEcreate.tpl'
        name = u'createTemplate'

    class SbmPARAMETERS_DEMOTHE_documenttype:
        doctype = u'DEMOTHE'
        value = u'fulltext'
        name = u'documenttype'

    class SbmPARAMETERS_DEMOTHE_edsrn:
        doctype = u'DEMOTHE'
        value = u'DEMOTHE_RN'
        name = u'edsrn'

    class SbmPARAMETERS_DEMOTHE_emailFile:
        doctype = u'DEMOTHE'
        value = u'SuE'
        name = u'emailFile'

    class SbmPARAMETERS_DEMOTHE_fieldnameMBI:
        doctype = u'DEMOTHE'
        value = u'DEMOTHE_CHANGE'
        name = u'fieldnameMBI'

    class SbmPARAMETERS_DEMOTHE_filestobestamped:
        doctype = u'DEMOTHE'
        value = u'DEMOTHE_FILE'
        name = u'files_to_be_stamped'

    class SbmPARAMETERS_DEMOTHE_iconsize:
        doctype = u'DEMOTHE'
        value = u'180>,700>'
        name = u'iconsize'

    class SbmPARAMETERS_DEMOTHE_latextemplate:
        doctype = u'DEMOTHE'
        value = u'demo-stamp-left.tex'
        name = u'latex_template'

    class SbmPARAMETERS_DEMOTHE_latextemplatevars:
        doctype = u'DEMOTHE'
        value = u"{'REPORTNUMBER':'FILE:DEMOTHE_RN','DATE':'FILE:DEMOTHE_DATE'}"
        name = u'latex_template_vars'

    class SbmPARAMETERS_DEMOTHE_modifyTemplate:
        doctype = u'DEMOTHE'
        value = u'DEMOTHEmodify.tpl'
        name = u'modifyTemplate'

    class SbmPARAMETERS_DEMOTHE_newrnin:
        doctype = u'DEMOTHE'
        value = u''
        name = u'newrnin'

    class SbmPARAMETERS_DEMOTHE_pathsandsuffixes:
        doctype = u'DEMOTHE'
        value = u'{"DEMOTHE_FILE":""}'
        name = u'paths_and_suffixes'

    class SbmPARAMETERS_DEMOTHE_rename:
        doctype = u'DEMOTHE'
        value = u'<PA>file:DEMOTHE_RN</PA>'
        name = u'rename'

    class SbmPARAMETERS_DEMOTHE_rnformat:
        doctype = u'DEMOTHE'
        value = u'DEMO-THESIS-<PA>yy</PA>'
        name = u'rnformat'

    class SbmPARAMETERS_DEMOTHE_rnin:
        doctype = u'DEMOTHE'
        value = u'comboDEMOTHE'
        name = u'rnin'

    class SbmPARAMETERS_DEMOTHE_sourceDoc:
        doctype = u'DEMOTHE'
        value = u'Thesis'
        name = u'sourceDoc'

    class SbmPARAMETERS_DEMOTHE_sourceTemplate:
        doctype = u'DEMOTHE'
        value = u'DEMOTHE.tpl'
        name = u'sourceTemplate'

    class SbmPARAMETERS_DEMOTHE_stamp:
        doctype = u'DEMOTHE'
        value = u'first'
        name = u'stamp'

    class SbmPARAMETERS_DEMOTHE_status:
        doctype = u'DEMOTHE'
        value = u'ADDED'
        name = u'status'

    class SbmPARAMETERS_DEMOTHE_titleFile:
        doctype = u'DEMOTHE'
        value = u'DEMOTHE_TITLE'
        name = u'titleFile'

    class SbmPARAMETERS_DEMOTHE_yeargen:
        doctype = u'DEMOTHE'
        value = u'AUTO'
        name = u'yeargen'

    class SbmPARAMETERS_DEMOVID_aspect:
        doctype = u'DEMOVID'
        value = u'DEMOVID_ASPECT'
        name = u'aspect'

    class SbmPARAMETERS_DEMOVID_authorfile:
        doctype = u'DEMOVID'
        value = u'DEMOVID_AU'
        name = u'authorfile'

    class SbmPARAMETERS_DEMOVID_autorngen:
        doctype = u'DEMOVID'
        value = u'Y'
        name = u'autorngen'

    class SbmPARAMETERS_DEMOVID_counterpath:
        doctype = u'DEMOVID'
        value = u'lastid_DEMOVID_<PA>yy</PA>'
        name = u'counterpath'

    class SbmPARAMETERS_DEMOVID_createTemplate:
        doctype = u'DEMOVID'
        value = u'DEMOVIDcreate.tpl'
        name = u'createTemplate'

    class SbmPARAMETERS_DEMOVID_edsrn:
        doctype = u'DEMOVID'
        value = u'DEMOVID_RN'
        name = u'edsrn'

    class SbmPARAMETERS_DEMOVID_emailFile:
        doctype = u'DEMOVID'
        value = u'SuE'
        name = u'emailFile'

    class SbmPARAMETERS_DEMOVID_newrnin:
        doctype = u'DEMOVID'
        value = u'NEWRN'
        name = u'newrnin'

    class SbmPARAMETERS_DEMOVID_rnformat:
        doctype = u'DEMOVID'
        value = u'DEMO-VIDEO-<PA>yy</PA>'
        name = u'rnformat'

    class SbmPARAMETERS_DEMOVID_rnin:
        doctype = u'DEMOVID'
        value = u'comboDEMOVID'
        name = u'rnin'

    class SbmPARAMETERS_DEMOVID_sourceTemplate:
        doctype = u'DEMOVID'
        value = u'DEMOVID.tpl'
        name = u'sourceTemplate'

    class SbmPARAMETERS_DEMOVID_status:
        doctype = u'DEMOVID'
        value = u'ADDED'
        name = u'status'

    class SbmPARAMETERS_DEMOVID_title:
        doctype = u'DEMOVID'
        value = u'DEMOVID_TITLE'
        name = u'title'

    class SbmPARAMETERS_DEMOVID_titleFile:
        doctype = u'DEMOVID'
        value = u'DEMOVID_TITLE'
        name = u'titleFile'

    class SbmPARAMETERS_DEMOVID_yeargen:
        doctype = u'DEMOVID'
        value = u'AUTO'
        name = u'yeargen'
