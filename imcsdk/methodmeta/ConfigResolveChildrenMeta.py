"""This module contains the meta information of ConfigResolveChildren ExternalMethod."""

from ..imccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigResolveChildren", "configResolveChildren", "Version142b")

prop_meta = {
    "class_id": MethodPropertyMeta("ClassId", "classId", "NamingClassId", "Version142b", "Input", False),
    "cookie": MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "Output", False),
    "in_dn": MethodPropertyMeta("InDn", "inDn", "ReferenceObject", "Version142b", "Input", False),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "classId": "class_id",
    "cookie": "cookie",
    "dn": "dn",
    "inDn": "in_dn",
    "inHierarchical": "in_hierarchical",
    "outConfigs": "out_configs",
}

