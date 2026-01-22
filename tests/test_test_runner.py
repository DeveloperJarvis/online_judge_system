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
# test_test_runner MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import pytest
from online_judge.core.test_runner import CaseRunner
from online_judge.core.sandbox_executor import SandboxExecutor
from online_judge.models.test_case import JudgeTestCase


def test_test_runner_single_case(tmp_path):
    code = "print(input())"
    file_path = tmp_path / "solution.py"
    file_path.write_text(code)

    executor = SandboxExecutor()
    runner = CaseRunner(executor)

    test_cases = [
        JudgeTestCase(
            input_data="hello",
            expected_output="hello",
        )
    ]

    results = runner.run(
        command=["python", str(file_path)],
        test_cases=test_cases,
        time_limit=2,
    )

    assert len(results) == 1
    assert results[0].passed is True
    assert results[0].actual_output == "hello"
