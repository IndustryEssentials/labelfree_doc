coco数据集官网：https://cocodataset.org/#format-data

labelfree扩展信息

- shape：图形类型
- meta：元数据
  - annotator：标注员数据
  - points：点、线数据
  - result_type：结果类型，ground_truth为实际结果,consensus_test为一致性测试结果


```
{==
           "shape": "point",                            // 图形类型
            "meta": {                                    // labelfree 元数据
                "annotator": "labeluser@qq.com",         // 标注员数据
                "points": [{"x":100, "y": 120}],         // 点数据
                "result_type": "consensus_test",         // ground_truth为实际结果,consensus_test为一致性测试结果
            }
==}
```



## 目录结构

```JSON
coco
  ├── annotations
  │   ├── stuff_train2014.json
  │   ├── stuff_train2017.json
  │   ├── stuff_val2014.json
  │   ├── stuff_val2017.json
  │   |   ...
  ├── train2017
  │   ├── 000000000009.jpg
  │   ├── 000000580008.jpg
  │   |   ...
  ├── val2017
  │   ├── 000000000139.jpg
  │   ├── 000000000285.jpg
  │   |   ...
  |   ...
```

Demo:

```JSON
{
        "info": {
            "contributor": "...",
            "about": "...",
            "date_created": "...",
            "description": "...",
            "url": "...",
            "version": "1.0",
            "year": 2020
        },

        "categories": [
            {"supercategory": "person","id": 1,"name": "person"},
            {"supercategory": "vehicle","id": 2,"name": "bicycle"},
            {"supercategory": "vehicle","id": 3,"name": "car"},
            {"supercategory": "vehicle","id": 4,"name": "motorcycle"},
            {"supercategory": "vehicle","id": 5,"name": "airplane"},        
        ],
    
        "images": [
            {
                "id": 20289,
                "file_name": "000000020289.jpg",
                "width": 300,
                "height": 300
            },
            {
                "id": 45176,
                "file_name": "000000045176.jpg",
                "width": 300,
                "height": 300
            }
        ],

        "annotations": [
            {
                "id": 377545,
                "image_id": 44153, 
                "segmentation": [
                        [152.0, 180.0, 156.0, 176.0, 160.0, 181.0, 156.0, 186.0, 152.0, 180.0]
                ],
                "area": 42.0,
                "bbox": [152.0, 152.0, 28.0, 8.0],
                "category_id": 100,
                "iscrowd": 0
            }, 
            {
                "id": 446305,
                "image_id": 52178,
                "segmentation": [
                        [257, 123, 243, 123, 243, 112, 257, 112, 257, 123]
                ],
                "area": 154.0,
                "bbox": [123, 243, 134, 14],
                "category_id": 100,
                "iscrowd": 0,
                "shape": "point",
                "meta": {
                    "annotator": "labeluser@qq.com",
                    "points": [{"x":100, "y": 120}]
                }
            }
        ]
}
```

## Annotation文件格式

### 总体格式：

```JSON
{
    "info":  info,               // 字典,图片基本信息，时间，版本，贡献者，可为空
    "licenses":  [license],      //列表，内容为字典，版权许可证，可为空
    "images":[image],            // 列表，内容为字典
    "annotations":[annotation],  // 列表，内容为字典
    "categories":[category]      // 列表，内容为字典，列表长度等同于数据集类别的数
}
```

### info内容：

```JSON
 "info": 
        {
        "description": "COCO 2017 Dataset",     // 描述
        "url": "http://cocodataset.org",        // 图片地址
        "version": "1.0",                       // 版本
        "year": 2017,                           // 年份
        "contributor": "COCO Consortium",       // 贡献者
        "date_created": "2017/09/01"            // 创建时间
    }
```

### license内容：

```JSON
"licenses": [
        {
            "url": "http://creativecommons.org/licenses/by-nc-sa/2.0/",  // 许可证网路路径
            "id": 1,                                                     // 许可证ID
            "name": "Attribution-NonCommercial-ShareAlike License"       // 许可证名称
        }]
        
```

### images内容：

```JSON
   "images": 
        [{
            "license": 4,                                            // license id
            "file_name": "000000397133.jpg",                         //图片文件名 
            "coco_url": "http://labelfree.com/val2017/397133.jpg",   //图片网络地址路径
            "height": 427,                                           // 图像高度
            "width": 640,                                            // 图像宽度
            "date_captured": "2013-11-14 17:02:52",                  //拍摄日期
            "flickr_url": "http://ickr.com/6116/2c9e_z.jpg",         // flickr网络地址
            "id": 397133                                             //图片的身份ID
        }] 
```

### categories内容：

```JSON
"categories":
[
    {
    "supercategory":"person",      // 主类名
    "id":1,                        // 标签类别ID
    "name":"person"                // 子类名
    }
]
```

### annotation内容：


```JSON
 "annotations":[
            {
            "segmentation": [
                [
                    510.66,
                    423.01,
                    511.72,
                    ...
                    423.01,
                    510.45,
                    423.01
                ]                                        // 分割信息
            ],
            "area": 702.1057499999998,                   //segmentation的面积
            "iscrowd": 0,                                // 0：多边形 1: rle编码的mask
            "image_id": 289343,                          // 图片的身份ID
            "bbox":[
                473.07,
                395.93,
                38.65,
                28.67],                                  // 目标框位置 [x,y,width,height]
            "category_id": 18,                           // 标签类别ID
            "id": 1768,                                  // 框的身份编号
            "shape": "point",                            // 图形类型
            "meta": {                                    // labelfree 元数据
                "annotator": "labeluser@qq.com",         // 标注员数据
                "points": [{"x":100, "y": 120}],         // 点数据
                "result_type": "consensus_test",         // ground_truth为实际结果,consensus_test为一致性测试结果
            }
        }]
```

### segmentation内容

#### 多边形

- "iscrowd": 0 

```JSON
"segmentation": [
    [
        289.74,
        443.39,
        289.74,
        443.39
    ],
    [
        289.74,
        443.39,
        289.74,
        443.39
    ]
]
```

#### 掩膜

- "iscrowd": 1 

```JSON
 "segmentation": {
            "size": [300, 300],
            "counts": "`l>Y1R83N1O00O10000001OO1000000000000000000000000000000000000000000O10O10000000000000000000000000001O0000000000000000000000000000000000000000000000O10000000000001O00000000000000000001O0000000O10000000000000000000000000000000000000000000000001O00000000000000000000000000000000000000001O000001O000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000d1"
        },
```