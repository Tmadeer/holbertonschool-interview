# Holberton School — Interview Preparation Project

## Description

This repository contains solutions to common technical interview
questions, focusing on algorithms and data structures. Each task lives
in its own directory and is solved in Python 3.

The goal of this project is not just to produce a working solution,
but to reason clearly about time and space complexity, and to choose
the data structure or traversal strategy that best fits each problem.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files are interpreted on Ubuntu 14.04 LTS using `python3`
  (version 3.4.3)
- All files end with a new line
- The first line of every file is exactly `#!/usr/bin/python3`
- Code follows the `PEP 8` style guide (version 1.7.x)
- All files are executable
- A `README.md` file, at the root of the project, is mandatory

## How to Run

Each solution file is executable on its own:

```bash
chmod +x <task_directory>/<file>.py
./<task_directory>/<file>.py
```

A matching `main_*.py` test file is provided for each task to verify
the expected output.

## Tasks

### 0. Lockboxes

**Directory:** `lockboxes`
**File:** `0-lockboxes.py`

Given `n` locked boxes, numbered `0` to `n - 1`, where each box may
contain keys to other boxes, determine whether all boxes can be
unlocked, starting from box `0` (which is unlocked by default).

**Prototype:**

```python
def canUnlockAll(boxes)
```

- `boxes` is a list of lists; `boxes[i]` holds the keys found inside
  box `i`.
- A key with the same number as a box opens that box.
- Some keys may not correspond to any existing box.
- Returns `True` if every box can be opened, `False` otherwise.

**Approach:** The problem is modeled as a directed graph, where each
box is a node and each key is an edge to another box. A
depth-first search (DFS), implemented with an explicit stack, starts
from box `0` and marks every box reachable through the keys it finds
along the way. If every box ends up marked as unlocked, the function
returns `True`.

**Example:**

```bash
$ ./main_0.py
True
True
False
```

## Author

Tumadhir Hani Al-Fattah
