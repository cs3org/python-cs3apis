# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from cs3.preferences.v0alpha import preferences_pb2 as cs3_dot_preferences_dot_v0alpha_dot_preferences__pb2


class PreferencesServiceStub(object):
  """Preferences API.

  The Preferences API is responsible for creating
  a key-value map according to user preferences.

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
    self.SetKey = channel.unary_unary(
        '/cs3.preferencesv0alpha.PreferencesService/SetKey',
        request_serializer=cs3_dot_preferences_dot_v0alpha_dot_preferences__pb2.SetKeyRequest.SerializeToString,
        response_deserializer=cs3_dot_preferences_dot_v0alpha_dot_preferences__pb2.SetKeyResponse.FromString,
        )
    self.GetKey = channel.unary_unary(
        '/cs3.preferencesv0alpha.PreferencesService/GetKey',
        request_serializer=cs3_dot_preferences_dot_v0alpha_dot_preferences__pb2.GetKeyRequest.SerializeToString,
        response_deserializer=cs3_dot_preferences_dot_v0alpha_dot_preferences__pb2.GetKeyResponse.FromString,
        )


class PreferencesServiceServicer(object):
  """Preferences API.

  The Preferences API is responsible for creating
  a key-value map according to user preferences.

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

  def SetKey(self, request, context):
    """Maps the key-value pair.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetKey(self, request, context):
    """Returns the value associated with the
    requested key.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PreferencesServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SetKey': grpc.unary_unary_rpc_method_handler(
          servicer.SetKey,
          request_deserializer=cs3_dot_preferences_dot_v0alpha_dot_preferences__pb2.SetKeyRequest.FromString,
          response_serializer=cs3_dot_preferences_dot_v0alpha_dot_preferences__pb2.SetKeyResponse.SerializeToString,
      ),
      'GetKey': grpc.unary_unary_rpc_method_handler(
          servicer.GetKey,
          request_deserializer=cs3_dot_preferences_dot_v0alpha_dot_preferences__pb2.GetKeyRequest.FromString,
          response_serializer=cs3_dot_preferences_dot_v0alpha_dot_preferences__pb2.GetKeyResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'cs3.preferencesv0alpha.PreferencesService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))