<Introduction>
**第一段：废弃混凝土回收很重要，对双碳绿色发展废物利用……等都有作用+国家政策支持+当前痛点（你补充）+实践问题（在此背景下，需要构建合理的废弃混凝土回收体系，指引企业参与废弃混凝土回收并做出正确决策，以提高其积极性。）

**第二段：随着对环境的重视，回收建筑垃圾的关注，而废弃混凝土占建筑垃圾的70%（我随便说的数，你看看应该是多少，这里加ref），废弃混凝土回收工作也得到重视，许多企业参与到这一工作，包括混凝土制造商和回收商；但是废弃混凝土回收涉及……等诸多技术，程序（这里想表达意思就是回收混凝土需要的技术水平较高，同时需要投资设备），制造商通常不具备独立处理的能力或者不愿意投入大量成本开展这一工作。但是他们存在回收渠道的优势，他们可以利用这个优势委托回收商来帮助进行处理，从而解决技术不足的问题。而对于回收企业而言, 利用其技术优势，从市场收购废弃混凝土和帮助制造商合作处理可以有效满足产能, 进而增加利润。（参考陈庭强那篇pdf的引言第二段，合理的表述制造商和回收商的关系）。文件or研究指出，支持这种委托处理模式。因此，本研究将构建这种废弃混凝土回收模式，探讨各参与方的决策。

**第三段：现有研究综述分类，现有关于废弃混凝土回收的文献聚焦于……方面，例如。废弃混凝土回收的……点没有考虑到，没考虑到（参与主体的积极性，决策，利润分配；需要关注回收技术及市场竞争导致的回收模式单一、梯次利用收益不高的问题, 以及回收技术起步晚、成熟度不高对回收收益的影响）。此外相较于其他回收（光伏回收，电池回收），废弃混凝土回收（阐述工程管理情境特点）。因此我们将基于废弃混凝土回收的工程管理情境，纳入各参与方的经济效益进行决策

**第四段：提出rq
rq：1.在废弃混凝土回收的竞合关系模式下，M和R将如何进行废弃混凝土的定价回收（针对定价竞争将如何决策）
2.双方如何通过合作实现利润的提升（利润最大化）

**第五段：为解决上述问题，我们采用非合作合作两型博弈，构建制造商和回收商针对废弃混凝土回收的竞合关系模型。非合作合作博弈对本研究问题的适配性：（参考陈庭强那篇文章引言倒数第二段，说一说这个方法如何适用于这个废弃混凝土回收的情境，结合我前面几段说的）。最后说因此, 借助两型博弈分析废弃混凝土回收过程中参与主体的回收策略以及利润分配问题是一条有效且可行的途径.

**第六段：本文其他结构

<Literature review>

<废弃混凝土回收>
文献综述表格

<非合作-合作博弈>


<问题描述>
本文考虑由传统混凝土制造商M（简称制造商M）与专业建筑固废回收商R（简称回收商R）构成的废弃混凝土回收供应链。制造商M与回收商R均参与前端废弃混凝土的回收工作。回收商R拥有专业的建筑固废处理技术与设备，负责对收集到的废弃混凝土进行破碎、筛分、除杂及强化等资源化处理，将其转化为再生混凝土骨料。为方便分析，做出如下假设：
假设1： 制造商M与回收商R确定对废弃混凝土产出方（如建筑施工单位或拆除承包商）的回收价格为 $(p_M, p_R)$。由于两者均参与废弃混凝土的回收，彼此之间存在回收竞争关系，设竞争强度为 $\beta$。此外，回收量也受回收价格影响，即废弃混凝土产出方对废弃混凝土回收价格的敏感程度，用 $\alpha$ 表示。假定市场上有充足的废弃混凝土供回收，且回收商R的产能足以处理所有回收量。回收量函数为：$$q_i = \alpha p_i - \beta p_j \quad (i,j \in \{M, R\}, i \neq j)$$由式可知，$\alpha$ 的值越大，表明废弃混凝土产出方对价格越敏感，回收量越高；$\beta$ 的值越大，表明制造商M与回收商R之间争夺废弃混凝土的竞争越激烈。
假设2： 当前，不同处理工艺对废弃混凝土的资源化利用效率差异显著。本文用再生混凝土骨料转化率来描述回收商R的回收处理能力，且 $k \in [0,1]$。提升该转化率（例如引入强化去砂浆技术、多级风选技术等）需要投入固定的技术与设备改造成本。假设投资成本函数为：$$C(k) = \frac{1}{2} c k^2$$其中，$c$ 表示投资成本系数。该式表明，投资成本与再生混凝土骨料转化率之间呈二次函数关系。
假设3： 在实际工程中，传统混凝土制造商往往缺乏深加工环保设备或受限于场地与环保资质，因此需要将其回收的废弃混凝土委托给专业的回收商R进行集中处理。假定制造商M委托回收商R处理废弃混凝土，需支付单位委托处理费用为 $w$；而回收商R处理单位废弃混凝土的实际操作成本（如水电、设备折旧、人工等）为 $m$。
假设4： 假设废弃混凝土被完美转化为最高品质再生骨料时的单位潜在价值为 $\theta$。那么，在实际的再生混凝土骨料转化率 $k$ 下，单位废弃混凝土回收后的实际提取价值为 $\theta k$。考虑到“无废城市”建设背景，为鼓励建筑垃圾资源化利用，政府会给予每单位废弃混凝土回收处理的补贴额为 $s$。
假设5： 为获取高品质的再生骨料并维持稳定的代工合作，制造商M愿意与回收商R共担提升再生混凝土骨料转化率的投资费用。设制造商M分担的比例为 $(1-n)$，由回收商R承担的比例为 $n$，其中 $n \in [0,1]$。当 $n=1$ 时表示全部投资费用由回收商R独自承担。

