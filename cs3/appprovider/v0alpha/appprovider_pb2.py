# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/appprovider/v0alpha/appprovider.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.rpc import status_pb2 as cs3_dot_rpc_dot_status__pb2
from cs3.storageprovider.v0alpha import resources_pb2 as cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2
from cs3.types import types_pb2 as cs3_dot_types_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cs3/appprovider/v0alpha/appprovider.proto',
  package='cs3.appproviderv0alpha',
  syntax='proto3',
  serialized_options=_b('\n\032com.cs3.appproviderv0alphaB\020AppproviderProtoP\001Z\024appproviderv0alphapb\242\002\006CBOXAB\252\002\026CS3.AppProviderV0Alpha\312\002\026CS3\\AppProviderV0Alpha'),
  serialized_pb=_b('\n)cs3/appprovider/v0alpha/appprovider.proto\x12\x16\x63s3.appproviderv0alpha\x1a\x14\x63s3/rpc/status.proto\x1a+cs3/storageprovider/v0alpha/resources.proto\x1a\x15\x63s3/types/types.proto\"\x87\x01\n\x0bOpenRequest\x12!\n\x06opaque\x18\x01 \x01(\x0b\x32\x11.cs3.types.Opaque\x12?\n\rresource_info\x18\x02 \x01(\x0b\x32(.cs3.storageproviderv0alpha.ResourceInfo\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x03 \x01(\t\"f\n\x0cOpenResponse\x12\x1f\n\x06status\x18\x01 \x01(\x0b\x32\x0f.cs3.rpc.Status\x12!\n\x06opaque\x18\x02 \x01(\x0b\x32\x11.cs3.types.Opaque\x12\x12\n\niframe_url\x18\x03 \x01(\t2g\n\x12\x41ppProviderService\x12Q\n\x04Open\x12#.cs3.appproviderv0alpha.OpenRequest\x1a$.cs3.appproviderv0alpha.OpenResponseB\x81\x01\n\x1a\x63om.cs3.appproviderv0alphaB\x10\x41ppproviderProtoP\x01Z\x14\x61ppproviderv0alphapb\xa2\x02\x06\x43\x42OXAB\xaa\x02\x16\x43S3.AppProviderV0Alpha\xca\x02\x16\x43S3\\AppProviderV0Alphab\x06proto3')
  ,
  dependencies=[cs3_dot_rpc_dot_status__pb2.DESCRIPTOR,cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2.DESCRIPTOR,cs3_dot_types_dot_types__pb2.DESCRIPTOR,])




_OPENREQUEST = _descriptor.Descriptor(
  name='OpenRequest',
  full_name='cs3.appproviderv0alpha.OpenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.appproviderv0alpha.OpenRequest.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_info', full_name='cs3.appproviderv0alpha.OpenRequest.resource_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_token', full_name='cs3.appproviderv0alpha.OpenRequest.access_token', index=2,
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
  serialized_start=160,
  serialized_end=295,
)


_OPENRESPONSE = _descriptor.Descriptor(
  name='OpenResponse',
  full_name='cs3.appproviderv0alpha.OpenResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.appproviderv0alpha.OpenResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.appproviderv0alpha.OpenResponse.opaque', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iframe_url', full_name='cs3.appproviderv0alpha.OpenResponse.iframe_url', index=2,
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
  serialized_start=297,
  serialized_end=399,
)

_OPENREQUEST.fields_by_name['opaque'].message_type = cs3_dot_types_dot_types__pb2._OPAQUE
_OPENREQUEST.fields_by_name['resource_info'].message_type = cs3_dot_storageprovider_dot_v0alpha_dot_resources__pb2._RESOURCEINFO
_OPENRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_status__pb2._STATUS
_OPENRESPONSE.fields_by_name['opaque'].message_type = cs3_dot_types_dot_types__pb2._OPAQUE
DESCRIPTOR.message_types_by_name['OpenRequest'] = _OPENREQUEST
DESCRIPTOR.message_types_by_name['OpenResponse'] = _OPENRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OpenRequest = _reflection.GeneratedProtocolMessageType('OpenRequest', (_message.Message,), {
  'DESCRIPTOR' : _OPENREQUEST,
  '__module__' : 'cs3.appprovider.v0alpha.appprovider_pb2'
  # @@protoc_insertion_point(class_scope:cs3.appproviderv0alpha.OpenRequest)
  })
_sym_db.RegisterMessage(OpenRequest)

OpenResponse = _reflection.GeneratedProtocolMessageType('OpenResponse', (_message.Message,), {
  'DESCRIPTOR' : _OPENRESPONSE,
  '__module__' : 'cs3.appprovider.v0alpha.appprovider_pb2'
  # @@protoc_insertion_point(class_scope:cs3.appproviderv0alpha.OpenResponse)
  })
_sym_db.RegisterMessage(OpenResponse)


DESCRIPTOR._options = None

_APPPROVIDERSERVICE = _descriptor.ServiceDescriptor(
  name='AppProviderService',
  full_name='cs3.appproviderv0alpha.AppProviderService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=401,
  serialized_end=504,
  methods=[
  _descriptor.MethodDescriptor(
    name='Open',
    full_name='cs3.appproviderv0alpha.AppProviderService.Open',
    index=0,
    containing_service=None,
    input_type=_OPENREQUEST,
    output_type=_OPENRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_APPPROVIDERSERVICE)

DESCRIPTOR.services_by_name['AppProviderService'] = _APPPROVIDERSERVICE

# @@protoc_insertion_point(module_scope)
