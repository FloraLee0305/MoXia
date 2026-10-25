# 墨匣 · 知乎网文 Skill 包 实施计划

> **Goal:** 搭建墨匣 Skill 包的知乎网文模式，跑通「灵感→大纲→正文→去AI味→交付」全流程

**Architecture:** 基于 oh-story-claudecode 的短篇写作流程简化，保留五阶段工作流、题材包、去AI味三层质检，去掉多宿主适配等复杂机制

**Tech Stack:** Markdown (SKILL.md) + 少量 Python 脚本（字数统计、AI 模式检测）

---

## 文件结构

```
moxia/
├── SKILL.md                              # 主路由入口
├── skills/
│   ├── moxia-router/SKILL.md             # 路由 + 灵感输入
│   ├── moxia-webnovel/
│   │   ├── SKILL.md                      # 网文五阶段工作流
│   │   └── references/
│   │       ├── short-craft.md            # 短篇通用写法
│   │       ├── deslop.md                 # 去AI味三层质检规则
│   │       └── genre-styles/
│   │           ├── 世情打脸.md
│   │           ├── 甜宠.md
│   │           ├── 悬疑.md
│   │           ├── 重生爽文.md
│   │           └── 追妻火葬场.md
│   └── moxia-shared/
│       └── SKILL.md                      # 共享工具（字数统计脚本说明）
├── templates/
│   ├── 设定.md.tmpl
│   ├── 角色.md.tmpl
│   ├── 大纲.md.tmpl
│   └── 正文.md.tmpl
└── scripts/
    └── check_wordcount.py               # 字数统计 + AI 高频词检测
```

---

## Task 1: 创建主路由入口 SKILL.md

**Files:**
- Create: `moxia/SKILL.md`

- [ ] **Step 1: 创建 moxia/SKILL.md**

内容：

```markdown
---
name: moxia
description: "墨匣三合一创作工作台。支持知乎网文、漫剧剧本、易次元文游三种模式。触发方式：/墨匣、/moxia、「我想写网文」「帮我写个漫剧剧本」「做个文游」。"
---

# 墨匣 · 三合一创作工作台

识别用户的创作需求，路由到对应模式。

## 路由表

| 用户意图 | 关键词 | 路由到 |
|---------|--------|--------|
| 知乎网文/短篇 | 网文、短篇、盐言、知乎、写小说 | `/墨匣-网文` |
| 漫剧剧本 | 漫剧、短剧、剧本、分镜 | `/墨匣-漫剧` |
| 易次元文游 | 文游、易次元、橙光、文字游戏、分支 | `/墨匣-文游` |
| 改编 | 把这篇改成漫剧/文游 | 先确认源作品，再路由 |

能明确匹配就直接调用；匹配不上时只问缺的那一项。
用户说"我想写东西"但没说类型，先问是网文、漫剧还是文游。

## 裸调用

只说 `/墨匣` 时，给三个选项：
1. 写知乎网文 → `/墨匣-网文`
2. 写漫剧剧本 → `/墨匣-漫剧`
3. 写易次元文游 → `/墨匣-文游`
```

- [ ] **Step 2: 提交**

```bash
cd D:\Desktop\MoXia
git add moxia/SKILL.md
git commit -m "feat: 创建墨匣主路由入口"
```

---

## Task 2: 创建路由 skill（灵感输入）

**Files:**
- Create: `moxia/skills/moxia-router/SKILL.md`

- [ ] **Step 1: 创建 moxia-router/SKILL.md**

内容：

