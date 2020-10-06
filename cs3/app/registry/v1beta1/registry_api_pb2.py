# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/app/registry/v1beta1/registry_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.app.registry.v1beta1 import resources_pb2 as cs3_dot_app_dot_registry_dot_v1beta1_dot_resources__pb2
from cs3.rpc.v1beta1 import status_pb2 as cs3_dot_rpc_dot_v1beta1_dot_status__pb2
from cs3.storage.provider.v1beta1 import resources_pb2 as cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2
from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cs3/app/registry/v1beta1/registry_api.proto',
  package='cs3.app.registry.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\034com.cs3.app.registry.v1beta1B\020RegistryApiProtoP\001Z\017registryv1beta1\242\002\003CAR\252\002\030Cs3.App.Registry.V1Beta1\312\002\030Cs3\\App\\Registry\\V1Beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+cs3/app/registry/v1beta1/registry_api.proto\x12\x18\x63s3.app.registry.v1beta1\x1a(cs3/app/registry/v1beta1/resources.proto\x1a\x1c\x63s3/rpc/v1beta1/status.proto\x1a,cs3/storage/provider/v1beta1/resources.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\"\x86\x01\n\x16GetAppProvidersRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x41\n\rresource_info\x18\x02 \x01(\x0b\x32*.cs3.storage.provider.v1beta1.ResourceInfo\"\xa8\x01\n\x17GetAppProvidersResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x39\n\tproviders\x18\x03 \x03(\x0b\x32&.cs3.app.registry.v1beta1.ProviderInfo\"D\n\x17ListAppProvidersRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\"\xa9\x01\n\x18ListAppProvidersResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x39\n\tproviders\x18\x03 \x03(\x0b\x32&.cs3.app.registry.v1beta1.ProviderInfo2\x80\x02\n\x0bRegistryAPI\x12v\n\x0fGetAppProviders\x12\x30.cs3.app.registry.v1beta1.GetAppProvidersRequest\x1a\x31.cs3.app.registry.v1beta1.GetAppProvidersResponse\x12y\n\x10ListAppProviders\x12\x31.cs3.app.registry.v1beta1.ListAppProvidersRequest\x1a\x32.cs3.app.registry.v1beta1.ListAppProvidersResponseB\x7f\n\x1c\x63om.cs3.app.registry.v1beta1B\x10RegistryApiProtoP\x01Z\x0fregistryv1beta1\xa2\x02\x03\x43\x41R\xaa\x02\x18\x43s3.App.Registry.V1Beta1\xca\x02\x18\x43s3\\App\\Registry\\V1Beta1b\x06proto3'
  ,
  dependencies=[cs3_dot_app_dot_registry_dot_v1beta1_dot_resources__pb2.DESCRIPTOR,cs3_dot_rpc_dot_v1beta1_dot_status__pb2.DESCRIPTOR,cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2.DESCRIPTOR,cs3_dot_types_dot_v1beta1_dot_types__pb2.DESCRIPTOR,])




_GETAPPPROVIDERSREQUEST = _descriptor.Descriptor(
  name='GetAppProvidersRequest',
  full_name='cs3.app.registry.v1beta1.GetAppProvidersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.app.registry.v1beta1.GetAppProvidersRequest.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_info', full_name='cs3.app.registry.v1beta1.GetAppProvidersRequest.resource_info', index=1,
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
  serialized_start=223,
  serialized_end=357,
)


_GETAPPPROVIDERSRESPONSE = _descriptor.Descriptor(
  name='GetAppProvidersResponse',
  full_name='cs3.app.registry.v1beta1.GetAppProvidersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.app.registry.v1beta1.GetAppProvidersResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.app.registry.v1beta1.GetAppProvidersResponse.opaque', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='providers', full_name='cs3.app.registry.v1beta1.GetAppProvidersResponse.providers', index=2,
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
  serialized_start=360,
  serialized_end=528,
)


_LISTAPPPROVIDERSREQUEST = _descriptor.Descriptor(
  name='ListAppProvidersRequest',
  full_name='cs3.app.registry.v1beta1.ListAppProvidersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.app.registry.v1beta1.ListAppProvidersRequest.opaque', index=0,
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
  serialized_start=530,
  serialized_end=598,
)


