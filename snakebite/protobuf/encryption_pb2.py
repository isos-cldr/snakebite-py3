# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: encryption.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import hdfs_pb2 as hdfs__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='encryption.proto',
  package='hadoop.hdfs',
  syntax='proto2',
  serialized_options=_b('\n%org.apache.hadoop.hdfs.protocol.protoB\025EncryptionZonesProtos\240\001\001'),
  serialized_pb=_b('\n\x10\x65ncryption.proto\x12\x0bhadoop.hdfs\x1a\nhdfs.proto\"@\n CreateEncryptionZoneRequestProto\x12\x0b\n\x03src\x18\x01 \x02(\t\x12\x0f\n\x07keyName\x18\x02 \x01(\t\"#\n!CreateEncryptionZoneResponseProto\"-\n\x1fListEncryptionZonesRequestProto\x12\n\n\x02id\x18\x01 \x02(\x03\"\xb6\x01\n\x13\x45ncryptionZoneProto\x12\n\n\x02id\x18\x01 \x02(\x03\x12\x0c\n\x04path\x18\x02 \x02(\t\x12,\n\x05suite\x18\x03 \x02(\x0e\x32\x1d.hadoop.hdfs.CipherSuiteProto\x12\x46\n\x15\x63ryptoProtocolVersion\x18\x04 \x02(\x0e\x32\'.hadoop.hdfs.CryptoProtocolVersionProto\x12\x0f\n\x07keyName\x18\x05 \x02(\t\"d\n ListEncryptionZonesResponseProto\x12/\n\x05zones\x18\x01 \x03(\x0b\x32 .hadoop.hdfs.EncryptionZoneProto\x12\x0f\n\x07hasMore\x18\x02 \x02(\x08\"f\n#ReencryptEncryptionZoneRequestProto\x12\x31\n\x06\x61\x63tion\x18\x01 \x02(\x0e\x32!.hadoop.hdfs.ReencryptActionProto\x12\x0c\n\x04zone\x18\x02 \x02(\t\"&\n$ReencryptEncryptionZoneResponseProto\"0\n\"ListReencryptionStatusRequestProto\x12\n\n\x02id\x18\x01 \x02(\x03\"\x86\x02\n\x1bZoneReencryptionStatusProto\x12\n\n\x02id\x18\x01 \x02(\x03\x12\x0c\n\x04path\x18\x02 \x02(\t\x12\x32\n\x05state\x18\x03 \x02(\x0e\x32#.hadoop.hdfs.ReencryptionStateProto\x12\x18\n\x10\x65zKeyVersionName\x18\x04 \x02(\t\x12\x16\n\x0esubmissionTime\x18\x05 \x02(\x03\x12\x10\n\x08\x63\x61nceled\x18\x06 \x02(\x08\x12\x16\n\x0enumReencrypted\x18\x07 \x02(\x03\x12\x13\n\x0bnumFailures\x18\x08 \x02(\x03\x12\x16\n\x0e\x63ompletionTime\x18\t \x01(\x03\x12\x10\n\x08lastFile\x18\n \x01(\t\"r\n#ListReencryptionStatusResponseProto\x12:\n\x08statuses\x18\x01 \x03(\x0b\x32(.hadoop.hdfs.ZoneReencryptionStatusProto\x12\x0f\n\x07hasMore\x18\x02 \x02(\x08\"\'\n\x18GetEZForPathRequestProto\x12\x0b\n\x03src\x18\x01 \x02(\t\"K\n\x19GetEZForPathResponseProto\x12.\n\x04zone\x18\x01 \x01(\x0b\x32 .hadoop.hdfs.EncryptionZoneProto*A\n\x14ReencryptActionProto\x12\x14\n\x10\x43\x41NCEL_REENCRYPT\x10\x01\x12\x13\n\x0fSTART_REENCRYPT\x10\x02*F\n\x16ReencryptionStateProto\x12\r\n\tSUBMITTED\x10\x01\x12\x0e\n\nPROCESSING\x10\x02\x12\r\n\tCOMPLETED\x10\x03\x42\x41\n%org.apache.hadoop.hdfs.protocol.protoB\x15\x45ncryptionZonesProtos\xa0\x01\x01')
  ,
  dependencies=[hdfs__pb2.DESCRIPTOR,])