```markdown
---
name: moxia-router
description: "墨匣路由与灵感输入。接收用户的创作灵感，确认模式和基本参数。"
---

# 墨匣路由

接收用户的创作灵感，确认以下信息后交给对应模式：

## 确认项

### 知乎网文模式
1. 灵感内容（一句话或一个片段）
2. 目标情绪（爽感释放/意难平/反转震撼/治愈温暖/细思极恐/共鸣感动）
3. 题材方向（世情打脸/甜宠/悬疑/重生爽文/追妻火葬场/其他）

### 漫剧剧本模式
1. 灵感或原著来源
2. 制作形态（写实漫剧/二次元/水墨国风/Q版）

### 易次元文游模式
1. 灵感内容
2. 主线长度（短篇5-10章/中篇10-30章/长篇30章+）
3. 支线数量（2-3条/4-6条/先做主线）

## 交互规则

- 信息足够时直接工作，不为凑问题而问
- 只有会改变核心方向的缺口才提问
- 用户已给的信息不重复确认
```

- [ ] **Step 2: 提交**

```bash
git add moxia/skills/moxia-router/SKILL.md
git commit -m "feat: 创建路由与灵感输入 skill"
```

---

## Task 3: 创建网文模式主 SKILL.md（五阶段工作流）

**Files:**
- Create: `moxia/skills/moxia-webnovel/SKILL.md`

- [ ] **Step 1: 创建 moxia-webnovel/SKILL.md**

内容：

```markdown
---
name: moxia-webnovel
description: "知乎网文写作。从灵感到成稿，五阶段工作流：灵感输入→大纲补全→正文生成→去AI味→成稿交付。触发方式：/墨匣-网文、「帮我写篇网文」「写个盐言故事」。"
---

# 墨匣 · 知乎网文写作

从灵感到成稿，辅助用户完成一篇知乎盐言风格短篇小说。

**核心原则：短篇以情绪为目标，所有内容为情绪服务。用户是导演，AI 是执行助手。**

## 五阶段工作流

### 阶段 1：灵感输入

1. 接收用户的灵感（一句话或片段）
2. 确认目标情绪（6 选 1：爽感释放/意难平/反转震撼/治愈温暖/细思极恐/共鸣感动）
3. 确认题材方向

**情绪-题材匹配参考：**
| 情绪 | 常配题材 |
|------|---------|
| 爽感释放 | 世情打脸/重生爽文/复仇打脸 |
| 意难平 | 追妻火葬场/甜宠(先虐后甜) |
| 反转震撼 | 悬疑/重生爽文 |
| 治愈温暖 | 甜宠/双男主 |
| 细思极恐 | 悬疑/民俗怪谈 |
| 共鸣感动 | 世情打脸/追妻火葬场 |

### 阶段 2：AI 补全大纲

1. 读取 `references/short-craft.md` 通用写法
2. 读取对应题材包 `references/genre-styles/{题材}.md`
3. 基于灵感生成 **3 个不同方向**的大纲方案
4. 每个方案包含：故事核、主要人物、反转点、情绪曲线

**用户确认后落盘：**
- `设定.md`（题材、情绪、世界观、核心冲突）
- `角色.md`（主角、对手、配角）
- `大纲.md`（章节规划：每章目标+冲突+转折+钩子）

### 阶段 3：生成正文

1. 读取 `设定.md` + `角色.md` + `大纲.md`
2. 按大纲逐章生成正文
3. **每章生成后停下等用户确认**，不自动连写
4. 用户选项：确认继续 / 重写本章 / 局部修改 / 先放着

**落盘：** `正文.md`（追加模式，每章用 `---` 分隔）

### 阶段 4：去 AI 味

三层质检：
1. **表达层**：电报体、短碎句、机械复现、AI 高频词
2. **用笔层**：场景详略、细节功能、无用描写
3. **故事层**：行为因果、人物动机、知情顺序

详细规则见 `references/deslop.md`。

### 阶段 5：成稿交付

- 合并完整正文
- 字数统计（目标 8000-15000 字）
- 知乎盐言投稿格式优化

## 质量门禁

| 检查项 | 标准 |
|--------|------|
| 总字数 | 8000-15000 |
| 开头钩子 | 前 3 句有冲突/悬念 |
| AI 高频词 | "仿佛""好像"不超过 10 处 |
| 章节数 | 与大纲一致 |

## 写前必读

进入正文写作前，完整读取：
- `references/short-craft.md`（通用写法）
- `references/genre-styles/{题材}.md`（题材特化）
- `references/deslop.md`（去 AI 味规则）
```

