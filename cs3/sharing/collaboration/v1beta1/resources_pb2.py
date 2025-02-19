# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/sharing/collaboration/v1beta1/resources.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.identity.user.v1beta1 import resources_pb2 as cs3_dot_identity_dot_user_dot_v1beta1_dot_resources__pb2
from cs3.storage.provider.v1beta1 import resources_pb2 as cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2
from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1cs3/sharing/collaboration/v1beta1/resources.proto\x12!cs3.sharing.collaboration.v1beta1\x1a)cs3/identity/user/v1beta1/resources.proto\x1a,cs3/storage/provider/v1beta1/resources.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\"\xe4\x04\n\x05Share\x12:\n\x02id\x18\x01 \x01(\x0b\x32*.cs3.sharing.collaboration.v1beta1.ShareIdR\x02id\x12I\n\x0bresource_id\x18\x02 \x01(\x0b\x32(.cs3.storage.provider.v1beta1.ResourceIdR\nresourceId\x12U\n\x0bpermissions\x18\x03 \x01(\x0b\x32\x33.cs3.sharing.collaboration.v1beta1.SharePermissionsR\x0bpermissions\x12?\n\x07grantee\x18\x04 \x01(\x0b\x32%.cs3.storage.provider.v1beta1.GranteeR\x07grantee\x12\x37\n\x05owner\x18\x05 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserIdR\x05owner\x12;\n\x07\x63reator\x18\x06 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserIdR\x07\x63reator\x12\x32\n\x05\x63time\x18\x07 \x01(\x0b\x32\x1c.cs3.types.v1beta1.TimestampR\x05\x63time\x12\x32\n\x05mtime\x18\x08 \x01(\x0b\x32\x1c.cs3.types.v1beta1.TimestampR\x05mtime\x12<\n\nexpiration\x18\t \x01(\x0b\x32\x1c.cs3.types.v1beta1.TimestampR\nexpiration\x12 \n\x0b\x64\x65scription\x18\n \x01(\tR\x0b\x64\x65scription\"g\n\x10SharePermissions\x12S\n\x0bpermissions\x18\x01 \x01(\x0b\x32\x31.cs3.storage.provider.v1beta1.ResourcePermissionsR\x0bpermissions\"\x8c\x02\n\rReceivedShare\x12>\n\x05share\x18\x01 \x01(\x0b\x32(.cs3.sharing.collaboration.v1beta1.ShareR\x05share\x12\x43\n\x05state\x18\x02 \x01(\x0e\x32-.cs3.sharing.collaboration.v1beta1.ShareStateR\x05state\x12H\n\x0bmount_point\x18\x03 \x01(\x0b\x32\'.cs3.storage.provider.v1beta1.ReferenceR\nmountPoint\x12\x16\n\x06hidden\x18\x04 \x01(\x08R\x06hidden\x12\x14\n\x05\x61lias\x18\x05 \x01(\tR\x05\x61lias\"\xcf\x01\n\x08ShareKey\x12\x37\n\x05owner\x18\x02 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserIdR\x05owner\x12I\n\x0bresource_id\x18\x03 \x01(\x0b\x32(.cs3.storage.provider.v1beta1.ResourceIdR\nresourceId\x12?\n\x07grantee\x18\x04 \x01(\x0b\x32%.cs3.storage.provider.v1beta1.GranteeR\x07grantee\"&\n\x07ShareId\x12\x1b\n\topaque_id\x18\x02 \x01(\tR\x08opaqueId\"\x97\x01\n\x0eShareReference\x12<\n\x02id\x18\x01 \x01(\x0b\x32*.cs3.sharing.collaboration.v1beta1.ShareIdH\x00R\x02id\x12?\n\x03key\x18\x02 \x01(\x0b\x32+.cs3.sharing.collaboration.v1beta1.ShareKeyH\x00R\x03keyB\x06\n\x04spec\"\xe2\x01\n\nShareGrant\x12?\n\x07grantee\x18\x01 \x01(\x0b\x32%.cs3.storage.provider.v1beta1.GranteeR\x07grantee\x12U\n\x0bpermissions\x18\x02 \x01(\x0b\x32\x33.cs3.sharing.collaboration.v1beta1.SharePermissionsR\x0bpermissions\x12<\n\nexpiration\x18\x03 \x01(\x0b\x32\x1c.cs3.types.v1beta1.TimestampR\nexpiration\"\x83\x05\n\x06\x46ilter\x12\x42\n\x04type\x18\x02 \x01(\x0e\x32..cs3.sharing.collaboration.v1beta1.Filter.TypeR\x04type\x12K\n\x0bresource_id\x18\x03 \x01(\x0b\x32(.cs3.storage.provider.v1beta1.ResourceIdH\x00R\nresourceId\x12\x39\n\x05owner\x18\x04 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserIdH\x00R\x05owner\x12=\n\x07\x63reator\x18\x05 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserIdH\x00R\x07\x63reator\x12N\n\x0cgrantee_type\x18\x06 \x01(\x0e\x32).cs3.storage.provider.v1beta1.GranteeTypeH\x00R\x0bgranteeType\x12\x1b\n\x08space_id\x18\x07 \x01(\tH\x00R\x07spaceId\x12\x45\n\x05state\x18\x08 \x01(\x0e\x32-.cs3.sharing.collaboration.v1beta1.ShareStateH\x00R\x05state\"\xb1\x01\n\x04Type\x12\x10\n\x0cTYPE_INVALID\x10\x00\x12\x0b\n\x07TYPE_NO\x10\x01\x12\x14\n\x10TYPE_RESOURCE_ID\x10\x02\x12\x0e\n\nTYPE_OWNER\x10\x03\x12\x10\n\x0cTYPE_CREATOR\x10\x04\x12\x15\n\x11TYPE_GRANTEE_TYPE\x10\x05\x12\x18\n\x14TYPE_EXCLUDE_DENIALS\x10\x06\x12\x11\n\rTYPE_SPACE_ID\x10\x07\x12\x0e\n\nTYPE_STATE\x10\x08\x42\x06\n\x04term*r\n\nShareState\x12\x17\n\x13SHARE_STATE_INVALID\x10\x00\x12\x17\n\x13SHARE_STATE_PENDING\x10\x01\x12\x18\n\x14SHARE_STATE_ACCEPTED\x10\x02\x12\x18\n\x14SHARE_STATE_REJECTED\x10\x03\x42\xb3\x02\n%com.cs3.sharing.collaboration.v1beta1B\x0eResourcesProtoP\x01ZSgithub.com/cs3org/go-cs3apis/cs3/sharing/collaboration/v1beta1;collaborationv1beta1\xa2\x02\x03\x43SC\xaa\x02!Cs3.Sharing.Collaboration.V1beta1\xca\x02!Cs3\\Sharing\\Collaboration\\V1beta1\xe2\x02-Cs3\\Sharing\\Collaboration\\V1beta1\\GPBMetadata\xea\x02$Cs3::Sharing::Collaboration::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cs3.sharing.collaboration.v1beta1.resources_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%com.cs3.sharing.collaboration.v1beta1B\016ResourcesProtoP\001ZSgithub.com/cs3org/go-cs3apis/cs3/sharing/collaboration/v1beta1;collaborationv1beta1\242\002\003CSC\252\002!Cs3.Sharing.Collaboration.V1beta1\312\002!Cs3\\Sharing\\Collaboration\\V1beta1\342\002-Cs3\\Sharing\\Collaboration\\V1beta1\\GPBMetadata\352\002$Cs3::Sharing::Collaboration::V1beta1'
  _globals['_SHARESTATE']._serialized_start=2478
  _globals['_SHARESTATE']._serialized_end=2592
  _globals['_SHARE']._serialized_start=209
  _globals['_SHARE']._serialized_end=821
  _globals['_SHAREPERMISSIONS']._serialized_start=823
  _globals['_SHAREPERMISSIONS']._serialized_end=926
  _globals['_RECEIVEDSHARE']._serialized_start=929
  _globals['_RECEIVEDSHARE']._serialized_end=1197
  _globals['_SHAREKEY']._serialized_start=1200
  _globals['_SHAREKEY']._serialized_end=1407
  _globals['_SHAREID']._serialized_start=1409
  _globals['_SHAREID']._serialized_end=1447
  _globals['_SHAREREFERENCE']._serialized_start=1450
  _globals['_SHAREREFERENCE']._serialized_end=1601
  _globals['_SHAREGRANT']._serialized_start=1604
  _globals['_SHAREGRANT']._serialized_end=1830
  _globals['_FILTER']._serialized_start=1833
  _globals['_FILTER']._serialized_end=2476
  _globals['_FILTER_TYPE']._serialized_start=2291
  _globals['_FILTER_TYPE']._serialized_end=2468
# @@protoc_insertion_point(module_scope)
