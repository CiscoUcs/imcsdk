"""This module contains the general information for AaaUserPolicy ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AaaUserPolicyConsts:
    pass


class AaaUserPolicy(ManagedObject):
    """This is AaaUserPolicy class."""

    consts = AaaUserPolicyConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AaaUserPolicy", "aaaUserPolicy", "policy", VersionMeta.Version209c, "InputOutput", 0x1f, [], ["admin", "user"], [u'aaaUserEp'], [], ["Get", "Set"]),
        "modular": MoMeta("AaaUserPolicy", "aaaUserPolicy", "policy", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "user"], [u'aaaUserEp'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version209c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "password_policy_rules": MoPropertyMeta("password_policy_rules", "passwordPolicyRules", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 0, 2500, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "user_password_policy": MoPropertyMeta("user_password_policy", "userPasswordPolicy", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "password_policy_rules": MoPropertyMeta("password_policy_rules", "passwordPolicyRules", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 2500, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "user_password_policy": MoPropertyMeta("user_password_policy", "userPasswordPolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "passwordPolicyRules": "password_policy_rules", 
            "rn": "rn", 
            "status": "status", 
            "userPasswordPolicy": "user_password_policy", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "passwordPolicyRules": "password_policy_rules", 
            "rn": "rn", 
            "status": "status", 
            "userPasswordPolicy": "user_password_policy", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.password_policy_rules = None
        self.status = None
        self.user_password_policy = None

        ManagedObject.__init__(self, "AaaUserPolicy", parent_mo_or_dn, **kwargs)

