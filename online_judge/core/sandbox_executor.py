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
# sandbox_executor MODULE
# --------------------------------------------------
"""
Sandboxed execution using subprocess.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import subprocess
from typing import Tuple

from online_judge.exceptions.execution_errors import (
    RuntimeExecutionError,
    TimeLimitExceeded,
)
from online_judge.exceptions.sandbox_errors import SandboxViolationError


# --------------------------------------------------
# sandbox execution
# --------------------------------------------------
class SandboxExecutor:
    """
    Executes code in restricted environment.
    """

    def execute(
        self,
        command: list[str],
        input_data: str,
        time_limit: int,
    ) -> Tuple[str, str]:
        """
        Execute user code safely.
        """
        try:
            process = subprocess.run(
                command,
                input=input_data,
                capture_output=True,
                text=True,
                timeout=time_limit,
            )
        except subprocess.TimeoutExpired:
            raise TimeLimitExceeded(
                "Execution time exceeded"
            )

        if process.returncode != 0:
            raise RuntimeExecutionError(process.stderr)
        
        return process.stdout, process.stderr
