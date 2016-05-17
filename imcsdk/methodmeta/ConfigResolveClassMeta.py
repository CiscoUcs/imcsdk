"""This module contains the meta information of ConfigResolveClass ExternalMethod."""

from ..imccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigResolveClass", "configResolveClass", "Version142b")

prop_meta = {
    "class_id": MethodPropertyMeta("ClassId", "classId", "NamingClassId", "Version142b", "InputOutput", False),
    "cookie": MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "InputOutput", False),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "Input", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "classId": "class_id",
    "cookie": "cookie",
    "inHierarchical": "in_hierarchical",
    "outConfigs": "out_configs",
}

