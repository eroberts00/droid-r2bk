from lib.protobuf.droid_r2bk.comm.types import types_pb2 as _types_pb2
from lib.protobuf.droid_r2bk.comm.auth import auth_pb2 as _auth_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor
MODIFY_ALL: Status
NONE: Status
QUERY_ALL: Status

class GetInfoRequest(_message.Message):
    __slots__ = ["authorization"]
    AUTHORIZATION_FIELD_NUMBER: ClassVar[int]
    authorization: _auth_pb2.AuthorizationToken
    def __init__(self, authorization: Optional[Union[_auth_pb2.AuthorizationToken, Mapping]] = ...) -> None: ...

class GetInfoResponse(_message.Message):
    __slots__ = ["mfg", "model", "name", "protocol_major_version", "protocol_minor_version", "responder_identity", "time", "type"]
    MFG_FIELD_NUMBER: ClassVar[int]
    MODEL_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    PROTOCOL_MAJOR_VERSION_FIELD_NUMBER: ClassVar[int]
    PROTOCOL_MINOR_VERSION_FIELD_NUMBER: ClassVar[int]
    RESPONDER_IDENTITY_FIELD_NUMBER: ClassVar[int]
    TIME_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    mfg: int
    model: int
    name: str
    protocol_major_version: int
    protocol_minor_version: int
    responder_identity: bytes
    time: _types_pb2.Timestamp
    type: int
    def __init__(self, time: Optional[Union[_types_pb2.Timestamp, Mapping]] = ..., type: Optional[int] = ..., mfg: Optional[int] = ..., model: Optional[int] = ..., protocol_major_version: Optional[int] = ..., protocol_minor_version: Optional[int] = ..., responder_identity: Optional[bytes] = ..., name: Optional[str] = ...) -> None: ...

class GetStatusRequest(_message.Message):
    __slots__ = ["authorization"]
    AUTHORIZATION_FIELD_NUMBER: ClassVar[int]
    authorization: _auth_pb2.AuthorizationToken
    def __init__(self, authorization: Optional[Union[_auth_pb2.AuthorizationToken, Mapping]] = ...) -> None: ...

class GetStatusResponse(_message.Message):
    __slots__ = ["status", "time"]
    STATUS_FIELD_NUMBER: ClassVar[int]
    TIME_FIELD_NUMBER: ClassVar[int]
    status: Status
    time: _types_pb2.Timestamp
    def __init__(self, time: Optional[Union[_types_pb2.Timestamp, Mapping]] = ..., status: Optional[Union[Status, str]] = ...) -> None: ...

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
