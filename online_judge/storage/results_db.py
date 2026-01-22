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
# results_db MODULE
# --------------------------------------------------
"""
Execution results storage.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from typing import Dict, List
from online_judge.models.execution_result import ExecutionResult


# --------------------------------------------------
# results DB
# --------------------------------------------------
class ResultsDB:
    """
    In-memory storage for execution results.
    """

    def __init__(self) -> None:
        self._results: Dict[str, List[ExecutionResult]] = {}
    
    def save(
        self,
        submission_id: str,
        result: ExecutionResult,
    ) -> None:
        """
        Save result for a submission.
        """
        self._results.setdefault(
            submission_id, []
        ).append(result)
    
    def get_results(
            self,
            submission_id: str,
        ) -> List[ExecutionResult]:
        """
        Get all results for a submission.
        """
        return self._results.get(submission_id, [])
    
    def clear(self) -> None:
        """
        Clear all stored results.
        """
        self._results.clear()
