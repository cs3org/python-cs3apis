# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/storage/provider/v1beta1/resources.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.identity.group.v1beta1 import resources_pb2 as cs3_dot_identity_dot_group_dot_v1beta1_dot_resources__pb2
from cs3.identity.user.v1beta1 import resources_pb2 as cs3_dot_identity_dot_user_dot_v1beta1_dot_resources__pb2
from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,cs3/storage/provider/v1beta1/resources.proto\x12\x1c\x63s3.storage.provider.v1beta1\x1a*cs3/identity/group/v1beta1/resources.proto\x1a)cs3/identity/user/v1beta1/resources.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\"\xea\x05\n\x0cResourceInfo\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x38\n\x04type\x18\x02 \x01(\x0e\x32*.cs3.storage.provider.v1beta1.ResourceType\x12\x34\n\x02id\x18\x03 \x01(\x0b\x32(.cs3.storage.provider.v1beta1.ResourceId\x12@\n\x08\x63hecksum\x18\x04 \x01(\x0b\x32..cs3.storage.provider.v1beta1.ResourceChecksum\x12\x0c\n\x04\x65tag\x18\x05 \x01(\t\x12\x11\n\tmime_type\x18\x06 \x01(\t\x12+\n\x05mtime\x18\x07 \x01(\x0b\x32\x1c.cs3.types.v1beta1.Timestamp\x12\x0c\n\x04path\x18\x08 \x01(\t\x12I\n\x0epermission_set\x18\t \x01(\x0b\x32\x31.cs3.storage.provider.v1beta1.ResourcePermissions\x12\x0c\n\x04size\x18\n \x01(\x04\x12\x30\n\x05owner\x18\x0b \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserId\x12\x0e\n\x06target\x18\x0c \x01(\t\x12K\n\x12\x63\x61nonical_metadata\x18\r \x01(\x0b\x32/.cs3.storage.provider.v1beta1.CanonicalMetadata\x12K\n\x12\x61rbitrary_metadata\x18\x0e \x01(\x0b\x32/.cs3.storage.provider.v1beta1.ArbitraryMetadata\x12\x30\n\x04lock\x18\x0f \x01(\x0b\x32\".cs3.storage.provider.v1beta1.Lock\x12:\n\x0e\x61\x64visory_locks\x18\x10 \x03(\x0b\x32\".cs3.storage.provider.v1beta1.Lock\"L\n\x11\x43\x61nonicalMetadata\x12\x37\n\x06target\x18\x01 \x01(\x0b\x32\'.cs3.storage.provider.v1beta1.Reference\"\x95\x01\n\x11\x41rbitraryMetadata\x12O\n\x08metadata\x18\x01 \x03(\x0b\x32=.cs3.storage.provider.v1beta1.ArbitraryMetadata.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xed\x01\n\x04Lock\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x0f\n\x07lock_id\x18\x02 \x01(\t\x12\x34\n\x04type\x18\x03 \x01(\x0e\x32&.cs3.storage.provider.v1beta1.LockType\x12/\n\x04user\x18\x04 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserId\x12\x10\n\x08\x61pp_name\x18\x05 \x01(\t\x12\x30\n\nexpiration\x18\x06 \x01(\x0b\x32\x1c.cs3.types.v1beta1.Timestamp\"a\n\x10ResourceChecksum\x12@\n\x04type\x18\x01 \x01(\x0e\x32\x32.cs3.storage.provider.v1beta1.ResourceChecksumType\x12\x0b\n\x03sum\x18\x02 \x01(\t\"n\n\x18ResourceChecksumPriority\x12@\n\x04type\x18\x01 \x01(\x0e\x32\x32.cs3.storage.provider.v1beta1.ResourceChecksumType\x12\x10\n\x08priority\x18\x02 \x01(\r\"X\n\tReference\x12=\n\x0bresource_id\x18\x01 \x01(\x0b\x32(.cs3.storage.provider.v1beta1.ResourceId\x12\x0c\n\x04path\x18\x02 \x01(\t\"3\n\nResourceId\x12\x12\n\nstorage_id\x18\x01 \x01(\t\x12\x11\n\topaque_id\x18\x02 \x01(\t\"\xc3\x03\n\x13ResourcePermissions\x12\x11\n\tadd_grant\x18\x01 \x01(\x08\x12\x18\n\x10\x63reate_container\x18\x02 \x01(\x08\x12\x0e\n\x06\x64\x65lete\x18\x03 \x01(\x08\x12\x10\n\x08get_path\x18\x05 \x01(\x08\x12\x11\n\tget_quota\x18\x06 \x01(\x08\x12\x1e\n\x16initiate_file_download\x18\x07 \x01(\x08\x12\x1c\n\x14initiate_file_upload\x18\x08 \x01(\x08\x12\x13\n\x0blist_grants\x18\t \x01(\x08\x12\x16\n\x0elist_container\x18\n \x01(\x08\x12\x1a\n\x12list_file_versions\x18\x0b \x01(\x08\x12\x14\n\x0clist_recycle\x18\x0c \x01(\x08\x12\x0c\n\x04move\x18\r \x01(\x08\x12\x14\n\x0cremove_grant\x18\x0e \x01(\x08\x12\x15\n\rpurge_recycle\x18\x0f \x01(\x08\x12\x1c\n\x14restore_file_version\x18\x10 \x01(\x08\x12\x1c\n\x14restore_recycle_item\x18\x11 \x01(\x08\x12\x0c\n\x04stat\x18\x12 \x01(\x08\x12\x14\n\x0cupdate_grant\x18\x13 \x01(\x08\x12\x12\n\ndeny_grant\x18\x14 \x01(\x08\"\x87\x01\n\x05Grant\x12\x36\n\x07grantee\x18\x01 \x01(\x0b\x32%.cs3.storage.provider.v1beta1.Grantee\x12\x46\n\x0bpermissions\x18\x02 \x01(\x0b\x32\x31.cs3.storage.provider.v1beta1.ResourcePermissions\"\xe2\x01\n\x07Grantee\x12\x37\n\x04type\x18\x01 \x01(\x0e\x32).cs3.storage.provider.v1beta1.GranteeType\x12\x34\n\x07user_id\x18\x03 \x01(\x0b\x32!.cs3.identity.user.v1beta1.UserIdH\x00\x12\x37\n\x08group_id\x18\x04 \x01(\x0b\x32#.cs3.identity.group.v1beta1.GroupIdH\x00\x12)\n\x06opaque\x18\x05 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueB\x04\n\x02id\"p\n\x0b\x46ileVersion\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\x0c\n\x04size\x18\x04 \x01(\x04\x12\r\n\x05mtime\x18\x05 \x01(\x04\x12\x0c\n\x04\x65tag\x18\x06 \x01(\t\"\xf8\x01\n\x0bRecycleItem\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x38\n\x04type\x18\x02 \x01(\x0e\x32*.cs3.storage.provider.v1beta1.ResourceType\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\x34\n\x03ref\x18\x04 \x01(\x0b\x32\'.cs3.storage.provider.v1beta1.Reference\x12\x0c\n\x04size\x18\x05 \x01(\x04\x12\x33\n\rdeletion_time\x18\x06 \x01(\x0b\x32\x1c.cs3.types.v1beta1.Timestamp\"\xcf\x01\n\x12\x46ileUploadProtocol\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x10\n\x08protocol\x18\x02 \x01(\t\x12\x17\n\x0fupload_endpoint\x18\x03 \x01(\t\x12S\n\x13\x61vailable_checksums\x18\x04 \x03(\x0b\x32\x36.cs3.storage.provider.v1beta1.ResourceChecksumPriority\x12\x0e\n\x06\x65xpose\x18\x05 \x01(\x08\"~\n\x14\x46ileDownloadProtocol\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x10\n\x08protocol\x18\x02 \x01(\t\x12\x19\n\x11\x64ownload_endpoint\x18\x03 \x01(\t\x12\x0e\n\x06\x65xpose\x18\x04 \x01(\x08\"\xde\x02\n\x0cStorageSpace\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x38\n\x02id\x18\x02 \x01(\x0b\x32,.cs3.storage.provider.v1beta1.StorageSpaceId\x12.\n\x05owner\x18\x03 \x01(\x0b\x32\x1f.cs3.identity.user.v1beta1.User\x12\x36\n\x04root\x18\x04 \x01(\x0b\x32(.cs3.storage.provider.v1beta1.ResourceId\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x32\n\x05quota\x18\x06 \x01(\x0b\x32#.cs3.storage.provider.v1beta1.Quota\x12\x12\n\nspace_type\x18\x07 \x01(\t\x12+\n\x05mtime\x18\x08 \x01(\x0b\x32\x1c.cs3.types.v1beta1.Timestamp\"#\n\x0eStorageSpaceId\x12\x11\n\topaque_id\x18\x01 \x01(\t\"d\n\x05Quota\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x17\n\x0fquota_max_bytes\x18\x02 \x01(\x04\x12\x17\n\x0fquota_max_files\x18\x03 \x01(\x04*`\n\x08LockType\x12\x15\n\x11LOCK_TYPE_INVALID\x10\x00\x12\x14\n\x10LOCK_TYPE_SHARED\x10\x01\x12\x13\n\x0fLOCK_TYPE_WRITE\x10\x02\x12\x12\n\x0eLOCK_TYPE_EXCL\x10\x03*\xb2\x01\n\x0cResourceType\x12\x19\n\x15RESOURCE_TYPE_INVALID\x10\x00\x12\x16\n\x12RESOURCE_TYPE_FILE\x10\x01\x12\x1b\n\x17RESOURCE_TYPE_CONTAINER\x10\x02\x12\x1b\n\x17RESOURCE_TYPE_REFERENCE\x10\x03\x12\x19\n\x15RESOURCE_TYPE_SYMLINK\x10\x04\x12\x1a\n\x16RESOURCE_TYPE_INTERNAL\x10\x05*\xc1\x01\n\x14ResourceChecksumType\x12\"\n\x1eRESOURCE_CHECKSUM_TYPE_INVALID\x10\x00\x12 \n\x1cRESOURCE_CHECKSUM_TYPE_UNSET\x10\x01\x12\"\n\x1eRESOURCE_CHECKSUM_TYPE_ADLER32\x10\x02\x12\x1e\n\x1aRESOURCE_CHECKSUM_TYPE_MD5\x10\x03\x12\x1f\n\x1bRESOURCE_CHECKSUM_TYPE_SHA1\x10\x04*V\n\x0bGranteeType\x12\x18\n\x14GRANTEE_TYPE_INVALID\x10\x00\x12\x15\n\x11GRANTEE_TYPE_USER\x10\x01\x12\x16\n\x12GRANTEE_TYPE_GROUP\x10\x02\x42\x89\x01\n com.cs3.storage.provider.v1beta1B\x0eResourcesProtoP\x01Z\x0fproviderv1beta1\xa2\x02\x03\x43SP\xaa\x02\x1c\x43s3.Storage.Provider.V1Beta1\xca\x02\x1c\x43s3\\Storage\\Provider\\V1Beta1b\x06proto3')

