import pytest
from src import dataclasses
from src import parse_request

Url = dataclasses.Url


@pytest.fixture
def swatch_data():
    return {
        "primaryImage": "https://images.lululemon.com/is/image/lululemon/LM1219S_053870_1",
        "hoverImage": "https://images.lululemon.com/is/image/lululemon/LM1219S_053870_2",
        "url": "/p/mens-tanks/Metal-Vent-Breathe-Tank-MD/_/prod9370474?color=53870",
        "colorId": "53870",
        "inStore": False,
        "__typename": "ColorSwatch_CDP"
    }


@pytest.fixture
def prod_variant_data():
    return {
        "colorGroup": "orangePrinted",
        "colorId": "53884",
        "colorName": "Covered Camo Vintage Plum/Auric Gold",
        "inStore": False,
        "size": "XXL",
        "sku": "us_142325756",
        "skuStyleOrderId": "3",
        "styleId01": "LM1219S",
        "styleId02": "053884",
        "styleId": "LM1219S-053884",
        "__typename": "SkuStyle_CDP"
    }


def test_make_swatch(swatch_data):
    swatch = parse_request.make_swatch(swatch_data)
    assert swatch == dataclasses.Swatch(
        primary_img=Url(
            'https://images.lululemon.com/is/image/lululemon/LM1219S_053870_1'),
        hover_img=Url(
            'https://images.lululemon.com/is/image/lululemon/LM1219S_053870_2'),
        url=Url(
            '/p/mens-tanks/Metal-Vent-Breathe-Tank-MD/_/prod9370474?color=53870'),
        color_id=53870,
        is_in_store=False,
        type_name='ColorSwatch_CDP'
    )


def test_make_product_variant(prod_variant_data):
    pv = parse_request.make_product_variant(prod_variant_data)
    color = dataclasses.Color(
        group='orangePrinted',
        id=53884,
        name='Covered Camo Vintage Plum/Auric Gold'
    )
    assert pv == dataclasses.ProductVariant(
        color=color,
        is_in_store=False,
        size=dataclasses.Sizes.XXL,
        sku="us_142325756",
        sku_style_order_id=3,
        style_id_01='LM1219S',
        style_id_02='053884',
        style_id='LM1219S-053884',
        type_name='SkuStyle_CDP'
    )
