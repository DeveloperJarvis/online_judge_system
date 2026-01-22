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
# compiler MODULE
# --------------------------------------------------
"""
Compiler module for Online Judge.
Handles compilation or syntax validation.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import subprocess
from online_judge.exceptions.execution_errors import CompilationError


# --------------------------------------------------
# compiler
# --------------------------------------------------
class Compiler:
    """
    Compiler or validates user-submitted code.
    """

    def compile(self, source_file: str,
                language: str) -> None:
        """
        Compile source code if required.
        """
        if language == "python":
            # Python: syntax check only
            result = subprocess.run(
                ["python", "-m", "py_compile", source_file],
                capture_output=True,
                text=True,
            )
            if result.returncode != 0:
                raise CompilationError(result.stderr)
        else:
            raise CompilationError(
                f"Unsupported language: {language}"
            )
