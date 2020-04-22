"""This module contains the general information for BiosVfEnergyEfficientTurbo ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfEnergyEfficientTurboConsts:
    VP_ENERGY_EFFICIENT_TURBO_DISABLED = "Disabled"
    VP_ENERGY_EFFICIENT_TURBO_ENABLED = "Enabled"
    _VP_ENERGY_EFFICIENT_TURBO_DISABLED = "disabled"
    _VP_ENERGY_EFFICIENT_TURBO_ENABLED = "enabled"
    VP_ENERGY_EFFICIENT_TURBO_PLATFORM_DEFAULT = "platform-default"


class BiosVfEnergyEfficientTurbo(ManagedObject):
    """This is BiosVfEnergyEfficientTurbo class."""

    consts = BiosVfEnergyEfficientTurboConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfEnergyEfficientTurbo", "biosVfEnergyEfficientTurbo", "energy-efficient-turbo", VersionMeta.Version304a, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
        "modular": MoMeta("BiosVfEnergyEfficientTurbo", "biosVfEnergyEfficientTurbo", "energy-efficient-turbo", VersionMeta.Version404b, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_energy_efficient_turbo": MoPropertyMeta("vp_energy_efficient_turbo", "vpEnergyEfficientTurbo", "string", VersionMeta.Version304a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version304a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_energy_efficient_turbo": MoPropertyMeta("vp_energy_efficient_turbo", "vpEnergyEfficientTurbo", "string", VersionMeta.Version404b, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version404b, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpEnergyEfficientTurbo": "vp_energy_efficient_turbo", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpEnergyEfficientTurbo": "vp_energy_efficient_turbo", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_energy_efficient_turbo = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfEnergyEfficientTurbo", parent_mo_or_dn, **kwargs)

