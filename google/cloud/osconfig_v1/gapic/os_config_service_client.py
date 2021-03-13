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

"""Accesses the google.cloud.osconfig.v1 OsConfigService API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.page_iterator
import google.api_core.path_template
import grpc

from google.cloud.osconfig_v1.gapic import enums
from google.cloud.osconfig_v1.gapic import os_config_service_client_config
from google.cloud.osconfig_v1.gapic.transports import os_config_service_grpc_transport
from google.cloud.osconfig_v1.proto import osconfig_service_pb2_grpc
from google.cloud.osconfig_v1.proto import patch_deployments_pb2
from google.cloud.osconfig_v1.proto import patch_jobs_pb2
from google.protobuf import duration_pb2
from google.protobuf import empty_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    "google-cloud-os-config",
).version


class OsConfigServiceClient(object):
    """
    OS Config API

    The OS Config service is a server-side component that you can use to
    manage package installations and patch jobs for virtual machine instances.
    """

    SERVICE_ADDRESS = "osconfig.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.cloud.osconfig.v1.OsConfigService"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            OsConfigServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def patch_deployment_path(cls, project, patch_deployment):
        """Return a fully-qualified patch_deployment string."""
        return google.api_core.path_template.expand(
            "projects/{project}/patchDeployments/{patch_deployment}",
            project=project,
            patch_deployment=patch_deployment,
        )

    @classmethod
    def patch_job_path(cls, project, patch_job):
        """Return a fully-qualified patch_job string."""
        return google.api_core.path_template.expand(
            "projects/{project}/patchJobs/{patch_job}",
            project=project,
            patch_job=patch_job,
        )

    @classmethod
    def project_path(cls, project):
        """Return a fully-qualified project string."""
        return google.api_core.path_template.expand(
            "projects/{project}", project=project,
        )

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.OsConfigServiceGrpcTransport,
                    Callable[[~.Credentials, type], ~.OsConfigServiceGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = os_config_service_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=os_config_service_grpc_transport.OsConfigServiceGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = os_config_service_grpc_transport.OsConfigServiceGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials,
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION,
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME],
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def execute_patch_job(
        self,
        parent,
        instance_filter,
        description=None,
        patch_config=None,
        duration=None,
        dry_run=None,
        display_name=None,
        rollout=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Patch VM instances by creating and running a patch job.

        Example:
            >>> from google.cloud import osconfig_v1
            >>>
            >>> client = osconfig_v1.OsConfigServiceClient()
            >>>
            >>> parent = client.project_path('[PROJECT]')
            >>>
            >>> # TODO: Initialize `instance_filter`:
            >>> instance_filter = {}
            >>>
            >>> response = client.execute_patch_job(parent, instance_filter)

        Args:
            parent (str): Required. The project in which to run this patch in the form
                ``projects/*``
            instance_filter (Union[dict, ~google.cloud.osconfig_v1.types.PatchInstanceFilter]): Required. Instances to patch, either explicitly or filtered by some
                criteria such as zone or labels.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.osconfig_v1.types.PatchInstanceFilter`
            description (str): Description of the patch job. Length of the description is limited
                to 1024 characters.
            patch_config (Union[dict, ~google.cloud.osconfig_v1.types.PatchConfig]): Patch configuration being applied. If omitted, instances are
                patched using the default configurations.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.osconfig_v1.types.PatchConfig`
            duration (Union[dict, ~google.cloud.osconfig_v1.types.Duration]): Duration of the patch job. After the duration ends, the patch job
                times out.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.osconfig_v1.types.Duration`
            dry_run (bool): If this patch is a dry-run only, instances are contacted but
                will do nothing.
            display_name (str): Display name for this patch job. This does not have to be unique.
            rollout (Union[dict, ~google.cloud.osconfig_v1.types.PatchRollout]): Rollout strategy of the patch job.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.osconfig_v1.types.PatchRollout`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.osconfig_v1.types.PatchJob` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "execute_patch_job" not in self._inner_api_calls:
            self._inner_api_calls[
                "execute_patch_job"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.execute_patch_job,
                default_retry=self._method_configs["ExecutePatchJob"].retry,
                default_timeout=self._method_configs["ExecutePatchJob"].timeout,
                client_info=self._client_info,
            )

        request = patch_jobs_pb2.ExecutePatchJobRequest(
            parent=parent,
            instance_filter=instance_filter,
            description=description,
            patch_config=patch_config,
            duration=duration,
            dry_run=dry_run,
            display_name=display_name,
            rollout=rollout,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["execute_patch_job"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_patch_job(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Get the patch job. This can be used to track the progress of an
        ongoing patch job or review the details of completed jobs.

        Example:
            >>> from google.cloud import osconfig_v1
            >>>
            >>> client = osconfig_v1.OsConfigServiceClient()
            >>>
            >>> name = client.patch_job_path('[PROJECT]', '[PATCH_JOB]')
            >>>
            >>> response = client.get_patch_job(name)

        Args:
            name (str): Required. Name of the patch in the form ``projects/*/patchJobs/*``
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.osconfig_v1.types.PatchJob` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_patch_job" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_patch_job"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_patch_job,
                default_retry=self._method_configs["GetPatchJob"].retry,
                default_timeout=self._method_configs["GetPatchJob"].timeout,
                client_info=self._client_info,
            )

        request = patch_jobs_pb2.GetPatchJobRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_patch_job"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def cancel_patch_job(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Cancel a patch job. The patch job must be active. Canceled patch jobs
        cannot be restarted.

        Example:
            >>> from google.cloud import osconfig_v1
            >>>
            >>> client = osconfig_v1.OsConfigServiceClient()
            >>>
            >>> name = client.patch_job_path('[PROJECT]', '[PATCH_JOB]')
            >>>
            >>> response = client.cancel_patch_job(name)

        Args:
            name (str): Required. Name of the patch in the form ``projects/*/patchJobs/*``
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.osconfig_v1.types.PatchJob` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "cancel_patch_job" not in self._inner_api_calls:
            self._inner_api_calls[
                "cancel_patch_job"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.cancel_patch_job,
                default_retry=self._method_configs["CancelPatchJob"].retry,
                default_timeout=self._method_configs["CancelPatchJob"].timeout,
                client_info=self._client_info,
            )

        request = patch_jobs_pb2.CancelPatchJobRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["cancel_patch_job"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_patch_jobs(
        self,
        parent,
        page_size=None,
        filter_=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Get a list of patch jobs.

        Example:
            >>> from google.cloud import osconfig_v1
            >>>
            >>> client = osconfig_v1.OsConfigServiceClient()
            >>>
            >>> parent = client.project_path('[PROJECT]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_patch_jobs(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_patch_jobs(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. In the form of ``projects/*``
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            filter_ (str): If provided, this field specifies the criteria that must be met by
                patch jobs to be included in the response. Currently, filtering is only
                available on the patch_deployment field.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.osconfig_v1.types.PatchJob` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_patch_jobs" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_patch_jobs"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_patch_jobs,
                default_retry=self._method_configs["ListPatchJobs"].retry,
                default_timeout=self._method_configs["ListPatchJobs"].timeout,
                client_info=self._client_info,
            )

        request = patch_jobs_pb2.ListPatchJobsRequest(
            parent=parent, page_size=page_size, filter=filter_,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_patch_jobs"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="patch_jobs",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def list_patch_job_instance_details(
        self,
        parent,
        page_size=None,
        filter_=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Get a list of instance details for a given patch job.

        Example:
            >>> from google.cloud import osconfig_v1
            >>>
            >>> client = osconfig_v1.OsConfigServiceClient()
            >>>
            >>> parent = client.patch_job_path('[PROJECT]', '[PATCH_JOB]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_patch_job_instance_details(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_patch_job_instance_details(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. The parent for the instances are in the form of
                ``projects/*/patchJobs/*``.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            filter_ (str): A filter expression that filters results listed in the response.
                This field supports filtering results by instance zone, name, state, or
                ``failure_reason``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.osconfig_v1.types.PatchJobInstanceDetails` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_patch_job_instance_details" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_patch_job_instance_details"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_patch_job_instance_details,
                default_retry=self._method_configs["ListPatchJobInstanceDetails"].retry,
                default_timeout=self._method_configs[
                    "ListPatchJobInstanceDetails"
                ].timeout,
                client_info=self._client_info,
            )

        request = patch_jobs_pb2.ListPatchJobInstanceDetailsRequest(
            parent=parent, page_size=page_size, filter=filter_,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_patch_job_instance_details"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="patch_job_instance_details",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def create_patch_deployment(
        self,
        parent,
        patch_deployment_id,
        patch_deployment,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Create an OS Config patch deployment.

        Example:
            >>> from google.cloud import osconfig_v1
            >>>
            >>> client = osconfig_v1.OsConfigServiceClient()
            >>>
            >>> parent = client.project_path('[PROJECT]')
            >>>
            >>> # TODO: Initialize `patch_deployment_id`:
            >>> patch_deployment_id = ''
            >>>
            >>> # TODO: Initialize `patch_deployment`:
            >>> patch_deployment = {}
            >>>
            >>> response = client.create_patch_deployment(parent, patch_deployment_id, patch_deployment)

        Args:
            parent (str): Required. The project to apply this patch deployment to in the form
                ``projects/*``.
            patch_deployment_id (str): Required. A name for the patch deployment in the project. When
                creating a name the following rules apply:

                -  Must contain only lowercase letters, numbers, and hyphens.
                -  Must start with a letter.
                -  Must be between 1-63 characters.
                -  Must end with a number or a letter.
                -  Must be unique within the project.

            patch_deployment (Union[dict, ~google.cloud.osconfig_v1.types.PatchDeployment]): Required. The patch deployment to create.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.osconfig_v1.types.PatchDeployment`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.osconfig_v1.types.PatchDeployment` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_patch_deployment" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_patch_deployment"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_patch_deployment,
                default_retry=self._method_configs["CreatePatchDeployment"].retry,
                default_timeout=self._method_configs["CreatePatchDeployment"].timeout,
                client_info=self._client_info,
            )

        request = patch_deployments_pb2.CreatePatchDeploymentRequest(
            parent=parent,
            patch_deployment_id=patch_deployment_id,
            patch_deployment=patch_deployment,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_patch_deployment"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_patch_deployment(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Get an OS Config patch deployment.

        Example:
            >>> from google.cloud import osconfig_v1
            >>>
            >>> client = osconfig_v1.OsConfigServiceClient()
            >>>
            >>> name = client.patch_deployment_path('[PROJECT]', '[PATCH_DEPLOYMENT]')
            >>>
            >>> response = client.get_patch_deployment(name)

        Args:
            name (str): Required. The resource name of the patch deployment in the form
                ``projects/*/patchDeployments/*``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.osconfig_v1.types.PatchDeployment` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_patch_deployment" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_patch_deployment"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_patch_deployment,
                default_retry=self._method_configs["GetPatchDeployment"].retry,
                default_timeout=self._method_configs["GetPatchDeployment"].timeout,
                client_info=self._client_info,
            )

        request = patch_deployments_pb2.GetPatchDeploymentRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_patch_deployment"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_patch_deployments(
        self,
        parent,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Get a page of OS Config patch deployments.

        Example:
            >>> from google.cloud import osconfig_v1
            >>>
            >>> client = osconfig_v1.OsConfigServiceClient()
            >>>
            >>> parent = client.project_path('[PROJECT]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_patch_deployments(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_patch_deployments(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. The resource name of the parent in the form
                ``projects/*``.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.osconfig_v1.types.PatchDeployment` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_patch_deployments" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_patch_deployments"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_patch_deployments,
                default_retry=self._method_configs["ListPatchDeployments"].retry,
                default_timeout=self._method_configs["ListPatchDeployments"].timeout,
                client_info=self._client_info,
            )

        request = patch_deployments_pb2.ListPatchDeploymentsRequest(
            parent=parent, page_size=page_size,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_patch_deployments"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="patch_deployments",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def delete_patch_deployment(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Delete an OS Config patch deployment.

        Example:
            >>> from google.cloud import osconfig_v1
            >>>
            >>> client = osconfig_v1.OsConfigServiceClient()
            >>>
            >>> name = client.patch_deployment_path('[PROJECT]', '[PATCH_DEPLOYMENT]')
            >>>
            >>> client.delete_patch_deployment(name)

        Args:
            name (str): Required. The resource name of the patch deployment in the form
                ``projects/*/patchDeployments/*``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_patch_deployment" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_patch_deployment"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_patch_deployment,
                default_retry=self._method_configs["DeletePatchDeployment"].retry,
                default_timeout=self._method_configs["DeletePatchDeployment"].timeout,
                client_info=self._client_info,
            )

        request = patch_deployments_pb2.DeletePatchDeploymentRequest(name=name,)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_patch_deployment"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
