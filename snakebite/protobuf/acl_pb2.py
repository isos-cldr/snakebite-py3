# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: acl.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='acl.proto',
  package='hadoop.hdfs',
  syntax='proto2',
  serialized_options=_b('\n%org.apache.hadoop.hdfs.protocol.protoB\tAclProtos\240\001\001'),
  serialized_pb=_b('\n\tacl.proto\x12\x0bhadoop.hdfs\"!\n\x11\x46sPermissionProto\x12\x0c\n\x04perm\x18\x01 \x02(\r\"\xc4\x03\n\rAclEntryProto\x12:\n\x04type\x18\x01 \x02(\x0e\x32,.hadoop.hdfs.AclEntryProto.AclEntryTypeProto\x12<\n\x05scope\x18\x02 \x02(\x0e\x32-.hadoop.hdfs.AclEntryProto.AclEntryScopeProto\x12=\n\x0bpermissions\x18\x03 \x02(\x0e\x32(.hadoop.hdfs.AclEntryProto.FsActionProto\x12\x0c\n\x04name\x18\x04 \x01(\t\"-\n\x12\x41\x63lEntryScopeProto\x12\n\n\x06\x41\x43\x43\x45SS\x10\x00\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x01\"=\n\x11\x41\x63lEntryTypeProto\x12\x08\n\x04USER\x10\x00\x12\t\n\x05GROUP\x10\x01\x12\x08\n\x04MASK\x10\x02\x12\t\n\x05OTHER\x10\x03\"~\n\rFsActionProto\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07\x45XECUTE\x10\x01\x12\t\n\x05WRITE\x10\x02\x12\x11\n\rWRITE_EXECUTE\x10\x03\x12\x08\n\x04READ\x10\x04\x12\x10\n\x0cREAD_EXECUTE\x10\x05\x12\x0e\n\nREAD_WRITE\x10\x06\x12\x0c\n\x08PERM_ALL\x10\x07\"\x9f\x01\n\x0e\x41\x63lStatusProto\x12\r\n\x05owner\x18\x01 \x02(\t\x12\r\n\x05group\x18\x02 \x02(\t\x12\x0e\n\x06sticky\x18\x03 \x02(\x08\x12+\n\x07\x65ntries\x18\x04 \x03(\x0b\x32\x1a.hadoop.hdfs.AclEntryProto\x12\x32\n\npermission\x18\x05 \x01(\x0b\x32\x1e.hadoop.hdfs.FsPermissionProto\"X\n\x1cModifyAclEntriesRequestProto\x12\x0b\n\x03src\x18\x01 \x02(\t\x12+\n\x07\x61\x63lSpec\x18\x02 \x03(\x0b\x32\x1a.hadoop.hdfs.AclEntryProto\"\x1f\n\x1dModifyAclEntriesResponseProto\"$\n\x15RemoveAclRequestProto\x12\x0b\n\x03src\x18\x01 \x02(\t\"\x18\n\x16RemoveAclResponseProto\"X\n\x1cRemoveAclEntriesRequestProto\x12\x0b\n\x03src\x18\x01 \x02(\t\x12+\n\x07\x61\x63lSpec\x18\x02 \x03(\x0b\x32\x1a.hadoop.hdfs.AclEntryProto\"\x1f\n\x1dRemoveAclEntriesResponseProto\"+\n\x1cRemoveDefaultAclRequestProto\x12\x0b\n\x03src\x18\x01 \x02(\t\"\x1f\n\x1dRemoveDefaultAclResponseProto\"N\n\x12SetAclRequestProto\x12\x0b\n\x03src\x18\x01 \x02(\t\x12+\n\x07\x61\x63lSpec\x18\x02 \x03(\x0b\x32\x1a.hadoop.hdfs.AclEntryProto\"\x15\n\x13SetAclResponseProto\"\'\n\x18GetAclStatusRequestProto\x12\x0b\n\x03src\x18\x01 \x02(\t\"H\n\x19GetAclStatusResponseProto\x12+\n\x06result\x18\x01 \x02(\x0b\x32\x1b.hadoop.hdfs.AclStatusProtoB5\n%org.apache.hadoop.hdfs.protocol.protoB\tAclProtos\xa0\x01\x01')
)



