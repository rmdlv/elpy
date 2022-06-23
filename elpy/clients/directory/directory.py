import socket
from datetime import datetime

from .packet_patterns import MAKE_ONLINE, MAKE_OFFLINE, MAKE_BUSY, GET_STATIONS

from .exceptions import InvalidResponse, LoginRequired


class DirectoryClient:
    PACKET_ENCODING = "latin1"
    CHUNK_SIZE = 1024

    def __init__(
        self,
        callsign: str,
        password: str,
        description: str,
        host: str,
        port: int = 5200,
    ) -> None:
        self.callsign = callsign
        self.password = password
        self.description = description

        self.host = host
        self.port = port

        self._logged = False

    def _send_packet(self, packet: str, validate: bool = False) -> str:
        tcp_client = socket.socket()
        tcp_client.connect((self.host, self.port))
        tcp_client.send(packet.encode(self.PACKET_ENCODING))

        # Read full response by chunks
        response = b""
        while True:
            chunk_data = tcp_client.recv(self.CHUNK_SIZE)
            if chunk_data:
                response += chunk_data
            else:
                tcp_client.close()

                response = response.decode(self.PACKET_ENCODING)
                if validate and not self._validate_response(response):
                    raise InvalidResponse(response)

                return response

    def _get_time_string(self) -> str:
        now = datetime.now()
        return now.strftime("%H:%M")

    def _validate_response(self, response: str) -> bool:
        if response != "OK2.5":
            return False
        return True

    def make_online(self):
        response = self._send_packet(
            MAKE_ONLINE.format(
                callsign=self.callsign,
                password=self.password,
                time_string=self._get_time_string(),
                description=self.description,
            ),
            True,
        )
        self._logged = True
        return response

    def make_offline(self):
        response = self._send_packet(
            MAKE_OFFLINE.format(
                callsign=self.callsign,
                password=self.password,
                description=self.description,
            ),
            True,
        )
        self._logged = True
        return response

    def make_busy(self):
        response = self._send_packet(
            MAKE_BUSY.format(
                callsign=self.callsign,
                password=self.password,
                time_string=self._get_time_string(),
                description=self.description,
            ),
            True,
        )
        self._logged = True
        return response

    def get_stations(self):
        if not self._logged:
            raise LoginRequired
        response = self._send_packet(GET_STATIONS)
        # TODO: Add station list parsing
        return response
