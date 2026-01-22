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
# run_basic_submission MODULE
# --------------------------------------------------
"""
Example: Run a basic submission with one test case
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
from online_judge.core.worker import Worker
from online_judge.models.submission import Submission
from online_judge.models.test_case import JudgeTestCase


def main():
    # Sample user code
    code = """
x = input()
print(x[::-1])
"""
    # Single test case
    test_case = JudgeTestCase(
        input_data="hello",
        expected_output="olleh",
    )

    submission = Submission(
        code=code,
        language="python",
        problem_id="reverse_string",
        test_cases=[test_case],
        time_limit=2,
    )

    worker = Worker()
    results = worker.process(submission)

    for idx, result in enumerate(results):
        print(f"Test #{idx + 1}")
        print(f" Passed: {result.passed}")
        print(f" Output: {result.actual_output}")
        print(f" Expected: {result.expected_output}")
        print("-" * 30)


if __name__ == "__main__":
    main()