- [ ] **Step 2: 提交**

```bash
git add moxia/skills/moxia-webnovel/SKILL.md
git commit -m "feat: 创建网文模式五阶段工作流"
```

---

## Task 4: 创建短篇通用写法参考

**Files:**
- Create: `moxia/skills/moxia-webnovel/references/short-craft.md`

- [ ] **Step 1: 从 oh-story 提取 short-craft.md 核心内容**

从 `D:\Desktop\MoXia\novel-ai-toolbox\novel-ai-toolbox\oh-story-claudecode\skills\story-short-write\references\short-craft.md` 提取核心规则，精简后写入。

关键内容（保留这些章节）：
1. 人称与腔调：第一人称受害者，双轨切换（受虐段直白宣泄 / 反击段冷静审判）
2. 情绪落地：直接写情绪词，四个落点
3. 叙述姿态：在场叙述者，可主观评论
4. 小节结构：每节围绕一个主问题
5. 开头 3 句定生死：必须包含钩子
6. 结尾定传播：留余韵

- [ ] **Step 2: 提交**

```bash
git add moxia/skills/moxia-webnovel/references/short-craft.md
git commit -m "feat: 添加短篇通用写法参考"
```

---

## Task 5: 创建去 AI 味规则参考

**Files:**
- Create: `moxia/skills/moxia-webnovel/references/deslop.md`

- [ ] **Step 1: 从 oh-story 提取 deslop 核心规则**

从 oh-story 的 story-deslop skill 提取三层质检规则：

```markdown
# 去 AI 味三层质检

## 表达层

### 要查的问题
- 电报体：句子过短、碎片感强
- 短碎句：连续多个极短句
- 机械复现：同一句式/词语反复出现
- AI 高频词："仿佛""好像""似乎""宛如"超过 10 处需复核

### 处理原则
- 不机械全删，逐处看功能
- 准确直写、心理活动、带立场的叙述可保留

## 用笔层

### 要查的问题
- 场景详略不当：重要场景一笔带过，无关场景啰嗦
- 细节无功能：描写不推动剧情、不铺垫反转、不推高情绪
- 无用环境描写：为凑字数写的风景/陈设

### 处理原则
- 每句话必须有用，没用就删
- 细节要服务于情绪或剧情

## 故事层

### 要查的问题
- 行为无因果：角色做事没有动机
- 人物动机矛盾：前文铺垫和后文行为冲突
- 知情顺序错误：角色知道了不该知道的事

### 处理原则
- 先判断故事成立条件，再安排场景用笔
- 剧情缺口给出方案，用户授权后再改
```

- [ ] **Step 2: 提交**

```bash
git add moxia/skills/moxia-webnovel/references/deslop.md
git commit -m "feat: 添加去AI味三层质检规则"
```

---

## Task 6: 创建题材包（5 个核心题材）

**Files:**
- Create: `moxia/skills/moxia-webnovel/references/genre-styles/世情打脸.md`
- Create: `moxia/skills/moxia-webnovel/references/genre-styles/甜宠.md`
- Create: `moxia/skills/moxia-webnovel/references/genre-styles/悬疑.md`
- Create: `moxia/skills/moxia-webnovel/references/genre-styles/重生爽文.md`
- Create: `moxia/skills/moxia-webnovel/references/genre-styles/追妻火葬场.md`

- [ ] **Step 1: 从 oh-story 提取世情打脸.md**

从 `oh-story-claudecode/skills/story-short-write/references/genre-styles/世情打脸.md` 提取核心内容（叙述腔调、开篇范式、钩子母题、情绪烈度、金句招式、收尾）。

- [ ] **Step 2: 提取甜宠.md**

从 oh-story 提取甜宠题材包核心内容。

- [ ] **Step 3: 提取悬疑.md**

