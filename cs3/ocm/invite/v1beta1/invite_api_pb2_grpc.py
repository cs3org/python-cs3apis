# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from cs3.ocm.invite.v1beta1 import invite_api_pb2 as cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2


class InviteAPIStub(object):
    """Invite API

    The Invite API is meant to invite users and groups belonging to other
    sync'n'share systems, so that collaboration of resources can be enabled.

    The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
    NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and
    "OPTIONAL" in this document are to be interpreted as described in
    RFC 2119.

    The following are global requirements that apply to all methods:
    Any method MUST return CODE_OK on a succesful operation.
    Any method MAY return NOT_IMPLEMENTED.
    Any method MAY return INTERNAL.
    Any method MAY return UNKNOWN.
    Any method MAY return UNAUTHENTICATED.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GenerateInviteToken = channel.unary_unary(
                '/cs3.ocm.invite.v1beta1.InviteAPI/GenerateInviteToken',
                request_serializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.GenerateInviteTokenRequest.SerializeToString,
                response_deserializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.GenerateInviteTokenResponse.FromString,
                )
        self.ForwardInvite = channel.unary_unary(
                '/cs3.ocm.invite.v1beta1.InviteAPI/ForwardInvite',
                request_serializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.ForwardInviteRequest.SerializeToString,
                response_deserializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.ForwardInviteResponse.FromString,
                )
        self.AcceptInvite = channel.unary_unary(
                '/cs3.ocm.invite.v1beta1.InviteAPI/AcceptInvite',
                request_serializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.AcceptInviteRequest.SerializeToString,
                response_deserializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.AcceptInviteResponse.FromString,
                )
        self.GetAcceptedUser = channel.unary_unary(
                '/cs3.ocm.invite.v1beta1.InviteAPI/GetAcceptedUser',
                request_serializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.GetAcceptedUserRequest.SerializeToString,
                response_deserializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.GetAcceptedUserResponse.FromString,
                )
        self.FindAcceptedUsers = channel.unary_unary(
                '/cs3.ocm.invite.v1beta1.InviteAPI/FindAcceptedUsers',
                request_serializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.FindAcceptedUsersRequest.SerializeToString,
                response_deserializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.FindAcceptedUsersResponse.FromString,
                )


class InviteAPIServicer(object):
    """Invite API

    The Invite API is meant to invite users and groups belonging to other
    sync'n'share systems, so that collaboration of resources can be enabled.

    The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
    NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and
    "OPTIONAL" in this document are to be interpreted as described in
    RFC 2119.

    The following are global requirements that apply to all methods:
    Any method MUST return CODE_OK on a succesful operation.
    Any method MAY return NOT_IMPLEMENTED.
    Any method MAY return INTERNAL.
    Any method MAY return UNKNOWN.
    Any method MAY return UNAUTHENTICATED.
    """

    def GenerateInviteToken(self, request, context):
        """Generates a new token for the user with a validity of 24 hours.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ForwardInvite(self, request, context):
        """Forwards a received invite to the sync'n'share system provider.
        MUST return CODE_NOT_FOUND if the token does not exist.
        MUST return CODE_INVALID_ARGUMENT if the token expired.
        MUST return CODE_ALREADY_EXISTS if the user already accepted an invite.
        MUST return CODE_PERMISSION_DENIED if the remote service is not trusted to accept invitations.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AcceptInvite(self, request, context):
        """Completes an invitation acceptance.
        MUST return CODE_NOT_FOUND if the token does not exist.
        MUST return CODE_INVALID_ARGUMENT if the token expired.
        MUST return CODE_ALREADY_EXISTS if the user already accepted an invite.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAcceptedUser(self, request, context):
        """Retrieves details about a remote user who has accepted an invite to share.
        MUST return CODE_NOT_FOUND if the user does not exist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindAcceptedUsers(self, request, context):
        """Finds users who accepted invite tokens by their attributes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InviteAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GenerateInviteToken': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateInviteToken,
                    request_deserializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.GenerateInviteTokenRequest.FromString,
                    response_serializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.GenerateInviteTokenResponse.SerializeToString,
            ),
            'ForwardInvite': grpc.unary_unary_rpc_method_handler(
                    servicer.ForwardInvite,
                    request_deserializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.ForwardInviteRequest.FromString,
                    response_serializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.ForwardInviteResponse.SerializeToString,
            ),
            'AcceptInvite': grpc.unary_unary_rpc_method_handler(
                    servicer.AcceptInvite,
                    request_deserializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.AcceptInviteRequest.FromString,
                    response_serializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.AcceptInviteResponse.SerializeToString,
            ),
            'GetAcceptedUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAcceptedUser,
                    request_deserializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.GetAcceptedUserRequest.FromString,
                    response_serializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.GetAcceptedUserResponse.SerializeToString,
            ),
            'FindAcceptedUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.FindAcceptedUsers,
                    request_deserializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.FindAcceptedUsersRequest.FromString,
                    response_serializer=cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.FindAcceptedUsersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cs3.ocm.invite.v1beta1.InviteAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InviteAPI(object):
    """Invite API

    The Invite API is meant to invite users and groups belonging to other
    sync'n'share systems, so that collaboration of resources can be enabled.

    The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
    NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and
    "OPTIONAL" in this document are to be interpreted as described in
    RFC 2119.

    The following are global requirements that apply to all methods:
    Any method MUST return CODE_OK on a succesful operation.
    Any method MAY return NOT_IMPLEMENTED.
    Any method MAY return INTERNAL.
    Any method MAY return UNKNOWN.
    Any method MAY return UNAUTHENTICATED.
    """

    @staticmethod
    def GenerateInviteToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.ocm.invite.v1beta1.InviteAPI/GenerateInviteToken',
            cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.GenerateInviteTokenRequest.SerializeToString,
            cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.GenerateInviteTokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ForwardInvite(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.ocm.invite.v1beta1.InviteAPI/ForwardInvite',
            cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.ForwardInviteRequest.SerializeToString,
            cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.ForwardInviteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AcceptInvite(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.ocm.invite.v1beta1.InviteAPI/AcceptInvite',
            cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.AcceptInviteRequest.SerializeToString,
            cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.AcceptInviteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAcceptedUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.ocm.invite.v1beta1.InviteAPI/GetAcceptedUser',
            cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.GetAcceptedUserRequest.SerializeToString,
            cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.GetAcceptedUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindAcceptedUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.ocm.invite.v1beta1.InviteAPI/FindAcceptedUsers',
            cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.FindAcceptedUsersRequest.SerializeToString,
            cs3_dot_ocm_dot_invite_dot_v1beta1_dot_invite__api__pb2.FindAcceptedUsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
