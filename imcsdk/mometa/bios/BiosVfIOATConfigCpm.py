"""This module contains the general information for BiosVfIOATConfigCpm ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfIOATConfigCpmConsts:
    VP_IOATCONFIG_CPM_DISABLED = "Disabled"
    VP_IOATCONFIG_CPM_ENABLED = "Enabled"
    _VP_IOATCONFIG_CPM_DISABLED = "disabled"
    _VP_IOATCONFIG_CPM_ENABLED = "enabled"
    VP_IOATCONFIG_CPM_PLATFORM_DEFAULT = "platform-default"


class BiosVfIOATConfigCpm(ManagedObject):
    """This is BiosVfIOATConfigCpm class."""

    consts = BiosVfIOATConfigCpmConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfIOATConfigCpm", "biosVfIOATConfigCpm", "IOAT Configuration", VersionMeta.Version433_240024, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version433_240024, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_ioat_config_cpm": MoPropertyMeta("vp_ioat_config_cpm", "vpIOATConfigCpm", "string", VersionMeta.Version433_240024, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpIOATConfigCpm": "vp_ioat_config_cpm", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_ioat_config_cpm = None

        ManagedObject.__init__(self, "BiosVfIOATConfigCpm", parent_mo_or_dn, **kwargs)

