"""This module contains the general information for CommSnmpConfigCommit ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class CommSnmpConfigCommitConsts:
    COMMIT_YES = "Yes"
    _COMMIT_YES = "yes"


class CommSnmpConfigCommit(ManagedObject):
    """This is CommSnmpConfigCommit class."""

    consts = CommSnmpConfigCommitConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("CommSnmpConfigCommit", "commSnmpConfigCommit", "snmp-config-commit", VersionMeta.Version401a, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['commSnmp'], [], [None]),
        "modular": MoMeta("CommSnmpConfigCommit", "commSnmpConfigCommit", "snmp-config-commit", VersionMeta.Version404b, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['commSnmp'], [], [None])
    }


    prop_meta = {

        "classic": {
            "commit": MoPropertyMeta("commit", "commit", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["Yes", "yes"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version401a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version401a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "commit": MoPropertyMeta("commit", "commit", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 510, None, ["Yes", "yes"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "commit": "commit", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

        "modular": {
            "commit": "commit", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.commit = None
        self.status = None
        self.child_action = None

        ManagedObject.__init__(self, "CommSnmpConfigCommit", parent_mo_or_dn, **kwargs)

