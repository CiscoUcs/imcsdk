"""This module contains the general information for LsbootDef ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class LsbootDefConsts:
    PURPOSE_OPERATIONAL = "operational"
    PURPOSE_UTILITY = "utility"
    REBOOT_ON_UPDATE_FALSE = "false"
    REBOOT_ON_UPDATE_NO = "no"
    REBOOT_ON_UPDATE_TRUE = "true"
    REBOOT_ON_UPDATE_YES = "yes"


class LsbootDef(ManagedObject):
    """This is LsbootDef class."""

    consts = LsbootDefConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("LsbootDef", "lsbootDef", "boot-policy", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['computeRackUnit'], ['lsbootBootSecurity', 'lsbootEfi', 'lsbootLan', 'lsbootStorage', 'lsbootVirtualMedia'], ["Get", "Set"]),
        "modular": MoMeta("LsbootDef", "lsbootDef", "boot-policy", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['computeServerNode'], ['lsbootBootSecurity', 'lsbootEfi', 'lsbootLan', 'lsbootStorage', 'lsbootVirtualMedia'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "reboot_on_update": MoPropertyMeta("reboot_on_update", "rebootOnUpdate", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
            "purpose": MoPropertyMeta("purpose", "purpose", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, None, None, None, ["operational", "utility"], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "reboot_on_update": MoPropertyMeta("reboot_on_update", "rebootOnUpdate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["No", "Yes", "no", "yes"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, r"""[\-\.:_a-zA-Z0-9]{0,16}""", [], []),
            "purpose": MoPropertyMeta("purpose", "purpose", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["operational", "utility"], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rebootOnUpdate": "reboot_on_update", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "name": "name", 
            "purpose": "purpose", 
        },

        "modular": {
            "dn": "dn", 
            "rebootOnUpdate": "reboot_on_update", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "name": "name", 
            "purpose": "purpose", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.reboot_on_update = None
        self.status = None
        self.child_action = None
        self.name = None
        self.purpose = None

        ManagedObject.__init__(self, "LsbootDef", parent_mo_or_dn, **kwargs)