以下是表格：
符号,含义
θ,单位废弃混凝土转化为最高品质再生骨料的潜在价值
α,废弃混凝土产出方对回收价格的敏感程度
β,"制造商与回收商争夺废弃混凝土的竞争强度，β∈[0,1]"
pM​,制造商M支付给废弃混凝土产出方的单位回收价格
pR​,回收商R支付给废弃混凝土产出方的单位回收价格
qM​,制造商M的废弃混凝土回收量
qR​,回收商R的废弃混凝土回收量
n,"回收商R承担的设备与技术投资费用比例，n∈[0,1]"
k,"回收商R的再生混凝土骨料转化率，k∈[0,1]"
c,投资成本系数
m,回收商R处理单位废弃混凝土的实际操作成本
s,政府对每单位废弃混凝土回收处理的补贴额
w,制造商M支付给回收商R的单位委托处理费用
Πi​,"参与主体 i 的利润函数，i∈{M,R}"

利润函数：
$$\Pi_M = (\theta k - p_M - w + s)(\alpha p_M - \beta p_R) - (1 - n)\frac{c k^2}{2}$$
$$\Pi_R = (\theta k - p_R - m + s)(\alpha p_R - \beta p_M) + (w - m)(\alpha p_M - \beta p_R) - n\frac{c k^2}{2}$$

<模型构建>

<Title>考虑碳限额与交易机制的两阶段废弃混凝土回收处理的竞合策略研究
<Introduction>新版

第一段：由于近几十年来建筑行业的快速发展，建筑施工与拆除（C&D）废弃物的产生量呈现急剧增长态势，其中超过一半的C&D建筑废弃物是废弃混凝土（碳捕集技术那篇的引言第一段(Zengfeng et al. 2020).）。由于这些废弃物对环境和社会都产生了损害，迫切需要对其回收进行管理。其中废弃混凝土因其具备再生与可利用价值已被证明对其进行回收处理具备缓解环境压力和建筑原材料短缺的潜力。许多国家，尤其是自然资源有限的发达国家，已经广泛采用了再生混凝土。然而，废弃混凝土回收管理的推广因技术成熟度不高，经济效益模糊，政策尚未完善等而受到阻碍，导致相关企业的参与积极性不高（补贴差异(Liu et al., 2021; Ma et al., 2020).）。面对较高的技术成本和市场的不确定性，混凝土制造商和回收商往往不具备独立克服这些障碍的能力，需要通过跨企业协调实现优势互补与风险共担等模式以寻求废弃混凝土回收的经济效益最大化。因此，如何有效协调废弃混凝土回收管理过程，已成为制约废弃混凝土回收产业发展的重要管理决策难题。

