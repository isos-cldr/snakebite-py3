# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xattr.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='xattr.proto',
  package='hadoop.hdfs',
  syntax='proto2',
  serialized_options=_b('\n%org.apache.hadoop.hdfs.protocol.protoB\013XAttrProtos\240\001\001'),
  serialized_pb=_b('\n\x0bxattr.proto\x12\x0bhadoop.hdfs\"\xba\x01\n\nXAttrProto\x12>\n\tnamespace\x18\x01 \x02(\x0e\x32+.hadoop.hdfs.XAttrProto.XAttrNamespaceProto\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\r\n\x05value\x18\x03 \x01(\x0c\"O\n\x13XAttrNamespaceProto\x12\x08\n\x04USER\x10\x00\x12\x0b\n\x07TRUSTED\x10\x01\x12\x0c\n\x08SECURITY\x10\x02\x12\n\n\x06SYSTEM\x10\x03\x12\x07\n\x03RAW\x10\x04\"Y\n\x14SetXAttrRequestProto\x12\x0b\n\x03src\x18\x01 \x02(\t\x12&\n\x05xAttr\x18\x02 \x01(\x0b\x32\x17.hadoop.hdfs.XAttrProto\x12\x0c\n\x04\x66lag\x18\x03 \x01(\r\"\x17\n\x15SetXAttrResponseProto\"M\n\x15GetXAttrsRequestProto\x12\x0b\n\x03src\x18\x01 \x02(\t\x12\'\n\x06xAttrs\x18\x02 \x03(\x0b\x32\x17.hadoop.hdfs.XAttrProto\"A\n\x16GetXAttrsResponseProto\x12\'\n\x06xAttrs\x18\x01 \x03(\x0b\x32\x17.hadoop.hdfs.XAttrProto\"%\n\x16ListXAttrsRequestProto\x12\x0b\n\x03src\x18\x01 \x02(\t\"B\n\x17ListXAttrsResponseProto\x12\'\n\x06xAttrs\x18\x01 \x03(\x0b\x32\x17.hadoop.hdfs.XAttrProto\"N\n\x17RemoveXAttrRequestProto\x12\x0b\n\x03src\x18\x01 \x02(\t\x12&\n\x05xAttr\x18\x02 \x01(\x0b\x32\x17.hadoop.hdfs.XAttrProto\"\x1a\n\x18RemoveXAttrResponseProto*8\n\x11XAttrSetFlagProto\x12\x10\n\x0cXATTR_CREATE\x10\x01\x12\x11\n\rXATTR_REPLACE\x10\x02\x42\x37\n%org.apache.hadoop.hdfs.protocol.protoB\x0bXAttrProtos\xa0\x01\x01')
)

_XATTRSETFLAGPROTO = _descriptor.EnumDescriptor(
  name='XAttrSetFlagProto',
  full_name='hadoop.hdfs.XAttrSetFlagProto',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='XATTR_CREATE', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='XATTR_REPLACE', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=694,
  serialized_end=750,
)
_sym_db.RegisterEnumDescriptor(_XATTRSETFLAGPROTO)

XAttrSetFlagProto = enum_type_wrapper.EnumTypeWrapper(_XATTRSETFLAGPROTO)
XATTR_CREATE = 1
XATTR_REPLACE = 2


_XATTRPROTO_XATTRNAMESPACEPROTO = _descriptor.EnumDescriptor(
  name='XAttrNamespaceProto',
  full_name='hadoop.hdfs.XAttrProto.XAttrNamespaceProto',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRUSTED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SECURITY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYSTEM', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RAW', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=136,
  serialized_end=215,
)
_sym_db.RegisterEnumDescriptor(_XATTRPROTO_XATTRNAMESPACEPROTO)


_XATTRPROTO = _descriptor.Descriptor(
  name='XAttrProto',
  full_name='hadoop.hdfs.XAttrProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='hadoop.hdfs.XAttrProto.namespace', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='hadoop.hdfs.XAttrProto.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='hadoop.hdfs.XAttrProto.value', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _XATTRPROTO_XATTRNAMESPACEPROTO,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=215,
)


