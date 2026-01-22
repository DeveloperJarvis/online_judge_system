@echo off

REM Root directory
@REM set ROOT=online_judge_system
set ROOT=.

REM Create directories if they do not exist
call :create_folder "%ROOT%"
call :create_folder "%ROOT%\config"
call :create_folder "%ROOT%\docs"
call :create_folder "%ROOT%\examples"
call :create_folder "%ROOT%\logs"
call :create_folder "%ROOT%\online_judge"
call :create_folder "%ROOT%\tests"
call :create_folder "%ROOT%\online_judge\core"
call :create_folder "%ROOT%\online_judge\exceptions"
call :create_folder "%ROOT%\online_judge\models"
call :create_folder "%ROOT%\online_judge\storage"
call :create_folder "%ROOT%\online_judge\utils"

REM Create files only if they do not exist
REM Python source files (with header)
call :create_py_file "%ROOT%\main.py"
call :create_py_file "%ROOT%\setup.py"

call :create_py_file "%ROOT%\config\__init__.py"
call :create_py_file "%ROOT%\config\config.py"

call :create_py_file "%ROOT%\examples\run_basic_submission.py"
call :create_py_file "%ROOT%\examples\run_multiple_tests.py"

call :create_py_file "%ROOT%\online_judge\__init__.py"
call :create_py_file "%ROOT%\online_judge\core\__init__.py"
call :create_py_file "%ROOT%\online_judge\core\compiler.py"
call :create_py_file "%ROOT%\online_judge\core\evaluator.py"
call :create_py_file "%ROOT%\online_judge\core\sandbox_executor.py"
call :create_py_file "%ROOT%\online_judge\core\test_runner.py"
call :create_py_file "%ROOT%\online_judge\core\worker.py"
call :create_py_file "%ROOT%\online_judge\exceptions\__init__.py"
call :create_py_file "%ROOT%\online_judge\exceptions\execution_errors.py"
call :create_py_file "%ROOT%\online_judge\exceptions\sandbox_errors.py"
call :create_py_file "%ROOT%\online_judge\models\__init__.py"
call :create_py_file "%ROOT%\online_judge\models\execution_result.py"
call :create_py_file "%ROOT%\online_judge\models\submission.py"
call :create_py_file "%ROOT%\online_judge\models\test_case.py"
call :create_py_file "%ROOT%\online_judge\storage\__init__.py"
call :create_py_file "%ROOT%\online_judge\storage\submissions.py"
call :create_py_file "%ROOT%\online_judge\storage\results_db.py"
call :create_py_file "%ROOT%\online_judge\utils\__init__.py"
call :create_py_file "%ROOT%\online_judge\utils\file_ops.py"
call :create_py_file "%ROOT%\online_judge\utils\logging.py"
call :create_py_file "%ROOT%\online_judge\utils\security.py"

call :create_py_file "%ROOT%\tests\__init__.py"
call :create_py_file "%ROOT%\tests\test_compiler.py"
call :create_py_file "%ROOT%\tests\test_evaluator.py"
call :create_py_file "%ROOT%\tests\test_test_runner.py"
call :create_py_file "%ROOT%\tests\test_sandbox_executor.py"

REM Non-Python files (empty)
call :create_file "%ROOT%\logs\online_judge.log"

call :create_file "%ROOT%\requirements.txt"
call :create_file "%ROOT%\README.md"
call :create_file "%ROOT%\LICENSE"

echo Folder structure created (existing files and folders were preserved).
goto :eof

REM -------------------------------------------
REM Create folders if does not exist
REM -------------------------------------------

:create_folder
if not exist "%~1" (
    mkdir "%~1"
)

REM -------------------------------------------
REM Create empty file if it does not exist
REM -------------------------------------------

:create_file
if not exist "%~1" (
    type nul > "%~1"
)

exit /b

REM -------------------------------------------
REM Create python file with GPL header
REM -------------------------------------------
:create_py_file
if exist "%~1" exit /b

set FILEPATH=%~1
set FILENAME=%~n1

(
echo # --------------------------------------------------
echo # -*- Python -*- Compatibility Header
echo #
echo # Copyright ^(C^) 2023 Developer Jarvis ^(Pen Name^)
echo #
echo # This file is part of the Online Judge System Library. This library is free
echo # software; you can redistribute it and/or modify it under the
echo # terms of the GNU General Public License as published by the
echo # Free Software Foundation; either version 3, or ^(at your option^)
echo # any later version.
echo #
echo # This program is distributed in the hope that it will be useful,
echo # but WITHOUT ANY WARRANTY; without even the implied warranty of
echo # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
echo # GNU General Public License for more details.
echo #
echo # You should have received a copy of the GNU General Public License
echo # along with this program. If not, see ^<https://www.gnu.org/licenses/^>.
echo #
echo # SPDX-License-Identifier: GPL-3.0-or-later
echo #
echo # Online Judge System - Run user-submitted code safely with test cases
echo #                   Skills: sandboxing, subprocess, security
echo #
echo # Author: Developer Jarvis ^(Pen Name^)
echo # Contact: https://github.com/DeveloperJarvis
echo #
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # %FILENAME%% MODULE
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # imports
echo # --------------------------------------------------
echo.
) > "%FILEPATH%"

exit /b