## B. Sampling and positive-layer occupation

Fix \(L\ge3\), \(q>0\), and \(d>0\).
For each population size \(a\ge1\), let
\[
G_a=q(R_a+d^{-1}I_a)
\]
on \(\mathbb T_L^a\), with the operators of Section 1.1.
Each label jumps independently to each neighbor at rate \(q\), and onto each adjacent label at rate \(q/d\).
The same parameters \(L,q,d\) are used at every population size.
For \(L=3\), the two neighbors are distinct and each directed label-pair jump occurs once.
All these chains have finite state spaces.

### B.1. Uniform sampling

For \(1\le m\le a\) and symmetric \(f:\mathbb T_L^m\to\mathbb R\), define
\[
D_{a,m}f(z)=\binom am^{-1}
\sum_{\substack{S\subseteq\{1,\ldots,a\}\\|S|=m}}f(z_S).
\tag{B.1.1}
\]
The order used to list \(z_S\) does not affect this definition.
Write \(P_t^{[a]}\) for the semigroup with generator \(G_a\).
Let \(\Omega_a=\{\eta\in\mathbb N_0^{\mathbb T_L}:\sum_x\eta_x=a\}\).

**Lemma B.1 (sampling identity).** For every symmetric \(f\),
\[
G_aD_{a,m}f=D_{a,m}G_mf,
\qquad
P_t^{[a]}D_{a,m}f=D_{a,m}P_t^{[m]}f.
\tag{B.1.2}
\]
In occupation coordinates, the same operator is
\[
D_{a,m}f(\eta)=\binom am^{-1}
\sum_{k\in\Omega_m}
\prod_x\binom{\eta_x}{k_x}f(k),
\qquad \eta\in\Omega_a.
\tag{B.1.3}
\]
Here symmetric tuple functions are identified with occupation functions.
The operator is an averaging contraction.

