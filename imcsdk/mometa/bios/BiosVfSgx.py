"""This module contains the general information for BiosVfSgx ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfSgxConsts:
    VP_ENABLE_SGX_DISABLED = "Disabled"
    VP_ENABLE_SGX_ENABLED = "Enabled"
    _VP_ENABLE_SGX_DISABLED = "disabled"
    _VP_ENABLE_SGX_ENABLED = "enabled"
    VP_ENABLE_SGX_PLATFORM_DEFAULT = "platform-default"
    VP_SGX_AUTO_REGISTRATION_AGENT_DISABLED = "Disabled"
    VP_SGX_AUTO_REGISTRATION_AGENT_ENABLED = "Enabled"
    _VP_SGX_AUTO_REGISTRATION_AGENT_DISABLED = "disabled"
    _VP_SGX_AUTO_REGISTRATION_AGENT_ENABLED = "enabled"
    VP_SGX_AUTO_REGISTRATION_AGENT_PLATFORM_DEFAULT = "platform-default"
    VP_SGX_FACTORY_RESET_DISABLED = "Disabled"
    VP_SGX_FACTORY_RESET_ENABLED = "Enabled"
    _VP_SGX_FACTORY_RESET_DISABLED = "disabled"
    _VP_SGX_FACTORY_RESET_ENABLED = "enabled"
    VP_SGX_FACTORY_RESET_PLATFORM_DEFAULT = "platform-default"
    VP_SGX_LE_WR_DISABLED = "Disabled"
    VP_SGX_LE_WR_ENABLED = "Enabled"
    _VP_SGX_LE_WR_DISABLED = "disabled"
    _VP_SGX_LE_WR_ENABLED = "enabled"
    VP_SGX_LE_WR_PLATFORM_DEFAULT = "platform-default"
    VP_SGX_PACKAGE_INFO_IN_BAND_ACCESS_DISABLED = "Disabled"
    VP_SGX_PACKAGE_INFO_IN_BAND_ACCESS_ENABLED = "Enabled"
    _VP_SGX_PACKAGE_INFO_IN_BAND_ACCESS_DISABLED = "disabled"
    _VP_SGX_PACKAGE_INFO_IN_BAND_ACCESS_ENABLED = "enabled"
    VP_SGX_PACKAGE_INFO_IN_BAND_ACCESS_PLATFORM_DEFAULT = "platform-default"
    VP_SGX_QOS_DISABLED = "Disabled"
    VP_SGX_QOS_ENABLED = "Enabled"
    _VP_SGX_QOS_DISABLED = "disabled"
    _VP_SGX_QOS_ENABLED = "enabled"
    VP_SGX_QOS_PLATFORM_DEFAULT = "platform-default"


class BiosVfSgx(ManagedObject):
    """This is BiosVfSgx class."""

    consts = BiosVfSgxConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfSgx", "biosVfSgx", "Enable-Sgx", VersionMeta.Version421a, "InputOutput", 0x3ff, [], ["admin"], ['biosPlatformDefaults', 'biosSettings'], [], [None]),
    }


    prop_meta = {

        "classic": {
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version421a, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_enable_sgx": MoPropertyMeta("vp_enable_sgx", "vpEnableSgx", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_sgx_auto_registration_agent": MoPropertyMeta("vp_sgx_auto_registration_agent", "vpSgxAutoRegistrationAgent", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_sgx_factory_reset": MoPropertyMeta("vp_sgx_factory_reset", "vpSgxFactoryReset", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_sgx_le_wr": MoPropertyMeta("vp_sgx_le_wr", "vpSgxLeWr", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_sgx_package_info_in_band_access": MoPropertyMeta("vp_sgx_package_info_in_band_access", "vpSgxPackageInfoInBandAccess", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
            "vp_sgx_qos": MoPropertyMeta("vp_sgx_qos", "vpSgxQos", "string", VersionMeta.Version421a, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

    }

    prop_map = {

        "classic": {
            "childAction": "child_action", 
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpEnableSgx": "vp_enable_sgx", 
            "vpSgxAutoRegistrationAgent": "vp_sgx_auto_registration_agent", 
            "vpSgxFactoryReset": "vp_sgx_factory_reset", 
            "vpSgxLeWr": "vp_sgx_le_wr", 
            "vpSgxPackageInfoInBandAccess": "vp_sgx_package_info_in_band_access", 
            "vpSgxQos": "vp_sgx_qos", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.status = None
        self.vp_enable_sgx = None
        self.vp_sgx_auto_registration_agent = None
        self.vp_sgx_factory_reset = None
        self.vp_sgx_le_wr = None
        self.vp_sgx_package_info_in_band_access = None
        self.vp_sgx_qos = None

        ManagedObject.__init__(self, "BiosVfSgx", parent_mo_or_dn, **kwargs)