第二段：尽管废弃混凝土回收在节约原生资源方面具有显著优势，但其处理过程本身往往伴随着不容忽视的碳排放。现有废弃混凝土回收处理的主流工艺通常是破碎分离以及煅烧热处理为主，该过程中仍会产生大量二氧化碳。在全球积极推进脱碳目标的背景下，回收产业的“二次碳足迹”也是亟待规制的议题。在应对产业高碳排放方面，各国政府陆续出台了多项环境政策，其中碳限额与交易（Cap-and-Trade）机制作为一种基于市场导向的代表性政策工具脱颖而出 (Zhengxiaoxue等引用)。该机制通过设定碳排放上限并允许企业自由交易排放配额，不仅激励企业寻求更低成本的减排路径，还在经济效益与环境保护之间提供了灵活的平衡机制 (南江霞的引用【1】)。包括中国和美国在内的多个国家已广泛实践该政策，证实了其在抑制碳排放方面的有效性 (Yenipazarli 2019)。对于废弃混凝土回收产业来说，碳配额的约束与交易价格的波动直接重塑了参与主体的成本结构和利润边界，驱使其在制定经济决策时必须考虑碳排放的经济影响。因此，将碳限额与交易机制纳入研究框架，探究其如何干预废弃混凝土回收的经济效益及微观主体的决策行为，显得尤为必要。

第三段：在废弃混凝土回收处理过程中，包含混凝土制造商和回收商两大参与主体。混凝土制造商综合其渠道优势及回收处理的技术成本高昂等考量会将前端收集的废弃混凝土交由专业的回收商进行处理，形成“委托处理模式”。同时，双方在这一纵向互动中呈现出复杂的“竞合（Co-opetition）”动态。一方面，在前端收集环节，为了争夺市场上有限的废弃混凝土资源，双方围绕回收定价展开非合作竞争；另一方面，在后端处理环节，为了突破技术瓶颈并提升系统整体利润，双方也会选择开展横向合作，共同分担技术投资以提高废弃混凝土转化为再生骨料的转化率。这导致前端的回收定价策略必须考虑双方摊销合作投资成本的能力；而合作技术投资带来的转化率提升又将影响双方在定价竞争中的利润空间与市场优势。随着碳限额与交易政策的引入，碳排放配额的收紧与碳交易价格的波动冲击着回收商在处理废弃混凝土过程中的经济收益。这种政策环境与市场竞争叠加的不确定性，使得双方在利润分配上也面临利益博弈，导致制造商和回收商在推进产业升级和关键技术投资时陷入“战略犹豫”。因此，亟需构建一个系统的理论框架，对这种复杂的竞合机制进行系统的剖析。


第四段：然而，现有模型中，无论是非合作博弈论还是合作博弈论都不足以解决这种因竞争与合作相互作用而影响决策的竞合机制。为此，本文提出了一个两阶段的废弃混凝土回收的博弈框架，同时纳入非合作博弈与合作博弈，对混凝土制造商和回收商的竞合策略并行分析。非合作策略可视为混凝土制造商和回收商之间的回收竞争，他们不产生最终均衡解决方案，而是建立竞争背景，使其在合作投资中做出决策。与此同时，合作策略由双方共同决定。这些合作策略产生的利润分配随后成为解决最终非合作策略的关键利润函数。此外我们还将这种竞合策略与纯非合作场景进行比较。具体而言，本研究致力于解决以下研究问题：
RQ1:碳限额与交易机制将对废弃混凝土回收中混凝土制造商和回收商的在非合作策略和基于两型博弈的竞合策略的经济决策有什么影响？
RQ2:在废弃混凝土回收中，相比于纯非合作模式采用基于两型博弈的竞合策略将在何种市场与政策边界条件下实现系统及各主体经济效益的帕累托改善？

第五段：该两型博弈框架同时探讨了非合作阶段的废弃混凝土回收定价及回收量竞争，以及合作阶段的投资分担及碳减排效益考量，并基于废弃混凝土回收的委托处理模式进行考量。该框架还考虑了政府补贴的影响，以及制造商和回收商因物流成本差异及技术差异所带来的互动的复杂性。与Huqidan关于在单阶段建筑废弃物的竞争合作的研究及关于zhengxiaoxue对建筑废弃物回收中政府补贴机制差异的研究不同。我们揭示了宏观碳限额政策冲击下，微观企业主体“横向技术合作”与“纵向定价竞争”的内生耦合机制。 我们不仅量化了多阶段互动中的政策因素影响，并为废弃混凝土产业在“双碳”目标下的利益分配契约设计、关键技术投资决策制定，以及政府配套补贴政策的动态调整，提供了理论见解与管理启示。

第六段：本文其他结构如下……

<Module Formulation>
我们考察了一个两阶段废弃混凝土回收模型
我们开发了两种不同的模型并进行比较，一种是考虑碳减排与交易机制的非合作废弃混凝土回收模型，另一种是考虑碳减排与交易机制的结合合作投资的两型博弈模型。
在非合作博弈模型中，混凝土制造商和回收商独立做出定价决策，以在两阶段最大化自身利益。第一阶段，混凝土制造商和回收商首先确定废弃混凝土的回收单价
在两型博弈模型中，

