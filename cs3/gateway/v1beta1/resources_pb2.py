# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/gateway/v1beta1/resources.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.storage.provider.v1beta1 import resources_pb2 as cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2
from cs3.sharing.collaboration.v1beta1 import resources_pb2 as cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_resources__pb2
from cs3.sharing.link.v1beta1 import resources_pb2 as cs3_dot_sharing_dot_link_dot_v1beta1_dot_resources__pb2
from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#cs3/gateway/v1beta1/resources.proto\x12\x13\x63s3.gateway.v1beta1\x1a,cs3/storage/provider/v1beta1/resources.proto\x1a\x31\x63s3/sharing/collaboration/v1beta1/resources.proto\x1a(cs3/sharing/link/v1beta1/resources.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\"\x8b\x02\n\x12\x46ileUploadProtocol\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x1a\n\x08protocol\x18\x02 \x01(\tR\x08protocol\x12\'\n\x0fupload_endpoint\x18\x03 \x01(\tR\x0euploadEndpoint\x12g\n\x13\x61vailable_checksums\x18\x04 \x03(\x0b\x32\x36.cs3.storage.provider.v1beta1.ResourceChecksumPriorityR\x12\x61vailableChecksums\x12\x14\n\x05token\x18\x05 \x01(\tR\x05token\"\xa8\x01\n\x14\x46ileDownloadProtocol\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x1a\n\x08protocol\x18\x02 \x01(\tR\x08protocol\x12+\n\x11\x64ownload_endpoint\x18\x03 \x01(\tR\x10\x64ownloadEndpoint\x12\x14\n\x05token\x18\x04 \x01(\tR\x05token\"\xd7\x01\n\x11ShareResourceInfo\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12>\n\x05share\x18\x02 \x01(\x0b\x32(.cs3.sharing.collaboration.v1beta1.ShareR\x05share\x12O\n\rresource_info\x18\x03 \x01(\x0b\x32*.cs3.storage.provider.v1beta1.ResourceInfoR\x0cresourceInfo\"\xf8\x01\n\x19ReceivedShareResourceInfo\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12W\n\x0ereceived_share\x18\x02 \x01(\x0b\x32\x30.cs3.sharing.collaboration.v1beta1.ReceivedShareR\rreceivedShare\x12O\n\rresource_info\x18\x03 \x01(\x0b\x32*.cs3.storage.provider.v1beta1.ResourceInfoR\x0cresourceInfo\"\xe7\x01\n\x17PublicShareResourceInfo\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12H\n\x0cpublic_share\x18\x02 \x01(\x0b\x32%.cs3.sharing.link.v1beta1.PublicShareR\x0bpublicShare\x12O\n\rresource_info\x18\x03 \x01(\x0b\x32*.cs3.storage.provider.v1beta1.ResourceInfoR\x0cresourceInfoB\xd8\x01\n\x17\x63om.cs3.gateway.v1beta1B\x0eResourcesProtoP\x01Z?github.com/cs3org/go-cs3apis/cs3/gateway/v1beta1;gatewayv1beta1\xa2\x02\x03\x43GX\xaa\x02\x13\x43s3.Gateway.V1beta1\xca\x02\x13\x43s3\\Gateway\\V1beta1\xe2\x02\x1f\x43s3\\Gateway\\V1beta1\\GPBMetadata\xea\x02\x15\x43s3::Gateway::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cs3.gateway.v1beta1.resources_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.cs3.gateway.v1beta1B\016ResourcesProtoP\001Z?github.com/cs3org/go-cs3apis/cs3/gateway/v1beta1;gatewayv1beta1\242\002\003CGX\252\002\023Cs3.Gateway.V1beta1\312\002\023Cs3\\Gateway\\V1beta1\342\002\037Cs3\\Gateway\\V1beta1\\GPBMetadata\352\002\025Cs3::Gateway::V1beta1'
  _globals['_FILEUPLOADPROTOCOL']._serialized_start=231
  _globals['_FILEUPLOADPROTOCOL']._serialized_end=498
  _globals['_FILEDOWNLOADPROTOCOL']._serialized_start=501
  _globals['_FILEDOWNLOADPROTOCOL']._serialized_end=669
  _globals['_SHARERESOURCEINFO']._serialized_start=672
  _globals['_SHARERESOURCEINFO']._serialized_end=887
  _globals['_RECEIVEDSHARERESOURCEINFO']._serialized_start=890
  _globals['_RECEIVEDSHARERESOURCEINFO']._serialized_end=1138
  _globals['_PUBLICSHARERESOURCEINFO']._serialized_start=1141
  _globals['_PUBLICSHARERESOURCEINFO']._serialized_end=1372
# @@protoc_insertion_point(module_scope)
