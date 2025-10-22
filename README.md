# Fake FPS Overlay / โปรแกรมแสดงค่า FPS ปลอม

A fake FPS overlay application that displays simulated gaming metrics (FPS, PING, PL, CPU) on your screen. Perfect for streaming or recording purposes.

โปรแกรมแสดงค่า FPS ปลอมที่แสดงเมตริกซ์การเล่นเกมจำลอง (FPS, PING, PL, CPU) บนหน้าจอ เหมาะสำหรับการสตรีมหรือบันทึกวิดีโอ

## Features / คุณสมบัติ

- **GUI Version**: Standalone desktop overlay with customizable metrics
- **Auto-positioning**: Automatically positions over FiveM window
- **Focus Detection**: Only shows when FiveM is active
- **Configurable**: Easy configuration via text file
- **Real-time Updates**: Dynamic metric changes for realistic appearance

- **เวอร์ชัน GUI**: โอเวอร์เลย์เดสก์ท็อปแบบสแตนด์อโลนพร้อมเมตริกซ์ที่ปรับแต่งได้
- **การจัดตำแหน่งอัตโนมัติ**: จัดตำแหน่งเหนือหน้าต่าง FiveM อัตโนมัติ
- **การตรวจจับโฟกัส**: แสดงเฉพาะเมื่อ FiveM ใช้งานอยู่
- **ปรับแต่งได้**: การกำหนดค่าผ่านไฟล์ข้อความ
- **อัปเดตแบบเรียลไทม์**: การเปลี่ยนแปลงเมตริกซ์แบบไดนามิกเพื่อความสมจริง

## Installation / การติดตั้ง

### Option 1: Run from Source / ตัวเลือกที่ 1: รันจากซอร์สโค้ด

1. Clone this repository:
```bash
git clone https://github.com/De3w/FakeFps.git
cd FakeFps
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

### Option 2: Use Executable / ตัวเลือกที่ 2: ใช้ไฟล์ที่รันได้

Download the latest release from the [Releases](https://github.com/De3w/FakeFps/releases) page and run the executable files.

ดาวน์โหลดเวอร์ชันล่าสุดจากหน้า [Releases](https://github.com/De3w/FakeFps/releases) และรันไฟล์ที่รันได้

## Configuration / การกำหนดค่า

Edit `config.txt` to customize the default values:

แก้ไข `config.txt` เพื่อปรับแต่งค่าเริ่มต้น:

```
FPS=600
PING=10
PL=0
CPU=5
```

## Usage / การใช้งาน

### GUI Version (main.py) / เวอร์ชัน GUI (main.py)
- Shows a persistent overlay on your screen
- Automatically positions over FiveM window
- Only visible when FiveM is the active window
- Real-time metric updates with realistic variations

- แสดงโอเวอร์เลย์ถาวรบนหน้าจอ
- จัดตำแหน่งเหนือหน้าต่าง FiveM อัตโนมัติ
- แสดงเฉพาะเมื่อ FiveM เป็นหน้าต่างที่ใช้งานอยู่
- อัปเดตเมตริกซ์แบบเรียลไทม์พร้อมการเปลี่ยนแปลงที่สมจริง

## Building Executables / การสร้างไฟล์ที่รันได้

To build executable files from source:

เพื่อสร้างไฟล์ที่รันได้จากซอร์สโค้ด:

```bash
# Install PyInstaller
pip install pyinstaller

# Build GUI version
pyinstaller --onefile --windowed --name "FakeFPS-GUI" main.py
```

## Requirements / ความต้องการ

- Python 3.7+
- Windows (for win32gui support)
- FiveM (optional, for auto-positioning)

## License / ใบอนุญาต

This project is for educational and entertainment purposes only.

โปรเจกต์นี้มีไว้เพื่อการศึกษาและความบันเทิงเท่านั้น

## Disclaimer / ข้อจำกัดความรับผิดชอบ

This tool is for educational and entertainment purposes only. Use responsibly and in accordance with applicable laws and regulations.

เครื่องมือนี้มีไว้เพื่อการศึกษาและความบันเทิงเท่านั้น ใช้อย่างรับผิดชอบและปฏิบัติตามกฎหมายและข้อบังคับที่เกี่ยวข้อง