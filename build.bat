@echo off
echo Building Fake FPS Overlay Executables...
echo กำลังสร้างไฟล์ที่รันได้ของ Fake FPS Overlay...

REM Install PyInstaller if not already installed
echo Installing PyInstaller...
pip install pyinstaller

REM Create build directory
if not exist "dist" mkdir dist

REM Build GUI version
echo Building GUI version...
echo กำลังสร้างเวอร์ชัน GUI...
pyinstaller --onefile --windowed --name "FakeFPS-GUI" --distpath "dist" main.py


REM Copy config file to dist
copy config.txt dist\

echo Build complete! Executables are in the 'dist' folder.
echo สร้างเสร็จแล้ว! ไฟล์ที่รันได้อยู่ในโฟลเดอร์ 'dist'
pause