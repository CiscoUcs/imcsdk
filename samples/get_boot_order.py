import logging
from connection.info import imc_login, imc_logout
from imcsdk.imccoreutils import write_object

logging.basicConfig()
log = logging.getLogger('imc')
log.setLevel(logging.DEBUG)


def boot_order(handle):
    boot_device_list = handle.query_children(in_dn=
                                             "sys/rack-unit-1/boot-policy")
    log.info("   Boot Order is:")
    log.info("-------------------")
    log.info("   Order \t\t Device")
    for device in boot_device_list:
        if hasattr(device, "order"):
            log.info("    %s \t\t\t %s" %(device.order, device.type))


def main():
    handle = imc_login()
    handle.set_dump_xml()

    boot_order(handle)

    handle.unset_dump_xml()
    imc_logout(handle)

main()
