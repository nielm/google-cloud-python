# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/websecurityscanner_v1alpha/proto/crawled_url.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/websecurityscanner_v1alpha/proto/crawled_url.proto',
  package='google.cloud.websecurityscanner.v1alpha',
  syntax='proto3',
  serialized_options=_b('\n+com.google.cloud.websecurityscanner.v1alphaB\017CrawledUrlProtoP\001ZYgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1alpha;websecurityscanner'),
  serialized_pb=_b('\n?google/cloud/websecurityscanner_v1alpha/proto/crawled_url.proto\x12\'google.cloud.websecurityscanner.v1alpha\x1a\x1cgoogle/api/annotations.proto\"<\n\nCrawledUrl\x12\x13\n\x0bhttp_method\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0c\n\x04\x62ody\x18\x03 \x01(\tB\x9b\x01\n+com.google.cloud.websecurityscanner.v1alphaB\x0f\x43rawledUrlProtoP\x01ZYgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1alpha;websecurityscannerb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CRAWLEDURL = _descriptor.Descriptor(
  name='CrawledUrl',
  full_name='google.cloud.websecurityscanner.v1alpha.CrawledUrl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='http_method', full_name='google.cloud.websecurityscanner.v1alpha.CrawledUrl.http_method', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='google.cloud.websecurityscanner.v1alpha.CrawledUrl.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='google.cloud.websecurityscanner.v1alpha.CrawledUrl.body', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=198,
)

DESCRIPTOR.message_types_by_name['CrawledUrl'] = _CRAWLEDURL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CrawledUrl = _reflection.GeneratedProtocolMessageType('CrawledUrl', (_message.Message,), dict(
  DESCRIPTOR = _CRAWLEDURL,
  __module__ = 'google.cloud.websecurityscanner_v1alpha.proto.crawled_url_pb2'
  ,
  __doc__ = """A CrawledUrl resource represents a URL that was crawled during a
  ScanRun. Web Security Scanner Service crawls the web applications,
  following all links within the scope of sites, to find the URLs to test
  against.
  
  
  Attributes:
      http_method:
          Output only. The http method of the request that was used to
          visit the URL, in uppercase.
      url:
          Output only. The URL that was crawled.
      body:
          Output only. The body of the request that was used to visit
          the URL.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1alpha.CrawledUrl)
  ))
_sym_db.RegisterMessage(CrawledUrl)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
