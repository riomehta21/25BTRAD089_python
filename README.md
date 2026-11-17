# 25BTRAD089 — Python Programming & Experiential Learning Portfolio

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite%20%7C%20PostgreSQL-003B57?logo=sqlite&logoColor=white)](https://sqlite.org/)
[![Optimization](https://img.shields.io/badge/Optimization-SciPy%20MILP-orange)](https://scipy.org/)
[![License](https://img.shields.io/badge/License-Academic%20Use-green)](#license)

This repository contains the complete academic coursework, laboratory experiments, problem-solving tasks, mini-projects, and an experiential learning capstone project for **Python Programming** by **Rio Mehta (25BTRAD089)**.

---

## 📑 Table of Contents

- [Repository Overview](#-repository-overview)
- [Directory Structure](#-directory-structure)
- [1. Lab Experiments](#1-lab-experiments)
- [2. Problem Solving & Mini Projects](#2-problem-solving--mini-projects)
  - [Problem Solving Tasks](#problem-solving-tasks)
  - [Mini Projects](#mini-projects)
- [3. Experiential Learning Project: SceneGraph AI](#3-experiential-learning-project-scenegraph-ai)
  - [Key Capabilities](#key-capabilities)
  - [Architecture](#architecture)
  - [Running SceneGraph AI](#running-scenegraph-ai)
- [Getting Started & Usage](#-getting-started--usage)
- [License & Academic Integrity](#-license--academic-integrity)

---

## 🌟 Repository Overview

The repository is organized into three major modules representing a progressive journey from foundational programming concepts to a production-grade full-stack web application:

1. **Lab Experiments (`Lab_Experiments/`)**: Structured laboratory exercises spanning core syntax, data structures, recursion, file handling (TXT, CSV, JSON), and Object-Oriented Programming (OOP).
2. **Problem Solving (`Problem_Solving/`)**: Hands-on programming challenges covering input/output formatting, type casting, arithmetic calculations, conditional statements, and three CLI mini-projects.
3. **Experiential Learning (`25BTRAD089_Exp Learning/`)**: **SceneGraph AI**, a full-stack production intelligence platform featuring screenplay parsing, knowledge graphs, continuity validation, and constraint-based scheduling optimization using SciPy MILP.

---

## 📂 Directory Structure

```text
25BTRAD089_python/
│
├── Lab_Experiments/                    # Structured Python Lab Exercises
│   ├── Lab_Exercise_02.py              # Hello World & Basic Output
│   ├── Lab_Exercise_03.py              # User Input & Type Conversion
│   ├── Lab_Exercise_04.py              # Simple Arithmetic Calculator
│   ├── Lab_Exercise_05.py              # Number Guessing Game (Loops & Random)
│   ├── Lab_Exercise_06.py              # Prime Number Checker
│   ├── Lab_Exercise_07.py              # Fibonacci Sequence (Recursion)
│   ├── Lab_Exercise_08.py              # Contact Management System
│   ├── Lab_Exercise_09.py              # Student Grade Evaluation System
│   ├── Lab_Exercise_10.py              # Word Frequency Counter
│   ├── Lab_Exercise_11.py              # Server Log Analyzer
│   ├── Lab_Exercise_12.py              # Student Records (JSON File I/O)
│   ├── Lab_Exercise_13.py              # Employee Database (CSV File I/O)
│   ├── Lab_Exercise_14.py              # Bank Account Class (OOP)
│   ├── Lab_Exercise_15.py              # Library Book Management (OOP)
│   └── Lab_Exercise_16.py              # Dice Rolling Simulator
│
├── Problem_Solving/                    # Progressive Coding Tasks & Mini-Projects
│   ├── Task_01.py to Task_18.py       # Core logic, formatting, casting & control flow
│   ├── Mini_Project01.py               # Supermarket Bill Generator
│   ├── Mini_Project02.py               # Student Report Card Generator
│   └── Mini_Project03.py               # Student Records Management CLI
│
├── 25BTRAD089_Exp Learning/            # Capstone Experiential Learning Project
│   └── SceneGraph_Production/          # SceneGraph AI Web Application
│       ├── app.py                      # FastAPI REST API Backend
│       ├── models.py                   # SQLAlchemy ORM Database Schemas
│       ├── project_service.py          # Business logic & repository services
│       ├── core/                       # Core algorithms (Parser, Scheduler, Graph)
│       │   ├── parser.py               # Fountain screenplay parser
│       │   ├── scheduler.py            # SciPy MILP production scheduling solver
│       │   ├── continuity.py           # Prop & continuity checker
│       │   ├── graph_engine.py         # Scene-character knowledge graph engine
│       │   └── constraints.py          # Solver constraint rules
│       ├── docs/                       # Static frontend assets (HTML/CSS/JS)
│       ├── tests/                      # Automated test suite (Pytest)
│       ├── requirements.txt            # Python dependencies
│       └── render.yaml                 # Cloud deployment configuration
│
├── .gitignore                          # Git ignore rules for Python, cache & secrets
└── README.md                           # Main documentation
```

---

## 1. Lab Experiments

| Experiment File | Title | Key Concepts & Topics Covered |
|:---|:---|:---|
| [`Lab_Exercise_02.py`](Lab_Experiments/Lab_Exercise_02.py) | Hello World & Output | Basic print statements, output streaming |
| [`Lab_Exercise_03.py`](Lab_Experiments/Lab_Exercise_03.py) | Input & Type Casting | `input()`, integer casting with `int()`, arithmetic operations |
| [`Lab_Exercise_04.py`](Lab_Experiments/Lab_Exercise_04.py) | Simple Calculator | Arithmetic operations (`+`, `-`, `*`, `/`), `math` module |
| [`Lab_Exercise_05.py`](Lab_Experiments/Lab_Exercise_05.py) | Number Guessing Game | Random number generation (`random.randint`), `while` loops |
| [`Lab_Exercise_06.py`](Lab_Experiments/Lab_Exercise_06.py) | Prime Number Checker | Conditional logic, loop termination, mathematical primality |
| [`Lab_Exercise_07.py`](Lab_Experiments/Lab_Exercise_07.py) | Fibonacci Generator | Recursion, base cases, algorithmic problem solving |
| [`Lab_Exercise_08.py`](Lab_Experiments/Lab_Exercise_08.py) | Contact Book | Dynamic list of dictionaries, search, add, view operations |
| [`Lab_Exercise_09.py`](Lab_Experiments/Lab_Exercise_09.py) | Grade Evaluator | Conditional grading criteria, dictionary records, data validation |
| [`Lab_Exercise_10.py`](Lab_Experiments/Lab_Exercise_10.py) | Word Frequency Counter | String normalization (`lower()`, `split()`), dictionary mapping |
| [`Lab_Exercise_11.py`](Lab_Experiments/Lab_Exercise_11.py) | Server Log Analyzer | File handling (`open()`, `readlines()`), `collections.Counter` |
| [`Lab_Exercise_12.py`](Lab_Experiments/Lab_Exercise_12.py) | JSON Student Records | Structured file serialization & deserialization with `json` module |
| [`Lab_Exercise_13.py`](Lab_Experiments/Lab_Exercise_13.py) | CSV Employee Manager | Tabular file handling with `csv.reader` and `csv.writer` |
| [`Lab_Exercise_14.py`](Lab_Experiments/Lab_Exercise_14.py) | Bank Account (OOP) | Classes, objects, constructor `__init__`, encapsulation, methods |
| [`Lab_Exercise_15.py`](Lab_Experiments/Lab_Exercise_15.py) | Library Book Manager (OOP) | Object state tracking, status toggling, availability validation |
| [`Lab_Exercise_16.py`](Lab_Experiments/Lab_Exercise_16.py) | Dice Rolling Simulator | Randomization, loop control, user prompts |

---

## 2. Problem Solving & Mini Projects

### Problem Solving Tasks

| Task File | Description | Core Concept |
|:---|:---|:---|
| [`Task_01.py`](Problem_Solving/Task_01.py) | Personal Profile Display | Standard console output |
| [`Task_02.py`](Problem_Solving/Task_02.py) | Star Pattern Printing | Block pattern formatting |
| [`Task_03.py`](Problem_Solving/Task_03.py) | Basic Message Output | Simple print execution |
| [`Task_04.py`](Problem_Solving/Task_04.py) | Number Triangle Pattern | Sequential number patterns |
| [`Task_05.py`](Problem_Solving/Task_05.py) | Multi-line String Output | Escape sequence `\n` |
| [`Task_06.py`](Problem_Solving/Task_06.py) | Tabular Column Output | Escape sequence `\t` |
| [`Task_07.py`](Problem_Solving/Task_07.py) | Single-Line Commenting | Documentation using `#` |
| [`Task_08.py`](Problem_Solving/Task_08.py) | Multi-Line Commenting | Triple quotes `"""` documentation |
| [`Task_09.py`](Problem_Solving/Task_09.py) | Sequential Inline Comments | Step-by-step code commentary |
| [`Task_10.py`](Problem_Solving/Task_10.py) | String Variable Declaration | Variable initialization & assignment |
| [`Task_11.py`](Problem_Solving/Task_11.py) | Multi-Variable Assignment | Handling multiple variable declarations |
| [`Task_12.py`](Problem_Solving/Task_12.py) | String to Integer Conversion | Type casting with `int()`, inspection with `type()` |
| [`Task_13.py`](Problem_Solving/Task_13.py) | Integer to Float Conversion | Type casting with `float()`, inspection with `type()` |
| [`Task_14.py`](Problem_Solving/Task_14.py) | Interactive Age Reader | Dynamic user prompts with `input()` |
| [`Task_15.py`](Problem_Solving/Task_15.py) | Addition Calculator | Numeric inputs addition & output |
| [`Task_16.py`](Problem_Solving/Task_16.py) | Formatted Profile String | String interpolation using f-strings |
| [`Task_17.py`](Problem_Solving/Task_17.py) | Temperature Converter | Formula execution ($^{\circ}\text{C} \to {^\circ}\text{F}$) |
| [`Task_18.py`](Problem_Solving/Task_18.py) | Number Parity Checker | Modulo operator `%` and `if/else` branching |

### Mini Projects

| Mini Project | Description | Features |
|:---|:---|:---|
| **[`Mini_Project01.py`](Problem_Solving/Mini_Project01.py)** | **Supermarket Bill Generator** | Interactive product selection from store menu, cart accumulator, itemized receipt display, and total amount calculation. |
| **[`Mini_Project02.py`](Problem_Solving/Mini_Project02.py)** | **Student Performance Card** | Multi-subject marks input, aggregate sum, percentage calculation, and automated grade assignment (A, B, C, Fail). |
| **[`Mini_Project03.py`](Problem_Solving/Mini_Project03.py)** | **Student Management System** | Menu-driven interactive terminal interface to Add, View, and Search student records with input validation and duplicate prevention. |

---

## 3. Experiential Learning Project: SceneGraph AI

Located in [`25BTRAD089_Exp Learning/SceneGraph_Production/`](25BTRAD089_Exp%20Learning/SceneGraph_Production/), **SceneGraph AI** is a production-grade full-stack platform designed for film pre-production, screenplay analysis, continuity verification, and filming schedule optimization.

### Key Capabilities

- **Fountain Screenplay Parsing**: Parses `.fountain` and `.txt` scripts into structured scene records, extracting scene headers, time of day (INT/EXT, DAY/NIGHT), characters, locations, and dialogue.
- **Knowledge Graph Extraction**: Visualizes scene-character-location relationships and network topology.
- **Continuity Inconsistency Detection**: Traces props across scene chronologies in story order to detect annotated continuity mismatches.
- **MILP Production Scheduling**: Employs **SciPy MILP** (Mixed-Integer Linear Programming) optimization to build feasible, single-crew shooting schedules respecting actor availability, turnaround buffers, and location setups.
- **Full-Stack Architecture**: Built with **FastAPI** backend, **SQLAlchemy** database layer, session-based authentication, and a responsive cinematic vanilla **HTML5/CSS3/JavaScript** frontend.
- **Automated Testing Suite**: Full integration test coverage with `pytest` covering authentication, parser accuracy, graph generation, and scheduling solvers.

### Architecture

```text
       Browser Frontend (docs/)
     [HTML5 / CSS3 / ES6 JavaScript]
                   │
         REST API  │  Bearer Token
                   ▼
         FastAPI Backend (app.py)
   ┌───────────────────────────────┐
   │ • Screenplay Parser           │
   │ • Scene Knowledge Graph       │
   │ • Continuity Validator        │
   │ • SciPy MILP Scheduler        │
   └───────────────┬───────────────┘
                   │ SQLAlchemy ORM
                   ▼
     Relational Database (SQLite / PostgreSQL)
     [Users, Scenes, Cast, Schedules, Audit]
```

### Running SceneGraph AI

1. Navigate to the project directory:
   ```bash
   cd "25BTRAD089_Exp Learning/SceneGraph_Production"
   ```
2. Set up virtual environment and install dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate    # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Start the application:
   ```bash
   python3 start.py
   # Or directly:
   uvicorn app:app --reload --port 8000
   ```
4. Open `http://localhost:8000` in your browser.

---

## 🚀 Getting Started & Usage

### Prerequisites
- Python 3.10 or higher
- `git` version control

### Running Any Individual Lab Experiment or Task
Clone the repository:
```bash
git clone https://github.com/riomehta21/25BTRAD089_python.git
cd 25BTRAD089_python
```

Run any script directly using the Python interpreter:
```bash
# Example: Run Lab Experiment 04
python3 Lab_Experiments/Lab_Exercise_04.py

# Example: Run Mini Project 01
python3 Problem_Solving/Mini_Project01.py

# Example: Run Problem Solving Task 17
python3 Problem_Solving/Task_17.py
```

---

## 📜 License & Academic Integrity

This repository is maintained for academic coursework and portfolio assessment for **25BTRAD089**. Code is provided for educational, demonstration, and evaluation purposes.
