# 照片上传指南

## 方案1：使用路过图床 (推荐)

1. 访问 https://imgse.com
2. 批量上传照片
3. 复制图片链接
4. 更新 `docs/.vitepress/theme/photos.json`

## 方案2：使用 SM.MS

1. 访问 https://sm.ms
2. 注册账号获取 API Token
3. 使用脚本批量上传

## 方案3：压缩照片后直接放仓库

```bash
# 安装 ImageMagick
# 然后压缩照片到 200KB 以内
mogrify -resize 1200x1200 -quality 75 D:/photo/*.jpg
```

## 当前照片统计

- 总数: 81 张
- 总大小: 388MB
- 时间范围: 2023年4月 - 2025年9月

## 相册页面数据格式

```json
{
  "photos": [
    {
      "name": "IMG_20250916_094627.jpg",
      "url": "https://xxx.com/image.jpg",
      "year": "2025",
      "month": "09",
      "day": "16",
      "date": "2025-09-16"
    }
  ]
}
```
