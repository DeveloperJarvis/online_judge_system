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
# test_evaluator MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import pytest
from online_judge.core.evaluator import Evaluator
from online_judge.models.execution_result import ExecutionResult
from online_judge.exceptions.execution_errors import WrongAnswerError


def test_evaluator_all_passed():
    results = [
        ExecutionResult(
            passed=True,
            actual_output="4",
            expected_output="4",
            input_data="2",
        )
    ]
    evaluator = Evaluator()
    evaluator.evaluate(results) # should not raise


def test_evaluator_wrong_answer():
    results = [
        ExecutionResult(
            passed=False,
            actual_output="3",
            expected_output="4",
            input_data="2",
        )
    ]
    evaluator = Evaluator()
    with pytest.raises(WrongAnswerError):
        evaluator.evaluate(results)