_SETXATTRREQUESTPROTO = _descriptor.Descriptor(
  name='SetXAttrRequestProto',
  full_name='hadoop.hdfs.SetXAttrRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='hadoop.hdfs.SetXAttrRequestProto.src', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xAttr', full_name='hadoop.hdfs.SetXAttrRequestProto.xAttr', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flag', full_name='hadoop.hdfs.SetXAttrRequestProto.flag', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=217,
  serialized_end=306,
)


_SETXATTRRESPONSEPROTO = _descriptor.Descriptor(
  name='SetXAttrResponseProto',
  full_name='hadoop.hdfs.SetXAttrResponseProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=308,
  serialized_end=331,
)


_GETXATTRSREQUESTPROTO = _descriptor.Descriptor(
  name='GetXAttrsRequestProto',
  full_name='hadoop.hdfs.GetXAttrsRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='hadoop.hdfs.GetXAttrsRequestProto.src', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xAttrs', full_name='hadoop.hdfs.GetXAttrsRequestProto.xAttrs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=333,
  serialized_end=410,
)


_GETXATTRSRESPONSEPROTO = _descriptor.Descriptor(
  name='GetXAttrsResponseProto',
  full_name='hadoop.hdfs.GetXAttrsResponseProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='xAttrs', full_name='hadoop.hdfs.GetXAttrsResponseProto.xAttrs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=412,
  serialized_end=477,
)


_LISTXATTRSREQUESTPROTO = _descriptor.Descriptor(
  name='ListXAttrsRequestProto',
  full_name='hadoop.hdfs.ListXAttrsRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='hadoop.hdfs.ListXAttrsRequestProto.src', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=479,
  serialized_end=516,
)


_LISTXATTRSRESPONSEPROTO = _descriptor.Descriptor(
  name='ListXAttrsResponseProto',
  full_name='hadoop.hdfs.ListXAttrsResponseProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='xAttrs', full_name='hadoop.hdfs.ListXAttrsResponseProto.xAttrs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=518,
  serialized_end=584,
)


_REMOVEXATTRREQUESTPROTO = _descriptor.Descriptor(
  name='RemoveXAttrRequestProto',
  full_name='hadoop.hdfs.RemoveXAttrRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='hadoop.hdfs.RemoveXAttrRequestProto.src', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xAttr', full_name='hadoop.hdfs.RemoveXAttrRequestProto.xAttr', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=586,
  serialized_end=664,
)


_REMOVEXATTRRESPONSEPROTO = _descriptor.Descriptor(
  name='RemoveXAttrResponseProto',
  full_name='hadoop.hdfs.RemoveXAttrResponseProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=666,
  serialized_end=692,
)

_XATTRPROTO.fields_by_name['namespace'].enum_type = _XATTRPROTO_XATTRNAMESPACEPROTO
_XATTRPROTO_XATTRNAMESPACEPROTO.containing_type = _XATTRPROTO
_SETXATTRREQUESTPROTO.fields_by_name['xAttr'].message_type = _XATTRPROTO
_GETXATTRSREQUESTPROTO.fields_by_name['xAttrs'].message_type = _XATTRPROTO
_GETXATTRSRESPONSEPROTO.fields_by_name['xAttrs'].message_type = _XATTRPROTO
_LISTXATTRSRESPONSEPROTO.fields_by_name['xAttrs'].message_type = _XATTRPROTO
_REMOVEXATTRREQUESTPROTO.fields_by_name['xAttr'].message_type = _XATTRPROTO
DESCRIPTOR.message_types_by_name['XAttrProto'] = _XATTRPROTO
DESCRIPTOR.message_types_by_name['SetXAttrRequestProto'] = _SETXATTRREQUESTPROTO
DESCRIPTOR.message_types_by_name['SetXAttrResponseProto'] = _SETXATTRRESPONSEPROTO
DESCRIPTOR.message_types_by_name['GetXAttrsRequestProto'] = _GETXATTRSREQUESTPROTO
DESCRIPTOR.message_types_by_name['GetXAttrsResponseProto'] = _GETXATTRSRESPONSEPROTO
DESCRIPTOR.message_types_by_name['ListXAttrsRequestProto'] = _LISTXATTRSREQUESTPROTO
DESCRIPTOR.message_types_by_name['ListXAttrsResponseProto'] = _LISTXATTRSRESPONSEPROTO
DESCRIPTOR.message_types_by_name['RemoveXAttrRequestProto'] = _REMOVEXATTRREQUESTPROTO
DESCRIPTOR.message_types_by_name['RemoveXAttrResponseProto'] = _REMOVEXATTRRESPONSEPROTO
DESCRIPTOR.enum_types_by_name['XAttrSetFlagProto'] = _XATTRSETFLAGPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