从 oh-story 提取悬疑题材包核心内容。

- [ ] **Step 4: 提取追妻火葬场.md**

从 oh-story 提取追妻火葬场题材包核心内容。

- [ ] **Step 5: 编写重生爽文.md**

oh-story 没有独立的重生爽文题材包，根据知乎盐言常见写法编写：

```markdown
# 题材风格包：重生爽文

> 一句话定位：主角带着前世记忆/经验重生，用信息差碾压对手，实现逆袭打脸。

## 叙述腔调
第一人称「我」，重生者视角。前期冷静布局，中期步步为营，后期当众打脸。
腔调从"看透一切的从容"到"碾压对手的痛快"。

## 开篇范式
- 重生瞬间：死亡/绝望场景 + 睁眼回到过去
- 信息差展示：主角知道未来会发生什么，读者期待他如何利用
- 立 flag：主角立下改变命运的目标

## 钩子母题
- 信息差碾压：主角提前知道对手的阴谋
- 扮猪吃虎：主角表面普通，实则深不可测
- 当众打脸：前世欺负主角的人被反杀
- 资源抢占：主角提前布局抢占未来的机遇

## 情绪烈度
烈度 8-9：爽感直接、强烈。打脸要干脆利落，不拖泥带水。
```

- [ ] **Step 6: 提交**

```bash
git add moxia/skills/moxia-webnovel/references/genre-styles/
git commit -m "feat: 添加5个核心题材包"
```

---

## Task 7: 创建文件模板

**Files:**
- Create: `moxia/templates/设定.md.tmpl`
- Create: `moxia/templates/角色.md.tmpl`
- Create: `moxia/templates/大纲.md.tmpl`
- Create: `moxia/templates/正文.md.tmpl`

- [ ] **Step 1: 创建设定.md.tmpl**

```markdown
# 设定 · {作品名}

## 基本信息
- 题材：{题材}
- 目标情绪：{情绪}
- 时代背景：{背景}
- 字数目标：8000-15000
- 人称：第一人称

## 世界观
{世界观描述}

## 核心冲突
{核心矛盾}

## 故事核
{一句话概括故事}
```

- [ ] **Step 2: 创建角色.md.tmpl**

```markdown
# 角色 · {作品名}

## {主角名}（主角）
- 身份：{身份}
- 性格：{性格}
- 目标：{目标}
- 秘密：{秘密/金手指}
- 弧光：{成长变化}

## {对手名}（对手）
- 身份：{身份}
- 性格：{性格}
- 目标：{目标}
- 与主角关系：{关系}

## {配角名}（配角）
- 身份：{身份}
- 作用：{在故事中的功能}
```

- [ ] **Step 3: 创建大纲.md.tmpl**

```markdown
# 大纲 · {作品名}

## 章节规划

### 第1章 · {章名}
- 目标：{本章要完成什么}
- 冲突：{核心矛盾}
- 转折：{关键反转}
- 章尾钩子：{留下什么悬念}

### 第2章 · {章名}
...
```

- [ ] **Step 4: 创建正文.md.tmpl**

```markdown
# 正文 · {作品名}

---

## 第1章 · {章名}

{正文内容}

---

## 第2章 · {章名}
...
```

- [ ] **Step 5: 提交**

```bash
git add moxia/templates/
git commit -m "feat: 添加文件结构模板"
```

---

## Task 8: 创建字数统计脚本

**Files:**
- Create: `moxia/scripts/check_wordcount.py`

- [ ] **Step 1: 编写 check_wordcount.py**

