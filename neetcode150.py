#!/usr/bin/env python3
"""
Here is the read me file and program file of it and i hope this info of 
my task is helpful for you to run this

NeetCode 150 DSA Tracker

HOW TO RUN
----------
Always use this format:
   & c:\python314\python.exe "c:/Users/ADMIN/Desktop/New folder/neetcode150.py" [COMMAND]


COMMANDS
--------

Show all problems + stats:
   & c:\python314\python.exe "c:/Users/ADMIN/Desktop/New folder/neetcode150.py"

Mark problems as done/undone (USE THIS DAILY):
   & c:\python314\python.exe "c:/Users/ADMIN/Desktop/New folder/neetcode150.py" mark

Show only completed problems:
   & c:\python314\python.exe "c:/Users/ADMIN/Desktop/New folder/neetcode150.py" done

Show only pending problems:
   & c:\python314\python.exe "c:/Users/ADMIN/Desktop/New folder/neetcode150.py" todo

Filter by difficulty:
   & c:\python314\python.exe "c:/Users/ADMIN/Desktop/New folder/neetcode150.py" easy
   & c:\python314\python.exe "c:/Users/ADMIN/Desktop/New folder/neetcode150.py" medium
   & c:\python314\python.exe "c:/Users/ADMIN/Desktop/New folder/neetcode150.py" hard

Show progress stats only:
   & c:\python314\python.exe "c:/Users/ADMIN/Desktop/New folder/neetcode150.py" stats

Reset all progress:
   & c:\python314\python.exe "c:/Users/ADMIN/Desktop/New folder/neetcode150.py" reset



WHERE IS MY PROGRESS SAVED?
----------------------------
Automatically saved to:
   C:\Users\ADMIN\Desktop\New folder\neetcode150_progress.json

Do NOT delete this file — it stores all your checkmarks.
You can back it up by copying it somewhere safe.


COMMON ERROR FIX
----------------
Error: 'neetcode150.py' is not recognized...
Fix:   Always type the full command with c:\python314\python.exe in front.
       Never run it as just: neetcode150.py mark

================================================================"""

import json
import os
import sys

SAVE_FILE = "neetcode150_progress.json"

