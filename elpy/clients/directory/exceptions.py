class InvalidResponse(Exception):
    def __init__(self, response: str) -> None:
        super().__init__("Response must be OK2.5, but returned: " + response)


class LoginRequired(Exception):
    def __init__(self) -> None:
        super().__init__("Need to execute make_online, make_offline or make_busy")
