"""This module contains the meta information of AaaGetComputeAuthTokens ExternalMethod."""

from ..imccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("AaaGetComputeAuthTokens", "aaaGetComputeAuthTokens", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "InputOutput", False),
    "out_tokens": MethodPropertyMeta("OutTokens", "outTokens", "Xs:string", "Version142b", "Output", False),
}

prop_map = {
    "cookie": "cookie",
    "outTokens": "out_tokens",
}

