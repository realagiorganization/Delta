# Usage Guide

## Prerequisites

- Xcode 15.4 or newer
- Ruby 3.2 with Bundler
- Python 3.12 or newer
- Git LFS
- Access to the required submodules

## Clone and Bootstrap

```bash
git clone https://github.com/realagiorganization/Delta.git
cd Delta
git lfs install
git submodule sync --recursive
git submodule update --init --recursive
bundle install
```

## Build the App Locally

Use a simulator build when you only need compile validation.

```bash
xcodebuild \
  -workspace Delta.xcworkspace \
  -scheme Delta \
  -configuration Debug \
  -destination 'generic/platform=iOS Simulator' \
  CODE_SIGNING_ALLOWED=NO \
  clean build
```

For local device builds or archives, open `Delta.xcworkspace` in Xcode, set your signing team, and use a unique bundle identifier if needed.

## Run the BDD Suite

The BDD suite validates the principal use-case descriptions under `Tests/BDD`.

```bash
python scripts/run_bdd.py
```

To generate the same summary artifacts used in CI:

```bash
python scripts/run_bdd.py \
  --markdown-summary build/bdd-summary.md \
  --json-summary build/bdd-summary.json
```

## Regenerate the BDD GIF

The repository includes `Docs/bdd/bdd-run.tape` for `vhs-action`. Locally, you can use VHS to rebuild `Docs/bdd/bdd-run.gif` if you have the tool installed.

## Run a TestFlight Release Locally

1. Export the mandatory variables documented in `docs/ENVS.md`.
2. Ensure your signing certificate and provisioning profile match `APP_IDENTIFIER` and `APPLE_TEAM_ID`.
3. Run:

```bash
bundle exec fastlane testflight
```

## GitHub Actions

- `iOS CI`: generic iOS Simulator build validation on GitHub-hosted macOS runners.
- `BDD Suite`: feature validation plus VHS capture on GitHub-hosted Linux runners.
- `iOS TestFlight`: signed Release archive and TestFlight upload on GitHub-hosted macOS runners.

GitHub-hosted runners are sufficient for this repository's hosted compute requirement and are backed by Azure infrastructure.
