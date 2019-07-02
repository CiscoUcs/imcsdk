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
        "modular": MoMeta("AaaUserPolicy", "aaaUserPolicy", "policy", VersionMeta.Version2013e, "InputOutput", 0xff, [], ["admin", "user"], [u'aaaUserEp'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "user_password_policy": MoPropertyMeta("user_password_policy", "userPasswordPolicy", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version209c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "password_policy_rules": MoPropertyMeta("password_policy_rules", "passwordPolicyRules", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 0, 2500, None, [], []), 
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "user_password_policy": MoPropertyMeta("user_password_policy", "userPasswordPolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
            "allowed_attempts": MoPropertyMeta("allowed_attempts", "allowedAttempts", "uint", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, [], ["0-20"]), 
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "lockout_period": MoPropertyMeta("lockout_period", "lockoutPeriod", "uint", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, [], ["0-60"]), 
            "password_policy_rules": MoPropertyMeta("password_policy_rules", "passwordPolicyRules", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 2500, None, [], []), 
            "user_disable_on_lockout": MoPropertyMeta("user_disable_on_lockout", "userDisableOnLockout", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []), 
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "userPasswordPolicy": "user_password_policy", 
            "childAction": "child_action", 
            "passwordPolicyRules": "password_policy_rules", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "userPasswordPolicy": "user_password_policy", 
            "allowedAttempts": "allowed_attempts", 
            "childAction": "child_action", 
            "lockoutPeriod": "lockout_period", 
            "passwordPolicyRules": "password_policy_rules", 
            "userDisableOnLockout": "user_disable_on_lockout", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.user_password_policy = None
        self.child_action = None
        self.password_policy_rules = None
        self.allowed_attempts = None
        self.lockout_period = None
        self.user_disable_on_lockout = None

        ManagedObject.__init__(self, "AaaUserPolicy", parent_mo_or_dn, **kwargs)

