# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/sharing/ocm/v1beta1/resources.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.app.provider.v1beta1 import resources_pb2 as cs3_dot_app_dot_provider_dot_v1beta1_dot_resources__pb2
from cs3.identity.user.v1beta1 import resources_pb2 as cs3_dot_identity_dot_user_dot_v1beta1_dot_resources__pb2
from cs3.storage.provider.v1beta1 import resources_pb2 as cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2
from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'cs3/sharing/ocm/v1beta1/resources.proto\x12\x17\x63s3.sharing.ocm.v1beta1\x1a(cs3/app/provider/v1beta1/resources.proto\x1a)cs3/identity/user/v1beta1/resources.proto\x1a,cs3/storage/provider/v1beta1/resources.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\"\xdd\x04\n\x05Share\x12,\n\x02id\x18\x01 \x01(\x0b\x32 .cs3.sharing.ocm.v1beta1.ShareId\x12=\n\x0bresource_id\x18\x02 \x01(\x0b\x32(.cs3.storage.provider.v1beta1.ResourceId\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05token\x18\x04 \x01(\t\x12\x36\n\x07grantee\x18\x05 \x01(\x0b\x32%.cs3.storage.provider.v1beta1.Grantee\x12\x30\n\x05owner\x18\x06 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserId\x12\x32\n\x07\x63reator\x18\x07 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserId\x12+\n\x05\x63time\x18\x08 \x01(\x0b\x32\x1c.cs3.types.v1beta1.Timestamp\x12+\n\x05mtime\x18\t \x01(\x0b\x32\x1c.cs3.types.v1beta1.Timestamp\x12\x30\n\nexpiration\x18\n \x01(\x0b\x32\x1c.cs3.types.v1beta1.Timestamp\x12\x36\n\nshare_type\x18\x0b \x01(\x0e\x32\".cs3.sharing.ocm.v1beta1.ShareType\x12=\n\x0e\x61\x63\x63\x65ss_methods\x18\x0c \x03(\x0b\x32%.cs3.sharing.ocm.v1beta1.AccessMethod\x12)\n\x06opaque\x18\r \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\"k\n\x10SharePermissions\x12\x46\n\x0bpermissions\x18\x01 \x01(\x0b\x32\x31.cs3.storage.provider.v1beta1.ResourcePermissions\x12\x0f\n\x07reshare\x18\x02 \x01(\x08\"\x81\x05\n\rReceivedShare\x12,\n\x02id\x18\x01 \x01(\x0b\x32 .cs3.sharing.ocm.v1beta1.ShareId\x12\x0c\n\x04name\x18\x02 \x01(\t\x12=\n\x0bresource_id\x18\x03 \x01(\x0b\x32(.cs3.storage.provider.v1beta1.ResourceId\x12\x36\n\x07grantee\x18\x04 \x01(\x0b\x32%.cs3.storage.provider.v1beta1.Grantee\x12\x30\n\x05owner\x18\x05 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserId\x12\x32\n\x07\x63reator\x18\x06 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserId\x12+\n\x05\x63time\x18\x07 \x01(\x0b\x32\x1c.cs3.types.v1beta1.Timestamp\x12+\n\x05mtime\x18\x08 \x01(\x0b\x32\x1c.cs3.types.v1beta1.Timestamp\x12\x30\n\nexpiration\x18\t \x01(\x0b\x32\x1c.cs3.types.v1beta1.Timestamp\x12\x36\n\nshare_type\x18\n \x01(\x0e\x32\".cs3.sharing.ocm.v1beta1.ShareType\x12\x34\n\tprotocols\x18\x0b \x03(\x0b\x32!.cs3.sharing.ocm.v1beta1.Protocol\x12\x32\n\x05state\x18\x0c \x01(\x0e\x32#.cs3.sharing.ocm.v1beta1.ShareState\x12)\n\x06opaque\x18\r \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\"\xb3\x01\n\x08ShareKey\x12\x30\n\x05owner\x18\x01 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserId\x12=\n\x0bresource_id\x18\x02 \x01(\x0b\x32(.cs3.storage.provider.v1beta1.ResourceId\x12\x36\n\x07grantee\x18\x03 \x01(\x0b\x32%.cs3.storage.provider.v1beta1.Grantee\"\x1c\n\x07ShareId\x12\x11\n\topaque_id\x18\x01 \x01(\t\"z\n\x0eShareReference\x12.\n\x02id\x18\x01 \x01(\x0b\x32 .cs3.sharing.ocm.v1beta1.ShareIdH\x00\x12\x30\n\x03key\x18\x02 \x01(\x0b\x32!.cs3.sharing.ocm.v1beta1.ShareKeyH\x00\x42\x06\n\x04spec\"\x84\x01\n\nShareGrant\x12\x36\n\x07grantee\x18\x01 \x01(\x0b\x32%.cs3.storage.provider.v1beta1.Grantee\x12>\n\x0bpermissions\x18\x02 \x01(\x0b\x32).cs3.sharing.ocm.v1beta1.SharePermissions\"\x95\x02\n\x08Protocol\x12\x41\n\x0ewebdav_options\x18\x01 \x01(\x0b\x32\'.cs3.sharing.ocm.v1beta1.WebDAVProtocolH\x00\x12\x41\n\x0ewebapp_options\x18\x02 \x01(\x0b\x32\'.cs3.sharing.ocm.v1beta1.WebappProtocolH\x00\x12\x45\n\x10transfer_options\x18\x03 \x01(\x0b\x32).cs3.sharing.ocm.v1beta1.TransferProtocolH\x00\x12\x34\n\x0fgeneric_options\x18\x04 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueH\x00\x42\x06\n\x04term\"t\n\x0eWebDAVProtocol\x12\x15\n\rshared_secret\x18\x01 \x01(\t\x12>\n\x0bpermissions\x18\x02 \x01(\x0b\x32).cs3.sharing.ocm.v1beta1.SharePermissions\x12\x0b\n\x03uri\x18\x03 \x01(\t\"&\n\x0eWebappProtocol\x12\x14\n\x0curi_template\x18\x01 \x01(\t\"K\n\x10TransferProtocol\x12\x15\n\rshared_secret\x18\x01 \x01(\t\x12\x12\n\nsource_uri\x18\x02 \x01(\t\x12\x0c\n\x04size\x18\x03 \x01(\x04\"\xa5\x02\n\x0c\x41\x63\x63\x65ssMethod\x12\x45\n\x0ewebdav_options\x18\x01 \x01(\x0b\x32+.cs3.sharing.ocm.v1beta1.WebDAVAccessMethodH\x00\x12\x45\n\x0ewebapp_options\x18\x02 \x01(\x0b\x32+.cs3.sharing.ocm.v1beta1.WebappAccessMethodH\x00\x12I\n\x10transfer_options\x18\x03 \x01(\x0b\x32-.cs3.sharing.ocm.v1beta1.TransferAccessMethodH\x00\x12\x34\n\x0fgeneric_options\x18\x04 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueH\x00\x42\x06\n\x04term\"\\\n\x12WebDAVAccessMethod\x12\x46\n\x0bpermissions\x18\x02 \x01(\x0b\x32\x31.cs3.storage.provider.v1beta1.ResourcePermissions\"K\n\x12WebappAccessMethod\x12\x35\n\tview_mode\x18\x02 \x01(\x0e\x32\".cs3.app.provider.v1beta1.ViewMode\"\x16\n\x14TransferAccessMethod*r\n\nShareState\x12\x17\n\x13SHARE_STATE_INVALID\x10\x00\x12\x17\n\x13SHARE_STATE_PENDING\x10\x01\x12\x18\n\x14SHARE_STATE_ACCEPTED\x10\x02\x12\x18\n\x14SHARE_STATE_REJECTED\x10\x03*N\n\tShareType\x12\x16\n\x12SHARE_TYPE_INVALID\x10\x00\x12\x13\n\x0fSHARE_TYPE_USER\x10\x01\x12\x14\n\x10SHARE_TYPE_GROUP\x10\x02\x42u\n\x1b\x63om.cs3.sharing.ocm.v1beta1B\x0eResourcesProtoP\x01Z\nocmv1beta1\xa2\x02\x03\x43SO\xaa\x02\x17\x43s3.Sharing.Ocm.V1Beta1\xca\x02\x17\x43s3\\Sharing\\Ocm\\V1Beta1b\x06proto3')

