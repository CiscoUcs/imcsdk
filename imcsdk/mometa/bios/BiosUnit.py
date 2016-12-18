"""This module contains the general information for BiosUnit ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosUnitConsts:
    ADMIN_ACTION_ENTER_BIOS_SETUP = "enter-bios-setup"


class BiosUnit(ManagedObject):
    """This is BiosUnit class."""

    consts = BiosUnitConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosUnit", "biosUnit", "bios", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'computeRackUnit'], [u'biosBOT', u'biosPlatformDefaults', u'biosProfileManagement', u'biosSettings', u'firmwareBootDefinition', u'firmwareRunning', u'firmwareUpdatable'], ["Get", "Set"]),
        "modular": MoMeta("BiosUnit", "biosUnit", "bios", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'computeServerNode'], [u'biosBOT', u'biosPlatformDefaults', u'biosProfileManagement', u'biosSettings', u'firmwareBootDefinition', u'firmwareRunning', u'firmwareUpdatable'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["enter-bios-setup"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version151f, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["enter-bios-setup"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "model": MoPropertyMeta("model", "model", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vendor": MoPropertyMeta("vendor", "vendor", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "childAction": "child_action", 
            "dn": "dn", 
            "model": "model", 
            "rn": "rn", 
            "status": "status", 
            "vendor": "vendor", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "childAction": "child_action", 
            "dn": "dn", 
            "model": "model", 
            "rn": "rn", 
            "status": "status", 
            "vendor": "vendor", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.child_action = None
        self.model = None
        self.status = None
        self.vendor = None

        ManagedObject.__init__(self, "BiosUnit", parent_mo_or_dn, **kwargs)

