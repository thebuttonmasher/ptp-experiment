from PTPSession import *

ptpip = PTPIPSession()
ptpip.open(host='192.168.1.2', port=15740)
while 1:
    cmd_to_send = int(input("input cmd"), 16)
    param = input("and param")
    if param:
        param = int(param, 16)
    param2 = input("and param2")
    if param2:
        param2 = int(param2, 16)
    ptip_cmd = PtpIpCmdRequest(cmd=cmd_to_send, param1=param, param2=param2)
    ptpip.send_recieve_ptpip_packet(ptip_cmd, ptpip.session)