<3.2 non-cooperative game module>
……
The proof of Proposition 1 is provided in Appendix A.
proposition 1.
列出最优结果
<3.3 biform game module>
在本节中，我们将非合作博弈模型扩展到非合作-合作两型博弈框架，并探讨其对经济效益的影响。基于上一节的场景，我们进一步假设混凝土制造商愿意与回收商建立技术投资合作。在该基础上，我们建立了一种基于两型博弈的废弃混凝土回收管理框架，结合非合作博弈和合作博弈以实现经济利益最大化。我们假设混凝土制造商和回收同意采取这种两型博弈结构来制定竞合策略，决策框架如图所示。
（此处放图，我自己画）
在非合作博弈，混凝土制造商和回收商通过纳什均衡非合作的决定定价策略。与section 3.2non-cooperative game module的情境不同，混凝土制造商和回收商在两型博弈进行非合作定价决策时，会根据合作时的技术投资合作，预测最终收益会如何通过合作博弈分配。因此，这部分定价策略不会产生最终收益，但创造了竞争环境。
在合作博弈中，混凝土制造商和回收商进行技术投资合作，混凝土制造商帮助回收商分担一定比例的技术研发成本。双方可以选择是否组建合作联盟，为了确定利益分配机制，我们首先计算联盟的特征值。然后，我们利用沙普利值根据联盟的特征函数分配合作收益。该分析是在非合作部分中给出的竞争环境（即定价策略组合 
 ）下计算的。合作博弈中分配的利润将被视为非合作部分双方的目标函数，我们通过最大化该利润函数来推导均衡解。
3.3.1 cooperative game
……
3.3.2 non-cooperative game
……

propostion 2.
propostion 3.
propostion 4.

<Numerical analysis>
数值模拟：变化参数：敏感系数alpha；竞争强度beta；补贴s；单位废弃混凝土价值theta（无需设置直接得到）；委托处理费用w，处理成本m；运输成本miuM，miuR；其他设置参数：c（成本系数）;单位碳配额G；碳交易单位价格pc；单位废弃混凝土处理产生量，无需设置直接得到：k（转化率）；n（分担比例）
分析参数：p；q；pi（利润）；
数值模拟：为了更加直观呈现上述结果，探究回收价格敏感系数，竞争强度，回收价值，运输成本等参数变化，分别对回收价格，回收量，分担比例，处理技术水平等因素的影响，本文借助MATLAB 2023b软件进行数值分析。
废弃混凝土回收是国际性议题，然而不同国家不同背景下关于废弃混凝土的各项参数都有所不同。为了确保数值模拟符合实际情境，我们将数值模拟的背景置于中国情境下。原因有二：首先中国对废弃混凝土回收很重视，如……（举个实际例子，出台多项政策等）；再者，中国废弃混凝土回收处理正处于起步发展阶段，各企业都在积极进行技术改造升级并寻求研发合作。结合本研究的非合作合作博弈情境，有利于为企业决策与政府指引提出建设性意见。结合中国近年来发布的各项政策，研究报告，项目报道，领域内专家访谈及相关文献，我们对各参数的设置和理由如下：

对于回收价格敏感系数alpha，该系数反映了对价格波动的反应剧烈强度，越大表示对价格变化越敏感。根据Liu的《上海建筑垃圾资源化利用情况调研报告》，废弃混凝土的回收价格大概在10-15/吨，同时文献（陈庭强）对该系数的设置，我们设置alpha=15/10=1.5

对于竞争强度beta，根据《中国建筑垃圾回收处理行业概览》，废弃混凝土等建筑垃圾的年复合增长率为13.4%。由于混凝土制造和回收处理都需要较大的资金投入与技术成本，有一定的行业门槛，因此中国大型的混凝土制造商和回收商企业数量基本不变。在各企业原有的渠道资源较为稳定的情况下，我们将每年新增的废弃混凝土资源作为竞争强度，故设beta=0.134

对于回收商处理成本m，肖在《世界环境》杂志的报道中指出，每10万方废弃混凝土处理只需要800万元，因此我们设m=80元/方（32/方）
而对于支付费用w，我们结合几家将废弃混凝土处理作为主营业务的a股上市公司年报，如中再资源，中国天楹，上海环境等，从中我们发现各企业的毛利率大概在7.88%-13.04%，因此我们取平均毛利率为9.84%来测算w。即w=m*9.84%+m=88元/方（35/方）（已改为50）

