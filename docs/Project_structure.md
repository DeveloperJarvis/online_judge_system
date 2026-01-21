## **Project Structure**

```
online_judge/
│
├── README.md
├── setup.py
├── pyproject.toml
├── LICENSE
├── .gitignore
│
├── online_judge/                  # Main package
│   ├── __init__.py
│   │
│   ├── core/                      # Core execution & sandbox logic
│   │   ├── __init__.py
│   │   ├── sandbox_executor.py    # Run user code safely
│   │   ├── compiler.py            # Language compilation abstraction
│   │   ├── test_runner.py         # Run code against test cases
│   │   ├── evaluator.py           # Compare outputs (diff, float tolerance)
│   │   └── worker.py              # Job lifecycle manager
│   │
│   ├── models/                    # Data structures
│   │   ├── __init__.py
│   │   ├── execution_result.py    # ExecutionResult, ExecutionStatus, ExecutionLimits
│   │   ├── test_case.py           # Test case representation
│   │   └── submission.py          # User submission metadata
│   │
│   ├── utils/                     # Helpers
│   │   ├── __init__.py
│   │   ├── security.py            # Path checks, sandbox validations
│   │   ├── logging.py             # Logger for OJ events
│   │   └── file_ops.py            # Safe file read/write
│   │
│   ├── storage/                   # Optional persistence
│   │   ├── __init__.py
│   │   ├── submissions_db.py      # Store submissions metadata
│   │   └── results_db.py          # Store results
│   │
│   └── exceptions/                # Custom exceptions
│       ├── __init__.py
│       ├── execution_errors.py
│       └── sandbox_errors.py
│
├── tests/                         # Unit tests
│   ├── __init__.py
│   ├── test_sandbox_executor.py
│   ├── test_compiler.py
│   ├── test_test_runner.py
│   └── test_evaluator.py
│
├── examples/                      # Example scripts
│   ├── run_basic_submission.py
│   └── run_multiple_tests.py
│
└── docs/                          # Documentation
    ├── architecture.md
    ├── usage.md
    └── sandboxing.md
```

---

### **Key Design Decisions**

1. **`core/`**
   - Contains all critical logic for **sandboxing, compiling, executing, and evaluating code**.
   - Isolated to make security audits easier.

2. **`models/`**
   - Clean data objects for submissions, test cases, and execution results.

3. **`utils/`**
   - Shared helpers like logging, file operations, and security checks.
   - Keeps core logic minimal and testable.

4. **`storage/`**
   - Optional persistence (DB, files, in-memory).
   - Can later integrate SQLite, PostgreSQL, or Redis.

5. **`exceptions/`**
   - Strong exception hierarchy to separate **execution errors vs sandbox violations**.

6. **`tests/`**
   - Unit tests for each module.
   - Designed for `pytest`.

7. **`examples/`**
   - Quickstart scripts to demonstrate usage.

8. **`docs/`**
   - Architecture diagrams, sandbox design, and usage instructions.

---

### **Next Steps**

1. I can create a **skeleton code base** with all folders, `__init__.py`, and stub classes/functions ready to implement.
2. Then we can **implement a fully working `sandbox_executor`** with time/memory limits.
3. Optionally, integrate **Docker or Linux seccomp sandboxing**.
