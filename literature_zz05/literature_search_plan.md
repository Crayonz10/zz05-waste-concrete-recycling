# zz05 文献检索方案

> **日期**: 2026-03-25
> **检索平台**: Web of Science (WOS) Core Collection
> **总预算**: 360篇
> **目标期刊**: TODO
> **Idea成熟度**: mature（idea.md v1.0，Gap/RQ/方法均明确）
> **规则**: 每个方向**仅一条检索式**，复制粘贴即用

---

## 方向1：建筑废弃物回收管理与经济决策
> **层面**: 行业背景 + 核心研究领域
> **论文角色**: 提供废弃混凝土回收的行业背景、经济决策现状和管理挑战，支撑 Introduction 的问题提出和 Literature Review 的行业梳理
> **功能标签**: BG + LR + GAP-RQ2 + DISC-RQ2
> **优先级**: **P1**
> **配额**: 82篇（核心≤21 / 重要≤33 / 备选≤28）

```
TS=("construction and demolition waste" OR "C&D waste" OR "waste concrete" OR "demolition waste" OR "concrete recycl*") AND TS=("recycl*" OR "reuse" OR "circular economy" OR "resource recovery") AND TS=("management" OR "economic*" OR "cost*" OR "supply chain" OR "decision*" OR "policy" OR "incentive*" OR "stakeholder*" OR "pricing")
```
> **设计说明**: 使用 TS 而非 TI，因为"management""economic"等词常出现在摘要而非标题中。核心限定词为"construction and demolition waste"及其变体，交叉"recycl*"确保聚焦回收主题，再交叉管理/经济类关键词排除纯技术文献。预估检索量 200-400 篇，筛选后取 82 篇。

---

## 方向2：回收/逆向物流供应链博弈模型
> **层面**: 核心理论
> **论文角色**: 本文的直接理论对话对象——在回收供应链中使用博弈论建模的文献。支撑 Literature Review 中博弈论应用的综述，同时用于识别 Gap（缺少竞合并存模型）和 Discussion 中的结果对比
> **功能标签**: LR + GAP-RQ1 + GAP-RQ2 + DISC-RQ1 + DISC-RQ2
> **优先级**: **P1**
> **配额**: 58篇（核心≤15 / 重要≤24 / 备选≤19）

```
TS=("recycl*" OR "reverse logistics" OR "remanufactur*" OR "closed-loop supply chain" OR "waste" OR "end-of-life") AND TS=("game theory" OR "game-theoretic" OR "Nash equilibrium" OR "Stackelberg" OR "cooperative game" OR "non-cooperative game" OR "evolutionary game")
```
> **设计说明**: 第一组 OR 覆盖回收/逆向物流/再制造/废弃物等近义词，第二组 OR 覆盖各类博弈论方法。TS 检索确保广泛捕获。"waste" 单独加入是因为部分建筑废弃物文献不用 "recycl*" 而用 "waste treatment/processing"。预估检索量 300-600 篇，需适当筛选。如超 500 篇可加 NOT TS=("evolutionary game") 缩窄。

---

## 方向3：Biform game 理论与应用
> **层面**: 方法论
> **论文角色**: 本文所用核心方法的理论来源和应用先例。Biform game 是较新的博弈框架，文献量有限但每篇都高度相关。支撑 Literature Review 中方法论脉络和 Methodology 的理论依据
> **功能标签**: LR + METHOD-基础 + METHOD-先例
> **优先级**: **P1**
> **配额**: 54篇（核心≤14 / 重要≤22 / 备选≤18）

```
TS=("biform game" OR "biform games") OR (TI=("cooperative" AND "non-cooperative" AND "game") AND TS=("supply chain" OR "alliance" OR "coalition" OR "profit allocation" OR "cost sharing"))
```
> **设计说明**: "biform game" 是专用术语，用 TS 直接检索。同时用第二条 OR 分支捕获未使用 "biform" 标签但实质上同时建模合作与非合作博弈的文献——这类文献用 TI 限定（标题必须同时含三个关键词），再交叉供应链/联盟等主题词确保相关性。Biform game 文献量本身较少（约 30-80 篇），第二分支可能贡献额外 20-50 篇。如总量不足 54 篇，放宽为全部纳入。

---

## 方向4：Shapley值在供应链利润分配中的应用
> **层面**: 方法论
> **论文角色**: Shapley 值是本文合作博弈阶段的核心求解工具。该方向文献提供方法论先例和应用对比，支撑 Methodology 中 Shapley 值选择的合理性论证
> **功能标签**: LR + METHOD-先例
> **优先级**: **P2**
> **配额**: 54篇（核心≤14 / 重要≤22 / 备选≤18）

```
TS=("Shapley value" OR "Shapley") AND TS=("supply chain" OR "profit allocation" OR "cost allocation" OR "cost sharing" OR "revenue sharing" OR "logistics" OR "recycl*")
```
> **设计说明**: "Shapley" 是高辨识度术语，用 TS 检索即可。交叉供应链/利润分配/成本分担等词确保应用导向（排除纯数学理论文献）。加入 "recycl*" 捕获回收领域的 Shapley 应用。预估检索量 100-200 篇。

