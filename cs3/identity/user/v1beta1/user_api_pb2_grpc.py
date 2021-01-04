# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from cs3.identity.user.v1beta1 import user_api_pb2 as cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2


class UserAPIStub(object):
    """UserProvider API.

    The UserProvider API is responsible for providing
    methods to retrieve information about the users.

    The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
    NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and
    "OPTIONAL" in this document are to be interpreted as described in
    RFC 2119.

    The following are global requirements that apply to all methods:
    Any method MUST return CODE_OK on a successful operation.
    Any method MAY return NOT_IMPLEMENTED.
    Any method MAY return INTERNAL.
    Any method MAY return UNKNOWN.
    Any method MAY return UNAUTHENTICATED.

    Provides an API for managing users.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUser = channel.unary_unary(
                '/cs3.identity.user.v1beta1.UserAPI/GetUser',
                request_serializer=cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.GetUserRequest.SerializeToString,
                response_deserializer=cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.GetUserResponse.FromString,
                )
        self.GetUserByClaim = channel.unary_unary(
                '/cs3.identity.user.v1beta1.UserAPI/GetUserByClaim',
                request_serializer=cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.GetUserByClaimRequest.SerializeToString,
                response_deserializer=cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.GetUserByClaimResponse.FromString,
                )
        self.GetUserGroups = channel.unary_unary(
                '/cs3.identity.user.v1beta1.UserAPI/GetUserGroups',
                request_serializer=cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.GetUserGroupsRequest.SerializeToString,
                response_deserializer=cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.GetUserGroupsResponse.FromString,
                )
        self.FindUsers = channel.unary_unary(
                '/cs3.identity.user.v1beta1.UserAPI/FindUsers',
                request_serializer=cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.FindUsersRequest.SerializeToString,
                response_deserializer=cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.FindUsersResponse.FromString,
                )


class UserAPIServicer(object):
    """UserProvider API.

    The UserProvider API is responsible for providing
    methods to retrieve information about the users.

    The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
    NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and
    "OPTIONAL" in this document are to be interpreted as described in
    RFC 2119.

    The following are global requirements that apply to all methods:
    Any method MUST return CODE_OK on a successful operation.
    Any method MAY return NOT_IMPLEMENTED.
    Any method MAY return INTERNAL.
    Any method MAY return UNKNOWN.
    Any method MAY return UNAUTHENTICATED.

    Provides an API for managing users.
    """

    def GetUser(self, request, context):
        """Gets the information about a user by the user id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserByClaim(self, request, context):
        """Gets the information about a user based on a specified claim.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserGroups(self, request, context):
        """Gets the groups of a user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindUsers(self, request, context):
        """Finds users by any attribute of the user.
        TODO(labkode): to define the filters that make more sense.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.GetUserRequest.FromString,
                    response_serializer=cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.GetUserResponse.SerializeToString,
            ),
            'GetUserByClaim': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserByClaim,
                    request_deserializer=cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.GetUserByClaimRequest.FromString,
                    response_serializer=cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.GetUserByClaimResponse.SerializeToString,
            ),
            'GetUserGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserGroups,
                    request_deserializer=cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.GetUserGroupsRequest.FromString,
                    response_serializer=cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.GetUserGroupsResponse.SerializeToString,
            ),
            'FindUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.FindUsers,
                    request_deserializer=cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.FindUsersRequest.FromString,
                    response_serializer=cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.FindUsersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cs3.identity.user.v1beta1.UserAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserAPI(object):
    """UserProvider API.

    The UserProvider API is responsible for providing
    methods to retrieve information about the users.

    The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
    NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and
    "OPTIONAL" in this document are to be interpreted as described in
    RFC 2119.

    The following are global requirements that apply to all methods:
    Any method MUST return CODE_OK on a successful operation.
    Any method MAY return NOT_IMPLEMENTED.
    Any method MAY return INTERNAL.
    Any method MAY return UNKNOWN.
    Any method MAY return UNAUTHENTICATED.

    Provides an API for managing users.
    """

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.identity.user.v1beta1.UserAPI/GetUser',
            cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.GetUserRequest.SerializeToString,
            cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.GetUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserByClaim(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.identity.user.v1beta1.UserAPI/GetUserByClaim',
            cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.GetUserByClaimRequest.SerializeToString,
            cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.GetUserByClaimResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.identity.user.v1beta1.UserAPI/GetUserGroups',
            cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.GetUserGroupsRequest.SerializeToString,
            cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.GetUserGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.identity.user.v1beta1.UserAPI/FindUsers',
            cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.FindUsersRequest.SerializeToString,
            cs3_dot_identity_dot_user_dot_v1beta1_dot_user__api__pb2.FindUsersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
