"""This module contains the meta information of AaaKeepAlive ExternalMethod."""

from ..imccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("AaaKeepAlive", "aaaKeepAlive", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "InputOutput", False),
}

prop_map = {
    "cookie": "cookie",
}

