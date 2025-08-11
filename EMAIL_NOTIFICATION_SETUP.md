# JM漫画下载邮件通知设置指南

## 概述

新的 `download_with_email.yml` 工作流在原有下载功能基础上，增加了邮件附件发送功能。下载完成后，会自动将压缩文件（tar.gz和zip）作为邮件附件发送到您的邮箱。

## 功能特点

- ✅ 支持大附件发送（自动分割超过20MB的文件）
- ✅ 支持多种发送方式（通过notification-service或直接SMTP）
- ✅ 自动处理图片和PDF压缩文件
- ✅ 完整的错误处理和日志记录
- ✅ 临时文件自动清理

## 配置方法

### 必需的Secrets配置

在GitHub仓库的 Settings > Secrets and variables > Actions 中添加以下secrets：

```
# JM登录信息
JM_USERNAME=your_jm_username
JM_PASSWORD=your_jm_password

# SMTP邮件配置
SMTP_SERVER=smtp.gmail.com
SMTP_SSL=true
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_app_password
SMTP_NAME=JM漫画下载服务


```

## 常用邮件服务器配置

### Gmail
```
SMTP_SERVER=smtp.gmail.com
SMTP_SSL=true
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_app_password  # 需要开启两步验证并生成应用专用密码
```

### QQ邮箱
```
SMTP_SERVER=smtp.qq.com
SMTP_SSL=true
SMTP_EMAIL=your_email@qq.com
SMTP_PASSWORD=your_authorization_code  # 需要开启SMTP服务并获取授权码
```

### 163邮箱
```
SMTP_SERVER=smtp.163.com
SMTP_SSL=true
SMTP_EMAIL=your_email@163.com
SMTP_PASSWORD=your_authorization_code  # 需要开启SMTP服务并获取授权码
```

### Outlook/Hotmail
```
SMTP_SERVER=smtp-mail.outlook.com
SMTP_SSL=true
SMTP_EMAIL=your_email@outlook.com
SMTP_PASSWORD=your_password
```

## 使用方法

1. 在GitHub仓库页面，点击 "Actions" 标签
2. 选择 "下载JM本子并发送邮件 (dispatch)" 工作流
3. 点击 "Run workflow" 按钮
4. 填入相关参数：
   - **JM_ALBUM_IDS**: 本子ID（必填）
   - **EMAIL_TITLE**: 邮件标题（可选，默认：JM漫画下载完成）
   - **EMAIL_CONTENT**: 邮件内容（可选）
   - 其他参数与原工作流相同
5. 点击 "Run workflow" 开始执行

## 大附件处理

### 自动分割机制

- 单个文件超过20MB时，会自动分割为多个小文件
- 分割后的文件命名格式：`原文件名.part001.扩展名`
- 每个分割文件不超过20MB

### 分批发送机制

- 如果总附件大小超过25MB，会分多批次发送邮件
- 每批次邮件标题会标注：`原标题 (第1批，共3批)`
- 每批次邮件内容会说明包含的文件数量

## 工作流程

1. **下载阶段**: 执行原有的JM漫画下载逻辑
2. **压缩阶段**: 创建tar.gz和zip压缩文件
3. **上传阶段**: 上传到GitHub Actions artifacts
4. **邮件准备**: 复制压缩文件到临时目录
5. **邮件发送**: 根据配置选择发送方式
6. **清理阶段**: 删除临时文件

## 故障排除

### 常见问题

1. **邮件发送失败**
   - 检查SMTP配置是否正确
   - 确认邮箱服务商是否开启SMTP服务
   - 验证用户名和密码/授权码是否正确

2. **附件过大**
   - 系统会自动分割大文件
   - 如果仍然失败，可能是邮件服务商限制
   - 建议使用支持大附件的邮件服务

3. **GitHub Token权限不足**
   - 确保Token有repo权限
   - 检查NOTIFICATION_REPO是否正确

### 调试方法

1. 查看GitHub Actions运行日志
2. 检查"准备邮件附件"步骤的输出
3. 查看邮件发送步骤的详细错误信息

## 安全注意事项

1. **Secrets安全**
   - 不要在代码中硬编码敏感信息
   - 定期更换密码和Token
   - 使用应用专用密码而非主密码

2. **权限控制**
   - GitHub Token使用最小权限原则
   - 定期检查Token的使用情况

3. **邮件安全**
   - 建议使用专用邮箱账户
   - 开启邮箱的安全验证功能

## 高级配置

### 自定义邮件内容

可以在工作流输入中自定义邮件标题和内容：

```
EMAIL_TITLE: "🎉 您的JM漫画下载完成啦！"
EMAIL_CONTENT: |
  亲爱的用户，
  
  您请求的JM漫画已经下载完成，请查看邮件附件。
  
  下载信息：
  - 下载时间：$(date)
  - 文件格式：tar.gz 和 PDF
  
  感谢使用我们的服务！
```

### 条件发送

可以通过修改工作流，添加条件判断：

```yaml
- name: 发送邮件通知
  if: success() && env.SMTP_EMAIL != ''  # 只在成功且配置了邮箱时发送
```

## 更新日志

- **v1.0**: 初始版本，支持基本邮件附件发送
- **v1.1**: 添加大附件分割和分批发送功能
- **v1.2**: 支持两种发送方式（notification-service和直接SMTP）

## 技术支持

如有问题，请：
1. 查看GitHub Actions运行日志
2. 参考notification-service文档
3. 在Issues中提交问题报告