import os, sys

python_cmd          = "python3"
target_id           = 0x31100004
min_version_os      = 0x01050500    # e.g. 1.5.5 => 1.5.5.0 => 0x01050500
min_version_mcu     = 0x01070000    # e.g. 1.7   => 1.7.0.0 => 0x01070000
file_name           = "/root/veo-ledger/download/app.hex"
data_size           = 0x00000000    # `cat debug/app.map |grep _nvram_data_size | tr -s ' ' | cut -f2 -d' '`
icon_hex            = "0100000000ffffff00ffffffff1ff88ff067e633ce13ce4bc7e3d273c873cc67e60ff11ff8ffffffff"
cmd_check_version   = "-m get_ledger_version --targetId 0x%08X --minVersionOS 0x%08X --minVersionMCU 0x%08X" % (target_id, min_version_os, min_version_mcu)
cmd_load_app        = "-m ledgerblue.loadApp --appFlags 0x00 --tlv --targetId 0x%08X --delete --fileName %s --appName \"Amoveo\" --appVersion 1.0.0 --dataSize 0x%08X --icon %s" % (target_id, file_name, data_size, icon_hex)

exit_code = 1
try:
    exit_code = os.system("%s %s" % (python_cmd, cmd_check_version))
    if exit_code != 0:          # muXxer: Otherwise it returned 256, which was recognized as 0 in the shell
        exit_code = 2
    else:
        exit_code = os.system("%s %s" % (python_cmd, cmd_load_app))
        if exit_code != 0:      # muXxer: Otherwise it returned 256, which was recognized as 0 in the shell
            exit_code = 3
except:
    pass
sys.exit(exit_code)
