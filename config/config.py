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
# config MODULE
# --------------------------------------------------
"""
Configuration module for Online Judge System
"""
# --------------------------------------------------
# imports
# --------------------------------------------------
import os
from dataclasses import dataclass


# Paths
PARENT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
LOG_DIR = os.path.join(PARENT_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "online_judge.log")
SUBMISSION_DIR = os.path.join(PARENT_DIR, "submissions")
RESULTS_DIR = os.path.join(PARENT_DIR, "results")

# Ensure directories exist
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(SUBMISSION_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)


# --------------------------------------------------
# OJ config
# --------------------------------------------------
@dataclass(frozen=True)
class OJConfig:
    """
    Online Judge System configuration object.
    """
    max_execution_time: int = 3     # seconds per submission
    max_memory_mb: int = 64         # per submission
    languages_supported: tuple = ("python", "c", "cpp", "java")
    log_file: str = LOG_FILE
    submission_dir: str = SUBMISSION_DIR
    results_dir: str = RESULTS_DIR
