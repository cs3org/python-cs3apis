# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from cs3.storage.registry.v1beta1 import registry_api_pb2 as cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2


class RegistryAPIStub(object):
    """Storage Registry API

    The Storage Registry API is meant to as registry to obtain
    information of available storage providers.

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
        self.GetStorageProviders = channel.unary_unary(
                '/cs3.storage.registry.v1beta1.RegistryAPI/GetStorageProviders',
                request_serializer=cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetStorageProvidersRequest.SerializeToString,
                response_deserializer=cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetStorageProvidersResponse.FromString,
                )
        self.ListStorageProviders = channel.unary_unary(
                '/cs3.storage.registry.v1beta1.RegistryAPI/ListStorageProviders',
                request_serializer=cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.ListStorageProvidersRequest.SerializeToString,
                response_deserializer=cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.ListStorageProvidersResponse.FromString,
                )
        self.GetHome = channel.unary_unary(
                '/cs3.storage.registry.v1beta1.RegistryAPI/GetHome',
                request_serializer=cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetHomeRequest.SerializeToString,
                response_deserializer=cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetHomeResponse.FromString,
                )


class RegistryAPIServicer(object):
    """Storage Registry API

    The Storage Registry API is meant to as registry to obtain
    information of available storage providers.

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

    def GetStorageProviders(self, request, context):
        """Returns the storage provider that is reponsible for the given
        resource reference.
        MUST return CODE_NOT_FOUND if the reference does not exist.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListStorageProviders(self, request, context):
        """Returns a list of the available storage providers known by this registry.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHome(self, request, context):
        """Gets the user home storage provider.
        TODO(labkode): missing methods for adding and removing a storage provider
        with different visibility levels (system-wide, user-wide, group-wide)...
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RegistryAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetStorageProviders': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStorageProviders,
                    request_deserializer=cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetStorageProvidersRequest.FromString,
                    response_serializer=cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetStorageProvidersResponse.SerializeToString,
            ),
            'ListStorageProviders': grpc.unary_unary_rpc_method_handler(
                    servicer.ListStorageProviders,
                    request_deserializer=cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.ListStorageProvidersRequest.FromString,
                    response_serializer=cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.ListStorageProvidersResponse.SerializeToString,
            ),
            'GetHome': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHome,
                    request_deserializer=cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetHomeRequest.FromString,
                    response_serializer=cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetHomeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cs3.storage.registry.v1beta1.RegistryAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RegistryAPI(object):
    """Storage Registry API

    The Storage Registry API is meant to as registry to obtain
    information of available storage providers.

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
    def GetStorageProviders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.storage.registry.v1beta1.RegistryAPI/GetStorageProviders',
            cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetStorageProvidersRequest.SerializeToString,
            cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetStorageProvidersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListStorageProviders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.storage.registry.v1beta1.RegistryAPI/ListStorageProviders',
            cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.ListStorageProvidersRequest.SerializeToString,
            cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.ListStorageProvidersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetHome(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.storage.registry.v1beta1.RegistryAPI/GetHome',
            cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetHomeRequest.SerializeToString,
            cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetHomeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
