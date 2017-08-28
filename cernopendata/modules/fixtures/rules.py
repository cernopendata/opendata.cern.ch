"""CERN Open Data custom fields of MARC 21 model."""

from dojson import utils
from dojson.contrib.marc21.model import marc21


@marc21.over('269', '^269__')
@utils.filter_values
def field_269(self, key, value):
    """269 field."""
    field_map = {
        'a': 'a',
        'b': 'b',
        'c': 'c',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('a'),
        'b': value.get('b'),
        'c': value.get('c'),
    }


@marc21.over('593', '^593__')
@utils.filter_values
def field_593(self, key, value):
    """593 field."""
    field_map = {
        'a': 'a',
        'b': 'b',
    }

    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'a': value.get('a'),
        'b': value.get('b'),
    }


@marc21.over('693', '^693[_1]_')
@utils.filter_values
def accelerator_experiment(self, key, value):
    """Accelerator experiment."""
    return {
        'accelerator': value.get('a'),
        'experiment': value.get('e'),
    }


@marc21.over('beam_energy', '^942__')
def collision_energy(self, key, value):
    """Collision energy."""
    return value.get('a')


@marc21.over('reprocessing_date', '^960__')
def reprocessing_date(self, key, value):
    """Reprocessing date."""
    return value.get('c')


@marc21.over('accelerator_run', '^964_[_0]')
def accelerator_run(self, key, value):
    """Accelerator run."""
    return value.get('c')


@marc21.over('files', '^FFT__')
@utils.for_each_value
@utils.filter_values
def fft_files(self, key, value):
    """593 field."""
    field_map = {
        'z': 'comment',
        'y': 'description',
        'q': 'eformat',
        'f': 'name',
        's': 'size',
        'u': 'url',
    }
    order = utils.map_order(field_map, value)

    return {
        '__order__': tuple(order) if len(order) else None,
        'comment': value.get('z'),
        'description': value.get('y'),
        'eformat': value.get('q'),
        'name': value.get('f'),
        'size': value.get('s'),
        'url': value.get('u'),
    }