PROBLEMS = {
    "Arrays & Hashing": [
        ("Contains Duplicate", "easy"),
        ("Valid Anagram", "easy"),
        ("Two Sum", "easy"),
        ("Group Anagrams", "medium"),
        ("Top K Frequent Elements", "medium"),
        ("Encode and Decode Strings", "medium"),
        ("Product of Array Except Self", "medium"),
        ("Valid Sudoku", "medium"),
        ("Longest Consecutive Sequence", "medium"),
    ],
    "Two Pointers": [
        ("Valid Palindrome", "easy"),
        ("Two Sum II", "medium"),
        ("3Sum", "medium"),
        ("Container With Most Water", "medium"),
        ("Trapping Rain Water", "hard"),
    ],
    "Sliding Window": [
        ("Best Time to Buy and Sell Stock", "easy"),
        ("Longest Substring Without Repeating Characters", "medium"),
        ("Longest Repeating Character Replacement", "medium"),
        ("Permutation in String", "medium"),
        ("Minimum Window Substring", "hard"),
        ("Sliding Window Maximum", "hard"),
    ],
    "Stack": [
        ("Valid Parentheses", "easy"),
        ("Min Stack", "medium"),
        ("Evaluate Reverse Polish Notation", "medium"),
        ("Generate Parentheses", "medium"),
        ("Daily Temperatures", "medium"),
        ("Car Fleet", "medium"),
        ("Largest Rectangle in Histogram", "hard"),
    ],
    "Binary Search": [
        ("Binary Search", "easy"),
        ("Search a 2D Matrix", "medium"),
        ("Koko Eating Bananas", "medium"),
        ("Find Minimum in Rotated Sorted Array", "medium"),
        ("Search in Rotated Sorted Array", "medium"),
        ("Time Based Key-Value Store", "medium"),
        ("Median of Two Sorted Arrays", "hard"),
    ],
    "Linked List": [
        ("Reverse Linked List", "easy"),
        ("Merge Two Sorted Lists", "easy"),
        ("Linked List Cycle", "easy"),
        ("Reorder List", "medium"),
        ("Remove Nth Node From End of List", "medium"),
        ("Copy List with Random Pointer", "medium"),
        ("Add Two Numbers", "medium"),
        ("Find the Duplicate Number", "medium"),
        ("LRU Cache", "medium"),
        ("Merge K Sorted Lists", "hard"),
        ("Reverse Nodes in K-Group", "hard"),
    ],
    "Trees": [
        ("Invert Binary Tree", "easy"),
        ("Maximum Depth of Binary Tree", "easy"),
        ("Diameter of Binary Tree", "easy"),
        ("Balanced Binary Tree", "easy"),
        ("Same Tree", "easy"),
        ("Subtree of Another Tree", "easy"),
        ("Lowest Common Ancestor of BST", "medium"),
        ("Binary Tree Level Order Traversal", "medium"),
        ("Binary Tree Right Side View", "medium"),
        ("Count Good Nodes in Binary Tree", "medium"),
        ("Validate Binary Search Tree", "medium"),
        ("Kth Smallest Element in BST", "medium"),
        ("Construct Binary Tree from Preorder and Inorder", "medium"),
        ("Binary Tree Maximum Path Sum", "hard"),
        ("Serialize and Deserialize Binary Tree", "hard"),
    ],
    "Heap / Priority Queue": [
        ("Kth Largest Element in a Stream", "easy"),
        ("Last Stone Weight", "easy"),
        ("K Closest Points to Origin", "medium"),
        ("Kth Largest Element in an Array", "medium"),
        ("Task Scheduler", "medium"),
        ("Design Twitter", "medium"),
        ("Find Median from Data Stream", "hard"),
    ],
    "Backtracking": [
        ("Subsets", "medium"),
        ("Combination Sum", "medium"),
        ("Permutations", "medium"),
        ("Subsets II", "medium"),
        ("Combination Sum II", "medium"),
        ("Word Search", "medium"),
        ("Palindrome Partitioning", "medium"),
        ("Letter Combinations of a Phone Number", "medium"),
        ("N-Queens", "hard"),
    ],
    "Graphs": [
        ("Number of Islands", "medium"),
        ("Clone Graph", "medium"),
        ("Max Area of Island", "medium"),
        ("Pacific Atlantic Water Flow", "medium"),
        ("Surrounded Regions", "medium"),
        ("Rotting Oranges", "medium"),
        ("Walls and Gates", "medium"),
        ("Course Schedule", "medium"),
        ("Course Schedule II", "medium"),
        ("Redundant Connection", "medium"),
        ("Number of Connected Components in Undirected Graph", "medium"),
        ("Graph Valid Tree", "medium"),
        ("Word Ladder", "hard"),
    ],
    "Advanced Graphs": [
        ("Reconstruct Itinerary", "hard"),
        ("Min Cost to Connect All Points", "medium"),
        ("Network Delay Time", "medium"),
        ("Swim in Rising Water", "hard"),
        ("Alien Dictionary", "hard"),
        ("Cheapest Flights Within K Stops", "medium"),
    ],
    "1D Dynamic Programming": [
        ("Climbing Stairs", "easy"),
        ("Min Cost Climbing Stairs", "easy"),
        ("House Robber", "medium"),
        ("House Robber II", "medium"),
        ("Longest Palindromic Substring", "medium"),
        ("Palindromic Substrings", "medium"),
        ("Decode Ways", "medium"),
        ("Coin Change", "medium"),
        ("Maximum Product Subarray", "medium"),
        ("Word Break", "medium"),
        ("Longest Increasing Subsequence", "medium"),
        ("Partition Equal Subset Sum", "medium"),
    ],
    "2D Dynamic Programming": [
        ("Unique Paths", "medium"),
        ("Longest Common Subsequence", "medium"),
        ("Best Time to Buy and Sell Stock with Cooldown", "medium"),
        ("Coin Change II", "medium"),
        ("Target Sum", "medium"),
        ("Interleaving String", "medium"),
        ("Longest Increasing Path in Matrix", "hard"),
        ("Distinct Subsequences", "hard"),
        ("Edit Distance", "hard"),
        ("Burst Balloons", "hard"),
        ("Regular Expression Matching", "hard"),
    ],
    "Greedy": [
        ("Maximum Subarray", "medium"),
        ("Jump Game", "medium"),
        ("Jump Game II", "medium"),
        ("Gas Station", "medium"),
        ("Hand of Straights", "medium"),
        ("Merge Triplets to Form Target Triplet", "medium"),
        ("Partition Labels", "medium"),
        ("Valid Parenthesis String", "medium"),
    ],
    "Intervals": [
        ("Insert Interval", "medium"),
        ("Merge Intervals", "medium"),
        ("Non-Overlapping Intervals", "medium"),
        ("Meeting Rooms", "easy"),
        ("Meeting Rooms II", "medium"),
        ("Minimum Interval to Include Each Query", "hard"),
    ],
    "Math & Geometry": [
        ("Rotate Image", "medium"),
        ("Spiral Matrix", "medium"),
        ("Set Matrix Zeroes", "medium"),
        ("Happy Number", "easy"),
        ("Plus One", "easy"),
        ("Pow(x, n)", "medium"),
        ("Multiply Strings", "medium"),
        ("Detect Squares", "medium"),
    ],
    "Bit Manipulation": [
        ("Single Number", "easy"),
        ("Number of 1 Bits", "easy"),
        ("Counting Bits", "easy"),
        ("Reverse Bits", "easy"),
        ("Missing Number", "easy"),
        ("Sum of Two Integers", "medium"),
        ("Reverse Integer", "medium"),
    ],
    "Trie": [
        ("Implement Trie (Prefix Tree)", "medium"),
        ("Design Add and Search Words Data Structure", "medium"),
        ("Word Search II", "hard"),
    ],
}

