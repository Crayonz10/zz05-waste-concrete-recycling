# Section 3. Model Formulation (Updated with Cap-and-Trade)

---

\section{Model formulation}

\subsection{Problem description}

We consider a waste concrete recycling supply chain consisting of a traditional concrete manufacturer $M$ and a specialized construction waste recycler $R$. Both $M$ and $R$ participate in the collection of waste concrete from waste generators (e.g., construction companies or demolition contractors). Recycler $R$ possesses specialized waste processing technologies and equipment, responsible for crushing, screening, decontamination, and enhancement of collected waste concrete to produce recycled concrete aggregate (RCA). Under the cap-and-trade mechanism, recycler $R$ is subject to government-allocated carbon emission quotas and must engage in carbon trading based on actual emissions generated during the processing stage.

This section establishes a non-cooperative and cooperative game model to investigate the competition in collection and cooperation in processing technology cost sharing between manufacturer $M$ and recycler $R$ in concrete waste recycling. First, in the non-cooperative game, manufacturer $M$ and recycler $R$ determine their respective collection prices to form a competitive situation $(p_M, p_R)$. Second, in the cooperative game, under any competitive situation, manufacturer $M$ and recycler $R$ determine the strategy of the cooperative game, i.e., the proportion of investment cost sharing $n$ and the corresponding conversion rate $k$, to obtain the characteristic values of each coalition. The Shapley value method is used to calculate the profit distribution values $\varphi_M$ and $\varphi_R$ for manufacturer $M$ and recycler $R$, respectively. Third, using the obtained profit distribution values as the payoff function for the non-cooperative game, the optimal collection prices $(p_M^{C*}, p_R^{C*})$ are derived. Finally, substituting the optimal collection prices into the cooperative game yields the optimal strategies $n^*$ and $k^*$, as well as the corresponding optimal profit allocations $(\Pi_M^{C*}, \Pi_R^{C*})$ and optimal collection quantities $(q_M^{C*}, q_R^{C*})$.

The following assumptions are made:

\textbf{Assumption 1.} Manufacturer $M$ and recycler $R$ set collection prices $(p_M, p_R)$ for waste concrete generators. Since both parties participate in collection, there exists competitive pressure in the recycling market. Let $\beta$ denote the competition intensity between $M$ and $R$. Additionally, the collection quantity depends on the collection price, with $\alpha$ representing the sensitivity of waste generators to collection prices. We assume sufficient waste concrete available in the market and $R$ has sufficient capacity to process all collected quantity. The collection quantity function follows:
\begin{equation}
q_i = \alpha p_i - \beta p_j \quad (i,j \in \{M, R\}, i \neq j)
\end{equation}
where $\alpha > \beta > 0$ ensures positive collection quantities. A larger $\alpha$ indicates higher sensitivity to prices and thus greater collection quantity, and a larger $\beta$ indicates more intense competition between $M$ and $R$.

\textbf{Assumption 2.} The recycling processing capability of recycler $R$ is characterized by the RCA conversion rate $k \in [0,1]$. Improving this conversion rate (e.g., through enhanced mortar removal technology or multi-stage air separation) requires fixed investment in technology and equipment upgrades. The investment cost function is:
\begin{equation}
C(k) = \frac{1}{2} c k^2
\end{equation}
where $c$ is the investment cost coefficient. This quadratic function indicates that investment costs increase with the conversion rate.

\textbf{Assumption 3.} In practice, traditional concrete manufacturers often lack deep-processing environmental equipment or are constrained by site and environmental qualifications. Therefore, manufacturer $M$ outsources the collected waste concrete to recycler $R$ for centralized processing. Manufacturer $M$ pays a unit outsourcing fee $w$ to recycler $R$, while recycler $R$ incurs actual operational costs $m$ (e.g., utilities, equipment depreciation, labor) per unit of waste concrete processed.

