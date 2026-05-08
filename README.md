================================================================
  NEETCODE 150 — DSA Progress Tracker
  A command-line tool to track your LeetCode prep
================================================================

GitHub Repo  :  https://github.com/venkatnakka626/neetcode150-tracker
Live Demo    :  https://github.com/venkatnakka626/neetcode150-tracker#demo

----------------------------------------------------------------
WHAT THIS PROJECT DOES
----------------------------------------------------------------
A Python CLI tool that tracks your progress through all 150
problems in the NeetCode 150 list — the most popular curated
DSA problem set for software engineering interviews.

  - Tracks 150 problems across 18 patterns
  - Mark problems done/undone interactively
  - Visual progress bar for overall + per-pattern + per-difficulty
  - Filters: easy / medium / hard / done / todo
  - Progress auto-saved to a local JSON file
  - Zero dependencies — pure Python standard library

----------------------------------------------------------------
TECH STACK
----------------------------------------------------------------
Language     :  Python 3.x
Storage      :  JSON (local file)
Dependencies :  None (uses only json, os, sys)

----------------------------------------------------------------
PROBLEMS COVERED (150 total)
----------------------------------------------------------------
  Arrays & Hashing         —   9 problems
  Two Pointers             —   5 problems
  Sliding Window           —   6 problems
  Stack                    —   7 problems
  Binary Search            —   7 problems
  Linked List              —  11 problems
  Trees                    —  15 problems
  Heap / Priority Queue    —   7 problems
  Backtracking             —   9 problems
  Graphs                   —  13 problems
  Advanced Graphs          —   6 problems
  1D Dynamic Programming   —  12 problems
  2D Dynamic Programming   —  11 problems
  Greedy                   —   8 problems
  Intervals                —   6 problems
  Math & Geometry          —   8 problems
  Bit Manipulation         —   7 problems
  Trie                     —   3 problems

----------------------------------------------------------------
HOW TO RUN
----------------------------------------------------------------
Step 1 — Make sure Python is installed:
  python --version

Step 2 — Download the file:
  neetcode150.py

Step 3 — Run it:

  Show all problems + stats:
    python neetcode150.py

  Mark a problem done/undone (use this daily):
    python neetcode150.py mark

  Show only completed problems:
    python neetcode150.py done

  Show only pending problems:
    python neetcode150.py todo

  Filter by difficulty:
    python neetcode150.py easy
    python neetcode150.py medium
    python neetcode150.py hard

  Show progress stats only:
    python neetcode150.py stats

  Reset all progress:
    python neetcode150.py reset

----------------------------------------------------------------
WHERE IS MY PROGRESS SAVED?
----------------------------------------------------------------
Automatically saved to the same folder as the script:
  neetcode150_progress.json

Do NOT delete this file — it stores all your checkmarks.
Back it up by copying it somewhere safe or pushing it to GitHub.

----------------------------------------------------------------
WINDOWS NOTE
----------------------------------------------------------------
If "python" does not work, use the full path:
  & c:\python314\python.exe neetcode150.py mark

----------------------------------------------------------------
AUTHOR
----------------------------------------------------------------
Name     :  Venkat
College  :  IIIT (B.Tech CSE, 3rd Year)
Goal     :  Placement prep — SDE / Frontend / Full-Stack roles
GitHub   :  https://github.com/venkat626

================================================================