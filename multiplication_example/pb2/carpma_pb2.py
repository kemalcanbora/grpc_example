# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: carpma.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='carpma.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x63\x61rpma.proto\"\x1e\n\x06inputs\x12\t\n\x01\x61\x18\x04 \x03(\x02\x12\t\n\x01\x62\x18\x02 \x01(\x05\"\x19\n\x08return_x\x12\r\n\x05value\x18\x01 \x03(\x02\x32*\n\nCalculator\x12\x1c\n\x06\x63\x61rpma\x12\x07.inputs\x1a\t.return_xb\x06proto3')
)




_INPUTS = _descriptor.Descriptor(
  name='inputs',
  full_name='inputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='inputs.a', index=0,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b', full_name='inputs.b', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=46,
)


_RETURN_X = _descriptor.Descriptor(
  name='return_x',
  full_name='return_x',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='return_x.value', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=73,
)

DESCRIPTOR.message_types_by_name['inputs'] = _INPUTS
DESCRIPTOR.message_types_by_name['return_x'] = _RETURN_X
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

inputs = _reflection.GeneratedProtocolMessageType('inputs', (_message.Message,), dict(
  DESCRIPTOR = _INPUTS,
  __module__ = 'carpma_pb2'
  # @@protoc_insertion_point(class_scope:inputs)
  ))
_sym_db.RegisterMessage(inputs)

return_x = _reflection.GeneratedProtocolMessageType('return_x', (_message.Message,), dict(
  DESCRIPTOR = _RETURN_X,
  __module__ = 'carpma_pb2'
  # @@protoc_insertion_point(class_scope:return_x)
  ))
_sym_db.RegisterMessage(return_x)



_CALCULATOR = _descriptor.ServiceDescriptor(
  name='Calculator',
  full_name='Calculator',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=75,
  serialized_end=117,
  methods=[
  _descriptor.MethodDescriptor(
    name='carpma',
    full_name='Calculator.carpma',
    index=0,
    containing_service=None,
    input_type=_INPUTS,
    output_type=_RETURN_X,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATOR)

DESCRIPTOR.services_by_name['Calculator'] = _CALCULATOR

# @@protoc_insertion_point(module_scope)
