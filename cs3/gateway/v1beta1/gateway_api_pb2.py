# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/gateway/v1beta1/gateway_api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.app.provider.v1beta1 import provider_api_pb2 as cs3_dot_app_dot_provider_dot_v1beta1_dot_provider__api__pb2
from cs3.app.registry.v1beta1 import registry_api_pb2 as cs3_dot_app_dot_registry_dot_v1beta1_dot_registry__api__pb2
from cs3.auth.applications.v1beta1 import applications_api_pb2 as cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2
from cs3.auth.registry.v1beta1 import registry_api_pb2 as cs3_dot_auth_dot_registry_dot_v1beta1_dot_registry__api__pb2
from cs3.gateway.v1beta1 import resources_pb2 as cs3_dot_gateway_dot_v1beta1_dot_resources__pb2
from cs3.identity.group.v1beta1 import group_api_pb2 as cs3_dot_identity_dot_group_dot_v1beta1_dot_group__api__pb2
from cs3.identity.user.v1beta1 import resources_pb2 as cs3_dot_identity_dot_user_dot_v1beta1_dot_resources__pb2
from cs3.identity.user.v1beta1 import user_api_pb2 as cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2
from cs3.ocm.core.v1beta1 import ocm_core_api_pb2 as cs3_dot_ocm_dot_core_dot_v1beta1_dot_ocm__core__api__pb2
from cs3.ocm.invite.v1beta1 import invite_api_pb2 as cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2
from cs3.ocm.provider.v1beta1 import provider_api_pb2 as cs3_dot_ocm_dot_provider_dot_v1beta1_dot_provider__api__pb2
from cs3.permissions.v1beta1 import permissions_api_pb2 as cs3_dot_permissions_dot_v1beta1_dot_permissions__api__pb2
from cs3.preferences.v1beta1 import preferences_api_pb2 as cs3_dot_preferences_dot_v1beta1_dot_preferences__api__pb2
from cs3.rpc.v1beta1 import status_pb2 as cs3_dot_rpc_dot_v1beta1_dot_status__pb2
from cs3.sharing.collaboration.v1beta1 import collaboration_api_pb2 as cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2
from cs3.sharing.link.v1beta1 import link_api_pb2 as cs3_dot_sharing_dot_link_dot_v1beta1_dot_link__api__pb2
from cs3.sharing.ocm.v1beta1 import ocm_api_pb2 as cs3_dot_sharing_dot_ocm_dot_v1beta1_dot_ocm__api__pb2
from cs3.storage.provider.v1beta1 import provider_api_pb2 as cs3_dot_storage_dot_provider_dot_v1beta1_dot_provider__api__pb2
from cs3.storage.provider.v1beta1 import resources_pb2 as cs3_dot_storage_dot_provider_dot_v1beta1_dot_resources__pb2
from cs3.tx.v1beta1 import tx_api_pb2 as cs3_dot_tx_dot_v1beta1_dot_tx__api__pb2
from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%cs3/gateway/v1beta1/gateway_api.proto\x12\x13\x63s3.gateway.v1beta1\x1a+cs3/app/provider/v1beta1/provider_api.proto\x1a+cs3/app/registry/v1beta1/registry_api.proto\x1a\x34\x63s3/auth/applications/v1beta1/applications_api.proto\x1a,cs3/auth/registry/v1beta1/registry_api.proto\x1a#cs3/gateway/v1beta1/resources.proto\x1a*cs3/identity/group/v1beta1/group_api.proto\x1a)cs3/identity/user/v1beta1/resources.proto\x1a(cs3/identity/user/v1beta1/user_api.proto\x1a\'cs3/ocm/core/v1beta1/ocm_core_api.proto\x1a\'cs3/ocm/invite/v1beta1/invite_api.proto\x1a+cs3/ocm/provider/v1beta1/provider_api.proto\x1a-cs3/permissions/v1beta1/permissions_api.proto\x1a-cs3/preferences/v1beta1/preferences_api.proto\x1a\x1c\x63s3/rpc/v1beta1/status.proto\x1a\x39\x63s3/sharing/collaboration/v1beta1/collaboration_api.proto\x1a\'cs3/sharing/link/v1beta1/link_api.proto\x1a%cs3/sharing/ocm/v1beta1/ocm_api.proto\x1a/cs3/storage/provider/v1beta1/provider_api.proto\x1a,cs3/storage/provider/v1beta1/resources.proto\x1a\x1b\x63s3/tx/v1beta1/tx_api.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\"x\n\x13\x41uthenticateRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x11\n\tclient_id\x18\x03 \x01(\t\x12\x15\n\rclient_secret\x18\x04 \x01(\t\"\xa8\x01\n\x14\x41uthenticateResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\r\n\x05token\x18\x03 \x01(\t\x12-\n\x04user\x18\x04 \x01(\x0b\x32\x1f.cs3.identity.user.v1beta1.User\"I\n\rWhoAmIRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\r\n\x05token\x18\x02 \x01(\t\"\x93\x01\n\x0eWhoAmIResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12-\n\x04user\x18\x03 \x01(\x0b\x32\x1f.cs3.identity.user.v1beta1.User\"r\n\x0fGetQuotaRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x34\n\x03ref\x18\x02 \x01(\x0b\x32\'.cs3.storage.provider.v1beta1.Reference\"\xb0\x01\n\x1cInitiateFileDownloadResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12<\n\tprotocols\x18\x03 \x03(\x0b\x32).cs3.gateway.v1beta1.FileDownloadProtocol\"\xac\x01\n\x1aInitiateFileUploadResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12:\n\tprotocols\x18\x03 \x03(\x0b\x32\'.cs3.gateway.v1beta1.FileUploadProtocol\"~\n\x19ListAuthProvidersResponse\x12\'\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.Status\x12)\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\r\n\x05types\x18\x03 \x03(\t\"\xdb\x02\n\x10OpenInAppRequest\x12)\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.Opaque\x12\x34\n\x03ref\x18\x02 \x01(\x0b\x32\'.cs3.storage.provider.v1beta1.Reference\x12\x41\n\tview_mode\x18\x03 \x01(\x0e\x32..cs3.gateway.v1beta1.OpenInAppRequest.ViewMode\x12\x0b\n\x03\x61pp\x18\x04 \x01(\t\x12\x0f\n\x07lock_id\x18\x05 \x01(\t\"\x84\x01\n\x08ViewMode\x12\x15\n\x11VIEW_MODE_INVALID\x10\x00\x12\x17\n\x13VIEW_MODE_VIEW_ONLY\x10\x01\x12\x17\n\x13VIEW_MODE_READ_ONLY\x10\x02\x12\x18\n\x14VIEW_MODE_READ_WRITE\x10\x03\x12\x15\n\x11VIEW_MODE_PREVIEW\x10\x04\x32\xbd[\n\nGatewayAPI\x12\x63\n\x0c\x41uthenticate\x12(.cs3.gateway.v1beta1.AuthenticateRequest\x1a).cs3.gateway.v1beta1.AuthenticateResponse\x12Q\n\x06WhoAmI\x12\".cs3.gateway.v1beta1.WhoAmIRequest\x1a#.cs3.gateway.v1beta1.WhoAmIResponse\x12\x8c\x01\n\x13GenerateAppPassword\x12\x39.cs3.auth.applications.v1beta1.GenerateAppPasswordRequest\x1a:.cs3.auth.applications.v1beta1.GenerateAppPasswordResponse\x12\x83\x01\n\x10ListAppPasswords\x12\x36.cs3.auth.applications.v1beta1.ListAppPasswordsRequest\x1a\x37.cs3.auth.applications.v1beta1.ListAppPasswordsResponse\x12\x92\x01\n\x15InvalidateAppPassword\x12;.cs3.auth.applications.v1beta1.InvalidateAppPasswordRequest\x1a<.cs3.auth.applications.v1beta1.InvalidateAppPasswordResponse\x12}\n\x0eGetAppPassword\x12\x34.cs3.auth.applications.v1beta1.GetAppPasswordRequest\x1a\x35.cs3.auth.applications.v1beta1.GetAppPasswordResponse\x12~\n\x0f\x43reateContainer\x12\x34.cs3.storage.provider.v1beta1.CreateContainerRequest\x1a\x35.cs3.storage.provider.v1beta1.CreateContainerResponse\x12l\n\tTouchFile\x12..cs3.storage.provider.v1beta1.TouchFileRequest\x1a/.cs3.storage.provider.v1beta1.TouchFileResponse\x12\x63\n\x06\x44\x65lete\x12+.cs3.storage.provider.v1beta1.DeleteRequest\x1a,.cs3.storage.provider.v1beta1.DeleteResponse\x12\x66\n\x07GetPath\x12,.cs3.storage.provider.v1beta1.GetPathRequest\x1a-.cs3.storage.provider.v1beta1.GetPathResponse\x12`\n\x08GetQuota\x12$.cs3.gateway.v1beta1.GetQuotaRequest\x1a..cs3.storage.provider.v1beta1.GetQuotaResponse\x12\x84\x01\n\x14InitiateFileDownload\x12\x39.cs3.storage.provider.v1beta1.InitiateFileDownloadRequest\x1a\x31.cs3.gateway.v1beta1.InitiateFileDownloadResponse\x12~\n\x12InitiateFileUpload\x12\x37.cs3.storage.provider.v1beta1.InitiateFileUploadRequest\x1a/.cs3.gateway.v1beta1.InitiateFileUploadResponse\x12\x8c\x01\n\x13ListContainerStream\x12\x38.cs3.storage.provider.v1beta1.ListContainerStreamRequest\x1a\x39.cs3.storage.provider.v1beta1.ListContainerStreamResponse0\x01\x12x\n\rListContainer\x12\x32.cs3.storage.provider.v1beta1.ListContainerRequest\x1a\x33.cs3.storage.provider.v1beta1.ListContainerResponse\x12\x81\x01\n\x10ListFileVersions\x12\x35.cs3.storage.provider.v1beta1.ListFileVersionsRequest\x1a\x36.cs3.storage.provider.v1beta1.ListFileVersionsResponse\x12\x86\x01\n\x11ListRecycleStream\x12\x36.cs3.storage.provider.v1beta1.ListRecycleStreamRequest\x1a\x37.cs3.storage.provider.v1beta1.ListRecycleStreamResponse0\x01\x12r\n\x0bListRecycle\x12\x30.cs3.storage.provider.v1beta1.ListRecycleRequest\x1a\x31.cs3.storage.provider.v1beta1.ListRecycleResponse\x12]\n\x04Move\x12).cs3.storage.provider.v1beta1.MoveRequest\x1a*.cs3.storage.provider.v1beta1.MoveResponse\x12u\n\x0cPurgeRecycle\x12\x31.cs3.storage.provider.v1beta1.PurgeRecycleRequest\x1a\x32.cs3.storage.provider.v1beta1.PurgeRecycleResponse\x12\x87\x01\n\x12RestoreFileVersion\x12\x37.cs3.storage.provider.v1beta1.RestoreFileVersionRequest\x1a\x38.cs3.storage.provider.v1beta1.RestoreFileVersionResponse\x12\x87\x01\n\x12RestoreRecycleItem\x12\x37.cs3.storage.provider.v1beta1.RestoreRecycleItemRequest\x1a\x38.cs3.storage.provider.v1beta1.RestoreRecycleItemResponse\x12]\n\x04Stat\x12).cs3.storage.provider.v1beta1.StatRequest\x1a*.cs3.storage.provider.v1beta1.StatResponse\x12x\n\rCreateSymlink\x12\x32.cs3.storage.provider.v1beta1.CreateSymlinkRequest\x1a\x33.cs3.storage.provider.v1beta1.CreateSymlinkResponse\x12\x8d\x01\n\x14SetArbitraryMetadata\x12\x39.cs3.storage.provider.v1beta1.SetArbitraryMetadataRequest\x1a:.cs3.storage.provider.v1beta1.SetArbitraryMetadataResponse\x12\x93\x01\n\x16UnsetArbitraryMetadata\x12;.cs3.storage.provider.v1beta1.UnsetArbitraryMetadataRequest\x1a<.cs3.storage.provider.v1beta1.UnsetArbitraryMetadataResponse\x12\x66\n\x07SetLock\x12,.cs3.storage.provider.v1beta1.SetLockRequest\x1a-.cs3.storage.provider.v1beta1.SetLockResponse\x12\x66\n\x07GetLock\x12,.cs3.storage.provider.v1beta1.GetLockRequest\x1a-.cs3.storage.provider.v1beta1.GetLockResponse\x12r\n\x0bRefreshLock\x12\x30.cs3.storage.provider.v1beta1.RefreshLockRequest\x1a\x31.cs3.storage.provider.v1beta1.RefreshLockResponse\x12\x63\n\x06Unlock\x12+.cs3.storage.provider.v1beta1.UnlockRequest\x1a,.cs3.storage.provider.v1beta1.UnlockResponse\x12o\n\nCreateHome\x12/.cs3.storage.provider.v1beta1.CreateHomeRequest\x1a\x30.cs3.storage.provider.v1beta1.CreateHomeResponse\x12\x87\x01\n\x12\x43reateStorageSpace\x12\x37.cs3.storage.provider.v1beta1.CreateStorageSpaceRequest\x1a\x38.cs3.storage.provider.v1beta1.CreateStorageSpaceResponse\x12\x84\x01\n\x11ListStorageSpaces\x12\x36.cs3.storage.provider.v1beta1.ListStorageSpacesRequest\x1a\x37.cs3.storage.provider.v1beta1.ListStorageSpacesResponse\x12\x87\x01\n\x12UpdateStorageSpace\x12\x37.cs3.storage.provider.v1beta1.UpdateStorageSpaceRequest\x1a\x38.cs3.storage.provider.v1beta1.UpdateStorageSpaceResponse\x12\x87\x01\n\x12\x44\x65leteStorageSpace\x12\x37.cs3.storage.provider.v1beta1.DeleteStorageSpaceRequest\x1a\x38.cs3.storage.provider.v1beta1.DeleteStorageSpaceResponse\x12_\n\tOpenInApp\x12%.cs3.gateway.v1beta1.OpenInAppRequest\x1a+.cs3.app.provider.v1beta1.OpenInAppResponse\x12|\n\x0b\x43reateShare\x12\x35.cs3.sharing.collaboration.v1beta1.CreateShareRequest\x1a\x36.cs3.sharing.collaboration.v1beta1.CreateShareResponse\x12|\n\x0bRemoveShare\x12\x35.cs3.sharing.collaboration.v1beta1.RemoveShareRequest\x1a\x36.cs3.sharing.collaboration.v1beta1.RemoveShareResponse\x12s\n\x08GetShare\x12\x32.cs3.sharing.collaboration.v1beta1.GetShareRequest\x1a\x33.cs3.sharing.collaboration.v1beta1.GetShareResponse\x12y\n\nListShares\x12\x34.cs3.sharing.collaboration.v1beta1.ListSharesRequest\x1a\x35.cs3.sharing.collaboration.v1beta1.ListSharesResponse\x12|\n\x0bUpdateShare\x12\x35.cs3.sharing.collaboration.v1beta1.UpdateShareRequest\x1a\x36.cs3.sharing.collaboration.v1beta1.UpdateShareResponse\x12\x91\x01\n\x12ListReceivedShares\x12<.cs3.sharing.collaboration.v1beta1.ListReceivedSharesRequest\x1a=.cs3.sharing.collaboration.v1beta1.ListReceivedSharesResponse\x12\x94\x01\n\x13UpdateReceivedShare\x12=.cs3.sharing.collaboration.v1beta1.UpdateReceivedShareRequest\x1a>.cs3.sharing.collaboration.v1beta1.UpdateReceivedShareResponse\x12\x8b\x01\n\x10GetReceivedShare\x12:.cs3.sharing.collaboration.v1beta1.GetReceivedShareRequest\x1a;.cs3.sharing.collaboration.v1beta1.GetReceivedShareResponse\x12Y\n\x06SetKey\x12&.cs3.preferences.v1beta1.SetKeyRequest\x1a\'.cs3.preferences.v1beta1.SetKeyResponse\x12Y\n\x06GetKey\x12&.cs3.preferences.v1beta1.GetKeyRequest\x1a\'.cs3.preferences.v1beta1.GetKeyResponse\x12|\n\x11\x43reatePublicShare\x12\x32.cs3.sharing.link.v1beta1.CreatePublicShareRequest\x1a\x33.cs3.sharing.link.v1beta1.CreatePublicShareResponse\x12|\n\x11RemovePublicShare\x12\x32.cs3.sharing.link.v1beta1.RemovePublicShareRequest\x1a\x33.cs3.sharing.link.v1beta1.RemovePublicShareResponse\x12s\n\x0eGetPublicShare\x12/.cs3.sharing.link.v1beta1.GetPublicShareRequest\x1a\x30.cs3.sharing.link.v1beta1.GetPublicShareResponse\x12\x88\x01\n\x15GetPublicShareByToken\x12\x36.cs3.sharing.link.v1beta1.GetPublicShareByTokenRequest\x1a\x37.cs3.sharing.link.v1beta1.GetPublicShareByTokenResponse\x12y\n\x10ListPublicShares\x12\x31.cs3.sharing.link.v1beta1.ListPublicSharesRequest\x1a\x32.cs3.sharing.link.v1beta1.ListPublicSharesResponse\x12|\n\x11UpdatePublicShare\x12\x32.cs3.sharing.link.v1beta1.UpdatePublicShareRequest\x1a\x33.cs3.sharing.link.v1beta1.UpdatePublicShareResponse\x12q\n\x0e\x43reateOCMShare\x12..cs3.sharing.ocm.v1beta1.CreateOCMShareRequest\x1a/.cs3.sharing.ocm.v1beta1.CreateOCMShareResponse\x12q\n\x0eRemoveOCMShare\x12..cs3.sharing.ocm.v1beta1.RemoveOCMShareRequest\x1a/.cs3.sharing.ocm.v1beta1.RemoveOCMShareResponse\x12h\n\x0bGetOCMShare\x12+.cs3.sharing.ocm.v1beta1.GetOCMShareRequest\x1a,.cs3.sharing.ocm.v1beta1.GetOCMShareResponse\x12}\n\x12GetOCMShareByToken\x12\x32.cs3.sharing.ocm.v1beta1.GetOCMShareByTokenRequest\x1a\x33.cs3.sharing.ocm.v1beta1.GetOCMShareByTokenResponse\x12n\n\rListOCMShares\x12-.cs3.sharing.ocm.v1beta1.ListOCMSharesRequest\x1a..cs3.sharing.ocm.v1beta1.ListOCMSharesResponse\x12q\n\x0eUpdateOCMShare\x12..cs3.sharing.ocm.v1beta1.UpdateOCMShareRequest\x1a/.cs3.sharing.ocm.v1beta1.UpdateOCMShareResponse\x12\x86\x01\n\x15ListReceivedOCMShares\x12\x35.cs3.sharing.ocm.v1beta1.ListReceivedOCMSharesRequest\x1a\x36.cs3.sharing.ocm.v1beta1.ListReceivedOCMSharesResponse\x12\x89\x01\n\x16UpdateReceivedOCMShare\x12\x36.cs3.sharing.ocm.v1beta1.UpdateReceivedOCMShareRequest\x1a\x37.cs3.sharing.ocm.v1beta1.UpdateReceivedOCMShareResponse\x12\x80\x01\n\x13GetReceivedOCMShare\x12\x33.cs3.sharing.ocm.v1beta1.GetReceivedOCMShareRequest\x1a\x34.cs3.sharing.ocm.v1beta1.GetReceivedOCMShareResponse\x12v\n\x0fGetAppProviders\x12\x30.cs3.app.registry.v1beta1.GetAppProvidersRequest\x1a\x31.cs3.app.registry.v1beta1.GetAppProvidersResponse\x12s\n\x0e\x41\x64\x64\x41ppProvider\x12/.cs3.app.registry.v1beta1.AddAppProviderRequest\x1a\x30.cs3.app.registry.v1beta1.AddAppProviderResponse\x12y\n\x10ListAppProviders\x12\x31.cs3.app.registry.v1beta1.ListAppProvidersRequest\x1a\x32.cs3.app.registry.v1beta1.ListAppProvidersResponse\x12\x8b\x01\n\x16ListSupportedMimeTypes\x12\x37.cs3.app.registry.v1beta1.ListSupportedMimeTypesRequest\x1a\x38.cs3.app.registry.v1beta1.ListSupportedMimeTypesResponse\x12\xa9\x01\n GetDefaultAppProviderForMimeType\x12\x41.cs3.app.registry.v1beta1.GetDefaultAppProviderForMimeTypeRequest\x1a\x42.cs3.app.registry.v1beta1.GetDefaultAppProviderForMimeTypeResponse\x12\xa9\x01\n SetDefaultAppProviderForMimeType\x12\x41.cs3.app.registry.v1beta1.SetDefaultAppProviderForMimeTypeRequest\x1a\x42.cs3.app.registry.v1beta1.SetDefaultAppProviderForMimeTypeResponse\x12`\n\x07GetUser\x12).cs3.identity.user.v1beta1.GetUserRequest\x1a*.cs3.identity.user.v1beta1.GetUserResponse\x12u\n\x0eGetUserByClaim\x12\x30.cs3.identity.user.v1beta1.GetUserByClaimRequest\x1a\x31.cs3.identity.user.v1beta1.GetUserByClaimResponse\x12r\n\rGetUserGroups\x12/.cs3.identity.user.v1beta1.GetUserGroupsRequest\x1a\x30.cs3.identity.user.v1beta1.GetUserGroupsResponse\x12\x66\n\tFindUsers\x12+.cs3.identity.user.v1beta1.FindUsersRequest\x1a,.cs3.identity.user.v1beta1.FindUsersResponse\x12\x65\n\x08GetGroup\x12+.cs3.identity.group.v1beta1.GetGroupRequest\x1a,.cs3.identity.group.v1beta1.GetGroupResponse\x12z\n\x0fGetGroupByClaim\x12\x32.cs3.identity.group.v1beta1.GetGroupByClaimRequest\x1a\x33.cs3.identity.group.v1beta1.GetGroupByClaimResponse\x12k\n\nGetMembers\x12-.cs3.identity.group.v1beta1.GetMembersRequest\x1a..cs3.identity.group.v1beta1.GetMembersResponse\x12h\n\tHasMember\x12,.cs3.identity.group.v1beta1.HasMemberRequest\x1a-.cs3.identity.group.v1beta1.HasMemberResponse\x12k\n\nFindGroups\x12-.cs3.identity.group.v1beta1.FindGroupsRequest\x1a..cs3.identity.group.v1beta1.FindGroupsResponse\x12x\n\x11ListAuthProviders\x12\x33.cs3.auth.registry.v1beta1.ListAuthProvidersRequest\x1a..cs3.gateway.v1beta1.ListAuthProvidersResponse\x12\x66\n\x07GetHome\x12,.cs3.storage.provider.v1beta1.GetHomeRequest\x1a-.cs3.storage.provider.v1beta1.GetHomeResponse\x12~\n\x13GenerateInviteToken\x12\x32.cs3.ocm.invite.v1beta1.GenerateInviteTokenRequest\x1a\x33.cs3.ocm.invite.v1beta1.GenerateInviteTokenResponse\x12u\n\x10ListInviteTokens\x12/.cs3.ocm.invite.v1beta1.ListInviteTokensRequest\x1a\x30.cs3.ocm.invite.v1beta1.ListInviteTokensResponse\x12l\n\rForwardInvite\x12,.cs3.ocm.invite.v1beta1.ForwardInviteRequest\x1a-.cs3.ocm.invite.v1beta1.ForwardInviteResponse\x12i\n\x0c\x41\x63\x63\x65ptInvite\x12+.cs3.ocm.invite.v1beta1.AcceptInviteRequest\x1a,.cs3.ocm.invite.v1beta1.AcceptInviteResponse\x12r\n\x0fGetAcceptedUser\x12..cs3.ocm.invite.v1beta1.GetAcceptedUserRequest\x1a/.cs3.ocm.invite.v1beta1.GetAcceptedUserResponse\x12x\n\x11\x46indAcceptedUsers\x12\x30.cs3.ocm.invite.v1beta1.FindAcceptedUsersRequest\x1a\x31.cs3.ocm.invite.v1beta1.FindAcceptedUsersResponse\x12{\n\x12\x44\x65leteAcceptedUser\x12\x31.cs3.ocm.invite.v1beta1.DeleteAcceptedUserRequest\x1a\x32.cs3.ocm.invite.v1beta1.DeleteAcceptedUserResponse\x12|\n\x11IsProviderAllowed\x12\x32.cs3.ocm.provider.v1beta1.IsProviderAllowedRequest\x1a\x33.cs3.ocm.provider.v1beta1.IsProviderAllowedResponse\x12v\n\x0fGetInfoByDomain\x12\x30.cs3.ocm.provider.v1beta1.GetInfoByDomainRequest\x1a\x31.cs3.ocm.provider.v1beta1.GetInfoByDomainResponse\x12y\n\x10ListAllProviders\x12\x31.cs3.ocm.provider.v1beta1.ListAllProvidersRequest\x1a\x32.cs3.ocm.provider.v1beta1.ListAllProvidersResponse\x12w\n\x12\x43reateOCMCoreShare\x12/.cs3.ocm.core.v1beta1.CreateOCMCoreShareRequest\x1a\x30.cs3.ocm.core.v1beta1.CreateOCMCoreShareResponse\x12w\n\x12UpdateOCMCoreShare\x12/.cs3.ocm.core.v1beta1.UpdateOCMCoreShareRequest\x1a\x30.cs3.ocm.core.v1beta1.UpdateOCMCoreShareResponse\x12w\n\x12\x44\x65leteOCMCoreShare\x12/.cs3.ocm.core.v1beta1.DeleteOCMCoreShareRequest\x1a\x30.cs3.ocm.core.v1beta1.DeleteOCMCoreShareResponse\x12_\n\x0e\x43reateTransfer\x12%.cs3.tx.v1beta1.CreateTransferRequest\x1a&.cs3.tx.v1beta1.CreateTransferResponse\x12h\n\x11GetTransferStatus\x12(.cs3.tx.v1beta1.GetTransferStatusRequest\x1a).cs3.tx.v1beta1.GetTransferStatusResponse\x12_\n\x0e\x43\x61ncelTransfer\x12%.cs3.tx.v1beta1.CancelTransferRequest\x1a&.cs3.tx.v1beta1.CancelTransferResponse\x12\\\n\rListTransfers\x12$.cs3.tx.v1beta1.ListTransfersRequest\x1a%.cs3.tx.v1beta1.ListTransfersResponse\x12\\\n\rRetryTransfer\x12$.cs3.tx.v1beta1.RetryTransferRequest\x1a%.cs3.tx.v1beta1.RetryTransferResponse\x12t\n\x0f\x43heckPermission\x12/.cs3.permissions.v1beta1.CheckPermissionRequest\x1a\x30.cs3.permissions.v1beta1.CheckPermissionResponseBn\n\x17\x63om.cs3.gateway.v1beta1B\x0fGatewayApiProtoP\x01Z\x0egatewayv1beta1\xa2\x02\x03\x43GX\xaa\x02\x13\x43s3.Gateway.V1Beta1\xca\x02\x13\x43s3\\Gateway\\V1Beta1b\x06proto3')



