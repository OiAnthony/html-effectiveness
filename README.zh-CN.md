# html-effectiveness

<p align="center"><a href="README.md">English</a></p>

看了 [ThariqS/html-effectiveness](https://github.com/ThariqS/html-effectiveness) 那篇文章之后，想把这个思路做成一个 agent skill，自己用着玩。

让 AI agent 输出自包含的 HTML 文件，替代 Markdown。比较方案、做代码评审、写状态报告、做幻灯片，HTML 都比 Markdown 信息密度高、更好读。

装好之后，你让 agent "做个对比"或"出份报告"，它会直接生成一个 `.html` 文件，浏览器打开就能看，不依赖任何外部资源。

## 安装

```bash
npx skills add https://github.com/OiAnthony/html-effectiveness --skill html-effectiveness
```

## 模板

| 模板 | 适合的场景 |
|------|-----------|
| exploration | 多方案对比，按列排开 |
| code-review | PR / 代码走查，带 diff 和批注 |
| report | 指标看板 + 时间线 + 分段正文 |
| deck | 全屏幻灯片，方向键翻页 |
| editor | 拖拽排序、配置编辑，带导出按钮 |
| research | 长篇研究，可折叠章节 |
| changelog | 版本日志，按分类筛选 |

不限于这些模板。内容不匹配时，agent 会从设计系统直接搭页面。

## 设计系统

视觉风格来自 Kami "Parchment"：暖色纸张底（`#f5f4ed`），墨蓝唯一强调色（`#1B365D`），Charter 衬线字体，没有粗体和斜体。用 Tailwind CSS v4 Play CDN 做布局，所有样式内联，打开就能看。

## 致谢

- [html-effectiveness](https://github.com/ThariqS/html-effectiveness) by [Thariq Shihipar](https://x.com/trq212)，原始文章和 20 个 HTML demo，演示了 HTML 作为 AI 输出格式的效果。（[在线示例](https://thariqs.github.io/html-effectiveness/)）
- [Kami (紙)](https://github.com/anthropics/kami) by [Tw93](https://github.com/Tw93)，文档排版 skill，设计系统和模板结构的参考来源。
- [AntV Infographic](https://github.com/antvis/infographic) by [AntV](https://github.com/antvis)，声明式信息图引擎，图表生成模式和视觉语言的参考。