XAttrProto = _reflection.GeneratedProtocolMessageType('XAttrProto', (_message.Message,), dict(
  DESCRIPTOR = _XATTRPROTO,
  __module__ = 'xattr_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.XAttrProto)
  ))
_sym_db.RegisterMessage(XAttrProto)

SetXAttrRequestProto = _reflection.GeneratedProtocolMessageType('SetXAttrRequestProto', (_message.Message,), dict(
  DESCRIPTOR = _SETXATTRREQUESTPROTO,
  __module__ = 'xattr_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.SetXAttrRequestProto)
  ))
_sym_db.RegisterMessage(SetXAttrRequestProto)

SetXAttrResponseProto = _reflection.GeneratedProtocolMessageType('SetXAttrResponseProto', (_message.Message,), dict(
  DESCRIPTOR = _SETXATTRRESPONSEPROTO,
  __module__ = 'xattr_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.SetXAttrResponseProto)
  ))
_sym_db.RegisterMessage(SetXAttrResponseProto)

GetXAttrsRequestProto = _reflection.GeneratedProtocolMessageType('GetXAttrsRequestProto', (_message.Message,), dict(
  DESCRIPTOR = _GETXATTRSREQUESTPROTO,
  __module__ = 'xattr_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.GetXAttrsRequestProto)
  ))
_sym_db.RegisterMessage(GetXAttrsRequestProto)

GetXAttrsResponseProto = _reflection.GeneratedProtocolMessageType('GetXAttrsResponseProto', (_message.Message,), dict(
  DESCRIPTOR = _GETXATTRSRESPONSEPROTO,
  __module__ = 'xattr_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.GetXAttrsResponseProto)
  ))
_sym_db.RegisterMessage(GetXAttrsResponseProto)

ListXAttrsRequestProto = _reflection.GeneratedProtocolMessageType('ListXAttrsRequestProto', (_message.Message,), dict(
  DESCRIPTOR = _LISTXATTRSREQUESTPROTO,
  __module__ = 'xattr_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.ListXAttrsRequestProto)
  ))
_sym_db.RegisterMessage(ListXAttrsRequestProto)

ListXAttrsResponseProto = _reflection.GeneratedProtocolMessageType('ListXAttrsResponseProto', (_message.Message,), dict(
  DESCRIPTOR = _LISTXATTRSRESPONSEPROTO,
  __module__ = 'xattr_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.ListXAttrsResponseProto)
  ))
_sym_db.RegisterMessage(ListXAttrsResponseProto)

RemoveXAttrRequestProto = _reflection.GeneratedProtocolMessageType('RemoveXAttrRequestProto', (_message.Message,), dict(
  DESCRIPTOR = _REMOVEXATTRREQUESTPROTO,
  __module__ = 'xattr_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.RemoveXAttrRequestProto)
  ))
_sym_db.RegisterMessage(RemoveXAttrRequestProto)

RemoveXAttrResponseProto = _reflection.GeneratedProtocolMessageType('RemoveXAttrResponseProto', (_message.Message,), dict(
  DESCRIPTOR = _REMOVEXATTRRESPONSEPROTO,
  __module__ = 'xattr_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.RemoveXAttrResponseProto)
  ))
_sym_db.RegisterMessage(RemoveXAttrResponseProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