_AUTHENTICATEREQUEST = DESCRIPTOR.message_types_by_name['AuthenticateRequest']
_AUTHENTICATERESPONSE = DESCRIPTOR.message_types_by_name['AuthenticateResponse']
_WHOAMIREQUEST = DESCRIPTOR.message_types_by_name['WhoAmIRequest']
_WHOAMIRESPONSE = DESCRIPTOR.message_types_by_name['WhoAmIResponse']
_GETQUOTAREQUEST = DESCRIPTOR.message_types_by_name['GetQuotaRequest']
_INITIATEFILEDOWNLOADRESPONSE = DESCRIPTOR.message_types_by_name['InitiateFileDownloadResponse']
_INITIATEFILEUPLOADRESPONSE = DESCRIPTOR.message_types_by_name['InitiateFileUploadResponse']
_LISTAUTHPROVIDERSRESPONSE = DESCRIPTOR.message_types_by_name['ListAuthProvidersResponse']
_OPENINAPPREQUEST = DESCRIPTOR.message_types_by_name['OpenInAppRequest']
_OPENINAPPREQUEST_VIEWMODE = _OPENINAPPREQUEST.enum_types_by_name['ViewMode']
AuthenticateRequest = _reflection.GeneratedProtocolMessageType('AuthenticateRequest', (_message.Message,), {
  'DESCRIPTOR' : _AUTHENTICATEREQUEST,
  '__module__' : 'cs3.gateway.v1beta1.gateway_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.gateway.v1beta1.AuthenticateRequest)
  })
