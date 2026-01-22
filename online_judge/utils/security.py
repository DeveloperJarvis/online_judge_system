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
# security MODULE
# --------------------------------------------------
"""
Security helpers for Online Judge System.

⚠️ NOTE:
This is a *baseline* implementation.
A real production judge must be OS-level sandboxing
(e.g., Docker, seccomp, namespaces).
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import ast
from typing import List
try:
    import resource
except ImportError:
    resource = None
    import warnings


# Dangerous modules that should not be allowed
BLOCKED_IMPORTS: List[str] = [
    "os",
    "sys",
    "subprocess",
    "socket",
    "shutil",
    "pathlib",
    "resource",
]


def is_code_safe(code: str) -> bool:
    """
    Perform static analysis to reject obviously dangerous code.
    """
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return False
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if (alias.name.split(".")[0] 
                    in BLOCKED_IMPORTS):
                    return False
        elif isinstance(node, ast.ImportFrom):
            if node.module and (node.module.split(".")
                                in BLOCKED_IMPORTS):
                return False
    return True


def enforce_resource_limits(
        cpu_seconds: int,
        memory_mb: int,
    ) -> None:
    """
    Apply OS-level resource limits (Unix only).
    No-op on Windows.
    """
    if resource is None:
        warnings.warn(
            "OS-level resource limits are not supported "
            "on this platform (Windows). Execution is "
            "not fully sandboxed.",
            RuntimeWarning
        )
        return  # Windows: cannot enforce limits
    
    # CPU time limit
    resource.setrlimit(
        resource.RLIMIT_CPU,
        (cpu_seconds, cpu_seconds),
    )

    # Address space (memory) limit
    memory_bytes = memory_mb * 1024 * 1024
    resource.setrlimit(
        resource.RLIMIT_AS,
        (memory_bytes, memory_bytes),
    )