```python
#!/usr/bin/env python3
"""墨匣网文质量检查：字数统计 + AI 高频词检测"""

import sys
import re
from pathlib import Path


def count_chinese_chars(text: str) -> int:
    """统计中文字符数（不含标点和空白）"""
    return len(re.findall(r'[\u4e00-\u9fff]', text))


def check_ai_patterns(text: str) -> dict:
    """检测 AI 高频词"""
    patterns = {
        '仿佛': r'仿佛',
        '好像': r'好像',
        '似乎': r'似乎',
        '宛如': r'宛如',
        '犹如': r'犹如',
    }
    results = {}
    for word, pattern in patterns.items():
        count = len(re.findall(pattern, text))
        results[word] = count
    return results


def check_degeneration(text: str) -> list:
    """检测退化问题：复读、截断、工程词泄漏"""
    issues = []
    # 连续重复句子
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i in range(len(lines) - 1):
        if lines[i] == lines[i + 1]:
            issues.append(f'复读：第{i+1}行与第{i+2}行完全相同')
    # 工程词泄漏
    leak_words = ['作为一个', '总而言之', '综上所述', '首先', '其次', '最后']
    for word in leak_words:
        if word in text:
            issues.append(f'工程词泄漏：包含"{word}"')
    return issues


def main():
    if len(sys.argv) < 2:
        print('用法: python check_wordcount.py <正文文件>')
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f'文件不存在: {file_path}')
        sys.exit(1)

    text = file_path.read_text(encoding='utf-8')

    # 字数统计
    char_count = count_chinese_chars(text)
    print(f'中文字数: {char_count}')
    if char_count < 8000:
        print(f'⚠ 字数不足，目标 8000-15000，当前 {char_count}')
    elif char_count > 15000:
        print(f'⚠ 字数超标，目标 8000-15000，当前 {char_count}')
    else:
        print('✓ 字数达标')

    # AI 高频词
    print('\n--- AI 高频词检测 ---')
    ai_patterns = check_ai_patterns(text)
    total_ai = sum(ai_patterns.values())
    for word, count in ai_patterns.items():
        if count > 0:
            print(f'  {word}: {count} 处')
    if total_ai > 10:
        print(f'⚠ AI 高频词共 {total_ai} 处，超过 10 处阈值，建议复核')
    else:
        print(f'✓ AI 高频词共 {total_ai} 处，在阈值内')

    # 退化检测
    print('\n--- 退化检测 ---')
    issues = check_degeneration(text)
    if issues:
        for issue in issues:
            print(f'  ⚠ {issue}')
    else:
        print('✓ 未发现退化问题')


if __name__ == '__main__':
    main()
```

- [ ] **Step 2: 验证脚本可运行**

```bash
cd D:\Desktop\MoXia\moxia
python scripts/check_wordcount.py ../novel-ai-toolbox/novel-ai-toolbox/oh-story-claudecode/demo/短篇-曾将爱意私藏.txt
```

预期：输出字数统计和 AI 高频词检测结果。

- [ ] **Step 3: 提交**

```bash
git add moxia/scripts/check_wordcount.py
git commit -m "feat: 添加字数统计和AI模式检测脚本"
```

---

## Task 9: 端到端验证

**Files:**
- 无新建文件，使用已有 skill

- [ ] **Step 1: 用真实灵感测试全流程**

在 Trae 中加载 moxia skill，执行：

```
/墨匣-网文
灵感：一个过气的新媒体运营重生回 2018 年，用未来经验帮文工团做账号逆袭
情绪：爽感释放
题材：重生爽文
```

验证：
- AI 是否生成 3 个方向的大纲
- 用户选择后是否落盘 设定.md + 角色.md + 大纲.md
- 生成正文是否逐章停下确认
- 去 AI 味是否执行三层质检
- 字数统计脚本是否正常运行

- [ ] **Step 2: 根据测试结果调整**

如果流程有断点或提示词效果不好，调整对应 SKILL.md 的内容。

- [ ] **Step 3: 提交最终调整**

```bash
git add -A
git commit -m "fix: 根据端到端测试调整网文工作流"
```

---

## 自检结果

1. **Spec 覆盖**：设计文档 Part 3（知乎网文模式）的五阶段工作流、质量门禁、文件结构均有对应任务
2. **占位符**：无 TBD/TODO，所有步骤都有具体内容
3. **类型一致**：文件名、路径在各任务间一致
