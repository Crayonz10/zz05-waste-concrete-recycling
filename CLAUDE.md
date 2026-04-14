# LaTeX项目配置 - Elsarticle模板

## 项目信息
- **项目编号**: zz05
- **研究主题**: TODO: 填写研究主题
- **英文标题**: TODO: Fill in English title
- **方法**: TODO: 填写研究方法
- **模型文档**: `idea_zz05/modeling.md`（当前 v0.0）
- **研究战略**: `idea_zz05/idea.md`（当前 v0.0）

## 项目阶段
- 状态: writing
- 更新时间: 2026-03-29

## 核心配置
- **模板**: Elsarticle (preprint格式)
- **编译引擎**: pdfLaTeX + BibTeX
- **触发方式**: 保存时自动编译（`onSave`）
- **主文件**: `manuscript.tex` (单文件，所有内容已合并)
- **参考文献**: `zz05.bib`

## 文件结构
```
项目根目录/
├── manuscript.tex              # 论文主文件（单文件，包含所有section）
├── zz05.bib                   # 参考文献数据库
├── coverletter.tex            # 投稿信（独立提交文件）
├── declaration.tex            # 利益冲突声明（独立提交文件）
├── highlights.tex             # 研究亮点（独立提交文件）
├── idea_zz05/                 # 研究构思与模型推导
│   ├── modeling.md             # 模型文档 — 纯方法论
│   ├── modeling.pdf            # ← modeling.md 的 PDF 导出（自动更新）
│   ├── idea.md                 # 研究战略文档 — 可行性/差异化/骨架
│   ├── idea.pdf                # ← idea.md 的 PDF 导出（自动更新）
│   └── pandoc_header.tex       # Pandoc PDF 导出的 LaTeX 头文件
├── literature_zz05/           # 文献资料
│   ├── *.ris                  # WOS 文献导出
│   ├── gap_analysis_report.md # 文献 Gap 分析报告
│   └── parsed_*.json          # RIS 解析文件
├── simulation/                # 数值仿真
│   ├── simulate_zz05.py       # Python 仿真脚本
│   └── figures/               # 仿真图表输出
├── drafts/                    # /draft 命令输出（writing_brief + 各章节草稿）
├── polish/                    # Mode B 语言润色输出（顺序编号 001.md, 002.md, ...）
├── PROGRESS.MD                # 项目进度跟踪
├── .vscode/settings.json      # VS Code配置
├── latexmkrc                  # latexmk编译配置
└── elsarticle.cls             # Elsevier模板文件
```

## idea_zz05/ 核心文件说明

`idea.md` 和 `modeling.md` 是 `manuscript.tex` 的两大支柱文件，随研究深入持续迭代更新。

| 文件 | 定位 | 内容范围 | 版本 |
|------|------|---------|:----:|
| **`modeling.md`** | **纯方法论** | 模型构建（问题描述、符号、假设）、推导过程、命题及证明、比较静态、数值仿真框架 | v0.0 |
| **`idea.md`** | **研究战略** | Gap 验证、RQ 与命题的映射、Discussion 方向、理论/实践启示、差异化定位、文献支撑、风险评估 | v0.0 |

**分工原则**：方法论内容（公式推导、证明、仿真参数）只进 `modeling.md`；战略内容（定位、贡献论证、写作策略）只进 `idea.md`。两者通过尾注互相引用。

### PDF 自动更新规则

**每次修改 `idea.md` 或 `modeling.md` 后，必须立即重新生成对应的 PDF 文件**。使用以下 pandoc 命令（在 `idea_zz05/` 目录下执行）：

```bash
# idea.md → idea.pdf
pandoc idea.md -o idea.pdf --pdf-engine=xelatex -H pandoc_header.tex --wrap=auto -V geometry:margin=2.5cm -V fontsize=11pt

# modeling.md → modeling.pdf
pandoc modeling.md -o modeling.pdf --pdf-engine=xelatex -H pandoc_header.tex --wrap=auto -V geometry:margin=2.5cm -V fontsize=11pt
```

- PDF 文件仅供阅读参考（如分享给导师/合作者），`.md` 是唯一的 source of truth
- `pandoc_header.tex` 提供 CJK 字体支持和排版优化，**不要删除或修改**

## 编译目录策略

**所有编译产物（`.aux`, `.bbl`, `.log` 等）直接生成在根目录**，不使用 `build/` 子目录。原因：
- VS Code LaTeX Workshop 会在根目录额外运行 pdflatex 生成诊断信息，若 `.bbl` 在 `build/` 中则找不到，导致满屏 citation 警告
- 根目录编译确保 latexmk 和 LaTeX Workshop 共享同一套 `.bbl`/`.aux`，避免双重编译环境不同步

**目录整洁方案**：
- `.gitignore` — 排除所有临时文件，不进入版本控制
- `.vscode/settings.json` 的 `files.exclude` — 在文件浏览器中隐藏临时文件，视觉上保持根目录整洁
- 排错时通过终端直接访问日志：`cat manuscript.log`

**禁止事项**：
- ❌ 不要在 `latexmkrc` 中设置 `$out_dir` / `$aux_dir`
- ❌ 不要在 VS Code tool args 中传 `-outdir=build`
- ❌ 不要启用 `$preview_continuous_mode = 1`（与 LaTeX Workshop 的 `onSave` 冲突）

