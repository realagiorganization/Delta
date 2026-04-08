# Assumptions

- The shared `Delta` Xcode scheme currently has no XCTest testables, so `iOS CI` is treated as a build-validation workflow while the separate BDD workflow provides the behavioral test badge.
- The TestFlight workflow relies on GitHub repository secrets for App Store Connect API keys, a distribution certificate, and a provisioning profile; those secrets are documented in `docs/ENVS.md` but are not stored in the repository.
- GitHub-hosted Actions runners provide the required compute, and those hosted runners are assumed to be sufficient for this project's Azure-backed execution requirement.
- The BDD suite is intentionally lightweight Gherkin validation so it remains runnable on non-macOS environments without pulling in a full Cucumber stack.
- The committed `Docs/bdd/bdd-run.gif` asset is a checked-in preview; the BDD workflow regenerates it with VHS on non-PR runs.
- The GitHub Pages visual check uses the screenshots supplied in the prompt attachments and stores the curated copies under `Docs/github-pages`.
- `Docs/` remains the repository's existing media/documentation asset directory, while `docs/` is the canonical location for the operational documentation required by this automation pass.