\textbf{Assumption 4.} Assume $\theta$ is the unit potential value of waste concrete converted to highest-quality RCA. Under the actual RCA conversion rate $k$ achieved by recycler $R$, the actual extracted value per unit of waste concrete is $\theta k$. For manufacturer $M$, this value represents the cost saving from substituting natural aggregates with RCA; for recycler $R$, it represents the selling price of processed RCA. To encourage construction waste recycling under the zero-waste city initiative, the government provides a subsidy $s$ per unit of waste concrete collected, which is distributed to the respective collector based on their collection quantity.

\textbf{Assumption 5.} To obtain high-quality recycled aggregate and maintain stable outsourcing cooperation, manufacturer $M$ is willing to share the investment cost for improving the RCA conversion rate with recycler $R$. Let manufacturer $M$ share a proportion $(1-n)$ and recycler $R$ bear a proportion $n$, where $n \in [0,1]$. When $n=1$, all investment costs are borne solely by recycler $R$.

\textbf{Assumption 6.} Both manufacturer $M$ and recycler $R$ incur unit transportation costs for collecting waste concrete from generators. Due to the distinctive backhaul logistics advantage in the construction industry, manufacturer $M$'s concrete delivery trucks can collect waste concrete on return trips from construction sites, resulting in a lower transportation cost $\mu_M$. In contrast, recycler $R$ must dispatch dedicated vehicles for collection, incurring a higher transportation cost $\mu_R$. We assume $\mu_M < \mu_R$. This cost asymmetry reflects a key engineering management characteristic of waste concrete recycling: the physical properties of waste concrete (heavy, large volume, low value density) make transportation costs a significant component of total recycling costs.

\textbf{Assumption 7 (Cap-and-Trade Mechanism).} Under the cap-and-trade mechanism, recycler $R$ is subject to government-allocated carbon emission quotas and engages in carbon trading. Let $G$ denote the total carbon emission quota allocated by the government to recycler $R$ in a compliance cycle. The actual carbon emissions generated by recycler $R$ processing a unit of waste concrete is denoted by $e$ (treated as a constant). The total processing quantity is $q_{total} = q_M + q_R = (\alpha - \beta)(p_M + p_R)$, which is derived as follows:
\begin{equation}
q_{total} = (\alpha p_M - \beta p_R) + (\alpha p_R - \beta p_M) = \alpha(p_M + p_R) - \beta(p_M + p_R) = (\alpha - \beta)(p_M + p_R)
\end{equation}
Let $p_c$ denote the trading price per unit of carbon emission in the carbon market. If recycler $R$'s actual carbon emissions $e \cdot q_{total}$ exceed the allocated quota $G$, recycler $R$ must purchase carbon allowances at price $p_c$, resulting in a carbon cost. Conversely, if emissions are below the quota, recycler $R$ can sell surplus allowances for profit. Therefore, the net carbon trading cost incurred by recycler $R$ is:
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

Note that in Equation~\eqref{eq:profit_R}, the last term $p_c[e(\alpha - \beta)(p_M + p_R) - G]$ represents the net carbon trading cost. When actual emissions $e(\alpha - \beta)(p_M + p_R)$ exceed the quota $G$, this term is positive (cost); when emissions are below quota, it becomes negative (profit from selling surplus allowances).

\subsection{Cooperative game: characteristic function construction and profit allocation}

Based on the game sequence of the non-cooperative and cooperative biform game, we construct the cooperative game model under any given competitive situation $(p_M, p_R)$. We calculate the characteristic values $V_{p_M,p_R}(S)$ for all possible coalitions, where $S \in \{\emptyset, \{M\}, \{R\}, \{M, R\}\}$. Here, $\{M, R\}$ denotes the grand coalition composed of manufacturer $M$ and recycler $R$. If the coalition is empty, we assume $V_{p_M,p_R}\{\varnothing\} = 0$. Under any competitive situation, the characteristic functions of the coalitions are determined using the maximin theorem.

For notational convenience, let us define:
\begin{equation}
A = \alpha p_M - \beta p_R \quad \text{and} \quad B = \alpha p_R - \beta p_M
\end{equation}
where $A$ and $B$ represent the collection quantities of manufacturer $M$ and recycler $R$, respectively, and are both non-negative.

