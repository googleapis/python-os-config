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

"""Wrappers for protocol buffer enum types."""

import enum


class DayOfWeek(enum.IntEnum):
    """
    Represents a day of the week.

    Attributes:
      DAY_OF_WEEK_UNSPECIFIED (int): The day of the week is unspecified.
      MONDAY (int): Monday
      TUESDAY (int): Tuesday
      WEDNESDAY (int): Wednesday
      THURSDAY (int): Thursday
      FRIDAY (int): Friday
      SATURDAY (int): Saturday
      SUNDAY (int): Sunday
    """

    DAY_OF_WEEK_UNSPECIFIED = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


class AptSettings(object):
    class Type(enum.IntEnum):
        """
        Apt patch type.

        Attributes:
          TYPE_UNSPECIFIED (int): By default, upgrade will be performed.
          DIST (int): Runs ``apt-get dist-upgrade``.
          UPGRADE (int): Runs ``apt-get upgrade``.
        """

        TYPE_UNSPECIFIED = 0
        DIST = 1
        UPGRADE = 2


class ExecStepConfig(object):
    class Interpreter(enum.IntEnum):
        """
        The interpreter used to execute the a file.

        Attributes:
          INTERPRETER_UNSPECIFIED (int): Invalid for a Windows ExecStepConfig. For a Linux ExecStepConfig, the
          interpreter will be parsed from the shebang line of the script if
          unspecified.
          SHELL (int): Indicates that the script is run with ``/bin/sh`` on Linux and
          ``cmd`` on Windows.
          POWERSHELL (int): Indicates that the file is run with PowerShell flags
          ``-NonInteractive``, ``-NoProfile``, and ``-ExecutionPolicy Bypass``.
        """

        INTERPRETER_UNSPECIFIED = 0
        SHELL = 1
        POWERSHELL = 2


class Instance(object):
    class PatchState(enum.IntEnum):
        """
        Patch state of an instance.

        Attributes:
          PATCH_STATE_UNSPECIFIED (int): Unspecified.
          PENDING (int): The instance is not yet notified.
          INACTIVE (int): Instance is inactive and cannot be patched.
          NOTIFIED (int): The instance is notified that it should be patched.
          STARTED (int): The instance has started the patching process.
          DOWNLOADING_PATCHES (int): The instance is downloading patches.
          APPLYING_PATCHES (int): The instance is applying patches.
          REBOOTING (int): The instance is rebooting.
          SUCCEEDED (int): The instance has completed applying patches.
          SUCCEEDED_REBOOT_REQUIRED (int): The instance has completed applying patches but a reboot is required.
          FAILED (int): The instance has failed to apply the patch.
          ACKED (int): The instance acked the notification and will start shortly.
          TIMED_OUT (int): The instance exceeded the time out while applying the patch.
          RUNNING_PRE_PATCH_STEP (int): The instance is running the pre-patch step.
          RUNNING_POST_PATCH_STEP (int): The instance is running the post-patch step.
          NO_AGENT_DETECTED (int): The service could not detect the presence of the agent. Check to ensure
          that the agent is installed, running, and able to communicate with the
          service.
        """

        PATCH_STATE_UNSPECIFIED = 0
        PENDING = 1
        INACTIVE = 2
        NOTIFIED = 3
        STARTED = 4
        DOWNLOADING_PATCHES = 5
        APPLYING_PATCHES = 6
        REBOOTING = 7
        SUCCEEDED = 8
        SUCCEEDED_REBOOT_REQUIRED = 9
        FAILED = 10
        ACKED = 11
        TIMED_OUT = 12
        RUNNING_PRE_PATCH_STEP = 13
        RUNNING_POST_PATCH_STEP = 14
        NO_AGENT_DETECTED = 15


class Inventory(object):
    class Item(object):
        class OriginType(enum.IntEnum):
            """
            The origin of a specific inventory item.

            Attributes:
              ORIGIN_TYPE_UNSPECIFIED (int): Invalid. An origin type must be specified.
              INVENTORY_REPORT (int): This inventory item was discovered as the result of the agent
              reporting inventory via the reporting API.
            """

            ORIGIN_TYPE_UNSPECIFIED = 0
            INVENTORY_REPORT = 1

        class Type(enum.IntEnum):
            """
            The different types of inventory that are tracked on a VM.

            Attributes:
              TYPE_UNSPECIFIED (int): Invalid. An type must be specified.
              INSTALLED_PACKAGE (int): This represents a package that is installed on the VM.
              AVAILABLE_PACKAGE (int): This represents an update that is available for a package.
            """

            TYPE_UNSPECIFIED = 0
            INSTALLED_PACKAGE = 1
            AVAILABLE_PACKAGE = 2


