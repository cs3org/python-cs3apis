# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/auth/applications/v1beta1/applications_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.auth.applications.v1beta1 import resources_pb2 as cs3_dot_auth_dot_applications_dot_v1beta1_dot_resources__pb2
from cs3.auth.provider.v1beta1 import resources_pb2 as cs3_dot_auth_dot_provider_dot_v1beta1_dot_resources__pb2
from cs3.identity.user.v1beta1 import resources_pb2 as cs3_dot_identity_dot_user_dot_v1beta1_dot_resources__pb2
from cs3.rpc.v1beta1 import status_pb2 as cs3_dot_rpc_dot_v1beta1_dot_status__pb2
from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cs3/auth/applications/v1beta1/applications_api.proto',
  package='cs3.auth.applications.v1beta1',
  syntax='proto3',
  serialized_options=b'\n!com.cs3.auth.applications.v1beta1B\024ApplicationsApiProtoP\001Z\023applicationsv1beta1\242\002\003CAA\252\002\035Cs3.Auth.Applications.V1Beta1\312\002\035Cs3\\Auth\\Applications\\V1Beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n4cs3/auth/applications/v1beta1/applications_api.proto\x12\x1d\x63s3.auth.applications.v1beta1\x1a-cs3/auth/applications/v1beta1/resources.proto\x1a)cs3/auth/provider/v1beta1/resources.proto\x1a)cs3/identity/user/v1beta1/resources.proto\x1a\x1c\x63s3/rpc/v1beta1/status.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\"\xbd\x02\n\x1aGenerateAppPasswordRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12^\n\x0btoken_scope\x18\x02 \x03(\x0b\x32I.cs3.auth.applications.v1beta1.GenerateAppPasswordRequest.TokenScopeEntry\x12\r\n\x05label\x18\x03 \x01(\t\x12\x30\n\nexpiration\x18\x04 \x01(\x0b\x32\x1c.cs3.types.v1beta1.Timestamp\x1aS\n\x0fTokenScopeEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .cs3.auth.provider.v1beta1.Scope:\x02\x38\x01\"\xb3\x01\n\x1bGenerateAppPasswordResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12@\n\x0c\x61pp_password\x18\x03 \x01(\x0b\x32*.cs3.auth.applications.v1beta1.AppPassword\"D\n\x17ListAppPasswordsRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\"\xb1\x01\n\x18ListAppPasswordsResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x41\n\rapp_passwords\x18\x03 \x03(\x0b\x32*.cs3.auth.applications.v1beta1.AppPassword\"[\n\x1cInvalidateAppPasswordRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x10\n\x08password\x18\x02 \x01(\t\"s\n\x1dInvalidateAppPasswordResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\"\x85\x01\n\x15GetAppPasswordRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12/\n\x04user\x18\x02 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserId\x12\x10\n\x08password\x18\x03 \x01(\t\"\xae\x01\n\x16GetAppPasswordResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12@\n\x0c\x61pp_password\x18\x03 \x01(\x0b\x32*.cs3.auth.applications.v1beta1.AppPassword2\xba\x04\n\x0f\x41pplicationsAPI\x12\x8c\x01\n\x13GenerateAppPassword\x12\x39.cs3.auth.applications.v1beta1.GenerateAppPasswordRequest\x1a:.cs3.auth.applications.v1beta1.GenerateAppPasswordResponse\x12\x83\x01\n\x10ListAppPasswords\x12\x36.cs3.auth.applications.v1beta1.ListAppPasswordsRequest\x1a\x37.cs3.auth.applications.v1beta1.ListAppPasswordsResponse\x12\x92\x01\n\x15InvalidateAppPassword\x12;.cs3.auth.applications.v1beta1.InvalidateAppPasswordRequest\x1a<.cs3.auth.applications.v1beta1.InvalidateAppPasswordResponse\x12}\n\x0eGetAppPassword\x12\x34.cs3.auth.applications.v1beta1.GetAppPasswordRequest\x1a\x35.cs3.auth.applications.v1beta1.GetAppPasswordResponseB\x96\x01\n!com.cs3.auth.applications.v1beta1B\x14\x41pplicationsApiProtoP\x01Z\x13\x61pplicationsv1beta1\xa2\x02\x03\x43\x41\x41\xaa\x02\x1d\x43s3.Auth.Applications.V1Beta1\xca\x02\x1d\x43s3\\Auth\\Applications\\V1Beta1b\x06proto3'
  ,
  dependencies=[cs3_dot_auth_dot_applications_dot_v1beta1_dot_resources__pb2.DESCRIPTOR,cs3_dot_auth_dot_provider_dot_v1beta1_dot_resources__pb2.DESCRIPTOR,cs3_dot_identity_dot_user_dot_v1beta1_dot_resources__pb2.DESCRIPTOR,cs3_dot_rpc_dot_v1beta1_dot_status__pb2.DESCRIPTOR,cs3_dot_types_dot_v1beta1_dot_types__pb2.DESCRIPTOR,])




