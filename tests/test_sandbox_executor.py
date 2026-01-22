# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the Online Judge System Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Online Judge System - Run user-submitted code safely with test cases
#                   Skills: sandboxing, subprocess, security
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# test_sandbox_executor MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import pytest
from online_judge.core.sandbox_executor import SandboxExecutor
from online_judge.exceptions.execution_errors import (
    RuntimeExecutionError,
    TimeLimitExceeded,
)


def test_sandbox_executor_success(tmp_path):
    code = "print('ok')"
    file_path = tmp_path / "solution.py"
    file_path.write_text(code)

    executor = SandboxExecutor()
    stdout, stderr = executor.execute(
        command=["python", str(file_path)],
        input_data="",
        time_limit=2,
    )

    assert stdout.strip() == "ok"
    assert stderr == ""

def test_sandbox_executor_runtime_error(tmp_path):
    code = "raise ValueError('boom')"
    file_path = tmp_path / "solution.py"
    file_path.write_text(code)

    executor = SandboxExecutor()
    with pytest.raises(RuntimeExecutionError):
        executor.execute(
        command=["python", str(file_path)],
        input_data="",
        time_limit=2,
    )


def test_sandbox_executor_timeout(tmp_path):
    code = "while True: pass"
    file_path = tmp_path / "solution.py"
    file_path.write_text(code)

    executor = SandboxExecutor()
    with pytest.raises(TimeLimitExceeded):
        executor.execute(
        command=["python", str(file_path)],
        input_data="",
        time_limit=1,
    )
