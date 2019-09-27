# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/auth/v0alpha/auth.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.auth.v0alpha import resources_pb2 as cs3_dot_auth_dot_v0alpha_dot_resources__pb2
from cs3.rpc import status_pb2 as cs3_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cs3/auth/v0alpha/auth.proto',
  package='cs3.authv0alpha',
  syntax='proto3',
  serialized_options=_b('\n\023com.cs3.authv0alphaB\tAuthProtoP\001Z\rauthv0alphapb\242\002\006CBOXAB\252\002\017CS3.AuthV0Alpha\312\002\017CS3\\AuthV0Alpha'),
  serialized_pb=_b('\n\x1b\x63s3/auth/v0alpha/auth.proto\x12\x0f\x63s3.authv0alpha\x1a cs3/auth/v0alpha/resources.proto\x1a\x14\x63s3/rpc/status.proto\"F\n\x1aGenerateAccessTokenRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x15\n\rclient_secret\x18\x02 \x01(\t\"T\n\x1bGenerateAccessTokenResponse\x12\x1f\n\x06status\x18\x01 \x01(\x0b\x32\x0f.cs3.rpc.Status\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\t\"%\n\rWhoAmIRequest\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\"V\n\x0eWhoAmIResponse\x12\x1f\n\x06status\x18\x01 \x01(\x0b\x32\x0f.cs3.rpc.Status\x12#\n\x04user\x18\x02 \x01(\x0b\x32\x15.cs3.authv0alpha.User2\xca\x01\n\x0b\x41uthService\x12p\n\x13GenerateAccessToken\x12+.cs3.authv0alpha.GenerateAccessTokenRequest\x1a,.cs3.authv0alpha.GenerateAccessTokenResponse\x12I\n\x06WhoAmI\x12\x1e.cs3.authv0alpha.WhoAmIRequest\x1a\x1f.cs3.authv0alpha.WhoAmIResponseB^\n\x13\x63om.cs3.authv0alphaB\tAuthProtoP\x01Z\rauthv0alphapb\xa2\x02\x06\x43\x42OXAB\xaa\x02\x0f\x43S3.AuthV0Alpha\xca\x02\x0f\x43S3\\AuthV0Alphab\x06proto3')
  ,
  dependencies=[cs3_dot_auth_dot_v0alpha_dot_resources__pb2.DESCRIPTOR,cs3_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GENERATEACCESSTOKENREQUEST = _descriptor.Descriptor(
  name='GenerateAccessTokenRequest',
  full_name='cs3.authv0alpha.GenerateAccessTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='cs3.authv0alpha.GenerateAccessTokenRequest.client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_secret', full_name='cs3.authv0alpha.GenerateAccessTokenRequest.client_secret', index=1,
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
  serialized_start=104,
  serialized_end=174,
)


_GENERATEACCESSTOKENRESPONSE = _descriptor.Descriptor(
  name='GenerateAccessTokenResponse',
  full_name='cs3.authv0alpha.GenerateAccessTokenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.authv0alpha.GenerateAccessTokenResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_token', full_name='cs3.authv0alpha.GenerateAccessTokenResponse.access_token', index=1,
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
  serialized_start=176,
  serialized_end=260,
)


_WHOAMIREQUEST = _descriptor.Descriptor(
  name='WhoAmIRequest',
  full_name='cs3.authv0alpha.WhoAmIRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_token', full_name='cs3.authv0alpha.WhoAmIRequest.access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=262,
  serialized_end=299,
)


_WHOAMIRESPONSE = _descriptor.Descriptor(
  name='WhoAmIResponse',
  full_name='cs3.authv0alpha.WhoAmIResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.authv0alpha.WhoAmIResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='cs3.authv0alpha.WhoAmIResponse.user', index=1,
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
  serialized_start=301,
  serialized_end=387,
)

_GENERATEACCESSTOKENRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_status__pb2._STATUS
_WHOAMIRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_status__pb2._STATUS
_WHOAMIRESPONSE.fields_by_name['user'].message_type = cs3_dot_auth_dot_v0alpha_dot_resources__pb2._USER
DESCRIPTOR.message_types_by_name['GenerateAccessTokenRequest'] = _GENERATEACCESSTOKENREQUEST
DESCRIPTOR.message_types_by_name['GenerateAccessTokenResponse'] = _GENERATEACCESSTOKENRESPONSE
DESCRIPTOR.message_types_by_name['WhoAmIRequest'] = _WHOAMIREQUEST
DESCRIPTOR.message_types_by_name['WhoAmIResponse'] = _WHOAMIRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenerateAccessTokenRequest = _reflection.GeneratedProtocolMessageType('GenerateAccessTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEACCESSTOKENREQUEST,
  '__module__' : 'cs3.auth.v0alpha.auth_pb2'
  # @@protoc_insertion_point(class_scope:cs3.authv0alpha.GenerateAccessTokenRequest)
  })
_sym_db.RegisterMessage(GenerateAccessTokenRequest)

GenerateAccessTokenResponse = _reflection.GeneratedProtocolMessageType('GenerateAccessTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEACCESSTOKENRESPONSE,
  '__module__' : 'cs3.auth.v0alpha.auth_pb2'
  # @@protoc_insertion_point(class_scope:cs3.authv0alpha.GenerateAccessTokenResponse)
  })
_sym_db.RegisterMessage(GenerateAccessTokenResponse)

WhoAmIRequest = _reflection.GeneratedProtocolMessageType('WhoAmIRequest', (_message.Message,), {
  'DESCRIPTOR' : _WHOAMIREQUEST,
  '__module__' : 'cs3.auth.v0alpha.auth_pb2'
  # @@protoc_insertion_point(class_scope:cs3.authv0alpha.WhoAmIRequest)
  })
_sym_db.RegisterMessage(WhoAmIRequest)

WhoAmIResponse = _reflection.GeneratedProtocolMessageType('WhoAmIResponse', (_message.Message,), {
  'DESCRIPTOR' : _WHOAMIRESPONSE,
  '__module__' : 'cs3.auth.v0alpha.auth_pb2'
  # @@protoc_insertion_point(class_scope:cs3.authv0alpha.WhoAmIResponse)
  })
_sym_db.RegisterMessage(WhoAmIResponse)


DESCRIPTOR._options = None

_AUTHSERVICE = _descriptor.ServiceDescriptor(
  name='AuthService',
  full_name='cs3.authv0alpha.AuthService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=390,
  serialized_end=592,
  methods=[
  _descriptor.MethodDescriptor(
    name='GenerateAccessToken',
    full_name='cs3.authv0alpha.AuthService.GenerateAccessToken',
    index=0,
    containing_service=None,
    input_type=_GENERATEACCESSTOKENREQUEST,
    output_type=_GENERATEACCESSTOKENRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WhoAmI',
    full_name='cs3.authv0alpha.AuthService.WhoAmI',
    index=1,
    containing_service=None,
    input_type=_WHOAMIREQUEST,
    output_type=_WHOAMIRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTHSERVICE)

DESCRIPTOR.services_by_name['AuthService'] = _AUTHSERVICE

# @@protoc_insertion_point(module_scope)