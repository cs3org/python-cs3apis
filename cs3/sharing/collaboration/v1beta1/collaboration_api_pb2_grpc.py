# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from cs3.sharing.collaboration.v1beta1 import collaboration_api_pb2 as cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2


class CollaborationAPIStub(object):
    """User Share Provider API

    The User Share Provider API is meant to manipulate share
    resources for a specific share type (user, group, ocm, ...)
    from the perspective of the creator or the share and
    from the perspective of the receiver of the share.

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
        self.CreateShare = channel.unary_unary(
                '/cs3.sharing.collaboration.v1beta1.CollaborationAPI/CreateShare',
                request_serializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.CreateShareRequest.SerializeToString,
                response_deserializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.CreateShareResponse.FromString,
                )
        self.RemoveShare = channel.unary_unary(
                '/cs3.sharing.collaboration.v1beta1.CollaborationAPI/RemoveShare',
                request_serializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.RemoveShareRequest.SerializeToString,
                response_deserializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.RemoveShareResponse.FromString,
                )
        self.GetShare = channel.unary_unary(
                '/cs3.sharing.collaboration.v1beta1.CollaborationAPI/GetShare',
                request_serializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.GetShareRequest.SerializeToString,
                response_deserializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.GetShareResponse.FromString,
                )
        self.ListShares = channel.unary_unary(
                '/cs3.sharing.collaboration.v1beta1.CollaborationAPI/ListShares',
                request_serializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.ListSharesRequest.SerializeToString,
                response_deserializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.ListSharesResponse.FromString,
                )
        self.UpdateShare = channel.unary_unary(
                '/cs3.sharing.collaboration.v1beta1.CollaborationAPI/UpdateShare',
                request_serializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.UpdateShareRequest.SerializeToString,
                response_deserializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.UpdateShareResponse.FromString,
                )
        self.ListReceivedShares = channel.unary_unary(
                '/cs3.sharing.collaboration.v1beta1.CollaborationAPI/ListReceivedShares',
                request_serializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.ListReceivedSharesRequest.SerializeToString,
                response_deserializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.ListReceivedSharesResponse.FromString,
                )
        self.UpdateReceivedShare = channel.unary_unary(
                '/cs3.sharing.collaboration.v1beta1.CollaborationAPI/UpdateReceivedShare',
                request_serializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.UpdateReceivedShareRequest.SerializeToString,
                response_deserializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.UpdateReceivedShareResponse.FromString,
                )
        self.GetReceivedShare = channel.unary_unary(
                '/cs3.sharing.collaboration.v1beta1.CollaborationAPI/GetReceivedShare',
                request_serializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.GetReceivedShareRequest.SerializeToString,
                response_deserializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.GetReceivedShareResponse.FromString,
                )


class CollaborationAPIServicer(object):
    """User Share Provider API

    The User Share Provider API is meant to manipulate share
    resources for a specific share type (user, group, ocm, ...)
    from the perspective of the creator or the share and
    from the perspective of the receiver of the share.

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

    def CreateShare(self, request, context):
        """Creates a new share.
        MUST return CODE_NOT_FOUND if the resource reference does not exist.
        MUST return CODE_LOCKED if the resource reference already locked.
        MUST return CODE_ALREADY_EXISTS if the share already exists for the 4-tuple consisting of
        (owner, shared_resource, grantee).
        New shares MUST be created in the state SHARE_STATE_PENDING.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveShare(self, request, context):
        """Removes a share.
        MUST return CODE_NOT_FOUND if the share reference does not exist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetShare(self, request, context):
        """Gets share information for a single share.
        MUST return CODE_NOT_FOUND if the share reference does not exist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListShares(self, request, context):
        """List the shares the authenticated principal has created,
        both as owner and creator. If a filter is specified, only
        shares satisfying the filter MUST be returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateShare(self, request, context):
        """Updates a share.
        MUST return CODE_NOT_FOUND if the share reference does not exist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListReceivedShares(self, request, context):
        """List all shares the authenticated principal has received.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateReceivedShare(self, request, context):
        """Update the received share to change the share state or the display name.
        MUST return CODE_NOT_FOUND if the share reference does not exist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetReceivedShare(self, request, context):
        """Get the information for the given received share reference.
        MUST return CODE_NOT_FOUND if the received share reference does not exist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CollaborationAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateShare': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateShare,
                    request_deserializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.CreateShareRequest.FromString,
                    response_serializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.CreateShareResponse.SerializeToString,
            ),
            'RemoveShare': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveShare,
                    request_deserializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.RemoveShareRequest.FromString,
                    response_serializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.RemoveShareResponse.SerializeToString,
            ),
            'GetShare': grpc.unary_unary_rpc_method_handler(
                    servicer.GetShare,
                    request_deserializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.GetShareRequest.FromString,
                    response_serializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.GetShareResponse.SerializeToString,
            ),
            'ListShares': grpc.unary_unary_rpc_method_handler(
                    servicer.ListShares,
                    request_deserializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.ListSharesRequest.FromString,
                    response_serializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.ListSharesResponse.SerializeToString,
            ),
            'UpdateShare': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateShare,
                    request_deserializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.UpdateShareRequest.FromString,
                    response_serializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.UpdateShareResponse.SerializeToString,
            ),
            'ListReceivedShares': grpc.unary_unary_rpc_method_handler(
                    servicer.ListReceivedShares,
                    request_deserializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.ListReceivedSharesRequest.FromString,
                    response_serializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.ListReceivedSharesResponse.SerializeToString,
            ),
            'UpdateReceivedShare': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateReceivedShare,
                    request_deserializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.UpdateReceivedShareRequest.FromString,
                    response_serializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.UpdateReceivedShareResponse.SerializeToString,
            ),
            'GetReceivedShare': grpc.unary_unary_rpc_method_handler(
                    servicer.GetReceivedShare,
                    request_deserializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.GetReceivedShareRequest.FromString,
                    response_serializer=cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.GetReceivedShareResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cs3.sharing.collaboration.v1beta1.CollaborationAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CollaborationAPI(object):
    """User Share Provider API

    The User Share Provider API is meant to manipulate share
    resources for a specific share type (user, group, ocm, ...)
    from the perspective of the creator or the share and
    from the perspective of the receiver of the share.

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
    def CreateShare(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.sharing.collaboration.v1beta1.CollaborationAPI/CreateShare',
            cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.CreateShareRequest.SerializeToString,
            cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.CreateShareResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveShare(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.sharing.collaboration.v1beta1.CollaborationAPI/RemoveShare',
            cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.RemoveShareRequest.SerializeToString,
            cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.RemoveShareResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetShare(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.sharing.collaboration.v1beta1.CollaborationAPI/GetShare',
            cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.GetShareRequest.SerializeToString,
            cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.GetShareResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListShares(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.sharing.collaboration.v1beta1.CollaborationAPI/ListShares',
            cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.ListSharesRequest.SerializeToString,
            cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.ListSharesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateShare(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.sharing.collaboration.v1beta1.CollaborationAPI/UpdateShare',
            cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.UpdateShareRequest.SerializeToString,
            cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.UpdateShareResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListReceivedShares(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.sharing.collaboration.v1beta1.CollaborationAPI/ListReceivedShares',
            cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.ListReceivedSharesRequest.SerializeToString,
            cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.ListReceivedSharesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateReceivedShare(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.sharing.collaboration.v1beta1.CollaborationAPI/UpdateReceivedShare',
            cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.UpdateReceivedShareRequest.SerializeToString,
            cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.UpdateReceivedShareResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetReceivedShare(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.sharing.collaboration.v1beta1.CollaborationAPI/GetReceivedShare',
            cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.GetReceivedShareRequest.SerializeToString,
            cs3_dot_sharing_dot_collaboration_dot_v1beta1_dot_collaboration__api__pb2.GetReceivedShareResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
