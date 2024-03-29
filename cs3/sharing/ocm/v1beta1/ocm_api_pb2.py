# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/sharing/ocm/v1beta1/ocm_api.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.identity.user.v1beta1 import resources_pb2 as cs3_dot_identity_dot_user_dot_v1beta1_dot_resources__pb2
from cs3.ocm.provider.v1beta1 import resources_pb2 as cs3_dot_ocm_dot_provider_dot_v1beta1_dot_resources__pb2
from cs3.rpc.v1beta1 import status_pb2 as cs3_dot_rpc_dot_v1beta1_dot_status__pb2
from cs3.sharing.ocm.v1beta1 import resources_pb2 as cs3_dot_sharing_dot_ocm_dot_v1beta1_dot_resources__pb2
from cs3.storage.provider.v1beta1 import resources_pb2 as cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2
from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%cs3/sharing/ocm/v1beta1/ocm_api.proto\x12\x17\x63s3.sharing.ocm.v1beta1\x1a)cs3/identity/user/v1beta1/resources.proto\x1a(cs3/ocm/provider/v1beta1/resources.proto\x1a\x1c\x63s3/rpc/v1beta1/status.proto\x1a\'cs3/sharing/ocm/v1beta1/resources.proto\x1a,cs3/storage/provider/v1beta1/resources.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\x1a google/protobuf/field_mask.proto\"\xc2\x03\n\x15\x43reateOCMShareRequest\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12I\n\x0bresource_id\x18\x02 \x01(\x0b\x32(.cs3.storage.provider.v1beta1.ResourceIdR\nresourceId\x12?\n\x07grantee\x18\x03 \x01(\x0b\x32%.cs3.storage.provider.v1beta1.GranteeR\x07grantee\x12^\n\x17recipient_mesh_provider\x18\x04 \x01(\x0b\x32&.cs3.ocm.provider.v1beta1.ProviderInfoR\x15recipientMeshProvider\x12L\n\x0e\x61\x63\x63\x65ss_methods\x18\x05 \x03(\x0b\x32%.cs3.sharing.ocm.v1beta1.AccessMethodR\raccessMethods\x12<\n\nexpiration\x18\x06 \x01(\x0b\x32\x1c.cs3.types.v1beta1.TimestampR\nexpiration\"\xe8\x01\n\x16\x43reateOCMShareResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x34\n\x05share\x18\x03 \x01(\x0b\x32\x1e.cs3.sharing.ocm.v1beta1.ShareR\x05share\x12\x34\n\x16recipient_display_name\x18\x04 \x01(\tR\x14recipientDisplayName\"\x80\x03\n\x15UpdateOCMShareRequest\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x39\n\x03ref\x18\x02 \x01(\x0b\x32\'.cs3.sharing.ocm.v1beta1.ShareReferenceR\x03ref\x12P\n\x05\x66ield\x18\x03 \x03(\x0b\x32:.cs3.sharing.ocm.v1beta1.UpdateOCMShareRequest.UpdateFieldR\x05\x66ield\x1a\xa6\x01\n\x0bUpdateField\x12>\n\nexpiration\x18\x01 \x01(\x0b\x32\x1c.cs3.types.v1beta1.TimestampH\x00R\nexpiration\x12N\n\x0e\x61\x63\x63\x65ss_methods\x18\x02 \x01(\x0b\x32%.cs3.sharing.ocm.v1beta1.AccessMethodH\x00R\raccessMethodsB\x07\n\x05\x66ield\"|\n\x16UpdateOCMShareResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\"\x92\x05\n\x14ListOCMSharesRequest\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12N\n\x07\x66ilters\x18\x02 \x03(\x0b\x32\x34.cs3.sharing.ocm.v1beta1.ListOCMSharesRequest.FilterR\x07\x66ilters\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x1a\xba\x03\n\x06\x46ilter\x12M\n\x04type\x18\x02 \x01(\x0e\x32\x39.cs3.sharing.ocm.v1beta1.ListOCMSharesRequest.Filter.TypeR\x04type\x12K\n\x0bresource_id\x18\x03 \x01(\x0b\x32(.cs3.storage.provider.v1beta1.ResourceIdH\x00R\nresourceId\x12\x39\n\x05owner\x18\x04 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserIdH\x00R\x05owner\x12=\n\x07\x63reator\x18\x05 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserIdH\x00R\x07\x63reator\"\x91\x01\n\x04Type\x12\x10\n\x0cTYPE_INVALID\x10\x00\x12\x0b\n\x07TYPE_NO\x10\x01\x12\x14\n\x10TYPE_RESOURCE_ID\x10\x02\x12\x0e\n\nTYPE_OWNER\x10\x03\x12\x10\n\x0cTYPE_CREATOR\x10\x04\x12\x17\n\x13TYPE_OWNER_PROVIDER\x10\x05\x12\x19\n\x15TYPE_CREATOR_PROVIDER\x10\x06\x42\x06\n\x04term\"\xdb\x01\n\x15ListOCMSharesResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x36\n\x06shares\x18\x03 \x03(\x0b\x32\x1e.cs3.sharing.ocm.v1beta1.ShareR\x06shares\x12&\n\x0fnext_page_token\x18\x04 \x01(\tR\rnextPageToken\"\x85\x01\n\x15RemoveOCMShareRequest\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x39\n\x03ref\x18\x02 \x01(\x0b\x32\'.cs3.sharing.ocm.v1beta1.ShareReferenceR\x03ref\"|\n\x16RemoveOCMShareResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\"\x82\x01\n\x12GetOCMShareRequest\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x39\n\x03ref\x18\x02 \x01(\x0b\x32\'.cs3.sharing.ocm.v1beta1.ShareReferenceR\x03ref\"\xaf\x01\n\x13GetOCMShareResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x34\n\x05share\x18\x03 \x01(\x0b\x32\x1e.cs3.sharing.ocm.v1beta1.ShareR\x05share\"1\n\x19GetOCMShareByTokenRequest\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\"\x83\x01\n\x1aGetOCMShareByTokenResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x34\n\x05share\x18\x02 \x01(\x0b\x32\x1e.cs3.sharing.ocm.v1beta1.ShareR\x05share\"\x8d\x01\n\x1cListReceivedOCMSharesRequest\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"\xeb\x01\n\x1dListReceivedOCMSharesResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12>\n\x06shares\x18\x03 \x03(\x0b\x32&.cs3.sharing.ocm.v1beta1.ReceivedShareR\x06shares\x12&\n\x0fnext_page_token\x18\x04 \x01(\tR\rnextPageToken\"\xcd\x01\n\x1dUpdateReceivedOCMShareRequest\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12<\n\x05share\x18\x02 \x01(\x0b\x32&.cs3.sharing.ocm.v1beta1.ReceivedShareR\x05share\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"\x84\x01\n\x1eUpdateReceivedOCMShareResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\"\x8a\x01\n\x1aGetReceivedOCMShareRequest\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x39\n\x03ref\x18\x02 \x01(\x0b\x32\'.cs3.sharing.ocm.v1beta1.ShareReferenceR\x03ref\"\xbf\x01\n\x1bGetReceivedOCMShareResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12<\n\x05share\x18\x03 \x01(\x0b\x32&.cs3.sharing.ocm.v1beta1.ReceivedShareR\x05share2\xd2\x08\n\x06OcmAPI\x12q\n\x0e\x43reateOCMShare\x12..cs3.sharing.ocm.v1beta1.CreateOCMShareRequest\x1a/.cs3.sharing.ocm.v1beta1.CreateOCMShareResponse\x12q\n\x0eRemoveOCMShare\x12..cs3.sharing.ocm.v1beta1.RemoveOCMShareRequest\x1a/.cs3.sharing.ocm.v1beta1.RemoveOCMShareResponse\x12h\n\x0bGetOCMShare\x12+.cs3.sharing.ocm.v1beta1.GetOCMShareRequest\x1a,.cs3.sharing.ocm.v1beta1.GetOCMShareResponse\x12}\n\x12GetOCMShareByToken\x12\x32.cs3.sharing.ocm.v1beta1.GetOCMShareByTokenRequest\x1a\x33.cs3.sharing.ocm.v1beta1.GetOCMShareByTokenResponse\x12n\n\rListOCMShares\x12-.cs3.sharing.ocm.v1beta1.ListOCMSharesRequest\x1a..cs3.sharing.ocm.v1beta1.ListOCMSharesResponse\x12q\n\x0eUpdateOCMShare\x12..cs3.sharing.ocm.v1beta1.UpdateOCMShareRequest\x1a/.cs3.sharing.ocm.v1beta1.UpdateOCMShareResponse\x12\x86\x01\n\x15ListReceivedOCMShares\x12\x35.cs3.sharing.ocm.v1beta1.ListReceivedOCMSharesRequest\x1a\x36.cs3.sharing.ocm.v1beta1.ListReceivedOCMSharesResponse\x12\x89\x01\n\x16UpdateReceivedOCMShare\x12\x36.cs3.sharing.ocm.v1beta1.UpdateReceivedOCMShareRequest\x1a\x37.cs3.sharing.ocm.v1beta1.UpdateReceivedOCMShareResponse\x12\x80\x01\n\x13GetReceivedOCMShare\x12\x33.cs3.sharing.ocm.v1beta1.GetReceivedOCMShareRequest\x1a\x34.cs3.sharing.ocm.v1beta1.GetReceivedOCMShareResponseB\xea\x01\n\x1b\x63om.cs3.sharing.ocm.v1beta1B\x0bOcmApiProtoP\x01Z?github.com/cs3org/go-cs3apis/cs3/sharing/ocm/v1beta1;ocmv1beta1\xa2\x02\x03\x43SO\xaa\x02\x17\x43s3.Sharing.Ocm.V1beta1\xca\x02\x17\x43s3\\Sharing\\Ocm\\V1beta1\xe2\x02#Cs3\\Sharing\\Ocm\\V1beta1\\GPBMetadata\xea\x02\x1a\x43s3::Sharing::Ocm::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cs3.sharing.ocm.v1beta1.ocm_api_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.cs3.sharing.ocm.v1beta1B\013OcmApiProtoP\001Z?github.com/cs3org/go-cs3apis/cs3/sharing/ocm/v1beta1;ocmv1beta1\242\002\003CSO\252\002\027Cs3.Sharing.Ocm.V1beta1\312\002\027Cs3\\Sharing\\Ocm\\V1beta1\342\002#Cs3\\Sharing\\Ocm\\V1beta1\\GPBMetadata\352\002\032Cs3::Sharing::Ocm::V1beta1'
  _globals['_CREATEOCMSHAREREQUEST']._serialized_start=334
  _globals['_CREATEOCMSHAREREQUEST']._serialized_end=784
  _globals['_CREATEOCMSHARERESPONSE']._serialized_start=787
  _globals['_CREATEOCMSHARERESPONSE']._serialized_end=1019
  _globals['_UPDATEOCMSHAREREQUEST']._serialized_start=1022
  _globals['_UPDATEOCMSHAREREQUEST']._serialized_end=1406
  _globals['_UPDATEOCMSHAREREQUEST_UPDATEFIELD']._serialized_start=1240
  _globals['_UPDATEOCMSHAREREQUEST_UPDATEFIELD']._serialized_end=1406
  _globals['_UPDATEOCMSHARERESPONSE']._serialized_start=1408
  _globals['_UPDATEOCMSHARERESPONSE']._serialized_end=1532
  _globals['_LISTOCMSHARESREQUEST']._serialized_start=1535
  _globals['_LISTOCMSHARESREQUEST']._serialized_end=2193
  _globals['_LISTOCMSHARESREQUEST_FILTER']._serialized_start=1751
  _globals['_LISTOCMSHARESREQUEST_FILTER']._serialized_end=2193
  _globals['_LISTOCMSHARESREQUEST_FILTER_TYPE']._serialized_start=2040
  _globals['_LISTOCMSHARESREQUEST_FILTER_TYPE']._serialized_end=2185
  _globals['_LISTOCMSHARESRESPONSE']._serialized_start=2196
  _globals['_LISTOCMSHARESRESPONSE']._serialized_end=2415
  _globals['_REMOVEOCMSHAREREQUEST']._serialized_start=2418
  _globals['_REMOVEOCMSHAREREQUEST']._serialized_end=2551
  _globals['_REMOVEOCMSHARERESPONSE']._serialized_start=2553
  _globals['_REMOVEOCMSHARERESPONSE']._serialized_end=2677
  _globals['_GETOCMSHAREREQUEST']._serialized_start=2680
  _globals['_GETOCMSHAREREQUEST']._serialized_end=2810
  _globals['_GETOCMSHARERESPONSE']._serialized_start=2813
  _globals['_GETOCMSHARERESPONSE']._serialized_end=2988
  _globals['_GETOCMSHAREBYTOKENREQUEST']._serialized_start=2990
  _globals['_GETOCMSHAREBYTOKENREQUEST']._serialized_end=3039
  _globals['_GETOCMSHAREBYTOKENRESPONSE']._serialized_start=3042
  _globals['_GETOCMSHAREBYTOKENRESPONSE']._serialized_end=3173
  _globals['_LISTRECEIVEDOCMSHARESREQUEST']._serialized_start=3176
  _globals['_LISTRECEIVEDOCMSHARESREQUEST']._serialized_end=3317
  _globals['_LISTRECEIVEDOCMSHARESRESPONSE']._serialized_start=3320
  _globals['_LISTRECEIVEDOCMSHARESRESPONSE']._serialized_end=3555
  _globals['_UPDATERECEIVEDOCMSHAREREQUEST']._serialized_start=3558
  _globals['_UPDATERECEIVEDOCMSHAREREQUEST']._serialized_end=3763
  _globals['_UPDATERECEIVEDOCMSHARERESPONSE']._serialized_start=3766
  _globals['_UPDATERECEIVEDOCMSHARERESPONSE']._serialized_end=3898
  _globals['_GETRECEIVEDOCMSHAREREQUEST']._serialized_start=3901
  _globals['_GETRECEIVEDOCMSHAREREQUEST']._serialized_end=4039
  _globals['_GETRECEIVEDOCMSHARERESPONSE']._serialized_start=4042
  _globals['_GETRECEIVEDOCMSHARERESPONSE']._serialized_end=4233
  _globals['_OCMAPI']._serialized_start=4236
  _globals['_OCMAPI']._serialized_end=5342
# @@protoc_insertion_point(module_scope)
