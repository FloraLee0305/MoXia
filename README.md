# 墨匣（MoXia）

三合一创作工作台：知乎网文 · 漫剧剧本 · 易次元文游

## 项目简介

墨匣是一个人机共创的创作 Skill 包，帮助用户把一个灵感打磨成完整的作品。用户是创作的导演，AI 是执行助手。

## 工作进度

### v2026-10-25

**已完成：**
- [x] 设计文档：[docs/specs/2026-10-25-moxia-design.md](docs/specs/2026-10-25-moxia-design.md)
- [x] 实施计划：[docs/plans/2026-10-25-moxia-webnovel-skill.md](docs/plans/2026-10-25-moxia-webnovel-skill.md)
- [x] 知乎网文 Skill 包（阶段 A）
  - 主路由入口 `moxia/SKILL.md`
  - 路由 + 灵感输入 `moxia/skills/moxia-router/`
  - 网文五阶段工作流 `moxia/skills/moxia-webnovel/`
  - 短篇通用写法 `references/short-craft.md`
  - 去 AI 味三层质检 `references/deslop.md`
  - 5 个核心题材包（世情打脸/甜宠/悬疑/重生爽文/追妻火葬场）
  - 4 个文件模板（设定/角色/大纲/正文）
  - 字数统计 + AI 模式检测脚本

**进行中：**
- [ ] 知乎网文 Skill 包端到端测试

**待办：**
- [ ] 漫剧剧本模式（阶段 B）
- [ ] 易次元文游模式（阶段 C）
- [ ] Web 应用化（阶段 D，可选）

## 安装使用

将 `moxia/` 目录复制到 Trae 的 skills 目录：

```
cp -r moxia ~/.trae-cn/skills/moxia
```

重启 Trae 后，在对话中输入 `/墨匣-网文` 开始创作。

## 设计来源

本项目的工作流和机制主要借鉴以下开源项目（均为 MIT / Apache-2.0 协议）：

| 借鉴项目 | 复用内容 |
|---------|---------|
| oh-story-claudecode | 网文五阶段流程、题材包、去 AI 味质检 |
| drama-skills | 漫剧剧本格式、视觉设定、连续性锁 |

## 协议

MIT
