# -*- coding: utf-8 -*-

"""cernopendata base Invenio configuration."""

from flask_celeryext import create_celery_app

from .factory import create_app

celery = create_celery_app(create_app())
