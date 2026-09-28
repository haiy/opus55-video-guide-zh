# 收录方法、来源与更新范围

快照日期：2026-09-28。[返回导航](resource-navigation.md)

## 这次收了什么

- 原MV的作者帖子、Donald提示词来源链和JAZII模型对比案例。
- 与代码动画、MV、产品宣传片直接相关的GitHub项目与案例合集。
- 动画、浏览器渲染、音视频处理、节拍分析与字幕工具。
- 三份公开上游目录中的X帖子链接，按status ID合并，并补入本片核心来源。

这是一份尽量覆盖相关公开资料的导航快照，不是全网穷尽清单，也不把某个合集的候选量等同于独立原创视频数量。

## 数据层

| 文件 | 内容 |
| --- | --- |
| [github-resources.json](../data/github-resources.json) | 项目、用途、当日Star、最近推送、GitHub许可元数据、README来源与核查时间 |
| [x-cases.json](../data/x-cases.json) | 去重后的X原帖、作者、分类、技术标签、提示词入口和上游依据 |
| [sources.json](../data/sources.json) | 上游固定提交、数据文件及原始行数 |
| [index-summary.json](../data/index-summary.json) | 收录数量与分类计数 |

## X索引来源

1. [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos) 的 `data/videos.json`：282行，提供原帖、技术标签与提示词定位。
2. [joeseesun/opus-video-prompts](https://github.com/joeseesun/opus-video-prompts) 的 `cases.json`：54行，其中42条为X链接；非X链接不进入X专用表。
3. [athemeroy/awesome-opus-5-5-videos](https://github.com/athemeroy/awesome-opus-5-5-videos) 的 `data/cases.csv`：本次实际读取168行，以文件快照为准，不沿用README中可能较早的数量。
4. 本教程原有的anabology、Donald和JAZII核心来源。

三个上游共有504条数据行，抽取492条X链接，按status ID去重后448条；补入此前未覆盖的两个核心来源，得到450条。不同帖子仍可能展示同一视频，未下载原视频做跨帖媒体去重。

上游由其维护者维护；本索引重新组织导航结构与用途说明，保留原帖与固定提交链接，不复制第三方完整长提示词、图片或音视频。athemeroy项目的原创研究标注按其[CC BY 4.0说明](https://github.com/athemeroy/awesome-opus-5-5-videos/blob/main/LICENSE)归属原作者；这里只提取链接与路线分类并重新编排，原帖素材权利仍归各自作者。

## 核查状态怎么理解

- **GitHub项目**：通过GitHub API读取仓库元信息和当前README；新增用途说明来自这些公开文档。本次没有批量安装或运行项目。
- **核心案例**：anabology、Donald和JAZII已在本教程此前整理中核对来源链。本轮X直接抓取返回403，不将其误记为帖子已删除。
- **其他X入口**：由固定提交的上游目录收录，保留出处；不声称逐条打开、看完全片或验证作者全部制作披露。
- **提示词状态**：沿用上游“部分公开”等字段；18个题材入口是18个文件，不等于18份完整可复现的实验上下文。
- **Star**：2026-09-28查询时的数值，分类内降序；与质量、成本或复现成功率不是同一指标。
- **许可**：JSON里的null或NOASSERTION代表API未给出明确SPDX结论，不能据此推断可任意复用。源码、音乐、图片和角色素材的许可应分别看原项目说明。

## 后续怎么补充

按[贡献说明](../CONTRIBUTING.md)提交新原帖或项目，先查重复ID、原作者和资料完整度。更新数据时同步分类页面与首页数量。过期、失效或被作者纠正的条目保留变更说明，避免悄悄把旧说法当成新事实。

首屏群二维码是限时入口，原图注明2026年10月5日前有效；失效后需换新码。它与资源导航独立，不影响继续阅读教程。
