# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/ocmshareprovider/v0alpha/resources.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.storageprovider.v0alpha import resources_pb2 as cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2
from cs3.types import types_pb2 as cs3_dot_types_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cs3/ocmshareprovider/v0alpha/resources.proto',
  package='cs3.ocmshareproviderv0alpha',
  syntax='proto3',
  serialized_options=_b('\n\037com.cs3.ocmshareproviderv0alphaB\016ResourcesProtoP\001Z\031ocmshareproviderv0alphapb\242\002\024CBOXocmshareprovider\252\002\033CS3.ocmshareproviderV0Alpha\312\002\033CS3\\ocmshareproviderV0Alpha'),
  serialized_pb=_b('\n,cs3/ocmshareprovider/v0alpha/resources.proto\x12\x1b\x63s3.ocmshareproviderv0alpha\x1a+cs3/storageprovider/v0alpha/resources.proto\x1a\x15\x63s3/types/types.proto\"\x80\x03\n\x05Share\x12\x30\n\x02id\x18\x01 \x01(\x0b\x32$.cs3.ocmshareproviderv0alpha.ShareId\x12;\n\x0bresource_id\x18\x02 \x01(\x0b\x32&.cs3.storageproviderv0alpha.ResourceId\x12\x42\n\x0bpermissions\x18\x03 \x01(\x0b\x32-.cs3.ocmshareproviderv0alpha.SharePermissions\x12\x34\n\x07grantee\x18\x04 \x01(\x0b\x32#.cs3.storageproviderv0alpha.Grantee\x12 \n\x05owner\x18\x05 \x01(\x0b\x32\x11.cs3.types.UserId\x12\"\n\x07\x63reator\x18\x06 \x01(\x0b\x32\x11.cs3.types.UserId\x12#\n\x05\x63time\x18\x07 \x01(\x0b\x32\x14.cs3.types.Timestamp\x12#\n\x05mtime\x18\x08 \x01(\x0b\x32\x14.cs3.types.Timestamp\"i\n\x10SharePermissions\x12\x44\n\x0bpermissions\x18\x01 \x01(\x0b\x32/.cs3.storageproviderv0alpha.ResourcePermissions\x12\x0f\n\x07reshare\x18\x02 \x01(\x08\"z\n\rReceivedShare\x12\x31\n\x05share\x18\x01 \x01(\x0b\x32\".cs3.ocmshareproviderv0alpha.Share\x12\x36\n\x05state\x18\x02 \x01(\x0e\x32\'.cs3.ocmshareproviderv0alpha.ShareState\"\x9f\x01\n\x08ShareKey\x12 \n\x05owner\x18\x02 \x01(\x0b\x32\x11.cs3.types.UserId\x12;\n\x0bresource_id\x18\x03 \x01(\x0b\x32&.cs3.storageproviderv0alpha.ResourceId\x12\x34\n\x07grantee\x18\x04 \x01(\x0b\x32#.cs3.storageproviderv0alpha.Grantee\"\x1c\n\x07ShareId\x12\x11\n\topaque_id\x18\x02 \x01(\t\"\x82\x01\n\x0eShareReference\x12\x32\n\x02id\x18\x01 \x01(\x0b\x32$.cs3.ocmshareproviderv0alpha.ShareIdH\x00\x12\x34\n\x03key\x18\x02 \x01(\x0b\x32%.cs3.ocmshareproviderv0alpha.ShareKeyH\x00\x42\x06\n\x04spec\"\x86\x01\n\nShareGrant\x12\x34\n\x07grantee\x18\x01 \x01(\x0b\x32#.cs3.storageproviderv0alpha.Grantee\x12\x42\n\x0bpermissions\x18\x02 \x01(\x0b\x32-.cs3.ocmshareproviderv0alpha.SharePermissions*r\n\nShareState\x12\x17\n\x13SHARE_STATE_INVALID\x10\x00\x12\x17\n\x13SHARE_STATE_PENDING\x10\x01\x12\x18\n\x14SHARE_STATE_ACCEPTED\x10\x02\x12\x18\n\x14SHARE_STATE_REJECTED\x10\x03\x42\xa1\x01\n\x1f\x63om.cs3.ocmshareproviderv0alphaB\x0eResourcesProtoP\x01Z\x19ocmshareproviderv0alphapb\xa2\x02\x14\x43\x42OXocmshareprovider\xaa\x02\x1b\x43S3.ocmshareproviderV0Alpha\xca\x02\x1b\x43S3\\ocmshareproviderV0Alphab\x06proto3')
  ,
  dependencies=[cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2.DESCRIPTOR,cs3_dot_types_dot_types__pb2.DESCRIPTOR,])

