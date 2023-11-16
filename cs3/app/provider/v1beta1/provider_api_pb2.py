# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/app/provider/v1beta1/provider_api.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.app.provider.v1beta1 import resources_pb2 as cs3_dot_app_dot_provider_dot_v1beta1_dot_resources__pb2
from cs3.rpc.v1beta1 import status_pb2 as cs3_dot_rpc_dot_v1beta1_dot_status__pb2
from cs3.storage.provider.v1beta1 import resources_pb2 as cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2
from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+cs3/app/provider/v1beta1/provider_api.proto\x12\x18\x63s3.app.provider.v1beta1\x1a(cs3/app/provider/v1beta1/resources.proto\x1a\x1c\x63s3/rpc/v1beta1/status.proto\x1a,cs3/storage/provider/v1beta1/resources.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\"\xfa\x01\n\x10OpenInAppRequest\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12O\n\rresource_info\x18\x02 \x01(\x0b\x32*.cs3.storage.provider.v1beta1.ResourceInfoR\x0cresourceInfo\x12?\n\tview_mode\x18\x03 \x01(\x0e\x32\".cs3.app.provider.v1beta1.ViewModeR\x08viewMode\x12!\n\x0c\x61\x63\x63\x65ss_token\x18\x04 \x01(\tR\x0b\x61\x63\x63\x65ssToken\"\xb8\x01\n\x11OpenInAppResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12?\n\x07\x61pp_url\x18\x03 \x01(\x0b\x32&.cs3.app.provider.v1beta1.OpenInAppURLR\x06\x61ppUrl2s\n\x0bProviderAPI\x12\x64\n\tOpenInApp\x12*.cs3.app.provider.v1beta1.OpenInAppRequest\x1a+.cs3.app.provider.v1beta1.OpenInAppResponseB\xfa\x01\n\x1c\x63om.cs3.app.provider.v1beta1B\x10ProviderApiProtoP\x01ZEgithub.com/cs3org/go-cs3apis/cs3/app/provider/v1beta1;providerv1beta1\xa2\x02\x03\x43\x41P\xaa\x02\x18\x43s3.App.Provider.V1beta1\xca\x02\x18\x43s3\\App\\Provider\\V1beta1\xe2\x02$Cs3\\App\\Provider\\V1beta1\\GPBMetadata\xea\x02\x1b\x43s3::App::Provider::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cs3.app.provider.v1beta1.provider_api_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034com.cs3.app.provider.v1beta1B\020ProviderApiProtoP\001ZEgithub.com/cs3org/go-cs3apis/cs3/app/provider/v1beta1;providerv1beta1\242\002\003CAP\252\002\030Cs3.App.Provider.V1beta1\312\002\030Cs3\\App\\Provider\\V1beta1\342\002$Cs3\\App\\Provider\\V1beta1\\GPBMetadata\352\002\033Cs3::App::Provider::V1beta1'
  _globals['_OPENINAPPREQUEST']._serialized_start=223
  _globals['_OPENINAPPREQUEST']._serialized_end=473
  _globals['_OPENINAPPRESPONSE']._serialized_start=476
  _globals['_OPENINAPPRESPONSE']._serialized_end=660
  _globals['_PROVIDERAPI']._serialized_start=662
  _globals['_PROVIDERAPI']._serialized_end=777
# @@protoc_insertion_point(module_scope)
