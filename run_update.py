import sys, os
from restAPI_Docuseal import fetch_submitter_names
from update_info_google_sheet import update_colmun, append_column


# ---- CONFIG DOCUSEAL ----
DOCUSEAL_URL = "https://api.docuseal.com/submitters"
API_TOKEN = os.getenv("DOCUSEAL_API_TOKEN") or 'FmzWAds1rshavQtaN3BWjSvnHsrW9vuUVLTBMjDuZM4'  # fallback if env var not set

# ---- CONFIG GOOGLE SHEET ----
SPREADSHEET_ID = ""
SHEET_NAME = "Sheet1"     # must match the tab label exactly
START_CELL = "A2"         # where updates begin
COLUMN_A1 = "A:A"         # which column to append into

cac_em_name = fetch_submitter_names(DOCUSEAL_URL,API_TOKEN)
#Success fully fetch sumitters
print(f'Success fetched {(cac_em_name)} names from Docuseal')

#def append_column(values_1d,sheetID: str,sheet_name: str,column:str):
runAppend = append_column(cac_em_name,SPREADSHEET_ID,SHEET_NAME,COLUMN_A1)
#Sucess fully append cac em name
print(f"Successfully appended names to {runAppend['updates'].get('updatedRange')}.")
