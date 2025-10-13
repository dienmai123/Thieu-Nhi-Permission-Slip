import os
import sys
from restAPI_Docuseal import fetch_submitter_names
from update_info_google_sheet import update_colmun, append_column  # keep both imports if you use either

# ---- CONFIG DOCUSEAL ----
DOCUSEAL_URL = "https://api.docuseal.com/submitters"


# ---- CONFIG GOOGLE SHEET ----
SPREADSHEET_ID = "1cL_1bYaq3Z5wXmOGq8W-t6C6tybyh7MQ-qoxzQfxBKA"
SHEET_NAME = "Sheet1"     # must match the tab label exactly
START_CELL = "A2"         # where updates begin
COLUMN_A1 = "A:A"         # which column to append into

def main():
    # Read Docuseal token from env ONLY (no hardcoded fallback)
    api_token = os.getenv("DOCUSEAL_API_TOKEN")
    if not api_token:
        raise RuntimeError("DOCUSEAL_API_TOKEN is not set")

    # Fetch names
    names = fetch_submitter_names(DOCUSEAL_URL, api_token)
    if not isinstance(names, list):
        raise RuntimeError(f"Unexpected response type from fetch_submitter_names: {type(names)}")
    print(f"Successfully fetched {len(names)} names from Docuseal")

    if not names:
        print("No names to append")
        return

    # Append to column A (or switch to update_colmun(...) if you intend cell-by-cell updates)
    result = append_column(names, SPREADSHEET_ID, SHEET_NAME, COLUMN_A1)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
