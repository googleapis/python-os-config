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
# Generated code. DO NOT EDIT!
#
# Snippet for CreatePatchDeployment
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-os-config


# [START osconfig_v1_generated_OsConfigService_CreatePatchDeployment_sync]
from google.cloud import osconfig_v1


def sample_create_patch_deployment():
    # Create a client
    client = osconfig_v1.OsConfigServiceClient()

    # Initialize request argument(s)
    request = osconfig_v1.CreatePatchDeploymentRequest(
        parent="parent_value",
        patch_deployment_id="patch_deployment_id_value",
    )

    # Make the request
    response = client.create_patch_deployment(request=request)

    # Handle the response
    print(response)

# [END osconfig_v1_generated_OsConfigService_CreatePatchDeployment_sync]