_ACLENTRYPROTO_ACLENTRYSCOPEPROTO = _descriptor.EnumDescriptor(
  name='AclEntryScopeProto',
  full_name='hadoop.hdfs.AclEntryProto.AclEntryScopeProto',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACCESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=278,
  serialized_end=323,
)
_sym_db.RegisterEnumDescriptor(_ACLENTRYPROTO_ACLENTRYSCOPEPROTO)

_ACLENTRYPROTO_ACLENTRYTYPEPROTO = _descriptor.EnumDescriptor(
  name='AclEntryTypeProto',
  full_name='hadoop.hdfs.AclEntryProto.AclEntryTypeProto',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USER', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MASK', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=325,
  serialized_end=386,
)
_sym_db.RegisterEnumDescriptor(_ACLENTRYPROTO_ACLENTRYTYPEPROTO)

_ACLENTRYPROTO_FSACTIONPROTO = _descriptor.EnumDescriptor(
  name='FsActionProto',
  full_name='hadoop.hdfs.AclEntryProto.FsActionProto',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXECUTE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRITE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRITE_EXECUTE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ_EXECUTE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READ_WRITE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERM_ALL', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=388,
  serialized_end=514,
)
_sym_db.RegisterEnumDescriptor(_ACLENTRYPROTO_FSACTIONPROTO)


_FSPERMISSIONPROTO = _descriptor.Descriptor(
  name='FsPermissionProto',
  full_name='hadoop.hdfs.FsPermissionProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='perm', full_name='hadoop.hdfs.FsPermissionProto.perm', index=0,
      number=1, type=13, cpp_type=3, label=2,
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
  serialized_start=26,
  serialized_end=59,
)


_ACLENTRYPROTO = _descriptor.Descriptor(
  name='AclEntryProto',
  full_name='hadoop.hdfs.AclEntryProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='hadoop.hdfs.AclEntryProto.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scope', full_name='hadoop.hdfs.AclEntryProto.scope', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permissions', full_name='hadoop.hdfs.AclEntryProto.permissions', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='hadoop.hdfs.AclEntryProto.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACLENTRYPROTO_ACLENTRYSCOPEPROTO,
    _ACLENTRYPROTO_ACLENTRYTYPEPROTO,
    _ACLENTRYPROTO_FSACTIONPROTO,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=514,
)


_ACLSTATUSPROTO = _descriptor.Descriptor(
  name='AclStatusProto',
  full_name='hadoop.hdfs.AclStatusProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner', full_name='hadoop.hdfs.AclStatusProto.owner', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group', full_name='hadoop.hdfs.AclStatusProto.group', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sticky', full_name='hadoop.hdfs.AclStatusProto.sticky', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entries', full_name='hadoop.hdfs.AclStatusProto.entries', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permission', full_name='hadoop.hdfs.AclStatusProto.permission', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=517,
  serialized_end=676,
)


_MODIFYACLENTRIESREQUESTPROTO = _descriptor.Descriptor(
  name='ModifyAclEntriesRequestProto',
  full_name='hadoop.hdfs.ModifyAclEntriesRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='hadoop.hdfs.ModifyAclEntriesRequestProto.src', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aclSpec', full_name='hadoop.hdfs.ModifyAclEntriesRequestProto.aclSpec', index=1,
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
  serialized_start=678,
  serialized_end=766,
)


_MODIFYACLENTRIESRESPONSEPROTO = _descriptor.Descriptor(
  name='ModifyAclEntriesResponseProto',
  full_name='hadoop.hdfs.ModifyAclEntriesResponseProto',
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
  serialized_start=768,
  serialized_end=799,
)


_REMOVEACLREQUESTPROTO = _descriptor.Descriptor(
  name='RemoveAclRequestProto',
  full_name='hadoop.hdfs.RemoveAclRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='hadoop.hdfs.RemoveAclRequestProto.src', index=0,
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
  serialized_start=801,
  serialized_end=837,
)