class PatchConfig(object):
    class RebootConfig(enum.IntEnum):
        """
        Post-patch reboot settings.

        Attributes:
          REBOOT_CONFIG_UNSPECIFIED (int): The default behavior is DEFAULT.
          DEFAULT (int): The agent decides if a reboot is necessary by checking signals such
          as registry keys on Windows or ``/var/run/reboot-required`` on APT based
          systems. On RPM based systems, a set of core system package install
          times are compared with system boot time.
          ALWAYS (int): Always reboot the machine after the update completes.
          NEVER (int): Never reboot the machine after the update completes.
        """

        REBOOT_CONFIG_UNSPECIFIED = 0
        DEFAULT = 1
        ALWAYS = 2
        NEVER = 3


class PatchJob(object):
    class State(enum.IntEnum):
        """
        Enumeration of the various states a patch job passes through as it
        executes.

        Attributes:
          STATE_UNSPECIFIED (int): State must be specified.
          STARTED (int): The patch job was successfully initiated.
          INSTANCE_LOOKUP (int): The patch job is looking up instances to run the patch on.
          PATCHING (int): Instances are being patched.
          SUCCEEDED (int): Patch job completed successfully.
          COMPLETED_WITH_ERRORS (int): Patch job completed but there were errors.
          CANCELED (int): The patch job was canceled.
          TIMED_OUT (int): The patch job timed out.
        """

        STATE_UNSPECIFIED = 0
        STARTED = 1
        INSTANCE_LOOKUP = 2
        PATCHING = 3
        SUCCEEDED = 4
        COMPLETED_WITH_ERRORS = 5
        CANCELED = 6
        TIMED_OUT = 7


class PatchRollout(object):
    class Mode(enum.IntEnum):
        """
        Type of the rollout.

        Attributes:
          MODE_UNSPECIFIED (int): Mode must be specified.
          ZONE_BY_ZONE (int): Patches are applied one zone at a time. The patch job begins in the
          region with the lowest number of targeted VMs. Within the region,
          patching begins in the zone with the lowest number of targeted VMs. If
          multiple regions (or zones within a region) have the same number of
          targeted VMs, a tie-breaker is achieved by sorting the regions or zones
          in alphabetical order.
          CONCURRENT_ZONES (int): Patches are applied to VMs in all zones at the same time.
        """

        MODE_UNSPECIFIED = 0
        ZONE_BY_ZONE = 1
        CONCURRENT_ZONES = 2


class RecurringSchedule(object):
    class Frequency(enum.IntEnum):
        """
        Specifies the frequency of the recurring patch deployments.

        Attributes:
          FREQUENCY_UNSPECIFIED (int): Invalid. A frequency must be specified.
          WEEKLY (int): Indicates that the frequency should be expressed in terms of
          weeks.
          MONTHLY (int): Indicates that the frequency should be expressed in terms of
          months.
        """

        FREQUENCY_UNSPECIFIED = 0
        WEEKLY = 1
        MONTHLY = 2


class WindowsUpdateSettings(object):
    class Classification(enum.IntEnum):
        """
        Microsoft Windows update classifications as defined in [1]
        https://support.microsoft.com/en-us/help/824684/description-of-the-standard-terminology-that-is-used-to-describe-micro

        Attributes:
          CLASSIFICATION_UNSPECIFIED (int): Invalid. If classifications are included, they must be specified.
          CRITICAL (int): "A widely released fix for a specific problem that addresses a
          critical, non-security-related bug." [1]
          SECURITY (int): "A widely released fix for a product-specific, security-related
          vulnerability. Security vulnerabilities are rated by their severity. The
          severity rating is indicated in the Microsoft security bulletin as
          critical, important, moderate, or low." [1]
          DEFINITION (int): "A widely released and frequent software update that contains
          additions to a product's definition database. Definition databases are
          often used to detect objects that have specific attributes, such as
          malicious code, phishing websites, or junk mail." [1]
          DRIVER (int): "Software that controls the input and output of a device." [1]
          FEATURE_PACK (int): "New product functionality that is first distributed outside the
          context of a product release and that is typically included in the next
          full product release." [1]
          SERVICE_PACK (int): "A tested, cumulative set of all hotfixes, security updates,
          critical updates, and updates. Additionally, service packs may contain
          additional fixes for problems that are found internally since the
          release of the product. Service packs my also contain a limited number
          of customer-requested design changes or features." [1]
          TOOL (int): "A utility or feature that helps complete a task or set of tasks."
          [1]
          UPDATE_ROLLUP (int): "A tested, cumulative set of hotfixes, security updates, critical
          updates, and updates that are packaged together for easy deployment. A
          rollup generally targets a specific area, such as security, or a
          component of a product, such as Internet Information Services (IIS)."
          [1]
          UPDATE (int): "A widely released fix for a specific problem. An update addresses a
          noncritical, non-security-related bug." [1]
        """

        CLASSIFICATION_UNSPECIFIED = 0
        CRITICAL = 1
        SECURITY = 2
        DEFINITION = 3
        DRIVER = 4
        FEATURE_PACK = 5
        SERVICE_PACK = 6
        TOOL = 7
        UPDATE_ROLLUP = 8
        UPDATE = 9
