MAKE_ONLINE = (
    'l{callsign}\254\254{password}\015ONLINE3.38("{time_string}")\015{description}\015'
)
MAKE_OFFLINE = "l{callsign}\254\254{password}\015OFF-V3.40\015{description}\015"
MAKE_BUSY = (
    'l{callsign}\254\254{password}\015BUSY3.40("{time_string}")\015{description}\015'
)
GET_CALLS = "s"
