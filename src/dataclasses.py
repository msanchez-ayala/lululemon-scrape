"""
Classes to store data from QraphQL query responses
"""

from enum import Enum
from dataclasses import dataclass


class Sizes(Enum):
    XXS = 'XXS'
    XS = 'XS'
    S = 'S'
    M = 'M'
    L = 'L'
    XL = 'XL'
    XXL = 'XXL'


class CurrencyCodes(Enum):
    USD = 'USD'


class Url(str):
    pass


@dataclass
class PriceRange:
    min: float = None
    max: float = None

    def __post_init__(self):
        if self.min is None and self.max is None:
            raise ValueError('At least one value must be specified')
        elif self.min is None and self.max is not None:
            self.min = self.max
        elif self.max is None and self.min is not None:
            self.max = self.min


@dataclass
class Color:
    group: str
    id: int
    name: str

@dataclass
class ProductVariant:
    color: Color
    is_in_store: bool
    size: Sizes
    sku: str
    sku_style_order_id: int
    style_id_01: str
    style_id_02: str
    style_id: str
    type_name: str


@dataclass
class Swatch:
    primary_img: Url
    hover_img: Url
    url: Url
    color_id: int
    is_in_store: bool
    type_name: str


@dataclass
class Product:
    allAvailableSizes: list[Sizes]
    currencyCode: CurrencyCodes
    defaultSku: str
    displayName: str
    listPrice: PriceRange
    parentCategoryUnifiedId: str
    productOnSale: bool
    productSalePrice: PriceRange
    pdpUrl: Url
    productCoverage: str
    repositoryId: str
    productId: str
    inStore: bool
    unifiedId: str
    skuStyleOrder: list[ProductVariant]
    swatches: list[Swatch]
    type_name: str