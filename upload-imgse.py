#!/usr/bin/env python3
"""
批量上传照片到路过图床 (imgse.com)
国内服务，速度快
"""

import os
import json
import requests
import time
from pathlib import Path

PHOTO_DIR = Path("D:/photo")
OUTPUT_FILE = Path("photo-links.json")

def upload_to_imgse(file_path):
    """上传单张照片到路过图床"""
    url = "https://imgse.com/api/upload"

    with open(file_path, 'rb') as f:
        files = {'image': (os.path.basename(file_path), f, 'image/jpeg')}

        try:
            response = requests.post(url, files=files, timeout=30)
            data = response.json()

            if data.get('success'):
                return data['data']['url']
            else:
                print(f"  Error: {data.get('message', 'Unknown')}")
                return None
        except Exception as e:
            print(f"  Exception: {e}")
            return None

def main():
    photos = []
    photo_files = sorted(PHOTO_DIR.glob("IMG_*.jpg"))

    print(f"Found {len(photo_files)} photos")
    print("=" * 50)

    for i, file in enumerate(photo_files, 1):
        print(f"[{i}/{len(photo_files)}] Uploading: {file.name}")

        url = upload_to_imgse(file)

        if url:
            name_parts = file.stem.split('_')
            if len(name_parts) >= 2:
                date_str = name_parts[1]
                year = date_str[:4]
                month = date_str[4:6]
                day = date_str[6:8]
            else:
                year, month, day = "0000", "00", "00"

            photos.append({
                "name": file.name,
                "url": url,
                "year": year,
                "month": month,
                "day": day,
                "date": f"{year}-{month}-{day}"
            })
            print(f"  OK: {url}")
        else:
            print(f"  FAILED")

        time.sleep(0.5)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump({"photos": photos, "total": len(photos)}, f, ensure_ascii=False, indent=2)

    print("=" * 50)
    print(f"Done! Success: {len(photos)}/{len(photo_files)}")
    print(f"Links saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