_sym_db.RegisterMessage(AuthenticateRequest)

AuthenticateResponse = _reflection.GeneratedProtocolMessageType('AuthenticateResponse', (_message.Message,), {
  'DESCRIPTOR' : _AUTHENTICATERESPONSE,
  '__module__' : 'cs3.gateway.v1beta1.gateway_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.gateway.v1beta1.AuthenticateResponse)
  })
_sym_db.RegisterMessage(AuthenticateResponse)

WhoAmIRequest = _reflection.GeneratedProtocolMessageType('WhoAmIRequest', (_message.Message,), {
  'DESCRIPTOR' : _WHOAMIREQUEST,
  '__module__' : 'cs3.gateway.v1beta1.gateway_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.gateway.v1beta1.WhoAmIRequest)
  })
_sym_db.RegisterMessage(WhoAmIRequest)

WhoAmIResponse = _reflection.GeneratedProtocolMessageType('WhoAmIResponse', (_message.Message,), {
  'DESCRIPTOR' : _WHOAMIRESPONSE,
  '__module__' : 'cs3.gateway.v1beta1.gateway_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.gateway.v1beta1.WhoAmIResponse)
  })
_sym_db.RegisterMessage(WhoAmIResponse)

GetQuotaRequest = _reflection.GeneratedProtocolMessageType('GetQuotaRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETQUOTAREQUEST,
  '__module__' : 'cs3.gateway.v1beta1.gateway_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.gateway.v1beta1.GetQuotaRequest)
  })