_SHARESTATE = _descriptor.EnumDescriptor(
  name='ShareState',
  full_name='cs3.ocmshareproviderv0alpha.ShareState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SHARE_STATE_INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHARE_STATE_PENDING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHARE_STATE_ACCEPTED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHARE_STATE_REJECTED', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1225,
  serialized_end=1339,
)
_sym_db.RegisterEnumDescriptor(_SHARESTATE)

ShareState = enum_type_wrapper.EnumTypeWrapper(_SHARESTATE)
SHARE_STATE_INVALID = 0
SHARE_STATE_PENDING = 1
SHARE_STATE_ACCEPTED = 2
SHARE_STATE_REJECTED = 3



_SHARE = _descriptor.Descriptor(
  name='Share',
  full_name='cs3.ocmshareproviderv0alpha.Share',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cs3.ocmshareproviderv0alpha.Share.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='cs3.ocmshareproviderv0alpha.Share.resource_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='cs3.ocmshareproviderv0alpha.Share.permissions', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cs3.ocmshareproviderv0alpha.Share.grantee', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner', full_name='cs3.ocmshareproviderv0alpha.Share.owner', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='cs3.ocmshareproviderv0alpha.Share.creator', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ctime', full_name='cs3.ocmshareproviderv0alpha.Share.ctime', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtime', full_name='cs3.ocmshareproviderv0alpha.Share.mtime', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=146,
  serialized_end=530,
)


_SHAREPERMISSIONS = _descriptor.Descriptor(
  name='SharePermissions',
  full_name='cs3.ocmshareproviderv0alpha.SharePermissions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='permissions', full_name='cs3.ocmshareproviderv0alpha.SharePermissions.permissions', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reshare', full_name='cs3.ocmshareproviderv0alpha.SharePermissions.reshare', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=532,
  serialized_end=637,
)


_RECEIVEDSHARE = _descriptor.Descriptor(
  name='ReceivedShare',
  full_name='cs3.ocmshareproviderv0alpha.ReceivedShare',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='share', full_name='cs3.ocmshareproviderv0alpha.ReceivedShare.share', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='cs3.ocmshareproviderv0alpha.ReceivedShare.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=639,
  serialized_end=761,
)


_SHAREKEY = _descriptor.Descriptor(
  name='ShareKey',
  full_name='cs3.ocmshareproviderv0alpha.ShareKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='cs3.ocmshareproviderv0alpha.ShareKey.owner', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='cs3.ocmshareproviderv0alpha.ShareKey.resource_id', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cs3.ocmshareproviderv0alpha.ShareKey.grantee', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=764,
  serialized_end=923,
)


_SHAREID = _descriptor.Descriptor(
  name='ShareId',
  full_name='cs3.ocmshareproviderv0alpha.ShareId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque_id', full_name='cs3.ocmshareproviderv0alpha.ShareId.opaque_id', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=925,
  serialized_end=953,
)


_SHAREREFERENCE = _descriptor.Descriptor(
  name='ShareReference',
  full_name='cs3.ocmshareproviderv0alpha.ShareReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='cs3.ocmshareproviderv0alpha.ShareReference.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='cs3.ocmshareproviderv0alpha.ShareReference.key', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='spec', full_name='cs3.ocmshareproviderv0alpha.ShareReference.spec',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=956,
  serialized_end=1086,
)


_SHAREGRANT = _descriptor.Descriptor(
  name='ShareGrant',
  full_name='cs3.ocmshareproviderv0alpha.ShareGrant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='grantee', full_name='cs3.ocmshareproviderv0alpha.ShareGrant.grantee', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='cs3.ocmshareproviderv0alpha.ShareGrant.permissions', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1089,
  serialized_end=1223,
)

_SHARE.fields_by_name['id'].message_type = _SHAREID
_SHARE.fields_by_name['resource_id'].message_type = cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2._RESOURCEID
_SHARE.fields_by_name['permissions'].message_type = _SHAREPERMISSIONS
_SHARE.fields_by_name['grantee'].message_type = cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2._GRANTEE
_SHARE.fields_by_name['owner'].message_type = cs3_dot_types_dot_types__pb2._USERID
_SHARE.fields_by_name['creator'].message_type = cs3_dot_types_dot_types__pb2._USERID
_SHARE.fields_by_name['ctime'].message_type = cs3_dot_types_dot_types__pb2._TIMESTAMP
_SHARE.fields_by_name['mtime'].message_type = cs3_dot_types_dot_types__pb2._TIMESTAMP
_SHAREPERMISSIONS.fields_by_name['permissions'].message_type = cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2._RESOURCEPERMISSIONS
_RECEIVEDSHARE.fields_by_name['share'].message_type = _SHARE
_RECEIVEDSHARE.fields_by_name['state'].enum_type = _SHARESTATE
_SHAREKEY.fields_by_name['owner'].message_type = cs3_dot_types_dot_types__pb2._USERID
_SHAREKEY.fields_by_name['resource_id'].message_type = cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2._RESOURCEID
_SHAREKEY.fields_by_name['grantee'].message_type = cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2._GRANTEE
_SHAREREFERENCE.fields_by_name['id'].message_type = _SHAREID
_SHAREREFERENCE.fields_by_name['key'].message_type = _SHAREKEY
_SHAREREFERENCE.oneofs_by_name['spec'].fields.append(
  _SHAREREFERENCE.fields_by_name['id'])
