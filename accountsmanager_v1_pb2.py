# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: accountsmanager_v1.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x61\x63\x63ountsmanager_v1.proto\"\x8a\x01\n\x11\x41\x64\x64\x41\x63\x63ountRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x14\n\x0cnew_password\x18\x03 \x01(\t\x12\r\n\x05renew\x18\x04 \x01(\x08\x12\x11\n\tuse_proxy\x18\x05 \x01(\x08\x12\x19\n\x11\x63ompare_passwords\x18\x06 \x01(\x08\"#\n\x12\x41\x64\x64\x41\x63\x63ountResponse\x12\r\n\x05vk_id\x18\x01 \x01(\x03\"\x8f\x01\n\x10VkApiCallRequest\x12\r\n\x05vk_id\x18\x01 \x01(\x03\x12\x0e\n\x06method\x18\x02 \x01(\t\x12-\n\x06params\x18\x03 \x03(\x0b\x32\x1d.VkApiCallRequest.ParamsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"#\n\x11VkApiCallResponse\x12\x0e\n\x06result\x18\x01 \x01(\x0c\"\x14\n\x12GetAccountsRequest\"5\n\x13GetAccountsResponse\x12\x0f\n\x07\x61\x63\x63_ids\x18\x01 \x03(\x03\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\")\n\x18\x43onnectAudioQueueRequest\x12\r\n\x05vk_id\x18\x01 \x01(\x03\"O\n\x14\x41udioQueuePollResult\x12-\n\x08response\x18\x02 \x01(\x0b\x32\x19.AudioQueueServerResponseH\x00\x42\x08\n\x06result\"<\n\x18\x41udioQueueServerResponse\x12 \n\x06\x65vents\x18\x01 \x03(\x0b\x32\x10.AudioQueueEvent\"\x1f\n\x0f\x41udioQueueEvent\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"@\n\x19\x43onnectAudioQueueResponse\x12#\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x15.AudioQueuePollResult\",\n\x1aGetAccountsSessionsRequest\x12\x0e\n\x06vk_ids\x18\x01 \x03(\x03\"{\n\"GetAccountsSessionsResponseSession\x12\r\n\x05vk_id\x18\x01 \x01(\x03\x12\x11\n\tdevice_id\x18\x02 \x01(\t\x12\x12\n\nuser_agent\x18\x03 \x01(\t\x12\r\n\x05\x61pi_v\x18\x04 \x01(\t\x12\x10\n\x08language\x18\x05 \x01(\t\"Q\n\x1bGetAccountsSessionsResponse\x12\x32\n\x05items\x18\x01 \x03(\x0b\x32#.GetAccountsSessionsResponseSession\"&\n\x14\x43heckAccountsRequest\x12\x0e\n\x06vk_ids\x18\x01 \x03(\x03\"W\n\x15\x43heckAccountsResponse\x12\r\n\x05valid\x18\x01 \x01(\x05\x12\x0f\n\x07invalid\x18\x02 \x01(\x05\x12\x0f\n\x07\x63hecked\x18\x03 \x01(\x05\x12\r\n\x05total\x18\x04 \x01(\x05\x32\x98\x03\n\x0f\x41\x63\x63ountsManager\x12\x35\n\nAddAccount\x12\x12.AddAccountRequest\x1a\x13.AddAccountResponse\x12\x32\n\tVkApiCall\x12\x11.VkApiCallRequest\x1a\x12.VkApiCallResponse\x12\x38\n\x0bGetAccounts\x12\x13.GetAccountsRequest\x1a\x14.GetAccountsResponse\x12L\n\x11\x43onnectAudioQueue\x12\x19.ConnectAudioQueueRequest\x1a\x1a.ConnectAudioQueueResponse0\x01\x12P\n\x13GetAccountsSessions\x12\x1b.GetAccountsSessionsRequest\x1a\x1c.GetAccountsSessionsResponse\x12@\n\rCheckAccounts\x12\x15.CheckAccountsRequest\x1a\x16.CheckAccountsResponse0\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'accountsmanager_v1_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VKAPICALLREQUEST_PARAMSENTRY._options = None
  _VKAPICALLREQUEST_PARAMSENTRY._serialized_options = b'8\001'
  _ADDACCOUNTREQUEST._serialized_start=29
  _ADDACCOUNTREQUEST._serialized_end=167
  _ADDACCOUNTRESPONSE._serialized_start=169
  _ADDACCOUNTRESPONSE._serialized_end=204
  _VKAPICALLREQUEST._serialized_start=207
  _VKAPICALLREQUEST._serialized_end=350
  _VKAPICALLREQUEST_PARAMSENTRY._serialized_start=305
  _VKAPICALLREQUEST_PARAMSENTRY._serialized_end=350
  _VKAPICALLRESPONSE._serialized_start=352
  _VKAPICALLRESPONSE._serialized_end=387
  _GETACCOUNTSREQUEST._serialized_start=389
  _GETACCOUNTSREQUEST._serialized_end=409
  _GETACCOUNTSRESPONSE._serialized_start=411
  _GETACCOUNTSRESPONSE._serialized_end=464
  _CONNECTAUDIOQUEUEREQUEST._serialized_start=466
  _CONNECTAUDIOQUEUEREQUEST._serialized_end=507
  _AUDIOQUEUEPOLLRESULT._serialized_start=509
  _AUDIOQUEUEPOLLRESULT._serialized_end=588
  _AUDIOQUEUESERVERRESPONSE._serialized_start=590
  _AUDIOQUEUESERVERRESPONSE._serialized_end=650
  _AUDIOQUEUEEVENT._serialized_start=652
  _AUDIOQUEUEEVENT._serialized_end=683
  _CONNECTAUDIOQUEUERESPONSE._serialized_start=685
  _CONNECTAUDIOQUEUERESPONSE._serialized_end=749
  _GETACCOUNTSSESSIONSREQUEST._serialized_start=751
  _GETACCOUNTSSESSIONSREQUEST._serialized_end=795
  _GETACCOUNTSSESSIONSRESPONSESESSION._serialized_start=797
  _GETACCOUNTSSESSIONSRESPONSESESSION._serialized_end=920
  _GETACCOUNTSSESSIONSRESPONSE._serialized_start=922
  _GETACCOUNTSSESSIONSRESPONSE._serialized_end=1003
  _CHECKACCOUNTSREQUEST._serialized_start=1005
  _CHECKACCOUNTSREQUEST._serialized_end=1043
  _CHECKACCOUNTSRESPONSE._serialized_start=1045
  _CHECKACCOUNTSRESPONSE._serialized_end=1132
  _ACCOUNTSMANAGER._serialized_start=1135
  _ACCOUNTSMANAGER._serialized_end=1543
# @@protoc_insertion_point(module_scope)