_LISTAPPPROVIDERSRESPONSE = _descriptor.Descriptor(
  name='ListAppProvidersResponse',
  full_name='cs3.app.registry.v1beta1.ListAppProvidersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.app.registry.v1beta1.ListAppProvidersResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.app.registry.v1beta1.ListAppProvidersResponse.opaque', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='providers', full_name='cs3.app.registry.v1beta1.ListAppProvidersResponse.providers', index=2,
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
  serialized_start=601,
  serialized_end=770,
)

_GETAPPPROVIDERSREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_GETAPPPROVIDERSREQUEST.fields_by_name['resource_info'].message_type = cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2._RESOURCEINFO
_GETAPPPROVIDERSRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_v1beta1_dot_status__pb2._STATUS
_GETAPPPROVIDERSRESPONSE.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_GETAPPPROVIDERSRESPONSE.fields_by_name['providers'].message_type = cs3_dot_app_dot_registry_dot_v1beta1_dot_resources__pb2._PROVIDERINFO
_LISTAPPPROVIDERSREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_LISTAPPPROVIDERSRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_v1beta1_dot_status__pb2._STATUS
_LISTAPPPROVIDERSRESPONSE.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_LISTAPPPROVIDERSRESPONSE.fields_by_name['providers'].message_type = cs3_dot_app_dot_registry_dot_v1beta1_dot_resources__pb2._PROVIDERINFO
DESCRIPTOR.message_types_by_name['GetAppProvidersRequest'] = _GETAPPPROVIDERSREQUEST
DESCRIPTOR.message_types_by_name['GetAppProvidersResponse'] = _GETAPPPROVIDERSRESPONSE
DESCRIPTOR.message_types_by_name['ListAppProvidersRequest'] = _LISTAPPPROVIDERSREQUEST
DESCRIPTOR.message_types_by_name['ListAppProvidersResponse'] = _LISTAPPPROVIDERSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAppProvidersRequest = _reflection.GeneratedProtocolMessageType('GetAppProvidersRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETAPPPROVIDERSREQUEST,
  '__module__' : 'cs3.app.registry.v1beta1.registry_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.app.registry.v1beta1.GetAppProvidersRequest)
  })
_sym_db.RegisterMessage(GetAppProvidersRequest)

GetAppProvidersResponse = _reflection.GeneratedProtocolMessageType('GetAppProvidersResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETAPPPROVIDERSRESPONSE,
  '__module__' : 'cs3.app.registry.v1beta1.registry_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.app.registry.v1beta1.GetAppProvidersResponse)
  })
_sym_db.RegisterMessage(GetAppProvidersResponse)

ListAppProvidersRequest = _reflection.GeneratedProtocolMessageType('ListAppProvidersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTAPPPROVIDERSREQUEST,
  '__module__' : 'cs3.app.registry.v1beta1.registry_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.app.registry.v1beta1.ListAppProvidersRequest)
  })
_sym_db.RegisterMessage(ListAppProvidersRequest)

ListAppProvidersResponse = _reflection.GeneratedProtocolMessageType('ListAppProvidersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTAPPPROVIDERSRESPONSE,
  '__module__' : 'cs3.app.registry.v1beta1.registry_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.app.registry.v1beta1.ListAppProvidersResponse)
  })
_sym_db.RegisterMessage(ListAppProvidersResponse)


DESCRIPTOR._options = None

_REGISTRYAPI = _descriptor.ServiceDescriptor(
  name='RegistryAPI',
  full_name='cs3.app.registry.v1beta1.RegistryAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=773,
  serialized_end=1029,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAppProviders',
    full_name='cs3.app.registry.v1beta1.RegistryAPI.GetAppProviders',
    index=0,
    containing_service=None,
    input_type=_GETAPPPROVIDERSREQUEST,
    output_type=_GETAPPPROVIDERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListAppProviders',
    full_name='cs3.app.registry.v1beta1.RegistryAPI.ListAppProviders',
    index=1,
    containing_service=None,
    input_type=_LISTAPPPROVIDERSREQUEST,
    output_type=_LISTAPPPROVIDERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REGISTRYAPI)

DESCRIPTOR.services_by_name['RegistryAPI'] = _REGISTRYAPI

# @@protoc_insertion_point(module_scope)
