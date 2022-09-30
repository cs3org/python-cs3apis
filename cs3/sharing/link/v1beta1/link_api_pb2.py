# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/sharing/link/v1beta1/link_api.proto
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
from cs3.sharing.link.v1beta1 import resources_pb2 as cs3_dot_sharing_dot_link_dot_v1beta1_dot_resources__pb2
from cs3.storage.provider.v1beta1 import resources_pb2 as cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2
from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'cs3/sharing/link/v1beta1/link_api.proto\x12\x18\x63s3.sharing.link.v1beta1\x1a)cs3/identity/user/v1beta1/resources.proto\x1a\x1c\x63s3/rpc/v1beta1/status.proto\x1a(cs3/sharing/link/v1beta1/resources.proto\x1a,cs3/storage/provider/v1beta1/resources.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\"\xcd\x01\n\x18\x43reatePublicShareRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x41\n\rresource_info\x18\x02 \x01(\x0b\x32*.cs3.storage.provider.v1beta1.ResourceInfo\x12.\n\x05grant\x18\x03 \x01(\x0b\x32\x1f.cs3.sharing.link.v1beta1.Grant\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\"\xa5\x01\n\x19\x43reatePublicShareResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x34\n\x05share\x18\x03 \x01(\x0b\x32%.cs3.sharing.link.v1beta1.PublicShare\"\x86\x04\n\x18UpdatePublicShareRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12;\n\x03ref\x18\x02 \x01(\x0b\x32..cs3.sharing.link.v1beta1.PublicShareReference\x12I\n\x06update\x18\x03 \x01(\x0b\x32\x39.cs3.sharing.link.v1beta1.UpdatePublicShareRequest.Update\x1a\xb6\x02\n\x06Update\x12L\n\x04type\x18\x03 \x01(\x0e\x32>.cs3.sharing.link.v1beta1.UpdatePublicShareRequest.Update.Type\x12.\n\x05grant\x18\x04 \x01(\x0b\x32\x1f.cs3.sharing.link.v1beta1.Grant\x12\x14\n\x0c\x64isplay_name\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\"\x82\x01\n\x04Type\x12\x10\n\x0cTYPE_INVALID\x10\x00\x12\x14\n\x10TYPE_PERMISSIONS\x10\x01\x12\x11\n\rTYPE_PASSWORD\x10\x02\x12\x13\n\x0fTYPE_EXPIRATION\x10\x03\x12\x14\n\x10TYPE_DISPLAYNAME\x10\x04\x12\x14\n\x10TYPE_DESCRIPTION\x10\x05\"\xa5\x01\n\x19UpdatePublicShareResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x34\n\x05share\x18\x03 \x01(\x0b\x32%.cs3.sharing.link.v1beta1.PublicShare\"\xa1\x04\n\x17ListPublicSharesRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12I\n\x07\x66ilters\x18\x02 \x03(\x0b\x32\x38.cs3.sharing.link.v1beta1.ListPublicSharesRequest.Filter\x12\x0c\n\x04sign\x18\x03 \x01(\x08\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t\x1a\xda\x02\n\x06\x46ilter\x12K\n\x04type\x18\x02 \x01(\x0e\x32=.cs3.sharing.link.v1beta1.ListPublicSharesRequest.Filter.Type\x12?\n\x0bresource_id\x18\x03 \x01(\x0b\x32(.cs3.storage.provider.v1beta1.ResourceIdH\x00\x12\x32\n\x05owner\x18\x04 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserIdH\x00\x12\x34\n\x07\x63reator\x18\x05 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserIdH\x00\"P\n\x04Type\x12\x10\n\x0cTYPE_INVALID\x10\x00\x12\x14\n\x10TYPE_RESOURCE_ID\x10\x01\x12\x0e\n\nTYPE_OWNER\x10\x02\x12\x10\n\x0cTYPE_CREATOR\x10\x03\x42\x06\n\x04term\"\xbd\x01\n\x18ListPublicSharesResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x34\n\x05share\x18\x03 \x03(\x0b\x32%.cs3.sharing.link.v1beta1.PublicShare\x12\x17\n\x0fnext_page_token\x18\x04 \x01(\t\"\x82\x01\n\x18RemovePublicShareRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12;\n\x03ref\x18\x02 \x01(\x0b\x32..cs3.sharing.link.v1beta1.PublicShareReference\"o\n\x19RemovePublicShareResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\"\x8d\x01\n\x15GetPublicShareRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12;\n\x03ref\x18\x02 \x01(\x0b\x32..cs3.sharing.link.v1beta1.PublicShareReference\x12\x0c\n\x04sign\x18\x03 \x01(\x08\"\xa2\x01\n\x16GetPublicShareResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x34\n\x05share\x18\x03 \x01(\x0b\x32%.cs3.sharing.link.v1beta1.PublicShare\"\xb3\x01\n\x1cGetPublicShareByTokenRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\r\n\x05token\x18\x02 \x01(\t\x12K\n\x0e\x61uthentication\x18\x03 \x01(\x0b\x32\x33.cs3.sharing.link.v1beta1.PublicShareAuthentication\x12\x0c\n\x04sign\x18\x04 \x01(\x08\"\xc4\x01\n\x1dGetPublicShareByTokenResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x34\n\x05share\x18\x03 \x01(\x0b\x32%.cs3.sharing.link.v1beta1.PublicShare\x12\x19\n\rpassword_hash\x18\x04 \x01(\tB\x02\x18\x01\x32\xfe\x05\n\x07LinkAPI\x12|\n\x11\x43reatePublicShare\x12\x32.cs3.sharing.link.v1beta1.CreatePublicShareRequest\x1a\x33.cs3.sharing.link.v1beta1.CreatePublicShareResponse\x12|\n\x11RemovePublicShare\x12\x32.cs3.sharing.link.v1beta1.RemovePublicShareRequest\x1a\x33.cs3.sharing.link.v1beta1.RemovePublicShareResponse\x12s\n\x0eGetPublicShare\x12/.cs3.sharing.link.v1beta1.GetPublicShareRequest\x1a\x30.cs3.sharing.link.v1beta1.GetPublicShareResponse\x12\x88\x01\n\x15GetPublicShareByToken\x12\x36.cs3.sharing.link.v1beta1.GetPublicShareByTokenRequest\x1a\x37.cs3.sharing.link.v1beta1.GetPublicShareByTokenResponse\x12y\n\x10ListPublicShares\x12\x31.cs3.sharing.link.v1beta1.ListPublicSharesRequest\x1a\x32.cs3.sharing.link.v1beta1.ListPublicSharesResponse\x12|\n\x11UpdatePublicShare\x12\x32.cs3.sharing.link.v1beta1.UpdatePublicShareRequest\x1a\x33.cs3.sharing.link.v1beta1.UpdatePublicShareResponseBw\n\x1c\x63om.cs3.sharing.link.v1beta1B\x0cLinkApiProtoP\x01Z\x0blinkv1beta1\xa2\x02\x03\x43SL\xaa\x02\x18\x43s3.Sharing.Link.V1Beta1\xca\x02\x18\x43s3\\Sharing\\Link\\V1Beta1b\x06proto3')



