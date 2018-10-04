# This file is part of sale_invisible_stock module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import product
from . import sale


def register():
    Pool.register(
        product.Template,
        sale.Sale,
        module='sale_invisible_stock', type_='model')
