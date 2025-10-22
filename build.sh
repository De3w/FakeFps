#!/bin/bash
echo "Building Fake FPS Overlay Executables..."
echo "กำลังสร้างไฟล์ที่รันได้ของ Fake FPS Overlay..."

# Install PyInstaller if not already installed
echo "Installing PyInstaller..."
pip install pyinstaller

# Create build directory
mkdir -p dist

# Build GUI version
echo "Building GUI version..."
echo "กำลังสร้างเวอร์ชัน GUI..."
pyinstaller --onefile --windowed --name "FakeFPS-GUI" --distpath "dist" main.py


# Copy config file to dist
cp config.txt dist/

echo "Build complete! Executables are in the 'dist' folder."
echo "สร้างเสร็จแล้ว! ไฟล์ที่รันได้อยู่ในโฟลเดอร์ 'dist'"