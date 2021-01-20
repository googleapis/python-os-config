# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unit tests."""

import mock
import pytest

from google.cloud import osconfig_v1
from google.cloud.osconfig_v1.proto import patch_deployments_pb2
from google.cloud.osconfig_v1.proto import patch_jobs_pb2
from google.protobuf import empty_pb2


class MultiCallableStub(object):
    """Stub for the grpc.UnaryUnaryMultiCallable interface."""

    def __init__(self, method, channel_stub):
        self.method = method
        self.channel_stub = channel_stub

    def __call__(self, request, timeout=None, metadata=None, credentials=None):
        self.channel_stub.requests.append((self.method, request))

        response = None
        if self.channel_stub.responses:
            response = self.channel_stub.responses.pop()

        if isinstance(response, Exception):
            raise response

        if response:
            return response


class ChannelStub(object):
    """Stub for the grpc.Channel interface."""

    def __init__(self, responses=[]):
        self.responses = responses
        self.requests = []

    def unary_unary(self, method, request_serializer=None, response_deserializer=None):
        return MultiCallableStub(method, self)


class CustomException(Exception):
    pass


class TestOsConfigServiceClient(object):
    def test_execute_patch_job(self):
        # Setup Expected Response
        name = "name3373707"
        display_name = "displayName1615086568"
        description = "description-1724546052"
        dry_run = False
        error_message = "errorMessage-1938755376"
        percent_complete = -1.96096922e8
        patch_deployment = "patchDeployment633565980"
        expected_response = {
            "name": name,
            "display_name": display_name,
            "description": description,
            "dry_run": dry_run,
            "error_message": error_message,
            "percent_complete": percent_complete,
            "patch_deployment": patch_deployment,
        }
        expected_response = patch_jobs_pb2.PatchJob(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = osconfig_v1.OsConfigServiceClient()

        # Setup Request
        parent = client.project_path("[PROJECT]")
        instance_filter = {}

        response = client.execute_patch_job(parent, instance_filter)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = patch_jobs_pb2.ExecutePatchJobRequest(
            parent=parent, instance_filter=instance_filter
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_execute_patch_job_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = osconfig_v1.OsConfigServiceClient()

        # Setup request
        parent = client.project_path("[PROJECT]")
        instance_filter = {}

        with pytest.raises(CustomException):
            client.execute_patch_job(parent, instance_filter)

    def test_get_patch_job(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        display_name = "displayName1615086568"
        description = "description-1724546052"
        dry_run = False
        error_message = "errorMessage-1938755376"
        percent_complete = -1.96096922e8
        patch_deployment = "patchDeployment633565980"
        expected_response = {
            "name": name_2,
            "display_name": display_name,
            "description": description,
            "dry_run": dry_run,
            "error_message": error_message,
            "percent_complete": percent_complete,
            "patch_deployment": patch_deployment,
        }
        expected_response = patch_jobs_pb2.PatchJob(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = osconfig_v1.OsConfigServiceClient()

        # Setup Request
        name = client.patch_job_path("[PROJECT]", "[PATCH_JOB]")

        response = client.get_patch_job(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = patch_jobs_pb2.GetPatchJobRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_patch_job_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = osconfig_v1.OsConfigServiceClient()

        # Setup request
        name = client.patch_job_path("[PROJECT]", "[PATCH_JOB]")

        with pytest.raises(CustomException):
            client.get_patch_job(name)

    def test_cancel_patch_job(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        display_name = "displayName1615086568"
        description = "description-1724546052"
        dry_run = False
        error_message = "errorMessage-1938755376"
        percent_complete = -1.96096922e8
        patch_deployment = "patchDeployment633565980"
        expected_response = {
            "name": name_2,
            "display_name": display_name,
            "description": description,
            "dry_run": dry_run,
            "error_message": error_message,
            "percent_complete": percent_complete,
            "patch_deployment": patch_deployment,
        }
        expected_response = patch_jobs_pb2.PatchJob(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = osconfig_v1.OsConfigServiceClient()

        # Setup Request
        name = client.patch_job_path("[PROJECT]", "[PATCH_JOB]")

        response = client.cancel_patch_job(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = patch_jobs_pb2.CancelPatchJobRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_cancel_patch_job_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = osconfig_v1.OsConfigServiceClient()

        # Setup request
        name = client.patch_job_path("[PROJECT]", "[PATCH_JOB]")

        with pytest.raises(CustomException):
            client.cancel_patch_job(name)

    def test_list_patch_jobs(self):
        # Setup Expected Response
        next_page_token = ""
        patch_jobs_element = {}
        patch_jobs = [patch_jobs_element]
        expected_response = {
            "next_page_token": next_page_token,
            "patch_jobs": patch_jobs,
        }
        expected_response = patch_jobs_pb2.ListPatchJobsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = osconfig_v1.OsConfigServiceClient()

        # Setup Request
        parent = client.project_path("[PROJECT]")

        paged_list_response = client.list_patch_jobs(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.patch_jobs[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = patch_jobs_pb2.ListPatchJobsRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_patch_jobs_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = osconfig_v1.OsConfigServiceClient()

        # Setup request
        parent = client.project_path("[PROJECT]")

        paged_list_response = client.list_patch_jobs(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_list_patch_job_instance_details(self):
        # Setup Expected Response
        next_page_token = ""
        patch_job_instance_details_element = {}
        patch_job_instance_details = [patch_job_instance_details_element]
        expected_response = {
            "next_page_token": next_page_token,
            "patch_job_instance_details": patch_job_instance_details,
        }
        expected_response = patch_jobs_pb2.ListPatchJobInstanceDetailsResponse(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = osconfig_v1.OsConfigServiceClient()

        # Setup Request
        parent = client.patch_job_path("[PROJECT]", "[PATCH_JOB]")

        paged_list_response = client.list_patch_job_instance_details(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.patch_job_instance_details[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = patch_jobs_pb2.ListPatchJobInstanceDetailsRequest(
            parent=parent
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_patch_job_instance_details_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = osconfig_v1.OsConfigServiceClient()

        # Setup request
        parent = client.patch_job_path("[PROJECT]", "[PATCH_JOB]")

        paged_list_response = client.list_patch_job_instance_details(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_create_patch_deployment(self):
        # Setup Expected Response
        name = "name3373707"
        description = "description-1724546052"
        expected_response = {"name": name, "description": description}
        expected_response = patch_deployments_pb2.PatchDeployment(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = osconfig_v1.OsConfigServiceClient()

        # Setup Request
        parent = client.project_path("[PROJECT]")
        patch_deployment_id = "patchDeploymentId-1817061090"
        patch_deployment = {}

        response = client.create_patch_deployment(
            parent, patch_deployment_id, patch_deployment
        )
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = patch_deployments_pb2.CreatePatchDeploymentRequest(
            parent=parent,
            patch_deployment_id=patch_deployment_id,
            patch_deployment=patch_deployment,
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_patch_deployment_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = osconfig_v1.OsConfigServiceClient()

        # Setup request
        parent = client.project_path("[PROJECT]")
        patch_deployment_id = "patchDeploymentId-1817061090"
        patch_deployment = {}

        with pytest.raises(CustomException):
            client.create_patch_deployment(
                parent, patch_deployment_id, patch_deployment
            )

    def test_get_patch_deployment(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        description = "description-1724546052"
        expected_response = {"name": name_2, "description": description}
        expected_response = patch_deployments_pb2.PatchDeployment(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = osconfig_v1.OsConfigServiceClient()

        # Setup Request
        name = client.patch_deployment_path("[PROJECT]", "[PATCH_DEPLOYMENT]")

        response = client.get_patch_deployment(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = patch_deployments_pb2.GetPatchDeploymentRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_patch_deployment_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = osconfig_v1.OsConfigServiceClient()

        # Setup request
        name = client.patch_deployment_path("[PROJECT]", "[PATCH_DEPLOYMENT]")

        with pytest.raises(CustomException):
            client.get_patch_deployment(name)

    def test_list_patch_deployments(self):
        # Setup Expected Response
        next_page_token = ""
        patch_deployments_element = {}
        patch_deployments = [patch_deployments_element]
        expected_response = {
            "next_page_token": next_page_token,
            "patch_deployments": patch_deployments,
        }
        expected_response = patch_deployments_pb2.ListPatchDeploymentsResponse(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = osconfig_v1.OsConfigServiceClient()

        # Setup Request
        parent = client.project_path("[PROJECT]")

        paged_list_response = client.list_patch_deployments(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.patch_deployments[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = patch_deployments_pb2.ListPatchDeploymentsRequest(
            parent=parent
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_patch_deployments_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = osconfig_v1.OsConfigServiceClient()

        # Setup request
        parent = client.project_path("[PROJECT]")

        paged_list_response = client.list_patch_deployments(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_delete_patch_deployment(self):
        channel = ChannelStub()
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = osconfig_v1.OsConfigServiceClient()

        # Setup Request
        name = client.patch_deployment_path("[PROJECT]", "[PATCH_DEPLOYMENT]")

        client.delete_patch_deployment(name)

        assert len(channel.requests) == 1
        expected_request = patch_deployments_pb2.DeletePatchDeploymentRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_patch_deployment_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = osconfig_v1.OsConfigServiceClient()

        # Setup request
        name = client.patch_deployment_path("[PROJECT]", "[PATCH_DEPLOYMENT]")

        with pytest.raises(CustomException):
            client.delete_patch_deployment(name)