_SHAREREFERENCE.fields_by_name['id'].containing_oneof = _SHAREREFERENCE.oneofs_by_name['spec']
_SHAREREFERENCE.oneofs_by_name['spec'].fields.append(
  _SHAREREFERENCE.fields_by_name['key'])
_SHAREREFERENCE.fields_by_name['key'].containing_oneof = _SHAREREFERENCE.oneofs_by_name['spec']
_SHAREGRANT.fields_by_name['grantee'].message_type = cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2._GRANTEE
_SHAREGRANT.fields_by_name['permissions'].message_type = _SHAREPERMISSIONS
DESCRIPTOR.message_types_by_name['Share'] = _SHARE
DESCRIPTOR.message_types_by_name['SharePermissions'] = _SHAREPERMISSIONS
DESCRIPTOR.message_types_by_name['ReceivedShare'] = _RECEIVEDSHARE
DESCRIPTOR.message_types_by_name['ShareKey'] = _SHAREKEY
DESCRIPTOR.message_types_by_name['ShareId'] = _SHAREID
DESCRIPTOR.message_types_by_name['ShareReference'] = _SHAREREFERENCE
DESCRIPTOR.message_types_by_name['ShareGrant'] = _SHAREGRANT
DESCRIPTOR.enum_types_by_name['ShareState'] = _SHARESTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Share = _reflection.GeneratedProtocolMessageType('Share', (_message.Message,), {
  'DESCRIPTOR' : _SHARE,
  '__module__' : 'cs3.ocmshareprovider.v0alpha.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.ocmshareproviderv0alpha.Share)
  })
_sym_db.RegisterMessage(Share)

SharePermissions = _reflection.GeneratedProtocolMessageType('SharePermissions', (_message.Message,), {
  'DESCRIPTOR' : _SHAREPERMISSIONS,
  '__module__' : 'cs3.ocmshareprovider.v0alpha.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.ocmshareproviderv0alpha.SharePermissions)
  })
_sym_db.RegisterMessage(SharePermissions)

ReceivedShare = _reflection.GeneratedProtocolMessageType('ReceivedShare', (_message.Message,), {
  'DESCRIPTOR' : _RECEIVEDSHARE,
  '__module__' : 'cs3.ocmshareprovider.v0alpha.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.ocmshareproviderv0alpha.ReceivedShare)
  })
_sym_db.RegisterMessage(ReceivedShare)

ShareKey = _reflection.GeneratedProtocolMessageType('ShareKey', (_message.Message,), {
  'DESCRIPTOR' : _SHAREKEY,
  '__module__' : 'cs3.ocmshareprovider.v0alpha.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.ocmshareproviderv0alpha.ShareKey)
  })
_sym_db.RegisterMessage(ShareKey)

ShareId = _reflection.GeneratedProtocolMessageType('ShareId', (_message.Message,), {
  'DESCRIPTOR' : _SHAREID,
  '__module__' : 'cs3.ocmshareprovider.v0alpha.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.ocmshareproviderv0alpha.ShareId)
  })
_sym_db.RegisterMessage(ShareId)

ShareReference = _reflection.GeneratedProtocolMessageType('ShareReference', (_message.Message,), {
  'DESCRIPTOR' : _SHAREREFERENCE,
  '__module__' : 'cs3.ocmshareprovider.v0alpha.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.ocmshareproviderv0alpha.ShareReference)
  })
_sym_db.RegisterMessage(ShareReference)

ShareGrant = _reflection.GeneratedProtocolMessageType('ShareGrant', (_message.Message,), {
  'DESCRIPTOR' : _SHAREGRANT,
  '__module__' : 'cs3.ocmshareprovider.v0alpha.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.ocmshareproviderv0alpha.ShareGrant)
  })
_sym_db.RegisterMessage(ShareGrant)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
