# Reviewer Report — Introduction Section

**Manuscript**: Non-cooperative and cooperative game model for waste concrete recycling  
**Role**: Reviewer for *Journal of Construction Engineering and Management* / *Journal of Management in Engineering*  
**Section under review**: §1 Introduction (Lines 122–140 of manuscript.tex)  
**Date**: 2026-04-04

---

## Overall Assessment

**Decision: Major Revision**

The Introduction presents a practically relevant topic — the coopetition dynamics between concrete manufacturers and specialized recyclers in waste concrete recycling. The engineering context (backhaul logistics, processing outsourcing) is interesting and has intuitive appeal. However, the current draft suffers from several critical weaknesses that significantly undermine its readiness for publication in a top-tier engineering management journal. The issues span from missing literature engagement, to vague gap articulation, to structural and rhetorical problems.

---

## Detailed Comments

### 1. Complete Absence of Citations — Fatal Flaw

**Severity: Critical**

The Introduction contains only two citation placeholders — both marked as `(ref)` — and **zero actual references**. For a journal like JCEM or JME, an Introduction of this length (≈6 paragraphs) would typically cite **20–35 references** to establish context, justify gaps, and position the study. The current draft reads as a series of unsupported assertions.

Specific locations where citations are mandatory but missing:

| Claim | Where citation is needed |
|:------|:------------------------|
| "waste concrete accounts for 30–40% of total C&D waste" | Quantitative claim requires authoritative source (e.g., EPA, EU reports, or peer-reviewed surveys) |
| "recycling addresses scarcity of natural aggregates" | Well-known but still needs citation to anchor the argument |
| "backhaul logistics inherent to the construction industry" | This is a key engineering premise of the paper — must cite industry reports or empirical studies |
| "manufacturers typically outsource... through processing fee arrangements" | Is this a documented practice? Where? In which markets? |
| "existing research primarily focuses on government subsidy mechanisms and pricing strategies" | This claim frames the entire gap — without citing the specific papers being critiqued, the gap is unverifiable |
| "non-cooperative and cooperative game-theoretic approach has been widely used in recycling-related studies" | Must cite those studies to demonstrate methodological precedent |

**Recommendation**: Every factual claim, every characterization of the literature, and every methodological justification must be supported by specific references. An Introduction without citations is essentially an opinion piece.

---

### 2. Gap Articulation is Vague and Unsubstantiated

**Severity: Major**

The paper identifies two limitations of existing research (Paragraph 3, Line 129), but both are stated in such broad terms that they are difficult to evaluate:

- **Gap 1** ("few studies have incorporated... transportation cost asymmetry"): Which studies have been examined? How many? A gap claim requires a mini literature map — at minimum, name 3–5 representative papers and explain precisely what they modeled and what they omitted. Otherwise, the reviewer cannot verify whether this gap is genuine or whether the authors simply have not read broadly enough.

- **Gap 2** ("they typically analyze competition and cooperation separately"): Again, which studies? The biform game / coopetition literature in operations research is substantial (Brandenburger & Stuart, 1996; Brandenburger & Stuart, 2007; Feess & Thun, 2014, among others). The claim that no prior work integrates competition and cooperation in a single model is a strong claim that requires careful substantiation. If the authors mean specifically in the C&D waste domain, this must be stated explicitly, and the broader OR/game theory literature must still be acknowledged.

**Recommendation**: Restructure the gap discussion to follow a "what exists → what is missing → why it matters" logic, with explicit references at each step.

---

### 3. Research Questions are Underspecified

**Severity: Major**

- **RQ1** ("does cooperation achieve better equilibrium outcomes than non-cooperation?") — This is an empirically/analytically trivial question if the cooperative game framework already guarantees superadditivity. If the characteristic function is superadditive by construction, then yes, cooperation is always better — making this RQ a foregone conclusion rather than a genuine inquiry. The authors need to clarify what is non-obvious about this question in their specific context.

- **RQ2** ("what are the impacts of key engineering and market parameters...?") — This is too broad to serve as a focused research question. Virtually any parametric model can answer "what happens when parameter X changes." A well-crafted RQ should point to a specific tension, trade-off, or counterintuitive mechanism. For example: "Under what conditions does increasing government subsidies actually decrease the recycler's profit?" or "How does transportation cost asymmetry shift the bargaining power in Shapley allocation?"

**Recommendation**: Sharpen both RQs to highlight the specific analytical tensions or counterintuitive insights the model is designed to reveal. Generic "what are the impacts" questions signal a lack of theoretical ambition.

---

### 4. Methodological Justification is Circular

**Severity: Moderate**

Line 138 states: *"the non-cooperative and cooperative game-theoretic approach has been widely used in recycling-related studies and has proven effective... Therefore, employing the non-cooperative and cooperative game approach... is an effective method."*

This is circular reasoning: "Method X has been used → therefore using Method X is effective." Methodological justification should explain **why this method is uniquely suited to the specific structure of the problem** (simultaneous competition + cooperation, transferable utility, two-player coalition), not merely that it has been used before. The fact that something has been done before is a precedent, not a justification.

Moreover, the term "non-cooperative and cooperative game" is used throughout without specifying the formal framework. Is this a biform game (Brandenburger & Stuart, 2007)? A two-stage game with a cooperative second stage? The exact game structure should be named and cited in the Introduction to signal methodological precision.

