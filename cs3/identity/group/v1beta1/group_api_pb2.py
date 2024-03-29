# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/identity/group/v1beta1/group_api.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.identity.group.v1beta1 import resources_pb2 as cs3_dot_identity_dot_group_dot_v1beta1_dot_resources__pb2
from cs3.identity.user.v1beta1 import resources_pb2 as cs3_dot_identity_dot_user_dot_v1beta1_dot_resources__pb2
from cs3.rpc.v1beta1 import status_pb2 as cs3_dot_rpc_dot_v1beta1_dot_status__pb2
from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*cs3/identity/group/v1beta1/group_api.proto\x12\x1a\x63s3.identity.group.v1beta1\x1a*cs3/identity/group/v1beta1/resources.proto\x1a)cs3/identity/user/v1beta1/resources.proto\x1a\x1c\x63s3/rpc/v1beta1/status.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\"\xb8\x01\n\x0fGetGroupRequest\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12>\n\x08group_id\x18\x02 \x01(\x0b\x32#.cs3.identity.group.v1beta1.GroupIdR\x07groupId\x12\x32\n\x15skip_fetching_members\x18\x03 \x01(\x08R\x13skipFetchingMembers\"\xaf\x01\n\x10GetGroupResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x37\n\x05group\x18\x03 \x01(\x0b\x32!.cs3.identity.group.v1beta1.GroupR\x05group\"\xab\x01\n\x16GetGroupByClaimRequest\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x14\n\x05\x63laim\x18\x02 \x01(\tR\x05\x63laim\x12\x14\n\x05value\x18\x03 \x01(\tR\x05value\x12\x32\n\x15skip_fetching_members\x18\x04 \x01(\x08R\x13skipFetchingMembers\"\xb6\x01\n\x17GetGroupByClaimResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x37\n\x05group\x18\x03 \x01(\x0b\x32!.cs3.identity.group.v1beta1.GroupR\x05group\"\x86\x01\n\x11GetMembersRequest\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12>\n\x08group_id\x18\x02 \x01(\x0b\x32#.cs3.identity.group.v1beta1.GroupIdR\x07groupId\"\xb5\x01\n\x12GetMembersResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12;\n\x07members\x18\x03 \x03(\x0b\x32!.cs3.identity.user.v1beta1.UserIdR\x07members\"\xc1\x01\n\x10HasMemberRequest\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12>\n\x08group_id\x18\x02 \x01(\x0b\x32#.cs3.identity.group.v1beta1.GroupIdR\x07groupId\x12:\n\x07user_id\x18\x03 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserIdR\x06userId\"\x87\x01\n\x11HasMemberResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x0e\n\x02ok\x18\x03 \x01(\x08R\x02ok\"\x92\x01\n\x11\x46indGroupsRequest\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x16\n\x06\x66ilter\x18\x02 \x01(\tR\x06\x66ilter\x12\x32\n\x15skip_fetching_members\x18\x03 \x01(\x08R\x13skipFetchingMembers\"\xb3\x01\n\x12\x46indGroupsResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x39\n\x06groups\x18\x03 \x03(\x0b\x32!.cs3.identity.group.v1beta1.GroupR\x06groups2\xb1\x04\n\x08GroupAPI\x12\x65\n\x08GetGroup\x12+.cs3.identity.group.v1beta1.GetGroupRequest\x1a,.cs3.identity.group.v1beta1.GetGroupResponse\x12z\n\x0fGetGroupByClaim\x12\x32.cs3.identity.group.v1beta1.GetGroupByClaimRequest\x1a\x33.cs3.identity.group.v1beta1.GetGroupByClaimResponse\x12k\n\nGetMembers\x12-.cs3.identity.group.v1beta1.GetMembersRequest\x1a..cs3.identity.group.v1beta1.GetMembersResponse\x12h\n\tHasMember\x12,.cs3.identity.group.v1beta1.HasMemberRequest\x1a-.cs3.identity.group.v1beta1.HasMemberResponse\x12k\n\nFindGroups\x12-.cs3.identity.group.v1beta1.FindGroupsRequest\x1a..cs3.identity.group.v1beta1.FindGroupsResponseB\x80\x02\n\x1e\x63om.cs3.identity.group.v1beta1B\rGroupApiProtoP\x01ZDgithub.com/cs3org/go-cs3apis/cs3/identity/group/v1beta1;groupv1beta1\xa2\x02\x03\x43IG\xaa\x02\x1a\x43s3.Identity.Group.V1beta1\xca\x02\x1a\x43s3\\Identity\\Group\\V1beta1\xe2\x02&Cs3\\Identity\\Group\\V1beta1\\GPBMetadata\xea\x02\x1d\x43s3::Identity::Group::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cs3.identity.group.v1beta1.group_api_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.cs3.identity.group.v1beta1B\rGroupApiProtoP\001ZDgithub.com/cs3org/go-cs3apis/cs3/identity/group/v1beta1;groupv1beta1\242\002\003CIG\252\002\032Cs3.Identity.Group.V1beta1\312\002\032Cs3\\Identity\\Group\\V1beta1\342\002&Cs3\\Identity\\Group\\V1beta1\\GPBMetadata\352\002\035Cs3::Identity::Group::V1beta1'
  _globals['_GETGROUPREQUEST']._serialized_start=223
  _globals['_GETGROUPREQUEST']._serialized_end=407
  _globals['_GETGROUPRESPONSE']._serialized_start=410
  _globals['_GETGROUPRESPONSE']._serialized_end=585
  _globals['_GETGROUPBYCLAIMREQUEST']._serialized_start=588
  _globals['_GETGROUPBYCLAIMREQUEST']._serialized_end=759
  _globals['_GETGROUPBYCLAIMRESPONSE']._serialized_start=762
  _globals['_GETGROUPBYCLAIMRESPONSE']._serialized_end=944
  _globals['_GETMEMBERSREQUEST']._serialized_start=947
  _globals['_GETMEMBERSREQUEST']._serialized_end=1081
  _globals['_GETMEMBERSRESPONSE']._serialized_start=1084
  _globals['_GETMEMBERSRESPONSE']._serialized_end=1265
  _globals['_HASMEMBERREQUEST']._serialized_start=1268
  _globals['_HASMEMBERREQUEST']._serialized_end=1461
  _globals['_HASMEMBERRESPONSE']._serialized_start=1464
  _globals['_HASMEMBERRESPONSE']._serialized_end=1599
  _globals['_FINDGROUPSREQUEST']._serialized_start=1602
  _globals['_FINDGROUPSREQUEST']._serialized_end=1748
  _globals['_FINDGROUPSRESPONSE']._serialized_start=1751
  _globals['_FINDGROUPSRESPONSE']._serialized_end=1930
  _globals['_GROUPAPI']._serialized_start=1933
  _globals['_GROUPAPI']._serialized_end=2494
# @@protoc_insertion_point(module_scope)