## 编译命令
```bash
latexmk manuscript.tex           # 编译
latexmk -pvc- -pv- manuscript.tex  # 单次编译（不进入持续监听模式）
latexmk -c                       # 清理临时文件（保留PDF）
latexmk -C                       # 完全清理（包括PDF）
```

## 关键规则

### 1. 文献引用标记
文本中标有 **`(ref)`** 的地方是待添加文献的标记，**不要修改或删除**！

### 2. Unicode 字符
pdfLaTeX 不支持直接使用 Unicode 希腊字母和特殊符号。正文中必须使用 LaTeX 命令：
- β → `$\beta$`，α → `$\alpha$`，χ → `$\chi$`
- → → `$\rightarrow$`，− → `$-$`
- 禁止使用全角标点（，。；等）

### 3. 投稿前准备
- 注释掉`manuscript.tex`中的geometry页边距设置，恢复Elsarticle默认格式
- 修改`\journal{}`为目标期刊名称
- 确保`zz05.bib`文件完整且格式正确

### 4. 标题大写规范
**所有标题均使用 Sentence case（句式大写），而非 Title Case（标题式大写）。**
- ✅ `\section{Results of necessary condition analysis}`
- ❌ `\section{Results of Necessary Condition Analysis}`
- **例外**：专有名词和缩写保持原有大写（如 COVID-19、China、BIM、SaaS 等）

### 5. 语言规范

**权威规则源**: `~/.claude/agents/language-polisher.md`（Categories A–M，含 Chinglish 消除、时态、修饰语、破折号等 13 类规则）。

主 agent 撰写英文文本时专注内容质量，**不需要**执行语言自检。
用户需要语言润色时会手动指示调用 `language-polisher` agent（Mode B），届时按提示执行即可。

#### Mode B 输出保存
调用 language-polisher（Mode B）后，主 agent **必须**将完整输出保存到文件：
- **目录**: `polish/`（项目根目录下，不存在则创建）
- **文件名**: 三位顺序编号，如 `001.md`、`002.md`（扫描已有文件取最大编号 +1）
- **内容**: polisher 返回的完整输出（润色后文本 + Change Summary），原样保存，不做额外加工
- **语言**: 报告使用**中文**撰写
- **保存后**：告知用户文件路径，方便查阅和合并

## 表格规范

### 标准模板
```latex
\begin{table}[!htbp]
\centering
\captionsetup{font=normalsize, labelsep=period}
setlength{\abovecaptionskip}{5pt}
setlength{\belowcaptionskip}{0pt}
\caption{表格标题}
\label{tab:label_name}
\small
\begin{threeparttable}
\begin{tabular*}{0.9\textwidth}{@{\extracolsep{\fill}}lccccccc}
\toprule
\textbf{列标题1} & \textbf{列标题2} & ... \\
\midrule
\textit{变量1} & 数据 & ... \\
\textit{变量2} & 数据 & ... \\
\bottomrule
\end{tabular*}
\begin{tablenotes}[flushleft]
\small\linespread{1}\selectfont
\item \textit{Note}: 注释内容...
\end{tablenotes}
\end{threeparttable}
\end{table}
\vspace{-15pt}
```

### 核心规则
- 统一 `\small` 字体，**禁止** `\footnotesize`、`\Large` 等
- 表头 `\textbf{}`，第一列 `\textit{}`，数据列居中 `c`
- 宽度 `0.9\textwidth`，浮动 `[!htbp]`

## 故障排查
- 编译问题：`Cmd+Shift+P` → `Kill LaTeX compiler process`，或手动 `latexmk -pvc- -pv- manuscript.tex`
- 参考文献不显示：确认 `\bibliography{zz05}` 和 `zz05.bib` 存在

## Academic Writing Workflow

本项目使用全局 4-Agent Pipeline（`~/.claude/agents/` + `~/.claude/commands/`）进行论文撰写和打磨。

| 命令 | 用途 |
|------|------|
| `/draft` | 从大纲/要点撰写 |
| `/polish` | 打磨已有文本 |

**使用方式**：在 VS Code 中选中文本，输入 `/draft` 或 `/polish`。

**输出**：`drafts/writing_brief.md`（期刊简报）+ `drafts/{Section}_{timestamp}/`（含 checkpoint 文件、changelog.md、final.md）+ `drafts/{Section}_latest_final.md`（便捷入口）。

**核心规则**：manuscript 文件全程只读 · 确认后手动合并 · 保持 `(ref)` 标记不变。

## 投稿待办 (TODO)

- [ ] 确定目标期刊
- [ ] 完成模型求解
- [ ] 完善命题的正式证明
- [ ] 数值仿真
- [ ] 撰写 Introduction 章节
- [ ] 撰写 Literature Review 章节
- [ ] 撰写 Model Formulation 章节
- [ ] 撰写 Equilibrium Analysis + Numerical Simulation 章节
- [ ] 撰写 Discussion / Conclusion
- [ ] 语言润色（language-polisher Mode B）
- [ ] 补充作者信息（取消注释 manuscript.tex 中的 author block）
- [ ] 补充 Funding / Acknowledgments 信息
- [ ] 准备 Cover letter
- [ ] （可选）准备 Graphical abstract
