# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/permissions/v1beta1/permissions_api.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.permissions.v1beta1 import resources_pb2 as cs3_dot_permissions_dot_v1beta1_dot_resources__pb2
from cs3.rpc.v1beta1 import status_pb2 as cs3_dot_rpc_dot_v1beta1_dot_status__pb2
from cs3.storage.provider.v1beta1 import resources_pb2 as cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-cs3/permissions/v1beta1/permissions_api.proto\x12\x17\x63s3.permissions.v1beta1\x1a\'cs3/permissions/v1beta1/resources.proto\x1a\x1c\x63s3/rpc/v1beta1/status.proto\x1a,cs3/storage/provider/v1beta1/resources.proto\"\xbf\x01\n\x16\x43heckPermissionRequest\x12\x1e\n\npermission\x18\x01 \x01(\tR\npermission\x12J\n\x0bsubject_ref\x18\x02 \x01(\x0b\x32).cs3.permissions.v1beta1.SubjectReferenceR\nsubjectRef\x12\x39\n\x03ref\x18\x03 \x01(\x0b\x32\'.cs3.storage.provider.v1beta1.ReferenceR\x03ref\"J\n\x17\x43heckPermissionResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status2\x86\x01\n\x0ePermissionsAPI\x12t\n\x0f\x43heckPermission\x12/.cs3.permissions.v1beta1.CheckPermissionRequest\x1a\x30.cs3.permissions.v1beta1.CheckPermissionResponseB\xf9\x01\n\x1b\x63om.cs3.permissions.v1beta1B\x13PermissionsApiProtoP\x01ZGgithub.com/cs3org/go-cs3apis/cs3/permissions/v1beta1;permissionsv1beta1\xa2\x02\x03\x43PX\xaa\x02\x17\x43s3.Permissions.V1beta1\xca\x02\x17\x43s3\\Permissions\\V1beta1\xe2\x02#Cs3\\Permissions\\V1beta1\\GPBMetadata\xea\x02\x19\x43s3::Permissions::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cs3.permissions.v1beta1.permissions_api_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.cs3.permissions.v1beta1B\023PermissionsApiProtoP\001ZGgithub.com/cs3org/go-cs3apis/cs3/permissions/v1beta1;permissionsv1beta1\242\002\003CPX\252\002\027Cs3.Permissions.V1beta1\312\002\027Cs3\\Permissions\\V1beta1\342\002#Cs3\\Permissions\\V1beta1\\GPBMetadata\352\002\031Cs3::Permissions::V1beta1'
  _globals['_CHECKPERMISSIONREQUEST']._serialized_start=192
  _globals['_CHECKPERMISSIONREQUEST']._serialized_end=383
  _globals['_CHECKPERMISSIONRESPONSE']._serialized_start=385
  _globals['_CHECKPERMISSIONRESPONSE']._serialized_end=459
  _globals['_PERMISSIONSAPI']._serialized_start=462
  _globals['_PERMISSIONSAPI']._serialized_end=596
# @@protoc_insertion_point(module_scope)
