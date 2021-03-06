# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/preferences/v1beta1/preferences_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.rpc.v1beta1 import status_pb2 as cs3_dot_rpc_dot_v1beta1_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cs3/preferences/v1beta1/preferences_api.proto',
  package='cs3.preferences.v1beta1',
  syntax='proto3',
  serialized_options=b'\n\033com.cs3.preferences.v1beta1B\023PreferencesApiProtoP\001Z\022preferencesv1beta1\242\002\003CPX\252\002\027Cs3.Preferences.V1Beta1\312\002\027Cs3\\Preferences\\V1Beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-cs3/preferences/v1beta1/preferences_api.proto\x12\x17\x63s3.preferences.v1beta1\x1a\x1c\x63s3/rpc/v1beta1/status.proto\")\n\rSetKeyRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0b\n\x03val\x18\x02 \x01(\t\"9\n\x0eSetKeyResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\"\x1c\n\rGetKeyRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"F\n\x0eGetKeyResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12\x0b\n\x03val\x18\x02 \x01(\t2\xc6\x01\n\x0ePreferencesAPI\x12Y\n\x06SetKey\x12&.cs3.preferences.v1beta1.SetKeyRequest\x1a\'.cs3.preferences.v1beta1.SetKeyResponse\x12Y\n\x06GetKey\x12&.cs3.preferences.v1beta1.GetKeyRequest\x1a\'.cs3.preferences.v1beta1.GetKeyResponseB\x82\x01\n\x1b\x63om.cs3.preferences.v1beta1B\x13PreferencesApiProtoP\x01Z\x12preferencesv1beta1\xa2\x02\x03\x43PX\xaa\x02\x17\x43s3.Preferences.V1Beta1\xca\x02\x17\x43s3\\Preferences\\V1Beta1b\x06proto3'
  ,
  dependencies=[cs3_dot_rpc_dot_v1beta1_dot_status__pb2.DESCRIPTOR,])




_SETKEYREQUEST = _descriptor.Descriptor(
  name='SetKeyRequest',
  full_name='cs3.preferences.v1beta1.SetKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cs3.preferences.v1beta1.SetKeyRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='val', full_name='cs3.preferences.v1beta1.SetKeyRequest.val', index=1,
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
  serialized_start=104,
  serialized_end=145,
)


_SETKEYRESPONSE = _descriptor.Descriptor(
  name='SetKeyResponse',
  full_name='cs3.preferences.v1beta1.SetKeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.preferences.v1beta1.SetKeyResponse.status', index=0,
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
  serialized_start=147,
  serialized_end=204,
)


_GETKEYREQUEST = _descriptor.Descriptor(
  name='GetKeyRequest',
  full_name='cs3.preferences.v1beta1.GetKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='cs3.preferences.v1beta1.GetKeyRequest.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=206,
  serialized_end=234,
)


_GETKEYRESPONSE = _descriptor.Descriptor(
  name='GetKeyResponse',
  full_name='cs3.preferences.v1beta1.GetKeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='cs3.preferences.v1beta1.GetKeyResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='val', full_name='cs3.preferences.v1beta1.GetKeyResponse.val', index=1,
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
  serialized_start=236,
  serialized_end=306,
)

_SETKEYRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_v1beta1_dot_status__pb2._STATUS
_GETKEYRESPONSE.fields_by_name['status'].message_type = cs3_dot_rpc_dot_v1beta1_dot_status__pb2._STATUS
DESCRIPTOR.message_types_by_name['SetKeyRequest'] = _SETKEYREQUEST
DESCRIPTOR.message_types_by_name['SetKeyResponse'] = _SETKEYRESPONSE
DESCRIPTOR.message_types_by_name['GetKeyRequest'] = _GETKEYREQUEST
DESCRIPTOR.message_types_by_name['GetKeyResponse'] = _GETKEYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetKeyRequest = _reflection.GeneratedProtocolMessageType('SetKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETKEYREQUEST,
  '__module__' : 'cs3.preferences.v1beta1.preferences_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.preferences.v1beta1.SetKeyRequest)
  })
_sym_db.RegisterMessage(SetKeyRequest)

SetKeyResponse = _reflection.GeneratedProtocolMessageType('SetKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETKEYRESPONSE,
  '__module__' : 'cs3.preferences.v1beta1.preferences_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.preferences.v1beta1.SetKeyResponse)
  })
_sym_db.RegisterMessage(SetKeyResponse)

GetKeyRequest = _reflection.GeneratedProtocolMessageType('GetKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETKEYREQUEST,
  '__module__' : 'cs3.preferences.v1beta1.preferences_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.preferences.v1beta1.GetKeyRequest)
  })
_sym_db.RegisterMessage(GetKeyRequest)

GetKeyResponse = _reflection.GeneratedProtocolMessageType('GetKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETKEYRESPONSE,
  '__module__' : 'cs3.preferences.v1beta1.preferences_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.preferences.v1beta1.GetKeyResponse)
  })
_sym_db.RegisterMessage(GetKeyResponse)


DESCRIPTOR._options = None

_PREFERENCESAPI = _descriptor.ServiceDescriptor(
  name='PreferencesAPI',
  full_name='cs3.preferences.v1beta1.PreferencesAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=309,
  serialized_end=507,
  methods=[
  _descriptor.MethodDescriptor(
    name='SetKey',
    full_name='cs3.preferences.v1beta1.PreferencesAPI.SetKey',
    index=0,
    containing_service=None,
    input_type=_SETKEYREQUEST,
    output_type=_SETKEYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetKey',
    full_name='cs3.preferences.v1beta1.PreferencesAPI.GetKey',
    index=1,
    containing_service=None,
    input_type=_GETKEYREQUEST,
    output_type=_GETKEYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PREFERENCESAPI)

DESCRIPTOR.services_by_name['PreferencesAPI'] = _PREFERENCESAPI

# @@protoc_insertion_point(module_scope)
