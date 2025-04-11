import os
import json
import gspread
from google.oauth2.service_account import Credentials

service_account_info = json.loads(os.environ["SERVICE_ACCOUNT_JSON"])
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
client = gspread.authorize(creds)

SHEET_A_ID = "1yg9oY2rmgAl7ogpkLAh0X3JYkryqa24_bOD86FXAhbU"
SHEET_B_ID = "1k3jW7rc5U9rECJUuU8AJem2Q1sCZ1c3RxcGPLob-4Bo"

sheet_a = client.open_by_key(SHEET_A_ID).sheet1
sheet_b = client.open_by_key(SHEET_B_ID).sheet1

data_a = sheet_a.get_all_values()
sheet_b.clear()
sheet_b.update("A1", data_a)

print("✅ ข้อมูลจาก Google Sheets A อัปเดตไป Google Sheets B สำเร็จ!")
