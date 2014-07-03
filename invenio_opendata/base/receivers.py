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

from datetime import datetime, timedelta
from fixture import DataSet

from invenio.base.factory import with_app_context


@with_app_context(new_context=True)
def post_handler_demosite_populate(sender, default_data='', *args, **kwargs):
    """Loads data after records are created."""

    if default_data != 'demosite':
        print '>>> You can define your own post hadler for `demosite populate`'
    print '>>> Loading demosite data for BibCirculation ...'

    class CrcLIBRARYData(DataSet):

        class CrcLIBRARY_1:
            phone = u'1234567'
            name = u'Atlantis Main Library'
            address = u'CH-1211 Geneva 23'
            notes = u''
            type = None
            id = 1L
            email = u'atlantis@cds.cern.ch'

        class CrcLIBRARY_2:
            phone = u'1234567'
            name = u'Atlantis HEP Library'
            address = u'CH-1211 Geneva 21'
            notes = u''
            type = None
            id = 2L
            email = u'atlantis.hep@cds.cern.ch'


    class CrcITEMData(DataSet):

        class CrcITEM_bc21001:
            id_crcLIBRARY = CrcLIBRARYData.CrcLIBRARY_2.ref('id')
            status = u'available'
            id_bibrec = 21
            description = u'Book'
            modification_date = datetime(2008, 7, 21, 0, 0)
            barcode = u'bc-21001'
            collection = u''
            creation_date = datetime(2008, 7, 21, 0, 0)
            loan_period = u'4 weeks'
            location = u'MLL-DS.63'
            number_of_requests = 0L
            expected_arrival_date = u''

        class CrcITEM_bc22001:
            id_crcLIBRARY = CrcLIBRARYData.CrcLIBRARY_1.ref('id')
            status = u'requested'
            id_bibrec = 22
            description = u'Book'
            modification_date = datetime(2008, 7, 21, 0, 0)
            barcode = u'bc-22001'
            collection = u''
            creation_date = datetime(2008, 7, 21, 0, 0)
            loan_period = u'1 week'
            location = u'AZD4E-865'
            number_of_requests = 0L
            expected_arrival_date = u''

        class CrcITEM_bc23001:
            id_crcLIBRARY = CrcLIBRARYData.CrcLIBRARY_1.ref('id')
            status = u'requested'
            id_bibrec = 23
            description = u'Book'
            modification_date = datetime(2008, 7, 21, 0, 0)
            barcode = u'bc-23001'
            collection = u''
            creation_date = datetime(2008, 7, 21, 0, 0)
            loan_period = u'4 weeks'
            location = u'JHL-465.DS'
            number_of_requests = 0L
            expected_arrival_date = u''

        class CrcITEM_bc24001:
            id_crcLIBRARY = CrcLIBRARYData.CrcLIBRARY_2.ref('id')
            status = u'available'
            id_bibrec = 24
            description = u'Book'
            modification_date = datetime(2008, 7, 21, 0, 0)
            barcode = u'bc-24001'
            collection = u''
            creation_date = datetime(2008, 7, 21, 0, 0)
            loan_period = u'4 weeks'
            location = u'J56-475'
            number_of_requests = 0L
            expected_arrival_date = u''

        class CrcITEM_bc25001:
            id_crcLIBRARY = CrcLIBRARYData.CrcLIBRARY_2.ref('id')
            status = u'on loan'
            id_bibrec = 25
            description = u'Book'
            modification_date = datetime(2008, 7, 21, 0, 0)
            barcode = u'bc-25001'
            collection = u''
            creation_date = datetime(2008, 7, 21, 0, 0)
            loan_period = u'4 weeks'
            location = u'AGT-MLL5'
            number_of_requests = 0L
            expected_arrival_date = u''

        class CrcITEM_bc26001:
            id_crcLIBRARY = CrcLIBRARYData.CrcLIBRARY_1.ref('id')
            status = u'missing'
            id_bibrec = 26
            description = u'Book'
            modification_date = datetime(2008, 7, 21, 0, 0)
            barcode = u'bc-26001'
            collection = u''
            creation_date = datetime(2008, 7, 21, 0, 0)
            loan_period = u'1 week'
            location = u'AZD456-465'
            number_of_requests = 0L
            expected_arrival_date = u''

        class CrcITEM_bc27001:
            id_crcLIBRARY = CrcLIBRARYData.CrcLIBRARY_2.ref('id')
            status = u'available'
            id_bibrec = 27
            description = u'Book'
            modification_date = datetime(2008, 7, 21, 0, 0)
            barcode = u'bc-27001'
            collection = u''
            creation_date = datetime(2008, 7, 21, 0, 0)
            loan_period = u'4 weeks'
            location = u'JLMQ-45-SQ'
            number_of_requests = 0L
            expected_arrival_date = u''

        class CrcITEM_bc28001:
            id_crcLIBRARY = CrcLIBRARYData.CrcLIBRARY_1.ref('id')
            status = u'available'
            id_bibrec = 28
            description = u'Book'
            modification_date = datetime(2008, 7, 21, 0, 0)
            barcode = u'bc-28001'
            collection = u''
            creation_date = datetime(2008, 7, 21, 0, 0)
            loan_period = u'4 weeks'
            location = u'AZD5-456'
            number_of_requests = 0L
            expected_arrival_date = u''

        class CrcITEM_bc29001:
            id_crcLIBRARY = CrcLIBRARYData.CrcLIBRARY_1.ref('id')
            status = u'requested'
            id_bibrec = 29
            description = u'Book'
            modification_date = datetime(2008, 7, 21, 0, 0)
            barcode = u'bc-29001'
            collection = u''
            creation_date = datetime(2008, 7, 21, 0, 0)
            loan_period = u'4 weeks'
            location = u'AZD456-465'
            number_of_requests = 0L
            expected_arrival_date = u''

        class CrcITEM_bc30001:
            id_crcLIBRARY = CrcLIBRARYData.CrcLIBRARY_1.ref('id')
            status = u'available'
            id_bibrec = 30
            description = u'Book'
            modification_date = datetime(2008, 7, 21, 0, 0)
            barcode = u'bc-30001'
            collection = u'Reference'
            creation_date = datetime(2008, 7, 21, 0, 0)
            loan_period = u'Not for loan'
            location = u'QSQS-52-S'
            number_of_requests = 0L
            expected_arrival_date = u''

        class CrcITEM_bc31001:
            id_crcLIBRARY = CrcLIBRARYData.CrcLIBRARY_2.ref('id')
            status = u'on loan'
            id_bibrec = 31
            description = u'Book'
            modification_date = datetime(2008, 7, 21, 0, 0)
            barcode = u'bc-31001'
            collection = u''
            creation_date = datetime(2008, 7, 21, 0, 0)
            loan_period = u'1 week'
            location = u'123LSKD'
            number_of_requests = 0L
            expected_arrival_date = u''

        class CrcITEM_bc31002:
            id_crcLIBRARY = CrcLIBRARYData.CrcLIBRARY_1.ref('id')
            status = u'available'
            id_bibrec = 31
            description = u'Book'
            modification_date = datetime(2008, 7, 21, 0, 0)
            barcode = u'bc-31002'
            collection = u''
            creation_date = datetime(2008, 7, 21, 0, 0)
            loan_period = u'1 week'
            location = u'QSQ452-S'
            number_of_requests = 0L
            expected_arrival_date = u''

        class CrcITEM_bc32001:
            id_crcLIBRARY = CrcLIBRARYData.CrcLIBRARY_1.ref('id')
            status = u'available'
            id_bibrec = 32
            description = u'Book'
            modification_date = datetime(2008, 7, 21, 0, 0)
            barcode = u'bc-32001'
            collection = u'Reference'
            creation_date = datetime(2008, 7, 21, 0, 0)
            loan_period = u'Not for loan'
            location = u'WDFG-54'
            number_of_requests = 0L
            expected_arrival_date = u''

        class CrcITEM_bc32002:
            id_crcLIBRARY = CrcLIBRARYData.CrcLIBRARY_2.ref('id')
            status = u'available'
            id_bibrec = 32
            description = u'Book'
            modification_date = datetime(2008, 7, 21, 0, 0)
            barcode = u'bc-32002'
            collection = u''
            creation_date = datetime(2008, 7, 21, 0, 0)
            loan_period = u'4 weeks'
            location = u'RZ.612-MK'
            number_of_requests = 0L
            expected_arrival_date = u''

        class CrcITEM_bc32003:
            id_crcLIBRARY = CrcLIBRARYData.CrcLIBRARY_1.ref('id')
            status = u'missing'
            id_bibrec = 32
            description = u'Book'
            modification_date = datetime(2008, 7, 21, 0, 0)
            barcode = u'bc-32003'
            collection = u''
            creation_date = datetime(2008, 7, 21, 0, 0)
            loan_period = u'4 weeks'
            location = u'RT-4654-E'
            number_of_requests = 0L
            expected_arrival_date = u''

        class CrcITEM_bc33001:
            id_crcLIBRARY = CrcLIBRARYData.CrcLIBRARY_1.ref('id')
            status = u'on loan'
            id_bibrec = 33
            description = u'Book'
            modification_date = datetime(2008, 7, 21, 0, 0)
            barcode = u'bc-33001'
            collection = u''
            creation_date = datetime(2008, 7, 21, 0, 0)
            loan_period = u'4 weeks'
            location = u'AZ.12-AK'
            number_of_requests = 0L
            expected_arrival_date = u''

        class CrcITEM_bc34001:
            id_crcLIBRARY = CrcLIBRARYData.CrcLIBRARY_1.ref('id')
            status = u'available'
            id_bibrec = 34
            description = u'Book'
            modification_date = datetime(2008, 7, 21, 0, 0)
            barcode = u'bc-34001'
            collection = u''
            creation_date = datetime(2008, 7, 21, 0, 0)
            loan_period = u'4 weeks'
            location = u'ABC-123'
            number_of_requests = 0L
            expected_arrival_date = u''

        class CrcITEM_bc34002:
            id_crcLIBRARY = CrcLIBRARYData.CrcLIBRARY_2.ref('id')
            status = u'requested'
            id_bibrec = 34
            description = u'Book'
            modification_date = datetime(2008, 7, 21, 0, 0)
            barcode = u'bc-34002'
            collection = u''
            creation_date = datetime(2008, 7, 21, 0, 0)
            loan_period = u'4 weeks'
            location = u'HEP-12A'
            number_of_requests = 0L
            expected_arrival_date = u''


    class CrcBORROWERData(DataSet):

        class CrcBORROWER_1:
            name = u'Admin'
            notes = u''
            borrower_until = datetime(1900, 1, 1, 0, 0)
            phone = u'20003'
            borrower_since = datetime(2008, 7, 21, 0, 0)
            email = u'admin@cds.cern.ch'
            address = u'99-Z-019'
            mailbox = None
            id = 1L
            ccid = None

        class CrcBORROWER_2:
            name = u'Jekyll'
            notes = u''
            borrower_until = datetime(1900, 1, 1, 0, 0)
            phone = u'01234'
            borrower_since = datetime(2008, 7, 21, 0, 0)
            email = u'jekyll@cds.cern.ch'
            address = u'21-Z-019'
            mailbox = None
            id = 2L
            ccid = None

        class CrcBORROWER_3:
            name = u'Hyde'
            notes = u''
            borrower_until = datetime(1900, 1, 1, 0, 0)
            phone = u'01574'
            borrower_since = datetime(2008, 7, 21, 0, 0)
            email = u'Hyde@cds.cern.ch'
            address = u'22-Z-119'
            mailbox = None
            id = 3L
            ccid = None

        class CrcBORROWER_4:
            name = u'Dorian Gray'
            notes = u''
            borrower_until = datetime(1900, 1, 1, 0, 0)
            phone = u'33234'
            borrower_since = datetime(2008, 7, 21, 0, 0)
            email = u'dorian.gray@cds.cern.ch'
            address = u'38-Y-819'
            mailbox = None
            id = 4L
            ccid = None

        class CrcBORROWER_5:
            name = u'Romeo Montague'
            notes = u''
            borrower_until = datetime(1900, 1, 1, 0, 0)
            phone = u'93844'
            borrower_since = datetime(2008, 7, 21, 0, 0)
            email = u'romeo.montague@cds.cern.ch'
            address = u'98-W-859'
            mailbox = None
            id = 5L
            ccid = None

        class CrcBORROWER_6:
            name = u'Juliet Capulet'
            notes = u''
            borrower_until = datetime(1900, 1, 1, 0, 0)
            phone = u'99874'
            borrower_since = datetime(2008, 7, 21, 0, 0)
            email = u'juliet.capulet@cds.cern.ch'
            address = u'91-X-098'
            mailbox = None
            id = 6L
            ccid = None

        class CrcBORROWER_7:
            name = u'Benvolio Montague'
            notes = u''
            borrower_until = datetime(1900, 1, 1, 0, 0)
            phone = u'32354'
            borrower_since = datetime(2008, 7, 21, 0, 0)
            email = u'benvolio.montague@cds.cern.ch'
            address = u'93-P-019'
            mailbox = None
            id = 7L
            ccid = None

        class CrcBORROWER_8:
            name = u'Balthasar Montague'
            notes = u''
            borrower_until = datetime(1900, 1, 1, 0, 0)
            phone = u'78644'
            borrower_since = datetime(2008, 7, 21, 0, 0)
            email = u'balthasar.montague@cds.cern.ch'
            address = u'20-M-349'
            mailbox = None
            id = 8L
            ccid = None


    class CrcLOANData(DataSet):

        class CrcLOAN_1:
            status = u'on loan'
            due_date = datetime.now() + timedelta(days=30)
            id_bibrec = 33
            overdue_letter_date = datetime(1900, 1, 1, 0, 0)
            notes = u''
            barcode = CrcITEMData.CrcITEM_bc33001.ref('barcode')
            id_crcBORROWER = CrcBORROWERData.CrcBORROWER_4.ref('id')
            number_of_renewals = 0L
            loaned_on = datetime.now()
            returned_on = None
            overdue_letter_number = 0L
            type = u'normal'
            id = 1L

        class CrcLOAN_2:
            status = u'on loan'
            due_date = datetime.now() + timedelta(days=7)
            id_bibrec = 31
            overdue_letter_date = datetime(1900, 1, 1, 0, 0)
            notes = u''
            barcode = CrcITEMData.CrcITEM_bc31001.ref('barcode')
            id_crcBORROWER = CrcBORROWERData.CrcBORROWER_5.ref('id')
            number_of_renewals = 0L
            loaned_on = datetime.now()
            returned_on = None
            overdue_letter_number = 0L
            type = u'normal'
            id = 2L

        class CrcLOAN_3:
            status = u'on loan'
            due_date = datetime.now() + timedelta(days=30)
            id_bibrec = 31
            overdue_letter_date = datetime(1900, 1, 1, 0, 0)
            notes = u''
            barcode = CrcITEMData.CrcITEM_bc25001.ref('barcode')
            id_crcBORROWER = CrcBORROWERData.CrcBORROWER_5.ref('id')
            number_of_renewals = 0L
            loaned_on = datetime.now()
            returned_on = None
            overdue_letter_number = 0L
            type = u'normal'
            id = 3L


    class CrcLOANREQUESTData(DataSet):

        class CrcLOANREQUEST_1:
            status = u'pending'
            period_of_interest_from = datetime.now()
            id_bibrec = 34
            request_date = datetime.now()
            notes = u''
            barcode = CrcITEMData.CrcITEM_bc34002.ref('barcode')
            id_crcBORROWER = CrcBORROWERData.CrcBORROWER_5.ref('id')
            period_of_interest_to = datetime.now() + timedelta(days=60)
            id = 1L

        class CrcLOANREQUEST_2:
            status = u'pending'
            period_of_interest_from = datetime.now()
            id_bibrec = 29
            request_date = datetime.now()
            notes = u''
            barcode = CrcITEMData.CrcITEM_bc29001.ref('barcode')
            id_crcBORROWER = CrcBORROWERData.CrcBORROWER_6.ref('id')
            period_of_interest_to = datetime.now() + timedelta(days=45)
            id = 2L

        class CrcLOANREQUEST_3:
            status = u'waiting'
            period_of_interest_from = datetime.now()
            id_bibrec = 33
            request_date = datetime.now()
            notes = u''
            barcode = CrcITEMData.CrcITEM_bc33001.ref('barcode')
            id_crcBORROWER = CrcBORROWERData.CrcBORROWER_5.ref('id')
            period_of_interest_to = datetime.now() + timedelta(days=45)
            id = 3L

        class CrcLOANREQUEST_4:
            status = u'pending'
            period_of_interest_from = datetime.now()
            id_bibrec = 22
            request_date = datetime.now()
            notes = u''
            barcode = CrcITEMData.CrcITEM_bc22001.ref('barcode')
            id_crcBORROWER = CrcBORROWERData.CrcBORROWER_7.ref('id')
            period_of_interest_to = datetime.now() + timedelta(days=90)
            id = 4L


    fixtures = [CrcLIBRARYData, CrcBORROWERData, CrcITEMData, CrcLOANData,
                CrcLOANREQUESTData]

    try:
        from invenio.ext.sqlalchemy import db
        from fixture import SQLAlchemyFixture
        from invenio.modules.circulation import models as bibcirculation_model

        models = dict((m.__name__, getattr(bibcirculation_model, m.__name__[:-4]))
                      for m in fixtures)

        dbfixture = SQLAlchemyFixture(env=models, engine=db.metadata.bind,
                                      session=db.session)
        data = dbfixture.data(*fixtures)

        print ">>> There are", len(models), "tables to be loaded."
        data.setup()

        print ">>> BibCirculation demosite data has been loaded."
    except Exception as e:
        print ">>> FAIL: data has not been loaded", e

