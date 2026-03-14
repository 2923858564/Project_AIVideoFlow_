# 项目名称：基于 ComfyUI 的全自动多模态 AI 视频生产流
**Project: Automated Multimodal AI Video Production Pipeline via ComfyUI**

---

## 📖 项目简介 (Project Overview)

本项目旨在解决 AI 视频创作中素材获取繁琐与语义意境对齐难的痛点。通过自研脚本与 ComfyUI 的深度集成，构建了一套从网页端原始素材抓取到高质量视频生成的全自动流水线。

项目核心亮点在于**"解耦式设计"**：将图片截图任务拆分为"视觉主体"与"背景语义"两部分，利用 OCR 与大模型 (LLM) 协同完成提示词工程，确保生成的视频既保留了原图的神韵，又精准复现了文字描述的意念。

---

## 🛠 技术架构 (Technical Architecture)

该工作流由四个关键层级组成：

### **数据采集层 (Data Acquisition)**
- **工具**: Python脚本
- **功能**: 自动化获取目标网站的光锥图片及其对应的背景描述文本
- **输出**: 原始截图 + 关联文本数据

### **视觉处理层 (Visual Processing)**
- **核心节点**: `Image Crop`
- **处理流程**:
  1. 将截图解耦为两部分
  2. 立绘部分 → 视频生成链路
  3. 文字部分 → OCR 识别链路

### **认知理解层 (Cognitive Understanding)**
- **OCR 引擎**: Florence-2
  - 负责精准 OCR 识别
  - 提取复杂排版中的背景故事
- **语义理解**: LLM 节点 (GPT)
  - 将原始 OCR 文本加工、改写
  - 生成符合视频生成逻辑的 Prompt

### **合成生成层 (Video Synthesis)**
- **视频模型**: SVD (Stable Video Diffusion)
- **生成机制**:
  - 输入: 原图立绘 (Image Hint) + LLM 生成的动态描述 (Prompt)
  - 输出: 高动态视频合成

---

## 🚀 核心功能与特性 (Key Features)

### **全流程自动化**
- 实现从 URL 输入到 MP4 产出的零人工干预闭环

### **语义解耦技术**
- 独立处理视觉与文本信息流
- 有效解决了传统图生视频中提示词污染或引导不足的问题

### **智能提示词工程**
- 引入 LLM 对 OCR 结果进行"视觉化翻译"
- 将枯燥的游戏数值/背景转化为充满动感的画面描述词
- 支持自定义提示词模板

### **可调式风格化**
- 支持在 ComfyUI 中一键切换采样器与 LoRA
- 实现视频质量与风格的快速迭代
- 模块化设计，便于扩展新模型

---

## 📈 效果展示 (Showcase)

| 阶段 | 输入/处理 | 输出结果 |
|------|-----------|----------|
| **原始素材** | 光锥截图 | ![img](file:///C:\Users\Mamihlapinatapai\AppData\Roaming\Tencent\Users\2923858564\QQ\WinTemp\RichOle\3TX3Z3YWT2IET9_ZJ[G7L7Q.png) |
| **OCR 识别** | 文字区域 | `"A girl manipulating glowing cosmic strings..." |
| **LLM 加工** | 提示词生成 | **Prompt:** > High-quality anime style, a girl with silver hair and glowing purple eyes staring at the camera. She is manipulating intricate, glowing cosmic strings that resemble a web of fate. In the foreground, a vibrant orange flame flickers intensely with heat distortion. The background is a deep blue mystical void filled with swirling magical particles and ethereal butterfly-like light effects. Cinematic lighting, slow motion, hair and silk ribbons flowing gently in the wind, mystical atmosphere, 4k, highly detailed.` |
| **视频生成** | SVD 模型 | "D:\360MoveData\Users\Mamihlapinatapai\Desktop\Project_AIVideoFlow_易学\_Showcase_Videos\爻光.mp4" |

## 
