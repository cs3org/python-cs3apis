# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/storage/registry/v1beta1/resources.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,cs3/storage/registry/v1beta1/resources.proto\x12\x1c\x63s3.storage.registry.v1beta1\x1a\x1d\x63s3/types/v1beta1/types.proto\"\xdf\x02\n\x0cProviderInfo\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x1f\n\x0bprovider_id\x18\x02 \x01(\tR\nproviderId\x12#\n\rprovider_path\x18\x03 \x01(\tR\x0cproviderPath\x12\x18\n\x07\x61\x64\x64ress\x18\x04 \x01(\tR\x07\x61\x64\x64ress\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x12O\n\x08\x66\x65\x61tures\x18\x06 \x01(\x0b\x32\x33.cs3.storage.registry.v1beta1.ProviderInfo.FeaturesR\x08\x66\x65\x61tures\x1aI\n\x08\x46\x65\x61tures\x12\x18\n\x07recycle\x18\x01 \x01(\x08R\x07recycle\x12#\n\rfile_versions\x18\x02 \x01(\x08R\x0c\x66ileVersionsB\x90\x02\n com.cs3.storage.registry.v1beta1B\x0eResourcesProtoP\x01ZIgithub.com/cs3org/go-cs3apis/cs3/storage/registry/v1beta1;registryv1beta1\xa2\x02\x03\x43SR\xaa\x02\x1c\x43s3.Storage.Registry.V1beta1\xca\x02\x1c\x43s3\\Storage\\Registry\\V1beta1\xe2\x02(Cs3\\Storage\\Registry\\V1beta1\\GPBMetadata\xea\x02\x1f\x43s3::Storage::Registry::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cs3.storage.registry.v1beta1.resources_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.cs3.storage.registry.v1beta1B\016ResourcesProtoP\001ZIgithub.com/cs3org/go-cs3apis/cs3/storage/registry/v1beta1;registryv1beta1\242\002\003CSR\252\002\034Cs3.Storage.Registry.V1beta1\312\002\034Cs3\\Storage\\Registry\\V1beta1\342\002(Cs3\\Storage\\Registry\\V1beta1\\GPBMetadata\352\002\037Cs3::Storage::Registry::V1beta1'
  _globals['_PROVIDERINFO']._serialized_start=110
  _globals['_PROVIDERINFO']._serialized_end=461
  _globals['_PROVIDERINFO_FEATURES']._serialized_start=388
  _globals['_PROVIDERINFO_FEATURES']._serialized_end=461
# @@protoc_insertion_point(module_scope)
