#!/usr/bin/env python3
"""
批量上传照片到 Imgur (免费，无需注册)
"""

import os
import json
import requests
import time
import base64
from pathlib import Path

PHOTO_DIR = Path("D:/photo")
OUTPUT_FILE = Path("photo-links.json")

def upload_to_imgur(file_path):
    """上传单张照片到 Imgur"""
    url = "https://api.imgur.com/3/image"

    # 读取图片并转为 base64
    with open(file_path, 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')

    headers = {
        'Authorization': 'Client-ID 546c25a59c58ad7',  # Imgur 公共 client-id
    }

    data = {
        'image': image_data,
        'type': 'base64'
    }

    try:
        response = requests.post(url, headers=headers, data=data, timeout=60)
        result = response.json()

        if result.get('success'):
            return result['data']['link']
        else:
            print(f"  Error: {result.get('data', {}).get('error', 'Unknown')}")
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

        url = upload_to_imgur(file)

        if url:
            # Extract date from filename
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

        # Rate limit
        time.sleep(1)

    # Save results
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump({"photos": photos, "total": len(photos)}, f, ensure_ascii=False, indent=2)

    print("=" * 50)
    print(f"Done! Success: {len(photos)}/{len(photo_files)}")
    print(f"Links saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