_LOCKTYPE = DESCRIPTOR.enum_types_by_name['LockType']
LockType = enum_type_wrapper.EnumTypeWrapper(_LOCKTYPE)
_RESOURCETYPE = DESCRIPTOR.enum_types_by_name['ResourceType']
ResourceType = enum_type_wrapper.EnumTypeWrapper(_RESOURCETYPE)
_RESOURCECHECKSUMTYPE = DESCRIPTOR.enum_types_by_name['ResourceChecksumType']
ResourceChecksumType = enum_type_wrapper.EnumTypeWrapper(_RESOURCECHECKSUMTYPE)
_GRANTEETYPE = DESCRIPTOR.enum_types_by_name['GranteeType']
GranteeType = enum_type_wrapper.EnumTypeWrapper(_GRANTEETYPE)
LOCK_TYPE_INVALID = 0
LOCK_TYPE_SHARED = 1
LOCK_TYPE_WRITE = 2
LOCK_TYPE_EXCL = 3
RESOURCE_TYPE_INVALID = 0
RESOURCE_TYPE_FILE = 1
RESOURCE_TYPE_CONTAINER = 2
RESOURCE_TYPE_REFERENCE = 3
RESOURCE_TYPE_SYMLINK = 4
RESOURCE_TYPE_INTERNAL = 5
RESOURCE_CHECKSUM_TYPE_INVALID = 0
RESOURCE_CHECKSUM_TYPE_UNSET = 1
RESOURCE_CHECKSUM_TYPE_ADLER32 = 2
RESOURCE_CHECKSUM_TYPE_MD5 = 3
RESOURCE_CHECKSUM_TYPE_SHA1 = 4
GRANTEE_TYPE_INVALID = 0
GRANTEE_TYPE_USER = 1
GRANTEE_TYPE_GROUP = 2