_REENCRYPTACTIONPROTO = _descriptor.EnumDescriptor(
  name='ReencryptActionProto',
  full_name='hadoop.hdfs.ReencryptActionProto',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CANCEL_REENCRYPT', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START_REENCRYPT', index=1, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1175,
  serialized_end=1240,
)
_sym_db.RegisterEnumDescriptor(_REENCRYPTACTIONPROTO)

ReencryptActionProto = enum_type_wrapper.EnumTypeWrapper(_REENCRYPTACTIONPROTO)
_REENCRYPTIONSTATEPROTO = _descriptor.EnumDescriptor(
  name='ReencryptionStateProto',
  full_name='hadoop.hdfs.ReencryptionStateProto',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUBMITTED', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROCESSING', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=2, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1242,
  serialized_end=1312,
)
_sym_db.RegisterEnumDescriptor(_REENCRYPTIONSTATEPROTO)

ReencryptionStateProto = enum_type_wrapper.EnumTypeWrapper(_REENCRYPTIONSTATEPROTO)
CANCEL_REENCRYPT = 1
START_REENCRYPT = 2
SUBMITTED = 1
PROCESSING = 2
COMPLETED = 3



_CREATEENCRYPTIONZONEREQUESTPROTO = _descriptor.Descriptor(
  name='CreateEncryptionZoneRequestProto',
  full_name='hadoop.hdfs.CreateEncryptionZoneRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='hadoop.hdfs.CreateEncryptionZoneRequestProto.src', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyName', full_name='hadoop.hdfs.CreateEncryptionZoneRequestProto.keyName', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=45,
  serialized_end=109,
)


_CREATEENCRYPTIONZONERESPONSEPROTO = _descriptor.Descriptor(
  name='CreateEncryptionZoneResponseProto',
  full_name='hadoop.hdfs.CreateEncryptionZoneResponseProto',
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
  serialized_start=111,
  serialized_end=146,
)


_LISTENCRYPTIONZONESREQUESTPROTO = _descriptor.Descriptor(
  name='ListEncryptionZonesRequestProto',
  full_name='hadoop.hdfs.ListEncryptionZonesRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hadoop.hdfs.ListEncryptionZonesRequestProto.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
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
  serialized_start=148,
  serialized_end=193,
)


_ENCRYPTIONZONEPROTO = _descriptor.Descriptor(
  name='EncryptionZoneProto',
  full_name='hadoop.hdfs.EncryptionZoneProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hadoop.hdfs.EncryptionZoneProto.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='hadoop.hdfs.EncryptionZoneProto.path', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suite', full_name='hadoop.hdfs.EncryptionZoneProto.suite', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cryptoProtocolVersion', full_name='hadoop.hdfs.EncryptionZoneProto.cryptoProtocolVersion', index=3,
      number=4, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyName', full_name='hadoop.hdfs.EncryptionZoneProto.keyName', index=4,
      number=5, type=9, cpp_type=9, label=2,
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
  serialized_start=196,
  serialized_end=378,
)


_LISTENCRYPTIONZONESRESPONSEPROTO = _descriptor.Descriptor(
  name='ListEncryptionZonesResponseProto',
  full_name='hadoop.hdfs.ListEncryptionZonesResponseProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='zones', full_name='hadoop.hdfs.ListEncryptionZonesResponseProto.zones', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hasMore', full_name='hadoop.hdfs.ListEncryptionZonesResponseProto.hasMore', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=380,
  serialized_end=480,
)


