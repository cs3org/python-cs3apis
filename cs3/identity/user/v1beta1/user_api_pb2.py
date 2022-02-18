# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/identity/user/v1beta1/user_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.identity.user.v1beta1 import resources_pb2 as cs3_dot_identity_dot_user_dot_v1beta1_dot_resources__pb2
from cs3.rpc.v1beta1 import status_pb2 as cs3_dot_rpc_dot_v1beta1_dot_status__pb2
from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(cs3/identity/user/v1beta1/user_api.proto\x12\x19\x63s3.identity.user.v1beta1\x1a)cs3/identity/user/v1beta1/resources.proto\x1a\x1c\x63s3/rpc/v1beta1/status.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\"\x92\x01\n\x0eGetUserRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x32\n\x07user_id\x18\x02 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserId\x12!\n\x19skip_fetching_user_groups\x18\x03 \x01(\x08\"\x94\x01\n\x0fGetUserResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12-\n\x04user\x18\x03 \x01(\x0b\x32\x1f.cs3.identity.user.v1beta1.User\"\x83\x01\n\x15GetUserByClaimRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\r\n\x05\x63laim\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12!\n\x19skip_fetching_user_groups\x18\x04 \x01(\x08\"\x9b\x01\n\x16GetUserByClaimResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12-\n\x04user\x18\x03 \x01(\x0b\x32\x1f.cs3.identity.user.v1beta1.User\"u\n\x14GetUserGroupsRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x32\n\x07user_id\x18\x02 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserId\"{\n\x15GetUserGroupsResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x0e\n\x06groups\x18\x03 \x03(\t\"p\n\x10\x46indUsersRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\x12!\n\x19skip_fetching_user_groups\x18\x03 \x01(\x08\"\x97\x01\n\x11\x46indUsersResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12.\n\x05users\x18\x03 \x03(\x0b\x32\x1f.cs3.identity.user.v1beta1.User2\xbe\x03\n\x07UserAPI\x12`\n\x07GetUser\x12).cs3.identity.user.v1beta1.GetUserRequest\x1a*.cs3.identity.user.v1beta1.GetUserResponse\x12u\n\x0eGetUserByClaim\x12\x30.cs3.identity.user.v1beta1.GetUserByClaimRequest\x1a\x31.cs3.identity.user.v1beta1.GetUserByClaimResponse\x12r\n\rGetUserGroups\x12/.cs3.identity.user.v1beta1.GetUserGroupsRequest\x1a\x30.cs3.identity.user.v1beta1.GetUserGroupsResponse\x12\x66\n\tFindUsers\x12+.cs3.identity.user.v1beta1.FindUsersRequest\x1a,.cs3.identity.user.v1beta1.FindUsersResponseBz\n\x1d\x63om.cs3.identity.user.v1beta1B\x0cUserApiProtoP\x01Z\x0buserv1beta1\xa2\x02\x03\x43IU\xaa\x02\x19\x43s3.Identity.User.V1Beta1\xca\x02\x19\x43s3\\Identity\\User\\V1Beta1b\x06proto3')



_GETUSERREQUEST = DESCRIPTOR.message_types_by_name['GetUserRequest']
_GETUSERRESPONSE = DESCRIPTOR.message_types_by_name['GetUserResponse']
_GETUSERBYCLAIMREQUEST = DESCRIPTOR.message_types_by_name['GetUserByClaimRequest']
_GETUSERBYCLAIMRESPONSE = DESCRIPTOR.message_types_by_name['GetUserByClaimResponse']
_GETUSERGROUPSREQUEST = DESCRIPTOR.message_types_by_name['GetUserGroupsRequest']
_GETUSERGROUPSRESPONSE = DESCRIPTOR.message_types_by_name['GetUserGroupsResponse']
_FINDUSERSREQUEST = DESCRIPTOR.message_types_by_name['FindUsersRequest']
_FINDUSERSRESPONSE = DESCRIPTOR.message_types_by_name['FindUsersResponse']
GetUserRequest = _reflection.GeneratedProtocolMessageType('GetUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERREQUEST,
  '__module__' : 'cs3.identity.user.v1beta1.user_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.identity.user.v1beta1.GetUserRequest)
  })
