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
ptip_cmd1 = PtpIpCmdRequest(cmd=0x911a, param1=0xfffff792, param2=0x00000100, param3=0x0)
ptip_cmd2 = PtpIpCmdRequest(cmd=0x911a, param1=0xfffff804, param2=0x00000100, param3=0x0)
ptip_cmd3 = PtpIpCmdRequest(cmd=0x9110)
ptip_cmd4 = PtpIpCmdRequest(cmd=0x911a, param1=0xfffff801, param2=0x00000100, param3=0x0)
ptip_cmd5 = PtpIpCmdRequest(cmd=0x911a, param1=0xfffff806, param2=0x00000100, param3=0x0)
ptip_cmd6 = PtpIpCmdRequest(cmd=0x9110)
ptip_cmd7 = PtpIpCmdRequest(cmd=0x9102, param1=0x00010001)
ptip_cmd8 = PtpIpCmdRequest(cmd=0x9102, param1=0x00020000)
cmds = [ptip_cmd1, ptip_cmd2, ptip_cmd3, ptip_cmd4, ptip_cmd5, ptip_cmd6, ptip_cmd7, ptip_cmd8]
for cmd in cmds:
    input("press enter to send next command...")
    ptpip.send_recieve_ptpip_packet(cmd, ptpip.session)
