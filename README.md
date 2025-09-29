# Website (static) - deploy to AWS S3

本文件包含将 `index.html` 部署到 AWS S3 的基本步骤（Console 或 CLI）。

## 快速 CLI 部署示例
1. 本地安装并配置 AWS CLI (`aws configure`)
2. 创建 bucket（替换为唯一的 bucket 名称）
   ```
   aws s3 mb s3://your-unique-bucket-name --region us-east-1
   ```
3. 上传网站文件
   ```
   aws s3 cp index.html s3://your-unique-bucket-name/ --acl public-read
   ```
4. 在 S3 控制台启用「静态网站托管」，设置 Index document 为 `index.html`
5. 配置 bucket policy 允许公有读取（或通过控制台设置对象为 public）

请参考 AWS 控制台的操作界面完成最后两步（启用静态网站托管与设置 Bucket Policy）。
