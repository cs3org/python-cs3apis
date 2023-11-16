# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cs3/tx/v1beta1/tx_api.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cs3.rpc.v1beta1 import status_pb2 as cs3_dot_rpc_dot_v1beta1_dot_status__pb2
from cs3.sharing.ocm.v1beta1 import resources_pb2 as cs3_dot_sharing_dot_ocm_dot_v1beta1_dot_resources__pb2
from cs3.tx.v1beta1 import resources_pb2 as cs3_dot_tx_dot_v1beta1_dot_resources__pb2
from cs3.types.v1beta1 import types_pb2 as cs3_dot_types_dot_v1beta1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x63s3/tx/v1beta1/tx_api.proto\x12\x0e\x63s3.tx.v1beta1\x1a\x1c\x63s3/rpc/v1beta1/status.proto\x1a\'cs3/sharing/ocm/v1beta1/resources.proto\x1a\x1e\x63s3/tx/v1beta1/resources.proto\x1a\x1d\x63s3/types/v1beta1/types.proto\"\xd5\x01\n\x15\x43reateTransferRequest\x12$\n\x0esrc_target_uri\x18\x01 \x01(\tR\x0csrcTargetUri\x12&\n\x0f\x64\x65st_target_uri\x18\x02 \x01(\tR\rdestTargetUri\x12;\n\x08share_id\x18\x03 \x01(\x0b\x32 .cs3.sharing.ocm.v1beta1.ShareIdR\x07shareId\x12\x31\n\x06opaque\x18\x04 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\"\xad\x01\n\x16\x43reateTransferResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12/\n\x07tx_info\x18\x02 \x01(\x0b\x32\x16.cs3.tx.v1beta1.TxInfoR\x06txInfo\x12\x31\n\x06opaque\x18\x03 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\"x\n\x18GetTransferStatusRequest\x12)\n\x05tx_id\x18\x01 \x01(\x0b\x32\x14.cs3.tx.v1beta1.TxIdR\x04txId\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\"\xb0\x01\n\x19GetTransferStatusResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12/\n\x07tx_info\x18\x02 \x01(\x0b\x32\x16.cs3.tx.v1beta1.TxInfoR\x06txInfo\x12\x31\n\x06opaque\x18\x03 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\"u\n\x15\x43\x61ncelTransferRequest\x12)\n\x05tx_id\x18\x01 \x01(\x0b\x32\x14.cs3.tx.v1beta1.TxIdR\x04txId\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\"\xad\x01\n\x16\x43\x61ncelTransferResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12/\n\x07tx_info\x18\x02 \x01(\x0b\x32\x16.cs3.tx.v1beta1.TxInfoR\x06txInfo\x12\x31\n\x06opaque\x18\x03 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\"\xd5\x03\n\x14ListTransfersRequest\x12\x31\n\x06opaque\x18\x01 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\x12\x45\n\x07\x66ilters\x18\x02 \x03(\x0b\x32+.cs3.tx.v1beta1.ListTransfersRequest.FilterR\x07\x66ilters\x1a\xc2\x02\n\x06\x46ilter\x12\x44\n\x04type\x18\x01 \x01(\x0e\x32\x30.cs3.tx.v1beta1.ListTransfersRequest.Filter.TypeR\x04type\x12\x30\n\x06status\x18\x02 \x01(\x0e\x32\x16.cs3.tx.v1beta1.StatusH\x00R\x06status\x12=\n\x08share_id\x18\x03 \x01(\x0b\x32 .cs3.sharing.ocm.v1beta1.ShareIdH\x00R\x07shareId\x12+\n\x05tx_id\x18\x04 \x01(\x0b\x32\x14.cs3.tx.v1beta1.TxIdH\x00R\x04txId\"L\n\x04Type\x12\x10\n\x0cTYPE_INVALID\x10\x00\x12\x0f\n\x0bTYPE_STATUS\x10\x01\x12\x11\n\rTYPE_SHARE_ID\x10\x02\x12\x0e\n\nTYPE_TX_ID\x10\x03\x42\x06\n\x04term\"\xb1\x01\n\x15ListTransfersResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12\x34\n\ttransfers\x18\x02 \x03(\x0b\x32\x16.cs3.tx.v1beta1.TxInfoR\ttransfers\x12\x31\n\x06opaque\x18\x03 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\"t\n\x14RetryTransferRequest\x12)\n\x05tx_id\x18\x01 \x01(\x0b\x32\x14.cs3.tx.v1beta1.TxIdR\x04txId\x12\x31\n\x06opaque\x18\x02 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque\"\xac\x01\n\x15RetryTransferResponse\x12/\n\x06status\x18\x01 \x01(\x0b\x32\x17.cs3.rpc.v1beta1.StatusR\x06status\x12/\n\x07tx_info\x18\x02 \x01(\x0b\x32\x16.cs3.tx.v1beta1.TxInfoR\x06txInfo\x12\x31\n\x06opaque\x18\x03 \x01(\x0b\x32\x19.cs3.types.v1beta1.OpaqueR\x06opaque2\xef\x03\n\x05TxAPI\x12_\n\x0e\x43reateTransfer\x12%.cs3.tx.v1beta1.CreateTransferRequest\x1a&.cs3.tx.v1beta1.CreateTransferResponse\x12h\n\x11GetTransferStatus\x12(.cs3.tx.v1beta1.GetTransferStatusRequest\x1a).cs3.tx.v1beta1.GetTransferStatusResponse\x12_\n\x0e\x43\x61ncelTransfer\x12%.cs3.tx.v1beta1.CancelTransferRequest\x1a&.cs3.tx.v1beta1.CancelTransferResponse\x12\\\n\rListTransfers\x12$.cs3.tx.v1beta1.ListTransfersRequest\x1a%.cs3.tx.v1beta1.ListTransfersResponse\x12\\\n\rRetryTransfer\x12$.cs3.tx.v1beta1.RetryTransferRequest\x1a%.cs3.tx.v1beta1.RetryTransferResponseB\xb1\x01\n\x12\x63om.cs3.tx.v1beta1B\nTxApiProtoP\x01Z5github.com/cs3org/go-cs3apis/cs3/tx/v1beta1;txv1beta1\xa2\x02\x03\x43TX\xaa\x02\x0e\x43s3.Tx.V1beta1\xca\x02\x0e\x43s3\\Tx\\V1beta1\xe2\x02\x1a\x43s3\\Tx\\V1beta1\\GPBMetadata\xea\x02\x10\x43s3::Tx::V1beta1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cs3.tx.v1beta1.tx_api_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\022com.cs3.tx.v1beta1B\nTxApiProtoP\001Z5github.com/cs3org/go-cs3apis/cs3/tx/v1beta1;txv1beta1\242\002\003CTX\252\002\016Cs3.Tx.V1beta1\312\002\016Cs3\\Tx\\V1beta1\342\002\032Cs3\\Tx\\V1beta1\\GPBMetadata\352\002\020Cs3::Tx::V1beta1'
  _globals['_CREATETRANSFERREQUEST']._serialized_start=182
  _globals['_CREATETRANSFERREQUEST']._serialized_end=395
  _globals['_CREATETRANSFERRESPONSE']._serialized_start=398
  _globals['_CREATETRANSFERRESPONSE']._serialized_end=571
  _globals['_GETTRANSFERSTATUSREQUEST']._serialized_start=573
  _globals['_GETTRANSFERSTATUSREQUEST']._serialized_end=693
  _globals['_GETTRANSFERSTATUSRESPONSE']._serialized_start=696
  _globals['_GETTRANSFERSTATUSRESPONSE']._serialized_end=872
  _globals['_CANCELTRANSFERREQUEST']._serialized_start=874
  _globals['_CANCELTRANSFERREQUEST']._serialized_end=991
  _globals['_CANCELTRANSFERRESPONSE']._serialized_start=994
  _globals['_CANCELTRANSFERRESPONSE']._serialized_end=1167
  _globals['_LISTTRANSFERSREQUEST']._serialized_start=1170
  _globals['_LISTTRANSFERSREQUEST']._serialized_end=1639
  _globals['_LISTTRANSFERSREQUEST_FILTER']._serialized_start=1317
  _globals['_LISTTRANSFERSREQUEST_FILTER']._serialized_end=1639
  _globals['_LISTTRANSFERSREQUEST_FILTER_TYPE']._serialized_start=1555
  _globals['_LISTTRANSFERSREQUEST_FILTER_TYPE']._serialized_end=1631
  _globals['_LISTTRANSFERSRESPONSE']._serialized_start=1642
  _globals['_LISTTRANSFERSRESPONSE']._serialized_end=1819
  _globals['_RETRYTRANSFERREQUEST']._serialized_start=1821
  _globals['_RETRYTRANSFERREQUEST']._serialized_end=1937
  _globals['_RETRYTRANSFERRESPONSE']._serialized_start=1940
  _globals['_RETRYTRANSFERRESPONSE']._serialized_end=2112
  _globals['_TXAPI']._serialized_start=2115
  _globals['_TXAPI']._serialized_end=2610
# @@protoc_insertion_point(module_scope)