_CREATEPUBLICSHAREREQUEST = DESCRIPTOR.message_types_by_name['CreatePublicShareRequest']
_CREATEPUBLICSHARERESPONSE = DESCRIPTOR.message_types_by_name['CreatePublicShareResponse']
_UPDATEPUBLICSHAREREQUEST = DESCRIPTOR.message_types_by_name['UpdatePublicShareRequest']
_UPDATEPUBLICSHAREREQUEST_UPDATE = _UPDATEPUBLICSHAREREQUEST.nested_types_by_name['Update']
_UPDATEPUBLICSHARERESPONSE = DESCRIPTOR.message_types_by_name['UpdatePublicShareResponse']
_LISTPUBLICSHARESREQUEST = DESCRIPTOR.message_types_by_name['ListPublicSharesRequest']
_LISTPUBLICSHARESREQUEST_FILTER = _LISTPUBLICSHARESREQUEST.nested_types_by_name['Filter']
_LISTPUBLICSHARESRESPONSE = DESCRIPTOR.message_types_by_name['ListPublicSharesResponse']
_REMOVEPUBLICSHAREREQUEST = DESCRIPTOR.message_types_by_name['RemovePublicShareRequest']
_REMOVEPUBLICSHARERESPONSE = DESCRIPTOR.message_types_by_name['RemovePublicShareResponse']
_GETPUBLICSHAREREQUEST = DESCRIPTOR.message_types_by_name['GetPublicShareRequest']
_GETPUBLICSHARERESPONSE = DESCRIPTOR.message_types_by_name['GetPublicShareResponse']
_GETPUBLICSHAREBYTOKENREQUEST = DESCRIPTOR.message_types_by_name['GetPublicShareByTokenRequest']
_GETPUBLICSHAREBYTOKENRESPONSE = DESCRIPTOR.message_types_by_name['GetPublicShareByTokenResponse']
_UPDATEPUBLICSHAREREQUEST_UPDATE_TYPE = _UPDATEPUBLICSHAREREQUEST_UPDATE.enum_types_by_name['Type']
_LISTPUBLICSHARESREQUEST_FILTER_TYPE = _LISTPUBLICSHARESREQUEST_FILTER.enum_types_by_name['Type']
CreatePublicShareRequest = _reflection.GeneratedProtocolMessageType('CreatePublicShareRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPUBLICSHAREREQUEST,
  '__module__' : 'cs3.sharing.link.v1beta1.link_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.link.v1beta1.CreatePublicShareRequest)
  })
