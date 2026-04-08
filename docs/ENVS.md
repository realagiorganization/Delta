# Environment Variables

This repository does not rely on app runtime environment variables for normal local development. Environment variables are primarily needed for CI and TestFlight release automation.

## Mandatory

These variables are required for the `iOS TestFlight` workflow and for running `bundle exec fastlane testflight` locally.

| Variable | Used By | Purpose |
| --- | --- | --- |
| `APP_IDENTIFIER` | Fastlane, TestFlight workflow | Bundle identifier to archive and upload. |
| `APPLE_TEAM_ID` | Fastlane, TestFlight workflow | Apple Developer team ID used for signing/export. |
| `APP_STORE_CONNECT_API_KEY_ID` | Fastlane | App Store Connect API key identifier. |
| `APP_STORE_CONNECT_API_ISSUER_ID` | Fastlane | App Store Connect API issuer identifier. |
| `APP_STORE_CONNECT_API_KEY_P8` | Fastlane | Raw `.p8` private key content for the App Store Connect API key. |
| `IOS_DISTRIBUTION_CERT_BASE64` | TestFlight workflow | Base64-encoded `.p12` distribution certificate payload. |
| `IOS_DISTRIBUTION_CERT_PASSWORD` | TestFlight workflow | Password for the distribution certificate. |
| `IOS_PROVISIONING_PROFILE_BASE64` | TestFlight workflow | Base64-encoded App Store provisioning profile. |
| `KEYCHAIN_PASSWORD` | TestFlight workflow | Temporary runner keychain password used to import signing assets. |

## Optional

These variables are helpful but not required in every environment.

| Variable | Used By | Purpose |
| --- | --- | --- |
| `DEVELOPER_DIR` | Local shell, GitHub Actions | Pins the Xcode installation path used by `xcodebuild`. |
| `CI` | Fastlane, GitHub Actions | Signals non-interactive CI execution. |
| `FASTLANE_SKIP_UPDATE_CHECK` | Fastlane | Suppresses Fastlane update prompts/noise in CI. |
| `GITHUB_STEP_SUMMARY` | BDD workflow | Lets the workflow publish the generated Markdown summary to the job summary page. |

## Notes

- Local simulator builds do not require the release secrets above when code signing is disabled.
- The BDD validator runs without external environment variables.
- GitHub automatically injects `GITHUB_TOKEN` and other workflow-scoped variables; they are not configured manually here.