对于政府补贴s，中国政府针对废弃混凝土处理相关企业已出台多项补贴措施，包括但不限于减免增值税，报销运输成本等。结合2025年江⻄省南城县建筑垃圾处理特许经营权项⽬披露数据，政府将基于废弃混凝土等建筑垃圾的回收量给予35元/吨的补贴。经单位换算，我们设置s=87.5元/方。

对于运输成本，我们进行了市场调研，对几家企业进行询价，并对工程造价从业人员进行了访谈，最终确认miuM=25/方，miuR=44/方

对于投资成本系数c，根据《中国建筑垃圾回收处理行业概览》所披露的废弃混凝土回收处理相关设备如破碎机，震动给料机，除铁器等设备的价格范围及使用比例，我们对价格范围取中位数并按比例加权平均，设置c=135000

对于基准值theta，根据Liu的《上海建筑垃圾资源化利用情况调研报告》，废弃混凝土转化为再生骨料对外销售价格为50-60元/吨，我们取中位数并进行单位换算，得到theta=137.5元/方。

对于pc（参考南江霞论文）：参考 2021年中国各个碳交易试点的价格在 50 元/吨 - 80 元/吨,因此取中间值设置pc=65

对于G（参考南江霞论文中参考sun的论文）=300（实际访谈，论文，政策）

对于e，根据欧洲环境署（EEA）的估算，处理1吨废弃混凝土（包括收集、破碎、运输等资源化利用过程）平均会产生约 0.02至0.05吨（即20至50公斤） 的二氧化碳，我们取e=0.035

对于pc：参考 2021年中国各个碳交易试点的价格在 50 元/吨 - 80 元/吨,因此取中间值设置pc=65

对于G（参考sun的论文）=300

对于e，根据欧洲环境署（EEA）的估算，处理1吨废弃混凝土（包括收集、破碎、运输等资源化利用过程）平均会产生约 0.02至0.05吨（即20至50公斤） 的二氧化碳，我们取e=0.035

画图
1.非合作博弈与合作博弈的对比
（1）碳排放交易价格pc对两类博弈的利润pi的影响
（2）竞争强度对两类博弈的利润pi的影响
（3）成本系数对两类博弈的利润pi的影响
2.两型博弈各参数的敏感性分析
（1）alpha
（2）s
（3）theta
（4）w m
（5）mu diff

<Conclusion>
本研究构建了一个包含混凝土制造商和回收商的废弃混凝土回收供应链两阶段两型博弈模型。该模型系统地考察了在碳交易机制下，前端收集定价竞争与后端技术投资合作之间的内生耦合机制 。通过将两型博弈的竞合策略与非合作模型进行对比，并分析市场、政策和工程参数的异质性影响，本研究得出以下主要结论：
This study constructs a two-stage biform game model for a waste concrete recycling supply chain comprising a traditional concrete manufacturer and a specialized recycler. The model systematically investigates the endogenous coupling mechanisms between front-end collection pricing competition and back-end technology investment cooperation under the cap-and-trade mechanism. By comparing the biform game model with a non-cooperative game model, and analyzing the heterogeneous impacts of market and engineering parameters, the study draws the following principal conclusions:

首先，我们开发了一个融合非合作定价竞争与合作技术投资的两型博弈框架。在合作博弈阶段，我们运用特征函数和Shapley值完善了混凝土制造商和回收商的利益分配机制。数学证明表明，该合作博弈具有凸性和超可加性，能够确保了各主体合作的稳定性。通过将这些稳定的分配结果作为非合作阶段的目标函数，进一步巩固了这一稳定性，有效化解了技术升级中的“战略犹豫”，并保证了最终均衡的实现。
First, we have developed a biform game model that integrates both non-cooperative pricing competition and cooperative technology investment. In the cooperative game stage, we refine the benefit allocation mechanism for supply chain members by employing characteristic functions and the Shapley Value. Our rigorous mathematical proofs demonstrate that the cooperative game is convex and super-additive, which ensures the stability of the agents' cooperative efforts. This stability is further reinforced by utilizing these distribution outcomes as the objective functions in the non-cooperative stage, effectively resolving the "strategic hesitation" in technological upgrades and guaranteeing a final equilibrium.

