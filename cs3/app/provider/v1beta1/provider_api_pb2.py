# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/app/provider/v1beta1/provider_api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
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
  serialized_options=_b('\n\034com.cs3.app.provider.v1beta1B\020ProviderApiProtoP\001Z\017providerv1beta1\242\002\003CAP\252\002\030Cs3.App.Provider.V1Beta1\312\002\030Cs3\\App\\Provider\\V1Beta1'),
  serialized_pb=_b('\n+cs3/app/provider/v1beta1/provider_api.proto\x12\x18\x63s3.app.provider.v1beta1\x1a\x1c\x63s3/rpc/v1beta1/status.proto\x1a,cs3/storage/provider/v1beta1/resources.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\"\x91\x01\n\x0bOpenRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x41\n\rresource_info\x18\x02 \x01(\x0b\x32*.cs3.storage.provider.v1beta1.ResourceInfo\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x03 \x01(\t\"v\n\x0cOpenResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x12\n\niframe_url\x18\x03 \x01(\t2d\n\x0bProviderAPI\x12U\n\x04Open\x12%.cs3.app.provider.v1beta1.OpenRequest\x1a&.cs3.app.provider.v1beta1.OpenResponseB\x7f\n\x1c\x63om.cs3.app.provider.v1beta1B\x10ProviderApiProtoP\x01Z\x0fproviderv1beta1\xa2\x02\x03\x43\x41P\xaa\x02\x18\x43s3.App.Provider.V1Beta1\xca\x02\x18\x43s3\\App\\Provider\\V1Beta1b\x06proto3')
  ,
  dependencies=[cs3_dot_rpc_dot_v1beta1_dot_status__pb2.DESCRIPTOR,cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2.DESCRIPTOR,cs3_dot_types_dot_v1beta1_dot_types__pb2.DESCRIPTOR,])




_OPENREQUEST = _descriptor.Descriptor(
  name='OpenRequest',
  full_name='cs3.app.provider.v1beta1.OpenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.app.provider.v1beta1.OpenRequest.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_info', full_name='cs3.app.provider.v1beta1.OpenRequest.resource_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_token', full_name='cs3.app.provider.v1beta1.OpenRequest.access_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=181,
  serialized_end=326,
)


_OPENRESPONSE = _descriptor.Descriptor(
  name='OpenResponse',
  full_name='cs3.app.provider.v1beta1.OpenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.app.provider.v1beta1.OpenResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.app.provider.v1beta1.OpenResponse.opaque', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iframe_url', full_name='cs3.app.provider.v1beta1.OpenResponse.iframe_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=328,
  serialized_end=446,
)

_OPENREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_OPENREQUEST.fields_by_name['resource_info'].message_type = cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2._RESOURCEINFO
_OPENRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_v1beta1_dot_status__pb2._STATUS
_OPENRESPONSE.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
DESCRIPTOR.message_types_by_name['OpenRequest'] = _OPENREQUEST
DESCRIPTOR.message_types_by_name['OpenResponse'] = _OPENRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OpenRequest = _reflection.GeneratedProtocolMessageType('OpenRequest', (_message.Message,), {
  'DESCRIPTOR' : _OPENREQUEST,
  '__module__' : 'cs3.app.provider.v1beta1.provider_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.app.provider.v1beta1.OpenRequest)
  })
_sym_db.RegisterMessage(OpenRequest)

OpenResponse = _reflection.GeneratedProtocolMessageType('OpenResponse', (_message.Message,), {
  'DESCRIPTOR' : _OPENRESPONSE,
  '__module__' : 'cs3.app.provider.v1beta1.provider_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.app.provider.v1beta1.OpenResponse)
  })
_sym_db.RegisterMessage(OpenResponse)


DESCRIPTOR._options = None

_PROVIDERAPI = _descriptor.ServiceDescriptor(
  name='ProviderAPI',
  full_name='cs3.app.provider.v1beta1.ProviderAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=448,
  serialized_end=548,
  methods=[
  _descriptor.MethodDescriptor(
    name='Open',
    full_name='cs3.app.provider.v1beta1.ProviderAPI.Open',
    index=0,
    containing_service=None,
    input_type=_OPENREQUEST,
    output_type=_OPENRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROVIDERAPI)

DESCRIPTOR.services_by_name['ProviderAPI'] = _PROVIDERAPI

# @@protoc_insertion_point(module_scope)
