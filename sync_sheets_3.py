import os
import json
import gspread
from google.oauth2.service_account import Credentials
from gspread.utils import a1_to_rowcol

# 🔹 ดึง JSON จาก ENV
SERVICE_ACCOUNT_JSON = os.environ["SERVICE_ACCOUNT_JSON"]
info = json.loads(SERVICE_ACCOUNT_JSON)

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_info(info, scopes=SCOPES)
client = gspread.authorize(creds)

# 🔹 ระบุ Google Sheets A และ B
SHEET_A_ID = "1yg9oY2rmgAl7ogpkLAh0X3JYkryqa24_bOD86FXAhbU"
SHEET_B_ID = "1k3jW7rc5U9rECJUuU8AJem2Q1sCZ1c3RxcGPLob-4Bo"

sheet_a = client.open_by_key(SHEET_A_ID).sheet1
sheet_b = client.open_by_key(SHEET_B_ID).sheet1

# 🔹 ดึงข้อมูลจาก Sheet A
data_a = sheet_a.get_all_values()

# 🔹 แปลงข้อมูล [ชื่อ, ราคา, จำนวน]
formatted_data = []
for row in data_a[1:]:
    name = row[1]
    quantity = row[2]
    price = row[3]
    formatted_data.append([name, price, quantity])

# ✅ ระบุตำแหน่งเริ่มต้น
start_row, _ = a1_to_rowcol("A1")  # เริ่มที่แถว 1
_, col_name = a1_to_rowcol("D1")
_, col_price = a1_to_rowcol("G1")
_, col_quantity = a1_to_rowcol("H1")

# ✅ เขียนหัวตาราง
sheet_b.update_cell(start_row, col_name, "ชื่อ")
sheet_b.update_cell(start_row, col_price, "ราคา")
sheet_b.update_cell(start_row, col_quantity, "จำนวน")

# ✅ เขียนข้อมูล
for i, row in enumerate(formatted_data):
    sheet_b.update_cell(start_row + 1 + i, col_name, row[0])
    sheet_b.update_cell(start_row + 1 + i, col_price, row[1])
    sheet_b.update_cell(start_row + 1 + i, col_quantity, row[2])

print("✅ อัปเดตข้อมูลจาก A → B ที่คอลัมน์ D, G, H สำเร็จ!")
