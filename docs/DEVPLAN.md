# Delta Development Plan

## Current Status
- [x] Audit the repository's existing automation, docs, media assets, and release tooling.
- [x] Normalize the required operational docs under `docs/`.
- [x] Add and harden GitHub Actions for iOS build validation, BDD validation, VHS capture, and TestFlight release delivery.
- [x] Publish workflow badges and automation previews in `README.md`.
- [x] Run repository-safe validation available in this container (`python3 scripts/run_bdd.py`, `git diff --check`).
- [ ] Validate the updated workflows on GitHub-hosted macOS runners with real signing secrets.
- [ ] Publish the first TestFlight build from the new release workflow and capture any follow-up fixes.

## Delivery Tracks

### 1. Repository Bootstrap
- [x] Document prerequisites for local development.
- [x] Document release-specific environment variables and secrets.
- [x] Convert submodule URLs to HTTPS so GitHub Actions can clone them without SSH key management.
- [ ] Confirm every external submodule remains reachable from CI and pin replacements if an upstream disappears.

### 2. App Build Validation
- [x] Build the `Delta` scheme for a generic iOS Simulator destination in CI.
- [x] Disable code signing for simulator builds.
- [x] Surface build status through a dedicated GitHub Actions badge.
- [ ] Add native XCTest or XCUITest coverage if the project later needs executable simulator assertions beyond feature specs.

### 3. Behavioral Test Coverage
- [x] Keep the principal user journeys described as `.feature` files in `Tests/BDD`.
- [x] Validate feature completeness with `scripts/run_bdd.py`.
- [x] Generate Markdown and JSON summaries from the BDD validation step.
- [x] Capture the BDD console run with VHS and embed the GIF in `README.md`.
- [ ] Expand feature coverage for onboarding, error handling, purchase flows, and regressions introduced by future app changes.

### 4. Release Automation
- [x] Keep a Fastlane lane dedicated to Release archive and TestFlight upload.
- [x] Fail fast when required App Store Connect or signing inputs are missing.
- [x] Install certificate and provisioning profile material on the macOS runner during release jobs.
- [x] Archive build outputs as workflow artifacts for debugging.
- [ ] Move TestFlight release jobs behind a protected GitHub Environment once the team configures reviewers and secret scopes.

### 5. Documentation and Readiness
- [x] Keep assumptions current in `docs/ASSUMPTIONS.md`.
- [x] Publish developer setup/run instructions in `docs/USAGE.md`.
- [x] Publish environment variable definitions in `docs/ENVS.md`.
- [x] Publish the agent working prompts in `docs/AGENTS.md`.
- [ ] Add a troubleshooting section after the first real CI failures expose the highest-friction setup issues.

## External Dependencies

### Build, CI, and Release
- GitHub Actions: orchestrates CI, BDD validation, VHS capture, and TestFlight release jobs.
- GitHub-hosted runners on Azure: provide the hosted Linux and macOS compute used by the workflows.
- Fastlane: builds the Release archive and uploads it to TestFlight with App Store Connect API credentials.
- Ruby/Bundler: installs and pins the Fastlane toolchain used by release automation.
- Git LFS: required for large assets that must be present during checkout.

### Apple Tooling
- Xcode 15.4+: required to build the app and archive iOS releases.
- iOS SDK / Simulator runtimes: required for CI build validation.
- App Store Connect API: required for authenticated TestFlight uploads.
- Apple distribution certificate and provisioning profile: required for signed device archives.

### Project Modules and Libraries
- CocoaPods: dependency manager for pods declared in `Podfile`.
- DeltaCore: shared emulator integration layer used by the app.
- NESDeltaCore, SNESDeltaCore, N64DeltaCore, GBCDeltaCore, GBADeltaCore, MelonDSDeltaCore, GPGXDeltaCore: system-specific emulator cores.
- Roxas: shared utility framework used throughout the app.
- Harmony: sync framework used by Delta Sync.
- CheatBase: external submodule supplying cheat metadata functionality.
- SQLite.swift, SDWebImage, SMCalloutView: pod-managed libraries used by the app target.
- RevenueCat and KeychainAccess: Swift package dependencies already referenced by the Xcode project.

### User-Facing Service Integrations
- Google Drive: one of the cloud sync providers exposed through Delta Sync.
- Dropbox: one of the cloud sync providers exposed through Delta Sync.
- TestFlight: Apple distribution channel for prerelease iOS builds.
