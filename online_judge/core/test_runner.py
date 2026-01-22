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
# test_runner MODULE
# --------------------------------------------------
"""
Runs submission against multiple test cases.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from typing import List

from online_judge.core.sandbox_executor import SandboxExecutor
from online_judge.models.test_case import JudgeTestCase
from online_judge.models.execution_result import ExecutionResult


# --------------------------------------------------
# test runner
# --------------------------------------------------
class CaseRunner:
    """
    Executes test cases sequentially.
    """

    def __init__(self, executor: SandboxExecutor):
        self.executor = executor
    
    def run(
        self,
        command: list[str],
        test_cases: List[JudgeTestCase],
        time_limit: int,
    ) -> List[ExecutionResult]:
        results: List[ExecutionResult] = []

        for test in test_cases:
            stdout, stderr = self.executor.execute(
                command,
                test.input_data,
                time_limit,
            )
            expected = test.expected_output or ""
            results.append(
                ExecutionResult(
                    input_data=test.input_data,
                    expected_output=test.expected_output,
                    actual_output=stdout.strip(),
                    passed=(
                True if test.expected_output is None 
                else stdout.strip() == expected.strip()
                    ),
                )
            )
    
        return results
