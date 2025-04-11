# sheets-sync-project

📄 ใช้ Python + GitHub Actions เพื่อ sync ข้อมูลระหว่าง Google Sheets A → B อัตโนมัติ

## วิธีใช้งาน
1. สร้างไฟล์ `sync_sheets.py`
2. ตั้งค่า GitHub Secrets → `SERVICE_ACCOUNT_JSON`
3. เพิ่ม workflow `.github/workflows/sheets-sync.yml`
4. กำหนดเวลา หรือกด Run ด้วยตนเอง

## Dependencies
- gspread
- google-auth
