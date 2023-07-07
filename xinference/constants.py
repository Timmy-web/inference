# Copyright 2022-2023 XProbe Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from pathlib import Path

XINFERENCE_HOME = str(Path.home() / ".xinference")
XINFERENCE_CACHE_DIR = os.path.join(XINFERENCE_HOME, "cache")
XINFERENCE_LOG_DIR = os.path.join(XINFERENCE_HOME, "logs")

XINFERENCE_DEFAULT_HOST = "127.0.0.1"
XINFERENCE_DEFAULT_SUPERVISOR_PORT = 9998
XINFERENCE_DEFAULT_WORKER_PORT = 9999