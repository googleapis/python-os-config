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


import google.api_core.grpc_helpers

from google.cloud.osconfig_v1.proto import osconfig_service_pb2_grpc


class OsConfigServiceGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.cloud.osconfig.v1 OsConfigService API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """

    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    def __init__(
        self, channel=None, credentials=None, address="osconfig.googleapis.com:443"
    ):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                "The `channel` and `credentials` arguments are mutually " "exclusive.",
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    "grpc.max_send_message_length": -1,
                    "grpc.max_receive_message_length": -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            "os_config_service_stub": osconfig_service_pb2_grpc.OsConfigServiceStub(
                channel
            ),
        }

    @classmethod
    def create_channel(
        cls, address="osconfig.googleapis.com:443", credentials=None, **kwargs
    ):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address, credentials=credentials, scopes=cls._OAUTH_SCOPES, **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def execute_patch_job(self):
        """Return the gRPC stub for :meth:`OsConfigServiceClient.execute_patch_job`.

        Patch VM instances by creating and running a patch job.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["os_config_service_stub"].ExecutePatchJob

    @property
    def get_patch_job(self):
        """Return the gRPC stub for :meth:`OsConfigServiceClient.get_patch_job`.

        Get the patch job. This can be used to track the progress of an
        ongoing patch job or review the details of completed jobs.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["os_config_service_stub"].GetPatchJob

    @property
    def cancel_patch_job(self):
        """Return the gRPC stub for :meth:`OsConfigServiceClient.cancel_patch_job`.

        Cancel a patch job. The patch job must be active. Canceled patch jobs
        cannot be restarted.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["os_config_service_stub"].CancelPatchJob

    @property
    def list_patch_jobs(self):
        """Return the gRPC stub for :meth:`OsConfigServiceClient.list_patch_jobs`.

        Get a list of patch jobs.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["os_config_service_stub"].ListPatchJobs

    @property
    def list_patch_job_instance_details(self):
        """Return the gRPC stub for :meth:`OsConfigServiceClient.list_patch_job_instance_details`.

        Get a list of instance details for a given patch job.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["os_config_service_stub"].ListPatchJobInstanceDetails

    @property
    def create_patch_deployment(self):
        """Return the gRPC stub for :meth:`OsConfigServiceClient.create_patch_deployment`.

        Create an OS Config patch deployment.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["os_config_service_stub"].CreatePatchDeployment

    @property
    def get_patch_deployment(self):
        """Return the gRPC stub for :meth:`OsConfigServiceClient.get_patch_deployment`.

        Get an OS Config patch deployment.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["os_config_service_stub"].GetPatchDeployment

    @property
    def list_patch_deployments(self):
        """Return the gRPC stub for :meth:`OsConfigServiceClient.list_patch_deployments`.

        Get a page of OS Config patch deployments.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["os_config_service_stub"].ListPatchDeployments

    @property
    def delete_patch_deployment(self):
        """Return the gRPC stub for :meth:`OsConfigServiceClient.delete_patch_deployment`.

        Delete an OS Config patch deployment.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs["os_config_service_stub"].DeletePatchDeployment