_REMOVEACLRESPONSEPROTO = _descriptor.Descriptor(
  name='RemoveAclResponseProto',
  full_name='hadoop.hdfs.RemoveAclResponseProto',
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
  serialized_start=839,
  serialized_end=863,
)


_REMOVEACLENTRIESREQUESTPROTO = _descriptor.Descriptor(
  name='RemoveAclEntriesRequestProto',
  full_name='hadoop.hdfs.RemoveAclEntriesRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='hadoop.hdfs.RemoveAclEntriesRequestProto.src', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aclSpec', full_name='hadoop.hdfs.RemoveAclEntriesRequestProto.aclSpec', index=1,
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
  serialized_start=865,
  serialized_end=953,
)


_REMOVEACLENTRIESRESPONSEPROTO = _descriptor.Descriptor(
  name='RemoveAclEntriesResponseProto',
  full_name='hadoop.hdfs.RemoveAclEntriesResponseProto',
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
  serialized_start=955,
  serialized_end=986,
)


_REMOVEDEFAULTACLREQUESTPROTO = _descriptor.Descriptor(
  name='RemoveDefaultAclRequestProto',
  full_name='hadoop.hdfs.RemoveDefaultAclRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='hadoop.hdfs.RemoveDefaultAclRequestProto.src', index=0,
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
  serialized_start=988,
  serialized_end=1031,
)


_REMOVEDEFAULTACLRESPONSEPROTO = _descriptor.Descriptor(
  name='RemoveDefaultAclResponseProto',
  full_name='hadoop.hdfs.RemoveDefaultAclResponseProto',
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
  serialized_start=1033,
  serialized_end=1064,
)


_SETACLREQUESTPROTO = _descriptor.Descriptor(
  name='SetAclRequestProto',
  full_name='hadoop.hdfs.SetAclRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='hadoop.hdfs.SetAclRequestProto.src', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aclSpec', full_name='hadoop.hdfs.SetAclRequestProto.aclSpec', index=1,
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
  serialized_start=1066,
  serialized_end=1144,
)


_SETACLRESPONSEPROTO = _descriptor.Descriptor(
  name='SetAclResponseProto',
  full_name='hadoop.hdfs.SetAclResponseProto',
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
  serialized_start=1146,
  serialized_end=1167,
)


_GETACLSTATUSREQUESTPROTO = _descriptor.Descriptor(
  name='GetAclStatusRequestProto',
  full_name='hadoop.hdfs.GetAclStatusRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='hadoop.hdfs.GetAclStatusRequestProto.src', index=0,
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
  serialized_start=1169,
  serialized_end=1208,
)


_GETACLSTATUSRESPONSEPROTO = _descriptor.Descriptor(
  name='GetAclStatusResponseProto',
  full_name='hadoop.hdfs.GetAclStatusResponseProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='hadoop.hdfs.GetAclStatusResponseProto.result', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  serialized_start=1210,
  serialized_end=1282,
)

