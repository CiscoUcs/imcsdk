import logging
from connection.info import imc_login, imc_logout
from imcsdk.imccoreutils import write_object

logging.basicConfig()
log = logging.getLogger('imc')
log.setLevel(logging.DEBUG)


def main():
    handle = imc_login()
    handle.set_dump_xml()

    firmware_list = handle.query_classid(class_id="firmwareRunning")
    write_object(mo_or_list=firmware_list)

    handle.unset_dump_xml()
    imc_logout(handle)

main()
