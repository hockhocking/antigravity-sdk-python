# Copyright 2026 Google LLC
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

"""Pytest configuration for OSS test runs."""

from absl import flags
from absl.testing import absltest  # noqa: F401  # Registers --test_tmpdir flag.
import pytest


@pytest.fixture(scope="session", autouse=True)
def _parse_absl_flags(tmp_path_factory: pytest.TempPathFactory) -> None:
  """Parses absl flags once per pytest session so absltest helpers work."""
  if not flags.FLAGS.is_parsed():
    tmp_dir = str(tmp_path_factory.mktemp("absl_test_tmpdir"))
    flags.FLAGS(["pytest", f"--test_tmpdir={tmp_dir}"], known_only=True)
