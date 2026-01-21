# Online Judge System

> **Run user-submitted code safely with test cases**
> Skills: sandboxing, subprocess management, security, multi-language execution

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Architecture](#architecture)
- [Security & Sandboxing](#security--sandboxing)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The **Online Judge System (OJS)** is a Python library that provides a safe, extensible environment to execute user-submitted code and validate it against test cases. It is designed with security and isolation in mind, allowing code execution without compromising the host system.

It is suitable for:

- Competitive programming platforms
- Coding interview platforms
- Educational tools for automated grading

---

## Features

- ✅ Multi-language support (Python, C/C++, Java, etc.) via compilation/execution abstraction
- ✅ Safe sandboxed execution using subprocesses
- ✅ Resource limits (time, memory, CPU) per submission
- ✅ Test case evaluation and output comparison
- ✅ Detailed execution reporting and logs
- ✅ Extensible architecture for storage or distributed execution

---

## Project Structure

```
online_judge/
│
├── online_judge/                  # Main package
│   ├── core/                      # Core execution & sandbox logic
│   ├── models/                    # Data structures (Submission, TestCase, ExecutionResult)
│   ├── utils/                     # Helpers: logging, security, file operations
│   ├── storage/                   # Optional persistence
│   └── exceptions/                # Custom exceptions
│
├── tests/                         # Unit tests
├── examples/                      # Example usage scripts
├── docs/                          # Documentation and architecture diagrams
├── README.md                       # Project overview
├── setup.py                        # Installation setup
└── LICENSE                         # GPL-3.0 license
```

---

## Installation

```bash
# Clone the repository
git clone https://github.com/DeveloperJarvis/online_judge.git
cd online_judge

# Create a virtual environment
python -m venv .env
source .env/bin/activate  # Linux/macOS
.env\Scripts\activate     # Windows

# Install the package
pip install -e .
```

---

## Usage

### Running a Basic Submission

```python
from online_judge.core.sandbox_executor import SandboxExecutor
from online_judge.models.submission import Submission
from online_judge.models.test_case import TestCase

# Prepare submission
submission = Submission(
    language="python",
    code='print(input()[::-1])'
)

# Prepare test cases
tests = [
    TestCase(input_data="hello", expected_output="olleh"),
    TestCase(input_data="world", expected_output="dlrow")
]

# Execute
executor = SandboxExecutor()
results = executor.run(submission, tests)

for idx, result in enumerate(results):
    print(f"Test #{idx+1}: {result.status}, Output: {result.output}")
```

---

## Architecture

1. **Core Execution (`core/`)**
   - Handles compilation, execution, and sandboxing of user code.

2. **Models (`models/`)**
   - Defines structured objects: `Submission`, `TestCase`, `ExecutionResult`.

3. **Utilities (`utils/`)**
   - Logging, file operations, and sandbox validation helpers.

4. **Storage (`storage/`)**
   - Optional persistence layer for submissions and results.

5. **Exceptions (`exceptions/`)**
   - Custom exceptions for execution errors, sandbox violations, or invalid submissions.

---

## Security & Sandboxing

The system is designed to **isolate user-submitted code**:

- Runs each submission in a **separate subprocess**.
- Limits **execution time** and **memory usage**.
- Validates inputs and restricts file system access.
- Extensible to use **Docker, seccomp, or chroot jails** for added security.

---

## Contributing

We welcome contributions!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m "Add my feature"`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

Please follow **PEP8** coding standards and add unit tests for new features.

---

## License

This project is licensed under **GNU General Public License v3.0 or later**.
See [LICENSE](LICENSE) for details.

---

This README provides **clear instructions, a professional overview, and aligns with the GPL license in your headers**.