# ── ANSI colours ─────────────────────────────────────────────────────────────
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
RESET  = "\033[0m"
CHECK  = "✓"
CROSS  = "○"

DIFF_COLOR = {"easy": GREEN, "medium": YELLOW, "hard": RED}


def load_progress():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE) as f:
            return json.load(f)
    return {}


def save_progress(progress):
    with open(SAVE_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def problem_id(pattern, name):
    return f"{pattern}::{name}"


def print_bar(done, total, width=30):
    filled = int(width * done / total) if total else 0
    bar = "█" * filled + "░" * (width - filled)
    pct = int(100 * done / total) if total else 0
    return f"[{bar}] {done}/{total} ({pct}%)"


def show_stats(progress):
    total = sum(len(v) for v in PROBLEMS.values())
    done_total = 0
    by_diff = {"easy": [0, 0], "medium": [0, 0], "hard": [0, 0]}

    for pattern, items in PROBLEMS.items():
        for name, diff in items:
            by_diff[diff][1] += 1
            if progress.get(problem_id(pattern, name)):
                done_total += 1
                by_diff[diff][0] += 1

    print(f"\n{BOLD}── Overall Progress ──────────────────────────────{RESET}")
    print(f"  {print_bar(done_total, total)}")

    print(f"\n{BOLD}── By Difficulty ─────────────────────────────────{RESET}")
    for diff, (d, t) in by_diff.items():
        color = DIFF_COLOR[diff]
        print(f"  {color}{diff:<8}{RESET}  {print_bar(d, t, 20)}")

    print(f"\n{BOLD}── By Pattern ────────────────────────────────────{RESET}")
    for pattern, items in PROBLEMS.items():
        done_p = sum(1 for name, _ in items if progress.get(problem_id(pattern, name)))
        total_p = len(items)
        bar_p = "█" * int(20 * done_p / total_p) + "░" * (20 - int(20 * done_p / total_p))
        status = f"{GREEN}✓{RESET}" if done_p == total_p else f"{DIM}○{RESET}"
        print(f"  {status} {pattern:<40} [{bar_p}] {done_p}/{total_p}")
    print()


def list_problems(progress, diff_filter=None, status_filter=None):
    for pattern, items in PROBLEMS.items():
        filtered = [
            (name, diff) for name, diff in items
            if (diff_filter is None or diff == diff_filter)
            and (status_filter is None
                 or (status_filter == "done" and progress.get(problem_id(pattern, name)))
                 or (status_filter == "todo" and not progress.get(problem_id(pattern, name))))
        ]
        if not filtered:
            continue

        done_p = sum(1 for name, _ in items if progress.get(problem_id(pattern, name)))
        print(f"\n{BOLD}{CYAN}{pattern}{RESET} {DIM}({done_p}/{len(items)}){RESET}")

        for name, diff in filtered:
            pid = problem_id(pattern, name)
            color = DIFF_COLOR[diff]
            tick = f"{GREEN}{CHECK}{RESET}" if progress.get(pid) else f"{DIM}{CROSS}{RESET}"
            name_str = f"{DIM}{name}{RESET}" if progress.get(pid) else name
            print(f"  {tick}  {name_str:<55} {color}{diff}{RESET}")
    print()


def mark_done(progress):
    """Interactive mode: type problem name (partial match) to toggle."""
    flat = [
        (problem_id(p, name), name, diff, p)
        for p, items in PROBLEMS.items()
        for name, diff in items
    ]
    print(f"\n{BOLD}Mark problems as done / undone{RESET}")
    print(f"{DIM}Type part of a problem name. Leave blank to quit.{RESET}\n")

    while True:
        query = input("Problem name (or blank to quit): ").strip().lower()
        if not query:
            break

        matches = [(pid, name, diff, pat) for pid, name, diff, pat in flat
                   if query in name.lower()]

        if not matches:
            print(f"  {RED}No matches found.{RESET}")
            continue

        if len(matches) == 1:
            pid, name, diff, pat = matches[0]
        else:
            print(f"  Multiple matches:")
            for i, (pid, name, diff, pat) in enumerate(matches):
                status = f"{GREEN}done{RESET}" if progress.get(pid) else "todo"
                print(f"    [{i+1}] {name} ({pat}) — {status}")
            try:
                idx = int(input("  Pick number: ")) - 1
                pid, name, diff, pat = matches[idx]
            except (ValueError, IndexError):
                print(f"  {RED}Invalid choice.{RESET}")
                continue

        if progress.get(pid):
            del progress[pid]
            print(f"  {DIM}Unmarked:{RESET} {name}")
        else:
            progress[pid] = True
            print(f"  {GREEN}Marked done:{RESET} {name}")

        save_progress(progress)


def main():
    progress = load_progress()
    args = [a.lower() for a in sys.argv[1:]]

    if not args:
        list_problems(progress)
        show_stats(progress)
        print(f"{DIM}Run with 'mark' to toggle problems, or filter with: easy / medium / hard / done / todo / stats / reset{RESET}\n")
        return

    cmd = args[0]

    if cmd == "stats":
        show_stats(progress)

    elif cmd in ("easy", "medium", "hard"):
        list_problems(progress, diff_filter=cmd)

    elif cmd in ("done", "todo"):
        list_problems(progress, status_filter=cmd)

    elif cmd == "mark":
        mark_done(progress)

    elif cmd == "reset":
        confirm = input("Reset ALL progress? This cannot be undone. Type 'yes' to confirm: ")
        if confirm.strip().lower() == "yes":
            save_progress({})
            print(f"{GREEN}Progress reset.{RESET}")
        else:
            print("Cancelled.")

    else:
        print(__doc__)


if __name__ == "__main__":
    main()