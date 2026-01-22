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
# test_compiler MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import pytest
from online_judge.core.compiler import Compiler
from online_judge.exceptions.execution_errors import CompilationError


def test_python_compiler_success(tmp_path):
    code = "print('hello')"
    file_path = tmp_path / "solution.py"
    file_path.write_text(code)

    compiler = Compiler()
    # should not raise
    compiler.compile(str(file_path), "python") 


def test_python_compiler_syntax_error(tmp_path):
    code = "print("
    file_path = tmp_path / "solution.py"
    file_path.write_text(code)

    compiler = Compiler()
    with pytest.raises(CompilationError):
        compiler.compile(str(file_path), "python")


def test_unsupported_language(tmp_path):
    code = "int main() {}"
    file_path = tmp_path / "solution.c"
    file_path.write_text(code)

    compiler = Compiler()
    with pytest.raises(CompilationError):
        compiler.compile(str(file_path), "c")