_sym_db.RegisterMessage(CreatePublicShareRequest)

CreatePublicShareResponse = _reflection.GeneratedProtocolMessageType('CreatePublicShareResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEPUBLICSHARERESPONSE,
  '__module__' : 'cs3.sharing.link.v1beta1.link_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.link.v1beta1.CreatePublicShareResponse)
  })
_sym_db.RegisterMessage(CreatePublicShareResponse)

UpdatePublicShareRequest = _reflection.GeneratedProtocolMessageType('UpdatePublicShareRequest', (_message.Message,), {

  'Update' : _reflection.GeneratedProtocolMessageType('Update', (_message.Message,), {
    'DESCRIPTOR' : _UPDATEPUBLICSHAREREQUEST_UPDATE,
    '__module__' : 'cs3.sharing.link.v1beta1.link_api_pb2'
    # @@protoc_insertion_point(class_scope:cs3.sharing.link.v1beta1.UpdatePublicShareRequest.Update)
    })
  ,
  'DESCRIPTOR' : _UPDATEPUBLICSHAREREQUEST,
  '__module__' : 'cs3.sharing.link.v1beta1.link_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.link.v1beta1.UpdatePublicShareRequest)
  })
_sym_db.RegisterMessage(UpdatePublicShareRequest)
_sym_db.RegisterMessage(UpdatePublicShareRequest.Update)

UpdatePublicShareResponse = _reflection.GeneratedProtocolMessageType('UpdatePublicShareResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPUBLICSHARERESPONSE,
  '__module__' : 'cs3.sharing.link.v1beta1.link_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.link.v1beta1.UpdatePublicShareResponse)
  })
_sym_db.RegisterMessage(UpdatePublicShareResponse)

ListPublicSharesRequest = _reflection.GeneratedProtocolMessageType('ListPublicSharesRequest', (_message.Message,), {

  'Filter' : _reflection.GeneratedProtocolMessageType('Filter', (_message.Message,), {
    'DESCRIPTOR' : _LISTPUBLICSHARESREQUEST_FILTER,
    '__module__' : 'cs3.sharing.link.v1beta1.link_api_pb2'
    # @@protoc_insertion_point(class_scope:cs3.sharing.link.v1beta1.ListPublicSharesRequest.Filter)
    })
  ,
  'DESCRIPTOR' : _LISTPUBLICSHARESREQUEST,
  '__module__' : 'cs3.sharing.link.v1beta1.link_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.link.v1beta1.ListPublicSharesRequest)
  })
_sym_db.RegisterMessage(ListPublicSharesRequest)
_sym_db.RegisterMessage(ListPublicSharesRequest.Filter)

ListPublicSharesResponse = _reflection.GeneratedProtocolMessageType('ListPublicSharesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPUBLICSHARESRESPONSE,
  '__module__' : 'cs3.sharing.link.v1beta1.link_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.link.v1beta1.ListPublicSharesResponse)
  })
_sym_db.RegisterMessage(ListPublicSharesResponse)

RemovePublicShareRequest = _reflection.GeneratedProtocolMessageType('RemovePublicShareRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEPUBLICSHAREREQUEST,
  '__module__' : 'cs3.sharing.link.v1beta1.link_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.link.v1beta1.RemovePublicShareRequest)
  })
_sym_db.RegisterMessage(RemovePublicShareRequest)

RemovePublicShareResponse = _reflection.GeneratedProtocolMessageType('RemovePublicShareResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVEPUBLICSHARERESPONSE,
  '__module__' : 'cs3.sharing.link.v1beta1.link_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.link.v1beta1.RemovePublicShareResponse)
  })
_sym_db.RegisterMessage(RemovePublicShareResponse)

GetPublicShareRequest = _reflection.GeneratedProtocolMessageType('GetPublicShareRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPUBLICSHAREREQUEST,
  '__module__' : 'cs3.sharing.link.v1beta1.link_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.link.v1beta1.GetPublicShareRequest)
  })
