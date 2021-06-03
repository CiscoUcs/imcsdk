"""This module contains the general information for AaaLdapRoleGroup ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AaaLdapRoleGroupConsts:
    ADMIN_ACTION_CLEAR = "clear"
    ROLE_ = ""
    ROLE_ADMIN = "admin"
    ROLE_READ_ONLY = "read-only"
    ROLE_USER = "user"


class AaaLdapRoleGroup(ManagedObject):
    """This is AaaLdapRoleGroup class."""

    consts = AaaLdapRoleGroupConsts()
    naming_props = set(['id'])

    mo_meta = {
        "classic": MoMeta("AaaLdapRoleGroup", "aaaLdapRoleGroup", "rolegroup-[id]", VersionMeta.Version151f, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['aaaLdap'], [], ["Get", "Set"]),
        "modular": MoMeta("AaaLdapRoleGroup", "aaaLdapRoleGroup", "rolegroup-[id]", VersionMeta.Version2013e, "InputOutput", 0x1ff, [], ["admin", "read-only", "user"], ['aaaLdap'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version202c, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "domain": MoPropertyMeta("domain", "domain", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 1, 254, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version151f, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["1-28"]),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, 0, 127, r"""([^+\-][a-zA-Z0-9=!#$%()*+,-.:;@ _{|}~?&]*){0,127}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "role": MoPropertyMeta("role", "role", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "admin", "read-only", "user"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "admin_action": MoPropertyMeta("admin_action", "adminAction", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["clear"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "domain": MoPropertyMeta("domain", "domain", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 1, 254, None, [], []),
            "id": MoPropertyMeta("id", "id", "uint", VersionMeta.Version2013e, MoPropertyMeta.NAMING, 0x10, None, None, None, [], ["1-28"]),
            "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, 0, 127, r"""([^+\-][a-zA-Z0-9=!#$%()*+,-.:;@ _{|}~?&]*){0,127}""", [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, 0, 255, None, [], []),
            "role": MoPropertyMeta("role", "role", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["", "admin", "read-only", "user"], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "domain": "domain", 
            "id": "id", 
            "name": "name", 
            "rn": "rn", 
            "role": "role", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "adminAction": "admin_action", 
            "dn": "dn", 
            "domain": "domain", 
            "id": "id", 
            "name": "name", 
            "rn": "rn", 
            "role": "role", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.admin_action = None
        self.domain = None
        self.name = None
        self.role = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "AaaLdapRoleGroup", parent_mo_or_dn, **kwargs)