(1) For coalition $\{M\}$, based on the profit function $\Pi_M$ in Equation~\eqref{eq:profit_M}, the characteristic function is:
\begin{equation}
V_{p_M,p_R}(\{M\}) = \max_{n \in [0,1]} \min_{k \in [0,1]} \{\Pi_M\} = \max_{n \in [0,1]} \min_{k \in [0,1]} \left\{(\theta k + s - p_M - w - \mu_M)A - (1 - n)\frac{ck^2}{2}\right\}
\end{equation}
Since $n \in [0,1]$, the term $(1 - n)\frac{ck^2}{2}$ is minimized when $n^* = 1$, which yields the maximum value. Substituting $n^* = 1$ into the above equation, we have:
\begin{equation}
V_{p_M,p_R}(\{M\}) = \min_{k \in [0,1]} \left\{(\theta k + s - p_M - w - \mu_M)A\right\}
\end{equation}
Since $A \geq 0$, the minimum is achieved when $k = 0$. Therefore, the characteristic function of coalition $\{M\}$ is:
\begin{equation}
V_{p_M,p_R}(\{M\}) = (s - p_M - w - \mu_M)A
\label{eq:V_M}
\end{equation}

(2) For coalition $\{R\}$, based on the profit function $\Pi_R$ in Equation~\eqref{eq:profit_R}, the characteristic function is:
\begin{equation}
V_{p_M,p_R}(\{R\}) = \max_{k \in [0,1]} \min_{n \in [0,1]} \{\Pi_R\}
\end{equation}
Since $n \in [0,1]$, the investment cost term $n\frac{ck^2}{2}$ is minimized when $n^* = 1$, which yields the maximum profit. Setting $n^* = 1$, we have:
\begin{equation}
V_{p_M,p_R}(\{R\}) = \max_{k \in [0,1]} \left\{(\theta k + s - p_R - m - \mu_R)B + (w - m)A - \frac{ck^2}{2} - p_c\left[ e(\alpha - \beta)(p_M + p_R) - G \right]\right\}
\end{equation}
Note that the carbon trading cost term $p_c[e(\alpha - \beta)(p_M + p_R) - G]$ does not depend on $k$ and can be treated as a constant in the optimization. Taking the first derivative with respect to $k$ and setting it to zero, we obtain:
\begin{equation}
\frac{\partial \Pi_R}{\partial k} = \theta B - ck = 0
\end{equation}
Solving for $k$, we have:
\begin{equation}
k_R^* = \frac{\theta B}{c}
\end{equation}
Substituting $k_R^*$ into the characteristic function, we obtain:
\begin{equation}
V_{p_M,p_R}(\{R\}) = (s - p_R - m - \mu_R)B + (w - m)A + \frac{\theta^2 B^2}{2c} - p_c\left[ e(\alpha - \beta)(p_M + p_R) - G \right]
\label{eq:V_R}
\end{equation}

(3) When manufacturer $M$ cooperates with recycler $R$, they form the grand coalition $\{M,R\}$. Based on the profit functions in Equations~\eqref{eq:profit_M} and~\eqref{eq:profit_R}, the characteristic function of the grand coalition is:
\begin{equation}
V_{p_M,p_R}(\{M,R\}) = \max_{k \in [0,1]} \left\{(\theta k + s - p_M - m - \mu_M)A + (\theta k + s - p_R - m - \mu_R)B - \frac{ck^2}{2} - p_c\left[ e(\alpha - \beta)(p_M + p_R) - G \right]\right\}
\end{equation}
Again, the carbon trading cost term is independent of $k$ and can be treated as a constant. Taking the first derivative with respect to $k$ and setting it to zero, we obtain:
\begin{equation}
\frac{\partial (\Pi_M + \Pi_R)}{\partial k} = \theta A + \theta B - ck = 0
\end{equation}
Solving for $k$, we have:
\begin{equation}
k^* = \frac{\theta(A + B)}{c} = \frac{\theta(\alpha - \beta)(p_M + p_R)}{c}
\label{eq:k_star_grand}
\end{equation}
Substituting $k^*$ into the characteristic function, we obtain:
\begin{equation}
V_{p_M,p_R}(\{M,R\}) = (s - p_M - m - \mu_M)A + (s - p_R - m - \mu_R)B + \frac{\theta^2(A + B)^2}{2c} - p_c\left[ e(\alpha - \beta)(p_M + p_R) - G \right]
\label{eq:V_MR}
\end{equation}