_REENCRYPTENCRYPTIONZONEREQUESTPROTO = _descriptor.Descriptor(
  name='ReencryptEncryptionZoneRequestProto',
  full_name='hadoop.hdfs.ReencryptEncryptionZoneRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='hadoop.hdfs.ReencryptEncryptionZoneRequestProto.action', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zone', full_name='hadoop.hdfs.ReencryptEncryptionZoneRequestProto.zone', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=482,
  serialized_end=584,
)


_REENCRYPTENCRYPTIONZONERESPONSEPROTO = _descriptor.Descriptor(
  name='ReencryptEncryptionZoneResponseProto',
  full_name='hadoop.hdfs.ReencryptEncryptionZoneResponseProto',
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
  serialized_start=586,
  serialized_end=624,
)


_LISTREENCRYPTIONSTATUSREQUESTPROTO = _descriptor.Descriptor(
  name='ListReencryptionStatusRequestProto',
  full_name='hadoop.hdfs.ListReencryptionStatusRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hadoop.hdfs.ListReencryptionStatusRequestProto.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
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
  serialized_start=626,
  serialized_end=674,
)


_ZONEREENCRYPTIONSTATUSPROTO = _descriptor.Descriptor(
  name='ZoneReencryptionStatusProto',
  full_name='hadoop.hdfs.ZoneReencryptionStatusProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hadoop.hdfs.ZoneReencryptionStatusProto.id', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='hadoop.hdfs.ZoneReencryptionStatusProto.path', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='hadoop.hdfs.ZoneReencryptionStatusProto.state', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ezKeyVersionName', full_name='hadoop.hdfs.ZoneReencryptionStatusProto.ezKeyVersionName', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='submissionTime', full_name='hadoop.hdfs.ZoneReencryptionStatusProto.submissionTime', index=4,
      number=5, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='canceled', full_name='hadoop.hdfs.ZoneReencryptionStatusProto.canceled', index=5,
      number=6, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numReencrypted', full_name='hadoop.hdfs.ZoneReencryptionStatusProto.numReencrypted', index=6,
      number=7, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numFailures', full_name='hadoop.hdfs.ZoneReencryptionStatusProto.numFailures', index=7,
      number=8, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='completionTime', full_name='hadoop.hdfs.ZoneReencryptionStatusProto.completionTime', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastFile', full_name='hadoop.hdfs.ZoneReencryptionStatusProto.lastFile', index=9,
      number=10, type=9, cpp_type=9, label=1,
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
  serialized_start=677,
  serialized_end=939,
)


_LISTREENCRYPTIONSTATUSRESPONSEPROTO = _descriptor.Descriptor(
  name='ListReencryptionStatusResponseProto',
  full_name='hadoop.hdfs.ListReencryptionStatusResponseProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='statuses', full_name='hadoop.hdfs.ListReencryptionStatusResponseProto.statuses', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hasMore', full_name='hadoop.hdfs.ListReencryptionStatusResponseProto.hasMore', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=941,
  serialized_end=1055,
)


_GETEZFORPATHREQUESTPROTO = _descriptor.Descriptor(
  name='GetEZForPathRequestProto',
  full_name='hadoop.hdfs.GetEZForPathRequestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src', full_name='hadoop.hdfs.GetEZForPathRequestProto.src', index=0,
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
  serialized_start=1057,
  serialized_end=1096,
)


_GETEZFORPATHRESPONSEPROTO = _descriptor.Descriptor(
  name='GetEZForPathResponseProto',
  full_name='hadoop.hdfs.GetEZForPathResponseProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='zone', full_name='hadoop.hdfs.GetEZForPathResponseProto.zone', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=1098,
  serialized_end=1173,
)

