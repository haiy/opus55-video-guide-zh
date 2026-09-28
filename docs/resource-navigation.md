# GitHub 与 X 视频制作资源导航

更新：2026-09-28。收录 **34 个 GitHub 项目**、**450 条去重后的 X 原帖入口**。这是公开可发现资料的快照；完整范围与验证方式见[收录方法](METHOD.md)。

[返回中文教程](../README.md) · [X分类目录](x-cases.md) · [提示词定位](prompt-navigation.md) · [按作品选路线](workflow-map.md)

## 先按要做的作品找入口

| 想做什么 | 从哪里开始 | 接下来读什么 |
| --- | --- | --- |
| 复盘本视频里的MV | [anabology原帖](https://x.com/anabology/status/2103534482930491441) → [Donald提示词](https://x.com/donaldjewkes/status/2102801469976248500) | [中文MV总提示词](../README.md#master-prompt) |
| 手绘／水彩音乐MV | 在下方找PDoomVideo、ClaudeAnimationBase、paint-mv-skills | [音乐与歌词准备](../README.md#inputs) |
| 给自己的软件做宣传片 | 在下方找brag、归藏技能、Opus Video Studio | [产品宣传路线](workflow-map.md#product) |
| 科普、讲解与图形动画 | 在下方找Manim、Motion Canvas、Remotion | [科普与图解路线](workflow-map.md#explainer) |
| 先看更多风格 | 在下方找Lemo-Opuscar及案例合集 | [X分类目录](x-cases.md) |
| 找英文原提示词并改成自己的题材 | [提示词定位导航](prompt-navigation.md) | [中文分阶段模板](../README.md#stage-prompts) |

## GitHub 项目

Star为2026-09-28 GitHub API查询快照，各分类内从高到低排列。数量反映关注度，不能代替适用性判断。用途和依赖来自项目自述；本轮未安装或批量运行这些项目。

### 合集与提示词

| 项目 | Star | 有什么／适合做什么 | 使用前看这一点 |
| --- | ---: | --- | --- |
| [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos) | 408 | **案例与提示词索引**：从原帖跳到对应提示词，适合先找视觉参考。 | 查看每条是否为部分提示词；不是统一成片引擎。 |
| [athemeroy/awesome-opus-5-5-videos](https://github.com/athemeroy/awesome-opus-5-5-videos) | 259 | **案例研究与路线分类**：辨别程序绘制、已有素材变换、外部视频生成等不同路线。 | 目录来源为维护者观察，不等于本仓库复现了全部案例。 |
| [opusvideo/awesome-claude-video](https://github.com/opusvideo/awesome-claude-video) | 119 | **案例与工作流合集**：继续寻找作品、原帖和制作流程入口。 | 合集中的展示效果不代表完整工程公开。 |
| [zhuyansen/awesome-claude-video-skills](https://github.com/zhuyansen/awesome-claude-video-skills) | 72 | **制作工具合集**：继续按宣传片、讲解、剪辑、MV等类别扩展找工具。 | 上游评级是维护者判断，本导航不当作运行安全保证。 |
| [joeseesun/opus-video-prompts](https://github.com/joeseesun/opus-video-prompts) | 64 | **中文案例与提示词**：按作品类型寻找中文说明和提示词文件。 | 摘要、部分公开与完整提示词需逐条区分。 |
| [TripoGrowthLab/awesome-opus-5-5-prompts](https://github.com/TripoGrowthLab/awesome-opus-5-5-prompts) | 14 | **视觉案例提示词**：查动画和Three.js视觉实验的参考方向。 | 也含游戏与交互；不是每项都直接输出MP4。 |

### MV源码与制作技能

| 项目 | Star | 有什么／适合做什么 | 使用前看这一点 |
| --- | ---: | --- | --- |
| [latent-spaces/brag](https://github.com/latent-spaces/brag) | 10,893 | **产品发布片技能**：从软件项目或网站内容组织卖点、动效和发布文案。 | 区分经典HyperFrames路线与brag-slim路线。 |
| [mexicat/pdoom-video](https://github.com/mexicat/pdoom-video) | 1,309 | **歌词驱动MV源码**：研究词级时间轴、节拍分析、Three.js场景和离线渲染。 | Bun、Chrome、FFmpeg；音频分析为单独Python步骤。 |
| [JohnHeibel/PDoomVideo](https://github.com/JohnHeibel/PDoomVideo) | 1,291 | **水彩MV源码**：沿着分镜、章节代码和渲染脚本研究一支完整MV。 | 本片灵感链中的前序参考，不是anabology成片的源码。 |
| [JohnHeibel/ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase) | 488 | **角色动画起步工程**：基于角色与笔刷风格做短片，先读动画指南再改题材。 | 适合启动新工程；素材和角色需要按自己的作品调整。 |
| [op7418/guizang-product-video-skill](https://github.com/op7418/guizang-product-video-skill) | 461 | **中文产品宣传片技能**：从真实代码库提取组件、更新和设计风格来做宣传片。 | 更适合已有产品，不是通用歌曲MV模板。 |
| [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 402 | **影片风格与制作指南**：按风格图鉴选样片，再读导演、技术和对应风格说明。 | 使用前核对选定风格所需音源、语音和渲染条件。 |
| [lintsinghua/paint-mv-skills](https://github.com/lintsinghua/paint-mv-skills) | 23 | **水彩MV技能**：输入歌曲与歌词，串起对拍、分镜、章节绘制与导出。 | Node、Chrome、FFmpeg；纯文本歌词对齐另需Python相关依赖。 |
| [makevoid/motion-graphics-music-video-skill](https://github.com/makevoid/motion-graphics-music-video-skill) | 22 | **混合素材MV插件**：歌曲和创意方向驱动素材生成、动画、声音与合成。 | 包含外部图像／视频服务与API费用，不属于纯本地程序绘制。 |
| [petergpt/painted-rickroll](https://github.com/petergpt/painted-rickroll) | 21 | **绘画动画源码**：研究笔触、角色动作、WebAudio配乐及节拍驱动画面。 | 浏览器WebGL2演示；查看项目自己的构建与输出方式。 |
| [opus-pro/opus-video-studio](https://github.com/opus-pro/opus-video-studio) | 5 | **产品视频模板与组件**：按实际产品挑发布片模板和动作组件。 | 看模板自己的任务说明、素材输入与导出要求。 |
| [francozanardi/papermotion](https://github.com/francozanardi/papermotion) | 2 | **纸片动画引擎**：研究剪纸风角色、场景、镜头与代码声音的组织方式。 | 上游标注实验性，先测试一个短镜头。 |

### 动画与视频框架

| 项目 | Star | 有什么／适合做什么 | 使用前看这一点 |
| --- | ---: | --- | --- |
| [mrdoob/three.js](https://github.com/mrdoob/three.js) | 116,000 | **3D与WebGL库**：用于镜头、场景、粒子和三维视觉。 | 浏览器互动效果与离线视频要分清。 |
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | 60,803 | **React视频框架**：用组件和逐帧时间组织字幕、动效与可复用视频。 | 需要React／Node基础；具体使用条件看项目许可。 |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | 53,703 | **HTML视频工具**：把网页式动效、时间线和渲染流程组织成视频。 | 安装和导出以当前官方文档为准。 |
| [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | 41,091 | **Python讲解动画框架**：用于公式、图形、坐标和概念演示的分步表达。 | 叙事和视觉设计仍需自己安排。 |
| [greensock/GSAP](https://github.com/greensock/GSAP) | 28,669 | **动画时间轴库**：编排文字、SVG、界面和DOM属性动画。 | 离线导出需固定时间并配合渲染工具。 |
| [processing/p5.js](https://github.com/processing/p5.js) | 24,057 | **创意绘图库**：在Canvas里编排图形、角色和程序动画。 | 先确定时间函数与导出链，网页播放不等于成片。 |
| [motion-canvas/motion-canvas](https://github.com/motion-canvas/motion-canvas) | 19,186 | **TypeScript动效框架**：制作有明确时间编排的图解、演示和转场。 | 更适合可控图形叙事，而非自动生成写实人物。 |
| [remotion-dev/skills](https://github.com/remotion-dev/skills) | 4,745 | **Remotion技能资料**：给编程助手补充Remotion制作与渲染的项目知识。 | 技能指导与渲染框架分别管理。 |
| [acamposuribe/p5.brush](https://github.com/acamposuribe/p5.brush) | 935 | **p5笔刷扩展**：让代码绘图有笔触、填色和排线质感。 | 它负责绘画风格，时间线与编码需其他工具。 |

### 渲染声音与字幕

| 项目 | Star | 有什么／适合做什么 | 使用前看这一点 |
| --- | ---: | --- | --- |
| [openai/whisper](https://github.com/openai/whisper) | 109,667 | **语音转写**：制作字幕草稿与时间段信息。 | 音乐与歌声可能误识别，必须校对歌词。 |
| [microsoft/playwright](https://github.com/microsoft/playwright) | 96,781 | **浏览器自动化**：按指定时间打开页面、截图和检查实际布局。 | 它是渲染链的一环，不负责自动设计影片。 |
| [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) | 64,590 | **音视频编码与处理**：合成帧、裁剪片段、处理音频和输出MP4。 | 能力取决于本机编译组件；编码前先检查可用滤镜。 |
| [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) | 25,603 | **Whisper推理实现**：在字幕工作流中做本地转写与对齐辅助。 | 设备与模型配置影响效果；不能把ASR当作最终歌词。 |
| [librosa/librosa](https://github.com/librosa/librosa) | 8,634 | **音乐分析**：计算节拍、起音、频谱与能量，为画面时间轴提供依据。 | 分析结果需要结合真实听感校准。 |

### 源码案例补充

| 项目 | Star | 有什么／适合做什么 | 使用前看这一点 |
| --- | ---: | --- | --- |
| [riba2534/claude-opus-5-5-demo](https://github.com/riba2534/claude-opus-5-5-demo) | 846 | **3D交互源码案例**：观察Three.js场景、动作与提示词如何对应。 | 这是可玩网页项目，做视频还需另行录制或渲染。 |
| [Aureliengmz/clearwater](https://github.com/Aureliengmz/clearwater) | 474 | **实时水面视觉源码**：研究单HTML的水面、光照、镜头与时间控制。 | 属于实时视觉示范，不是成片制作流水线。 |
| [WinterArc21/Battle-of-Austerlitz-Film](https://github.com/WinterArc21/Battle-of-Austerlitz-Film) | 10 | **历史叙事片源码**：研究较长WebGL叙事片的场景、旁白和字幕组织。 | 表现形式可参考；历史事实应另行核对。 |

## 本片最相关的 X 入口

| 作者／入口 | 看什么 | 资料类型 |
| --- | --- | --- |
| [anabology MV](https://x.com/anabology/status/2103534482930491441) | 本片展示作品；作者提及Donald提示词、Midjourney及参考板 | 作品与制作说明 |
| [Donald MV发布帖](https://x.com/donaldjewkes/status/2102801274173587569) | 看作品发布与提示词来源链 | 作品发布 |
| [Donald提示词帖](https://x.com/donaldjewkes/status/2102801469976248500) | 阅读原作者长提示词，再对照自己的素材和工具 | 提示词入口 |
| [JAZII模型对比](https://x.com/notjazii/status/2103884167104831573) | 用户指定的同提示词动画比较案例 | 展示帖，未确认完整实验提示词 |
| [Deedy产品发布片](https://x.com/deedydas/status/2102787937482252537) | 从一个清楚的产品方向开始组织宣传片 | 上游收录的短提示词案例 |
| [WY历史线稿](https://x.com/akokoi1/status/2102583898865873225) | 中文主题、线稿风格和较长叙事的需求写法 | 上游收录的中文案例 |
| [Stephan动态设计](https://x.com/stephanlivera/status/2103315922098470926) | 紧凑的动效作品集需求 | 上游收录的动效案例 |
| [zero UI动效](https://x.com/twoclipping/status/2103273003555402193) | 连续形态变换与UI视觉编排 | 上游收录的产品动效案例 |
| [Gavin纪录片](https://x.com/gavinpurcell/status/2103304514329854102) | 较长作品的素材与叙事流程 | 上游收录，不能直接归为纯代码绘制 |
| [gregpr07素材剪辑](https://x.com/gregpr07/status/2102984873351037161) | 已有视频素材参与的编排思路 | 素材剪辑案例 |
更多原帖按类别进入 [X完整索引](x-cases.md)。帖子可能需要登录或后来被删除；不把一次抓取403当作帖子不存在。

## 下一步

拿到一个案例后，先确认有没有原始提示词、素材输入和可运行工程，再做10—15秒样片。需要从头组织需求，直接用[中文需求单](../README.md#inputs)和[总提示词](../README.md#master-prompt)。
