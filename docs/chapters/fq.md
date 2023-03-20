# 常见问题

## 为什么我的项目显示数据解析失败？

请检查你的数据集是否符合规范，如果不符合规范，请参考[VOC数据集格式](./chapters/voc.md)与 [COCO数据集格式](./chapters/coco.md)进行修改。

## 为什么标注历史页面中的数据减少了？

标注历史中只包含质检合格的数据，如果标注的数据被质检员标记为不合格，那么这些图片将会被重新标注，标注历史中的数据将会减少。