_ACLENTRYPROTO.fields_by_name['type'].enum_type = _ACLENTRYPROTO_ACLENTRYTYPEPROTO
_ACLENTRYPROTO.fields_by_name['scope'].enum_type = _ACLENTRYPROTO_ACLENTRYSCOPEPROTO
_ACLENTRYPROTO.fields_by_name['permissions'].enum_type = _ACLENTRYPROTO_FSACTIONPROTO
_ACLENTRYPROTO_ACLENTRYSCOPEPROTO.containing_type = _ACLENTRYPROTO
_ACLENTRYPROTO_ACLENTRYTYPEPROTO.containing_type = _ACLENTRYPROTO
_ACLENTRYPROTO_FSACTIONPROTO.containing_type = _ACLENTRYPROTO
_ACLSTATUSPROTO.fields_by_name['entries'].message_type = _ACLENTRYPROTO
_ACLSTATUSPROTO.fields_by_name['permission'].message_type = _FSPERMISSIONPROTO
_MODIFYACLENTRIESREQUESTPROTO.fields_by_name['aclSpec'].message_type = _ACLENTRYPROTO
_REMOVEACLENTRIESREQUESTPROTO.fields_by_name['aclSpec'].message_type = _ACLENTRYPROTO
_SETACLREQUESTPROTO.fields_by_name['aclSpec'].message_type = _ACLENTRYPROTO
_GETACLSTATUSRESPONSEPROTO.fields_by_name['result'].message_type = _ACLSTATUSPROTO
DESCRIPTOR.message_types_by_name['FsPermissionProto'] = _FSPERMISSIONPROTO
DESCRIPTOR.message_types_by_name['AclEntryProto'] = _ACLENTRYPROTO
DESCRIPTOR.message_types_by_name['AclStatusProto'] = _ACLSTATUSPROTO
DESCRIPTOR.message_types_by_name['ModifyAclEntriesRequestProto'] = _MODIFYACLENTRIESREQUESTPROTO
DESCRIPTOR.message_types_by_name['ModifyAclEntriesResponseProto'] = _MODIFYACLENTRIESRESPONSEPROTO
DESCRIPTOR.message_types_by_name['RemoveAclRequestProto'] = _REMOVEACLREQUESTPROTO
DESCRIPTOR.message_types_by_name['RemoveAclResponseProto'] = _REMOVEACLRESPONSEPROTO
DESCRIPTOR.message_types_by_name['RemoveAclEntriesRequestProto'] = _REMOVEACLENTRIESREQUESTPROTO
DESCRIPTOR.message_types_by_name['RemoveAclEntriesResponseProto'] = _REMOVEACLENTRIESRESPONSEPROTO
DESCRIPTOR.message_types_by_name['RemoveDefaultAclRequestProto'] = _REMOVEDEFAULTACLREQUESTPROTO
DESCRIPTOR.message_types_by_name['RemoveDefaultAclResponseProto'] = _REMOVEDEFAULTACLRESPONSEPROTO
DESCRIPTOR.message_types_by_name['SetAclRequestProto'] = _SETACLREQUESTPROTO
DESCRIPTOR.message_types_by_name['SetAclResponseProto'] = _SETACLRESPONSEPROTO
DESCRIPTOR.message_types_by_name['GetAclStatusRequestProto'] = _GETACLSTATUSREQUESTPROTO
DESCRIPTOR.message_types_by_name['GetAclStatusResponseProto'] = _GETACLSTATUSRESPONSEPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FsPermissionProto = _reflection.GeneratedProtocolMessageType('FsPermissionProto', (_message.Message,), dict(
  DESCRIPTOR = _FSPERMISSIONPROTO,
  __module__ = 'acl_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.FsPermissionProto)
  ))
_sym_db.RegisterMessage(FsPermissionProto)

AclEntryProto = _reflection.GeneratedProtocolMessageType('AclEntryProto', (_message.Message,), dict(
  DESCRIPTOR = _ACLENTRYPROTO,
  __module__ = 'acl_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.AclEntryProto)
  ))
_sym_db.RegisterMessage(AclEntryProto)

AclStatusProto = _reflection.GeneratedProtocolMessageType('AclStatusProto', (_message.Message,), dict(
  DESCRIPTOR = _ACLSTATUSPROTO,
  __module__ = 'acl_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.AclStatusProto)
  ))
_sym_db.RegisterMessage(AclStatusProto)

ModifyAclEntriesRequestProto = _reflection.GeneratedProtocolMessageType('ModifyAclEntriesRequestProto', (_message.Message,), dict(
  DESCRIPTOR = _MODIFYACLENTRIESREQUESTPROTO,
  __module__ = 'acl_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.ModifyAclEntriesRequestProto)
  ))
_sym_db.RegisterMessage(ModifyAclEntriesRequestProto)

ModifyAclEntriesResponseProto = _reflection.GeneratedProtocolMessageType('ModifyAclEntriesResponseProto', (_message.Message,), dict(
  DESCRIPTOR = _MODIFYACLENTRIESRESPONSEPROTO,
  __module__ = 'acl_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.ModifyAclEntriesResponseProto)
  ))
