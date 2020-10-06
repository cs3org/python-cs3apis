# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/auth/registry/v1beta1/registry_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.auth.registry.v1beta1 import resources_pb2 as cs3_dot_auth_dot_registry_dot_v1beta1_dot_resources__pb2
from cs3.rpc.v1beta1 import status_pb2 as cs3_dot_rpc_dot_v1beta1_dot_status__pb2
from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cs3/auth/registry/v1beta1/registry_api.proto',
  package='cs3.auth.registry.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\035com.cs3.auth.registry.v1beta1B\020RegistryApiProtoP\001Z\017registryv1beta1\242\002\003CAR\252\002\031Cs3.Auth.Registry.V1Beta1\312\002\031Cs3\\Auth\\Registry\\V1Beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,cs3/auth/registry/v1beta1/registry_api.proto\x12\x19\x63s3.auth.registry.v1beta1\x1a)cs3/auth/registry/v1beta1/resources.proto\x1a\x1c\x63s3/rpc/v1beta1/status.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\"Q\n\x16GetAuthProviderRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x0c\n\x04type\x18\x02 \x01(\t\"\xa8\x01\n\x17GetAuthProviderResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x39\n\x08provider\x18\x03 \x01(\x0b\x32\'.cs3.auth.registry.v1beta1.ProviderInfo\"E\n\x18ListAuthProvidersRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\"\xab\x01\n\x19ListAuthProvidersResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12:\n\tproviders\x18\x03 \x03(\x0b\x32\'.cs3.auth.registry.v1beta1.ProviderInfo2\x87\x02\n\x0bRegistryAPI\x12x\n\x0fGetAuthProvider\x12\x31.cs3.auth.registry.v1beta1.GetAuthProviderRequest\x1a\x32.cs3.auth.registry.v1beta1.GetAuthProviderResponse\x12~\n\x11ListAuthProviders\x12\x33.cs3.auth.registry.v1beta1.ListAuthProvidersRequest\x1a\x34.cs3.auth.registry.v1beta1.ListAuthProvidersResponseB\x82\x01\n\x1d\x63om.cs3.auth.registry.v1beta1B\x10RegistryApiProtoP\x01Z\x0fregistryv1beta1\xa2\x02\x03\x43\x41R\xaa\x02\x19\x43s3.Auth.Registry.V1Beta1\xca\x02\x19\x43s3\\Auth\\Registry\\V1Beta1b\x06proto3'
  ,
  dependencies=[cs3_dot_auth_dot_registry_dot_v1beta1_dot_resources__pb2.DESCRIPTOR,cs3_dot_rpc_dot_v1beta1_dot_status__pb2.DESCRIPTOR,cs3_dot_types_dot_v1beta1_dot_types__pb2.DESCRIPTOR,])




_GETAUTHPROVIDERREQUEST = _descriptor.Descriptor(
  name='GetAuthProviderRequest',
  full_name='cs3.auth.registry.v1beta1.GetAuthProviderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.auth.registry.v1beta1.GetAuthProviderRequest.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='cs3.auth.registry.v1beta1.GetAuthProviderRequest.type', index=1,
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
  serialized_start=179,
  serialized_end=260,
)


_GETAUTHPROVIDERRESPONSE = _descriptor.Descriptor(
  name='GetAuthProviderResponse',
  full_name='cs3.auth.registry.v1beta1.GetAuthProviderResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.auth.registry.v1beta1.GetAuthProviderResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.auth.registry.v1beta1.GetAuthProviderResponse.opaque', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='provider', full_name='cs3.auth.registry.v1beta1.GetAuthProviderResponse.provider', index=2,
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
  serialized_start=263,
  serialized_end=431,
)


_LISTAUTHPROVIDERSREQUEST = _descriptor.Descriptor(
  name='ListAuthProvidersRequest',
  full_name='cs3.auth.registry.v1beta1.ListAuthProvidersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.auth.registry.v1beta1.ListAuthProvidersRequest.opaque', index=0,
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
  serialized_start=433,
  serialized_end=502,
)


