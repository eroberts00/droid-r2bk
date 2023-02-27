from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Timestamp(_message.Message):
    __slots__ = ["nanos", "seconds"]
    NANOS_FIELD_NUMBER: ClassVar[int]
    SECONDS_FIELD_NUMBER: ClassVar[int]
    nanos: int
    seconds: int
    def __init__(self, seconds: Optional[int] = ..., nanos: Optional[int] = ...) -> None: ...