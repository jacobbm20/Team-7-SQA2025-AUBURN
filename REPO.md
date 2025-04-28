# 4a. Create a Git Hook that will run and report all security weaknesses in the project in a CSV file whenever a Python file is changed and committed. (10%)

## Activities Performed

### Understanding the Purpose of the Script
- The pre-commit hook is a Git hook that runs automatically before a commit is finalized. It is used to enforce checks and validations on the code being committed.
- This specific script performs several checks, including:
  - Running security scans on Python files using Bandit.
  - Preventing non-ASCII filenames from being added to the repository.
  - Checking for trailing whitespace errors in staged files.

#### Initial Setup
- The script determines the reference point (HEAD or an empty tree object for the initial commit) to compare staged changes.
- It redirects output to stderr to ensure error messages are visible.

#### Python Security Checks
- The script searches for all Python files (`*.py`) in the `KubeSec-master` directory.
- If Python files are found, it runs Bandit to perform a security scan and outputs the results to `bandit_report.csv`.
- It uses `awk` to check if any issues with HIGH or CRITICAL severity are present in the Bandit report. If such issues are found, the commit is blocked.

### Testing the Script

| Scenario | Result |
|:---------|:-------|
| Committing Python files with HIGH or CRITICAL severity issues in Bandit | The commit was blocked with an appropriate error message |
| Staging files with non-ASCII filenames | The commit was blocked with a message advising renaming the file |
| Staging files with trailing whitespace | The commit was blocked, and the offending lines were displayed |
| Committing clean files | The commit proceeded successfully |

## What we Learned

### Purpose of Pre-Commit Hooks
- Pre-commit hooks are powerful tools for enforcing code quality and repository standards before changes are committed.
- They help catch issues early in the development process, reducing the likelihood of introducing bugs or vulnerabilities.

### Using Bandit for Security Scans
- Bandit is a static analysis tool for Python that identifies common security issues.
- Integrating Bandit into a pre-commit hook ensures that security vulnerabilities are addressed before code is committed.

### Customizing Git Hooks
- Git hooks can be customized to suit the needs of a project, such as:
  - Ignoring specific checks (e.g., trailing whitespace).
  - Adding new checks (e.g., linting or formatting).

### Workflow Integration
- Pre-commit hooks are part of a larger workflow that includes CI/CD pipelines.
- They act as a first line of defense, ensuring that only high-quality code reaches the repository.

## Conclusion
The pre-commit hook script is a well-designed tool for enforcing code quality and security standards in the repository. By analyzing and testing the script, we gained a deeper understanding of how Git hooks work and how they can be customized to meet project requirements. This knowledge can be applied to improve development workflows and maintain high standards in collaborative projects.

