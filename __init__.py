# This file is part of sale_invisible_stock module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .product import *
from .sale import *


def register():
    Pool.register(
        Template,
        Sale,
        module='sale_invisible_stock', type_='model')
