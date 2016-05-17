"""This module contains the meta information of EventSubscribe ExternalMethod."""

from ..imccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("EventSubscribe", "eventSubscribe", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "InputOutput", False),
}

prop_map = {
    "cookie": "cookie",
}