_GENERATEAPPPASSWORDREQUEST_TOKENSCOPEENTRY = _descriptor.Descriptor(
  name='TokenScopeEntry',
  full_name='cs3.auth.applications.v1beta1.GenerateAppPasswordRequest.TokenScopeEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cs3.auth.applications.v1beta1.GenerateAppPasswordRequest.TokenScopeEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='cs3.auth.applications.v1beta1.GenerateAppPasswordRequest.TokenScopeEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=516,
  serialized_end=599,
)

_GENERATEAPPPASSWORDREQUEST = _descriptor.Descriptor(
  name='GenerateAppPasswordRequest',
  full_name='cs3.auth.applications.v1beta1.GenerateAppPasswordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.auth.applications.v1beta1.GenerateAppPasswordRequest.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token_scope', full_name='cs3.auth.applications.v1beta1.GenerateAppPasswordRequest.token_scope', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='cs3.auth.applications.v1beta1.GenerateAppPasswordRequest.label', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expiration', full_name='cs3.auth.applications.v1beta1.GenerateAppPasswordRequest.expiration', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GENERATEAPPPASSWORDREQUEST_TOKENSCOPEENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=599,
)


_GENERATEAPPPASSWORDRESPONSE = _descriptor.Descriptor(
  name='GenerateAppPasswordResponse',
  full_name='cs3.auth.applications.v1beta1.GenerateAppPasswordResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.auth.applications.v1beta1.GenerateAppPasswordResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.auth.applications.v1beta1.GenerateAppPasswordResponse.opaque', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_password', full_name='cs3.auth.applications.v1beta1.GenerateAppPasswordResponse.app_password', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=602,
  serialized_end=781,
)


_LISTAPPPASSWORDSREQUEST = _descriptor.Descriptor(
  name='ListAppPasswordsRequest',
  full_name='cs3.auth.applications.v1beta1.ListAppPasswordsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.auth.applications.v1beta1.ListAppPasswordsRequest.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=783,
  serialized_end=851,
)


_LISTAPPPASSWORDSRESPONSE = _descriptor.Descriptor(
  name='ListAppPasswordsResponse',
  full_name='cs3.auth.applications.v1beta1.ListAppPasswordsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.auth.applications.v1beta1.ListAppPasswordsResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.auth.applications.v1beta1.ListAppPasswordsResponse.opaque', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_passwords', full_name='cs3.auth.applications.v1beta1.ListAppPasswordsResponse.app_passwords', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=854,
  serialized_end=1031,
)


_INVALIDATEAPPPASSWORDREQUEST = _descriptor.Descriptor(
  name='InvalidateAppPasswordRequest',
  full_name='cs3.auth.applications.v1beta1.InvalidateAppPasswordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.auth.applications.v1beta1.InvalidateAppPasswordRequest.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='cs3.auth.applications.v1beta1.InvalidateAppPasswordRequest.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1033,
  serialized_end=1124,
)


_INVALIDATEAPPPASSWORDRESPONSE = _descriptor.Descriptor(
  name='InvalidateAppPasswordResponse',
  full_name='cs3.auth.applications.v1beta1.InvalidateAppPasswordResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.auth.applications.v1beta1.InvalidateAppPasswordResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.auth.applications.v1beta1.InvalidateAppPasswordResponse.opaque', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1126,
  serialized_end=1241,
)


_GETAPPPASSWORDREQUEST = _descriptor.Descriptor(
  name='GetAppPasswordRequest',
  full_name='cs3.auth.applications.v1beta1.GetAppPasswordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.auth.applications.v1beta1.GetAppPasswordRequest.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='cs3.auth.applications.v1beta1.GetAppPasswordRequest.user', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='cs3.auth.applications.v1beta1.GetAppPasswordRequest.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1244,
  serialized_end=1377,
)


_GETAPPPASSWORDRESPONSE = _descriptor.Descriptor(
  name='GetAppPasswordResponse',
  full_name='cs3.auth.applications.v1beta1.GetAppPasswordResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.auth.applications.v1beta1.GetAppPasswordResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.auth.applications.v1beta1.GetAppPasswordResponse.opaque', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_password', full_name='cs3.auth.applications.v1beta1.GetAppPasswordResponse.app_password', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1380,
  serialized_end=1554,
)

