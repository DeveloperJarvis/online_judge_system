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
# setup MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from setuptools import setup, find_packages
from pathlib import Path


ROOT = Path(__file__).parent


setup(
    name="online-judge-system",
    version="0.1.0",
    description="Run user-submitted code safety with test cases",
    long_description=(ROOT / "README.md").read_text(
        encoding="utf-8"
    ),
    long_description_content_type="text/markdown",
    author="Developer Jarvis",
    author_email="developerjarvis@github.com",
    url="https://github.com/DeveloperJarvis/online_judge_system",
    license="GPL-3.0-or-later",
    packages=find_packages(
        exclude=["tests*", "examples*", "logs*"]
    ),
    python_requires=">=3.9",
    install_requires=[
        "typing-extensions>=4.0.0"
    ],
    extras_require={
        "dev": [
            "pytest",
            "black",
            "flake8",
            "mypy",
        ]
    },
    entry_points={
        "console_scripts": [
            "online-judge=main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later",
        "Operating System :: OS Independent",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries",
    ],
    include_package_data=True,
    zip_safe=False,
)
