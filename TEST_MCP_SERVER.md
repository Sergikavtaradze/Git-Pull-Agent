# Testing Your MCP Server with This Repository

This guide shows how to test your MCP server's PR template selection capabilities using this test repository.

## Setup

1. Make sure your MCP server is configured and running
2. This repository is already set up with:
   - A `main` branch (initial commit)
   - A `feature/add-multiply-function` branch with new functionality
   - All PR templates in the `templates/` directory

## Test Scenarios

### Scenario 1: Analyzing a Feature Addition

This is the default state - we have a feature branch ready to go.

**Steps:**
1. Make sure you're on the `feature/add-multiply-function` branch
2. Ask your MCP server to analyze changes:
   ```
   "I'm working on feature/add-multiply-function branch. Can you analyze my changes and suggest a PR template?"
   ```
3. Your MCP server should:
   - Call `analyze_file_changes` to see the diff
   - Call `get_pr_templates` to see available templates
   - Call `suggest_template` with analysis of the feature
   - Recommend the **feature.md** template

### Scenario 2: Create a Bug Fix

To test bug fix detection:

1. Create a new branch: `git checkout -b bugfix/fix-divide-by-zero`
2. Modify `src/example.py` to improve error handling
3. Commit the changes
4. Ask your MCP server to suggest a template for a bug fix

### Scenario 3: Create a Documentation Update

To test documentation template selection:

1. Create a new branch: `git checkout -b docs/update-contributing`
2. Update `docs/CONTRIBUTING.md` with more detailed information
3. Commit the changes
4. Ask your MCP server to suggest a template for documentation

### Scenario 4: Create a Refactoring

To test refactoring detection:

1. Create a new branch: `git checkout -b refactor/improve-code-structure`
2. Reorganize or improve code structure in `src/example.py`
3. Commit the changes
4. Ask your MCP server to suggest a template for refactoring

## Quick Commands

**View current branch:**
```bash
git branch
```

**Switch branches:**
```bash
git checkout main
git checkout feature/add-multiply-function
```

**Create a new test branch:**
```bash
git checkout -b feature/your-feature-name
```

**View changes on current branch:**
```bash
git diff main...HEAD
```

**View file changes summary:**
```bash
git diff --stat main...HEAD
```

## Expected MCP Server Behavior

When you ask your MCP server to analyze changes and suggest a template:

1. **analyze_file_changes** should return:
   - List of changed files
   - Full diff (or truncated if large)
   - Commit messages
   - Statistics about the changes

2. **get_pr_templates** should return:
   - All 7 available templates (bug, feature, docs, refactor, test, performance, security)
   - Content of each template

3. **suggest_template** should return:
   - The recommended template based on change type
   - Reasoning for the recommendation
   - The template content
   - Usage hints

## Example MCP Server Workflow

```
User: "I made some changes on my feature branch. Can you help me with a PR template?"
↓
MCP Server calls: analyze_file_changes(base_branch="main")
↓
MCP Server receives: Diff showing new divide() and power() functions added
↓
MCP Server calls: get_pr_templates()
↓
MCP Server receives: All available templates
↓
MCP Server calls: suggest_template(
    changes_summary="Added divide and power mathematical functions",
    change_type="feature"
)
↓
MCP Server returns: feature.md template with guidance
↓
User: "Here's your PR template filled out..."
```

## Troubleshooting

**MCP Server can't find git repository:**
- Make sure you're asking from within the test-repo directory or set working_directory parameter

**Templates not found:**
- Verify the TEMPLATES_DIR path in server.py points to the templates/ directory

**No changes detected:**
- Make sure you're on a different branch than main
- Run `git diff main...HEAD` to verify changes exist

## Next Steps

After testing with this repository:
1. Test with your own actual repositories
2. Integrate the MCP server with Claude Code
3. Use it in your actual development workflow
