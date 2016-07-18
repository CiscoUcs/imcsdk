import logging
from connection.info import imc_login, imc_logout

logging.basicConfig()
log = logging.getLogger('imc')
log.setLevel(logging.DEBUG)


def boot_order(handle):
    boot_order_dict = {}
    boot_device_list = handle.query_children(in_dn=
                                             "sys/rack-unit-1/boot-precision")
    log.info("   Precision Boot Order is:")
    log.info("------------------------------")
    log.info("   Order \t\t Device")
    for device in boot_device_list:
        if hasattr(device, "order"):
            boot_order_dict[int(device.order)] = device

    for b_order in sorted(boot_order_dict.keys()):
        if hasattr(boot_order_dict[b_order], "subtype") and \
                        boot_order_dict[b_order].subtype is not None:
            device_type = boot_order_dict[b_order].type + "  " + \
                   boot_order_dict[b_order].subtype
        else:
            device_type = boot_order_dict[b_order].type
        log.info("    %s           %s" %(b_order, device_type))


def main():
    handle = imc_login()
    handle.set_dump_xml()

    boot_order(handle)

    handle.unset_dump_xml()
    imc_logout(handle)

main()
