"""This module contains the general information for BiosVfOSBootWatchdogTimerTimeout ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfOSBootWatchdogTimerTimeoutConsts:
    VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_10_MINUTES = "10-minutes"
    VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_15_MINUTES = "15-minutes"
    VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_20_MINUTES = "20-minutes"
    VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_5_MINUTES = "5-minutes"
    VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_PLATFORM_DEFAULT = "platform-default"
    __VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_10_MINUTES = "10 minutes"
    __VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_15_MINUTES = "15 minutes"
    __VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_20_MINUTES = "20 minutes"
    __VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT_5_MINUTES = "5 minutes"


class BiosVfOSBootWatchdogTimerTimeout(ManagedObject):
    """This is BiosVfOSBootWatchdogTimerTimeout class."""

    consts = BiosVfOSBootWatchdogTimerTimeoutConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfOSBootWatchdogTimerTimeout", "biosVfOSBootWatchdogTimerTimeout", "OS-Boot-Watchdog-Timer-Time-Out", VersionMeta.Version151x, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfOSBootWatchdogTimerTimeout", "biosVfOSBootWatchdogTimerTimeout", "OS-Boot-Watchdog-Timer-Time-Out", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_os_boot_watchdog_timer_timeout": MoPropertyMeta("vp_os_boot_watchdog_timer_timeout", "vpOSBootWatchdogTimerTimeout", "string", VersionMeta.Version151x, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["10-minutes", "15-minutes", "20-minutes", "5-minutes", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151x, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_os_boot_watchdog_timer_timeout": MoPropertyMeta("vp_os_boot_watchdog_timer_timeout", "vpOSBootWatchdogTimerTimeout", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["10 minutes", "10-minutes", "15 minutes", "15-minutes", "20 minutes", "20-minutes", "5 minutes", "5-minutes", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpOSBootWatchdogTimerTimeout": "vp_os_boot_watchdog_timer_timeout", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpOSBootWatchdogTimerTimeout": "vp_os_boot_watchdog_timer_timeout", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_os_boot_watchdog_timer_timeout = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfOSBootWatchdogTimerTimeout", parent_mo_or_dn, **kwargs)

