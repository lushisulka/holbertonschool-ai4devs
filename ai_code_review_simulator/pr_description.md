# Pull Request: Add Task Filtering Feature

## Summary
Implements a task filtering feature that allows filtering tasks by status and priority level.

## Changes
- Added `filter_tasks()` function in `tasks.py`
- Supports filtering by:
  - Task status (e.g., "todo", "done")
  - Maximum priority threshold
- Added simple test cases in main block

## Context
~120 LOC feature addition.
Improves usability for task management by allowing flexible filtering without modifying original task list.
Related issue: #42