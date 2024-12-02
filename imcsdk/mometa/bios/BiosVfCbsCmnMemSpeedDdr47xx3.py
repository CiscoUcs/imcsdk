"""This module contains the general information for BiosVfCbsCmnMemSpeedDdr47xx3 ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfCbsCmnMemSpeedDdr47xx3Consts:
    VP_CBS_CMN_MEM_SPEED_DDR47XX3_1067_MHZ = "1067MHz"
    VP_CBS_CMN_MEM_SPEED_DDR47XX3_1200_MHZ = "1200MHz"
    VP_CBS_CMN_MEM_SPEED_DDR47XX3_1333_MHZ = "1333MHz"
    VP_CBS_CMN_MEM_SPEED_DDR47XX3_1467_MHZ = "1467MHz"
    VP_CBS_CMN_MEM_SPEED_DDR47XX3_1600_MHZ = "1600MHz"
    VP_CBS_CMN_MEM_SPEED_DDR47XX3_1633_MHZ = "1633MHz"
    VP_CBS_CMN_MEM_SPEED_DDR47XX3_1667_MHZ = "1667MHz"
    VP_CBS_CMN_MEM_SPEED_DDR47XX3_1700_MHZ = "1700MHz"
    VP_CBS_CMN_MEM_SPEED_DDR47XX3_1733_MHZ = "1733MHz"
    VP_CBS_CMN_MEM_SPEED_DDR47XX3_1767_MHZ = "1767MHz"
    VP_CBS_CMN_MEM_SPEED_DDR47XX3_1800_MHZ = "1800MHz"
    VP_CBS_CMN_MEM_SPEED_DDR47XX3_400_MHZ = "400MHz"
    VP_CBS_CMN_MEM_SPEED_DDR47XX3_800_MHZ = "800MHz"
    VP_CBS_CMN_MEM_SPEED_DDR47XX3_933_MHZ = "933MHz"
    VP_CBS_CMN_MEM_SPEED_DDR47XX3_AUTO = "Auto"
    VP_CBS_CMN_MEM_SPEED_DDR47XX3_PLATFORM_DEFAULT = "platform-default"


class BiosVfCbsCmnMemSpeedDdr47xx3(ManagedObject):
    """This is BiosVfCbsCmnMemSpeedDdr47xx3 class."""

    consts = BiosVfCbsCmnMemSpeedDdr47xx3Consts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfCbsCmnMemSpeedDdr47xx3", "biosVfCbsCmnMemSpeedDdr47xx3", "memory-clock-speed-7xx3", VersionMeta.Version434_240077, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version434_240077, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_cbs_cmn_mem_speed_ddr47xx3": MoPropertyMeta("vp_cbs_cmn_mem_speed_ddr47xx3", "vpCbsCmnMemSpeedDdr47xx3", "string", VersionMeta.Version434_240077, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["1067MHz", "1200MHz", "1333MHz", "1467MHz", "1600MHz", "1633MHz", "1667MHz", "1700MHz", "1733MHz", "1767MHz", "1800MHz", "400MHz", "800MHz", "933MHz", "Auto", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpCbsCmnMemSpeedDdr47xx3": "vp_cbs_cmn_mem_speed_ddr47xx3", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_cbs_cmn_mem_speed_ddr47xx3 = None

        ManagedObject.__init__(self, "BiosVfCbsCmnMemSpeedDdr47xx3", parent_mo_or_dn, **kwargs)

