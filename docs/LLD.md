# 🧠 Online Judge System — Low-Level Design (LLD)

## 1. System Overview

An **Online Judge System** allows users to:

1. Submit source code in a supported language
2. Compile (if required)
3. Execute the program in a **sandboxed environment**
4. Run it against **hidden and public test cases**
5. Capture output, runtime, memory usage
6. Return verdicts securely

### Key Constraints

- **Untrusted user code**
- **Resource isolation**
- **Deterministic execution**
- **High concurrency**
- **Strong security guarantees**

---

## 2. High-Level Architecture

```
Client (Web/UI/API)
        |
        v
Submission Service
        |
        v
Job Queue  ---> Worker Pool
        |
        v
Sandbox Executor
        |
        v
Result Evaluator
        |
        v
Verdict Store
```

---

## 3. Core Components (LLD)

---

## 3.1 Submission Service

### Responsibilities

- Accept code submissions
- Validate metadata
- Store source code
- Enqueue execution job

### Data Model

**Submission**

- submission_id
- user_id
- problem_id
- language
- source_code
- timestamp
- status (PENDING / RUNNING / DONE)

### Security

- Input size limits
- Language whitelist
- Encoding validation
- Rate limiting per user

---

## 3.2 Job Queue

### Purpose

- Decouple submission from execution
- Control system load

### Characteristics

- FIFO or priority-based
- At-least-once execution
- Job timeout enforcement

### Job Payload

- submission_id
- language
- test_case_ids
- execution_limits

---

## 3.3 Worker Pool

### Role

- Execute jobs in isolation
- Horizontally scalable

### Worker States

- IDLE
- RUNNING
- TERMINATED
- QUARANTINED (security breach)

### Concurrency Model

- One job per worker
- No shared memory between jobs
- OS-level isolation

---

## 3.4 Sandbox Executor (Critical Component)

### Goal

Run **untrusted code safely**

---

### 3.4.1 Sandboxing Strategy

| Layer      | Mechanism           |
| ---------- | ------------------- |
| Process    | `subprocess`        |
| OS         | Linux namespaces    |
| CPU        | cgroups             |
| Memory     | cgroups             |
| Filesystem | chroot / overlay FS |
| Network    | Disabled            |
| Syscalls   | seccomp             |
| Time       | wall + CPU limits   |

---

### 3.4.2 Execution Lifecycle

1. Create sandbox environment
2. Copy user code (read-only)
3. Mount input files
4. Disable network
5. Apply resource limits
6. Run program
7. Capture stdout/stderr
8. Kill process if limits exceeded
9. Cleanup sandbox

---

### 3.4.3 Resource Limits

| Resource         | Enforcement |
| ---------------- | ----------- |
| CPU Time         | OS signals  |
| Wall Time        | Watchdog    |
| Memory           | cgroups     |
| Disk             | Quota       |
| Processes        | ulimit      |
| File descriptors | ulimit      |

---

## 3.5 Language Runtime Manager

### Responsibility

Language-specific setup

### Examples

- Python: interpreter + virtualenv
- C++: compile then execute binary
- Java: JVM memory caps

### Interface

- prepare()
- compile()
- execute()

---

## 3.6 Test Case Manager

### Test Case Types

- Public
- Private
- Sample

### Data Stored

- input.txt
- expected_output.txt
- time_limit
- memory_limit
- score_weight

### Security

- Immutable
- Read-only mounts
- Encrypted at rest

---

## 3.7 Result Evaluator

### Responsibilities

- Compare output
- Trim whitespace
- Normalize line endings
- Floating-point tolerance
- Partial scoring

### Verdicts

- Accepted (AC)
- Wrong Answer (WA)
- Time Limit Exceeded (TLE)
- Memory Limit Exceeded (MLE)
- Runtime Error (RE)
- Compilation Error (CE)
- Security Violation (SV)

---

## 3.8 Verdict Store

### Stores

- Verdict
- Execution time
- Memory usage
- Output (limited)
- Logs (sanitized)

### Retention Policy

- Outputs truncated
- Logs rotated
- Source immutable

---

## 4. Security Design (Very Important)

---

### 4.1 Threat Model

| Threat             | Mitigation          |
| ------------------ | ------------------- |
| Infinite loops     | CPU limits          |
| Fork bombs         | process limits      |
| File access        | chroot              |
| Network calls      | namespace isolation |
| Kernel exploits    | seccomp             |
| Side-channel leaks | isolated workers    |
| Data exfiltration  | no network          |

---

### 4.2 Forbidden Operations

- Network access
- File system traversal
- Environment variable access
- Process spawning
- Kernel syscalls
- Signals outside sandbox

---

## 5. Failure Handling

### Execution Failures

- Kill process
- Capture reason
- Mark verdict

### Worker Failures

- Restart worker
- Requeue job

### Sandbox Breach

- Kill worker
- Alert security system
- Rotate sandbox image

---

## 6. Scaling Strategy

### Horizontal Scaling

- Stateless workers
- Shared queue
- Auto-scaling groups

### Load Control

- Submission rate limiting
- Priority queues (contests)
- Backpressure

---

## 7. Observability

### Metrics

- Jobs/sec
- Avg execution time
- Sandbox failures
- Resource violations

### Logging

- Submission lifecycle
- Sandbox logs
- Security events

### Alerts

- High TLE rate
- Worker crashes
- Sandbox escapes

---

## 8. Data Flow Summary

```
User → Submit → Queue → Worker
 → Sandbox → Execute → Evaluate
 → Verdict → User
```

---

## 9. Non-Goals (Explicit)

- No persistent user state inside sandbox
- No internet access
- No interactive problems (unless special mode)
- No cross-submission caching

---

## 10. Interview-Ready Talking Points

If asked:

> “How do you safely run user code?”

Answer:

> Multiple layers of isolation: subprocess → OS namespaces → cgroups → syscall filtering → resource limits → no network → read-only FS.

> “What’s your weakest point?”
> Kernel-level exploits; mitigated via minimal images, seccomp, and frequent rotation.

---

## 🏁 Summary

This LLD provides:

- **Strong sandbox isolation**
- **Deterministic execution**
- **Production-grade security**
- **Scalable worker model**
- **Clean responsibility separation**

This is **Google / Amazon / Meta system-design level** for an Online Judge.
