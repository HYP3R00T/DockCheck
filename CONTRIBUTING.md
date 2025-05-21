# Contributing to DockCheck

Thank you for your interest in contributing to DockCheck! We welcome contributions from the community to help improve this project.

## Getting Started

1. **Fork the repository** and clone it to your local machine.
2. **Create a new branch** for your feature or bugfix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Install dependencies** using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **(Recommended) Use Dev Container for Local Development:**

   If you use [Visual Studio Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers), you can open this project directly in a pre-configured development environment. This ensures all dependencies, Python, and linting tools are set up for you automatically.

   - Open the project in VS Code and select "Reopen in Container" when prompted.
   - The dev container includes up-to-date Python, uv, and other tools for seamless development.

## Coding Standards

- **Type Safety:** Use type hints throughout the codebase.
- **Naming Conventions:**
  - PascalCase for component names, interfaces, and type aliases
  - camelCase for variables, functions, and methods
  - Prefix private class members with an underscore (_)
  - ALL_CAPS for constants
- **Modularity:** Write modular, readable, and DRY code.
- **Error Handling:**
  - Use appropriate exception types
  - Return meaningful error messages and status codes
  - Handle database errors gracefully
  - Log errors with appropriate severity
- **Testing:**
  - All parsing logic must have corresponding unit tests in `/tests`
  - Use `pytest` for testing
  - Do not include test code in main modules

## Making Changes

- Ensure your code passes all tests:

  ```bash
  pytest
  ```

- Add or update documentation and comments for complex logic.
- Follow the existing code style and conventions.

## Submitting a Pull Request

1. Push your branch to your fork.
2. Open a pull request against the `main` branch.
3. Provide a clear description of your changes and reference any related issues.
4. Ensure all checks pass and requested changes are addressed.

## Code of Conduct

Please be respectful and considerate in all interactions. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) if available.

---

Thank you for helping make DockCheck better!
