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
# execution_result MODULE
# --------------------------------------------------
"""
Execution result model.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from dataclasses import dataclass
from typing import Optional


# --------------------------------------------------
# execution result
# --------------------------------------------------
@dataclass(frozen=True)
class ExecutionResult:
    """
    Result of executing code against a test case.
    """
    passed: bool
    actual_output: str
    input_data: str
    expected_output: str
    execution_time: float = 0.0
    memory_used_mb: int = 0
    error: Optional[str] = None
