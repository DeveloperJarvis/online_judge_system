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
# evaluator MODULE
# --------------------------------------------------
"""
Evaluates test execution results.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from typing import List
from online_judge.models.execution_result import ExecutionResult
from online_judge.exceptions.execution_errors import WrongAnswerError


# --------------------------------------------------
# evaluator
# --------------------------------------------------
class Evaluator:
    """
    Evaluates correctness of outputs.
    """

    def evaluate(self, 
                 results: List[ExecutionResult]) -> None:
        """
        Raise error if any test fails.
        """
        for result in results:
            if not result.passed:
                raise WrongAnswerError(
                    f"Expected: {result.expected_output}, "
                    f"Got: {result.actual_output}"
                )
