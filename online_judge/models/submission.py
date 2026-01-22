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
# submission MODULE
# --------------------------------------------------
"""
Submission model.
Represents a user-submitted solution.
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from dataclasses import dataclass, field
from typing import Optional
import uuid
import time
from typing import List

from online_judge.models.test_case import JudgeTestCase


# --------------------------------------------------
# submission
# --------------------------------------------------
@dataclass(frozen=True)
class Submission:
    """
    Represents a code submission.
    """
    code: str
    language: str
    problem_id: str
    test_cases: List[JudgeTestCase]
    time_limit: int
    
    submission_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )
    created_at: float = field(
        default_factory=time.time
    )
    user_id: Optional[str] = None

    def run_command(self, file_path: str) -> list[str]:
        if self.language == "python":
            return ["python", file_path]
        raise ValueError(
            f"Unsupported langauge: {self.language}"
        )
