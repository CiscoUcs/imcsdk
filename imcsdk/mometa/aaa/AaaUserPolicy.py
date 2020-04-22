"""This module contains the general information for AaaUserPolicy ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class AaaUserPolicyConsts:
    USER_MODE_IPMI = "ipmi"
    USER_MODE_NON_IPMI = "non-ipmi"


class AaaUserPolicy(ManagedObject):
    """This is AaaUserPolicy class."""

    consts = AaaUserPolicyConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("AaaUserPolicy", "aaaUserPolicy", "policy", VersionMeta.Version209c, "InputOutput", 0x1ff, [], ["admin", "user"], ['aaaUserEp'], [], ["Get", "Set"]),
        "modular": MoMeta("AaaUserPolicy", "aaaUserPolicy", "policy", VersionMeta.Version2013e, "InputOutput", 0x1ff, [], ["admin", "user"], ['aaaUserEp'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "allowed_attempts": MoPropertyMeta("allowed_attempts", "allowedAttempts", "uint", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["0-20"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "lockout_period": MoPropertyMeta("lockout_period", "lockoutPeriod", "uint", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-60"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "user_disable_on_lockout": MoPropertyMeta("user_disable_on_lockout", "userDisableOnLockout", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "user_mode": MoPropertyMeta("user_mode", "userMode", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["ipmi", "non-ipmi"], []),
            "user_password_policy": MoPropertyMeta("user_password_policy", "userPasswordPolicy", "string", VersionMeta.Version209c, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version209c, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "password_policy_rules": MoPropertyMeta("password_policy_rules", "passwordPolicyRules", "string", VersionMeta.Version209c, MoPropertyMeta.READ_ONLY, None, 0, 2500, None, [], []),
        },

        "modular": {
            "allowed_attempts": MoPropertyMeta("allowed_attempts", "allowedAttempts", "uint", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["0-20"]),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "lockout_period": MoPropertyMeta("lockout_period", "lockoutPeriod", "uint", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], ["0-60"]),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "user_disable_on_lockout": MoPropertyMeta("user_disable_on_lockout", "userDisableOnLockout", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "user_mode": MoPropertyMeta("user_mode", "userMode", "string", VersionMeta.Version411c, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["ipmi", "non-ipmi"], []),
            "user_password_policy": MoPropertyMeta("user_password_policy", "userPasswordPolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["Disabled", "Enabled", "disabled", "enabled"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "password_policy_rules": MoPropertyMeta("password_policy_rules", "passwordPolicyRules", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_ONLY, None, 0, 2500, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "allowedAttempts": "allowed_attempts", 
            "dn": "dn", 
            "lockoutPeriod": "lockout_period", 
            "rn": "rn", 
            "status": "status", 
            "userDisableOnLockout": "user_disable_on_lockout", 
            "userMode": "user_mode", 
            "userPasswordPolicy": "user_password_policy", 
            "childAction": "child_action", 
            "passwordPolicyRules": "password_policy_rules", 
        },

        "modular": {
            "allowedAttempts": "allowed_attempts", 
            "dn": "dn", 
            "lockoutPeriod": "lockout_period", 
            "rn": "rn", 
            "status": "status", 
            "userDisableOnLockout": "user_disable_on_lockout", 
            "userMode": "user_mode", 
            "userPasswordPolicy": "user_password_policy", 
            "childAction": "child_action", 
            "passwordPolicyRules": "password_policy_rules", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.allowed_attempts = None
        self.lockout_period = None
        self.status = None
        self.user_disable_on_lockout = None
        self.user_mode = None
        self.user_password_policy = None
        self.child_action = None
        self.password_policy_rules = None

        ManagedObject.__init__(self, "AaaUserPolicy", parent_mo_or_dn, **kwargs)

