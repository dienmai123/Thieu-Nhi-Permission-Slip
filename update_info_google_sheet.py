#update_info_google_sheet.py
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# ---- EXAMPLE GOOGLE API ----
# https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit?gid=SHEET_ID#gid=SHEET_ID


# ---- SETTINGS ----
SPREADSHEET_ID = "1cL_1bYaq3Z5wXmOGq8W-t6C6tybyh7MQ-qoxzQfxBKA"       # Parse in the target google sheet ID
SHEET_NAME = "Sheet1"     # must match the tab label exactly
START_CELL = "A2"         # where updates begin
COLUMN_A1 = "A:A"         # which column to append into

# ---- AUTH ----
def _get_service():
    creds = Credentials.from_service_account_file(
        ("e-ngiem-tap-dd92e14e408c.json"),
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    return build("sheets", "v4", credentials=creds)

# ---- SHEET UPDATE ----
def update_colmun(values_id,sheetID: str,sheet_name: str,start_cell:str):
    service = _get_service()
    range_a1 = f"{sheet_name}!{start_cell}:{start_cell[0]}"
    bodyFinal = {'values': [[v] for v in values_id]}
    resp = service.spreadsheets().values().update(
        spreadsheetId = sheetID,
        range = range_a1,
        valueInputOption = 'RAW',
        body = bodyFinal
    ).execute()
    return resp

# ---- SHEET APPEND ----
def append_column(values_1d,sheetID: str,sheet_name: str,column:str):
    """Append new rows at the bottom of the column."""
    service = _get_service()
    range_a1 = f"{sheet_name}!{column}"  # e.g., Sheet1!A:A
    body = {"values": [[v] for v in values_1d]}  # 2D list
    resp = service.spreadsheets().values().append(
        spreadsheetId=sheetID,
        range=range_a1,
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body=body
    ).execute()
    return resp

# ---- EXAMPLE DATA ----
# ----------------------
arr1 = [1,2,3,4]

if __name__ == "__main__":
    # Append
    #result = append_column(arr1,SPREADSHEET_ID,SHEET_NAME,COLUMN_A1)

    # Update
    #resultUpdate = update_colmun(arr1,SPREADSHEET_ID,SHEET_NAME,START_CELL)

    print('Done')

