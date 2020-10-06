# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from cs3.preferences.v1beta1 import preferences_api_pb2 as cs3_dot_preferences_dot_v1beta1_dot_preferences__api__pb2


class PreferencesAPIStub(object):
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
                '/cs3.preferences.v1beta1.PreferencesAPI/SetKey',
                request_serializer=cs3_dot_preferences_dot_v1beta1_dot_preferences__api__pb2.SetKeyRequest.SerializeToString,
                response_deserializer=cs3_dot_preferences_dot_v1beta1_dot_preferences__api__pb2.SetKeyResponse.FromString,
                )
        self.GetKey = channel.unary_unary(
                '/cs3.preferences.v1beta1.PreferencesAPI/GetKey',
                request_serializer=cs3_dot_preferences_dot_v1beta1_dot_preferences__api__pb2.GetKeyRequest.SerializeToString,
                response_deserializer=cs3_dot_preferences_dot_v1beta1_dot_preferences__api__pb2.GetKeyResponse.FromString,
                )


class PreferencesAPIServicer(object):
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


def add_PreferencesAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetKey': grpc.unary_unary_rpc_method_handler(
                    servicer.SetKey,
                    request_deserializer=cs3_dot_preferences_dot_v1beta1_dot_preferences__api__pb2.SetKeyRequest.FromString,
                    response_serializer=cs3_dot_preferences_dot_v1beta1_dot_preferences__api__pb2.SetKeyResponse.SerializeToString,
            ),
            'GetKey': grpc.unary_unary_rpc_method_handler(
                    servicer.GetKey,
                    request_deserializer=cs3_dot_preferences_dot_v1beta1_dot_preferences__api__pb2.GetKeyRequest.FromString,
                    response_serializer=cs3_dot_preferences_dot_v1beta1_dot_preferences__api__pb2.GetKeyResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cs3.preferences.v1beta1.PreferencesAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PreferencesAPI(object):
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

    @staticmethod
    def SetKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.preferences.v1beta1.PreferencesAPI/SetKey',
            cs3_dot_preferences_dot_v1beta1_dot_preferences__api__pb2.SetKeyRequest.SerializeToString,
            cs3_dot_preferences_dot_v1beta1_dot_preferences__api__pb2.SetKeyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.preferences.v1beta1.PreferencesAPI/GetKey',
            cs3_dot_preferences_dot_v1beta1_dot_preferences__api__pb2.GetKeyRequest.SerializeToString,
            cs3_dot_preferences_dot_v1beta1_dot_preferences__api__pb2.GetKeyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
