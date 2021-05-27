# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from cs3.auth.applications.v1beta1 import applications_api_pb2 as cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2


class ApplicationsAPIStub(object):
    """Auth Applications API

    The Auth Applications API is meant to generate and manage authentication
    tokens with specified scopes to be used in third-party applications on behalf
    of the user.

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
        self.GenerateAppPassword = channel.unary_unary(
                '/cs3.auth.applications.v1beta1.ApplicationsAPI/GenerateAppPassword',
                request_serializer=cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.GenerateAppPasswordRequest.SerializeToString,
                response_deserializer=cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.GenerateAppPasswordResponse.FromString,
                )
        self.ListAppPasswords = channel.unary_unary(
                '/cs3.auth.applications.v1beta1.ApplicationsAPI/ListAppPasswords',
                request_serializer=cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.ListAppPasswordsRequest.SerializeToString,
                response_deserializer=cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.ListAppPasswordsResponse.FromString,
                )
        self.InvalidateAppPassword = channel.unary_unary(
                '/cs3.auth.applications.v1beta1.ApplicationsAPI/InvalidateAppPassword',
                request_serializer=cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.InvalidateAppPasswordRequest.SerializeToString,
                response_deserializer=cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.InvalidateAppPasswordResponse.FromString,
                )
        self.GetAppPassword = channel.unary_unary(
                '/cs3.auth.applications.v1beta1.ApplicationsAPI/GetAppPassword',
                request_serializer=cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.GetAppPasswordRequest.SerializeToString,
                response_deserializer=cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.GetAppPasswordResponse.FromString,
                )


class ApplicationsAPIServicer(object):
    """Auth Applications API

    The Auth Applications API is meant to generate and manage authentication
    tokens with specified scopes to be used in third-party applications on behalf
    of the user.

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

    def GenerateAppPassword(self, request, context):
        """GenerateAppPassword creates a password with specified scope to be used by
        third-party applications.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAppPasswords(self, request, context):
        """ListAppPasswords lists the application passwords created by a user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InvalidateAppPassword(self, request, context):
        """InvalidateAppPassword invalidates a generated password.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAppPassword(self, request, context):
        """GetAppPassword retrieves the password information by the combination of username and password.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ApplicationsAPIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GenerateAppPassword': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateAppPassword,
                    request_deserializer=cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.GenerateAppPasswordRequest.FromString,
                    response_serializer=cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.GenerateAppPasswordResponse.SerializeToString,
            ),
            'ListAppPasswords': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAppPasswords,
                    request_deserializer=cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.ListAppPasswordsRequest.FromString,
                    response_serializer=cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.ListAppPasswordsResponse.SerializeToString,
            ),
            'InvalidateAppPassword': grpc.unary_unary_rpc_method_handler(
                    servicer.InvalidateAppPassword,
                    request_deserializer=cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.InvalidateAppPasswordRequest.FromString,
                    response_serializer=cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.InvalidateAppPasswordResponse.SerializeToString,
            ),
            'GetAppPassword': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAppPassword,
                    request_deserializer=cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.GetAppPasswordRequest.FromString,
                    response_serializer=cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.GetAppPasswordResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cs3.auth.applications.v1beta1.ApplicationsAPI', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ApplicationsAPI(object):
    """Auth Applications API

    The Auth Applications API is meant to generate and manage authentication
    tokens with specified scopes to be used in third-party applications on behalf
    of the user.

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
    def GenerateAppPassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.auth.applications.v1beta1.ApplicationsAPI/GenerateAppPassword',
            cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.GenerateAppPasswordRequest.SerializeToString,
            cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.GenerateAppPasswordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAppPasswords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.auth.applications.v1beta1.ApplicationsAPI/ListAppPasswords',
            cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.ListAppPasswordsRequest.SerializeToString,
            cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.ListAppPasswordsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InvalidateAppPassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.auth.applications.v1beta1.ApplicationsAPI/InvalidateAppPassword',
            cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.InvalidateAppPasswordRequest.SerializeToString,
            cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.InvalidateAppPasswordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAppPassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cs3.auth.applications.v1beta1.ApplicationsAPI/GetAppPassword',
            cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.GetAppPasswordRequest.SerializeToString,
            cs3_dot_auth_dot_applications_dot_v1beta1_dot_applications__api__pb2.GetAppPasswordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
