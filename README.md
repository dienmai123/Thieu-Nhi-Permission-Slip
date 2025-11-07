# Thieu-Nhi-Permission-Slip

Lightweight Python scripts to interact with DocuSeal/rest API and update Google Sheets for permission-slip workflows.

## What this repo contains

- `e-ngiem-tap-1ad30daf6fdd.json` - Google service account JSON (used by `update_info_google_sheet.py`) — keep this private.
- `requirements.txt` - Python dependencies used by the scripts.
- `restAPI_Docuseal.py` - Helper/utility code to call the DocuSeal/rest API.
- `run_update.py` - Main script used to orchestrate updates (typical entry point used by the project owner).
- `testAPI.py` - Small test harness to exercise the API calls.
- `update_info_google_sheet.py` - Script to update a Google Sheet via service account credentials.
- `X-Auth-Token.txt` - File that should contain the DocuSeal API token (sensitive — do not commit secrets publicly).
- `__pycache__/` - Python cache files (automatically generated).

## Quick setup

1. Install Python (3.8+ recommended).
2. From the repository root, create a virtual environment and install dependencies:

```bash
# on WSL (or other bash-like shell)
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Ensure credentials are in place:
- Put your DocuSeal API token into `X-Auth-Token.txt` (single line, no trailing newline issues).
- Place the Google service account JSON in the repo (for example `e-ngiem-tap-1ad30daf6fdd.json`) or point the Google client to its path if the scripts accept an alternate path.

Security note: Do not commit API tokens or service account keys to public repositories. Keep `X-Auth-Token.txt` and the JSON file out of version control or add them to `.gitignore`.

## Usage

Run the main updater (example):

```bash
# from repository root, with virtualenv active
python run_update.py
```

Other useful commands:

```bash
python restAPI_Docuseal.py     # run helper or debug API functions
python testAPI.py             # run quick API tests
python update_info_google_sheet.py  # update Google Sheets using service account
```

If any script accepts command-line flags (check the top of each file), pass them as appropriate. If not, open the file to inspect configuration variables near the top (e.g., sheet ID, file paths, endpoints).

## Troubleshooting

- Missing dependencies: re-run `pip install -r requirements.txt`.
- Auth errors: verify `X-Auth-Token.txt` contains the correct token and no accidental whitespace. For Google API auth, ensure the service account JSON has correct permissions on the target sheet.
- Working on Windows: the project has been used with WSL; ensure path handling in scripts matches your environment or run from WSL for the closest match.

## Contributing / Notes

- This repository appears to be a small set of scripts for a private workflow. If you add features, please:
  - Avoid committing credentials.
  - Add tests for any new behavior.
  - Keep changes small and documented.