_SHARESTATE = DESCRIPTOR.enum_types_by_name['ShareState']
ShareState = enum_type_wrapper.EnumTypeWrapper(_SHARESTATE)
_SHARETYPE = DESCRIPTOR.enum_types_by_name['ShareType']
ShareType = enum_type_wrapper.EnumTypeWrapper(_SHARETYPE)
SHARE_STATE_INVALID = 0
SHARE_STATE_PENDING = 1
SHARE_STATE_ACCEPTED = 2
SHARE_STATE_REJECTED = 3
SHARE_TYPE_INVALID = 0
SHARE_TYPE_USER = 1
SHARE_TYPE_GROUP = 2


_SHARE = DESCRIPTOR.message_types_by_name['Share']
_SHAREPERMISSIONS = DESCRIPTOR.message_types_by_name['SharePermissions']
_RECEIVEDSHARE = DESCRIPTOR.message_types_by_name['ReceivedShare']
_SHAREKEY = DESCRIPTOR.message_types_by_name['ShareKey']
_SHAREID = DESCRIPTOR.message_types_by_name['ShareId']
_SHAREREFERENCE = DESCRIPTOR.message_types_by_name['ShareReference']
_SHAREGRANT = DESCRIPTOR.message_types_by_name['ShareGrant']
_PROTOCOL = DESCRIPTOR.message_types_by_name['Protocol']
_WEBDAVPROTOCOL = DESCRIPTOR.message_types_by_name['WebDAVProtocol']
_WEBAPPPROTOCOL = DESCRIPTOR.message_types_by_name['WebappProtocol']
_TRANSFERPROTOCOL = DESCRIPTOR.message_types_by_name['TransferProtocol']
_ACCESSMETHOD = DESCRIPTOR.message_types_by_name['AccessMethod']
_WEBDAVACCESSMETHOD = DESCRIPTOR.message_types_by_name['WebDAVAccessMethod']
_WEBAPPACCESSMETHOD = DESCRIPTOR.message_types_by_name['WebappAccessMethod']
_TRANSFERACCESSMETHOD = DESCRIPTOR.message_types_by_name['TransferAccessMethod']
Share = _reflection.GeneratedProtocolMessageType('Share', (_message.Message,), {
  'DESCRIPTOR' : _SHARE,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.Share)
  })
