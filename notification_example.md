# 快速配置示例

## 1. 设置GitHub Token

在JMComic-Crawler-Python仓库的Settings > Secrets and variables > Actions中添加：

```
Name: NOTIFICATION_TOKEN
Value: ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## 2. 使用示例

### 基本使用
```yaml
# 在GitHub Actions界面填写：
JM_ALBUM_IDS: "123456"
NOTIFICATION_REPO: "your-username/notification-service"
ENABLE_NOTIFICATION: true
```

### 批量下载
```yaml
JM_ALBUM_IDS: "123456-789012-345678"
NOTIFICATION_REPO: "your-username/notification-service"
NOTIFICATION_TITLE: "批量下载完成"
ENABLE_PDF: true
```

## 3. 通知效果预览

当下载完成后，你会收到类似这样的通知：

```
标题：JM漫画下载完成

内容：
JM漫画下载任务已完成！

📋 任务详情：
- 本子ID: 123456
- 章节ID: 未指定
- 压缩包: 本子.tar.gz
- PDF文件: 本子PDF.zip
- 执行时间: 1234567890

🔗 查看详情: https://github.com/your-username/JMComic-Crawler-Python/actions/runs/1234567890

附件：本子.tar.gz, 本子PDF.zip
```

## 4. 常用配置组合

### 只下载图片，发送简单通知
```yaml
JM_ALBUM_IDS: "123456"
ENABLE_PDF: false
NOTIFICATION_REPO: "your-username/notification-service"
NOTIFICATION_TITLE: "漫画下载完成"
```

### 下载PDF，自定义文件名
```yaml
JM_ALBUM_IDS: "123456"
ENABLE_PDF: true
ZIP_NAME: "我的漫画.tar.gz"
PDF_ZIP_NAME: "我的漫画PDF.zip"
NOTIFICATION_REPO: "your-username/notification-service"
NOTIFICATION_TITLE: "我的漫画下载完成"
```