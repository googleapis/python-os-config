# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from typing import Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import grpc_helpers
from google.api_core import operations_v1
from google.api_core import gapic_v1
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.osconfig_v1.types import inventory
from google.cloud.osconfig_v1.types import os_policy_assignment_reports
from google.cloud.osconfig_v1.types import os_policy_assignments
from google.cloud.osconfig_v1.types import vulnerability
from google.longrunning import operations_pb2  # type: ignore
from .base import OsConfigZonalServiceTransport, DEFAULT_CLIENT_INFO


class OsConfigZonalServiceGrpcTransport(OsConfigZonalServiceTransport):
    """gRPC backend transport for OsConfigZonalService.

    Zonal OS Config API
    The OS Config service is the server-side component that allows
    users to manage package installations and patch jobs for Compute
    Engine VM instances.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "osconfig.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Sequence[str] = None,
        channel: grpc.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id: Optional[str] = None,
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
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
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
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client: Optional[operations_v1.OperationsClient] = None

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
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
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

    @classmethod
    def create_channel(
        cls,
        host: str = "osconfig.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service."""
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Quick check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsClient(self.grpc_channel)

        # Return the client from cache.
        return self._operations_client

    @property
    def create_os_policy_assignment(
        self,
    ) -> Callable[
        [os_policy_assignments.CreateOSPolicyAssignmentRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the create os policy assignment method over gRPC.

        Create an OS policy assignment.

        This method also creates the first revision of the OS policy
        assignment.

        This method returns a long running operation (LRO) that contains
        the rollout details. The rollout can be cancelled by cancelling
        the LRO.

        For more information, see `Method:
        projects.locations.osPolicyAssignments.operations.cancel <https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel>`__.

        Returns:
            Callable[[~.CreateOSPolicyAssignmentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_os_policy_assignment" not in self._stubs:
            self._stubs["create_os_policy_assignment"] = self.grpc_channel.unary_unary(
                "/google.cloud.osconfig.v1.OsConfigZonalService/CreateOSPolicyAssignment",
                request_serializer=os_policy_assignments.CreateOSPolicyAssignmentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_os_policy_assignment"]

    @property
    def update_os_policy_assignment(
        self,
    ) -> Callable[
        [os_policy_assignments.UpdateOSPolicyAssignmentRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the update os policy assignment method over gRPC.

        Update an existing OS policy assignment.

        This method creates a new revision of the OS policy assignment.

        This method returns a long running operation (LRO) that contains
        the rollout details. The rollout can be cancelled by cancelling
        the LRO.

        For more information, see `Method:
        projects.locations.osPolicyAssignments.operations.cancel <https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel>`__.

        Returns:
            Callable[[~.UpdateOSPolicyAssignmentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_os_policy_assignment" not in self._stubs:
            self._stubs["update_os_policy_assignment"] = self.grpc_channel.unary_unary(
                "/google.cloud.osconfig.v1.OsConfigZonalService/UpdateOSPolicyAssignment",
                request_serializer=os_policy_assignments.UpdateOSPolicyAssignmentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_os_policy_assignment"]

    @property
    def get_os_policy_assignment(
        self,
    ) -> Callable[
        [os_policy_assignments.GetOSPolicyAssignmentRequest],
        os_policy_assignments.OSPolicyAssignment,
    ]:
        r"""Return a callable for the get os policy assignment method over gRPC.

        Retrieve an existing OS policy assignment.

        This method always returns the latest revision. In order to
        retrieve a previous revision of the assignment, also provide the
        revision ID in the ``name`` parameter.

        Returns:
            Callable[[~.GetOSPolicyAssignmentRequest],
                    ~.OSPolicyAssignment]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_os_policy_assignment" not in self._stubs:
            self._stubs["get_os_policy_assignment"] = self.grpc_channel.unary_unary(
                "/google.cloud.osconfig.v1.OsConfigZonalService/GetOSPolicyAssignment",
                request_serializer=os_policy_assignments.GetOSPolicyAssignmentRequest.serialize,
                response_deserializer=os_policy_assignments.OSPolicyAssignment.deserialize,
            )
        return self._stubs["get_os_policy_assignment"]

    @property
    def list_os_policy_assignments(
        self,
    ) -> Callable[
        [os_policy_assignments.ListOSPolicyAssignmentsRequest],
        os_policy_assignments.ListOSPolicyAssignmentsResponse,
    ]:
        r"""Return a callable for the list os policy assignments method over gRPC.

        List the OS policy assignments under the parent
        resource.
        For each OS policy assignment, the latest revision is
        returned.

        Returns:
            Callable[[~.ListOSPolicyAssignmentsRequest],
                    ~.ListOSPolicyAssignmentsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_os_policy_assignments" not in self._stubs:
            self._stubs["list_os_policy_assignments"] = self.grpc_channel.unary_unary(
                "/google.cloud.osconfig.v1.OsConfigZonalService/ListOSPolicyAssignments",
                request_serializer=os_policy_assignments.ListOSPolicyAssignmentsRequest.serialize,
                response_deserializer=os_policy_assignments.ListOSPolicyAssignmentsResponse.deserialize,
            )
        return self._stubs["list_os_policy_assignments"]

    @property
    def list_os_policy_assignment_revisions(
        self,
    ) -> Callable[
        [os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest],
        os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse,
    ]:
        r"""Return a callable for the list os policy assignment
        revisions method over gRPC.

        List the OS policy assignment revisions for a given
        OS policy assignment.

        Returns:
            Callable[[~.ListOSPolicyAssignmentRevisionsRequest],
                    ~.ListOSPolicyAssignmentRevisionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_os_policy_assignment_revisions" not in self._stubs:
            self._stubs[
                "list_os_policy_assignment_revisions"
            ] = self.grpc_channel.unary_unary(
                "/google.cloud.osconfig.v1.OsConfigZonalService/ListOSPolicyAssignmentRevisions",
                request_serializer=os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest.serialize,
                response_deserializer=os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse.deserialize,
            )
        return self._stubs["list_os_policy_assignment_revisions"]

    @property
    def delete_os_policy_assignment(
        self,
    ) -> Callable[
        [os_policy_assignments.DeleteOSPolicyAssignmentRequest],
        operations_pb2.Operation,
    ]:
        r"""Return a callable for the delete os policy assignment method over gRPC.

        Delete the OS policy assignment.

        This method creates a new revision of the OS policy assignment.

        This method returns a long running operation (LRO) that contains
        the rollout details. The rollout can be cancelled by cancelling
        the LRO.

        If the LRO completes and is not cancelled, all revisions
        associated with the OS policy assignment are deleted.

        For more information, see `Method:
        projects.locations.osPolicyAssignments.operations.cancel <https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel>`__.

        Returns:
            Callable[[~.DeleteOSPolicyAssignmentRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_os_policy_assignment" not in self._stubs:
            self._stubs["delete_os_policy_assignment"] = self.grpc_channel.unary_unary(
                "/google.cloud.osconfig.v1.OsConfigZonalService/DeleteOSPolicyAssignment",
                request_serializer=os_policy_assignments.DeleteOSPolicyAssignmentRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_os_policy_assignment"]

    @property
    def get_os_policy_assignment_report(
        self,
    ) -> Callable[
        [os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest],
        os_policy_assignment_reports.OSPolicyAssignmentReport,
    ]:
        r"""Return a callable for the get os policy assignment
        report method over gRPC.

        Get the OS policy asssignment report for the
        specified Compute Engine VM instance.

        Returns:
            Callable[[~.GetOSPolicyAssignmentReportRequest],
                    ~.OSPolicyAssignmentReport]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_os_policy_assignment_report" not in self._stubs:
            self._stubs[
                "get_os_policy_assignment_report"
            ] = self.grpc_channel.unary_unary(
                "/google.cloud.osconfig.v1.OsConfigZonalService/GetOSPolicyAssignmentReport",
                request_serializer=os_policy_assignment_reports.GetOSPolicyAssignmentReportRequest.serialize,
                response_deserializer=os_policy_assignment_reports.OSPolicyAssignmentReport.deserialize,
            )
        return self._stubs["get_os_policy_assignment_report"]

    @property
    def list_os_policy_assignment_reports(
        self,
    ) -> Callable[
        [os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest],
        os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse,
    ]:
        r"""Return a callable for the list os policy assignment
        reports method over gRPC.

        List OS policy asssignment reports for all Compute
        Engine VM instances in the specified zone.

        Returns:
            Callable[[~.ListOSPolicyAssignmentReportsRequest],
                    ~.ListOSPolicyAssignmentReportsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_os_policy_assignment_reports" not in self._stubs:
            self._stubs[
                "list_os_policy_assignment_reports"
            ] = self.grpc_channel.unary_unary(
                "/google.cloud.osconfig.v1.OsConfigZonalService/ListOSPolicyAssignmentReports",
                request_serializer=os_policy_assignment_reports.ListOSPolicyAssignmentReportsRequest.serialize,
                response_deserializer=os_policy_assignment_reports.ListOSPolicyAssignmentReportsResponse.deserialize,
            )
        return self._stubs["list_os_policy_assignment_reports"]

    @property
    def get_inventory(
        self,
    ) -> Callable[[inventory.GetInventoryRequest], inventory.Inventory]:
        r"""Return a callable for the get inventory method over gRPC.

        Get inventory data for the specified VM instance. If the VM has
        no associated inventory, the message ``NOT_FOUND`` is returned.

        Returns:
            Callable[[~.GetInventoryRequest],
                    ~.Inventory]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_inventory" not in self._stubs:
            self._stubs["get_inventory"] = self.grpc_channel.unary_unary(
                "/google.cloud.osconfig.v1.OsConfigZonalService/GetInventory",
                request_serializer=inventory.GetInventoryRequest.serialize,
                response_deserializer=inventory.Inventory.deserialize,
            )
        return self._stubs["get_inventory"]

    @property
    def list_inventories(
        self,
    ) -> Callable[
        [inventory.ListInventoriesRequest], inventory.ListInventoriesResponse
    ]:
        r"""Return a callable for the list inventories method over gRPC.

        List inventory data for all VM instances in the
        specified zone.

        Returns:
            Callable[[~.ListInventoriesRequest],
                    ~.ListInventoriesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_inventories" not in self._stubs:
            self._stubs["list_inventories"] = self.grpc_channel.unary_unary(
                "/google.cloud.osconfig.v1.OsConfigZonalService/ListInventories",
                request_serializer=inventory.ListInventoriesRequest.serialize,
                response_deserializer=inventory.ListInventoriesResponse.deserialize,
            )
        return self._stubs["list_inventories"]

    @property
    def get_vulnerability_report(
        self,
    ) -> Callable[
        [vulnerability.GetVulnerabilityReportRequest], vulnerability.VulnerabilityReport
    ]:
        r"""Return a callable for the get vulnerability report method over gRPC.

        Gets the vulnerability report for the specified VM
        instance. Only VMs with inventory data have
        vulnerability reports associated with them.

        Returns:
            Callable[[~.GetVulnerabilityReportRequest],
                    ~.VulnerabilityReport]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_vulnerability_report" not in self._stubs:
            self._stubs["get_vulnerability_report"] = self.grpc_channel.unary_unary(
                "/google.cloud.osconfig.v1.OsConfigZonalService/GetVulnerabilityReport",
                request_serializer=vulnerability.GetVulnerabilityReportRequest.serialize,
                response_deserializer=vulnerability.VulnerabilityReport.deserialize,
            )
        return self._stubs["get_vulnerability_report"]

    @property
    def list_vulnerability_reports(
        self,
    ) -> Callable[
        [vulnerability.ListVulnerabilityReportsRequest],
        vulnerability.ListVulnerabilityReportsResponse,
    ]:
        r"""Return a callable for the list vulnerability reports method over gRPC.

        List vulnerability reports for all VM instances in
        the specified zone.

        Returns:
            Callable[[~.ListVulnerabilityReportsRequest],
                    ~.ListVulnerabilityReportsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_vulnerability_reports" not in self._stubs:
            self._stubs["list_vulnerability_reports"] = self.grpc_channel.unary_unary(
                "/google.cloud.osconfig.v1.OsConfigZonalService/ListVulnerabilityReports",
                request_serializer=vulnerability.ListVulnerabilityReportsRequest.serialize,
                response_deserializer=vulnerability.ListVulnerabilityReportsResponse.deserialize,
            )
        return self._stubs["list_vulnerability_reports"]

    def close(self):
        self.grpc_channel.close()


__all__ = ("OsConfigZonalServiceGrpcTransport",)