_RESOURCEINFO = DESCRIPTOR.message_types_by_name['ResourceInfo']
_CANONICALMETADATA = DESCRIPTOR.message_types_by_name['CanonicalMetadata']
_ARBITRARYMETADATA = DESCRIPTOR.message_types_by_name['ArbitraryMetadata']
_ARBITRARYMETADATA_METADATAENTRY = _ARBITRARYMETADATA.nested_types_by_name['MetadataEntry']
_LOCK = DESCRIPTOR.message_types_by_name['Lock']
_RESOURCECHECKSUM = DESCRIPTOR.message_types_by_name['ResourceChecksum']
_RESOURCECHECKSUMPRIORITY = DESCRIPTOR.message_types_by_name['ResourceChecksumPriority']
_REFERENCE = DESCRIPTOR.message_types_by_name['Reference']
_RESOURCEID = DESCRIPTOR.message_types_by_name['ResourceId']
_RESOURCEPERMISSIONS = DESCRIPTOR.message_types_by_name['ResourcePermissions']
_GRANT = DESCRIPTOR.message_types_by_name['Grant']
_GRANTEE = DESCRIPTOR.message_types_by_name['Grantee']
_FILEVERSION = DESCRIPTOR.message_types_by_name['FileVersion']
_RECYCLEITEM = DESCRIPTOR.message_types_by_name['RecycleItem']
_FILEUPLOADPROTOCOL = DESCRIPTOR.message_types_by_name['FileUploadProtocol']
_FILEDOWNLOADPROTOCOL = DESCRIPTOR.message_types_by_name['FileDownloadProtocol']
_STORAGESPACE = DESCRIPTOR.message_types_by_name['StorageSpace']
_STORAGESPACEID = DESCRIPTOR.message_types_by_name['StorageSpaceId']
_QUOTA = DESCRIPTOR.message_types_by_name['Quota']
ResourceInfo = _reflection.GeneratedProtocolMessageType('ResourceInfo', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEINFO,
  '__module__' : 'cs3.storage.provider.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.storage.provider.v1beta1.ResourceInfo)
  })
