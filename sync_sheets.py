import os
import json
import gspread
from google.oauth2.service_account import Credentials

# โหลดจาก ENV
service_account_info = json.loads(os.environ["SERVICE_ACCOUNT_JSON"])

# กำหนด scope
scopes = ["https://www.googleapis.com/auth/spreadsheets"]

# สร้าง credentials จากข้อมูล JSON
creds = Credentials.from_service_account_info(service_account_info, scopes=scopes)
client = gspread.authorize(creds)

# ใช้งาน Google Sheets
SHEET_A_ID = "1yg9oY2rmgAl7ogpkLAh0X3JYkryqa24_bOD86FXAhbU"  # Google Sheets A (ต้นทาง)
SHEET_B_ID = "1k3jW7rc5U9rECJUuU8AJem2Q1sCZ1c3RxcGPLob-4Bo"  # Google Sheets B (ปลายทาง)

sheet_a = client.open_by_key(SHEET_A_ID).sheet1
sheet_b = client.open_by_key(SHEET_B_ID).sheet1

data_a = sheet_a.get_all_values()
sheet_b.clear()
sheet_b.update("A1", data_a)

print("✅ อัปเดตข้อมูลเรียบร้อย")
