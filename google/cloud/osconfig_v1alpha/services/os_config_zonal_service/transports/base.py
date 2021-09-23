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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union
import packaging.version
import pkg_resources

import google.auth  # type: ignore
import google.api_core  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.osconfig_v1alpha.types import instance_os_policies_compliance
from google.cloud.osconfig_v1alpha.types import inventory
from google.cloud.osconfig_v1alpha.types import os_policy_assignments
from google.cloud.osconfig_v1alpha.types import vulnerability
from google.longrunning import operations_pb2  # type: ignore

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-cloud-os-config",).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()

try:
    # google.auth.__version__ was added in 1.26.0
    _GOOGLE_AUTH_VERSION = google.auth.__version__
except AttributeError:
    try:  # try pkg_resources if it is available
        _GOOGLE_AUTH_VERSION = pkg_resources.get_distribution("google-auth").version
    except pkg_resources.DistributionNotFound:  # pragma: NO COVER
        _GOOGLE_AUTH_VERSION = None


class OsConfigZonalServiceTransport(abc.ABC):
    """Abstract transport class for OsConfigZonalService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "osconfig.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        **kwargs,
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
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        scopes_kwargs = self._get_scopes_kwargs(self._host, scopes)

        # Save the scopes.
        self._scopes = scopes

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file, **scopes_kwargs, quota_project_id=quota_project_id
            )

        elif credentials is None:
            credentials, _ = google.auth.default(
                **scopes_kwargs, quota_project_id=quota_project_id
            )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

    # TODO(busunkim): This method is in the base transport
    # to avoid duplicating code across the transport classes. These functions
    # should be deleted once the minimum required versions of google-auth is increased.

    # TODO: Remove this function once google-auth >= 1.25.0 is required
    @classmethod
    def _get_scopes_kwargs(
        cls, host: str, scopes: Optional[Sequence[str]]
    ) -> Dict[str, Optional[Sequence[str]]]:
        """Returns scopes kwargs to pass to google-auth methods depending on the google-auth version"""

        scopes_kwargs = {}

        if _GOOGLE_AUTH_VERSION and (
            packaging.version.parse(_GOOGLE_AUTH_VERSION)
            >= packaging.version.parse("1.25.0")
        ):
            scopes_kwargs = {"scopes": scopes, "default_scopes": cls.AUTH_SCOPES}
        else:
            scopes_kwargs = {"scopes": scopes or cls.AUTH_SCOPES}

        return scopes_kwargs

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.create_os_policy_assignment: gapic_v1.method.wrap_method(
                self.create_os_policy_assignment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_os_policy_assignment: gapic_v1.method.wrap_method(
                self.update_os_policy_assignment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_os_policy_assignment: gapic_v1.method.wrap_method(
                self.get_os_policy_assignment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_os_policy_assignments: gapic_v1.method.wrap_method(
                self.list_os_policy_assignments,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_os_policy_assignment_revisions: gapic_v1.method.wrap_method(
                self.list_os_policy_assignment_revisions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_os_policy_assignment: gapic_v1.method.wrap_method(
                self.delete_os_policy_assignment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_instance_os_policies_compliance: gapic_v1.method.wrap_method(
                self.get_instance_os_policies_compliance,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_instance_os_policies_compliances: gapic_v1.method.wrap_method(
                self.list_instance_os_policies_compliances,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_inventory: gapic_v1.method.wrap_method(
                self.get_inventory, default_timeout=None, client_info=client_info,
            ),
            self.list_inventories: gapic_v1.method.wrap_method(
                self.list_inventories, default_timeout=None, client_info=client_info,
            ),
            self.get_vulnerability_report: gapic_v1.method.wrap_method(
                self.get_vulnerability_report,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_vulnerability_reports: gapic_v1.method.wrap_method(
                self.list_vulnerability_reports,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def create_os_policy_assignment(
        self,
    ) -> Callable[
        [os_policy_assignments.CreateOSPolicyAssignmentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_os_policy_assignment(
        self,
    ) -> Callable[
        [os_policy_assignments.UpdateOSPolicyAssignmentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_os_policy_assignment(
        self,
    ) -> Callable[
        [os_policy_assignments.GetOSPolicyAssignmentRequest],
        Union[
            os_policy_assignments.OSPolicyAssignment,
            Awaitable[os_policy_assignments.OSPolicyAssignment],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_os_policy_assignments(
        self,
    ) -> Callable[
        [os_policy_assignments.ListOSPolicyAssignmentsRequest],
        Union[
            os_policy_assignments.ListOSPolicyAssignmentsResponse,
            Awaitable[os_policy_assignments.ListOSPolicyAssignmentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_os_policy_assignment_revisions(
        self,
    ) -> Callable[
        [os_policy_assignments.ListOSPolicyAssignmentRevisionsRequest],
        Union[
            os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse,
            Awaitable[os_policy_assignments.ListOSPolicyAssignmentRevisionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_os_policy_assignment(
        self,
    ) -> Callable[
        [os_policy_assignments.DeleteOSPolicyAssignmentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_instance_os_policies_compliance(
        self,
    ) -> Callable[
        [instance_os_policies_compliance.GetInstanceOSPoliciesComplianceRequest],
        Union[
            instance_os_policies_compliance.InstanceOSPoliciesCompliance,
            Awaitable[instance_os_policies_compliance.InstanceOSPoliciesCompliance],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_instance_os_policies_compliances(
        self,
    ) -> Callable[
        [instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesRequest],
        Union[
            instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse,
            Awaitable[
                instance_os_policies_compliance.ListInstanceOSPoliciesCompliancesResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_inventory(
        self,
    ) -> Callable[
        [inventory.GetInventoryRequest],
        Union[inventory.Inventory, Awaitable[inventory.Inventory]],
    ]:
        raise NotImplementedError()

    @property
    def list_inventories(
        self,
    ) -> Callable[
        [inventory.ListInventoriesRequest],
        Union[
            inventory.ListInventoriesResponse,
            Awaitable[inventory.ListInventoriesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_vulnerability_report(
        self,
    ) -> Callable[
        [vulnerability.GetVulnerabilityReportRequest],
        Union[
            vulnerability.VulnerabilityReport,
            Awaitable[vulnerability.VulnerabilityReport],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_vulnerability_reports(
        self,
    ) -> Callable[
        [vulnerability.ListVulnerabilityReportsRequest],
        Union[
            vulnerability.ListVulnerabilityReportsResponse,
            Awaitable[vulnerability.ListVulnerabilityReportsResponse],
        ],
    ]:
        raise NotImplementedError()


__all__ = ("OsConfigZonalServiceTransport",)
