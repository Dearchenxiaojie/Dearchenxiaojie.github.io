#!/usr/bin/env python3
"""
批量上传照片到 SM.MS 图床
"""

import os
import json
import requests
import time
from pathlib import Path

PHOTO_DIR = Path("D:/photo")
OUTPUT_FILE = Path("photo-links.json")

def upload_to_smms(file_path):
    """上传单张照片到 SM.MS"""
    url = "https://sm.ms/api/v2/upload"

    with open(file_path, 'rb') as f:
        files = {'smfile': (os.path.basename(file_path), f)}
        try:
            response = requests.post(url, files=files, timeout=30)
            data = response.json()

            if data.get('success'):
                return data['data']['url']
            elif data.get('code') == 'image_repeated':
                # 图片已存在，返回已有 URL
                return data.get('images', data.get('data', {}).get('url'))
            else:
                print(f"  Error: {data.get('message', 'Unknown error')}")
                return None
        except Exception as e:
            print(f"  Exception: {e}")
            return None

def main():
    photos = []
    photo_files = sorted(PHOTO_DIR.glob("IMG_*.jpg"))

    print(f"找到 {len(photo_files)} 张照片")
    print("=" * 50)

    for i, file in enumerate(photo_files, 1):
        print(f"[{i}/{len(photo_files)}] 上传: {file.name}")

        url = upload_to_smms(file)

        if url:
            # 从文件名提取日期信息
            # 格式: IMG_YYYYMMDD_HHMMSS.jpg
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
            print(f"  ✓ 成功: {url}")
        else:
            print(f"  ✗ 失败")

        # 避免请求过快
        time.sleep(0.5)

    # 保存结果
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump({"photos": photos, "total": len(photos)}, f, ensure_ascii=False, indent=2)

    print("=" * 50)
    print(f"上传完成！成功: {len(photos)}/{len(photo_files)}")
    print(f"链接保存到: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