_sym_db.RegisterMessage(ModifyAclEntriesResponseProto)

RemoveAclRequestProto = _reflection.GeneratedProtocolMessageType('RemoveAclRequestProto', (_message.Message,), dict(
  DESCRIPTOR = _REMOVEACLREQUESTPROTO,
  __module__ = 'acl_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.RemoveAclRequestProto)
  ))
_sym_db.RegisterMessage(RemoveAclRequestProto)

RemoveAclResponseProto = _reflection.GeneratedProtocolMessageType('RemoveAclResponseProto', (_message.Message,), dict(
  DESCRIPTOR = _REMOVEACLRESPONSEPROTO,
  __module__ = 'acl_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.RemoveAclResponseProto)
  ))
_sym_db.RegisterMessage(RemoveAclResponseProto)

RemoveAclEntriesRequestProto = _reflection.GeneratedProtocolMessageType('RemoveAclEntriesRequestProto', (_message.Message,), dict(
  DESCRIPTOR = _REMOVEACLENTRIESREQUESTPROTO,
  __module__ = 'acl_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.RemoveAclEntriesRequestProto)
  ))
_sym_db.RegisterMessage(RemoveAclEntriesRequestProto)

RemoveAclEntriesResponseProto = _reflection.GeneratedProtocolMessageType('RemoveAclEntriesResponseProto', (_message.Message,), dict(
  DESCRIPTOR = _REMOVEACLENTRIESRESPONSEPROTO,
  __module__ = 'acl_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.RemoveAclEntriesResponseProto)
  ))
_sym_db.RegisterMessage(RemoveAclEntriesResponseProto)

RemoveDefaultAclRequestProto = _reflection.GeneratedProtocolMessageType('RemoveDefaultAclRequestProto', (_message.Message,), dict(
  DESCRIPTOR = _REMOVEDEFAULTACLREQUESTPROTO,
  __module__ = 'acl_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.RemoveDefaultAclRequestProto)
  ))
_sym_db.RegisterMessage(RemoveDefaultAclRequestProto)

RemoveDefaultAclResponseProto = _reflection.GeneratedProtocolMessageType('RemoveDefaultAclResponseProto', (_message.Message,), dict(
  DESCRIPTOR = _REMOVEDEFAULTACLRESPONSEPROTO,
  __module__ = 'acl_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.RemoveDefaultAclResponseProto)
  ))
_sym_db.RegisterMessage(RemoveDefaultAclResponseProto)

SetAclRequestProto = _reflection.GeneratedProtocolMessageType('SetAclRequestProto', (_message.Message,), dict(
  DESCRIPTOR = _SETACLREQUESTPROTO,
  __module__ = 'acl_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.SetAclRequestProto)
  ))
_sym_db.RegisterMessage(SetAclRequestProto)

SetAclResponseProto = _reflection.GeneratedProtocolMessageType('SetAclResponseProto', (_message.Message,), dict(
  DESCRIPTOR = _SETACLRESPONSEPROTO,
  __module__ = 'acl_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.SetAclResponseProto)
  ))
_sym_db.RegisterMessage(SetAclResponseProto)

GetAclStatusRequestProto = _reflection.GeneratedProtocolMessageType('GetAclStatusRequestProto', (_message.Message,), dict(
  DESCRIPTOR = _GETACLSTATUSREQUESTPROTO,
  __module__ = 'acl_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.GetAclStatusRequestProto)
  ))
_sym_db.RegisterMessage(GetAclStatusRequestProto)

GetAclStatusResponseProto = _reflection.GeneratedProtocolMessageType('GetAclStatusResponseProto', (_message.Message,), dict(
  DESCRIPTOR = _GETACLSTATUSRESPONSEPROTO,
  __module__ = 'acl_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.GetAclStatusResponseProto)
  ))
_sym_db.RegisterMessage(GetAclStatusResponseProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
