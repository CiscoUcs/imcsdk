"""This module contains the general information for BiosProfileManagement ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosProfileManagementConsts:
    ADMIN_ACTION_BACKUP = "backup"


class BiosProfileManagement(ManagedObject):
    """This is BiosProfileManagement class."""

    consts = BiosProfileManagementConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosProfileManagement", "biosProfileManagement", "profile-mgmt", VersionMeta.Version301c, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'biosUnit'], [u'biosProfile', u'uploadBiosProfile'], ["Get", "Set"]),
        "modular": MoMeta("BiosProfileManagement", "biosProfileManagement", "profile-mgmt", VersionMeta.Version301c, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'biosUnit'], [u'biosProfile', u'uploadBiosProfile'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["backup"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "reboot_on_activate_info": MoPropertyMeta("reboot_on_activate_info", "rebootOnActivateInfo", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["backup"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "reboot_on_activate_info": MoPropertyMeta("reboot_on_activate_info", "rebootOnActivateInfo", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "childAction": "child_action", 
            "description": "description", 
            "dn": "dn", 
            "rebootOnActivateInfo": "reboot_on_activate_info", 
            "rn": "rn", 
            "status": "status", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "childAction": "child_action", 
            "description": "description", 
            "dn": "dn", 
            "rebootOnActivateInfo": "reboot_on_activate_info", 
            "rn": "rn", 
            "status": "status", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_action = None
        self.child_action = None
        self.description = None
        self.reboot_on_activate_info = None
        self.status = None

        ManagedObject.__init__(self, "BiosProfileManagement", parent_mo_or_dn, **kwargs)