_LISTAUTHPROVIDERSRESPONSE = _descriptor.Descriptor(
  name='ListAuthProvidersResponse',
  full_name='cs3.auth.registry.v1beta1.ListAuthProvidersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.auth.registry.v1beta1.ListAuthProvidersResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.auth.registry.v1beta1.ListAuthProvidersResponse.opaque', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='providers', full_name='cs3.auth.registry.v1beta1.ListAuthProvidersResponse.providers', index=2,
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
  serialized_start=505,
  serialized_end=676,
)

_GETAUTHPROVIDERREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_GETAUTHPROVIDERRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_v1beta1_dot_status__pb2._STATUS
_GETAUTHPROVIDERRESPONSE.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_GETAUTHPROVIDERRESPONSE.fields_by_name['provider'].message_type = cs3_dot_auth_dot_registry_dot_v1beta1_dot_resources__pb2._PROVIDERINFO
_LISTAUTHPROVIDERSREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_LISTAUTHPROVIDERSRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_v1beta1_dot_status__pb2._STATUS
_LISTAUTHPROVIDERSRESPONSE.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_LISTAUTHPROVIDERSRESPONSE.fields_by_name['providers'].message_type = cs3_dot_auth_dot_registry_dot_v1beta1_dot_resources__pb2._PROVIDERINFO
DESCRIPTOR.message_types_by_name['GetAuthProviderRequest'] = _GETAUTHPROVIDERREQUEST
DESCRIPTOR.message_types_by_name['GetAuthProviderResponse'] = _GETAUTHPROVIDERRESPONSE
DESCRIPTOR.message_types_by_name['ListAuthProvidersRequest'] = _LISTAUTHPROVIDERSREQUEST
DESCRIPTOR.message_types_by_name['ListAuthProvidersResponse'] = _LISTAUTHPROVIDERSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAuthProviderRequest = _reflection.GeneratedProtocolMessageType('GetAuthProviderRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETAUTHPROVIDERREQUEST,
  '__module__' : 'cs3.auth.registry.v1beta1.registry_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.auth.registry.v1beta1.GetAuthProviderRequest)
  })
_sym_db.RegisterMessage(GetAuthProviderRequest)

GetAuthProviderResponse = _reflection.GeneratedProtocolMessageType('GetAuthProviderResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETAUTHPROVIDERRESPONSE,
  '__module__' : 'cs3.auth.registry.v1beta1.registry_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.auth.registry.v1beta1.GetAuthProviderResponse)
  })
_sym_db.RegisterMessage(GetAuthProviderResponse)

ListAuthProvidersRequest = _reflection.GeneratedProtocolMessageType('ListAuthProvidersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTAUTHPROVIDERSREQUEST,
  '__module__' : 'cs3.auth.registry.v1beta1.registry_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.auth.registry.v1beta1.ListAuthProvidersRequest)
  })
_sym_db.RegisterMessage(ListAuthProvidersRequest)

ListAuthProvidersResponse = _reflection.GeneratedProtocolMessageType('ListAuthProvidersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTAUTHPROVIDERSRESPONSE,
  '__module__' : 'cs3.auth.registry.v1beta1.registry_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.auth.registry.v1beta1.ListAuthProvidersResponse)
  })
_sym_db.RegisterMessage(ListAuthProvidersResponse)


DESCRIPTOR._options = None

_REGISTRYAPI = _descriptor.ServiceDescriptor(
  name='RegistryAPI',
  full_name='cs3.auth.registry.v1beta1.RegistryAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=679,
  serialized_end=942,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAuthProvider',
    full_name='cs3.auth.registry.v1beta1.RegistryAPI.GetAuthProvider',
    index=0,
    containing_service=None,
    input_type=_GETAUTHPROVIDERREQUEST,
    output_type=_GETAUTHPROVIDERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListAuthProviders',
    full_name='cs3.auth.registry.v1beta1.RegistryAPI.ListAuthProviders',
    index=1,
    containing_service=None,
    input_type=_LISTAUTHPROVIDERSREQUEST,
    output_type=_LISTAUTHPROVIDERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REGISTRYAPI)

DESCRIPTOR.services_by_name['RegistryAPI'] = _REGISTRYAPI

# @@protoc_insertion_point(module_scope)
