# Working Agent Prompts

These are the self-prompts used during this automation pass:

1. Audit the repository before editing so workflow, Fastlane, README, and test changes match the current codebase instead of assumptions.
2. Treat the shared `Delta` scheme honestly: because it has no XCTest testables, keep build validation and behavioral validation as separate workflows.
3. Prefer GitHub Actions defaults that work on hosted runners without custom infrastructure, especially HTTPS submodule checkout and code-signing-free simulator builds.
4. Keep the documentation contract explicit by making `docs/` the canonical home for planning, assumptions, usage, and environment variables.
5. Fail fast in release automation when secrets or signing inputs are missing, and preserve artifacts needed to debug release failures.
6. Keep the README aligned with what the repository actually ships: badges, BDD features, VHS media, and developer entry points.
