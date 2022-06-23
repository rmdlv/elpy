import pytest

from elpy import DirectoryClient

from elpy.clients.directory import LoginRequired

CALLSIGN = "N0CALL"
PASSWORD = "PassWord1!"
DESCRIPTION = "rmdlv's station"

HOST = "asia.echolink.org"

directory_client = DirectoryClient(CALLSIGN, PASSWORD, DESCRIPTION, HOST)


def test_unathorized_request():
    with pytest.raises(LoginRequired):
        directory_client.get_stations()


def test_requests():
    assert directory_client.make_online() == "OK2.5"
    assert directory_client.make_busy() == "OK2.5"
    assert directory_client.make_offline() == "OK2.5"

    assert directory_client.get_stations().startswith("@@@\n")
