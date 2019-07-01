# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import sys
import pytest

# These fixtures are shared between sync and async clients
from .client_fixtures import (
    pipeline,
    pipeline_manual_cb,
    device_connection_string,
    module_connection_string,
    device_sas_token_string,
    module_sas_token_string,
    edge_container_env_vars,
    x509,
)

collect_ignore = []

# Ignore Async tests if below Python 3.5
if sys.version_info < (3, 5):
    collect_ignore.append("aio")