_sym_db.RegisterMessage(GetQuotaRequest)

InitiateFileDownloadResponse = _reflection.GeneratedProtocolMessageType('InitiateFileDownloadResponse', (_message.Message,), {
  'DESCRIPTOR' : _INITIATEFILEDOWNLOADRESPONSE,
  '__module__' : 'cs3.gateway.v1beta1.gateway_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.gateway.v1beta1.InitiateFileDownloadResponse)
  })
_sym_db.RegisterMessage(InitiateFileDownloadResponse)

InitiateFileUploadResponse = _reflection.GeneratedProtocolMessageType('InitiateFileUploadResponse', (_message.Message,), {
  'DESCRIPTOR' : _INITIATEFILEUPLOADRESPONSE,
  '__module__' : 'cs3.gateway.v1beta1.gateway_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.gateway.v1beta1.InitiateFileUploadResponse)
  })
_sym_db.RegisterMessage(InitiateFileUploadResponse)

ListAuthProvidersResponse = _reflection.GeneratedProtocolMessageType('ListAuthProvidersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTAUTHPROVIDERSRESPONSE,
  '__module__' : 'cs3.gateway.v1beta1.gateway_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.gateway.v1beta1.ListAuthProvidersResponse)
  })
_sym_db.RegisterMessage(ListAuthProvidersResponse)

