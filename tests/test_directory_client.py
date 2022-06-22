from elpy import DirectoryClient

CALLSIGN = "N0CALL"
PASSWORD = "PassWord1!"
DESCRIPTION = "rmdlv's station"

HOST = "asia.echolink.org"

directory_client = DirectoryClient(CALLSIGN, PASSWORD, DESCRIPTION, HOST)


def test_requests():
    assert directory_client.make_online() == "OK2.5"
    assert directory_client.make_busy() == "OK2.5"
    assert directory_client.make_offline() == "OK2.5"

    assert directory_client.get_calls().startswith("@@@\n")
