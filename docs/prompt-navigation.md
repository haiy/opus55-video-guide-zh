# 提示词与制作指南定位

[返回导航](resource-navigation.md) · [中文MV总提示词](../README.md#master-prompt) · [分阶段模板](../README.md#stage-prompts)

## 本片来源链

1. [anabology作品与说明](https://x.com/anabology/status/2103534482930491441)。
2. [Donald作品帖](https://x.com/donaldjewkes/status/2102801274173587569) → [作者长提示词](https://x.com/donaldjewkes/status/2102801469976248500)。
3. [社区收录的对应提示词](https://github.com/yihui-dev/awesome-opus5-5-videos/blob/1c092195b7bda246455827bc0be820be6d6a7b97/prompts/anabology-491441.md)。
4. [本仓库重新编排的中文模板](../README.md#master-prompt)。

中文模板是实操改编，不是原帖逐字翻译；社区收录不等于作者官方源码。JAZII对比帖仍作为观察案例，未把未公开实验提示词写成已获得。

## 18个按题材定位的提示词入口

以下为joeseesun合集的固定提交文件入口。文件可能是原文、部分原文、转述或摘要，打开后以各自说明与原帖为准，不把18个文件统称为18份完整原始提示词。

| 题材 | 提示词文件 |
| --- | --- |
| 推理公司发布片 | [打开收录文件](https://github.com/joeseesun/opus-video-prompts/blob/7977c807781d4ba7c235247b8899a72575a30d00/prompts/01-inference-startup-launch.md) |
| 15秒动效展示 | [打开收录文件](https://github.com/joeseesun/opus-video-prompts/blob/7977c807781d4ba7c235247b8899a72575a30d00/prompts/02-motion-showreel-15s.md) |
| 中国历史线稿 | [打开收录文件](https://github.com/joeseesun/opus-video-prompts/blob/7977c807781d4ba7c235247b8899a72575a30d00/prompts/03-china-5000-years-lineart.md) |
| 复古广告方向 | [打开收录文件](https://github.com/joeseesun/opus-video-prompts/blob/7977c807781d4ba7c235247b8899a72575a30d00/prompts/04-opus-1984-ad.md) |
| Transformer讲解 | [打开收录文件](https://github.com/joeseesun/opus-video-prompts/blob/7977c807781d4ba7c235247b8899a72575a30d00/prompts/05-transformer-explainer-js.md) |
| 连续尺度推进 | [打开收录文件](https://github.com/joeseesun/opus-video-prompts/blob/7977c807781d4ba7c235247b8899a72575a30d00/prompts/06-room-to-quarks-zoom.md) |
| 企业讲解结构 | [打开收录文件](https://github.com/joeseesun/opus-video-prompts/blob/7977c807781d4ba7c235247b8899a72575a30d00/prompts/07-business-explainer-30s.md) |
| 配方动态图解 | [打开收录文件](https://github.com/joeseesun/opus-video-prompts/blob/7977c807781d4ba7c235247b8899a72575a30d00/prompts/08-negroni-recipe-explainer.md) |
| 大气环流与旁白 | [打开收录文件](https://github.com/joeseesun/opus-video-prompts/blob/7977c807781d4ba7c235247b8899a72575a30d00/prompts/09-atmospheric-circulation-tts.md) |
| 口播转线稿 | [打开收录文件](https://github.com/joeseesun/opus-video-prompts/blob/7977c807781d4ba7c235247b8899a72575a30d00/prompts/10-talking-head-to-lineart.md) |
| 历史叙事片 | [打开收录文件](https://github.com/joeseesun/opus-video-prompts/blob/7977c807781d4ba7c235247b8899a72575a30d00/prompts/11-austerlitz-film.md) |
| Remotion产品片一 | [打开收录文件](https://github.com/joeseesun/opus-video-prompts/blob/7977c807781d4ba7c235247b8899a72575a30d00/prompts/12-remotion-app-promo-1.md) |
| Remotion产品片二 | [打开收录文件](https://github.com/joeseesun/opus-video-prompts/blob/7977c807781d4ba7c235247b8899a72575a30d00/prompts/13-remotion-app-promo-2.md) |
| 真实素材SaaS发布片 | [打开收录文件](https://github.com/joeseesun/opus-video-prompts/blob/7977c807781d4ba7c235247b8899a72575a30d00/prompts/14-saas-launch-real-assets.md) |
| UI形态循环 | [打开收录文件](https://github.com/joeseesun/opus-video-prompts/blob/7977c807781d4ba7c235247b8899a72575a30d00/prompts/15-ui-morph-loop.md) |
| 极简产品视频 | [打开收录文件](https://github.com/joeseesun/opus-video-prompts/blob/7977c807781d4ba7c235247b8899a72575a30d00/prompts/16-high-end-product-video.md) |
| 像素叙事动画 | [打开收录文件](https://github.com/joeseesun/opus-video-prompts/blob/7977c807781d4ba7c235247b8899a72575a30d00/prompts/17-pixel-wizard.md) |
| Three.js场景 | [打开收录文件](https://github.com/joeseesun/opus-video-prompts/blob/7977c807781d4ba7c235247b8899a72575a30d00/prompts/18-prehistoric-island-threejs.md) |

## 有源码的制作资料

| 资料 | 用途 |
| --- | --- |
| [PDoomVideo分镜](https://github.com/JohnHeibel/PDoomVideo/blob/main/STORYBOARD.md) | 看歌词和镜头如何对应 |
| [PDoomVideo动画指南](https://github.com/JohnHeibel/PDoomVideo/blob/main/ANIMATION_GUIDE.md) | 看角色、画风、代码协作的制作约束 |
| [ClaudeAnimationBase指南](https://github.com/JohnHeibel/ClaudeAnimationBase/blob/main/ANIMATION_GUIDE.md) | 把参考工程改成新的角色动画 |
| [Lemo-Opuscar风格目录](https://github.com/lemomo-ai/lemo-opuscar/blob/main/styles/README.md) | 按视觉方向找风格提示词与样片 |
| [Lemo中文导演指南](https://github.com/lemomo-ai/lemo-opuscar/blob/main/docs/zh-CN/DIRECTOR.md) | 故事、声音、镜头与自检 |
| [Lemo中文技术指南](https://github.com/lemomo-ai/lemo-opuscar/blob/main/docs/zh-CN/TECHNIQUE.md) | 渲染、声音和输出流程 |

## 怎么改成自己的提示词

先替换题材、观众、时长、音乐与已有素材；再定义风格和交付。指定一个可检查的短样片，而不是只堆“电影感”“震撼”等形容词。词句相同也不代表工具、素材、历史上下文相同，效果不能只靠复制文字保证。
