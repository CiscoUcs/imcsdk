"""This module contains the general information for BiosVfConsoleRedirection ManagedObject."""

from ...imcmo import ManagedObject
from ...imccoremeta import MoPropertyMeta, MoMeta
from ...imcmeta import VersionMeta


class BiosVfConsoleRedirectionConsts:
    VP_BAUD_RATE_115200 = "115200"
    VP_BAUD_RATE_19200 = "19200"
    VP_BAUD_RATE_38400 = "38400"
    VP_BAUD_RATE_57600 = "57600"
    VP_BAUD_RATE_9600 = "9600"
    VP_BAUD_RATE_PLATFORM_DEFAULT = "platform-default"
    VP_CONSOLE_REDIRECTION_COM_0 = "com-0"
    VP_CONSOLE_REDIRECTION_COM_1 = "com-1"
    VP_CONSOLE_REDIRECTION_DISABLED = "disabled"
    VP_CONSOLE_REDIRECTION_ENABLED = "enabled"
    VP_CONSOLE_REDIRECTION_PLATFORM_DEFAULT = "platform-default"
    VP_CONSOLE_REDIRECTION_SERIAL_PORT_A = "serial-port-a"
    VP_FLOW_CONTROL_NONE = "none"
    VP_FLOW_CONTROL_PLATFORM_DEFAULT = "platform-default"
    VP_FLOW_CONTROL_RTS_CTS = "rts-cts"
    VP_LEGACY_OSREDIRECTION_DISABLED = "Disabled"
    VP_LEGACY_OSREDIRECTION_ENABLED = "Enabled"
    _VP_LEGACY_OSREDIRECTION_DISABLED = "disabled"
    _VP_LEGACY_OSREDIRECTION_ENABLED = "enabled"
    VP_LEGACY_OSREDIRECTION_PLATFORM_DEFAULT = "platform-default"
    VP_PUTTY_KEY_PAD_ESCN = "ESCN"
    VP_PUTTY_KEY_PAD_LINUX = "LINUX"
    VP_PUTTY_KEY_PAD_SCO = "SCO"
    VP_PUTTY_KEY_PAD_VT100 = "VT100"
    VP_PUTTY_KEY_PAD_VT400 = "VT400"
    VP_PUTTY_KEY_PAD_XTERMR6 = "XTERMR6"
    VP_PUTTY_KEY_PAD_PLATFORM_DEFAULT = "platform-default"
    VP_REDIRECTION_AFTER_POST_ALWAYS_ENABLE = "Always Enable"
    VP_REDIRECTION_AFTER_POST_BOOTLOADER = "Bootloader"
    VP_REDIRECTION_AFTER_POST_PLATFORM_DEFAULT = "platform-default"
    VP_TERMINAL_TYPE_PC_ANSI = "pc-ansi"
    VP_TERMINAL_TYPE_PLATFORM_DEFAULT = "platform-default"
    VP_TERMINAL_TYPE_VT_UTF8 = "vt-utf8"
    VP_TERMINAL_TYPE_VT100 = "vt100"
    VP_TERMINAL_TYPE_VT100_PLUS = "vt100-plus"
    VP_BAUD_RATE_115_2K = "115.2k"
    VP_BAUD_RATE_19_2K = "19.2k"
    VP_BAUD_RATE_38_4K = "38.4k"
    VP_BAUD_RATE_57_6K = "57.6k"
    VP_BAUD_RATE_9_6K = "9.6k"


