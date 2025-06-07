import socket
import struct
from packet_types import *
from packet_types.PTPPacket import *
from packet_types.PTPInitCommand import *
from packet_types.PTPInitEvent import *
from packet_types.PTPInitCommandACK import *
from packet_types.PTPInitEventACK import *
from packet_types.PTPCommandReq import *
from packet_types.PTPCommandRES import *

def connect(host='192.168.1.2', port=15740):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    s.bind(('192.168.1.3', 0))
    s.connect((host, port))
    return s


class PTPIPSession:

    def __init__(self):
        self.session = None
        self.session_events = None
        self.session_id = None
        self.cmd_queue = []
        self.event_queue = []
        self.object_queue = []
        self.transaction_id = 0

    def open(self, host, port):
        self.session = connect(host=host, port=port)
        self.send_recieve_ptpip_packet(PtpIpInitCmdReq(), self.session)
        self.session_events = connect(host=host, port=port)
        self.send_recieve_ptpip_packet(PtpIpEventReq(), self.session_events)

        print(f"session id: {self.session_id}")
        ptip_cmd = PtpIpCmdRequest(cmd=0x1002, param1=int.from_bytes(self.session_id, "little"))
        self.send_recieve_ptpip_packet(ptip_cmd, self.session)


    def send_data(self, data, session):
        session.send(struct.pack('I', len(data) + 4) + data)
        self.transaction_id += 1

    def recieve_data(self, session):
        data = session.recv(4)
        (data_length,) = struct.unpack('I', data)
        print ("packet length: " + str(data_length))
        while data_length > len(data):
            data += session.recv(data_length - len(data))
        return data[4:]

    def send_recieve_ptpip_packet(self, ptpip_packet, session):
        if isinstance(ptpip_packet, PtpIpInitCmdReq):
            self.send_data(ptpip_packet.data(), session)

            # set the session id of the object if the reply is of type PtpIpInitCmdAck
            ptpip_packet_reply = PtpIpPacket().factory(data=self.recieve_data(session))

            if isinstance(ptpip_packet_reply, PtpIpInitCmdAck):
                self.session_id = ptpip_packet_reply.session_id

        elif isinstance(ptpip_packet, PtpIpEventReq):
            self.send_ptpip_event_req(ptpip_packet, session)
            ptpip_packet_reply = PtpIpPacket().factory(data=self.recieve_data(session))

        else:
            self.send_data(ptpip_packet.data(), session)
            ptpip_packet_reply = PtpIpPacket().factory(data=self.recieve_data(session))

        return ptpip_packet_reply

    def send_ptpip_event_req(self, ptpip_packet, session):
        # add the session id of the object itself if it is not specified in the package
        if ptpip_packet.session_id is None:
                ptpip_packet.session_id = self.session_id
        self.send_data(ptpip_packet.data(), session)
