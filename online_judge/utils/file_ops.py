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
# file_ops MODULE
# --------------------------------------------------
"""
Filesystem utilities for Online Judge System.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import os
import shutil
import tempfile
from typing import Optional


def create_temp_dir(prefix: str = "oj_") -> str:
    """
    Create a secure temporary directory for execution.
    """
    return tempfile.mkdtemp(prefix=prefix)


def write_code_file(
        directory: str,
        filename: str,
        code: str,
        encoding: str = "utf-8",
    ) -> str:
    """
    Write submitted code to a file inside a sandbox directory.
    """
    path = os.path.join(directory, filename)
    with open(path, "w", encoding=encoding) as f:
        f.write(code)
    return path


def cleanup_dir(path: str) -> None:
    """
    Safely remove a directory and all its contents.
    """
    if path and os.path.exists(path):
        shutil.rmtree(path, ignore_errors=True)
