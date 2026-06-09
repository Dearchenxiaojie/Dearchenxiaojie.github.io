#!/bin/bash

# SM.MS 图床上传脚本
# 使用方法: bash upload-photos.sh

PHOTO_DIR="D:/photo"
OUTPUT_FILE="photo-links.json"

echo '{"photos":[' > "$OUTPUT_FILE"

first=true
for file in "$PHOTO_DIR"/IMG_*.jpg; do
    filename=$(basename "$file")
    echo "上传: $filename"

    # 上传到 SM.MS
    response=$(curl -s -X POST \
        -H "Content-Type: multipart/form-data" \
        -F "smfile=@$file" \
        "https://sm.ms/api/v2/upload")

    # 提取 URL
    url=$(echo "$response" | grep -o '"url":"[^"]*"' | cut -d'"' -f4)

    if [ -n "$url" ]; then
        if [ "$first" = true ]; then
            first=false
        else
            echo "," >> "$OUTPUT_FILE"
        fi
        echo "  {\"name\":\"$filename\",\"url\":\"$url\"}" >> "$OUTPUT_FILE"
        echo "  ✓ 成功: $url"
    else
        echo "  ✗ 失败: $filename"
    fi

    # 避免请求过快
    sleep 1
done

echo ']}' >> "$OUTPUT_FILE"

echo ""
echo "上传完成！链接保存到: $OUTPUT_FILE"
