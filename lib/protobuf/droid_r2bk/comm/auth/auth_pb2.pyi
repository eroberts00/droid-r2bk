from lib.protobuf.droid_r2bk.comm.types import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor
MODIFY_ALL: AccessType
NONE: AccessType
QUERY_ALL: AccessType

class AuthorizationRequest(_message.Message):
    __slots__ = ["access_requests", "requestor_credentials", "requestor_identity"]
    ACCESS_REQUESTS_FIELD_NUMBER: ClassVar[int]
    REQUESTOR_CREDENTIALS_FIELD_NUMBER: ClassVar[int]
    REQUESTOR_IDENTITY_FIELD_NUMBER: ClassVar[int]
    access_requests: _containers.RepeatedScalarFieldContainer[AccessType]
    requestor_credentials: bytes
    requestor_identity: bytes
    def __init__(self, requestor_identity: Optional[bytes] = ..., requestor_credentials: Optional[bytes] = ..., access_requests: Optional[Iterable[Union[AccessType, str]]] = ...) -> None: ...

class AuthorizationResponse(_message.Message):
    __slots__ = ["error_message", "success", "token"]
    ERROR_MESSAGE_FIELD_NUMBER: ClassVar[int]
    SUCCESS_FIELD_NUMBER: ClassVar[int]
    TOKEN_FIELD_NUMBER: ClassVar[int]
    error_message: str
    success: bool
    token: AuthorizationToken
    def __init__(self, success: bool = ..., error_message: Optional[str] = ..., token: Optional[Union[AuthorizationToken, Mapping]] = ...) -> None: ...

class AuthorizationToken(_message.Message):
    __slots__ = ["authorization_token", "expiration_time"]
    AUTHORIZATION_TOKEN_FIELD_NUMBER: ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: ClassVar[int]
    authorization_token: bytes
    expiration_time: _types_pb2.Timestamp
    def __init__(self, authorization_token: Optional[bytes] = ..., expiration_time: Optional[Union[_types_pb2.Timestamp, Mapping]] = ...) -> None: ...

class AccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
