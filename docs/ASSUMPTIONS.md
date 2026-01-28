# Assumptions

- The TestFlight workflow relies on repository secrets for App Store Connect API keys and signing assets; placeholder environment variable names are documented in the workflow and Fastlane config.
- The BDD suite is implemented as lightweight Gherkin validation to keep it runnable without external BDD frameworks.
- The BDD VHS GIF committed to the repo is a placeholder snapshot generated locally; the workflow includes a VHS recording step to regenerate it during CI runs.
- The GitHub Pages visual check uses the provided screenshots from the prompt attachments and is stored under `Docs/github-pages`.