_GENERATEAPPPASSWORDREQUEST_TOKENSCOPEENTRY.fields_by_name['value'].message_type = cs3_dot_auth_dot_provider_dot_v1beta1_dot_resources__pb2._SCOPE
_GENERATEAPPPASSWORDREQUEST_TOKENSCOPEENTRY.containing_type = _GENERATEAPPPASSWORDREQUEST
_GENERATEAPPPASSWORDREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_GENERATEAPPPASSWORDREQUEST.fields_by_name['token_scope'].message_type = _GENERATEAPPPASSWORDREQUEST_TOKENSCOPEENTRY
_GENERATEAPPPASSWORDREQUEST.fields_by_name['expiration'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._TIMESTAMP
_GENERATEAPPPASSWORDRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_v1beta1_dot_status__pb2._STATUS
_GENERATEAPPPASSWORDRESPONSE.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_GENERATEAPPPASSWORDRESPONSE.fields_by_name['app_password'].message_type = cs3_dot_auth_dot_applications_dot_v1beta1_dot_resources__pb2._APPPASSWORD
_LISTAPPPASSWORDSREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_LISTAPPPASSWORDSRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_v1beta1_dot_status__pb2._STATUS
_LISTAPPPASSWORDSRESPONSE.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_LISTAPPPASSWORDSRESPONSE.fields_by_name['app_passwords'].message_type = cs3_dot_auth_dot_applications_dot_v1beta1_dot_resources__pb2._APPPASSWORD
_INVALIDATEAPPPASSWORDREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_INVALIDATEAPPPASSWORDRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_v1beta1_dot_status__pb2._STATUS
_INVALIDATEAPPPASSWORDRESPONSE.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_GETAPPPASSWORDREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_GETAPPPASSWORDREQUEST.fields_by_name['user'].message_type = cs3_dot_identity_dot_user_dot_v1beta1_dot_resources__pb2._USERID
_GETAPPPASSWORDRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_v1beta1_dot_status__pb2._STATUS
_GETAPPPASSWORDRESPONSE.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_GETAPPPASSWORDRESPONSE.fields_by_name['app_password'].message_type = cs3_dot_auth_dot_applications_dot_v1beta1_dot_resources__pb2._APPPASSWORD
DESCRIPTOR.message_types_by_name['GenerateAppPasswordRequest'] = _GENERATEAPPPASSWORDREQUEST
DESCRIPTOR.message_types_by_name['GenerateAppPasswordResponse'] = _GENERATEAPPPASSWORDRESPONSE
DESCRIPTOR.message_types_by_name['ListAppPasswordsRequest'] = _LISTAPPPASSWORDSREQUEST
DESCRIPTOR.message_types_by_name['ListAppPasswordsResponse'] = _LISTAPPPASSWORDSRESPONSE
DESCRIPTOR.message_types_by_name['InvalidateAppPasswordRequest'] = _INVALIDATEAPPPASSWORDREQUEST
DESCRIPTOR.message_types_by_name['InvalidateAppPasswordResponse'] = _INVALIDATEAPPPASSWORDRESPONSE
DESCRIPTOR.message_types_by_name['GetAppPasswordRequest'] = _GETAPPPASSWORDREQUEST
DESCRIPTOR.message_types_by_name['GetAppPasswordResponse'] = _GETAPPPASSWORDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenerateAppPasswordRequest = _reflection.GeneratedProtocolMessageType('GenerateAppPasswordRequest', (_message.Message,), {

  'TokenScopeEntry' : _reflection.GeneratedProtocolMessageType('TokenScopeEntry', (_message.Message,), {
    'DESCRIPTOR' : _GENERATEAPPPASSWORDREQUEST_TOKENSCOPEENTRY,
    '__module__' : 'cs3.auth.applications.v1beta1.applications_api_pb2'
    # @@protoc_insertion_point(class_scope:cs3.auth.applications.v1beta1.GenerateAppPasswordRequest.TokenScopeEntry)
    })
  ,
  'DESCRIPTOR' : _GENERATEAPPPASSWORDREQUEST,
  '__module__' : 'cs3.auth.applications.v1beta1.applications_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.auth.applications.v1beta1.GenerateAppPasswordRequest)
  })
_sym_db.RegisterMessage(GenerateAppPasswordRequest)
_sym_db.RegisterMessage(GenerateAppPasswordRequest.TokenScopeEntry)

GenerateAppPasswordResponse = _reflection.GeneratedProtocolMessageType('GenerateAppPasswordResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEAPPPASSWORDRESPONSE,
  '__module__' : 'cs3.auth.applications.v1beta1.applications_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.auth.applications.v1beta1.GenerateAppPasswordResponse)
  })
