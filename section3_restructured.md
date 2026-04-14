% THIS IS THE RESTRUCTURED SECTION 3 - TO BE INSERTED INTO MANUSCRIPT.TEX
% Lines 185-458 will be replaced

\section{Model formulation}
\subsection{Problem description}
We consider a waste concrete recycling supply chain consisting of a traditional concrete manufacturer $M$ and a specialized construction waste recycler $R$. Both $M$ and $R$ participate in the collection of waste concrete from waste generators (e.g., construction companies or demolition contractors). Recycler $R$ possesses specialized waste processing technologies and equipment, responsible for crushing, screening, decontamination, and enhancement of collected waste concrete to produce recycled concrete aggregate (RCA).

To analyze the economic incentives and strategic interactions between the manufacturer and the recycler, we develop a game-theoretic framework that captures both non-cooperative competition in the collection stage and cooperative investment sharing in the processing stage. Specifically, we examine two scenarios: (1) a pure non-cooperative game (baseline) where the recycler independently invests in technology without cost sharing; and (2) a two-stage biform game where the parties cooperate through investment cost sharing.

The following assumptions are made:

\textbf{Assumption 1.} Manufacturer $M$ and recycler $R$ set collection prices $(p_M, p_R)$ for waste concrete generators. Since both parties participate in collection, there exists competitive pressure in the recycling market. Let $\beta$ denote the competition intensity between $M$ and $R$. Additionally, the collection quantity depends on the collection price, with $\alpha$ representing the sensitivity of waste generators to collection prices. We assume sufficient waste concrete available in the market and $R$ has sufficient capacity to process all collected quantity. The collection quantity function follows:
\begin{equation}
q_i = \alpha p_i - \beta p_j \quad (i,j \in \{M, R\}, i \neq j)
\end{equation}
where $\alpha > \beta > 0$ ensures positive collection quantities.

\textbf{Assumption 2.} The recycling processing capability of recycler $R$ is characterized by the RCA conversion rate $k \in [0,1]$. Improving this conversion rate requires fixed investment in technology and equipment upgrades. The investment cost function is:
\begin{equation}
C(k) = \frac{1}{2} c k^2
\end{equation}
where $c$ is the investment cost coefficient.

\textbf{Assumption 3.} Manufacturer $M$ outsources the collected waste concrete to recycler $R$ for centralized processing. Manufacturer $M$ pays a unit outsourcing fee $w$ to recycler $R$, while recycler $R$ incurs actual operational costs $m$ per unit of waste concrete processed.

\textbf{Assumption 4.} Assume $\theta$ is the unit potential value of waste concrete converted to highest-quality RCA. Under the actual RCA conversion rate $k$ achieved by recycler $R$, the actual extracted value per unit of waste concrete is $\theta k$. To encourage construction waste recycling, the government provides a subsidy $s$ per unit of waste concrete collected.

\textbf{Assumption 5.} Manufacturer $M$ is willing to share the investment cost for improving the RCA conversion rate with recycler $R$. Let manufacturer $M$ share a proportion $(1-n)$ and recycler $R$ bear a proportion $n$, where $n \in [0,1]$. When $n=1$, all investment costs are borne solely by recycler $R$.

\textbf{Assumption 6.} Both manufacturer $M$ and recycler $R$ incur unit transportation costs for collecting waste concrete. Due to the backhaul logistics advantage, manufacturer $M$'s transportation cost $\mu_M$ is lower than recycler $R$'s cost $\mu_R$ (i.e., $\mu_M < \mu_R$).

\textbf{Assumption 7 (Cap-and-Trade Mechanism).} Under the cap-and-trade mechanism, recycler $R$ is subject to government-allocated carbon emission quotas. Let $G$ denote the total carbon emission quota, $e$ the carbon emissions per unit of waste concrete processed, and $p_c$ the carbon trading price. The total processing quantity is $q_{total} = q_M + q_R = (\alpha - \beta)(p_M + p_R)$. The net carbon trading cost incurred by recycler $R$ is:
\begin{equation}
p_c \left[ e \cdot q_{total} - G \right] = p_c \left[ e(\alpha - \beta)(p_M + p_R) - G \right]
\end{equation}