_sym_db.RegisterMessage(GetPublicShareRequest)

GetPublicShareResponse = _reflection.GeneratedProtocolMessageType('GetPublicShareResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPUBLICSHARERESPONSE,
  '__module__' : 'cs3.sharing.link.v1beta1.link_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.link.v1beta1.GetPublicShareResponse)
  })
_sym_db.RegisterMessage(GetPublicShareResponse)

GetPublicShareByTokenRequest = _reflection.GeneratedProtocolMessageType('GetPublicShareByTokenRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPUBLICSHAREBYTOKENREQUEST,
  '__module__' : 'cs3.sharing.link.v1beta1.link_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.link.v1beta1.GetPublicShareByTokenRequest)
  })
_sym_db.RegisterMessage(GetPublicShareByTokenRequest)

GetPublicShareByTokenResponse = _reflection.GeneratedProtocolMessageType('GetPublicShareByTokenResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPUBLICSHAREBYTOKENRESPONSE,
  '__module__' : 'cs3.sharing.link.v1beta1.link_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.sharing.link.v1beta1.GetPublicShareByTokenResponse)
  })
_sym_db.RegisterMessage(GetPublicShareByTokenResponse)

_LINKAPI = DESCRIPTOR.services_by_name['LinkAPI']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.cs3.sharing.link.v1beta1B\014LinkApiProtoP\001Z\013linkv1beta1\242\002\003CSL\252\002\030Cs3.Sharing.Link.V1Beta1\312\002\030Cs3\\Sharing\\Link\\V1Beta1'
  _GETPUBLICSHAREBYTOKENRESPONSE.fields_by_name['password_hash']._options = None
  _GETPUBLICSHAREBYTOKENRESPONSE.fields_by_name['password_hash']._serialized_options = b'\030\001'
  _CREATEPUBLICSHAREREQUEST._serialized_start=262
  _CREATEPUBLICSHAREREQUEST._serialized_end=467
  _CREATEPUBLICSHARERESPONSE._serialized_start=470
  _CREATEPUBLICSHARERESPONSE._serialized_end=635
  _UPDATEPUBLICSHAREREQUEST._serialized_start=638
  _UPDATEPUBLICSHAREREQUEST._serialized_end=1156
  _UPDATEPUBLICSHAREREQUEST_UPDATE._serialized_start=846
  _UPDATEPUBLICSHAREREQUEST_UPDATE._serialized_end=1156
  _UPDATEPUBLICSHAREREQUEST_UPDATE_TYPE._serialized_start=1026
  _UPDATEPUBLICSHAREREQUEST_UPDATE_TYPE._serialized_end=1156
  _UPDATEPUBLICSHARERESPONSE._serialized_start=1159
  _UPDATEPUBLICSHARERESPONSE._serialized_end=1324
  _LISTPUBLICSHARESREQUEST._serialized_start=1327
  _LISTPUBLICSHARESREQUEST._serialized_end=1872
  _LISTPUBLICSHARESREQUEST_FILTER._serialized_start=1526
  _LISTPUBLICSHARESREQUEST_FILTER._serialized_end=1872
  _LISTPUBLICSHARESREQUEST_FILTER_TYPE._serialized_start=1784
  _LISTPUBLICSHARESREQUEST_FILTER_TYPE._serialized_end=1864
  _LISTPUBLICSHARESRESPONSE._serialized_start=1875
  _LISTPUBLICSHARESRESPONSE._serialized_end=2064
  _REMOVEPUBLICSHAREREQUEST._serialized_start=2067
  _REMOVEPUBLICSHAREREQUEST._serialized_end=2197
  _REMOVEPUBLICSHARERESPONSE._serialized_start=2199
  _REMOVEPUBLICSHARERESPONSE._serialized_end=2310
  _GETPUBLICSHAREREQUEST._serialized_start=2313
  _GETPUBLICSHAREREQUEST._serialized_end=2454
  _GETPUBLICSHARERESPONSE._serialized_start=2457
  _GETPUBLICSHARERESPONSE._serialized_end=2619
  _GETPUBLICSHAREBYTOKENREQUEST._serialized_start=2622
  _GETPUBLICSHAREBYTOKENREQUEST._serialized_end=2801
  _GETPUBLICSHAREBYTOKENRESPONSE._serialized_start=2804
  _GETPUBLICSHAREBYTOKENRESPONSE._serialized_end=3000
  _LINKAPI._serialized_start=3003
  _LINKAPI._serialized_end=3769
# @@protoc_insertion_point(module_scope)
