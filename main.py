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
# main MODULE
# --------------------------------------------------
"""
CLI Entry point for Online Judge System
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import argparse
from online_judge.core.worker import Worker
from online_judge.models.submission import Submission
from online_judge.models.test_case import JudgeTestCase


def parse_args():
    parser = argparse.ArgumentParser(
        description="Online Judge System CLI",
    )
    parser.add_argument(
        "--language",
        type=str,
        default="python",
        help="Programming language of the submission",
    )
    parser.add_argument(
        "--file",
        type=str,
        required=True,
        help="Path to the code file to submit",
    )
    parser.add_argument(
        "--input",
        type=str,
        default=None,
        help="Input data for the program (optional)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=3,
        help="Execution timeout in seconds",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    # Read user-submitted code
    with open(args.file, "r", encoding="utf-8") as f:
        code = f.read()

    test_case = JudgeTestCase(
        input_data=args.input or "",
        expected_output=None    # Optional, for CLI run
    )

    submission = Submission(
        code=code,
        language=args.language,
        problem_id="cli",
        test_cases=[test_case],
        time_limit=args.timeout,
    )

    executor = Worker()
    results = executor.process(submission)

    for idx, result in enumerate(results):
        print(f"Test #{idx+1}")
        print(f" Passed: {result.passed}")
        print(f" Output: {result.actual_output}")
        print(f" Error: {result.error}")


if __name__ == "__main__":
    main()
