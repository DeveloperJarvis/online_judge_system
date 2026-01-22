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
# submissions MODULE
# --------------------------------------------------
"""
In-memory submission storage.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from typing import Dict, List
from online_judge.models.submission import Submission


# --------------------------------------------------
# submission store
# --------------------------------------------------
class SubmissionStore:
    """
    Simple in-memory submission store.
    """

    def __init__(self) -> None:
        self._submissions: Dict[str, Submission] = {}
    
    def save(self, submission: Submission) -> None:
        """
        Store a submission.
        """
        self._submissions[
            submission.submission_id] = submission
    
    def get(self, submission_id: str) -> Submission:
        """
        Retrieve a submission by ID.
        """
        return self._submissions[submission_id]
    
    def list_all(self) -> List[Submission]:
        """
        List all submissions.
        """
        return list(self._submissions.values())

