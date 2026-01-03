# Test Repository

This is a test repository for demonstrating MCP server PR template selection functionality.

## Purpose

This repository allows you to:
1. Make changes to files
2. Create commits
3. Test your MCP server's ability to analyze changes and suggest appropriate PR templates

## Getting Started

Make some changes to the files in this repository, commit them, and then use your MCP server to:
1. Analyze the changes with `analyze_file_changes`
2. Get available templates with `get_pr_templates`
3. Get a template suggestion with `suggest_template`

## Project Structure

```
test-repo/
├── README.md                 # This file
├── templates/               # PR templates directory
│   ├── bug.md              # Bug fix template
│   ├── feature.md          # Feature template
│   ├── docs.md             # Documentation template
│   ├── refactor.md         # Refactor template
│   ├── test.md             # Test template
│   ├── performance.md      # Performance template
│   └── security.md         # Security template
├── src/                     # Source code
│   └── example.py          # Example Python file
└── docs/                    # Documentation
    └── CONTRIBUTING.md     # Contributing guidelines
```

## Making Test Changes

To test your MCP server, try these scenarios:

### Test 1: Bug Fix
- Modify `src/example.py` to fix a bug
- Create a commit
- Ask your MCP server to suggest a template

### Test 2: Feature Addition
- Add new functionality to `src/example.py`
- Create a commit
- Ask your MCP server to suggest a template

### Test 3: Documentation Update
- Update `docs/CONTRIBUTING.md`
- Create a commit
- Ask your MCP server to suggest a template
