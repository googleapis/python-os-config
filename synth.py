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

"""This script is used to synthesize generated parts of this library."""
import os

import synthtool as s
import synthtool.gcp as gcp
from synthtool.languages import python

gapic = gcp.GAPICMicrogenerator()
common = gcp.CommonTemplates()

# ----------------------------------------------------------------------------
# Generate OS Config GAPIC layer
# ----------------------------------------------------------------------------
library = gapic.py_library(
    "osconfig", "v1"
)

s.move(library, excludes=["nox.py", "setup.py", "README.rst", "docs/index.rst"])

# correct license headers
python.fix_pb2_headers()
python.fix_pb2_grpc_headers()

# rename to google-cloud-os-config
s.replace(["google/**/*.py", "tests/**/*.py"], "google-cloud-osconfig", "google-cloud-os-config")

# Add newline after last item in list
s.replace("google/cloud/**/*_client.py",
"(-  Must be unique within the project\.)",
"\g<1>\n")

# Add missing blank line before Attributes: in generated docstrings
# https://github.com/googleapis/protoc-docs-plugin/pull/31
s.replace(
    "google/cloud/pubsub_v1/proto/pubsub_pb2.py",
    "(\s+)Attributes:",
    "\n\g<1>Attributes:"
)

# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------
templated_files = common.py_library(
    samples=False,
    microgenerator=True,
    unit_test_python_versions=["3.6", "3.7", "3.8"],
    system_test_python_versions=["3.7"],
)
s.move(
    templated_files, excludes=[".coveragerc"]
)  # the microgenerator has a good coveragerc file


s.shell.run(["nox", "-s", "blacken"], hide_output=False)