Based on Equations~\eqref{eq:V_M}, \eqref{eq:V_R} and~\eqref{eq:V_MR}, we can derive:
\begin{equation}
\begin{aligned}
V_{p_M,p_R}(\{M,R\}) - V_{p_M,p_R}(\{M\}) - V_{p_M,p_R}(\{R\})
&= \frac{\theta^2(A + B)^2}{2c} - \frac{\theta^2 B^2}{2c} \\
&= \frac{\theta^2(A^2 + 2AB)}{2c} \\
&= \frac{\theta^2 A(A + 2B)}{2c} \geq 0
\end{aligned}
\end{equation}
Since $\theta^2 A(A + 2B) \geq 0$ for all $A \geq 0$ and $B \geq 0$, we have:
\begin{equation}
V_{p_M,p_R}(\{M,R\}) \geq V_{p_M,p_R}(\{M\}) + V_{p_M,p_R}(\{R\})
\label{eq:superadditivity}
\end{equation}

Equation~\eqref{eq:superadditivity} shows that the characteristic functions satisfy superadditivity, indicating that the grand coalition yields weakly greater total profit than the sum of profits from individual coalitions. Therefore, the cooperative game is a convex game, and the Shapley value belongs to the core and satisfies individual rationality.

The Shapley value allocates the coalition profit using the following formula:
\begin{equation}
\varphi_i = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|! (n - |S| - 1)!}{n!} [V(S \cup \{i\}) - V(S)]
\end{equation}
where $n = 2$ is the total number of players. For the two-player game, this simplifies to:
\begin{equation}
\varphi_i = \frac{1}{2}[V(\{i\}) - V(\emptyset)] + \frac{1}{2}[V(\{M,R\}) - V(\{j\})], \quad i \neq j
\end{equation}

We now calculate the Shapley values for manufacturer $M$ and recycler $R$.

