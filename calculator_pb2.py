# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: calculator.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'calculator.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63\x61lculator.proto\"(\n\x10OperationRequest\x12\t\n\x01\x61\x18\x01 \x01(\x01\x12\t\n\x01\x62\x18\x02 \x01(\x01\"#\n\x11OperationResponse\x12\x0e\n\x06result\x18\x01 \x01(\x01\x32\xd1\x01\n\nCalculator\x12,\n\x03\x41\x64\x64\x12\x11.OperationRequest\x1a\x12.OperationResponse\x12\x31\n\x08Subtract\x12\x11.OperationRequest\x1a\x12.OperationResponse\x12\x31\n\x08Multiply\x12\x11.OperationRequest\x1a\x12.OperationResponse\x12/\n\x06\x44ivide\x12\x11.OperationRequest\x1a\x12.OperationResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'calculator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_OPERATIONREQUEST']._serialized_start=20
  _globals['_OPERATIONREQUEST']._serialized_end=60
  _globals['_OPERATIONRESPONSE']._serialized_start=62
  _globals['_OPERATIONRESPONSE']._serialized_end=97
  _globals['_CALCULATOR']._serialized_start=100
  _globals['_CALCULATOR']._serialized_end=309
# @@protoc_insertion_point(module_scope)