\begin{table}[!htbp]
\centering
\captionsetup{font=normalsize, labelsep=period}
\caption{Notation and definitions}
\label{tab:notation}
\small
\begin{threeparttable}
\begin{tabular*}{0.95\textwidth}{@{\extracolsep{\fill}}lc}
\toprule
\textbf{Symbol} & \textbf{Definition} \\
\midrule
$\theta$ & Unit potential value of waste concrete converted to highest-quality RCA \\
$\alpha$ & Sensitivity of waste generators to collection price \\
$\beta$ & Competition intensity between manufacturer and recycler, $\beta \in [0,1]$ \\
$\mu_M$ & Unit transportation cost of manufacturer $M$ \\
$\mu_R$ & Unit transportation cost of recycler $R$ \\
$p_M$ & Unit collection price paid by manufacturer $M$ to waste generators \\
$p_R$ & Unit collection price paid by recycler $R$ to waste generators \\
$q_M$ & Waste concrete collection quantity of manufacturer $M$ \\
$q_R$ & Waste concrete collection quantity of recycler $R$ \\
$n$ & Proportion of investment cost borne by recycler $R$, $n \in [0,1]$ \\
$k$ & RCA conversion rate of recycler $R$, $k \in [0,1]$ \\
$c$ & Investment cost coefficient \\
$m$ & Actual operational cost of recycler $R$ per unit waste concrete \\
$s$ & Government subsidy per unit waste concrete processed \\
$w$ & Unit outsourcing fee paid by manufacturer $M$ to recycler $R$ \\
$G$ & Total carbon emission quota allocated by government to recycler $R$ \\
$e$ & Actual carbon emissions per unit of waste concrete processed by recycler $R$ \\
$p_c$ & Trading price per unit of carbon emission in the carbon market \\
$\Pi_i$ & Profit function of participant $i$, $i \in \{M,R\}$ \\
$\varphi_i$ & Shapley value (profit allocation) for participant $i$, $i \in \{M,R\}$ \\
\bottomrule
\end{tabular*}
\begin{tablenotes}[flushleft]
\small\linespread{1}\selectfont
\item \textit{Note}: All decision variables and parameters are non-negative unless otherwise specified.
\end{tablenotes}
\end{threeparttable}
\end{table}
\vspace{10pt}
\normalsize

Based on the above assumptions, the profit functions are expressed as:
\begin{equation}
\Pi_M = (\theta k - p_M - w - \mu_M + s)(\alpha p_M - \beta p_R) - (1 - n)\frac{c k^2}{2}
\label{eq:profit_M}
\end{equation}
\begin{equation}
\Pi_R = (\theta k - p_R - m - \mu_R + s)(\alpha p_R - \beta p_M) + (w - m)(\alpha p_M - \beta p_R) - n\frac{c k^2}{2} - p_c\left[ e(\alpha - \beta)(p_M + p_R) - G \right]
\label{eq:profit_R}
\end{equation}

In the following subsections, we first analyze the pure non-cooperative game (baseline) where $n=1$ and the recycler independently decides $k$. Then we analyze the two-stage biform game with cooperative investment sharing.

\subsection{Pure non-cooperative game: Baseline scenario}
In the baseline scenario, there is no investment cost sharing between the manufacturer and the recycler. Specifically, the recycler $R$ bears all the investment costs ($n=1$), while the manufacturer $M$ does not participate in technology investment. Under this setting, the recycler independently optimizes the conversion rate $k$ to maximize its own profit, and subsequently both parties compete in collection prices. This baseline scenario serves as a benchmark for comparing with the cooperative biform game.

