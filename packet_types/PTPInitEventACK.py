from .PTPPacket import PtpIpPacket
import struct

class PtpIpEventAck(PtpIpPacket):
    """docstring for PtpIpInitCmd"""
    def __init__(self, data=None):
        super(PtpIpEventAck, self).__init__()
        self.cmdtype = struct.pack('I', 0x04)