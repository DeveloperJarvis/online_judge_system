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
# execution_errors MODULE
# --------------------------------------------------
"""
Execution-related errors for Online Judge System.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------


# --------------------------------------------------
# online judge error
# --------------------------------------------------
class OnlineJudgeError(Exception):
    """
    Base class for all Online Judge Errors.
    """
    pass


# --------------------------------------------------
# compilation error
# --------------------------------------------------
class CompilationError(OnlineJudgeError):
    """
    Raised when user code fails to compile.
    """
    pass


# --------------------------------------------------
# runtime execution error
# --------------------------------------------------
class RuntimeExecutionError(OnlineJudgeError):
    """
    Raised when runtime error occurs during execution.
    """
    pass


# --------------------------------------------------
# time limit exceeded
# --------------------------------------------------
class TimeLimitExceeded(OnlineJudgeError):
    """
    Raised when exectuon exceeds allowed time.
    """
    pass


# --------------------------------------------------
# memory limit exceeded
# --------------------------------------------------
class MemoryLimitExceeded(OnlineJudgeError):
    """
    Raised when execution exceeds memory limit.
    """
    pass


# --------------------------------------------------
# wrong answer error
# --------------------------------------------------
class WrongAnswerError(OnlineJudgeError):
    """
    Raised when execution exceeds memory limit.
    """
    pass