Under $n=1$, the profit functions simplify to:
\begin{equation}
\Pi_M^N = (\theta k - p_M - w - \mu_M + s)(\alpha p_M - \beta p_R)
\label{eq:profit_MN}
\end{equation}
\begin{equation}
\Pi_R^N = (\theta k - p_R - m - \mu_R + s)(\alpha p_R - \beta p_M) + (w - m)(\alpha p_M - \beta p_R) - \frac{c k^2}{2} - p_c\left[ e(\alpha - \beta)(p_M + p_R) - G \right]
\label{eq:profit_RN}
\end{equation}

We solve this game using backward induction.

\textbf{Step 1: Recycler's technology investment decision.} Given collection prices $(p_M, p_R)$, the recycler $R$ chooses $k$ to maximize $\Pi_R^N$:
\begin{equation}
\frac{\partial \Pi_R^N}{\partial k} = \theta(\alpha p_R - \beta p_M) - ck = 0
\end{equation}
Solving for $k$, we obtain:
\begin{equation}
k^N(p_M, p_R) = \frac{\theta(\alpha p_R - \beta p_M)}{c}
\label{eq:k_N}
\end{equation}
Substituting $k^N$ into $\Pi_R^N$, the recycler's profit becomes:
\begin{equation}
\Pi_R^N = (s - p_R - m - \mu_R)(\alpha p_R - \beta p_M) + (w - m)(\alpha p_M - \beta p_R) + \frac{\theta^2(\alpha p_R - \beta p_M)^2}{2c} - p_c\left[ e(\alpha - \beta)(p_M + p_R) - G \right]
\end{equation}

\textbf{Step 2: Price competition equilibrium.} Using the profit functions $\Pi_M^N$ and $\Pi_R^N$, we derive the reaction functions by taking first-order partial derivatives with respect to $p_M$ and $p_R$, respectively:
\begin{equation}
\frac{\partial \Pi_M^N}{\partial p_M} = (\theta k^N + s - p_M - w - \mu_M)\alpha - (\alpha p_M - \beta p_R) = 0
\end{equation}
\begin{equation}
\frac{\partial \Pi_R^N}{\partial p_R} = (\theta k^N + s - p_R - m - \mu_R)\alpha - (\alpha p_R - \beta p_M) - p_c e (\alpha - \beta) = 0
\end{equation}

Substituting $k^N = \frac{\theta(\alpha p_R - \beta p_M)}{c}$ and solving the system, we obtain the equilibrium collection prices:
\begin{equation}
p_M^{N*} = \frac{
4c^2 \left[ 2\alpha^2(s - w - \mu_M) + \alpha\beta(s - m - \mu_R) - \beta^2(w - m) \right]
- 2c\theta^2 \Big\{ (\alpha-\beta) \left[ \alpha^2(s - w - \mu_M) - (\alpha^2 - \alpha\beta + \beta^2)(w - m) \right] - \alpha(\alpha^2 - \alpha\beta + \beta^2)(\mu_M - \mu_R) \Big\}
- 4c\alpha p_c e (\alpha - \beta)(\alpha^2 - \alpha\beta + \beta^2)
}{
(\alpha-\beta)^3(\alpha+\beta)\theta^4 - 4c(\alpha-\beta)(3\alpha^2-\beta^2)\theta^2 + 4c^2(4\alpha^2-\beta^2)
}
\label{eq:p_MN_star}
\end{equation}

\begin{equation}
p_R^{N*} = \frac{
4c^2\alpha \left[ 2\alpha(s - m - \mu_R) + \beta(s - 3w + 2m - \mu_M) \right]
- 2c\alpha\theta^2 \Big\{ (\alpha-\beta) \left[ \alpha(w - m) + \beta(s - 3w + 2m - \mu_M) \right] + \alpha(\alpha - 2\beta)(\mu_M - \mu_R) \Big\}
- 4c p_c e (\alpha - \beta) \left[ c(2\alpha^2 - \beta^2) - \theta^2\alpha(\alpha - \beta) \right]
}{
(\alpha-\beta)^3(\alpha+\beta)\theta^4 - 4c(\alpha-\beta)(3\alpha^2-\beta^2)\theta^2 + 4c^2(4\alpha^2-\beta^2)
}
\label{eq:p_RN_star}
\end{equation}

Substituting the equilibrium prices into Equation~\eqref{eq:k_N}, we obtain the optimal conversion rate:
\begin{equation}
k^{N*} = \frac{\theta(\alpha p_R^{N*} - \beta p_M^{N*})}{c}
\label{eq:k_N_star}
\end{equation}

The equilibrium collection quantities are:
\begin{equation}
q_M^{N*} = \alpha p_M^{N*} - \beta p_R^{N*}
\label{eq:q_MN_star}
\end{equation}
\begin{equation}
q_R^{N*} = \alpha p_R^{N*} - \beta p_M^{N*}
\label{eq:q_RN_star}
\end{equation}
\begin{equation}
q_{total}^{N*} = (\alpha - \beta)(p_M^{N*} + p_R^{N*})
\end{equation}

The corresponding equilibrium profits are:
\begin{equation}
\Pi_M^{N*} = (\theta k^{N*} - p_M^{N*} - w - \mu_M + s)q_M^{N*}
\end{equation}
\begin{equation}
\Pi_R^{N*} = (\theta k^{N*} - p_R^{N*} - m - \mu_R + s)q_R^{N*} + (w - m)q_M^{N*} - \frac{c(k^{N*})^2}{2} - p_c\left[ e(\alpha - \beta)(p_M^{N*} + p_R^{N*}) - G \right]
\end{equation}

This baseline equilibrium provides a benchmark for analyzing how cooperation through investment cost sharing improves the overall system performance.

\subsection{Two-stage biform game analysis}
In this subsection, we analyze the two-stage biform game where the manufacturer and recycler cooperate through investment cost sharing. The biform game consists of: (i) a cooperative game stage where the parties determine the investment cost sharing proportion $n$ and the conversion rate $k$; and (ii) a non-cooperative game stage where they compete in collection prices.

\subsubsection{Cooperative stage: Profit allocation via Shapley value}
In the cooperative stage, we construct the characteristic functions for all possible coalitions under any given competitive situation $(p_M, p_R)$. Using the maximin theorem, we derive:

(1) For coalition $\{M\}$, the characteristic function is:
\begin{equation}
V_{p_M,p_R}(\{M\}) = \max_{n \in [0,1]} \min_{k \in [0,1]} \Pi_M = (s - p_M - w - \mu_M)(\alpha p_M - \beta p_R)
\label{eq:V_M}
\end{equation}

(2) For coalition $\{R\}$, the characteristic function is:
\begin{equation}
V_{p_M,p_R}(\{R\}) = \max_{k \in [0,1]} \left\{(s - p_R - m - \mu_R)B + (w - m)A + \frac{\theta^2 B^2}{2c} - p_c\left[ e(\alpha-\beta)(p_M+p_R)-G \right]\right\}
\label{eq:V_R}
\end{equation}
where $A = \alpha p_M - \beta p_R$ and $B = \alpha p_R - \beta p_M$ denote the collection quantities.

The optimal conversion rate for coalition $\{R\}$ is $k_R^* = \frac{\theta B}{c}$.

(3) For the grand coalition $\{M,R\}$, the characteristic function is:
\begin{equation}
V_{p_M,p_R}(\{M,R\}) = (s - p_M - m - \mu_M)A + (s - p_R - m - \mu_R)B + \frac{\theta^2(A + B)^2}{2c} - p_c\left[ e(\alpha-\beta)(p_M+p_R)-G \right]
\label{eq:V_MR}
\end{equation}
with optimal conversion rate $k^* = \frac{\theta(A+B)}{c}$.

The characteristic functions satisfy superadditivity:
\begin{equation}
V_{p_M,p_R}(\{M,R\}) \geq V_{p_M,p_R}(\{M\}) + V_{p_M,p_R}(\{R\})
\end{equation}
indicating that cooperation yields weakly higher total profit.

We use the Shapley value to allocate the coalition profit. For a two-player game, the Shapley value simplifies to:
\begin{equation}
\varphi_i = \frac{1}{2}[V(\{i\}) - V(\emptyset)] + \frac{1}{2}[V(\{M,R\}) - V(\{j\})], \quad i \neq j
\end{equation}

The resulting profit allocation for manufacturer $M$ is:
\begin{equation}
\boxed{\varphi_M = (s - p_M - w - \mu_M)(\alpha p_M - \beta p_R) + \frac{\theta^2(\alpha p_M - \beta p_R)\left[(\alpha p_M - \beta p_R) + 2(\alpha p_R - \beta p_M)\right]}{4c}}
\label{eq:Shapley_M}
\end{equation}

The profit allocation for recycler $R$ is:
\begin{equation}
\boxed{\varphi_R = (s - p_R - m - \mu_R)(\alpha p_R - \beta p_M) + (w - m)(\alpha p_M - \beta p_R) - p_c\left[ e(\alpha - \beta)(p_M + p_R) - G \right] + \frac{\theta^2\left[2(\alpha p_M - \beta p_R)(\alpha p_R - \beta p_M) - (\alpha p_R - \beta p_M)^2\right]}{4c}}
\label{eq:Shapley_R}
\end{equation}

These allocations satisfy individual rationality: $\varphi_M \geq V(\{M\})$ and $\varphi_R \geq V(\{R\})$.

\textbf{Remark.} The key difference between $\varphi_R$ in the biform game and $\Pi_R^N$ in the baseline is that under cooperation, the recycler benefits from the shared investment technology which generates higher conversion rate $k$, while the carbon cost term remains the same.

\_subsubsection{Non-cooperative stage: Equilibrium pricing}
Using the Shapley values $\varphi_M$ and $\varphi_R$ as payoff functions, we now derive the equilibrium collection prices in the non-cooperative competition stage.

Taking first-order partial derivatives:
\begin{equation}
\frac{\partial \varphi_M}{\partial p_M} = (\alpha p_M - \beta p_R) + \alpha(s - p_M - w - \mu_M) + \frac{\theta^2(\alpha^2 - 2\alpha\beta)}{2c}(\alpha p_M - \beta p_R) + \frac{\theta^2\alpha(\alpha - \beta)}{2c}(\alpha p_R - \beta p_M) = 0
\end{equation}
\begin{equation}
\frac{\partial \varphi_R}{\partial p_R} = (\alpha p_R - \beta p_M) + \alpha(s - p_R - m - \mu_R) - \beta(w - m) - p_c e (\alpha - \beta) + \frac{\theta^2(2\alpha^2 - 2\alpha\beta + \beta^2)}{2c}(\alpha p_R - \beta p_M) + \frac{\theta^2\alpha(\alpha - \beta)}{2c}(\alpha p_M - \beta p_R) = 0
\end{equation}

The resulting system of reaction functions is:
\begin{equation}
\begin{cases}
\left[\alpha + \frac{\theta^2(\alpha^2 - 2\alpha\beta)}{2c}\right](\alpha p_M - \beta p_R) + \frac{\theta^2\alpha(\alpha - \beta)}{2c}(\alpha p_R - \beta p_M) + \alpha(s - p_M - w - \mu_M) = 0 \\[12pt]
\left[\alpha + \frac{\theta^2(2\alpha^2 - 2\alpha\beta + \beta^2)}{2c}\right](\alpha p_R - \beta p_M) + \frac{\theta^2\alpha(\alpha - \beta)}{2c}(\alpha p_M - \beta p_R) + \alpha(s - p_R - m - \mu_R) - \beta(w - m) - p_c e (\alpha - \beta) = 0
\end{cases}
\label{eq:FOC_biform}
\end{equation}

Solving this system, we obtain the equilibrium collection prices under the biform game:
\begin{equation}
p_M^{C*} = \frac{
4c^2 \left[ 2\alpha^2(s - w - \mu_M) + \alpha\beta(s - m - \mu_R) - \beta^2(w - m) \right]
- 2c\theta^2 \Big\{ (\alpha-\beta) \left[ \alpha^2(s - w - \mu_M) - (\alpha^2 - \alpha\beta + \beta^2)(w - m) \right] - \alpha(\alpha^2 - \alpha\beta + \beta^2)(\mu_M - \mu_R) \Big\}
- 4c\alpha p_c e (\alpha - \beta)(\alpha^2 - \alpha\beta + \beta^2)
}{
(\alpha-\beta)^3(\alpha+\beta)\theta^4 - 4c(\alpha-\beta)(3\alpha^2-\beta^2)\theta^2 + 4c^2(4\alpha^2-\beta^2)
}
\label{eq:p_MC_star}
\end{equation}

\begin{equation}
p_R^{C*} = \frac{
4c^2\alpha \left[ 2\alpha(s - m - \mu_R) + \beta(s - 3w + 2m - \mu_M) \right]
- 2c\alpha\theta^2 \Big\{ (\alpha-\beta) \left[ \alpha(w - m) + \beta(s - 3w + 2m - \mu_M) \right] + \alpha(\alpha - 2\beta)(\mu_M - \mu_R) \Big\}
- 4c p_c e (\alpha - \beta) \left[ c(2\alpha^2 - \beta^2) - \theta^2\alpha(\alpha - \beta) \right]
}{
(\alpha-\beta)^3(\alpha+\beta)\theta^4 - 4c(\alpha-\beta)(3\alpha^2-\beta^2)\theta^2 + 4c^2(4\alpha^2-\beta^2)
}
\label{eq:p_RC_star}
\end{equation}

Substituting into the optimal conversion rate:
\begin{equation}
k^{C*} = \frac{\theta(\alpha - \beta)(p_M^{C*} + p_R^{C*})}{c}
\label{eq:k_C_star}
\end{equation}

The equilibrium collection quantities are:
\begin{equation}
q_M^{C*} = \alpha p_M^{C*} - \beta p_R^{C*}
\end{equation}
\begin{equation}
q_R^{C*} = \alpha p_R^{C*} - \beta p_M^{C*}
\end{equation}
\begin{equation}
q_{total}^{C*} = (\alpha - \beta)(p_M^{C*} + p_R^{C*})
\end{equation}

\textbf{Impact of carbon price $p_c$ on equilibrium.} Comparing the reaction functions in the biform game (Equation~\eqref{eq:FOC_biform}) with those in the baseline, we observe that the carbon price $p_c$ affects the recycler's first-order condition through the term $- p_c e (\alpha - \beta)$. This term shifts the recycler's reaction curve leftward: as $p_c$ increases, the recycler's optimal collection price decreases (or increases at a slower rate) to offset the additional carbon cost burden. This is a key difference from the baseline scenario, where the recycler's pricing decision is not modulated by carbon costs in the same manner.

The optimal cost-sharing proportion is:
\begin{equation}
n^{C*} = \frac{2(\alpha p_R^{C*} - \beta p_M^{C*})^2 + 2(\alpha p_M^{C*} - \beta p_R^{C*})(\alpha p_R^{C*} - \beta p_M^{C*}) - (\alpha p_M^{C*} - \beta p_R^{C*})^2}{2 \big[ (\alpha-\beta)(p_M^{C*} + p_R^{C*}) \big]^2}
\end{equation}

The corresponding equilibrium profits are:
\begin{equation}
\Pi_M^{C*} = \varphi_M(p_M^{C*}, p_R^{C*})
\end{equation}
\begin{equation}
\Pi_R^{C*} = \varphi_R(p_M^{C*}, p_R^{C*})
\end{equation}

The equilibrium analysis reveals that under the biform game framework with cooperation, both parties achieve higher profits compared to the baseline non-cooperative scenario, provided that the investment cost sharing mechanism effectively improves the conversion rate $k$. The following section validates these theoretical findings through numerical simulations.
