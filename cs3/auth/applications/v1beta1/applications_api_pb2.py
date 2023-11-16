# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/auth/applications/v1beta1/applications_api.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.auth.applications.v1beta1 import resources_pb2 as cs3_dot_auth_dot_applications_dot_v1beta1_dot_resources__pb2
from cs3.auth.provider.v1beta1 import resources_pb2 as cs3_dot_auth_dot_provider_dot_v1beta1_dot_resources__pb2
from cs3.identity.user.v1beta1 import resources_pb2 as cs3_dot_identity_dot_user_dot_v1beta1_dot_resources__pb2
from cs3.rpc.v1beta1 import status_pb2 as cs3_dot_rpc_dot_v1beta1_dot_status__pb2
from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4cs3/auth/applications/v1beta1/applications_api.proto\x12\x1d\x63s3.auth.applications.v1beta1\x1a-cs3/auth/applications/v1beta1/resources.proto\x1a)cs3/auth/provider/v1beta1/resources.proto\x1a)cs3/identity/user/v1beta1/resources.proto\x1a\x1c\x63s3/rpc/v1beta1/status.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\"\xf0\x02\n\x1aGenerateAppPasswordRequest\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12j\n\x0btoken_scope\x18\x02 \x03(\x0b\x32I.cs3.auth.applications.v1beta1.GenerateAppPasswordRequest.TokenScopeEntryR\ntokenScope\x12\x14\n\x05label\x18\x03 \x01(\tR\x05label\x12<\n\nexpiration\x18\x04 \x01(\x0b\x32\x1c.cs3.types.v1beta1.TimestampR\nexpiration\x1a_\n\x0fTokenScopeEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32 .cs3.auth.provider.v1beta1.ScopeR\x05value:\x02\x38\x01\"\xd0\x01\n\x1bGenerateAppPasswordResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12M\n\x0c\x61pp_password\x18\x03 \x01(\x0b\x32*.cs3.auth.applications.v1beta1.AppPasswordR\x0b\x61ppPassword\"L\n\x17ListAppPasswordsRequest\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\"\xcf\x01\n\x18ListAppPasswordsResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12O\n\rapp_passwords\x18\x03 \x03(\x0b\x32*.cs3.auth.applications.v1beta1.AppPasswordR\x0c\x61ppPasswords\"m\n\x1cInvalidateAppPasswordRequest\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x1a\n\x08password\x18\x02 \x01(\tR\x08password\"\x83\x01\n\x1dInvalidateAppPasswordResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\"\x9d\x01\n\x15GetAppPasswordRequest\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x35\n\x04user\x18\x02 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserIdR\x04user\x12\x1a\n\x08password\x18\x03 \x01(\tR\x08password\"\xcb\x01\n\x16GetAppPasswordResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12M\n\x0c\x61pp_password\x18\x03 \x01(\x0b\x32*.cs3.auth.applications.v1beta1.AppPasswordR\x0b\x61ppPassword2\xba\x04\n\x0f\x41pplicationsAPI\x12\x8c\x01\n\x13GenerateAppPassword\x12\x39.cs3.auth.applications.v1beta1.GenerateAppPasswordRequest\x1a:.cs3.auth.applications.v1beta1.GenerateAppPasswordResponse\x12\x83\x01\n\x10ListAppPasswords\x12\x36.cs3.auth.applications.v1beta1.ListAppPasswordsRequest\x1a\x37.cs3.auth.applications.v1beta1.ListAppPasswordsResponse\x12\x92\x01\n\x15InvalidateAppPassword\x12;.cs3.auth.applications.v1beta1.InvalidateAppPasswordRequest\x1a<.cs3.auth.applications.v1beta1.InvalidateAppPasswordResponse\x12}\n\x0eGetAppPassword\x12\x34.cs3.auth.applications.v1beta1.GetAppPasswordRequest\x1a\x35.cs3.auth.applications.v1beta1.GetAppPasswordResponseB\xa0\x02\n!com.cs3.auth.applications.v1beta1B\x14\x41pplicationsApiProtoP\x01ZNgithub.com/cs3org/go-cs3apis/cs3/auth/applications/v1beta1;applicationsv1beta1\xa2\x02\x03\x43\x41\x41\xaa\x02\x1d\x43s3.Auth.Applications.V1beta1\xca\x02\x1d\x43s3\\Auth\\Applications\\V1beta1\xe2\x02)Cs3\\Auth\\Applications\\V1beta1\\GPBMetadata\xea\x02 Cs3::Auth::Applications::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cs3.auth.applications.v1beta1.applications_api_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.cs3.auth.applications.v1beta1B\024ApplicationsApiProtoP\001ZNgithub.com/cs3org/go-cs3apis/cs3/auth/applications/v1beta1;applicationsv1beta1\242\002\003CAA\252\002\035Cs3.Auth.Applications.V1beta1\312\002\035Cs3\\Auth\\Applications\\V1beta1\342\002)Cs3\\Auth\\Applications\\V1beta1\\GPBMetadata\352\002 Cs3::Auth::Applications::V1beta1'
  _globals['_GENERATEAPPPASSWORDREQUEST_TOKENSCOPEENTRY']._options = None
  _globals['_GENERATEAPPPASSWORDREQUEST_TOKENSCOPEENTRY']._serialized_options = b'8\001'
  _globals['_GENERATEAPPPASSWORDREQUEST']._serialized_start=282
  _globals['_GENERATEAPPPASSWORDREQUEST']._serialized_end=650
  _globals['_GENERATEAPPPASSWORDREQUEST_TOKENSCOPEENTRY']._serialized_start=555
  _globals['_GENERATEAPPPASSWORDREQUEST_TOKENSCOPEENTRY']._serialized_end=650
  _globals['_GENERATEAPPPASSWORDRESPONSE']._serialized_start=653
  _globals['_GENERATEAPPPASSWORDRESPONSE']._serialized_end=861
  _globals['_LISTAPPPASSWORDSREQUEST']._serialized_start=863
  _globals['_LISTAPPPASSWORDSREQUEST']._serialized_end=939
  _globals['_LISTAPPPASSWORDSRESPONSE']._serialized_start=942
  _globals['_LISTAPPPASSWORDSRESPONSE']._serialized_end=1149
  _globals['_INVALIDATEAPPPASSWORDREQUEST']._serialized_start=1151
  _globals['_INVALIDATEAPPPASSWORDREQUEST']._serialized_end=1260
  _globals['_INVALIDATEAPPPASSWORDRESPONSE']._serialized_start=1263
  _globals['_INVALIDATEAPPPASSWORDRESPONSE']._serialized_end=1394
  _globals['_GETAPPPASSWORDREQUEST']._serialized_start=1397
  _globals['_GETAPPPASSWORDREQUEST']._serialized_end=1554
  _globals['_GETAPPPASSWORDRESPONSE']._serialized_start=1557
  _globals['_GETAPPPASSWORDRESPONSE']._serialized_end=1760
  _globals['_APPLICATIONSAPI']._serialized_start=1763
  _globals['_APPLICATIONSAPI']._serialized_end=2333
# @@protoc_insertion_point(module_scope)
