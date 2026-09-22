# Clock-Out Git Push Protocol

Whenever Soggy indicates they are clocking out, finishing their study session, or wrapping up:

1. **Mandatory Git Push Reminder**:
   - ALWAYS remind Soggy explicitly to stage, commit, and push their changes via Git Bash before closing down.
   - Show the quick terminal command sequence customized to their current branch:
     ```bash
     git status
     git add .
     git commit -m "Day 12: <brief description of progress>"
     git push origin Python_projects
     ```
2. **Never Skip**:
   - This reminder must be part of every clock-out / session wrap-up message without exception.
