from PTPPacket import PtpIpPacket
import struct

class PtpIpCmdRequest(PtpIpPacket):
    """

    """
    def __init__(self, data=None, cmd=None, param1=None, param2=None, param3=None, param4=None,
                param5=None, tid=0):
        super(PtpIpCmdRequest, self).__init__()
        self.cmdtype = struct.pack('I', 0x06)
        self.unkown = struct.pack('I', 0x01)
        self.ptp_cmd = cmd
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.param4 = param4
        self.param5 = param5
        self.transaction_id = struct.pack('I', tid)
        self.args = b''
        if self.param1 is not None:
            self.args = self.args + struct.pack('L', self.param1)

        if self.param2 is not None:
            self.args = self.args + struct.pack('L', self.param2)

        if self.param3 is not None:
            self.args = self.args + struct.pack('L', self.param3)

        if self.param4 is not None:
            self.args = self.args + struct.pack('L', self.param4)

        if self.param5 is not None:
            self.args = self.args + struct.pack('L', self.param5)

    def data(self):
        return self.cmdtype + self.unkown + struct.pack('H', self.ptp_cmd) + \
            self.transaction_id + self.args
