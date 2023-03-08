if_data（待取名） 是一个目录结构相对自由数据集格式。

- 图像与标注在同一级目录下
- 支持多级目录数据集

目录结构：

```Nginx
if_data.zip
 └── if_data
     ├── 1.jpg
     ├── 1.xml
     ├── 2.jpg
     ├── 2.xml
     ├── 3.jpg
     ├── 3.xml
     ├── sub_data1
     │   ├── 1.jpg
     │   ├── 1.xml
     │   ├── 2.jpg
     │   ├── 2.xml
     │   ├── 3.jpg
     │   ├── 3.xml
     │   └── sub_data2
     │       ├── 1.jpg
     │       ├── 1.xml
     │       ├── 2.jpg
     │       ├── 2.xml
     │       ├── 3.jpg
     │       └── 3.xml
     └── sub_data2
         ├── 1.jpg
         ├── 1.xml
         ├── 2.jpg
         ├── 2.xml
         ├── 3.jpg
         └── 3.xml
```

支持的标注类型：

- 目标检测、分类 voc
- 图像分割 coco