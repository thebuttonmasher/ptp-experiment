from PTPSession import *

ptpip = PTPIPSession()
ptpip.open(host='192.168.1.2', port=15740)
#while 1:
#    cmd_to_send = int(input("input cmd"), 16)
#    param = input("and param")
#    if param:
#        param = int(param, 16)
#    param2 = input("and param2")
#    if param2:
#        param2 = int(param2, 16)
#    ptip_cmd = PtpIpCmdRequest(cmd=cmd_to_send, param1=param, param2=param2)
#    ptpip.send_recieve_ptpip_packet(ptip_cmd, ptpip.session)
#ptip_cmd1 = PtpIpCmdRequest(cmd=0x911a, param1=0xfffff792, param2=0x00000100, param3=0x0)
#ptip_cmd2 = PtpIpCmdRequest(cmd=0x911a, param1=0xfffff804, param2=0x00000100, param3=0x0)
ptip_cmd3 = PtpIpCmdRequest(cmd=0x9125, data_phase=0x01, tid=ptpip.transaction_id)
#ptip_cmd4 = PtpIpCmdRequest(cmd=0x911a, param1=0xfffffbfb, param2=0x00000100, param3=0x0)
#ptip_cmd5 = PtpIpCmdRequest(cmd=0x911a, param1=0xfffff806, param2=0x00000100, param3=0x0)
ptip_cmd6 = PtpIpCmdRequest(cmd=0x9008, data_phase=0x01, tid=ptpip.transaction_id)
ptip_cmd7 = PtpIpCmdRequest(cmd=0x9009, tid=ptpip.transaction_id)# param1=0x00010001, tid=ptpip.transaction_id)
ptip_cmd8 = PtpIpCmdRequest(cmd=0x9126, tid=ptpip.transaction_id)# param1=0x00020000, tid=ptpip.transaction_id)
cmds = [ptip_cmd3, ptip_cmd6, ptip_cmd7, ptip_cmd8]
for cmd in cmds:
    input("press enter to send next command...")
    ptpip.send_recieve_ptpip_packet(cmd, ptpip.session)
input("press enter to close session")