\textbf{Manufacturer's Shapley value $\varphi_M$:}
\begin{equation}
\begin{aligned}
\varphi_M &= \frac{1}{2}[V_{p_M,p_R}(\{M\}) - V_{p_M,p_R}(\emptyset)] + \frac{1}{2}[V_{p_M,p_R}(\{M,R\}) - V_{p_M,p_R}(\{R\})] \\
&= \frac{1}{2}(s - p_M - w - \mu_M)A + \frac{1}{2}\left[(s - p_M - m - \mu_M)A + (s - p_R - m - \mu_R)B + \frac{\theta^2(A+B)^2}{2c} \right. \\
&\quad \left. - p_c[e(\alpha-\beta)(p_M+p_R)-G] - (s - p_R - m - \mu_R)B - (w - m)A - \frac{\theta^2 B^2}{2c} + p_c[e(\alpha-\beta)(p_M+p_R)-G]\right] \\
&= \frac{1}{2}(s - p_M - w - \mu_M)A + \frac{1}{2}(s - p_M - m - \mu_M)A - \frac{1}{2}(w - m)A + \frac{1}{2}\left[\frac{\theta^2(A+B)^2}{2c} - \frac{\theta^2 B^2}{2c}\right] \\
&= (s - p_M - w - \mu_M)A + \frac{\theta^2(A^2 + 2AB)}{4c} \\
&= (s - p_M - w - \mu_M)A + \frac{\theta^2 A(A + 2B)}{4c}
\end{aligned}
\end{equation}

Expanding back in terms of $p_M$ and $p_R$:
\begin{equation}
\boxed{\varphi_M = (s - p_M - w - \mu_M)(\alpha p_M - \beta p_R) + \frac{\theta^2(\alpha p_M - \beta p_R)\left[(\alpha p_M - \beta p_R) + 2(\alpha p_R - \beta p_M)\right]}{4c}}
\label{eq:Shapley_M}
\end{equation}

\textbf{Recycler's Shapley value $\varphi_R$:}
\begin{equation}
\begin{aligned}
\varphi_R &= \frac{1}{2}[V_{p_M,p_R}(\{R\}) - V_{p_M,p_R}(\emptyset)] + \frac{1}{2}[V_{p_M,p_R}(\{M,R\}) - V_{p_M,p_R}(\{M\})] \\
&= \frac{1}{2}\left[(s - p_R - m - \mu_R)B + (w - m)A + \frac{\theta^2 B^2}{2c} - p_c[e(\alpha-\beta)(p_M+p_R)-G]\right] \\
&\quad + \frac{1}{2}\left[(s - p_M - m - \mu_M)A + (s - p_R - m - \mu_R)B + \frac{\theta^2(A+B)^2}{2c} - p_c[e(\alpha-\beta)(p_M+p_R)-G] - (s - p_M - w - \mu_M)A\right] \\
&= (s - p_R - m - \mu_R)B + (w - m)A - p_c[e(\alpha-\beta)(p_M+p_R)-G] + \frac{\theta^2(2AB - B^2)}{4c}
\end{aligned}
\end{equation}

Expanding back in terms of $p_M$ and $p_R$:
\begin{equation}
\boxed{\varphi_R = (s - p_R - m - \mu_R)(\alpha p_R - \beta p_M) + (w - m)(\alpha p_M - \beta p_R) - p_c\left[ e(\alpha - \beta)(p_M + p_R) - G \right] + \frac{\theta^2\left[2(\alpha p_M - \beta p_R)(\alpha p_R - \beta p_M) - (\alpha p_R - \beta p_M)^2\right]}{4c}}
\label{eq:Shapley_R}
\end{equation}

\textbf{Verification of individual rationality:} Combining with Equations~\eqref{eq:V_M} and~\eqref{eq:V_R}, we can verify:
\begin{equation}
\varphi_M - V_{p_M,p_R}(\{M\}) = \frac{\theta^2(\alpha p_M - \beta p_R)\left[(\alpha p_M - \beta p_R) + 2(\alpha p_R - \beta p_M)\right]}{4c} \geq 0
\end{equation}
\begin{equation}
\varphi_R - V_{p_M,p_R}(\{R\}) = \frac{\theta^2\left[2(\alpha p_M - \beta p_R)(\alpha p_R - \beta p_M) - (\alpha p_R - \beta p_M)^2\right]}{4c} \geq 0
\end{equation}

The condition $\varphi_R - V_{p_M,p_R}(\{R\}) \geq 0$ requires $2(\alpha p_M - \beta p_R) \geq (\alpha p_R - \beta p_M)$, which holds when $2\alpha p_M \geq (\alpha + \beta)p_R$. For the baseline parameter values used in our numerical analysis, this condition is satisfied, ensuring that cooperation is individually rational for both parties.

Therefore, for any competitive situation $(p_M, p_R)$, the profit allocations for manufacturer $M$ and recycler $R$ satisfy $\varphi_M(p_M, p_R) \geq V_{p_M,p_R}(\{M\})$ and $\varphi_R(p_M, p_R) \geq V_{p_M,p_R}(\{R\})$. This indicates that under any competitive situation, when manufacturer $M$ and recycler $R$ cooperate, the allocated profit is no less than the profit when not cooperating, which helps achieve a stable cooperative alliance.

\subsection{Non-cooperative game: optimal pricing for manufacturer and recycler}

The above analysis solves the profit allocation values $\varphi_M$ and $\varphi_R$ in the cooperative game stage. Using these profit allocation values as the payoff functions for manufacturer $M$ and recycler $R$ in the non-cooperative game, we derive the reaction functions by taking first-order partial derivatives with respect to the collection prices $p_M$ and $p_R$, respectively. By simultaneously solving these reaction functions, we obtain the equilibrium strategies $(p_M^{C*}, p_R^{C*})$. The solution procedure is as follows:

Taking the second-order partial derivatives of the profit allocation functions $\varphi_M$ and $\varphi_R$ with respect to $p_M$ and $p_R$, we obtain:
\begin{equation}
\frac{\partial^2 \varphi_M}{\partial p_M^2} = \frac{\theta^2(\alpha^2 - 2\alpha\beta)}{2c}
\end{equation}
\begin{equation}
\frac{\partial^2 \varphi_R}{\partial p_R^2} = \frac{\theta^2(2\alpha^2 - 2\alpha\beta + \beta^2)}{2c}
\end{equation}
When $\alpha > 2\beta > 0$, we have $\frac{\partial^2 \varphi_M}{\partial p_M^2} < 0$ and $\frac{\partial^2 \varphi_R}{\partial p_R^2} < 0$. This indicates that the profit allocation functions are strictly concave with respect to the collection prices. Therefore, there exist optimal collection prices that maximize the profits of manufacturer $M$ and recycler $R$.

To find the profit maximization, we take the first-order partial derivatives of $\varphi_M$ and $\varphi_R$ with respect to $p_M$ and $p_R$ and set them equal to 0.

\textbf{First-order condition for manufacturer $M$:}
\begin{equation}
\frac{\partial \varphi_M}{\partial p_M} = (\alpha p_M - \beta p_R) + (s - p_M - w - \mu_M)\alpha + \frac{\theta^2(\alpha^2 - 2\alpha\beta)}{2c}(\alpha p_M - \beta p_R) + \frac{\theta^2\alpha(\alpha - \beta)}{2c}(\alpha p_R - \beta p_M) = 0
\end{equation}

\textbf{First-order condition for recycler $R$ (with carbon trading):}
\begin{equation}
\frac{\partial \varphi_R}{\partial p_R} = (\alpha p_R - \beta p_M) + (s - p_R - m - \mu_R)\alpha + (w - m)(-\beta) - p_c e(\alpha - \beta) + \frac{\theta^2(2\alpha^2 - 2\alpha\beta + \beta^2)}{2c}(\alpha p_R - \beta p_M) + \frac{\theta^2\alpha(\alpha - \beta)}{2c}(\alpha p_M - \beta p_R) = 0
\end{equation}

The resulting system of reaction function equations is:
\begin{equation}
\begin{cases}
\frac{\partial \varphi_M}{\partial p_M} = \left[\alpha + \frac{\theta^2(\alpha^2 - 2\alpha\beta)}{2c}\right](\alpha p_M - \beta p_R) + \left[\frac{\theta^2\alpha(\alpha - \beta)}{2c}\right](\alpha p_R - \beta p_M) + \alpha(s - p_M - w - \mu_M) = 0 \\[12pt]
\frac{\partial \varphi_R}{\partial p_R} = \left[\alpha + \frac{\theta^2(2\alpha^2 - 2\alpha\beta + \beta^2)}{2c}\right](\alpha p_R - \beta p_M) + \left[\frac{\theta^2\alpha(\alpha - \beta)}{2c}\right](\alpha p_M - \beta p_R) + \alpha(s - p_R - m - \mu_R) - \beta(w - m) - p_c e(\alpha - \beta) = 0
\end{cases}
\label{eq:FOC_system}
\end{equation}

From this system, we can obtain the optimal collection price $p_M^{C*}$ for manufacturer $M$:
\begin{equation}
p_M^{C*} = \frac{
\stackrel{}{
\begin{aligned}
&4c^2 \left[ 2\alpha^2(s - w - \mu_M) + \alpha\beta(s - m - \mu_R) - \beta^2(w - m) \right] \\
&\quad - 2c\theta^2 \Big\{ (\alpha-\beta) \left[ \alpha^2(s - w - \mu_M) - (\alpha^2 - \alpha\beta + \beta^2)(w - m) \right] \\
&\qquad - \alpha(\alpha^2 - \alpha\beta + \beta^2)(\mu_M - \mu_R) \Big\} \\
&\quad - 4c\alpha p_c e (\alpha - \beta)(\alpha^2 - \alpha\beta + \beta^2)
\end{aligned}}
{(\alpha-\beta)^3(\alpha+\beta)\theta^4 - 4c(\alpha-\beta)(3\alpha^2-\beta^2)\theta^2 + 4c^2(4\alpha^2-\beta^2)
}
\label{eq:p_M_equilibrium}
\end{equation}

And the optimal collection price $p_R^{C*}$ for recycler $R$:
\begin{equation}
p_R^{C*} = \frac{
\stackrel{}{
\begin{aligned}
&4c^2\alpha \left[ 2\alpha(s - m - \mu_R) + \beta(s - 3w + 2m - \mu_M) \right] \\
&\quad - 2c\alpha\theta^2 \Big\{ (\alpha-\beta) \left[ \alpha(w - m) + \beta(s - 3w + 2m - \mu_M) \right] \\
&\qquad + \alpha(\alpha - 2\beta)(\mu_M - \mu_R) \Big\} \\
&\quad - 4c p_c e (\alpha - \beta) \left[ c(2\alpha^2 - \beta^2) - \theta^2\alpha(\alpha - \beta) \right]
\end{aligned}}
{(\alpha-\beta)^3(\alpha+\beta)\theta^4 - 4c(\alpha-\beta)(3\alpha^2-\beta^2)\theta^2 + 4c^2(4\alpha^2-\beta^2)
}
\label{eq:p_R_equilibrium}
\end{equation}

Substituting Equations~\eqref{eq:p_M_equilibrium} and~\eqref{eq:p_R_equilibrium} into Equation~\eqref{eq:k_star_grand}, we can obtain the optimal conversion rate:
\begin{equation}
k^{C*} = \frac{\theta(\alpha - \beta)(p_M^{C*} + p_R^{C*})}{c}
\label{eq:k_equilibrium}
\end{equation}

The optimal proportion $n^{C*}$ can be derived by combining the optimal profits with the profit functions. The optimal profits are:
\begin{equation}
\Pi_M^{C*} = (s - p_M^{C*} - w - \mu_M)(\alpha p_M^{C*} - \beta p_R^{C*}) + \frac{\theta^2(\alpha p_M^{C*} - \beta p_R^{C*})\left[(\alpha p_M^{C*} - \beta p_R^{C*}) + 2(\alpha p_R^{C*} - \beta p_M^{C*})\right]}{4c}
\label{eq:Pi_M_equilibrium}
\end{equation}
\begin{equation}
\Pi_R^{C*} = (s - p_R^{C*} - m - \mu_R)(\alpha p_R^{C*} - \beta p_M^{C*}) + (w - m)(\alpha p_M^{C*} - \beta p_R^{C*}) - p_c\left[ e(\alpha - \beta)(p_M^{C*} + p_R^{C*}) - G \right] + \frac{\theta^2\left[2(\alpha p_M^{C*} - \beta p_R^{C*})(\alpha p_R^{C*} - \beta p_M^{C*}) - (\alpha p_R^{C*} - \beta p_M^{C*})^2\right]}{4c}
\label{eq:Pi_R_equilibrium}
\end{equation}

The optimal collection quantities are:
\begin{equation}
q_M^{C*} = \alpha p_M^{C*} - \beta p_R^{C*}
\label{eq:q_M_equilibrium}
\end{equation}
\begin{equation}
q_R^{C*} = \alpha p_R^{C*} - \beta p_M^{C*}
\label{eq:q_R_equilibrium}
\end{equation}
\begin{equation}
q_{total}^{C*} = q_M^{C*} + q_R^{C*} = (\alpha - \beta)(p_M^{C*} + p_R^{C*})
\label{eq:q_total_equilibrium}
\end{equation}

The above expressions are relatively complex, making it difficult to conduct theoretical analysis on the impacts of parameters such as competition intensity, carbon price, and R\&D cost coefficients on the equilibrium solutions. Therefore, the following numerical simulation analysis will be conducted with specific parameter values to investigate the effects of the cap-and-trade mechanism on the equilibrium outcomes.
