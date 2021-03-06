# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/app/provider/v1beta1/provider_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.rpc.v1beta1 import status_pb2 as cs3_dot_rpc_dot_v1beta1_dot_status__pb2
from cs3.storage.provider.v1beta1 import resources_pb2 as cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2
from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cs3/app/provider/v1beta1/provider_api.proto',
  package='cs3.app.provider.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\034com.cs3.app.provider.v1beta1B\020ProviderApiProtoP\001Z\017providerv1beta1\242\002\003CAP\252\002\030Cs3.App.Provider.V1Beta1\312\002\030Cs3\\App\\Provider\\V1Beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+cs3/app/provider/v1beta1/provider_api.proto\x12\x18\x63s3.app.provider.v1beta1\x1a\x1c\x63s3/rpc/v1beta1/status.proto\x1a,cs3/storage/provider/v1beta1/resources.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\"\xe5\x02\n\x1cOpenFileInAppProviderRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x41\n\rresource_info\x18\x02 \x01(\x0b\x32*.cs3.storage.provider.v1beta1.ResourceInfo\x12R\n\tview_mode\x18\x03 \x01(\x0e\x32?.cs3.app.provider.v1beta1.OpenFileInAppProviderRequest.ViewMode\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x04 \x01(\t\"m\n\x08ViewMode\x12\x15\n\x11VIEW_MODE_INVALID\x10\x00\x12\x17\n\x13VIEW_MODE_VIEW_ONLY\x10\x01\x12\x17\n\x13VIEW_MODE_READ_ONLY\x10\x02\x12\x18\n\x14VIEW_MODE_READ_WRITE\x10\x03\"\x8d\x01\n\x1dOpenFileInAppProviderResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x18\n\x10\x61pp_provider_url\x18\x03 \x01(\t2\x98\x01\n\x0bProviderAPI\x12\x88\x01\n\x15OpenFileInAppProvider\x12\x36.cs3.app.provider.v1beta1.OpenFileInAppProviderRequest\x1a\x37.cs3.app.provider.v1beta1.OpenFileInAppProviderResponseB\x7f\n\x1c\x63om.cs3.app.provider.v1beta1B\x10ProviderApiProtoP\x01Z\x0fproviderv1beta1\xa2\x02\x03\x43\x41P\xaa\x02\x18\x43s3.App.Provider.V1Beta1\xca\x02\x18\x43s3\\App\\Provider\\V1Beta1b\x06proto3'
  ,
  dependencies=[cs3_dot_rpc_dot_v1beta1_dot_status__pb2.DESCRIPTOR,cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2.DESCRIPTOR,cs3_dot_types_dot_v1beta1_dot_types__pb2.DESCRIPTOR,])



_OPENFILEINAPPPROVIDERREQUEST_VIEWMODE = _descriptor.EnumDescriptor(
  name='ViewMode',
  full_name='cs3.app.provider.v1beta1.OpenFileInAppProviderRequest.ViewMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VIEW_MODE_INVALID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VIEW_MODE_VIEW_ONLY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VIEW_MODE_READ_ONLY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VIEW_MODE_READ_WRITE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=429,
  serialized_end=538,
)
_sym_db.RegisterEnumDescriptor(_OPENFILEINAPPPROVIDERREQUEST_VIEWMODE)


_OPENFILEINAPPPROVIDERREQUEST = _descriptor.Descriptor(
  name='OpenFileInAppProviderRequest',
  full_name='cs3.app.provider.v1beta1.OpenFileInAppProviderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.app.provider.v1beta1.OpenFileInAppProviderRequest.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_info', full_name='cs3.app.provider.v1beta1.OpenFileInAppProviderRequest.resource_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='view_mode', full_name='cs3.app.provider.v1beta1.OpenFileInAppProviderRequest.view_mode', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='access_token', full_name='cs3.app.provider.v1beta1.OpenFileInAppProviderRequest.access_token', index=3,
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
    _OPENFILEINAPPPROVIDERREQUEST_VIEWMODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=538,
)


_OPENFILEINAPPPROVIDERRESPONSE = _descriptor.Descriptor(
  name='OpenFileInAppProviderResponse',
  full_name='cs3.app.provider.v1beta1.OpenFileInAppProviderResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.app.provider.v1beta1.OpenFileInAppProviderResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.app.provider.v1beta1.OpenFileInAppProviderResponse.opaque', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_provider_url', full_name='cs3.app.provider.v1beta1.OpenFileInAppProviderResponse.app_provider_url', index=2,
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
  serialized_start=541,
  serialized_end=682,
)

_OPENFILEINAPPPROVIDERREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_OPENFILEINAPPPROVIDERREQUEST.fields_by_name['resource_info'].message_type = cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2._RESOURCEINFO
_OPENFILEINAPPPROVIDERREQUEST.fields_by_name['view_mode'].enum_type = _OPENFILEINAPPPROVIDERREQUEST_VIEWMODE
_OPENFILEINAPPPROVIDERREQUEST_VIEWMODE.containing_type = _OPENFILEINAPPPROVIDERREQUEST
_OPENFILEINAPPPROVIDERRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_v1beta1_dot_status__pb2._STATUS
_OPENFILEINAPPPROVIDERRESPONSE.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
DESCRIPTOR.message_types_by_name['OpenFileInAppProviderRequest'] = _OPENFILEINAPPPROVIDERREQUEST
DESCRIPTOR.message_types_by_name['OpenFileInAppProviderResponse'] = _OPENFILEINAPPPROVIDERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OpenFileInAppProviderRequest = _reflection.GeneratedProtocolMessageType('OpenFileInAppProviderRequest', (_message.Message,), {
  'DESCRIPTOR' : _OPENFILEINAPPPROVIDERREQUEST,
  '__module__' : 'cs3.app.provider.v1beta1.provider_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.app.provider.v1beta1.OpenFileInAppProviderRequest)
  })
_sym_db.RegisterMessage(OpenFileInAppProviderRequest)

OpenFileInAppProviderResponse = _reflection.GeneratedProtocolMessageType('OpenFileInAppProviderResponse', (_message.Message,), {
  'DESCRIPTOR' : _OPENFILEINAPPPROVIDERRESPONSE,
  '__module__' : 'cs3.app.provider.v1beta1.provider_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.app.provider.v1beta1.OpenFileInAppProviderResponse)
  })
_sym_db.RegisterMessage(OpenFileInAppProviderResponse)


DESCRIPTOR._options = None

_PROVIDERAPI = _descriptor.ServiceDescriptor(
  name='ProviderAPI',
  full_name='cs3.app.provider.v1beta1.ProviderAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=685,
  serialized_end=837,
  methods=[
  _descriptor.MethodDescriptor(
    name='OpenFileInAppProvider',
    full_name='cs3.app.provider.v1beta1.ProviderAPI.OpenFileInAppProvider',
    index=0,
    containing_service=None,
    input_type=_OPENFILEINAPPPROVIDERREQUEST,
    output_type=_OPENFILEINAPPPROVIDERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROVIDERAPI)

DESCRIPTOR.services_by_name['ProviderAPI'] = _PROVIDERAPI

# @@protoc_insertion_point(module_scope)