*Proof.* Independent jumps act on each selected coordinate at rate \(q\), and give \(D_{a,m}(qR_mf)\).
For the interaction part, fix adjacent labels \(i,j\).
Their two jumps onto each other have the same rate \(q/d\).
Samples containing neither label contribute zero.
Samples containing both give exactly the interaction part of \(D_{a,m}G_mf\).
If \(S\) contains \(i\) but not \(j\), pair it with
\[
S'=(S\setminus\{i\})\cup\{j\}.
\]
The jump of \(i\) onto \(j\) changes \(f(z_S)\) by \(f(z_{S'})-f(z_S)\).
The reverse jump changes \(f(z_{S'})\) by the negative of this value.
These equal-rate terms cancel.
Summing over adjacent unordered label pairs proves the generator identity.

The generators preserve symmetry because their rates are invariant under label permutations.
Iteration of the identity and the finite matrix exponential give the semigroup identity.
There are \(\prod_x\binom{\eta_x}{k_x}\) subsets with sampled occupation \(k\).
This proves (B.1.3), and the weights sum to \(\binom am\).
Thus \(D_{a,m}\) is an averaging contraction.
Finally, summing labelled rates at each source site gives the occupation generator
\[
\widehat G_aF(\eta)=\frac qd\sum_{x:\eta_x>0}\sum_{y=x\pm1}
\eta_x(d+\eta_y)
[F(\eta-\delta_x+\delta_y)-F(\eta)].
\tag{B.1.4}
\]
Hence the same identities hold for the occupation semigroups.
The argument concerns the average over all samples; it requires no autonomous dynamics for a fixed set of labels.

### B.2. Conditional occupation estimate

For \(x,y\in\mathbb T_L\), let
\(\operatorname{dist}_L(x,y)=\min\{r,L-r\}\), where \(r\in\{0,\ldots,L-1\}\) represents \(y-x\).
For \(n\ge2\) and an integer \(1\le k<L/2\), put
\[
B_k(z)=\sum_{1\le i<j\le n}
\mathbf1_{\{0<\operatorname{dist}_L(z_i,z_j)\le k\}}.
\]
Pairs at equal sites are excluded.

**Proposition B.2 (conditional occupation estimate).** Let \(Z\) have generator \(G_n\), with any deterministic initial state or initial distribution.
Use its completed right-continuous natural filtration \((\mathcal F_t)\).
For every deterministic \(\delta\ge0\) and bounded nonnegative stopping times \(\tau,\sigma\) such that \(\tau\le\sigma\le\tau+\delta\) almost surely,
\[
\mathbb E\left[\int_\tau^\sigma B_k(Z_s)\,ds
\;\middle|\;\mathcal F_\tau\right]
\le\binom n2\left[\frac{2k\delta}{L+1/d}+\frac{Lk}{q}\right]
\quad\text{almost surely}.
\tag{B.2.1}
\]
The bound is uniform over all these parameters, initial laws, and stopping times.

### B.3. A finite pair Poisson equation

*Proof of Proposition B.2.* For two labels, the difference \(r=z_2-z_1\in\mathbb T_L\) has generator
\[
\begin{aligned}
\mathcal Hv(r)={}&2q[v(r+1)+v(r-1)-2v(r)]\\
&+\frac{2q}{d}\mathbf1_{\{r=1\}}[v(0)-v(1)]
+\frac{2q}{d}\mathbf1_{\{r=-1\}}[v(0)-v(-1)].
\end{aligned}
\tag{B.3.1}
\]
Indeed, two independent jumps increase the difference, and two decrease it.
At distance one, either label can jump onto the other.
For \(L=3\), the rates from \(r=1\) are \(2q(1+1/d)\) to zero and \(2q\) to \(r=2\); there is no extra collision jump between the two nonzero residues.

Use representatives \(r=0,\ldots,L-1\), with all subscripts modulo \(L\), and set
\[
m_r=1+d^{-1}\mathbf1_{\{r=0\}},
\qquad
a_r=1+d^{-1}\mathbf1_{\{r=0\text{ or }r=L-1\}}.
\]
The coefficient \(a_r\) belongs to the edge from \(r\) to \(r+1\).
Direct comparison with (B.3.1) gives
\[
\mathcal Hv(r)=\frac{2q}{m_r}
\left[a_r(v(r+1)-v(r))-a_{r-1}(v(r)-v(r-1))\right].
\tag{B.3.2}
\]
The two edges incident to zero are distinct for every \(L\ge3\), so this formula includes \(L=3\).

Put
\[
b(r)=\mathbf1_{\{0<\operatorname{dist}_L(r,0)\le k\}},
\qquad \beta=\frac{2k}{L+1/d},
\qquad g_r=m_r(b(r)-\beta).
\]
The layer has exactly \(2k\) nonzero residues.
Thus \(0<\beta<1\), \(\sum_rg_r=0\), and
\(\sum_r(g_r)^+=2k(1-\beta)\le2k\).
Define
\[
S_r=\frac1{2q}\sum_{j=0}^rg_j,
\qquad
\overline S=\frac{\sum_rS_r/a_r}{\sum_r1/a_r},
\qquad J_r=S_r-\overline S.
\]
Every difference of two partial sums is a signed sum over an interval.
The total positive and negative sums both have absolute value at most \(2k\).
It follows that \(\max S-\min S\le k/q\).
The weighted mean \(\overline S\) lies within this range, so
\[
|J_r|\le k/q,
\qquad \sum_rJ_r/a_r=0,
\qquad J_r-J_{r-1}=g_r/(2q).
\tag{B.3.3}
\]
The last identity also holds at zero because \(S_{L-1}=0\).
Prescribe \(v(0)=0\) and
\[
v(r+1)-v(r)=J_r/a_r.
\]
The zero sum makes \(v\) periodic.
Equations (B.3.2)–(B.3.3), and \(a_r\ge1\), give
\[
\mathcal Hv=b-\beta,
\qquad
\operatorname{osc}(v):=\max v-\min v\le Lk/q.
\tag{B.3.4}
\]
The operator \(\mathcal H\) commutes with reflection and \(b\) is even.
Replacing \(v(r)\) by \((v(r)+v(-r))/2\) therefore preserves the equation and the oscillation bound.
Use this even \(v\) below.

### B.4. Conditional Dynkin formula

The function \(f_v(z_1,z_2)=v(z_2-z_1)\) is symmetric.
Equation (B.3.1) gives \(G_2f_v(z)=\mathcal Hv(z_2-z_1)\).
Lemma B.1 gives
\[
V(z):=D_{n,2}f_v(z)=\binom n2^{-1}\sum_{i<j}v(z_j-z_i),
\]
\[
G_nV=\binom n2^{-1}B_k-\beta,
\qquad \operatorname{osc}(V)\le Lk/q.
\tag{B.4.1}
\]
On the finite state space, \(V\) and \(G_nV\) are bounded.
Its Dynkin martingale is bounded on each deterministic finite time interval.
Conditional optional sampling at the stated bounded stopping times yields
\[
\mathbb E\left[\int_\tau^\sigma G_nV(Z_s)\,ds\mid\mathcal F_\tau\right]
=\mathbb E[V(Z_\sigma)-V(Z_\tau)\mid\mathcal F_\tau].
\]
Insert (B.4.1), use \(\sigma-\tau\le\delta\), and obtain
\[
\begin{aligned}
\binom n2^{-1}
\mathbb E\left[\int_\tau^\sigma B_k(Z_s)\,ds\mid\mathcal F_\tau\right]
&=\beta\mathbb E[\sigma-\tau\mid\mathcal F_\tau]
+\mathbb E[V(Z_\sigma)-V(Z_\tau)\mid\mathcal F_\tau]\\
&\le\beta\delta+\operatorname{osc}(V)\\
&\le\frac{2k\delta}{L+1/d}+\frac{Lk}{q}.
\end{aligned}
\]
Multiplication by \(\binom n2\) proves (B.2.1).
