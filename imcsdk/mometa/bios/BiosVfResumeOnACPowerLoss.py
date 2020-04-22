"""This module contains the general information for BiosVfResumeOnACPowerLoss ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfResumeOnACPowerLossConsts:
    DELAY_TYPE_FIXED = "fixed"
    DELAY_TYPE_RANDOM = "random"
    VP_RESUME_ON_ACPOWER_LOSS_LAST_STATE = "last-state"
    VP_RESUME_ON_ACPOWER_LOSS_RESET = "reset"
    VP_RESUME_ON_ACPOWER_LOSS_STAY_OFF = "stay-off"
    VP_RESUME_ON_ACPOWER_LOSS_PLATFORM_DEFAULT = "platform-default"


class BiosVfResumeOnACPowerLoss(ManagedObject):
    """This is BiosVfResumeOnACPowerLoss class."""

    consts = BiosVfResumeOnACPowerLossConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfResumeOnACPowerLoss", "biosVfResumeOnACPowerLoss", "Resume-on-AC-power-loss", VersionMeta.Version151f, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['computeBoard'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfResumeOnACPowerLoss", "biosVfResumeOnACPowerLoss", "Resume-on-AC-power-loss", VersionMeta.Version2013e, "InputOutput", 0x7f, [], ["admin", "read-only", "user"], ['computeBoard'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "delay": MoPropertyMeta("delay", "delay", "uint", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["0-240"]),
            "delay_type": MoPropertyMeta("delay_type", "delayType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["fixed", "random"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_resume_on_ac_power_loss": MoPropertyMeta("vp_resume_on_ac_power_loss", "vpResumeOnACPowerLoss", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["last-state", "reset", "stay-off"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "delay": MoPropertyMeta("delay", "delay", "uint", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, None, None, None, [], ["0-240"]),
            "delay_type": MoPropertyMeta("delay_type", "delayType", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, None, None, None, ["fixed", "random"], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_resume_on_ac_power_loss": MoPropertyMeta("vp_resume_on_ac_power_loss", "vpResumeOnACPowerLoss", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["last-state", "platform-default", "reset", "stay-off"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "delay": "delay", 
            "delayType": "delay_type", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpResumeOnACPowerLoss": "vp_resume_on_ac_power_loss", 
            "childAction": "child_action", 
        },

        "modular": {
            "delay": "delay", 
            "delayType": "delay_type", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpResumeOnACPowerLoss": "vp_resume_on_ac_power_loss", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.delay = None
        self.delay_type = None
        self.status = None
        self.vp_resume_on_ac_power_loss = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfResumeOnACPowerLoss", parent_mo_or_dn, **kwargs)

