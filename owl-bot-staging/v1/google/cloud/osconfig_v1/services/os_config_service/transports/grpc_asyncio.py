# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import warnings
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import gapic_v1                   # type: ignore
from google.api_core import grpc_helpers_async         # type: ignore
from google.auth import credentials as ga_credentials   # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
import packaging.version

import grpc                        # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.osconfig_v1.types import patch_deployments
from google.cloud.osconfig_v1.types import patch_jobs
from google.protobuf import empty_pb2  # type: ignore
from .base import OsConfigServiceTransport, DEFAULT_CLIENT_INFO
from .grpc import OsConfigServiceGrpcTransport


class OsConfigServiceGrpcAsyncIOTransport(OsConfigServiceTransport):
    """gRPC AsyncIO backend transport for OsConfigService.

    OS Config API
    The OS Config service is a server-side component that you can
    use to manage package installations and patch jobs for virtual
    machine instances.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(cls,
                       host: str = 'osconfig.googleapis.com',
                       credentials: ga_credentials.Credentials = None,
                       credentials_file: Optional[str] = None,
                       scopes: Optional[Sequence[str]] = None,
                       quota_project_id: Optional[str] = None,
                       **kwargs) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """

        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs
        )

    def __init__(self, *,
            host: str = 'osconfig.googleapis.com',
            credentials: ga_credentials.Credentials = None,
            credentials_file: Optional[str] = None,
            scopes: Optional[Sequence[str]] = None,
            channel: aio.Channel = None,
            api_mtls_endpoint: str = None,
            client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
            ssl_channel_credentials: grpc.ChannelCredentials = None,
            client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
            quota_project_id=None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool] = False,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[aio.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                credentials=self._credentials,
                credentials_file=credentials_file,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def execute_patch_job(self) -> Callable[
            [patch_jobs.ExecutePatchJobRequest],
            Awaitable[patch_jobs.PatchJob]]:
        r"""Return a callable for the execute patch job method over gRPC.

        Patch VM instances by creating and running a patch
        job.

        Returns:
            Callable[[~.ExecutePatchJobRequest],
                    Awaitable[~.PatchJob]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'execute_patch_job' not in self._stubs:
            self._stubs['execute_patch_job'] = self.grpc_channel.unary_unary(
                '/google.cloud.osconfig.v1.OsConfigService/ExecutePatchJob',
                request_serializer=patch_jobs.ExecutePatchJobRequest.serialize,
                response_deserializer=patch_jobs.PatchJob.deserialize,
            )
        return self._stubs['execute_patch_job']

    @property
    def get_patch_job(self) -> Callable[
            [patch_jobs.GetPatchJobRequest],
            Awaitable[patch_jobs.PatchJob]]:
        r"""Return a callable for the get patch job method over gRPC.

        Get the patch job. This can be used to track the
        progress of an ongoing patch job or review the details
        of completed jobs.

        Returns:
            Callable[[~.GetPatchJobRequest],
                    Awaitable[~.PatchJob]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_patch_job' not in self._stubs:
            self._stubs['get_patch_job'] = self.grpc_channel.unary_unary(
                '/google.cloud.osconfig.v1.OsConfigService/GetPatchJob',
                request_serializer=patch_jobs.GetPatchJobRequest.serialize,
                response_deserializer=patch_jobs.PatchJob.deserialize,
            )
        return self._stubs['get_patch_job']

    @property
    def cancel_patch_job(self) -> Callable[
            [patch_jobs.CancelPatchJobRequest],
            Awaitable[patch_jobs.PatchJob]]:
        r"""Return a callable for the cancel patch job method over gRPC.

        Cancel a patch job. The patch job must be active.
        Canceled patch jobs cannot be restarted.

        Returns:
            Callable[[~.CancelPatchJobRequest],
                    Awaitable[~.PatchJob]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'cancel_patch_job' not in self._stubs:
            self._stubs['cancel_patch_job'] = self.grpc_channel.unary_unary(
                '/google.cloud.osconfig.v1.OsConfigService/CancelPatchJob',
                request_serializer=patch_jobs.CancelPatchJobRequest.serialize,
                response_deserializer=patch_jobs.PatchJob.deserialize,
            )
        return self._stubs['cancel_patch_job']

    @property
    def list_patch_jobs(self) -> Callable[
            [patch_jobs.ListPatchJobsRequest],
            Awaitable[patch_jobs.ListPatchJobsResponse]]:
        r"""Return a callable for the list patch jobs method over gRPC.

        Get a list of patch jobs.

        Returns:
            Callable[[~.ListPatchJobsRequest],
                    Awaitable[~.ListPatchJobsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_patch_jobs' not in self._stubs:
            self._stubs['list_patch_jobs'] = self.grpc_channel.unary_unary(
                '/google.cloud.osconfig.v1.OsConfigService/ListPatchJobs',
                request_serializer=patch_jobs.ListPatchJobsRequest.serialize,
                response_deserializer=patch_jobs.ListPatchJobsResponse.deserialize,
            )
        return self._stubs['list_patch_jobs']

    @property
    def list_patch_job_instance_details(self) -> Callable[
            [patch_jobs.ListPatchJobInstanceDetailsRequest],
            Awaitable[patch_jobs.ListPatchJobInstanceDetailsResponse]]:
        r"""Return a callable for the list patch job instance
        details method over gRPC.

        Get a list of instance details for a given patch job.

        Returns:
            Callable[[~.ListPatchJobInstanceDetailsRequest],
                    Awaitable[~.ListPatchJobInstanceDetailsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_patch_job_instance_details' not in self._stubs:
            self._stubs['list_patch_job_instance_details'] = self.grpc_channel.unary_unary(
                '/google.cloud.osconfig.v1.OsConfigService/ListPatchJobInstanceDetails',
                request_serializer=patch_jobs.ListPatchJobInstanceDetailsRequest.serialize,
                response_deserializer=patch_jobs.ListPatchJobInstanceDetailsResponse.deserialize,
            )
        return self._stubs['list_patch_job_instance_details']

    @property
    def create_patch_deployment(self) -> Callable[
            [patch_deployments.CreatePatchDeploymentRequest],
            Awaitable[patch_deployments.PatchDeployment]]:
        r"""Return a callable for the create patch deployment method over gRPC.

        Create an OS Config patch deployment.

        Returns:
            Callable[[~.CreatePatchDeploymentRequest],
                    Awaitable[~.PatchDeployment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'create_patch_deployment' not in self._stubs:
            self._stubs['create_patch_deployment'] = self.grpc_channel.unary_unary(
                '/google.cloud.osconfig.v1.OsConfigService/CreatePatchDeployment',
                request_serializer=patch_deployments.CreatePatchDeploymentRequest.serialize,
                response_deserializer=patch_deployments.PatchDeployment.deserialize,
            )
        return self._stubs['create_patch_deployment']

    @property
    def get_patch_deployment(self) -> Callable[
            [patch_deployments.GetPatchDeploymentRequest],
            Awaitable[patch_deployments.PatchDeployment]]:
        r"""Return a callable for the get patch deployment method over gRPC.

        Get an OS Config patch deployment.

        Returns:
            Callable[[~.GetPatchDeploymentRequest],
                    Awaitable[~.PatchDeployment]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'get_patch_deployment' not in self._stubs:
            self._stubs['get_patch_deployment'] = self.grpc_channel.unary_unary(
                '/google.cloud.osconfig.v1.OsConfigService/GetPatchDeployment',
                request_serializer=patch_deployments.GetPatchDeploymentRequest.serialize,
                response_deserializer=patch_deployments.PatchDeployment.deserialize,
            )
        return self._stubs['get_patch_deployment']

    @property
    def list_patch_deployments(self) -> Callable[
            [patch_deployments.ListPatchDeploymentsRequest],
            Awaitable[patch_deployments.ListPatchDeploymentsResponse]]:
        r"""Return a callable for the list patch deployments method over gRPC.

        Get a page of OS Config patch deployments.

        Returns:
            Callable[[~.ListPatchDeploymentsRequest],
                    Awaitable[~.ListPatchDeploymentsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'list_patch_deployments' not in self._stubs:
            self._stubs['list_patch_deployments'] = self.grpc_channel.unary_unary(
                '/google.cloud.osconfig.v1.OsConfigService/ListPatchDeployments',
                request_serializer=patch_deployments.ListPatchDeploymentsRequest.serialize,
                response_deserializer=patch_deployments.ListPatchDeploymentsResponse.deserialize,
            )
        return self._stubs['list_patch_deployments']

    @property
    def delete_patch_deployment(self) -> Callable[
            [patch_deployments.DeletePatchDeploymentRequest],
            Awaitable[empty_pb2.Empty]]:
        r"""Return a callable for the delete patch deployment method over gRPC.

        Delete an OS Config patch deployment.

        Returns:
            Callable[[~.DeletePatchDeploymentRequest],
                    Awaitable[~.Empty]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if 'delete_patch_deployment' not in self._stubs:
            self._stubs['delete_patch_deployment'] = self.grpc_channel.unary_unary(
                '/google.cloud.osconfig.v1.OsConfigService/DeletePatchDeployment',
                request_serializer=patch_deployments.DeletePatchDeploymentRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs['delete_patch_deployment']


__all__ = (
    'OsConfigServiceGrpcAsyncIOTransport',
)