_ENCRYPTIONZONEPROTO.fields_by_name['suite'].enum_type = hdfs__pb2._CIPHERSUITEPROTO
_ENCRYPTIONZONEPROTO.fields_by_name['cryptoProtocolVersion'].enum_type = hdfs__pb2._CRYPTOPROTOCOLVERSIONPROTO
_LISTENCRYPTIONZONESRESPONSEPROTO.fields_by_name['zones'].message_type = _ENCRYPTIONZONEPROTO
_REENCRYPTENCRYPTIONZONEREQUESTPROTO.fields_by_name['action'].enum_type = _REENCRYPTACTIONPROTO
_ZONEREENCRYPTIONSTATUSPROTO.fields_by_name['state'].enum_type = _REENCRYPTIONSTATEPROTO
_LISTREENCRYPTIONSTATUSRESPONSEPROTO.fields_by_name['statuses'].message_type = _ZONEREENCRYPTIONSTATUSPROTO
_GETEZFORPATHRESPONSEPROTO.fields_by_name['zone'].message_type = _ENCRYPTIONZONEPROTO
DESCRIPTOR.message_types_by_name['CreateEncryptionZoneRequestProto'] = _CREATEENCRYPTIONZONEREQUESTPROTO
DESCRIPTOR.message_types_by_name['CreateEncryptionZoneResponseProto'] = _CREATEENCRYPTIONZONERESPONSEPROTO
DESCRIPTOR.message_types_by_name['ListEncryptionZonesRequestProto'] = _LISTENCRYPTIONZONESREQUESTPROTO
DESCRIPTOR.message_types_by_name['EncryptionZoneProto'] = _ENCRYPTIONZONEPROTO
DESCRIPTOR.message_types_by_name['ListEncryptionZonesResponseProto'] = _LISTENCRYPTIONZONESRESPONSEPROTO
DESCRIPTOR.message_types_by_name['ReencryptEncryptionZoneRequestProto'] = _REENCRYPTENCRYPTIONZONEREQUESTPROTO
DESCRIPTOR.message_types_by_name['ReencryptEncryptionZoneResponseProto'] = _REENCRYPTENCRYPTIONZONERESPONSEPROTO
DESCRIPTOR.message_types_by_name['ListReencryptionStatusRequestProto'] = _LISTREENCRYPTIONSTATUSREQUESTPROTO
DESCRIPTOR.message_types_by_name['ZoneReencryptionStatusProto'] = _ZONEREENCRYPTIONSTATUSPROTO
DESCRIPTOR.message_types_by_name['ListReencryptionStatusResponseProto'] = _LISTREENCRYPTIONSTATUSRESPONSEPROTO
DESCRIPTOR.message_types_by_name['GetEZForPathRequestProto'] = _GETEZFORPATHREQUESTPROTO
DESCRIPTOR.message_types_by_name['GetEZForPathResponseProto'] = _GETEZFORPATHRESPONSEPROTO
DESCRIPTOR.enum_types_by_name['ReencryptActionProto'] = _REENCRYPTACTIONPROTO
DESCRIPTOR.enum_types_by_name['ReencryptionStateProto'] = _REENCRYPTIONSTATEPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateEncryptionZoneRequestProto = _reflection.GeneratedProtocolMessageType('CreateEncryptionZoneRequestProto', (_message.Message,), dict(
  DESCRIPTOR = _CREATEENCRYPTIONZONEREQUESTPROTO,
  __module__ = 'encryption_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.CreateEncryptionZoneRequestProto)
  ))
_sym_db.RegisterMessage(CreateEncryptionZoneRequestProto)

CreateEncryptionZoneResponseProto = _reflection.GeneratedProtocolMessageType('CreateEncryptionZoneResponseProto', (_message.Message,), dict(
  DESCRIPTOR = _CREATEENCRYPTIONZONERESPONSEPROTO,
  __module__ = 'encryption_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.CreateEncryptionZoneResponseProto)
  ))
_sym_db.RegisterMessage(CreateEncryptionZoneResponseProto)

ListEncryptionZonesRequestProto = _reflection.GeneratedProtocolMessageType('ListEncryptionZonesRequestProto', (_message.Message,), dict(
  DESCRIPTOR = _LISTENCRYPTIONZONESREQUESTPROTO,
  __module__ = 'encryption_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.ListEncryptionZonesRequestProto)
  ))
