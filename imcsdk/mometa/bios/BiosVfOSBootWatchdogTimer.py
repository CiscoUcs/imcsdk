"""This module contains the general information for BiosVfOSBootWatchdogTimer ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfOSBootWatchdogTimerConsts:
    VP_OSBOOT_WATCHDOG_TIMER_DISABLED = "Disabled"
    VP_OSBOOT_WATCHDOG_TIMER_ENABLED = "Enabled"
    _VP_OSBOOT_WATCHDOG_TIMER_DISABLED = "disabled"
    _VP_OSBOOT_WATCHDOG_TIMER_ENABLED = "enabled"
    VP_OSBOOT_WATCHDOG_TIMER_PLATFORM_DEFAULT = "platform-default"


class BiosVfOSBootWatchdogTimer(ManagedObject):
    """This is BiosVfOSBootWatchdogTimer class."""

    consts = BiosVfOSBootWatchdogTimerConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfOSBootWatchdogTimer", "biosVfOSBootWatchdogTimer", "OS-Boot-Watchdog-Timer-Param", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfOSBootWatchdogTimer", "biosVfOSBootWatchdogTimer", "OS-Boot-Watchdog-Timer-Param", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], [u'biosPlatformDefaults', u'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_os_boot_watchdog_timer": MoPropertyMeta("vp_os_boot_watchdog_timer", "vpOSBootWatchdogTimer", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        },

        "modular": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []), 
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []), 
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []), 
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []), 
            "vp_os_boot_watchdog_timer": MoPropertyMeta("vp_os_boot_watchdog_timer", "vpOSBootWatchdogTimer", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []), 
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpOSBootWatchdogTimer": "vp_os_boot_watchdog_timer", 
        },

        "modular": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpOSBootWatchdogTimer": "vp_os_boot_watchdog_timer", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_os_boot_watchdog_timer = None

        ManagedObject.__init__(self, "BiosVfOSBootWatchdogTimer", parent_mo_or_dn, **kwargs)

