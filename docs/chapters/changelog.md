## 4.1.0

此版本主要面向标注人员，提供了一些新功能、性能提升和改进。

### 新功能：

- 目标检测：
  - 支持检测框自动贴边
  - 超出边界
  - 辅助框模式
- 图像分类：
  - 支持拖拽模式选择图片
  - 支持shift多选
- 数据集：
  - 支持在数据集模块中进行质检
  - 支持释放数据给其他标注员进行标注
  - 支持[IF_DATA](./if_data.md)格式解析、导出
- 项目管理：
  - 支持指定人员进行标注
  - 支持交互设置

### 优化

- 图像分割
  - 引入高性能图形渲染组件，解决大量掩膜渲染问题
- 数据集
  - 全面优化数据集解析速度



## 4.0.0

### 新功能：

- 支持[图像分类](./classification.md)
- 支持批量标注
- 支持预标注多级标签导入

### 优化:

- 全面提升标注相关查询速度，优化标注体验
- 提升数据加载性能

### 修复:

- zip包中包含中文小概率发生乱码问题