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
SHEET_A_ID = "ใส่-ID-ชีตต้นทาง"
SHEET_B_ID = "ใส่-ID-ชีตปลายทาง"

sheet_a = client.open_by_key(SHEET_A_ID).sheet1
sheet_b = client.open_by_key(SHEET_B_ID).sheet1

data_a = sheet_a.get_all_values()
sheet_b.clear()
sheet_b.update("A1", data_a)

print("✅ อัปเดตข้อมูลเรียบร้อย")
