# Development Plan

## Goals
- Maintain a stable iOS emulator experience across supported systems.
- Keep the app modular by isolating platform-specific code in DeltaCore and the system cores.
- Ship releases through CI with clear checks for build, tests, and release automation.

## Core Development Steps
1. **Bootstrap environment**
   - Install Xcode 15+, Swift 5.9 toolchain, and Git LFS.
   - Ensure CocoaPods and Bundler are available for dependency management.
2. **Fetch dependencies and submodules**
   - Initialize git submodules for DeltaCore and system cores.
   - Verify private framework access for Roxas and Harmony (if applicable).
3. **Build and run locally**
   - Open `Delta.xcworkspace` in Xcode.
   - Configure signing and a unique bundle identifier.
   - Run on iOS Simulator and a physical device to validate device-only features.
4. **Implement features or fixes**
   - Update app UI/UX in `Delta` target.
   - Update emulator integrations or shared logic in DeltaCore.
   - Add or update unit/BDD scenarios describing behavior changes.
5. **Verify via automation**
   - Run local build/test (Xcode or CI) with simulator destination.
   - Run BDD validation suite.
6. **Release preparation**
   - Confirm versioning, release notes, and signing assets.
   - Trigger TestFlight workflow for release candidates.

## External Dependencies
- **Xcode/iOS SDK**: Required to build, test, and archive the app for devices and TestFlight.
- **CocoaPods**: Manages iOS dependencies listed in `Podfile`.
- **Git LFS**: Stores large assets used by the project.
- **DeltaCore**: Shared framework providing emulation APIs and core behaviors.
- **System Cores** (NESDeltaCore, SNESDeltaCore, N64DeltaCore, GBCDeltaCore, GBADeltaCore, MelonDSDeltaCore, GPGXDeltaCore): Provide the system-specific emulation engines.
- **Roxas**: Utility framework used across the app for shared functionality.
- **Harmony**: Sync framework enabling Delta Sync with cloud providers.
- **Third-party services**: Google Drive and Dropbox for sync backends.
- **GitHub Actions**: CI automation for builds, tests, BDD validation, and TestFlight deployments.
- **Fastlane**: Automates TestFlight uploads through App Store Connect API keys.
