# Project coding standards

## General Guidelines

- Prioritize **type safety** throughout the project.
- Use modern Python practices and avoid deprecated modules.
- Make code **modular and readable**.
- Prefer pure functions unless state is required.

## Naming Conventions

- Use PascalCase for component names, interfaces, and type aliases
- Use camelCase for variables, functions, and methods
- Prefix private class members with underscore (_)
- Use ALL_CAPS for constants

## Error Handling Preferences

- Use proper exception types
- Return meaningful error messages
- Include proper status codes
- Handle database errors gracefully
- Log errors with appropriate severity levels

## Testing

- All parsing logic should have corresponding unit tests
- Use `pytest`.
- Avoid test code in main modules — separate test files in `/tests`