_sym_db.RegisterMessage(ResourceInfo)

CanonicalMetadata = _reflection.GeneratedProtocolMessageType('CanonicalMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CANONICALMETADATA,
  '__module__' : 'cs3.storage.provider.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.storage.provider.v1beta1.CanonicalMetadata)
  })
_sym_db.RegisterMessage(CanonicalMetadata)

ArbitraryMetadata = _reflection.GeneratedProtocolMessageType('ArbitraryMetadata', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _ARBITRARYMETADATA_METADATAENTRY,
    '__module__' : 'cs3.storage.provider.v1beta1.resources_pb2'
    # @@protoc_insertion_point(class_scope:cs3.storage.provider.v1beta1.ArbitraryMetadata.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _ARBITRARYMETADATA,
  '__module__' : 'cs3.storage.provider.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.storage.provider.v1beta1.ArbitraryMetadata)
  })
_sym_db.RegisterMessage(ArbitraryMetadata)
_sym_db.RegisterMessage(ArbitraryMetadata.MetadataEntry)

Lock = _reflection.GeneratedProtocolMessageType('Lock', (_message.Message,), {
  'DESCRIPTOR' : _LOCK,
  '__module__' : 'cs3.storage.provider.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.storage.provider.v1beta1.Lock)
  })
_sym_db.RegisterMessage(Lock)

