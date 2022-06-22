class InvalidResponse(Exception):
    def __init__(self, response: str) -> None:
        super().__init__("Response must me OK2.5, but returned: " + response)
