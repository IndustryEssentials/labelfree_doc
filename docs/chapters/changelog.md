## 4.4.0
### 新功能：

1. 目标检测支持[多模态标注](./note.md)；
2. 标注与数据集预览页面图片排序逻辑变更，现按照名称升序排列（linux系统规则）；
3. 支持大分辨率（20000*10000）图片目标检测与分类标注；

## 4.2.1更新内容

此版本主要面向标注人员，提供了一些新功能、性能提升和改进。

### 新功能：


1.  支持**Segment Anything Model**进行分割辅助标注
2.  全新帮助文档模块，提供更加详细的使用指南
3.  新支持点、线类型数据标注
  
### 优化

1. 数据集
    -  支持缩放
    -  标注历史逻辑优化，以操作时间排序

2.  图像分类：
    - 支持以子目录名作为预标注导入
    - 单标签操作后自动取消选中


3. 问题中心：
    - 支持问题点拖拽式标记



## 4.1.0

此版本主要面向标注人员，提供了一些新功能、性能提升和改进。

### 新功能：


1.  目标检测：
  
    - 支持检测框自动贴边
    - 超出边界
    - 辅助框模式
  
2.  图像分类：
  
    - 支持拖拽模式选择图片
    - 支持shift多选
  
3.  数据集：
  
    * 支持在数据集模块中进行质检
    * 支持释放数据给其他标注员进行标注
    * 支持[IF_DATA](./if_data.md)格式解析、导出
  
4.  项目管理：

    - 支持指定人员进行标注

    - 支持交互设置

### 优化


1.  图像分割

    -  引入高性能图形渲染组件，解决大量掩膜渲染问题

  
2.  数据集
  
    -  全面优化数据集解析速度

3.  部署
  
    -  支持windows环境下[exe部署](./exe_install.md)
    -  支持单容器docekr部署


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
