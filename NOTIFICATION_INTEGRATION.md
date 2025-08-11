# JMComic下载通知集成说明

这个文档说明如何配置和使用新的 `download_with_notification.yml` 工作流，实现JMComic下载完成后自动发送通知到notification-service。

## 功能特性

- ✅ 基于原有的 `download_dispatch.yml` 工作流
- ✅ 下载完成后自动触发通知服务
- ✅ 支持将下载的压缩包作为附件传递
- ✅ 支持PDF文件附件传递
- ✅ 可配置的通知内容和目标仓库
- ✅ 文件大小检查（避免超过GitHub API限制）

## 配置步骤

### 1. 设置GitHub Token

在JMComic-Crawler-Python仓库中添加以下Secret：

```
NOTIFICATION_TOKEN
```

这个token需要有以下权限：
- `repo` - 访问仓库
- `workflow` - 触发工作流

**获取Token步骤：**
1. 访问 GitHub Settings > Developer settings > Personal access tokens
2. 创建新的token，选择上述权限
3. 将token添加到JMComic仓库的Secrets中

### 2. 配置notification-service仓库

确保你的notification-service仓库：
- 已经部署了 `.github/workflows/notification-service.yml`
- 配置了相应的通知渠道Secrets（如BARK_PUSH, TG_BOT_TOKEN等）

### 3. 修改工作流参数

在使用工作流时，需要设置以下参数：

#### 必需参数
- `NOTIFICATION_REPO`: 通知服务仓库地址（格式：`username/notification-service`）

#### 可选参数
- `ENABLE_NOTIFICATION`: 是否启用通知（默认：true）
- `NOTIFICATION_TITLE`: 通知标题（默认：'JM漫画下载完成'）

## 使用方法

### 手动触发

1. 进入JMComic-Crawler-Python仓库
2. 点击 Actions > "下载JM本子并发送通知"
3. 点击 "Run workflow"
4. 填写必要参数：
   - 本子ID或章节ID
   - 通知服务仓库地址
   - 其他可选配置

### 参数说明

| 参数名 | 描述 | 默认值 | 必需 |
|--------|------|--------|------|
| JM_ALBUM_IDS | 本子id（多个用-隔开） | - | 否 |
| JM_PHOTO_IDS | 章节id（多个用-隔开） | - | 否 |
| NOTIFICATION_REPO | 通知服务仓库 | your-username/notification-service | 是 |
| ENABLE_NOTIFICATION | 启用通知 | true | 否 |
| NOTIFICATION_TITLE | 通知标题 | JM漫画下载完成 | 否 |
| ENABLE_PDF | 生成PDF | true | 否 |

## 工作流程

1. **下载阶段**：执行原有的漫画下载逻辑
2. **压缩阶段**：创建图片和PDF压缩包
3. **上传阶段**：上传文件到GitHub Artifacts
4. **附件准备**：将压缩包转换为base64格式
5. **通知发送**：通过repository_dispatch触发通知服务
6. **状态记录**：记录通知发送状态

## 附件处理

### 支持的附件类型
- 图片压缩包（.tar.gz）
- PDF压缩包（.zip）

### 文件大小限制
- 单个附件最大1MB（GitHub API限制）
- 超过限制的文件会跳过附件传输，但仍会发送通知

### 附件格式
附件以JSON格式传递：
```json
{
  "filename": "本子.tar.gz",
  "content": "base64编码的文件内容",
  "encoding": "base64",
  "content_type": "application/gzip"
}
```

## 通知内容

通知包含以下信息：
- 📋 任务详情（本子ID、章节ID等）
- 📦 文件信息（压缩包名称、PDF状态）
- 🔗 GitHub Actions链接
- 📎 附件文件（如果大小允许）

## 故障排除

### 常见问题

1. **通知未发送**
   - 检查NOTIFICATION_TOKEN是否正确设置
   - 确认目标仓库地址格式正确
   - 验证token权限是否足够

2. **附件未传递**
   - 检查文件大小是否超过1MB
   - 确认文件是否成功生成
   - 查看工作流日志中的附件准备步骤

3. **通知服务无响应**
   - 检查notification-service仓库的工作流是否正常
   - 确认通知渠道配置是否正确
   - 查看notification-service的执行日志

### 调试方法

1. **查看工作流日志**：
   - JMComic仓库：检查附件准备和通知发送步骤
   - notification-service仓库：检查通知处理过程

2. **测试通知服务**：
   - 可以手动触发notification-service测试通知渠道
   - 使用简单的payload测试repository_dispatch

## 安全注意事项

- NOTIFICATION_TOKEN应该使用最小权限原则
- 不要在日志中暴露敏感信息
- 定期轮换访问token
- 确保notification-service仓库的安全配置

## 扩展功能

可以根据需要扩展以下功能：
- 支持更多文件格式
- 添加下载失败通知
- 集成更多通知渠道
- 支持批量下载通知汇总