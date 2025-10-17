import os
import sys
from restAPI_Docuseal import fetch_submitter_names
from update_info_google_sheet import update_colmun, append_column, get_column_data, compare_array  # keep both imports if you use either

# ---- CONFIG DOCUSEAL ----
DOCUSEAL_URL = "https://api.docuseal.com/submitters"


# ---- CONFIG GOOGLE SHEET ----
SPREADSHEET_ID = "1cL_1bYaq3Z5wXmOGq8W-t6C6tybyh7MQ-qoxzQfxBKA"
SHEET_NAME = "Sheet1"     # must match the tab label exactly
START_CELL = "A2"         # where updates begin
COLUMN_A1 = "A:A"         # which column to append into

'''
def main():
    # Read Docuseal token from env ONLY (no hardcoded fallback)
    api_token = os.getenv("DOCUSEAL_API_TOKEN")
    if not api_token:
        raise RuntimeError("DOCUSEAL_API_TOKEN is not set")
    
    # Fetch names
    names = fetch_submitter_names(DOCUSEAL_URL, api_token)
    if not isinstance(names, list):
        raise RuntimeError(f"Unexpected response type from fetch_submitter_names: {type(names)}")
    print(f"Successfully fetched {(names)} names from Docuseal")

    # Append user the to column
    result = append_column(names, SPREADSHEET_ID, SHEET_NAME, COLUMN_A1)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
'''

def main ():
    # Read Docuseal token from env ONLY (no hardcoded fallback)
    api_token = os.getenv("DOCUSEAL_API_TOKEN")
    if not api_token:
        raise RuntimeError("DOCUSEAL_API_TOKEN is not set")

    # Fetch names 
    apiCacEmNames = fetch_submitter_names(DOCUSEAL_URL,'FmzWAds1rshavQtaN3BWjSvnHsrW9vuUVLTBMjDuZM4')
    print(f'API call names: {(apiCacEmNames)}')

    currentCacEmNames = get_column_data(SPREADSHEET_ID,SHEET_NAME,COLUMN_A1)
    print(f"Current user on google sheet: {currentCacEmNames}")

    newSubmission = compare_array(currentCacEmNames,apiCacEmNames)
    print(f"Final cac em name to be added: {(newSubmission)}")

    addingNameToSheet = append_column(newSubmission,SPREADSHEET_ID,SHEET_NAME,COLUMN_A1)
    print('Done adding')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