class BiosVfConsoleRedirection(ManagedObject):
    """This is BiosVfConsoleRedirection class."""

    consts = BiosVfConsoleRedirectionConsts()
    naming_props = set([])

    mo_meta = {
        "classic": MoMeta("BiosVfConsoleRedirection", "biosVfConsoleRedirection", "Console-redirection", VersionMeta.Version151f, "InputOutput", 0x7ff, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"]),
        "modular": MoMeta("BiosVfConsoleRedirection", "biosVfConsoleRedirection", "Console-redirection", VersionMeta.Version2013e, "InputOutput", 0x3ff, [], ["admin", "read-only", "user"], ['biosPlatformDefaults', 'biosSettings'], [], ["Get", "Set"])
    }


    prop_meta = {

        "classic": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_baud_rate": MoPropertyMeta("vp_baud_rate", "vpBaudRate", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["115200", "19200", "38400", "57600", "9600", "platform-default"], []),
            "vp_console_redirection": MoPropertyMeta("vp_console_redirection", "vpConsoleRedirection", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["com-0", "com-1", "disabled", "enabled", "platform-default", "serial-port-a"], []),
            "vp_flow_control": MoPropertyMeta("vp_flow_control", "vpFlowControl", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["none", "platform-default", "rts-cts"], []),
            "vp_putty_key_pad": MoPropertyMeta("vp_putty_key_pad", "vpPuttyKeyPad", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["ESCN", "LINUX", "SCO", "VT100", "VT400", "XTERMR6", "platform-default"], []),
            "vp_redirection_after_post": MoPropertyMeta("vp_redirection_after_post", "vpRedirectionAfterPOST", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["Always Enable", "Bootloader", "platform-default"], []),
            "vp_terminal_type": MoPropertyMeta("vp_terminal_type", "vpTerminalType", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["pc-ansi", "platform-default", "vt-utf8", "vt100", "vt100-plus"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version151f, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
            "vp_legacy_os_redirection": MoPropertyMeta("vp_legacy_os_redirection", "vpLegacyOSRedirection", "string", VersionMeta.Version151f, MoPropertyMeta.READ_WRITE, 0x400, None, None, None, ["Disabled", "Enabled", "disabled", "enabled", "platform-default"], []),
        },

        "modular": {
            "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x2, 0, 255, None, [], []),
            "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x4, 0, 255, None, [], []),
            "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, ["", "created", "deleted", "modified", "removed"], []),
            "vp_baud_rate": MoPropertyMeta("vp_baud_rate", "vpBaudRate", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x10, None, None, None, ["115.2k", "115200", "19.2k", "19200", "38.4k", "38400", "57.6k", "57600", "9.6k", "9600", "platform-default"], []),
            "vp_console_redirection": MoPropertyMeta("vp_console_redirection", "vpConsoleRedirection", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x20, None, None, None, ["com-0", "com-1", "disabled", "enabled", "platform-default", "serial-port-a"], []),
            "vp_flow_control": MoPropertyMeta("vp_flow_control", "vpFlowControl", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x40, None, None, None, ["RTS-CTS", "none", "platform-default", "rts-cts"], []),
            "vp_putty_key_pad": MoPropertyMeta("vp_putty_key_pad", "vpPuttyKeyPad", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x80, None, None, None, ["ESCN", "LINUX", "SCO", "VT100", "VT400", "XTERMR6", "platform-default"], []),
            "vp_redirection_after_post": MoPropertyMeta("vp_redirection_after_post", "vpRedirectionAfterPOST", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x100, None, None, None, ["Always Enable", "Bootloader", "platform-default"], []),
            "vp_terminal_type": MoPropertyMeta("vp_terminal_type", "vpTerminalType", "string", VersionMeta.Version2013e, MoPropertyMeta.READ_WRITE, 0x200, None, None, None, ["pc-ansi", "platform-default", "vt-utf8", "vt100", "vt100-plus"], []),
            "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version2013e, MoPropertyMeta.INTERNAL, None, None, None, None, [], []),
        },

    }

    prop_map = {

        "classic": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpBaudRate": "vp_baud_rate", 
            "vpConsoleRedirection": "vp_console_redirection", 
            "vpFlowControl": "vp_flow_control", 
            "vpPuttyKeyPad": "vp_putty_key_pad", 
            "vpRedirectionAfterPOST": "vp_redirection_after_post", 
            "vpTerminalType": "vp_terminal_type", 
            "childAction": "child_action", 
            "vpLegacyOSRedirection": "vp_legacy_os_redirection", 
        },

        "modular": {
            "dn": "dn", 
            "rn": "rn", 
            "status": "status", 
            "vpBaudRate": "vp_baud_rate", 
            "vpConsoleRedirection": "vp_console_redirection", 
            "vpFlowControl": "vp_flow_control", 
            "vpPuttyKeyPad": "vp_putty_key_pad", 
            "vpRedirectionAfterPOST": "vp_redirection_after_post", 
            "vpTerminalType": "vp_terminal_type", 
            "childAction": "child_action", 
        },

    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.status = None
        self.vp_baud_rate = None
        self.vp_console_redirection = None
        self.vp_flow_control = None
        self.vp_putty_key_pad = None
        self.vp_redirection_after_post = None
        self.vp_terminal_type = None
        self.child_action = None
        self.vp_legacy_os_redirection = None

        ManagedObject.__init__(self, "BiosVfConsoleRedirection", parent_mo_or_dn, **kwargs)

