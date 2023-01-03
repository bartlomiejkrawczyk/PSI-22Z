class Packet:
    _content: bytes
    # based on final implementation this might be just bytes
    # with special functions to convert it to more headers and data
    # or
    # it might be parsed to/from bytes to headers and data in a constructor

    def __init__(self, data: bytes) -> None:
        self._content: bytes = data

    def content(self) -> bytes:
        return self._content

    def size(self) -> int:
        return len(self._content)


packet_type_client = {
    "initial": "1",
    "session_data": "2",
    "declaration": "3",
    "send": "4",
    "error": "5",
    "close": "6"
}

packet_type_server = {
    "initial": "1",
    "session_data": "2",
    "acknowledge": "3",
    "receive": "4",
    "terminal": "5",
    "close": "6",
    "malformed": "7",
}
