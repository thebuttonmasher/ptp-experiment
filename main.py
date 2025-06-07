from PTPSession import *

ptpip = PTPIPSession()
ptpip.open(host='192.168.1.2', port=15740)
while 1:
    cmd_to_send = int(input("input cmd"))
    param = int(input("and param"))
    ptip_cmd = PtpIpCmdRequest(cmd=cmd_to_send, param1=param)
    ptpip.send_recieve_ptpip_packet(ptip_cmd, ptpip.session)