**Recommendation**: (a) Name the specific game-theoretic framework (biform game, hybrid game, etc.) and cite its foundational references. (b) Explain why the problem's structure (competition in collection + cooperation in processing) maps naturally onto this framework's architecture.

---

### 5. Structural and Flow Issues

**Severity: Moderate**

The Introduction follows a rough Background → Context → Gap → RQ → Method → Roadmap structure, which is appropriate. However, the execution has problems:

- **Paragraph 1 (Lines 123–125)** and **Paragraph 2 (Lines 127)** are highly repetitive. Both describe the manufacturer-recycler relationship, the competition-cooperation dynamic, and the "lack of clarity." The first paragraph could be condensed to 2–3 sentences of background, with the detailed engineering context in Paragraph 2.

- **Paragraph 3 (Line 129)** jumps to critiquing the literature without having reviewed it. In a typical JCEM/JME paper, the Introduction provides a brief (not exhaustive) literature positioning, while §2 Literature Review provides the detailed review. Currently, the gap paragraph makes strong claims about "existing research" without any evidentiary basis.

- **The roadmap paragraph (Line 140)** is standard but mentions "Section 4 derives the equilibrium analysis" and "Section 5 conducts numerical simulations to verify the theoretical results." However, later in the manuscript, §4 is entirely TODO. The roadmap promises content that does not yet exist — this inconsistency must be resolved before submission.

**Recommendation**: (a) Merge/tighten Paragraphs 1–2 to eliminate redundancy. (b) Add at least a skeletal literature positioning (with citations) before stating the gaps.

---

### 6. Contribution Statement is Missing

**Severity: Major**

A JCEM/JME Introduction typically includes an explicit contribution statement — either a numbered list or a clear paragraph articulating what the paper adds to the body of knowledge. The current draft has none. The reader finishes the Introduction knowing the topic and the RQs but not knowing **what the paper claims to contribute** to theory or practice. This is a significant omission.

The idea.md document lists three theoretical and three practical contributions, but none of these appear in the Introduction.

**Recommendation**: Add a dedicated contribution paragraph (before the roadmap) that clearly states 2–3 specific contributions. Use language like "This study contributes to the literature in three ways: First, ... Second, ... Third, ..."

---

### 7. Engineering Context Lacks Empirical Grounding

**Severity: Moderate**

The backhaul logistics narrative (Paragraph 2) is compelling but reads as an assumption rather than a documented practice. Questions a reviewer would ask:

- Is this outsourcing arrangement (manufacturer collects → recycler processes) the dominant mode in practice, or one of several? What is the evidence?
- In which markets/countries is this arrangement prevalent? The numerical simulation section calibrates to China — this should be foreshadowed in the Introduction.
- Are there published industry reports or case studies documenting this manufacturer-recycler division of labor?

Without empirical grounding, the model's problem description risks being dismissed as a stylized scenario with limited practical relevance — particularly problematic for an engineering management journal that values practical applicability.

**Recommendation**: Cite industry reports, government documents, or empirical studies that validate the manufacturer-recycler cooperation pattern described.

---

### 8. Language and Precision Issues

**Severity: Minor**

- Repeated use of hedging phrases ("remain ambiguous," "remain unclear," "lack of clarity") weakens the argumentative force. State the gap directly.
- "This study develops a model... to guide their economic decision-making" (Line 127) — overpromises. A game-theoretic model provides analytical insights, not direct operational guidance. Tone down or qualify.
- "an effective method" (Line 138) — vague. Effective in what sense? Predictive accuracy? Analytical tractability? Prescriptive value?
- The Introduction does not define "biform game" despite the idea.md positioning the paper around this concept. If this is the methodological identity of the paper, it should appear in the Introduction.

---

## Summary Table

| # | Issue | Severity | Action Required |
|:-:|:------|:---------|:----------------|
| 1 | Zero citations | Critical | Add 20–35 references throughout |
| 2 | Gaps unsubstantiated | Major | Cite specific papers to validate each gap claim |
| 3 | RQs underspecified | Major | Sharpen to highlight specific tensions/trade-offs |
| 4 | Circular method justification | Moderate | Explain structural fit, name the framework |
| 5 | Redundant paragraphs, structural flow | Moderate | Merge Paragraphs 1–2, add literature positioning |
| 6 | No contribution statement | Major | Add explicit numbered contributions |
| 7 | Engineering context ungrounded | Moderate | Cite industry evidence for outsourcing model |
| 8 | Language precision | Minor | Reduce hedging, define key terms |

---

## Decision Rationale

The paper addresses a relevant problem at the intersection of construction waste management and game theory — a topic appropriate for JCEM/JME. However, the Introduction in its current form would not survive peer review at either journal. The complete absence of citations alone would likely trigger a desk reject at many journals. Combined with unsubstantiated gap claims, missing contributions, and underspecified research questions, the Introduction fails to establish the scholarly foundation needed to motivate the study.

The good news: the underlying research idea (biform game for coopetition in waste concrete recycling, with backhaul logistics as a distinguishing engineering feature) has genuine potential. The problems are largely in the writing and scholarly positioning, not in the research concept itself. A thorough revision addressing the above points should make this Introduction competitive.

**Verdict: Major Revision — resubmit after addressing all critical and major issues.**
