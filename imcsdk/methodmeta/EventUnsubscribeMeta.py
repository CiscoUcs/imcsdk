"""This module contains the meta information of EventUnsubscribe ExternalMethod."""

from ..imccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("EventUnsubscribe", "eventUnsubscribe", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "Input", False),
}

prop_map = {
    "cookie": "cookie",
}