OpenInAppRequest = _reflection.GeneratedProtocolMessageType('OpenInAppRequest', (_message.Message,), {
  'DESCRIPTOR' : _OPENINAPPREQUEST,
  '__module__' : 'cs3.gateway.v1beta1.gateway_api_pb2'
  # @@protoc_insertion_point(class_scope:cs3.gateway.v1beta1.OpenInAppRequest)
  })
_sym_db.RegisterMessage(OpenInAppRequest)

_GATEWAYAPI = DESCRIPTOR.services_by_name['GatewayAPI']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.cs3.gateway.v1beta1B\017GatewayApiProtoP\001Z\016gatewayv1beta1\242\002\003CGX\252\002\023Cs3.Gateway.V1Beta1\312\002\023Cs3\\Gateway\\V1Beta1'
  _AUTHENTICATEREQUEST._serialized_start=963
  _AUTHENTICATEREQUEST._serialized_end=1083
  _AUTHENTICATERESPONSE._serialized_start=1086
  _AUTHENTICATERESPONSE._serialized_end=1254
  _WHOAMIREQUEST._serialized_start=1256
  _WHOAMIREQUEST._serialized_end=1329
  _WHOAMIRESPONSE._serialized_start=1332
  _WHOAMIRESPONSE._serialized_end=1479
  _GETQUOTAREQUEST._serialized_start=1481
  _GETQUOTAREQUEST._serialized_end=1595
  _INITIATEFILEDOWNLOADRESPONSE._serialized_start=1598
  _INITIATEFILEDOWNLOADRESPONSE._serialized_end=1774
  _INITIATEFILEUPLOADRESPONSE._serialized_start=1777
  _INITIATEFILEUPLOADRESPONSE._serialized_end=1949
  _LISTAUTHPROVIDERSRESPONSE._serialized_start=1951
  _LISTAUTHPROVIDERSRESPONSE._serialized_end=2077
  _OPENINAPPREQUEST._serialized_start=2080
  _OPENINAPPREQUEST._serialized_end=2427
  _OPENINAPPREQUEST_VIEWMODE._serialized_start=2295
  _OPENINAPPREQUEST_VIEWMODE._serialized_end=2427
  _GATEWAYAPI._serialized_start=2430
  _GATEWAYAPI._serialized_end=14139
# @@protoc_insertion_point(module_scope)