_sym_db.RegisterMessage(GetUserRequest)

GetUserResponse = _reflection.GeneratedProtocolMessageType('GetUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERRESPONSE,
  '__module__' : 'cs3.identity.user.v1beta1.user_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.identity.user.v1beta1.GetUserResponse)
  })
_sym_db.RegisterMessage(GetUserResponse)

GetUserByClaimRequest = _reflection.GeneratedProtocolMessageType('GetUserByClaimRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERBYCLAIMREQUEST,
  '__module__' : 'cs3.identity.user.v1beta1.user_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.identity.user.v1beta1.GetUserByClaimRequest)
  })
_sym_db.RegisterMessage(GetUserByClaimRequest)

GetUserByClaimResponse = _reflection.GeneratedProtocolMessageType('GetUserByClaimResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERBYCLAIMRESPONSE,
  '__module__' : 'cs3.identity.user.v1beta1.user_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.identity.user.v1beta1.GetUserByClaimResponse)
  })
_sym_db.RegisterMessage(GetUserByClaimResponse)

GetUserGroupsRequest = _reflection.GeneratedProtocolMessageType('GetUserGroupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERGROUPSREQUEST,
  '__module__' : 'cs3.identity.user.v1beta1.user_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.identity.user.v1beta1.GetUserGroupsRequest)
  })
_sym_db.RegisterMessage(GetUserGroupsRequest)

GetUserGroupsResponse = _reflection.GeneratedProtocolMessageType('GetUserGroupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERGROUPSRESPONSE,
  '__module__' : 'cs3.identity.user.v1beta1.user_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.identity.user.v1beta1.GetUserGroupsResponse)
  })
_sym_db.RegisterMessage(GetUserGroupsResponse)

FindUsersRequest = _reflection.GeneratedProtocolMessageType('FindUsersRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINDUSERSREQUEST,
  '__module__' : 'cs3.identity.user.v1beta1.user_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.identity.user.v1beta1.FindUsersRequest)
  })
_sym_db.RegisterMessage(FindUsersRequest)

FindUsersResponse = _reflection.GeneratedProtocolMessageType('FindUsersResponse', (_message.Message,), {
  'DESCRIPTOR' : _FINDUSERSRESPONSE,
  '__module__' : 'cs3.identity.user.v1beta1.user_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.identity.user.v1beta1.FindUsersResponse)
  })
_sym_db.RegisterMessage(FindUsersResponse)

_USERAPI = DESCRIPTOR.services_by_name['UserAPI']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035com.cs3.identity.user.v1beta1B\014UserApiProtoP\001Z\013userv1beta1\242\002\003CIU\252\002\031Cs3.Identity.User.V1Beta1\312\002\031Cs3\\Identity\\User\\V1Beta1'
  _GETUSERREQUEST._serialized_start=176
  _GETUSERREQUEST._serialized_end=322
  _GETUSERRESPONSE._serialized_start=325
  _GETUSERRESPONSE._serialized_end=473
  _GETUSERBYCLAIMREQUEST._serialized_start=476
  _GETUSERBYCLAIMREQUEST._serialized_end=607
  _GETUSERBYCLAIMRESPONSE._serialized_start=610
  _GETUSERBYCLAIMRESPONSE._serialized_end=765
  _GETUSERGROUPSREQUEST._serialized_start=767
  _GETUSERGROUPSREQUEST._serialized_end=884
  _GETUSERGROUPSRESPONSE._serialized_start=886
  _GETUSERGROUPSRESPONSE._serialized_end=1009
  _FINDUSERSREQUEST._serialized_start=1011
  _FINDUSERSREQUEST._serialized_end=1123
  _FINDUSERSRESPONSE._serialized_start=1126
  _FINDUSERSRESPONSE._serialized_end=1277
  _USERAPI._serialized_start=1280
  _USERAPI._serialized_end=1726
# @@protoc_insertion_point(module_scope)
