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
# worker MODULE
# --------------------------------------------------
"""
Worker orchestrates compilation, execution and evaluation
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from online_judge.core.compiler import Compiler
from online_judge.core.sandbox_executor import SandboxExecutor
from online_judge.core.test_runner import CaseRunner
from online_judge.core.evaluator import Evaluator
from online_judge.models.submission import Submission
from online_judge.utils.file_ops import (
    create_temp_dir,
    write_code_file,
    cleanup_dir,
)


# --------------------------------------------------
# worker
# --------------------------------------------------
class Worker:
    """
    Main execution pipeline.
    """

    def __init__(self) -> None:
        self.compiler = Compiler()
        self.executor = SandboxExecutor()
        self.runner = CaseRunner(self.executor)
        self.evaluator = Evaluator()
    
    def process(self, submission: Submission) -> None:
        """
        Process a single submission.
        """
        temp_dir = create_temp_dir()
        try:
            source_file = write_code_file(
                temp_dir, "solution.py", submission.code
            )

            self.compiler.compile(
                source_file, submission.language,
            )

            results = self.runner.run(
                command=submission.run_command(source_file),
                test_cases=submission.test_cases,
                time_limit=submission.time_limit,
            )

            self.evaluator.evaluate(results)
            return results
        finally:
            cleanup_dir(temp_dir)
