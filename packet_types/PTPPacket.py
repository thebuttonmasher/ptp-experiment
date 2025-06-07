import struct
from PTPInitFail import PtpIpInitFail
from PTPInitEvent import PtpIpEventReq
from PTPInitCommand import PtpIpInitCmdReq
from PTPInitEventACK import PtpIpEventAck
from PTPInitCommandACK import PtpIpInitCmdAck
from PTPCommandReq import PtpIpCmdRequest
from PTPCommandRES import PtpIpCmdResponse

class PtpIpPacket(object):
    """docstring for PtpIpCmd"""
    """        
            elif self.cmdtype == 9:
                return PtpIpStartDataPacket(data[4:])
            elif self.cmdtype == 10:
                return PtpIpDataPacket(data[4:])
            elif self.cmdtype == 12:
                return PtpIpEndDataPacket(data[4:])
            elif self.cmdtype == 13:
                return PtpIpPing(data[4:])
    """
    def __init__(self):
        super(PtpIpPacket, self).__init__()
        self.cmdtype = None

    def factory(self, data=None):
        if data is None:
            self.cmdtype = None
        else:
            print("Cmd Type: " + str(struct.unpack('I', data[0:4])[0]))
            self.cmdtype = struct.unpack('I', data[0:4])[0]
        if self.cmdtype == 1:
            return PtpIpInitCmdReq(data[4:])
        elif self.cmdtype == 2:
            return PtpIpInitCmdAck(data[4:])
        elif self.cmdtype == 3:
            return PtpIpEventReq(data[4:])
        elif self.cmdtype == 4:
            return PtpIpEventAck(data[4:])
        elif self.cmdtype == 5:
            return PtpIpInitFail(data[4:])
        elif self.cmdtype == 6:
            return PtpIpCmdRequest(data[4:])
        elif self.cmdtype == 7:
            return PtpIpCmdResponse(data[4:])
        return None

    def data(self):
        pass
