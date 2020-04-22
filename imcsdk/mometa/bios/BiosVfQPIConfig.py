"""This module contains the general information for BiosVfQPIConfig ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfQPIConfigConsts:
    VP_QPILINK_FREQUENCY_6_4_GT_S = "6.4-gt/s"
    VP_QPILINK_FREQUENCY_7_2_GT_S = "7.2-gt/s"
    VP_QPILINK_FREQUENCY_8_0_GT_S = "8.0-gt/s"
    VP_QPILINK_FREQUENCY_9_6_GT_S = "9.6-gt/s"
    VP_QPILINK_FREQUENCY_AUTO = "auto"
    VP_QPILINK_FREQUENCY_PLATFORM_DEFAULT = "platform-default"


class BiosVfQPIConfig(ManagedObject):
    """This is BiosVfQPIConfig class."""

    consts = BiosVfQPIConfigConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfQPIConfig", "biosVfQPIConfig", "QPI-Config", VersionMeta.Version151f, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfQPIConfig", "biosVfQPIConfig", "QPI-Config", VersionMeta.Version2013e, "InputOutput", 0x1f, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_qpi_link_frequency": MoPropertyMeta("vp_qpi_link_frequency", "vpQPILinkFrequency", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["6.4-gt/s", "7.2-gt/s", "8.0-gt/s", "9.6-gt/s", "auto", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_qpi_link_frequency": MoPropertyMeta("vp_qpi_link_frequency", "vpQPILinkFrequency", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["6.4-gt/s", "7.2-gt/s", "8.0-gt/s", "9.6-gt/s", "auto", "platform-default"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpQPILinkFrequency": "vp_qpi_link_frequency", 
            "childAction": "child_action", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpQPILinkFrequency": "vp_qpi_link_frequency", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_qpi_link_frequency = None
        self.child_action = None

        ManagedObject.__init__(self, "BiosVfQPIConfig", parent_mo_or_dn, **kwargs)

