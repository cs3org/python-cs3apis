# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
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
    self.GetStorageProvider = channel.unary_unary(
        '/cs3.storage.registry.v1beta1.RegistryAPI/GetStorageProvider',
        request_serializer=cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetStorageProviderRequest.SerializeToString,
        response_deserializer=cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetStorageProviderResponse.FromString,
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

  def GetStorageProvider(self, request, context):
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
      'GetStorageProvider': grpc.unary_unary_rpc_method_handler(
          servicer.GetStorageProvider,
          request_deserializer=cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetStorageProviderRequest.FromString,
          response_serializer=cs3_dot_storage_dot_registry_dot_v1beta1_dot_registry__api__pb2.GetStorageProviderResponse.SerializeToString,
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