_sym_db.RegisterMessage(ListEncryptionZonesRequestProto)

EncryptionZoneProto = _reflection.GeneratedProtocolMessageType('EncryptionZoneProto', (_message.Message,), dict(
  DESCRIPTOR = _ENCRYPTIONZONEPROTO,
  __module__ = 'encryption_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.EncryptionZoneProto)
  ))
_sym_db.RegisterMessage(EncryptionZoneProto)

ListEncryptionZonesResponseProto = _reflection.GeneratedProtocolMessageType('ListEncryptionZonesResponseProto', (_message.Message,), dict(
  DESCRIPTOR = _LISTENCRYPTIONZONESRESPONSEPROTO,
  __module__ = 'encryption_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.ListEncryptionZonesResponseProto)
  ))
_sym_db.RegisterMessage(ListEncryptionZonesResponseProto)

ReencryptEncryptionZoneRequestProto = _reflection.GeneratedProtocolMessageType('ReencryptEncryptionZoneRequestProto', (_message.Message,), dict(
  DESCRIPTOR = _REENCRYPTENCRYPTIONZONEREQUESTPROTO,
  __module__ = 'encryption_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.ReencryptEncryptionZoneRequestProto)
  ))
_sym_db.RegisterMessage(ReencryptEncryptionZoneRequestProto)

ReencryptEncryptionZoneResponseProto = _reflection.GeneratedProtocolMessageType('ReencryptEncryptionZoneResponseProto', (_message.Message,), dict(
  DESCRIPTOR = _REENCRYPTENCRYPTIONZONERESPONSEPROTO,
  __module__ = 'encryption_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.ReencryptEncryptionZoneResponseProto)
  ))
_sym_db.RegisterMessage(ReencryptEncryptionZoneResponseProto)

ListReencryptionStatusRequestProto = _reflection.GeneratedProtocolMessageType('ListReencryptionStatusRequestProto', (_message.Message,), dict(
  DESCRIPTOR = _LISTREENCRYPTIONSTATUSREQUESTPROTO,
  __module__ = 'encryption_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.ListReencryptionStatusRequestProto)
  ))
_sym_db.RegisterMessage(ListReencryptionStatusRequestProto)

ZoneReencryptionStatusProto = _reflection.GeneratedProtocolMessageType('ZoneReencryptionStatusProto', (_message.Message,), dict(
  DESCRIPTOR = _ZONEREENCRYPTIONSTATUSPROTO,
  __module__ = 'encryption_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.ZoneReencryptionStatusProto)
  ))
_sym_db.RegisterMessage(ZoneReencryptionStatusProto)

ListReencryptionStatusResponseProto = _reflection.GeneratedProtocolMessageType('ListReencryptionStatusResponseProto', (_message.Message,), dict(
  DESCRIPTOR = _LISTREENCRYPTIONSTATUSRESPONSEPROTO,
  __module__ = 'encryption_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.ListReencryptionStatusResponseProto)
  ))
_sym_db.RegisterMessage(ListReencryptionStatusResponseProto)

GetEZForPathRequestProto = _reflection.GeneratedProtocolMessageType('GetEZForPathRequestProto', (_message.Message,), dict(
  DESCRIPTOR = _GETEZFORPATHREQUESTPROTO,
  __module__ = 'encryption_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.GetEZForPathRequestProto)
  ))
_sym_db.RegisterMessage(GetEZForPathRequestProto)

GetEZForPathResponseProto = _reflection.GeneratedProtocolMessageType('GetEZForPathResponseProto', (_message.Message,), dict(
  DESCRIPTOR = _GETEZFORPATHRESPONSEPROTO,
  __module__ = 'encryption_pb2'
  # @@protoc_insertion_point(class_scope:hadoop.hdfs.GetEZForPathResponseProto)
  ))
_sym_db.RegisterMessage(GetEZForPathResponseProto)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
