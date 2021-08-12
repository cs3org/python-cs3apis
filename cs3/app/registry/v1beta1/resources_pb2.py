# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/app/registry/v1beta1/resources.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cs3/app/registry/v1beta1/resources.proto',
  package='cs3.app.registry.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\034com.cs3.app.registry.v1beta1B\016ResourcesProtoP\001Z\017registryv1beta1\242\002\003CAR\252\002\030Cs3.App.Registry.V1Beta1\312\002\030Cs3\\App\\Registry\\V1Beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(cs3/app/registry/v1beta1/resources.proto\x12\x18\x63s3.app.registry.v1beta1\x1a\x1d\x63s3/types/v1beta1/types.proto\"\xa5\x01\n\x0cProviderInfo\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x12\n\nmime_types\x18\x02 \x03(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x0c\n\x04icon\x18\x06 \x01(\t\x12\x14\n\x0c\x64\x65sktop_only\x18\x07 \x01(\x08\"P\n\x0f\x41ppProviderList\x12=\n\rapp_providers\x18\x01 \x03(\x0b\x32&.cs3.app.registry.v1beta1.ProviderInfoB}\n\x1c\x63om.cs3.app.registry.v1beta1B\x0eResourcesProtoP\x01Z\x0fregistryv1beta1\xa2\x02\x03\x43\x41R\xaa\x02\x18\x43s3.App.Registry.V1Beta1\xca\x02\x18\x43s3\\App\\Registry\\V1Beta1b\x06proto3'
  ,
  dependencies=[cs3_dot_types_dot_v1beta1_dot_types__pb2.DESCRIPTOR,])




_PROVIDERINFO = _descriptor.Descriptor(
  name='ProviderInfo',
  full_name='cs3.app.registry.v1beta1.ProviderInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='opaque', full_name='cs3.app.registry.v1beta1.ProviderInfo.opaque', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mime_types', full_name='cs3.app.registry.v1beta1.ProviderInfo.mime_types', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='cs3.app.registry.v1beta1.ProviderInfo.address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cs3.app.registry.v1beta1.ProviderInfo.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='cs3.app.registry.v1beta1.ProviderInfo.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='icon', full_name='cs3.app.registry.v1beta1.ProviderInfo.icon', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='desktop_only', full_name='cs3.app.registry.v1beta1.ProviderInfo.desktop_only', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=102,
  serialized_end=267,
)


_APPPROVIDERLIST = _descriptor.Descriptor(
  name='AppProviderList',
  full_name='cs3.app.registry.v1beta1.AppProviderList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='app_providers', full_name='cs3.app.registry.v1beta1.AppProviderList.app_providers', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=269,
  serialized_end=349,
)

_PROVIDERINFO.fields_by_name['opaque'].message_type = cs3_dot_types_dot_v1beta1_dot_types__pb2._OPAQUE
_APPPROVIDERLIST.fields_by_name['app_providers'].message_type = _PROVIDERINFO
DESCRIPTOR.message_types_by_name['ProviderInfo'] = _PROVIDERINFO
DESCRIPTOR.message_types_by_name['AppProviderList'] = _APPPROVIDERLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProviderInfo = _reflection.GeneratedProtocolMessageType('ProviderInfo', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDERINFO,
  '__module__' : 'cs3.app.registry.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.app.registry.v1beta1.ProviderInfo)
  })
_sym_db.RegisterMessage(ProviderInfo)

AppProviderList = _reflection.GeneratedProtocolMessageType('AppProviderList', (_message.Message,), {
  'DESCRIPTOR' : _APPPROVIDERLIST,
  '__module__' : 'cs3.app.registry.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.app.registry.v1beta1.AppProviderList)
  })
_sym_db.RegisterMessage(AppProviderList)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