Second, the comparison between the non-cooperative game model and the biform game model demonstrates that the co-opetition strategy can achieve a Pareto improvement. Under the cap-and-trade mechanism, the results indicate that the biform game framework provides a stronger economic buffer against fluctuations in the carbon trading price ($p_c$). While an increase in carbon prices exerts downward pressure on the profitability of both parties in both scenarios, the profit levels under the biform game remain consistently higher and exhibit greater resilience than the non-cooperative baseline. This finding confirms that the cooperative investment mechanism effectively mitigates the economic risks associated with environmental policy volatility.

Third, our research uncovers that external market and engineering parameters exert distinct and occasionally asymmetric impacts on the operational strategies and profit distribution landscape. The findings indicate that an increase in the price sensitivity coefficient leads to a divergence in pricing strategies, where the manufacturer raises prices while the recycler lowers them to avoid vicious competition. Enhancements in the government subsidy and the potential recycled value both stimulate total system scale, but they alter the recycler's risk-return profile differently (risk mitigation vs. marginal return amplification). Furthermore, an excessive internal outsourcing fee severely suppresses the manufacturer's collection volume, which indirectly destroys the scale economies required by the recycler, leading to a monotonic decline in systemic profits. Similarly, the expansion of the transportation cost differential triggers external logistics friction, ultimately restricting the system's technological advancement.

<Theoretical implications>
This study contributes to the related literature on construction and demolition waste management and low-carbon recycling supply chains in two ways:

First, this study constructs a two-stage biform game framework for waste concrete recycling, which expands the application boundaries of biform game theory. By capturing the inherent resource asymmetry—the manufacturer's reverse logistics advantage and the recycler's technological expertise—within this framework, it overcomes the limitations of traditional single-stage games. This approach provides a novel theoretical reference and an analytical paradigm for economic decision-making and supply chain coordination research in related recycling fields.

Second, this research innovatively introduces the carbon emission reduction and cap-and-trade mechanism into the research of waste concrete recycling management. Previous operational models generally treat environmental policies merely as exogenous cost penalties. By integrating the carbon market dynamics with cooperative investment, our research theoretically demonstrates how strategic alliances can transform carbon compliance from a static constraint into a catalyst for system upgrading. This quantifies the "buffering effect" of cooperation against carbon price volatility, thereby advancing the theory of low-carbon supply chain resilience.

<Practical implications>
First, concrete manufacturers and specialized recyclers should establish cooperative alliances. The results demonstrate that this is the optimal path for maximizing both systemic and individual profits. To operationalize this alliance effectively, firms should transition from traditional transactional outsourcing to deep strategic integration. Specifically, partners should design "KPI-linked cost-sharing contracts." Rather than a simple, flat capital injection, the manufacturer's financial support should be contractually tied to the recycler's technological performance metrics, such as the aggregate conversion rate. Furthermore, the alliance should implement a joint logistics dispatch system. By integrating data across the supply chain, the recycler can coordinate its processing schedule with the manufacturer's delivery routes, fully exploiting the manufacturer's reverse logistics advantage. This operational integration ensures a stable, large-scale supply of waste concrete, thereby securing the economies of scale necessary for back-end profitability.

Second, participants in the waste concrete recycling supply chain should pay close attention to carbon emissions and the cap-and-trade mechanism, treating them as key operational variables rather than mere compliance costs. To effectively respond to carbon market volatility, concrete manufacturers and recyclers are encouraged to explore an internal "carbon risk-sharing and dividend" mechanism. When negotiating the outsourcing fee and the technology investment ratio, partners can dynamically factor in the projected carbon trading prices. For instance, the cooperative contract could include a floating adjustment clause: during periods of high carbon prices, the manufacturer temporarily increases its cost-sharing proportion or transfer payments to buffer the recycler's compliance burden; conversely, any financial dividends gained from selling surplus carbon quotas—achieved through the jointly funded high-efficiency waste concrete processing technology—could be shared between both parties. Additionally, partners can consider implementing joint carbon accounting across the waste concrete collection and processing stages to accurately track and certify emission reductions, helping to optimize their returns in the external carbon market.

Third, government policymakers can shift from uniform industry incentives to targeted structural interventions. To address the inherent capability asymmetry in the market, authorities should implement specialized logistics subsidies exclusively for dedicated recyclers to neutralize their transportation cost disadvantages compared to manufacturers. Additionally, regulators need to maintain a predictable carbon market environment with stable price guidance, which provides enterprises with the long-term confidence required to commit to capital-intensive cooperative investments. Policymakers could also promote industry-standard template contracts for "delegated treatment" that formally incorporate fair technology cost-sharing clauses, thereby reducing negotiation friction between firms.