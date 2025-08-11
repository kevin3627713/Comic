# 邮件附件功能使用说明

## 功能概述

修改后的 `download_dispatch.yml` 工作流现在支持在邮件中发送生成的压缩包作为附件，包括：
- 图片的 tar.gz 压缩包
- PDF 的 zip 压缩包

## 配置要求

### 1. GitHub Secrets 配置

在 GitHub 仓库的 Settings > Secrets and variables > Actions 中配置以下 secrets：

```
EMAIL_FROM: 发件人邮箱（如：your_email@qq.com）
EMAIL_TO: 收件人邮箱（如：recipient@example.com）
EMAIL_PASS: 邮箱授权码（不是密码！）
EMAIL_TITLE: 邮件标题（可选）
EMAIL_CONTENT: 邮件内容（可选）
```

### 2. 工作流参数

运行工作流时，可以设置以下参数：

- `SEND_EMAIL_ATTACHMENTS`: 是否发送附件（默认：true）
- `ZIP_NAME`: 图片压缩包文件名（默认：本子.tar.gz）
- `PDF_ZIP_NAME`: PDF压缩包文件名（默认：本子PDF.zip）

## 功能特性

### 1. 智能附件检测
- 自动检测生成的压缩包文件
- 只发送存在的文件作为附件
- 如果文件不存在，会记录警告但不影响邮件发送

### 2. 多重发送策略
- 优先使用 commonX 包的邮件功能
- 如果不支持附件，自动回退到内置 SMTP 实现
- 支持 QQ 邮箱的 SMTP 发送

### 3. 灵活控制
- 可以通过 `SEND_EMAIL_ATTACHMENTS` 参数控制是否发送附件
- 支持只发送通知邮件而不包含附件

## 使用示例

### 发送带附件的邮件
```yaml
# 在工作流运行时设置
SEND_EMAIL_ATTACHMENTS: true
ZIP_NAME: "我的漫画.tar.gz"
PDF_ZIP_NAME: "我的漫画PDF.zip"
```

### 只发送通知邮件
```yaml
# 在工作流运行时设置
SEND_EMAIL_ATTACHMENTS: false
```

## 注意事项

1. **邮箱授权码**：`EMAIL_PASS` 应该是邮箱的授权码，不是登录密码
2. **文件大小限制**：邮件附件有大小限制，通常不超过 25MB
3. **网络环境**：GitHub Actions 环境需要能够访问 SMTP 服务器
4. **安全性**：所有敏感信息都通过 GitHub Secrets 管理，不会在日志中泄露

## 故障排除

如果邮件发送失败，检查以下项目：
1. 邮箱授权码是否正确
2. 发件人邮箱是否开启了 SMTP 服务
3. 网络连接是否正常
4. 附件文件是否存在且大小合理

## 技术实现

- 使用 Python 的 `smtplib` 和 `email` 模块
- 支持 MIME 多部分邮件格式
- 自动处理文件编码和附件头信息
- 兼容现有的 commonX 邮件功能