ResourceChecksum = _reflection.GeneratedProtocolMessageType('ResourceChecksum', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCECHECKSUM,
  '__module__' : 'cs3.storage.provider.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.storage.provider.v1beta1.ResourceChecksum)
  })
_sym_db.RegisterMessage(ResourceChecksum)

ResourceChecksumPriority = _reflection.GeneratedProtocolMessageType('ResourceChecksumPriority', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCECHECKSUMPRIORITY,
  '__module__' : 'cs3.storage.provider.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.storage.provider.v1beta1.ResourceChecksumPriority)
  })
_sym_db.RegisterMessage(ResourceChecksumPriority)

Reference = _reflection.GeneratedProtocolMessageType('Reference', (_message.Message,), {
  'DESCRIPTOR' : _REFERENCE,
  '__module__' : 'cs3.storage.provider.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.storage.provider.v1beta1.Reference)
  })
_sym_db.RegisterMessage(Reference)

ResourceId = _reflection.GeneratedProtocolMessageType('ResourceId', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEID,
  '__module__' : 'cs3.storage.provider.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.storage.provider.v1beta1.ResourceId)
  })
_sym_db.RegisterMessage(ResourceId)

ResourcePermissions = _reflection.GeneratedProtocolMessageType('ResourcePermissions', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEPERMISSIONS,
  '__module__' : 'cs3.storage.provider.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.storage.provider.v1beta1.ResourcePermissions)
  })
_sym_db.RegisterMessage(ResourcePermissions)

Grant = _reflection.GeneratedProtocolMessageType('Grant', (_message.Message,), {
  'DESCRIPTOR' : _GRANT,
  '__module__' : 'cs3.storage.provider.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.storage.provider.v1beta1.Grant)
  })
_sym_db.RegisterMessage(Grant)

Grantee = _reflection.GeneratedProtocolMessageType('Grantee', (_message.Message,), {
  'DESCRIPTOR' : _GRANTEE,
  '__module__' : 'cs3.storage.provider.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.storage.provider.v1beta1.Grantee)
  })
_sym_db.RegisterMessage(Grantee)

FileVersion = _reflection.GeneratedProtocolMessageType('FileVersion', (_message.Message,), {
  'DESCRIPTOR' : _FILEVERSION,
  '__module__' : 'cs3.storage.provider.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.storage.provider.v1beta1.FileVersion)
  })
_sym_db.RegisterMessage(FileVersion)

RecycleItem = _reflection.GeneratedProtocolMessageType('RecycleItem', (_message.Message,), {
  'DESCRIPTOR' : _RECYCLEITEM,
  '__module__' : 'cs3.storage.provider.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.storage.provider.v1beta1.RecycleItem)
  })
_sym_db.RegisterMessage(RecycleItem)

FileUploadProtocol = _reflection.GeneratedProtocolMessageType('FileUploadProtocol', (_message.Message,), {
  'DESCRIPTOR' : _FILEUPLOADPROTOCOL,
  '__module__' : 'cs3.storage.provider.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.storage.provider.v1beta1.FileUploadProtocol)
  })
_sym_db.RegisterMessage(FileUploadProtocol)

FileDownloadProtocol = _reflection.GeneratedProtocolMessageType('FileDownloadProtocol', (_message.Message,), {
  'DESCRIPTOR' : _FILEDOWNLOADPROTOCOL,
  '__module__' : 'cs3.storage.provider.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.storage.provider.v1beta1.FileDownloadProtocol)
  })
_sym_db.RegisterMessage(FileDownloadProtocol)

