from lib.protobuf.droid_r2bk.comm.types import types_pb2 as _types_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class DiscoveryRequest(_message.Message):
    __slots__ = ["discover_major_version", "discover_mfg", "discover_model", "discover_type", "discover_uuid", "request_time", "requestor_address", "requestor_identity", "requestor_major_version", "requestor_mfg", "requestor_minor_version", "requestor_model", "requestor_port", "requestor_type", "requestor_verification"]
    DISCOVER_MAJOR_VERSION_FIELD_NUMBER: ClassVar[int]
    DISCOVER_MFG_FIELD_NUMBER: ClassVar[int]
    DISCOVER_MODEL_FIELD_NUMBER: ClassVar[int]
    DISCOVER_TYPE_FIELD_NUMBER: ClassVar[int]
    DISCOVER_UUID_FIELD_NUMBER: ClassVar[int]
    REQUESTOR_ADDRESS_FIELD_NUMBER: ClassVar[int]
    REQUESTOR_IDENTITY_FIELD_NUMBER: ClassVar[int]
    REQUESTOR_MAJOR_VERSION_FIELD_NUMBER: ClassVar[int]
    REQUESTOR_MFG_FIELD_NUMBER: ClassVar[int]
    REQUESTOR_MINOR_VERSION_FIELD_NUMBER: ClassVar[int]
    REQUESTOR_MODEL_FIELD_NUMBER: ClassVar[int]
    REQUESTOR_PORT_FIELD_NUMBER: ClassVar[int]
    REQUESTOR_TYPE_FIELD_NUMBER: ClassVar[int]
    REQUESTOR_VERIFICATION_FIELD_NUMBER: ClassVar[int]
    REQUEST_TIME_FIELD_NUMBER: ClassVar[int]
    discover_major_version: int
    discover_mfg: int
    discover_model: int
    discover_type: int
    discover_uuid: bytes
    request_time: _types_pb2.Timestamp
    requestor_address: int
    requestor_identity: bytes
    requestor_major_version: int
    requestor_mfg: int
    requestor_minor_version: int
    requestor_model: int
    requestor_port: int
    requestor_type: int
    requestor_verification: bytes
    def __init__(self, requestor_type: Optional[int] = ..., requestor_mfg: Optional[int] = ..., requestor_model: Optional[int] = ..., requestor_address: Optional[int] = ..., requestor_port: Optional[int] = ..., requestor_identity: Optional[bytes] = ..., requestor_verification: Optional[bytes] = ..., requestor_major_version: Optional[int] = ..., requestor_minor_version: Optional[int] = ..., discover_type: Optional[int] = ..., discover_mfg: Optional[int] = ..., discover_model: Optional[int] = ..., discover_uuid: Optional[bytes] = ..., discover_major_version: Optional[int] = ..., request_time: Optional[Union[_types_pb2.Timestamp, Mapping]] = ...) -> None: ...

class DiscoveryResponse(_message.Message):
    __slots__ = ["request_time", "responder_address", "responder_identity", "responder_major_version", "responder_mfg", "responder_minor_version", "responder_model", "responder_port", "responder_type", "responder_verification", "response_time"]
    REQUEST_TIME_FIELD_NUMBER: ClassVar[int]
    RESPONDER_ADDRESS_FIELD_NUMBER: ClassVar[int]
    RESPONDER_IDENTITY_FIELD_NUMBER: ClassVar[int]
    RESPONDER_MAJOR_VERSION_FIELD_NUMBER: ClassVar[int]
    RESPONDER_MFG_FIELD_NUMBER: ClassVar[int]
    RESPONDER_MINOR_VERSION_FIELD_NUMBER: ClassVar[int]
    RESPONDER_MODEL_FIELD_NUMBER: ClassVar[int]
    RESPONDER_PORT_FIELD_NUMBER: ClassVar[int]
    RESPONDER_TYPE_FIELD_NUMBER: ClassVar[int]
    RESPONDER_VERIFICATION_FIELD_NUMBER: ClassVar[int]
    RESPONSE_TIME_FIELD_NUMBER: ClassVar[int]
    request_time: _types_pb2.Timestamp
    responder_address: int
    responder_identity: bytes
    responder_major_version: int
    responder_mfg: int
    responder_minor_version: int
    responder_model: int
    responder_port: int
    responder_type: int
    responder_verification: bytes
    response_time: _types_pb2.Timestamp
    def __init__(self, responder_type: Optional[int] = ..., responder_mfg: Optional[int] = ..., responder_model: Optional[int] = ..., responder_address: Optional[int] = ..., responder_port: Optional[int] = ..., responder_major_version: Optional[int] = ..., responder_minor_version: Optional[int] = ..., responder_identity: Optional[bytes] = ..., responder_verification: Optional[bytes] = ..., request_time: Optional[Union[_types_pb2.Timestamp, Mapping]] = ..., response_time: Optional[Union[_types_pb2.Timestamp, Mapping]] = ...) -> None: ...
