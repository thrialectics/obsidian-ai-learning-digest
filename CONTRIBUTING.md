# Contributing to Obsidian Summarizer

Thank you for your interest in contributing to Obsidian Summarizer! This document provides guidelines and steps for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/obsidian-summarizer.git
   cd obsidian-summarizer
   ```
3. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. Create your feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Setup

1. Copy the example configuration files:
   ```bash
   cp .env.example .env
   cp example-config.py config.py
   ```
2. Update the configuration files with your test values
3. For macOS users, copy the example plist file:
   ```bash
   cp com.user.obsidian-summarizer.plist.example ~/Library/LaunchAgents/com.user.obsidian-summarizer.plist
   ```

## Making Changes

1. Write your code
2. Add or update tests as needed
3. Run the test suite:
   ```bash
   python -m pytest
   ```
4. Update documentation if necessary

## Commit Guidelines

- Use clear, descriptive commit messages
- Reference issue numbers in commit messages when applicable
- Keep commits focused and atomic

## Pull Request Process

1. Update the README.md with details of changes if needed
2. Update the requirements.txt if you've added dependencies
3. Ensure all tests pass
4. Create a pull request with a clear title and description

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Include docstrings for functions and classes

## Testing

- Write tests for new features
- Ensure existing tests pass
- Test your changes with different Python versions if possible

## Questions or Problems?

Feel free to open an issue for:
- Bug reports
- Feature requests
- Questions about the codebase
- Installation or setup issues

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (see LICENSE file). 