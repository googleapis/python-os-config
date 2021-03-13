# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/osconfig_v1/proto/osconfig_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.osconfig_v1.proto import (
    patch_deployments_pb2 as google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__deployments__pb2,
)
from google.cloud.osconfig_v1.proto import (
    patch_jobs_pb2 as google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__jobs__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/osconfig_v1/proto/osconfig_service.proto",
    package="google.cloud.osconfig.v1",
    syntax="proto3",
    serialized_options=b"\n\034com.google.cloud.osconfig.v1B\rOsConfigProtoZ@google.golang.org/genproto/googleapis/cloud/osconfig/v1;osconfig\252\002\030Google.Cloud.OsConfig.V1\312\002\030Google\\Cloud\\OsConfig\\V1\352\002\033Google::Cloud::OsConfig::V1\352AW\n\037compute.googleapis.com/Instance\0224projects/{project}/zones/{zone}/instances/{instance}",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n5google/cloud/osconfig_v1/proto/osconfig_service.proto\x12\x18google.cloud.osconfig.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x19google/api/resource.proto\x1a\x36google/cloud/osconfig_v1/proto/patch_deployments.proto\x1a/google/cloud/osconfig_v1/proto/patch_jobs.proto\x1a\x1bgoogle/protobuf/empty.proto2\xbe\r\n\x0fOsConfigService\x12\x9d\x01\n\x0f\x45xecutePatchJob\x12\x30.google.cloud.osconfig.v1.ExecutePatchJobRequest\x1a".google.cloud.osconfig.v1.PatchJob"4\x82\xd3\xe4\x93\x02.")/v1/{parent=projects/*}/patchJobs:execute:\x01*\x12\x91\x01\n\x0bGetPatchJob\x12,.google.cloud.osconfig.v1.GetPatchJobRequest\x1a".google.cloud.osconfig.v1.PatchJob"0\x82\xd3\xe4\x93\x02#\x12!/v1/{name=projects/*/patchJobs/*}\xda\x41\x04name\x12\x9a\x01\n\x0e\x43\x61ncelPatchJob\x12/.google.cloud.osconfig.v1.CancelPatchJobRequest\x1a".google.cloud.osconfig.v1.PatchJob"3\x82\xd3\xe4\x93\x02-"(/v1/{name=projects/*/patchJobs/*}:cancel:\x01*\x12\xa4\x01\n\rListPatchJobs\x12..google.cloud.osconfig.v1.ListPatchJobsRequest\x1a/.google.cloud.osconfig.v1.ListPatchJobsResponse"2\x82\xd3\xe4\x93\x02#\x12!/v1/{parent=projects/*}/patchJobs\xda\x41\x06parent\x12\xe0\x01\n\x1bListPatchJobInstanceDetails\x12<.google.cloud.osconfig.v1.ListPatchJobInstanceDetailsRequest\x1a=.google.cloud.osconfig.v1.ListPatchJobInstanceDetailsResponse"D\x82\xd3\xe4\x93\x02\x35\x12\x33/v1/{parent=projects/*/patchJobs/*}/instanceDetails\xda\x41\x06parent\x12\xec\x01\n\x15\x43reatePatchDeployment\x12\x36.google.cloud.osconfig.v1.CreatePatchDeploymentRequest\x1a).google.cloud.osconfig.v1.PatchDeployment"p\x82\xd3\xe4\x93\x02<"(/v1/{parent=projects/*}/patchDeployments:\x10patch_deployment\xda\x41+parent,patch_deployment,patch_deployment_id\x12\xad\x01\n\x12GetPatchDeployment\x12\x33.google.cloud.osconfig.v1.GetPatchDeploymentRequest\x1a).google.cloud.osconfig.v1.PatchDeployment"7\x82\xd3\xe4\x93\x02*\x12(/v1/{name=projects/*/patchDeployments/*}\xda\x41\x04name\x12\xc0\x01\n\x14ListPatchDeployments\x12\x35.google.cloud.osconfig.v1.ListPatchDeploymentsRequest\x1a\x36.google.cloud.osconfig.v1.ListPatchDeploymentsResponse"9\x82\xd3\xe4\x93\x02*\x12(/v1/{parent=projects/*}/patchDeployments\xda\x41\x06parent\x12\xa0\x01\n\x15\x44\x65letePatchDeployment\x12\x36.google.cloud.osconfig.v1.DeletePatchDeploymentRequest\x1a\x16.google.protobuf.Empty"7\x82\xd3\xe4\x93\x02**(/v1/{name=projects/*/patchDeployments/*}\xda\x41\x04name\x1aK\xca\x41\x17osconfig.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\x9d\x02\n\x1c\x63om.google.cloud.osconfig.v1B\rOsConfigProtoZ@google.golang.org/genproto/googleapis/cloud/osconfig/v1;osconfig\xaa\x02\x18Google.Cloud.OsConfig.V1\xca\x02\x18Google\\Cloud\\OsConfig\\V1\xea\x02\x1bGoogle::Cloud::OsConfig::V1\xea\x41W\n\x1f\x63ompute.googleapis.com/Instance\x12\x34projects/{project}/zones/{zone}/instances/{instance}b\x06proto3',
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_client__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__deployments__pb2.DESCRIPTOR,
        google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__jobs__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
    ],
)


_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_OSCONFIGSERVICE = _descriptor.ServiceDescriptor(
    name="OsConfigService",
    full_name="google.cloud.osconfig.v1.OsConfigService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=b"\312A\027osconfig.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform",
    create_key=_descriptor._internal_create_key,
    serialized_start=300,
    serialized_end=2026,
    methods=[
        _descriptor.MethodDescriptor(
            name="ExecutePatchJob",
            full_name="google.cloud.osconfig.v1.OsConfigService.ExecutePatchJob",
            index=0,
            containing_service=None,
            input_type=google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__jobs__pb2._EXECUTEPATCHJOBREQUEST,
            output_type=google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__jobs__pb2._PATCHJOB,
            serialized_options=b'\202\323\344\223\002.")/v1/{parent=projects/*}/patchJobs:execute:\001*',
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="GetPatchJob",
            full_name="google.cloud.osconfig.v1.OsConfigService.GetPatchJob",
            index=1,
            containing_service=None,
            input_type=google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__jobs__pb2._GETPATCHJOBREQUEST,
            output_type=google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__jobs__pb2._PATCHJOB,
            serialized_options=b"\202\323\344\223\002#\022!/v1/{name=projects/*/patchJobs/*}\332A\004name",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="CancelPatchJob",
            full_name="google.cloud.osconfig.v1.OsConfigService.CancelPatchJob",
            index=2,
            containing_service=None,
            input_type=google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__jobs__pb2._CANCELPATCHJOBREQUEST,
            output_type=google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__jobs__pb2._PATCHJOB,
            serialized_options=b'\202\323\344\223\002-"(/v1/{name=projects/*/patchJobs/*}:cancel:\001*',
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="ListPatchJobs",
            full_name="google.cloud.osconfig.v1.OsConfigService.ListPatchJobs",
            index=3,
            containing_service=None,
            input_type=google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__jobs__pb2._LISTPATCHJOBSREQUEST,
            output_type=google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__jobs__pb2._LISTPATCHJOBSRESPONSE,
            serialized_options=b"\202\323\344\223\002#\022!/v1/{parent=projects/*}/patchJobs\332A\006parent",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="ListPatchJobInstanceDetails",
            full_name="google.cloud.osconfig.v1.OsConfigService.ListPatchJobInstanceDetails",
            index=4,
            containing_service=None,
            input_type=google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__jobs__pb2._LISTPATCHJOBINSTANCEDETAILSREQUEST,
            output_type=google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__jobs__pb2._LISTPATCHJOBINSTANCEDETAILSRESPONSE,
            serialized_options=b"\202\323\344\223\0025\0223/v1/{parent=projects/*/patchJobs/*}/instanceDetails\332A\006parent",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="CreatePatchDeployment",
            full_name="google.cloud.osconfig.v1.OsConfigService.CreatePatchDeployment",
            index=5,
            containing_service=None,
            input_type=google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__deployments__pb2._CREATEPATCHDEPLOYMENTREQUEST,
            output_type=google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__deployments__pb2._PATCHDEPLOYMENT,
            serialized_options=b'\202\323\344\223\002<"(/v1/{parent=projects/*}/patchDeployments:\020patch_deployment\332A+parent,patch_deployment,patch_deployment_id',
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="GetPatchDeployment",
            full_name="google.cloud.osconfig.v1.OsConfigService.GetPatchDeployment",
            index=6,
            containing_service=None,
            input_type=google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__deployments__pb2._GETPATCHDEPLOYMENTREQUEST,
            output_type=google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__deployments__pb2._PATCHDEPLOYMENT,
            serialized_options=b"\202\323\344\223\002*\022(/v1/{name=projects/*/patchDeployments/*}\332A\004name",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="ListPatchDeployments",
            full_name="google.cloud.osconfig.v1.OsConfigService.ListPatchDeployments",
            index=7,
            containing_service=None,
            input_type=google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__deployments__pb2._LISTPATCHDEPLOYMENTSREQUEST,
            output_type=google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__deployments__pb2._LISTPATCHDEPLOYMENTSRESPONSE,
            serialized_options=b"\202\323\344\223\002*\022(/v1/{parent=projects/*}/patchDeployments\332A\006parent",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="DeletePatchDeployment",
            full_name="google.cloud.osconfig.v1.OsConfigService.DeletePatchDeployment",
            index=8,
            containing_service=None,
            input_type=google_dot_cloud_dot_osconfig__v1_dot_proto_dot_patch__deployments__pb2._DELETEPATCHDEPLOYMENTREQUEST,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=b"\202\323\344\223\002**(/v1/{name=projects/*/patchDeployments/*}\332A\004name",
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_OSCONFIGSERVICE)

DESCRIPTOR.services_by_name["OsConfigService"] = _OSCONFIGSERVICE

# @@protoc_insertion_point(module_scope)
