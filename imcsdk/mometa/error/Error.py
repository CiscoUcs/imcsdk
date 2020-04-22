"""This module contains the general information for Error ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class ErrorConsts:
    pass


class Error(ManagedObject):
    """This is Error class."""

    consts = ErrorConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("Error", "error", "", VersionMeta.Version151f, "OutputOnly", 0x1, [], [""], [], [], [None]),
        "modular": MoMeta("Error", "error", "", VersionMeta.Version2013e, "OutputOnly", 0x1, [], [""], [], [], [None])
    }


    prop_meta = {

        "classic": {
            "cookie": MoPropertyMeta("cookie", "cookie", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "error_code": MoPropertyMeta("error_code", "errorCode", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "error_descr": MoPropertyMeta("error_descr", "errorDescr", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "invocation_result": MoPropertyMeta("invocation_result", "invocationResult", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "response": MoPropertyMeta("response", "response", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
        },

        "modular": {
            "cookie": MoPropertyMeta("cookie", "cookie", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "error_code": MoPropertyMeta("error_code", "errorCode", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "error_descr": MoPropertyMeta("error_descr", "errorDescr", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "invocation_result": MoPropertyMeta("invocation_result", "invocationResult", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []),
            "response": MoPropertyMeta("response", "response", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["No", "Yes", "no", "yes"], []),
        },

    }

    prop_map = {

        "classic": {
            "cookie": "cookie", 
            "errorCode": "error_code", 
            "errorDescr": "error_descr", 
            "invocationResult": "invocation_result", 
            "response": "response", 
        },

        "modular": {
            "cookie": "cookie", 
            "errorCode": "error_code", 
            "errorDescr": "error_descr", 
            "invocationResult": "invocation_result", 
            "response": "response", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.cookie = None
        self.error_code = None
        self.error_descr = None
        self.invocation_result = None
        self.response = None

        ManagedObject.__init__(self, "Error", parent_mo_or_dn, **kwargs)