StorageSpace = _reflection.GeneratedProtocolMessageType('StorageSpace', (_message.Message,), {
  'DESCRIPTOR' : _STORAGESPACE,
  '__module__' : 'cs3.storage.provider.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.storage.provider.v1beta1.StorageSpace)
  })
_sym_db.RegisterMessage(StorageSpace)

StorageSpaceId = _reflection.GeneratedProtocolMessageType('StorageSpaceId', (_message.Message,), {
  'DESCRIPTOR' : _STORAGESPACEID,
  '__module__' : 'cs3.storage.provider.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.storage.provider.v1beta1.StorageSpaceId)
  })
_sym_db.RegisterMessage(StorageSpaceId)

Quota = _reflection.GeneratedProtocolMessageType('Quota', (_message.Message,), {
  'DESCRIPTOR' : _QUOTA,
  '__module__' : 'cs3.storage.provider.v1beta1.resources_pb2'
  # @@protoc_insertion_point(class_scope:cs3.storage.provider.v1beta1.Quota)
  })
_sym_db.RegisterMessage(Quota)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n com.cs3.storage.provider.v1beta1B\016ResourcesProtoP\001Z\017providerv1beta1\242\002\003CSP\252\002\034Cs3.Storage.Provider.V1Beta1\312\002\034Cs3\\Storage\\Provider\\V1Beta1'
  _ARBITRARYMETADATA_METADATAENTRY._options = None
  _ARBITRARYMETADATA_METADATAENTRY._serialized_options = b'8\001'
  _LOCKTYPE._serialized_start=3785
  _LOCKTYPE._serialized_end=3881
  _RESOURCETYPE._serialized_start=3884
  _RESOURCETYPE._serialized_end=4062
  _RESOURCECHECKSUMTYPE._serialized_start=4065
  _RESOURCECHECKSUMTYPE._serialized_end=4258
  _GRANTEETYPE._serialized_start=4260
  _GRANTEETYPE._serialized_end=4346
  _RESOURCEINFO._serialized_start=197
  _RESOURCEINFO._serialized_end=943
  _CANONICALMETADATA._serialized_start=945
  _CANONICALMETADATA._serialized_end=1021
  _ARBITRARYMETADATA._serialized_start=1024
  _ARBITRARYMETADATA._serialized_end=1173
  _ARBITRARYMETADATA_METADATAENTRY._serialized_start=1126
  _ARBITRARYMETADATA_METADATAENTRY._serialized_end=1173
  _LOCK._serialized_start=1176
  _LOCK._serialized_end=1413
  _RESOURCECHECKSUM._serialized_start=1415
  _RESOURCECHECKSUM._serialized_end=1512
  _RESOURCECHECKSUMPRIORITY._serialized_start=1514
  _RESOURCECHECKSUMPRIORITY._serialized_end=1624
  _REFERENCE._serialized_start=1626
  _REFERENCE._serialized_end=1714
  _RESOURCEID._serialized_start=1716
  _RESOURCEID._serialized_end=1767
  _RESOURCEPERMISSIONS._serialized_start=1770
  _RESOURCEPERMISSIONS._serialized_end=2221
  _GRANT._serialized_start=2224
  _GRANT._serialized_end=2359
  _GRANTEE._serialized_start=2362
  _GRANTEE._serialized_end=2588
  _FILEVERSION._serialized_start=2590
  _FILEVERSION._serialized_end=2702
  _RECYCLEITEM._serialized_start=2705
  _RECYCLEITEM._serialized_end=2953
  _FILEUPLOADPROTOCOL._serialized_start=2956
  _FILEUPLOADPROTOCOL._serialized_end=3163
  _FILEDOWNLOADPROTOCOL._serialized_start=3165
  _FILEDOWNLOADPROTOCOL._serialized_end=3291
  _STORAGESPACE._serialized_start=3294
  _STORAGESPACE._serialized_end=3644
  _STORAGESPACEID._serialized_start=3646
  _STORAGESPACEID._serialized_end=3681
  _QUOTA._serialized_start=3683
  _QUOTA._serialized_end=3783
# @@protoc_insertion_point(module_scope)