_sym_db.RegisterMessage(Share)

SharePermissions = _reflection.GeneratedProtocolMessageType('SharePermissions', (_message.Message,), {
  'DESCRIPTOR' : _SHAREPERMISSIONS,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.SharePermissions)
  })
_sym_db.RegisterMessage(SharePermissions)

ReceivedShare = _reflection.GeneratedProtocolMessageType('ReceivedShare', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVEDSHARE,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.ReceivedShare)
  })
_sym_db.RegisterMessage(ReceivedShare)

ShareKey = _reflection.GeneratedProtocolMessageType('ShareKey', (_message.Message,), {
  'DESCRIPTOR' : _SHAREKEY,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.ShareKey)
  })
_sym_db.RegisterMessage(ShareKey)

ShareId = _reflection.GeneratedProtocolMessageType('ShareId', (_message.Message,), {
  'DESCRIPTOR' : _SHAREID,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.ShareId)
  })
_sym_db.RegisterMessage(ShareId)

ShareReference = _reflection.GeneratedProtocolMessageType('ShareReference', (_message.Message,), {
  'DESCRIPTOR' : _SHAREREFERENCE,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.ShareReference)
  })
_sym_db.RegisterMessage(ShareReference)

ShareGrant = _reflection.GeneratedProtocolMessageType('ShareGrant', (_message.Message,), {
  'DESCRIPTOR' : _SHAREGRANT,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.ShareGrant)
  })
_sym_db.RegisterMessage(ShareGrant)

Protocol = _reflection.GeneratedProtocolMessageType('Protocol', (_message.Message,), {
  'DESCRIPTOR' : _PROTOCOL,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.Protocol)
  })