_sym_db.RegisterMessage(GenerateAppPasswordResponse)

ListAppPasswordsRequest = _reflection.GeneratedProtocolMessageType('ListAppPasswordsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTAPPPASSWORDSREQUEST,
  '__module__' : 'cs3.auth.applications.v1beta1.applications_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.auth.applications.v1beta1.ListAppPasswordsRequest)
  })
_sym_db.RegisterMessage(ListAppPasswordsRequest)

ListAppPasswordsResponse = _reflection.GeneratedProtocolMessageType('ListAppPasswordsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTAPPPASSWORDSRESPONSE,
  '__module__' : 'cs3.auth.applications.v1beta1.applications_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.auth.applications.v1beta1.ListAppPasswordsResponse)
  })
_sym_db.RegisterMessage(ListAppPasswordsResponse)

InvalidateAppPasswordRequest = _reflection.GeneratedProtocolMessageType('InvalidateAppPasswordRequest', (_message.Message,), {
  'DESCRIPTOR' : _INVALIDATEAPPPASSWORDREQUEST,
  '__module__' : 'cs3.auth.applications.v1beta1.applications_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.auth.applications.v1beta1.InvalidateAppPasswordRequest)
  })
_sym_db.RegisterMessage(InvalidateAppPasswordRequest)

InvalidateAppPasswordResponse = _reflection.GeneratedProtocolMessageType('InvalidateAppPasswordResponse', (_message.Message,), {
  'DESCRIPTOR' : _INVALIDATEAPPPASSWORDRESPONSE,
  '__module__' : 'cs3.auth.applications.v1beta1.applications_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.auth.applications.v1beta1.InvalidateAppPasswordResponse)
  })
_sym_db.RegisterMessage(InvalidateAppPasswordResponse)

GetAppPasswordRequest = _reflection.GeneratedProtocolMessageType('GetAppPasswordRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETAPPPASSWORDREQUEST,
  '__module__' : 'cs3.auth.applications.v1beta1.applications_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.auth.applications.v1beta1.GetAppPasswordRequest)
  })
_sym_db.RegisterMessage(GetAppPasswordRequest)

GetAppPasswordResponse = _reflection.GeneratedProtocolMessageType('GetAppPasswordResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETAPPPASSWORDRESPONSE,
  '__module__' : 'cs3.auth.applications.v1beta1.applications_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.auth.applications.v1beta1.GetAppPasswordResponse)
  })
_sym_db.RegisterMessage(GetAppPasswordResponse)


DESCRIPTOR._options = None
_GENERATEAPPPASSWORDREQUEST_TOKENSCOPEENTRY._options = None

_APPLICATIONSAPI = _descriptor.ServiceDescriptor(
  name='ApplicationsAPI',
  full_name='cs3.auth.applications.v1beta1.ApplicationsAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1557,
  serialized_end=2127,
  methods=[
  _descriptor.MethodDescriptor(
    name='GenerateAppPassword',
    full_name='cs3.auth.applications.v1beta1.ApplicationsAPI.GenerateAppPassword',
    index=0,
    containing_service=None,
    input_type=_GENERATEAPPPASSWORDREQUEST,
    output_type=_GENERATEAPPPASSWORDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListAppPasswords',
    full_name='cs3.auth.applications.v1beta1.ApplicationsAPI.ListAppPasswords',
    index=1,
    containing_service=None,
    input_type=_LISTAPPPASSWORDSREQUEST,
    output_type=_LISTAPPPASSWORDSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='InvalidateAppPassword',
    full_name='cs3.auth.applications.v1beta1.ApplicationsAPI.InvalidateAppPassword',
    index=2,
    containing_service=None,
    input_type=_INVALIDATEAPPPASSWORDREQUEST,
    output_type=_INVALIDATEAPPPASSWORDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAppPassword',
    full_name='cs3.auth.applications.v1beta1.ApplicationsAPI.GetAppPassword',
    index=3,
    containing_service=None,
    input_type=_GETAPPPASSWORDREQUEST,
    output_type=_GETAPPPASSWORDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_APPLICATIONSAPI)

DESCRIPTOR.services_by_name['ApplicationsAPI'] = _APPLICATIONSAPI

# @@protoc_insertion_point(module_scope)
