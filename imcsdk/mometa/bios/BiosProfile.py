"""This module contains the general information for BiosProfile ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosProfileConsts:
    ADMIN_ACTION_ACTIVATE = "activate"
    ADMIN_ACTION_DELETE = "delete"
    BACKUP_ON_ACTIVATE_FALSE = "false"
    BACKUP_ON_ACTIVATE_NO = "no"
    BACKUP_ON_ACTIVATE_TRUE = "true"
    BACKUP_ON_ACTIVATE_YES = "yes"
    REBOOT_ON_ACTIVATE_FALSE = "false"
    REBOOT_ON_ACTIVATE_NO = "no"
    REBOOT_ON_ACTIVATE_TRUE = "true"
    REBOOT_ON_ACTIVATE_YES = "yes"


class BiosProfile(ManagedObject):
    """This is BiosProfile class."""

    consts = BiosProfileConsts()
    naming_props = set(['name'])

    mo_meta = {
        "classic": MoMeta("BiosProfile", "biosProfile", "bios-profile-[name]", VersionMeta.Version301c, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['biosProfileManagement'], ['biosProfileToken'], ["Get", "Set"]),
        "modular": MoMeta("BiosProfile", "biosProfile", "bios-profile-[name]", VersionMeta.Version301c, "InputOutput", 0xff, [], ["admin", "read-only", "user"], ['biosProfileManagement'], ['biosProfileToken'], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["activate", "delete"], []),
            "backup_on_activate": MoPropertyMeta("backup_on_activate", "backupOnActivate", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "enabled": MoPropertyMeta("enabled", "enabled", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "reboot_on_activate": MoPropertyMeta("reboot_on_activate", "rebootOnActivate", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["No", "Yes", "false", "no", "true", "yes"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version301c, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["activate", "delete"], []),
            "backup_on_activate": MoPropertyMeta("backup_on_activate", "backupOnActivate", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["No", "Yes", "no", "yes"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "enabled": MoPropertyMeta("enabled", "enabled", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["No", "Yes", "no", "yes"], []),
            "reboot_on_activate": MoPropertyMeta("reboot_on_activate", "rebootOnActivate", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["No", "Yes", "no", "yes"], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version301c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version301c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "description": MoPropertyMeta("description", "description", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "id": MoPropertyMeta("id", "id", "string", VersionMeta.Version301c, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version301c, MoPropertyMeta.NAMING, None, 0, 510, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "backupOnActivate": "backup_on_activate", 
            "dn": "dn", 
            "enabled": "enabled", 
            "rebootOnActivate": "reboot_on_activate", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "description": "description", 
            "id": "id", 
            "name": "name", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "backupOnActivate": "backup_on_activate", 
            "dn": "dn", 
            "enabled": "enabled", 
            "rebootOnActivate": "reboot_on_activate", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
            "description": "description", 
            "id": "id", 
            "name": "name", 
        },

    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.admin_action = None
        self.backup_on_activate = None
        self.enabled = None
        self.reboot_on_activate = None
        self.status = None
        self.child_action = None
        self.description = None
        self.id = None

        ManagedObject.__init__(self, "BiosProfile", parent_mo_or_dn, **kwargs)

