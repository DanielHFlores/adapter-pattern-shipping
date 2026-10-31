from shipping_adapter.checkout import Checkout
from shipping_adapter.legacy_carrier import LegacyCarrier
from shipping_adapter.legacy_carrier_adapter import LegacyCarrierAdapter


def test_checkout_uses_legacy_carrier_through_adapter():
    carrier = LegacyCarrier()
    adapter = LegacyCarrierAdapter(carrier)
    checkout = Checkout(adapter)

    price = checkout.shipping_quote("45000", 2.0)

    assert price == 11.51