---

## 方向5：供应链竞合关系（Coopetition）
> **层面**: 理论基础
> **论文角色**: 竞合关系（coopetition）是本文的核心理论视角——制造商和回收商在收集环节竞争、在加工环节合作。该方向提供竞合理论框架和供应链竞合案例，支撑 Literature Review 和 Discussion
> **功能标签**: LR + GAP-RQ1 + DISC-RQ1
> **优先级**: **P2**
> **配额**: 58篇（核心≤15 / 重要≤24 / 备选≤19）

```
TS=("coopetition" OR "co-opetition" OR "cooperation and competition" OR "compete and cooperate" OR "competition-cooperation") AND TS=("supply chain" OR "pricing" OR "game" OR "alliance" OR "recycl*" OR "manufactur*")
```
> **设计说明**: "coopetition" 及其拼写变体是核心检索词。同时加入 "cooperation and competition""competition-cooperation" 等描述性短语，因为部分文献（尤其中国学者）不用 "coopetition" 而用这些表述。交叉供应链/博弈/制造等词确保聚焦。预估检索量 100-250 篇。

---

## 方向6：政府补贴与回收激励机制
> **层面**: 行业背景/政策
> **论文角色**: 政府补贴 s 是本文模型的关键参数之一，仿真分析发现补贴对回收量、技术投资和利润分配有显著影响。该方向文献支撑 Introduction 的政策背景和 Discussion 中补贴效应的对比分析
> **功能标签**: BG + GAP-RQ2 + DISC-RQ2
> **优先级**: **P2**
> **配额**: 54篇（核心≤14 / 重要≤22 / 备选≤18）

```
TS=("government subsidy" OR "government subsidies" OR "subsidy policy" OR "policy incentive*" OR "tax incentive*") AND TS=("recycl*" OR "remanufactur*" OR "reverse logistics" OR "waste" OR "circular economy") AND TS=("game" OR "pricing" OR "decision*" OR "supply chain" OR "optimal*")
```
> **设计说明**: 三层交叉：补贴政策 × 回收/废弃物 × 决策/博弈。第三层限定排除纯政策评论类文献，确保纳入的是有模型/决策分析的研究。预估检索量 80-200 篇。

---

## 检索汇总

| # | 方向 | 功能标签 | 优先级 | 配额 |
|:--|:-----|:---------|:------:|:----:|
| 1 | 建筑废弃物回收管理与经济决策 | BG, LR, GAP-RQ2, DISC-RQ2 | P1 | 82篇 |
| 2 | 回收/逆向物流供应链博弈模型 | LR, GAP-RQ1, GAP-RQ2, DISC-RQ1, DISC-RQ2 | P1 | 58篇 |
| 3 | Biform game 理论与应用 | LR, METHOD-基础, METHOD-先例 | P1 | 54篇 |
| 4 | Shapley值在供应链利润分配中的应用 | LR, METHOD-先例 | P2 | 54篇 |
| 5 | 供应链竞合关系（Coopetition） | LR, GAP-RQ1, DISC-RQ1 | P2 | 58篇 |
| 6 | 政府补贴与回收激励机制 | BG, GAP-RQ2, DISC-RQ2 | P2 | 54篇 |
| | **合计** | | | **360篇** |

**建议检索顺序**: D3（Biform game，文献量最少，先锁定方法论基石）→ D2（回收博弈，核心对话对象）→ D1（行业背景）→ D5（竞合理论）→ D4（Shapley值）→ D6（政策补贴）

---

## 标签覆盖检查

| 标签 | 覆盖方向 | 状态 |
|:-----|:---------|:----:|
| BG | D1, D6 | ✅ |
| LR | D1, D2, D3, D4, D5 | ✅ |
| GAP-RQ1 | D2, D5 | ✅ |
| GAP-RQ2 | D1, D2, D6 | ✅ |
| METHOD-基础 | D3 | ✅ |
| METHOD-先例 | D3, D4 | ✅ |
| DISC-RQ1 | D2, D5 | ✅ |
| DISC-RQ2 | D1, D2, D6 | ✅ |
| COMP | 各方向自然扫描 | ✅ |

---

## 需手动补入的经典文献

| 文献 | 论文中的角色 | 功能标签 |
|:-----|:------------|:---------|
| Brandenburger, A. & Stuart, H. (2007). Biform games. *Management Science*, 53(4), 537-549. | Biform game 的奠基性文献，定义了非合作-合作混合博弈框架 | METHOD-基础 |
| Shapley, L.S. (1953). A value for n-person games. *Contributions to the Theory of Games*, 2, 307-317. | Shapley 值的原始定义，合作博弈利润分配的理论基石 | METHOD-基础 |
| Nalebuff, B.J. & Brandenburger, A.M. (1996). *Co-opetition*. HarperCollins. | 竞合理论的奠基性著作 | LR |
| 肖建庄等. 再生混凝土技术相关专著/综述 | 废弃混凝土回收加工技术背景（中文文献，WoS 不收录） | BG |
| 中华人民共和国住房和城乡建设部 (2021). "十四五"城镇生活垃圾分类和处理设施发展规划 | 政策背景引用 | BG |