_sym_db.RegisterMessage(Protocol)

WebDAVProtocol = _reflection.GeneratedProtocolMessageType('WebDAVProtocol', (_message.Message,), {
  'DESCRIPTOR' : _WEBDAVPROTOCOL,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.WebDAVProtocol)
  })
_sym_db.RegisterMessage(WebDAVProtocol)

WebappProtocol = _reflection.GeneratedProtocolMessageType('WebappProtocol', (_message.Message,), {
  'DESCRIPTOR' : _WEBAPPPROTOCOL,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.WebappProtocol)
  })
_sym_db.RegisterMessage(WebappProtocol)

TransferProtocol = _reflection.GeneratedProtocolMessageType('TransferProtocol', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERPROTOCOL,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.TransferProtocol)
  })
_sym_db.RegisterMessage(TransferProtocol)

AccessMethod = _reflection.GeneratedProtocolMessageType('AccessMethod', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSMETHOD,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.AccessMethod)
  })
_sym_db.RegisterMessage(AccessMethod)

WebDAVAccessMethod = _reflection.GeneratedProtocolMessageType('WebDAVAccessMethod', (_message.Message,), {
  'DESCRIPTOR' : _WEBDAVACCESSMETHOD,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.WebDAVAccessMethod)
  })
_sym_db.RegisterMessage(WebDAVAccessMethod)

WebappAccessMethod = _reflection.GeneratedProtocolMessageType('WebappAccessMethod', (_message.Message,), {
  'DESCRIPTOR' : _WEBAPPACCESSMETHOD,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.WebappAccessMethod)
  })
_sym_db.RegisterMessage(WebappAccessMethod)

TransferAccessMethod = _reflection.GeneratedProtocolMessageType('TransferAccessMethod', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFERACCESSMETHOD,
  '__module__' : 'cs3.sharing.ocm.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.ocm.v1beta1.TransferAccessMethod)
  })
_sym_db.RegisterMessage(TransferAccessMethod)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.cs3.sharing.ocm.v1beta1B\016ResourcesProtoP\001Z\nocmv1beta1\242\002\003CSO\252\002\027Cs3.Sharing.Ocm.V1Beta1\312\002\027Cs3\\Sharing\\Ocm\\V1Beta1'
  _SHARESTATE._serialized_start=3068
  _SHARESTATE._serialized_end=3182
  _SHARETYPE._serialized_start=3184
  _SHARETYPE._serialized_end=3262
  _SHARE._serialized_start=231
  _SHARE._serialized_end=836
  _SHAREPERMISSIONS._serialized_start=838
  _SHAREPERMISSIONS._serialized_end=945
  _RECEIVEDSHARE._serialized_start=948
  _RECEIVEDSHARE._serialized_end=1589
  _SHAREKEY._serialized_start=1592
  _SHAREKEY._serialized_end=1771
  _SHAREID._serialized_start=1773
  _SHAREID._serialized_end=1801
  _SHAREREFERENCE._serialized_start=1803
  _SHAREREFERENCE._serialized_end=1925
  _SHAREGRANT._serialized_start=1928
  _SHAREGRANT._serialized_end=2060
  _PROTOCOL._serialized_start=2063
  _PROTOCOL._serialized_end=2340
  _WEBDAVPROTOCOL._serialized_start=2342
  _WEBDAVPROTOCOL._serialized_end=2458
  _WEBAPPPROTOCOL._serialized_start=2460
  _WEBAPPPROTOCOL._serialized_end=2498
  _TRANSFERPROTOCOL._serialized_start=2500
  _TRANSFERPROTOCOL._serialized_end=2575
  _ACCESSMETHOD._serialized_start=2578
  _ACCESSMETHOD._serialized_end=2871
  _WEBDAVACCESSMETHOD._serialized_start=2873
  _WEBDAVACCESSMETHOD._serialized_end=2965
  _WEBAPPACCESSMETHOD._serialized_start=2967
  _WEBAPPACCESSMETHOD._serialized_end=3042
  _TRANSFERACCESSMETHOD._serialized_start=3044
  _TRANSFERACCESSMETHOD._serialized_end=3066
# @@protoc_insertion_point(module_scope)
