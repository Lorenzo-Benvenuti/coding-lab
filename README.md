# Coding Laboratory

Welcome to my practice repository!

This workspace is a dedicated environment for solving algorithmic challenges, modelling small domains, and practising whichever engineering technique I am working on at the time, currently Test-Driven Development.  
Techniques and languages are both open ended. Java and Python are the ones in it today, each one in its own folder with its own build configuration.

The primary objective is to demonstrate clean code principles, robust software architecture, proper error handling and strict data boundaries, in whichever language the exercise is written.

---

## Repository Architecture

Each language folder is self-contained and independent. Inside it, raw algorithmic puzzles are kept apart from design exercises, and the test tree mirrors the source tree.

```
coding-lab/
├── java/                      Java 21, Maven, JUnit 5
│   ├── pom.xml
│   ├── code/tdd/
│   │   ├── src/main/<exercise>/     implementation + notes.md
│   │   ├── src/timed/               repetitions and simulations against the clock
│   │   ├── test/main/<exercise>/
│   │   └── test/timed/
│   └── dsa/leetcode/<problem>/
└── python/                    Python 3.12, pytest, ruff
    ├── pyproject.toml
    └── code/tdd/                    same shape
```

The `tdd` level names the practice rather than the content, so a different technique takes a sibling folder under `code/` instead of disturbing what is already there.

The workspace is organised around three pillars.

* **Drills and platform solutions** live under `dsa/` — isolated algorithmic problems and data structure implementations, kept as a record of what was solved on the platform.
* **Architectural katas** live under `code/tdd/src/main/` — design exercises with multi-method classes, domain modelling and the resolution of ambiguous business requirements.
* **Automated test suites** mirror the source packages — every implementation is locked down against regressions.

Every exercise folder carries a `notes.md` with the statement, the questions worth asking before writing anything, the decisions taken where the specification was silent, the ordered test list and the follow-ups an interviewer can add.

Source roots are declared explicitly, in `pom.xml` for Java and in `pyproject.toml` for Python, so both toolchains find the code where it actually lives.

---

## Technical Standards

Every solution added to this repository follows the same workflow:

1. **Requirement clarification** — Implicit edge cases, data boundaries and ambiguous specifications are identified and written down before any code exists.
2. **Test-driven development** — Tests come first and each one pins down a single decision.
3. **Performance consciousness** — Time and space complexity is stated for every solution, with data structures chosen accordingly.
4. **Production-ready code** — Fail fast on null, defensive boundaries, and locale-independent string processing.

---

## Getting Started

### Java

Requires JDK 21. Maven does not need to be installed, the wrapper handles it.

```bash
cd java
./mvnw test
```

### Python

Requires Python 3.12.

```bash
cd python
python -m venv venv
source venv/bin/activate       # Linux, macOS
venv\Scripts\activate          # Windows
pip install -r requirements.txt
pytest
ruff check .
```
