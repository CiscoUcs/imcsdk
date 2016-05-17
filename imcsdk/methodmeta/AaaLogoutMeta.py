"""This module contains the meta information of AaaLogout ExternalMethod."""

from ..imccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("AaaLogout", "aaaLogout", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "InputOutput", False),
    "in_cookie": MethodPropertyMeta("InCookie", "inCookie", "StringMin0Max47", "Version142b", "Input", False),
    "out_status": MethodPropertyMeta("OutStatus", "outStatus", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "inCookie": "in_cookie",
    "outStatus": "out_status",
}

