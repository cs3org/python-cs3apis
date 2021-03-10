# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/ocm/invite/v1beta1/resources.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.identity.user.v1beta1 import resources_pb2 as cs3_dot_identity_dot_user_dot_v1beta1_dot_resources__pb2
from cs3.storage.provider.v1beta1 import resources_pb2 as cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2
from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cs3/ocm/invite/v1beta1/resources.proto',
  package='cs3.ocm.invite.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\032com.cs3.ocm.invite.v1beta1B\016ResourcesProtoP\001Z\rinvitev1beta1\242\002\003COI\252\002\026Cs3.Ocm.Invite.V1Beta1\312\002\026Cs3\\Ocm\\Invite\\V1Beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&cs3/ocm/invite/v1beta1/resources.proto\x12\x16\x63s3.ocm.invite.v1beta1\x1a)cs3/identity/user/v1beta1/resources.proto\x1a,cs3/storage/provider/v1beta1/resources.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\"\x97\x01\n\x0bInviteToken\x12\r\n\x05token\x18\x01 \x01(\t\x12\x32\n\x07user_id\x18\x02 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserId\x12\x30\n\nexpiration\x18\x03 \x01(\x0b\x32\x1c.cs3.types.v1beta1.Timestamp\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\tBu\n\x1a\x63om.cs3.ocm.invite.v1beta1B\x0eResourcesProtoP\x01Z\rinvitev1beta1\xa2\x02\x03\x43OI\xaa\x02\x16\x43s3.Ocm.Invite.V1Beta1\xca\x02\x16\x43s3\\Ocm\\Invite\\V1Beta1b\x06proto3'
  ,
  dependencies=[cs3_dot_identity_dot_user_dot_v1beta1_dot_resources__pb2.DESCRIPTOR,cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2.DESCRIPTOR,cs3_dot_types_dot_v1beta1_dot_types__pb2.DESCRIPTOR,])




_INVITETOKEN = _descriptor.Descriptor(
  name='InviteToken',
  full_name='cs3.ocm.invite.v1beta1.InviteToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='cs3.ocm.invite.v1beta1.InviteToken.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='cs3.ocm.invite.v1beta1.InviteToken.user_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expiration', full_name='cs3.ocm.invite.v1beta1.InviteToken.expiration', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='cs3.ocm.invite.v1beta1.InviteToken.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=187,
  serialized_end=338,
)

_INVITETOKEN.fields_by_name['user_id'].message_type = cs3_dot_identity_dot_user_dot_v1beta1_dot_resources__pb2._USERID
_INVITETOKEN.fields_by_name['expiration'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['InviteToken'] = _INVITETOKEN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InviteToken = _reflection.GeneratedProtocolMessageType('InviteToken', (_message.Message,), {
  'DESCRIPTOR' : _INVITETOKEN,
  '__module__' : 'cs3.ocm.invite.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.ocm.invite.v1beta1.InviteToken)
  })
_sym_db.RegisterMessage(InviteToken)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
