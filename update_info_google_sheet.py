#update_info_google_sheet.py
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from typing import List



# ---- EXAMPLE GOOGLE API ----
# https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit?gid=SHEET_ID#gid=SHEET_ID


# ---- SETTINGS ----
SPREADSHEET_ID = "1cL_1bYaq3Z5wXmOGq8W-t6C6tybyh7MQ-qoxzQfxBKA" 
SHEET_NAME = "Sheet1"     # must match the tab label exactly
START_CELL = "A2"         # where updates begin
COLUMN_A1 = "A:A"         # which column to append into

# ---- AUTH ----

def _get_service():
    cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "e-ngiem-tap-69a3e7733ae6.json")
    if not os.path.exists(cred_path):
        raise RuntimeError(f"Google credentials file not found at {cred_path}")
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file(cred_path, scopes=scopes)
    return build("sheets", "v4", credentials=creds)

'''
def _get_service():
    creds = Credentials.from_service_account_file(
        "e-ngiem-tap-1ad30daf6fdd.json",
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    return build("sheets", "v4", credentials=creds)
'''

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

# ---- GET CURRENT DATA ----
def get_column_data(sheetID: str, sheet_name: str, column_a1: str):
    ''' Read the existing values in a column (e.g., 'A:A') and return a flat list'''
    service = _get_service()
    rng = f"{sheet_name}!{column_a1}" # e.g., Sheet1!A:A
    resp = service.spreadsheets().values().get(
        spreadsheetId = sheetID,
        range = rng,
        majorDimension = "COLUMNS",
        valueRenderOption = "UNFORMATTED_VALUE"
    ).execute()
    cols = resp.get("values",[]) #return a list of column
    col = cols[0] if cols else [] # taking the first column of the google sheet
    col = col[1:] # Cut the first value, which is the header for this instance
    return col

# ---- COMPARE ARRRAYS ----
def compare_array(oldName: List[str], newName: List[str]) -> List[str]:
    #Example
    # Current user submission: "Dien, Dat, Chinh"
    # API call return new user submission: "Dien, Dat, Chinh, Trish" 
    # Return Trish
    oldSet = set(oldName)
    result: List[str] =[]

    for name in newName:
        if name not in oldSet:
            result.append(name)
    return result

# ---- EXAMPLE DATA ----
# ----------------------
arr1 = ['Dien','Dat','Chinh','Trish']

if __name__ == "__main__":
    # Append
    # result = append_column(arr1,SPREADSHEET_ID,SHEET_NAME,COLUMN_A1)

    # Update
    #resultUpdate = update_colmun(arr1,SPREADSHEET_ID,SHEET_NAME,START_CELL)

    #result = get_column_data(SPREADSHEET_ID,SHEET_NAME,COLUMN_A1)
    #print(result)
    #print(arr1)

    #compareResult = compare_array(result,arr1)
    #print(compareResult)

    print('Done')

