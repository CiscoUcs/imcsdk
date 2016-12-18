"""This module contains the general information for BiosVfOSBootWatchdogTimerPolicy ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfOSBootWatchdogTimerPolicyConsts:
    VP_OSBOOT_WATCHDOG_TIMER_POLICY_DO_NOTHING = "do-nothing"
    VP_OSBOOT_WATCHDOG_TIMER_POLICY_PLATFORM_DEFAULT = "platform-default"
    VP_OSBOOT_WATCHDOG_TIMER_POLICY_POWER_OFF = "power-off"
    VP_OSBOOT_WATCHDOG_TIMER_POLICY_RESET = "reset"


class BiosVfOSBootWatchdogTimerPolicy(ManagedObject):
    """This is BiosVfOSBootWatchdogTimerPolicy class."""

    consts = BiosVfOSBootWatchdogTimerPolicyConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfOSBootWatchdogTimerPolicy", "biosVfOSBootWatchdogTimerPolicy", "OS-Boot-Watchdog-Timer-Policy", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfOSBootWatchdogTimerPolicy", "biosVfOSBootWatchdogTimerPolicy", "OS-Boot-Watchdog-Timer-Policy", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_os_boot_watchdog_timer_policy": MoPropertyMeta("vp_os_boot_watchdog_timer_policy", "vpOSBootWatchdogTimerPolicy", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["do-nothing", "platform-default", "power-off", "reset"], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_os_boot_watchdog_timer_policy": MoPropertyMeta("vp_os_boot_watchdog_timer_policy", "vpOSBootWatchdogTimerPolicy", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["do-nothing", "platform-default", "power-off", "reset"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpOSBootWatchdogTimerPolicy": "vp_os_boot_watchdog_timer_policy", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpOSBootWatchdogTimerPolicy": "vp_os_boot_watchdog_timer_policy", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_os_boot_watchdog_timer_policy = None

        ManagedObject.__init__(self, "BiosVfOSBootWatchdogTimerPolicy", parent_mo_or_dn, **kwargs)

