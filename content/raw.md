This proof was written by an AI model. No human or outside-family model audit is recorded.
{: .ai-note }

**Abstract.** We study the symmetric inclusion process on a discrete circle in the regime \(N/L_N\to\rho\in(0,\infty)\) and \(Nd_N\to\Theta\in(0,\infty)\). With time acceleration \(N^2/d_N\), we prove convergence of the full empirical mass process to the Le Jan–Raimond sticky Brownian mass flow. The initial configurations have a fixed finite bound on the number of isolated occupied sites. Normalized masses may vanish, and limiting stack positions may coincide. The convergence holds in the Skorokhod \(J_1\) topology, with a continuous limit. The proof first establishes path convergence for every fixed order of the auxiliary inclusion process. Harmonic corrections identify the splitting rates, and a conditional occupation estimate controls the collision layers. An exact factorial sampling identity then gives uniform convergence of the mass resolvents. A resolvent argument gives tightness and identifies the full mass path law.
{: .abstract }

## 1. Statement

For each positive integer \(N\), let \(L_N\) be a positive integer and let \(d_N>0\).
Assume
\[
\frac{N}{L_N}\longrightarrow\rho\in(0,\infty),
\qquad
Nd_N\longrightarrow\Theta\in(0,\infty).
\]
Set \(\alpha=\Theta/\rho\), so that \(L_Nd_N\to\alpha\).
Let \(\mathbb T=\mathbb R/\mathbb Z\), and let \(\lambda\) be its normalized Haar measure.
Define
\[
\mathbb T_{L_N}=\mathbb Z/(L_N\mathbb Z),
\qquad
\Omega_N=
\left\{\eta\in\mathbb N_0^{\mathbb T_{L_N}}:
\sum_{x\in\mathbb T_{L_N}}\eta_x=N\right\}.
\]
Let \(\eta_N\) be the continuous-time Markov chain on \(\Omega_N\) with generator
\[
\mathcal L_NF(\eta)=\frac{N^2}{d_N}
\sum_{x\in\mathbb T_{L_N}}\sum_{y=x\pm1}
\eta_x(d_N+\eta_y)
\bigl[F(\eta-\delta_x+\delta_y)-F(\eta)\bigr].
\]
The sum includes both directed nearest-neighbor jumps.
The generator includes the acceleration \(N^2/d_N\).
Since \(L_N\to\infty\), only tori with \(L_N\ge3\) affect the limit.
The limiting one-particle generator is \(\rho^2\partial_{xx}\).
Define the empirical mass map and its process by
\[
\Phi_N(\eta)=\frac1N\sum_{x\in\mathbb T_{L_N}}
\eta_x\delta_{x/L_N},
\qquad
\mu_N(t)=\Phi_N(\eta_N(t)).
\]

For \(n\ge1\), let \(\Pi_n\) be the set of partitions of \(\{1,\ldots,n\}\).
For \(\pi\in\Pi_n\), let
\(\iota_\pi:\mathbb T^{|\pi|}\to\mathbb T^n\)
assign one common coordinate to all indices in each block.
The formulas below do not depend on the order of the blocks.
Set
\[
p_\alpha(\pi)=
\frac{\alpha^{|\pi|}\Gamma(\alpha)}{\Gamma(\alpha+n)}
\prod_{B\in\pi}(|B|-1)!,
\qquad
m_{\alpha,n}=
\sum_{\pi\in\Pi_n}p_\alpha(\pi)
(\iota_\pi)_*\lambda^{\otimes|\pi|}.
\]
On smooth periodic functions, define
\[
\mathcal E_n(f,g)=
\rho^2\sum_{\pi\in\Pi_n}p_\alpha(\pi)
\int_{\mathbb T^{|\pi|}}
\nabla(f\circ\iota_\pi)\cdot\nabla(g\circ\iota_\pi)
\,d\lambda^{\otimes|\pi|}.
\]
Close this form in its form norm on \(L^2(m_{\alpha,n})\).
Let \(P_t^{(n)}\) be the associated continuous-path Feller semigroup from the Le Jan–Raimond Brownian sticky-flow construction.
These forms fix the target and its time scale.
See Le Jan and Raimond, [Sticky flows on the circle](https://arxiv.org/abs/math/0211387), and Le Jan and Lemaire, [Products of Beta matrices and sticky flows](https://arxiv.org/abs/math/0307106).

The Feller mass-process semigroup \(\mathsf P_t\) on \(\mathcal P(\mathbb T)\) is specified by
\[
F_f(\mu)=\int_{\mathbb T^n}f\,d\mu^{\otimes n},
\qquad
\mathsf P_tF_f(\mu)=
\int_{\mathbb T^n}P_t^{(n)}f\,d\mu^{\otimes n},
\qquad f\in C(\mathbb T^n),\quad n\ge1.
\]
Let \(Q_{\mu_0}\) be its continuous-path law with initial state \(\mu_0\).
Equivalently, the corresponding random transition kernel \(K_{0,t}\) gives
\[
\mu_t(A)=\int_{\mathbb T}K_{0,t}(x,A)\,\mu_0(dx)
\]
for Borel sets \(A\subseteq\mathbb T\).
All initial atoms use the same random kernel flow.

**Theorem 1 (full mass path convergence).**
For every parameter sequence specified above and every fixed integer \(k\ge1\), take a deterministic sequence \(\eta_N^0\in\Omega_N\).
Assume that each \(\eta_N^0\) has at most \(k\) occupied sites.
Assume that two distinct occupied sites have circular lattice distance at least two, and that
\[
\Phi_N(\eta_N^0)\longrightarrow\mu_0
\quad\text{weakly in }\mathcal P(\mathbb T).
\]
Then
\[
\operatorname{Law}_{\eta_N^0}\bigl(\mu_N(\cdot)\bigr)
\Longrightarrow Q_{\mu_0}
\quad\text{in }D([0,\infty),\mathcal P(\mathbb T)).
\]
Here \(\mathcal P(\mathbb T)\) has its weak topology, and the path space has the Skorokhod \(J_1\) topology.
Moreover,
\[
Q_{\mu_0}\bigl(C([0,\infty),\mathcal P(\mathbb T))\bigr)=1.
\]

The limit \(\mu_0\) has at most \(k\) atoms.
There is no uniform positive lower bound on the initial masses divided by \(N\).
There is no positive lower bound on their macroscopic separations.
Thus initial stacks may have vanishing normalized mass, and distinct occupied sites may converge to the same point.
The initial laws need not be stationary or absolutely continuous with respect to a reference measure.
The conclusion applies to the full empirical mass process on all finite time horizons.

### 1.1. Notation and proof structure

Sections 2–4 prove convergence of the auxiliary labelled processes and identify their limits.
Section 5 proves Theorem 1 by factorial sampling and uniform resolvent convergence.
Appendices A–C prove the harmonic correction estimates, the conditional occupation bound, and the path-transfer theorem used in the argument.
Equation labels I–IV refer to Sections 2–5.

For \(L\ge3\) and \(z\in\mathbb T_L^n\), set
\[
\eta_x(z)=\#\{i:z_i=x\},\qquad
z^{i,\epsilon}=z+\epsilon e_i,\quad \epsilon\in\{-1,1\}.
\]
Addition is modulo \(L\). Define
\[
R_nF(z)=\sum_{i=1}^n\sum_{\epsilon=\pm1}
[F(z^{i,\epsilon})-F(z)],
\]
\[
I_nF(z)=\sum_{i=1}^n\sum_{\epsilon=\pm1}
\eta_{z_i+\epsilon}(z)[F(z^{i,\epsilon})-F(z)].
\]
The same formulas on \(\mathbb Z^n\) define the line operators in Appendix A.
A chamber-affine test is a continuous function on \(\mathbb R^n\) that is affine on each coordinate-order chamber.
A common-cut chart lifts all circle coordinates into the same interval of length one.
Thus it preserves coordinate equalities.

Fix the parameter sequence in Theorem 1. Write
\[
L=L_N,\qquad d=d_N,\qquad q=N^2,\qquad
\frac{q}{L^2}\longrightarrow\rho^2,\qquad
\frac{qd}{L}\longrightarrow\alpha\rho^2,\qquad
d\longrightarrow0.
\]
Every labelled order \(n\) below is fixed but arbitrary; \(q\) is always \(N^2\), never \(n^2\). The labelled chain is an auxiliary chain with the explicitly displayed generator. No selected subset of physical labels is asserted to be autonomous. All common-cut lifts preserve exact collisions.

## 2. Circle traces and tightness


### 2.1. Trace process and tightness

Fix an integer \(n\ge2\). On \(\mathbb T_L^n\), use the labelled operators \(R_n,I_n\) of Appendix B. Let \(S\) be the tuples with no adjacent distinct occupied sites. For \(q>0\) and \(0<d\le d_n\), let \(Z\) have generator \(q(R_n+d^{-1}I_n)\). Write
\[
c_n=\frac{n(n-1)}4,\qquad r=2nc_nd\le\frac14.
\]
All circle distances below are geodesic distances, and the product metric is the maximum of the coordinate distances. Absorption means first entrance into \(S\), including time zero. An excursion includes its returning jump.

**Proposition 2.1 (tightness).** Under
\[
q=N^2,\qquad \frac{N}{L_N}\longrightarrow\rho,
\qquad L_Nd_N\longrightarrow\alpha\in(0,\infty),
\]
the laws of \(X_N(t)=Z_t/L_N\) are C-tight in \(D([0,T],\mathbb T^n)\), for every fixed \(T\), uniformly over initial states and initial distributions.

*Proof.* We first estimate absorption times, the time removed by the trace, and the displacement during each removed excursion. We then compare the line and circle trace generators at the accelerated time scale. The stopping-time estimates in Section 2.5 complete the proof.

Constants denoted by \(C_n\) or \(C_{n,p}\) may change between occurrences. They are uniform in positions and initial laws. Constants in the tightness argument may also depend on the limiting parameters, the fixed chart margin, and the indicated displacement threshold.

### 2.2. Arbitrary-start circle absorption and excursion marks

Let \(V(z)=\sum_x\eta_x(z)^2\). Summing the two directions of each undirected neighboring edge gives the exact identity
\[
I_nV(z)=4\sum_{\{x,y\}:\,x\sim y}\eta_x(z)\eta_y(z).
\]
Indeed, the jump from occupancies \((a,b)\) to \((a-1,b+1)\) changes \(V\) by \(2(b-a+1)\), and has inclusion rate \(ab\). The reverse direction contributes \(2(a-b+1)ab\). This convention also holds for \(L=3\), where the three undirected edges are distinct. Consequently \(I_nV\ge4\) off \(S\), while \(n\le V\le n^2\). Stopped Dynkin's formula and monotone convergence show that the pure-inclusion absorption time \(\tau_0\) satisfies
\[
\sup_{L\ge3}\sup_z\mathbb E_z\tau_0
\le\frac{n^2-n}{4}=c_n.
\]
In particular absorption is almost sure, for every initial state and every \(L\ge3\).

Run \(I_n+dR_n\) by superposing an independent clock of rate \(2nd\) on successive pure-inclusion pieces. From any state, the probability that this clock rings before pure-inclusion absorption is at most
\[
\mathbb E[1-\exp(-2nd\tau_0)]\le 2nd\mathbb E\tau_0\le r.
\]
Restart this argument after every independent event. Let \(J\) count all independent events before absorption, including one that causes absorption. Then, for arbitrary starting states,
\[
\mathbb P(J\ge j)\le r^j\quad(j\ge0),\qquad
\mathbb E\tau_d\le\sum_{j\ge0}c_nr^j\le2c_n.
\]
The same statements apply after an initiating independent jump from \(S\); that initiating jump is excluded from \(J\). They include duration-zero excursions.

The uniform mean estimate and the strong Markov property give
\[
\mathbb P_z(\tau_d>4c_n k)\le2^{-k}\quad(k\ge0).
\]
Thus \(\sup_{L,z}\mathbb E_z\tau_d^p\le C_{n,p}\) for every real \(p\ge1\). Geometric summation also gives, for integers \(m\ge0\),
\[
\mathbb E[(1+J)^p\mathbf 1_{\{J\ge m\}}]
\le C_{n,p}(m+1)^p r^m.
\tag{I.2.1}
\]
For example, bound the expectation by \(\sum_{j\ge m}(j+1)^pr^j\), write \(j=m+k\), and use \((m+k+1)^p\le(m+1)^p(k+1)^p\) and \(r\le1/4\).

There is also a deterministic displacement bound. Inclusion jumps never add a site to the occupied support. Each independent event adds at most one site to the set of sites ever occupied. Starting at an arbitrary tuple, this set has size at most \(n+J\); starting at a tuple in \(S\) and including one initiating jump, it has size at most \(n+1+J\). Each label's nearest-neighbor path lies in one connected component of this set. A proper connected subset of the circle is an arc whose length is its cardinality minus one. If the visited set is the entire circle, use the diameter bound \(L/2\) instead. In both cases, measured from the tuple before the initiating jump, or from an arbitrary initial tuple without one,
\[
\max_i\sup_{s\le\tau_d}
\operatorname{dist}_L(Z_i(s),Z_i(0))\le n+J.
\tag{I.2.2}
\]
In the initiating-jump formulation, \(Z(0)\) in (I.2.2) denotes the pre-jump tuple. The same visited-support argument on \(\mathbb Z\) bounds ordinary absolute displacement by \(n+J\). On the circle, (I.2.2) bounds geodesic displacement; it does not assert a bound on a winding lift.

### 2.3. Lost clock time and maximum deleted displacement

Return to the physical generator \(q(R_n+d^{-1}I_n)\). An excursion has physical duration \((d/q)\tau_d\), so its conditional expected duration, including from an arbitrary initial state, is at most \(2c_nd/q\). Put
\[
A(t)=\int_0^t\mathbf 1_{\{Z_s\in S\}}\,ds.
\]
Independent initiating events while in \(S\) have rate \(2nq\). Summing conditional expected excursion durations over their initiation times, and adding the initial absorption piece, gives
\[
\mathbb E[T-A(T)]\le\frac{2c_nd}{q}+4nc_ndT.
\tag{I.3.1}
\]
This uses completed durations even for an excursion that ends after \(T\); hence it is an upper bound without a terminal-excursion omission. The same compensator and strong Markov argument, starting at an arbitrary bounded stopping time \(\tau\), proves
\[
\mathbb E\left[\int_\tau^{\tau+\delta}
\mathbf 1_{\{Z_s\notin S\}}\,ds\,\middle|\,\mathcal F_\tau\right]
\le\frac{2c_nd}{q}+4nc_nd\delta.
\tag{I.3.2}
\]
As a separate direct use of the occupation estimate in Appendix B, \(\mathbf 1_{S^c}\le B_1\) yields, whenever \(\tau\le\sigma\le\tau+\delta\),
\[
\mathbb E\left[\int_\tau^\sigma
\mathbf 1_{\{Z_s\notin S\}}\,ds\,\middle|\,\mathcal F_\tau\right]
\le\binom n2\left[\frac{2\delta}{L+1/d}+\frac Lq\right].
\tag{I.3.3}
\]
The choice \(k=1\) is permitted for every \(L\ge3\). Both (I.3.1) and (I.3.3) imply \(\sup_{t\le T}|A(t)-t|\to0\) in probability under the stated scaling.

Let \(D_T\) be the greatest rescaled diameter, in the product metric, of the initial absorption path or of any entire excursion initiated by physical time \(T\). Equations (I.2.1)–(I.2.2), the initiating-event compensator, and the strong Markov property imply, for \(\varepsilon L/2>n\),
\[
\mathbb P(D_T>\varepsilon)
\le(1+2nqT)r^{\max\{0,\lfloor\varepsilon L/2-n\rfloor\}}.
\tag{I.3.4}
\]
The harmless floor weakens the integer threshold. Consequently \(D_T\to0\) in probability: the prefactor is of order \(L^2\), whereas \(r\le1/4\) and the exponent is proportional to \(L\).

Let \(\gamma(u)=\inf\{t:A(t)>u\}\) and \(Y_u=Z_{\gamma(u)}\). The initial state of this trace is the first absorbed state if \(Z_0\notin S\). Its generator is \(q\mathcal T_d^L\), where
\[
\mathcal T_d^L b(z)=
\sum_{i=1}^n\sum_{\epsilon\in\{-1,1\}}
\mathbb E_{z+\epsilon e_i}
[b(Z_{\tau_d})-b(z)],\qquad z\in S.
\tag{I.3.5}
\]
The absorption in (I.3.5) is for \(I_n+dR_n\). Formula (I.3.5) follows by deleting the waiting times outside \(S\) from independent attempts of rate one in each direction; returning to the same state contributes zero. It is conservative and its off-diagonal total rate is at most \(2n\). All its absorption expectations exist because the circle state space is finite. Finite-state irreducibility for \(d>0\) ensures that the inverse clock is defined for every finite \(u\).

At a time inside a deleted excursion, \(Y_{A(t)}\) is its returning state. Therefore, with division by \(L\) understood coordinatewise,
\[
\sup_{t\le T}\operatorname{dist}(Z_t/L,Y_{A(t)}/L)\le D_T.
\tag{I.3.6}
\]
This includes the initial absorption interval and an excursion returning after \(T\).

### 2.4. Local line-to-circle agreement with the rates included

Fix a cut \(a\in\mathbb T\). Lift each circle coordinate to its unique integer representative in \([aL,aL+L)\); call the resulting tuple \(\ell_a(z)\). For a continuum chamber-affine function \(f\) with Lipschitz constant \(D\), define its lattice-scale version \(f^{[L]}(u)=L f(u/L)\). This has the same Lipschitz bound. On the whole circle stable set put
\[
\widehat H_f^a(z)=H_{f^{[L]}}(\ell_a(z)),\qquad
h_f^a(z)=L^{-1}\widehat H_f^a(z).
\]
Consequently \(h_f^a(z)-f(\ell_a(z)/L)\) is uniformly bounded by \(a_nD/L\), including when \(f\) has a nonzero constant term. In the comparisons in this subsection, the line symbols \(H_f\) and \(BH_f\) abbreviate \(H_{f^{[L]}}\) and \(BH_{f^{[L]}}\); Appendix A is applied to this function. Coordinates are unchanged by this convention.
Here \(\ell_a(z)\in S_n\): circle stability excludes every possible line adjacency. These functions may jump across the cut, which is why the following estimate is localized.

Suppose every lifted coordinate of \(z\) has distance at least \(h\) from both ends of the lift interval, with \(n+4\le h\le L/2\), and put
\[
x=\ell_a(z),\qquad m=\lfloor h-n-2\rfloor\ge1.
\]
Couple the circle and line initiating-step excursions using the same independent and inclusion events until a coordinate comes within one site of the cut. Before that event, their rates, stable sets, and integer positions agree. By the visited-support bound, reaching this region requires at least \(m\) independent excursion events. On the failure event, both complete excursion counts are at least \(m\); after failure use any continuation with the correct marginal laws. The line count has the bound of assertion (A-H6), and the circle count has (I.2.1).

Circle corrected increments have absolute value at most \(C_nD(L+1)\), because the lift interval has length \(L\) and \(\|\psi_f\|_\infty\le a_nD\). Line corrected increments have absolute value at most \(C_nD(1+J)\). Multiplying these bounds by the failure indicators and using (I.2.1), then summing the \(2n\) initiating attempts, proves
\[
|\mathcal T_d^L\widehat H_f^a(z)-T_dH_f(x)|
\le C_nDLr^m.
\tag{I.4.1}
\]
For coordinates \(f_i(x)=x_i\), define the circle unscaled corrected covariance \(\widehat\Gamma_{d,L,a}^{ij}\) by the jump-rate sum for \(\mathcal T_d^L\) with increments of \(\widehat H_i^a,\widehat H_j^a\). Products of circle increments are bounded by \(C_nL^2\); products of line increments are bounded by \(C_n(1+J)^2\). The same argument proves
\[
|\widehat\Gamma_{d,L,a}^{ij}(z)-\Gamma_d^{ij}(x)|
\le C_nL^2r^m.
\tag{I.4.2}
\]
Thus these are rate-weighted estimates, not merely a statement that the two return distributions agree with high probability. In particular assertion (A-H5), assertion (A-H4), and (I.4.1)–(I.4.2) give
\[
\left|q\mathcal T_d^Lh_f^a(z)-\frac{qd}{L}BH_f(x)\right|
\le C_nD\left(\frac{qd^2}{L}+qr^m\right),
\tag{I.4.3}
\]
\[
\left|\frac q{L^2}\widehat\Gamma_{d,L,a}^{ij}(z)
-\frac q{L^2}\Gamma_d^{ij}(x)\right|\le C_nqr^m.
\tag{I.4.4}
\]
One may replace \(\Gamma_d\) by \(\Gamma_0\) in (I.4.4) at the additional cost \(C_nqd/L^2\). For every \(p\ge1\), assertion (A-H6) and the same coupling also give the local scaled jump-moment estimate
\[
q\sum_y\mathcal T_d^L(z,y)
|h_f^a(y)-h_f^a(z)|^p
\le C_{n,p}D^p\left(\frac q{L^p}+qr^m\right).
\tag{I.4.5}
\]
Diagonal terms in these sums are zero. No bound depending on the additive constant of \(f\) has been used.

For a fixed positive macroscopic margin \(b\), take \(h=bL\). Then \(m\) grows linearly in \(L\), and
\[
qr^m\longrightarrow0,\qquad
\frac{qd^2}{L}\longrightarrow0,\qquad
\frac{qd}{L}=O(1),\qquad\frac q{L^2}=O(1).
\]
This verifies explicitly that the circle-to-line errors vanish after the acceleration. In particular the local drift of each \(h_i^a\) and its local bracket density are uniformly bounded.

### 2.5. Nested charts and stopping-time C-tightness

Take \(b=1/(16n)\) and the \(4n\) cuts \(a_j=j/(4n)\). Define
\[
U_j=\{x:\min_i\operatorname{dist}_{\mathbb T}(x_i,a_j)>2b\},
\qquad
V_j=\{x:\min_i\operatorname{dist}_{\mathbb T}(x_i,a_j)>b\}.
\]
The \(U_j\) cover \(\mathbb T^n\): for each coordinate, the closed forbidden interval of radius \(2b\) has length \(1/(4n)\), hence contains at most two of the cuts. At most \(2n<4n\) cuts are forbidden. Also \(\overline U_j\subset V_j\).

Start the rescaled trace \(\overline Y=Y/L\) at any state in \(U_j\), and stop at its first exit \(\zeta\) from \(V_j\). For all sufficiently large \(N\), (I.4.3)–(I.4.4) apply at every pre-exit state with margin \(bL\). For each coordinate there is a martingale decomposition
\[
h_i^{a_j}(Y_{t\wedge\zeta})-h_i^{a_j}(Y_0)
=M_i(t)+\int_0^{t\wedge\zeta}\beta_i(Y_s)\,ds,
\]
with \(|\beta_i|\le C\) and predictable bracket \(\langle M_i\rangle_t\le Ct\). Here \(\zeta\) uses the physical trace time, and \(h_i^{a_j}\) is defined at the exit state as well. The finite-state martingale formula therefore includes an overshooting exit jump. Doob's inequality gives
\[
\mathbb E\sup_{s\le\delta}
|h_i^{a_j}(Y_{s\wedge\zeta})-h_i^{a_j}(Y_0)|^2
\le C(\delta+\delta^2).
\tag{I.5.1}
\]
The same estimate holds conditionally after a trace stopping time, selecting the first eligible cut measurably from its current state.

For every circle state, the coordinate correction is at most \(a_n/L\). The circle distance between two coordinates is consequently at most their corrected-lift difference plus \(2a_n/L\). An exit from \(V_j\), starting in \(U_j\), requires displacement at least \(b\) in one coordinate. Thus (I.5.1), summed over coordinates, implies, for each fixed \(\varepsilon>0\) and all sufficiently large \(N\),
\[
\sup_y\mathbb P_y\left(
\sup_{u\le\delta}\operatorname{dist}(\overline Y_u,\overline Y_0)
>\varepsilon\right)
\le C_{n,\varepsilon}(\delta+\delta^2).
\tag{I.5.2}
\]
To see the exit step explicitly, bound the exit probability using threshold \(b-2a_n/L\), and the stopped displacement probability using threshold \(\varepsilon-2a_n/L\). Both thresholds are positive for large \(N\). This justifies (I.5.2) without requiring a single chart to cover an entire path.

The trace also has vanishing maximum jumps. The excursion mark bound gives a uniform \(p\)-th moment for unscaled geodesic trace displacement, so, for every \(p>2\),
\[
\mathbb P\left(\sup_{u\le T}
\operatorname{dist}(\overline Y_u,\overline Y_{u-})>\varepsilon\right)
\le\frac{C_{n,p}qT}{\varepsilon^pL^p}\longrightarrow0.
\tag{I.5.3}
\]
The event-rate bound \(2nq\) justifies this compensator estimate; it does not presuppose a deterministic number of excursions.

For completeness, the required stopping-time estimate can be obtained directly in the original filtration. Let \(\tau\) be any bounded stopping time of the untraced chain, and let \(\theta\) be its first subsequent entrance into \(S\). Apply (I.2.1)–(I.2.2) to the entire absorption path from \(Z_\tau\). After \(\theta\), run a fresh trace, using the strong Markov property at \(\theta\). Its retained time within \([\theta,\tau+\delta]\) is at most \(\delta\), so (I.5.2) controls its displacement. Every original state in this interval differs from the corresponding trace state by the diameter of its deleted excursion. The conditional expected number of initiating events in \([\tau,\tau+\delta]\) is at most \(2nq\delta\). A union bound, also including the initial absorption piece, therefore gives
\[
\mathbb P\left(
\sup_{0\le s\le\delta}
\operatorname{dist}(X_N(\tau+s),X_N(\tau))>\varepsilon
\,\middle|\,\mathcal F_\tau\right)
\le C_{n,\varepsilon}(\delta+\delta^2)
+C_n(1+q\delta)r^{m_{\varepsilon,L}},
\tag{I.5.4}
\]
where one valid weakened threshold is
\[
m_{\varepsilon,L}=\max\{0,\lfloor\varepsilon L/8-n-2\rfloor\}.
\]
Indeed, keep each of the initial-piece diameter, the trace displacement, and the largest later excursion diameter below \(\varepsilon/4\). Their sum is at most \(3\varepsilon/4\); (I.2.2) and this choice of \(m_{\varepsilon,L}\) bound the two diameter failures. This argument remains valid if \(\theta>\tau+\delta\): then only the initial absorption path is needed. Excursions that return after the interval are counted in full. There is no assertion that \(A(\tau)\) is a stopping time in a trace filtration.

For each \(\varepsilon>0\), (I.5.4) implies the uniform stopping-time condition
\[
\lim_{\delta\downarrow0}\limsup_{N\to\infty}
\sup_{\tau\le T}
\mathbb P\left(
\sup_{s\le\delta}\operatorname{dist}(X_N(\tau+s),X_N(\tau))
>\varepsilon\right)=0.
\tag{I.5.5}
\]
Compact containment is automatic on \(\mathbb T^n\). The classical Aldous stopping-time tightness criterion therefore yields tightness in the Skorokhod \(J_1\) topology. The background criterion used here is the sufficient stopping-time condition for tightness of càdlàg processes in a compact metric state space; see D. Aldous, “Stopping Times and Tightness,” *Annals of Probability* **6** (1978), 335–340. Only this general criterion is used, not a model-specific convergence result.

Every jump of the actual untraced path changes one circle coordinate by \(1/L\). Its largest jump is therefore at most \(1/L\), deterministically. All subsequential limits are continuous: under \(J_1\) convergence, time changes give uniform approximation, and a jump of the limit is bounded by twice that uniform error plus the largest jump of the approximating path. This proves C-tightness of \(X_N\), uniformly over its arbitrary initial laws.

The preceding arguments also justify a pathwise transfer description: (I.5.2)–(I.5.3) give C-tightness of the trace, while (I.3.1), (I.3.4), and (I.3.6) give a clock converging uniformly to the identity and vanishing excursion error. The direct estimate (I.5.4) supplies the stronger check in the original filtration.

For \(n=1\), \(S=\mathbb T_L\), the clock and excursion errors vanish, and the coordinate lift has zero drift and local bracket density \(2q/L^2\) away from a cut. The same nested-chart argument proves the result, with no absorption or correction estimates needed.

## 3. Collision terms and microscopic convergence

**Proposition 3.1 (microscopic path convergence).** Fix \(n\ge1\). Let \(Z_N\) have generator \(N^2(R_n+d_N^{-1}I_n)\) on \(\mathbb T_{L_N}^n\). Under the parameter assumptions of Theorem 1, for every deterministic sequence \(z_N/L_N\to x\in\mathbb T^n\), the laws of \(Z_N/L_N\) started at \(z_N\) converge in \(D([0,\infty),\mathbb T^n)\) to the continuous \(n\)-point law with semigroup \(P_t^{(n)}\). The path topology is Skorokhod \(J_1\).

*Proof.* Proposition 2.1 gives tightness. We identify the collision drift and covariance of each limit. Section 4 proves uniqueness for the resulting local martingale problem.

### 3.1. Positive layers in trace time

Let \(\overline Y_N(u)=Y_u/L\) be the physical-time trace from Section 2. It may start from any distribution on the stable set. Write \(M_n=\binom n2\) and, for \(0<\varepsilon<1/4\), take \(k_N=\lfloor\varepsilon L\rfloor\); eventually \(1\le k_N<L/2\). Denote by \(B_{k_N}\) the positive-layer pair count in Appendix B. To estimate a trace started from a stable state, construct an untraced chain from that same state, with clock \(A\). The exact change of variables in retained time and \(0\le B_{k_N}\le M_n\) give
\[
\int_0^T B_{k_N}(Y_u)\,du
\le \int_0^{T+1}B_{k_N}(Z_s)\,ds
 +M_nT\,\mathbf1_{\{A(T+1)<T\}}.
\]
Indeed, on the complementary event the first integral is the retained part up to the inverse-clock time, which is at most \(T+1\); on the event itself its bound is \(M_nT\). Appendix B with deterministic horizon \(T+1\), and (I.3.1) with Markov's inequality, imply
\[
\begin{aligned}
\sup_y\mathbb E_y\int_0^T B_{k_N}(Y_u)\,du
\le{}&M_n\left[
\frac{2k_N(T+1)}{L+1/d}+\frac{Lk_N}{q}\right]\\
&+M_nT\left[\frac{2c_nd}{q}+4nc_nd(T+1)\right].
\end{aligned}
\tag{II.1}
\]
Thus, for each finite \(T\), there is a finite \(C_{n,T}\), independent of starting states and \(N\) sufficiently large, such that
\[
\sup_y\mathbb E_y\int_0^T B_{k_N}(Y_u)\,du
\le C_{n,T}(\varepsilon+d).
\tag{II.2}
\]
The same bound holds for initial distributions by averaging. For \(n=1\), all layer terms are zero. The estimate is about positive separations only: it does not make time on equality strata small.

### 3.2. Corrected drifts and brackets at every order

Fix a common-cut chart and a compact subset of that chart, so its lattice lifts have a fixed positive margin \(bL\) from the cut. For a chamber-affine \(f\), use \(h_f^a\) from Section 2 and define its trace drift
\[
\beta_{N,f}(z)=q\mathcal T_d^Lh_f^a(z).
\]
For the exact equality partition \(\pi(x)\), define on the chart
\[
b_f(x)=\alpha\rho^2
\sum_{B\in\pi(x)}
\sum_{\varnothing\ne A\subsetneq B}
\frac{(|A|-1)!(|B\setminus A|-1)!}{(|B|-1)!}
\,\partial_{-e_A+e_{B\setminus A}}f(\ell_a(x)).
\tag{II.3}
\]
Here \(\ell_a(x)\) denotes the real chart lift of the rescaled circle tuple, and \(e_A=\sum_{i\in A}e_i\). It is the same lift convention as \(\ell_a(z)/L\) on lattice tuples. Both the directional derivatives and \(b_f\) are constant on each weak-order cell. There are finitely many such cells, so \(|b_f|\le C_nD\).

If \(B_{k_N}(z)=0\), all distinct occupied sites have lattice separation greater than \(\varepsilon L\), also in the line lift. Use assertion (A-H3) with \(R_*=\varepsilon L/16\), which is at least \(16\) eventually. In the one-block case its exact formula applies. Since
\[
\partial_v f^{[L]}(\ell_a(z))
=\partial_v f(\ell_a(z)/L),
\]
(I.4.3) and the scaling show, uniformly over these states,
\[
|\beta_{N,f}(z)-b_f(z/L)|\le D e_N(\varepsilon),
\qquad e_N(\varepsilon)\longrightarrow0
\quad\hbox{for each fixed }\varepsilon>0.
\tag{II.4}
\]
For clarity, the errors here are bounded by a constant times
\[
(\varepsilon L)^{-1/8}
+\left|\frac{qd}{L}-\alpha\rho^2\right|
+\frac{qd^2}{L}+q r^{\lfloor bL-n-2\rfloor}.
\]
On every pre-exit state, including the layer, \(|\beta_{N,f}|+|b_f|\le C_nD\), by assertions (A-H2) and (A-H5), and (I.4.3).

Let \(c_N^{ij}\) be the physical trace covariance density for \(h_i^a,h_j^a\):
\[
c_N^{ij}(z)=\frac q{L^2}\widehat\Gamma_{d,L,a}^{ij}(z).
\]
Assertion (A-H4) and (I.4.4) similarly give a uniform bound \(|c_N^{ij}|\le C_n\), and off the positive layer
\[
\left|c_N^{ij}(z)-2\rho^2\mathbf1_{\{z_i=z_j\}}\right|
\le e_N'(\varepsilon)\longrightarrow0.
\tag{II.5}
\]
Its error is bounded by a constant times
\[
(\varepsilon L)^{-1/2}+d+
\left|\frac q{L^2}-\rho^2\right|
+q r^{\lfloor bL-n-2\rfloor}.
\]
For coordinate tests the oriented sum (II.3) vanishes: \(A\) and \(B\setminus A\) have equal coefficients and opposite derivatives. Therefore \(b_i=0\).

Let \(\zeta_N\) be any stopping time before exit from this compact chart region. The absolute errors are bounded by the off-layer bounds plus \(C_n(D+1)B_{k_N}\). Equation (II.2) gives
\[
\begin{aligned}
\mathbb E\int_0^{T\wedge\zeta_N}
|\beta_{N,f}(Y_u)-b_f(\overline Y_N(u))|\,du&\longrightarrow0,\\
\mathbb E\int_0^{T\wedge\zeta_N}
|c_N^{ij}(Y_u)-2\rho^2\mathbf1_{\{Y_i(u)=Y_j(u)\}}|\,du&\longrightarrow0.
\end{aligned}
\tag{II.6}
\]
Indeed the limsup for fixed \(\varepsilon\) is at most \(C_{n,T}(D+1)\varepsilon\); then let \(\varepsilon\downarrow0\). Restricting an absolute integral to a later starting time or multiplying its integrand by a bounded predictable variable preserves the assertion. All statements are uniform in initial distributions. No exchange between a fixed label order and \(N\) is made.

### 3.3. Passing discontinuous equality and weak-order cells

Consider a convergent subsequence of trace paths. Section 2 makes its limit \(X\) continuous. By the Skorokhod representation theorem we may arrange
\[
\sup_{u\le T}\operatorname{dist}(\overline Y_N(u),X(u))
\longrightarrow0
\quad\hbox{almost surely}
\]
for each integer \(T\). The trace layers retain their expectation bounds under this coupling, since those bounds depend only on individual path laws.

For a fixed pair \(i,j\), put
\[
a_N(u)=\mathbf1_{\{Y_i(u)=Y_j(u)\}},
\qquad a(u)=\mathbf1_{\{X_i(u)=X_j(u)\}}.
\]
At every time with \(a(u)=0\), the positive limiting separation makes \(a_N(u)=0\) eventually. Dominated convergence on the product of probability and time therefore gives
\[
\mathbb E\int_0^T a_N(u)(1-a(u))\,du\longrightarrow0.
\]
For the other mismatch, fix \(\varepsilon>0\). On the event that the uniform coordinate error is at most \(\varepsilon/4\), if \(a=1\) and \(a_N=0\), the discrete positive distance is at most \(\varepsilon L/2\), hence at most \(\lfloor\varepsilon L\rfloor\) for large \(N\). The exceptional event has probability tending to zero. Equation (II.2) consequently yields
\[
\limsup_N\mathbb E\int_0^T(1-a_N(u))a(u)\,du
\le C_{n,T}\varepsilon.
\]
Letting \(\varepsilon\downarrow0\) proves
\[
\mathbb E\int_0^T|a_N(u)-a(u)|\,du\longrightarrow0.
\tag{II.7}
\]

Work now before exits from a relatively compact common-cut region. If two limiting lifted coordinates are unequal at a time, their strict order is eventually the same in the approximations. If they are equal, an order-cell discrepancy can occur only if their equality indicators differ. A union bound over the finitely many pairs, (II.7), and dominated convergence for the unequal pairs prove convergence in expected time integral of the weak-order-cell indicators. Thus every bounded function constant on these cells, in particular (II.3), satisfies
\[
\mathbb E\int_0^{T\wedge\zeta_N\wedge\zeta}
|b_f(\overline Y_N(u))-b_f(X(u))|\,du\longrightarrow0
\tag{II.8}
\]
whenever the two paths there lie in the common compact chart region. If \(\zeta_N\wedge T\to\zeta\wedge T\), boundedness also removes the difference of the integration endpoints. These conclusions include the complete equality partition and all collision multiplicities; pairwise stickiness alone is not the identification being used.

### 3.4. Local martingale passage, including stopping times

Here are the localization details used to pass the finite-chain martingales. On a relatively compact chart region, \(h_f^a\) converges uniformly to the chart function \(f\). It is bounded on the entire circle stable set for fixed \(f\), uniformly in \(N\): the lift lies in a bounded cube and its correction is at most \(a_nD/L\). Its drift is bounded before exit. Therefore the stopped Dynkin martingales and their increments are uniformly integrable. For products of corrected coordinates the finite-chain generator identity is
\[
q\mathcal T_d^L(h_i^ah_j^a)
=h_i^a\beta_{N,j}+h_j^a\beta_{N,i}+c_N^{ij}.
\tag{II.9}
\]
The right side is also uniformly bounded before chart exit, so its stopped martingales have the same integrability property. No fourth-moment assertion for a product of unbounded lifts is needed.

We justify the choice and passage of exits without an unproved continuity assumption about hitting times. Fix a deterministic time \(s\), a chart point \(c\), and a radius \(r\) whose closed ball lies inside the chart. Put
\[
\sigma_s(r)=\inf\{u\ge s:\operatorname{dist}(X(u),c)\ge r\},
\]
including \(s\) if \(X(s)\) is already outside. Define \(\sigma_{N,s}(r)\) similarly. For uniformly convergent paths and every \(\delta>0\), the exit times at radii \(r-\delta,r+\delta\) bound the liminf and limsup of the approximating exit times at \(r\). The map \(r\mapsto \sigma_s(r)\wedge T\) is monotone, and hence has at most countably many discontinuities for each path. At every continuity radius its left and right bounding values agree. Fubini's theorem shows that for Lebesgue-almost every radius the exits converge almost surely after truncation at each integer \(T\). Also avoid radii satisfying \(\mathbb P(\operatorname{dist}(X(s),c)=r)>0\); there are at most countably many. Choose radii avoiding these exceptional sets simultaneously for every rational \(s\) and integer \(T\). A countable dense set of centers and a dense selection of permitted radii gives a deterministic basis of relatively compact chart balls.

For any such ball, stop the finite-chain martingales beginning at rational \(s\) at \(\sigma_{N,s}(r)\). On the event the initial state is outside the ball their increment is zero. On its complementary event, all pre-exit points and the limiting exit point lie in a compact subset of the chart. The possible microscopic overshoot is included in the generator and terminal value; its size tends to zero by Section 2. The exit-time convergence, (II.6)–(II.8), and boundedness pass both the Dynkin identity and the product identity to the limit. To check the martingale property rather than just its mean, multiply an increment between \(u\) and \(t\) by any bounded continuous cylinder of the path up to \(u\). Uniform path convergence and the same integral convergence pass this identity. Such cylinders generate the path sigma field, so the monotone-class theorem gives the conditional martingale identity. Rational \(u,t\), followed by continuity of the martingale and its bounded integral term, suffice for all times.

For precision, identities obtained this way at rational entry times extend to arbitrary entry stopping times inside a smaller ball. Let \(\theta\) be a bounded stopping time at which \(X(\theta)\) belongs to a ball with closure inside one of the preceding balls, and approximate \(\theta\) from above by dyadic stopping times \(\theta_m\). The rational-entry identities, partitioned over the finitely many values of each \(\theta_m\), hold conditionally on the past. By continuity and the positive margin, \(\theta_m\) precedes exit from the smaller ball for all sufficiently large \(m\) on each path. Stop those martingales additionally at this smaller-ball exit. Optional sampling applies because their values and drift integrals are bounded on fixed horizons. Letting \(m\to\infty\) passes the entry value and integral by continuity and bounded convergence and yields the identity starting at \(\theta\). Localization removes a bound on \(\theta\).

Finally, cover any compact subset of a chart by finitely many such smaller balls, each with closure in an available larger ball. Select a ball measurably at each exit and repeat. The distances between the selected inner closures and the corresponding outer complements have a positive minimum. Continuity gives only finitely many such exits on each finite horizon. Concatenating the stopped martingale identities therefore proves the local identities up to any exit from a relatively compact subset of the chart. This argument does not assume that the limiting process is Markov.

It follows that every trace limit has, in every common-cut chart, continuous coordinate local martingales \(Z_i\), and
\[
\langle Z_i,Z_j\rangle_{t\wedge\zeta}
=2\rho^2\int_0^{t\wedge\zeta}
\mathbf1_{\{Z_i(u)=Z_j(u)\}}\,du.
\tag{II.10}
\]
Indeed (II.6) makes each coordinate drift integral tend to zero. Equation (II.9), bounded corrected coordinates, and (II.6)–(II.8) make
\(Z_iZ_j-2\rho^2\int\mathbf1_{\{Z_i=Z_j\}}\)
a local martingale. The product characterization of quadratic covariation then gives (II.10). For every chamber-affine \(f\),
\[
f(Z_{t\wedge\zeta})-f(Z_0)
-\int_0^{t\wedge\zeta}b_f(X(u))\,du
\quad\hbox{is a martingale.}
\tag{II.11}
\]
The chamber-affine space is finite dimensional, because its finitely many affine pieces determine the function. Applying the argument to a basis and using linearity gives a common full-measure set for all its functions. These are all the tests needed below.

### 3.5. Identification of every full untraced point-start limit

Section 4 proves internally that (II.10)–(II.11) determine exactly the \(n\)-point law in Theorem 1, from every point, on the circle. Thus every trace subsequential limit is that target law.

This also identifies the full chain, for arbitrary starts. Let \(z_N\in\mathbb T_{L_N}^n\) be any sequence with \(z_N/L_N\to x\). The trace starts at the first absorbed state if necessary. The arbitrary-start bound (I.2.2) shows that its initial rescaled position differs from \(z_N/L_N\) by a quantity tending to zero in probability. Section 2 gives tightness of the trace and the original paths, a clock uniformly approaching the identity, and deleted-excursion error tending to zero. Explicitly, C-tightness of the trace gives a modulus of continuity in probability, so (I.3.6) implies
\[
\sup_{t\le T}\operatorname{dist}(Z_t/L_N,Y_t/L_N)
\le D_T+
\sup_{\substack{u,v\le T\\ |u-v|\le\sup_{s\le T}|A(s)-s|}}
\operatorname{dist}(Y_u/L_N,Y_v/L_N)
\longrightarrow0
\]
in probability. Here \(A(t)\le t\), and C-tightness makes the displayed modulus valid despite the small trace jumps. Therefore original and trace subsequential limits coincide. Compactness and the unique identification imply
\[
\operatorname{Law}_{z_N}(Z_\cdot/L_N)
\Longrightarrow P_x^{(n)}
\quad\hbox{in }D([0,\infty),\mathbb T^n),
\tag{II.12}
\]
where \(P_x^{(n)}\) is the continuous target \(n\)-point path law. If convergence failed, tightness would supply a subsequence with a further limit contradicting the identification. The same argument applies on every integer horizon and hence on the full path space. For \(n=1\), the zero drift and bracket \(2q/L^2\) in Section 2 give the Brownian case directly. At no order was the initial tuple required to be stable, separated, stationary, or sampled from a reference law.

## 4. Identification of the continuum target


### 4.1. Local martingale characterization

Fix \(n\geq 1\), \(\alpha>0\), and \(\rho>0\). Write \(m=m_{\alpha,n}\), \(p(\pi)=p_\alpha(\pi)\), and \(\mathcal E=\mathcal E_n\) for the exact measure and closed form in the statement. For a circle configuration \(x\), write \(\pi(x)\) for its exact equality partition. For a block \(B\), put
\[
e_B=\sum_{i\in B}e_i,
\qquad D_B=e_B\cdot\nabla.
\]
For \(\varnothing\ne A\subsetneq B\), put \(C=B\setminus A\) and
\[
v_{A,C}=-e_A+e_C,
\qquad
r(A,C)=\frac{(|A|-1)!(|C|-1)!}{(|B|-1)!}.
\]
Directional derivatives at a collision are one-sided derivatives along the displayed vector. Let \(\mathcal H_n\) be the continuous real functions on \(\mathbb R^n\) that are linear on each chamber of the weak coordinate-order decomposition, as in Howitt–Warren's space \(L_n\). Constants may be added without changing any assertion.

**Proposition 4.1 (characterization of the sticky motion).** Choose a common-cut chart \(U=(\mathbb T\setminus\{q\})^n\), with lift \(z:U\longrightarrow I^n\), where \(I\) is an open interval of length one. Choose an open \(W\) with \(\overline W\subset U\), and let \(\tau\) be its first exit time. For the target started at any deterministic \(x\in W\), set \(Z_t=z(X_t)\) up to \(\tau\). Then the stopped coordinates are continuous local martingales and
\[
\langle Z_i,Z_j\rangle_{t\wedge\tau}
=2\rho^2\int_0^{t\wedge\tau}
\mathbf 1_{\{Z_i(s)=Z_j(s)\}}\,ds.
\tag{III.1}
\]
For every \(h\in\mathcal H_n\),
\[
h(Z_{t\wedge\tau})-h(Z_0)
-\int_0^{t\wedge\tau}\mathcal B h(Z_s)\,ds
\tag{III.2}
\]
is a martingale, where
\[
\mathcal B h(z)
=\alpha\rho^2
\sum_{B\in\pi(z)}
\sum_{\varnothing\ne A\subsetneq B}
r(A,B\setminus A)D_{v_{A,B\setminus A}}h(z).
\tag{III.3}
\]
The inner sum is oriented: both \(A\) and \(B\setminus A\) occur. These local identities determine the continuous circle path law uniquely, including starts on arbitrary collision strata.

*Proof.* We first identify the partition forms with the continuum construction. We then derive the local martingale identities and prove uniqueness.

The target is indeed the Brownian specialization of Le Jan–Raimond's construction. Their parameter is \(\tau_0=1/(1+\alpha)\): the predictive probabilities in their Section 2 become \(\alpha/(\alpha+n)\) for a new block and \(|B|/(\alpha+n)\) for joining block \(B\). Starting from the unique partition of one label, these recurrences give precisely the displayed \(p_\alpha\) in the statement. Their equation (3.6), with one-point generator \(\rho^2\partial_{xx}\), gives precisely \(\mathcal E\). Their smooth form core agrees with the closure specified in the statement. Theorem 3.3 supplies compatible strong Feller semigroups. Compatibility with the one-point Brownian motion gives continuous coordinate paths, hence continuous joint paths, for every starting point. [Le Jan–Raimond, Sections 2–3 and Theorem 3.3](https://arxiv.org/pdf/math/0211387v1).

### 4.2. Cutoff chamber-linear functions belong to the closed form domain

Let \(\chi\) be a smooth function compactly supported in \(U\), and extend
\[
f(x)=\chi(x)h(z(x))
\]
by zero outside \(U\). The function \(f\) is globally Lipschitz on the torus and is smooth on the closures of its finitely many local chambers. Let \(f_\varepsilon\) be its convolution with a smooth periodic approximate identity in the ambient \(n\) coordinates.

Here ambient mollification must be checked on every lower-dimensional summand of the form. Fix \(\pi\) and a point of its exact stratum. In a sufficiently small neighborhood, the only collision hyperplanes through that point are those internal to blocks of \(\pi\). The affine pieces of \(h\) in all neighboring chambers agree on the local subspace where the coordinates within each block are equal. Therefore their derivatives along each \(e_B\), \(B\in\pi\), agree with the derivative of that trace. Multiplying by the smooth \(\chi\) preserves the corresponding limiting statement. Differentiating convolution along \(e_B\) consequently gives
\[
D_B f_\varepsilon(x)\longrightarrow
\partial_{y_B}(f\circ\iota_\pi)(y),
\qquad x=\iota_\pi(y),
\]
for Lebesgue-almost every block-coordinate vector \(y\). The excluded additional coincidences have zero Lebesgue measure in those block coordinates. All these derivatives are uniformly bounded by a fixed multiple of the Lipschitz constant of \(f\). Dominated convergence, applied to the finitely many \(\pi\), gives convergence of these tangential gradients in every summand of the form. Also \(f_\varepsilon\to f\) uniformly. Thus \(f_\varepsilon\) is Cauchy in the form norm, \(f\) belongs to the specified closed form domain, and its form derivatives are exactly the trace derivatives just described.

This argument also applies to a smooth cutoff times any smooth polynomial in the chart coordinates. For such a polynomial the extended cutoff function is already smooth globally.

### 4.3. Integration by parts and the oriented coefficient

On the exact stratum of \(\pi\), define the bounded Borel function
\[
b_f(x)=\rho^2\sum_{B\in\pi}D_B^2 f(x)
+\alpha\rho^2\sum_{B\in\pi}
\sum_{\varnothing\ne A\subsetneq B}
r(A,B\setminus A)D_{v_{A,B\setminus A}}f(x).
\tag{III.4}
\]
The second derivative here is taken along the smooth restriction to that stratum; the first derivative in each splitting direction is taken from the adjacent chamber. These derivatives exist. The cutoff, the finite chamber decomposition, and the finite number of partitions make \(b_f\) bounded. Outside the cutoff's chart neighborhood they vanish.

To verify (III.4), integrate each summand of \(\mathcal E(f,g)\), for smooth \(g\), by parts in its own block coordinates, subdividing into strict-order chambers. Interior terms give minus the first term of (III.4). A face with exactly two block coordinates equal belongs to a partition obtained by merging those blocks; intersections of multiple faces have zero surface measure and create no additional term.

More explicitly, suppose \(\sigma\) refines \(\pi\) by replacing \(B\) with the unordered pair \(\{A,C\}\). On the side \(y_A<y_C\), the outward unit normal is \((e_A-e_C)/\sqrt 2\) in the two independent block coordinates. Its flux is
\[
-\frac{1}{\sqrt 2}D_{v_{A,C}}f.
\]
Parameterizing the face by the common coordinate \(y_A=y_C=u\) multiplies surface measure by \(\sqrt 2\). The contribution to \(\mathcal E(f,g)\) is therefore
\[
-\rho^2 p(\sigma)\int D_{v_{A,C}}f\,g\,d\lambda_\pi.
\]
The opposite side gives the same expression with \(A,C\) reversed. These are two sides of one refined stratum, each counted once. The metric here is the metric of the independent block coordinates in the stated form; there is no block-size factor from the ambient embedding into \(\mathbb T^n\). Finally,
\[
\frac{p(\sigma)}{p(\pi)}
=\alpha\frac{(|A|-1)!(|C|-1)!}{(|B|-1)!}
=\alpha r(A,C).
\tag{III.5}
\]
Summing the interiors and faces, with no outer boundary term because of the cutoff, proves
\[
\mathcal E(f,g)=-\int b_f g\,dm
\tag{III.6}
\]
for every smooth \(g\). Form-core density extends (III.6) to all form-domain \(g\). Since \(b_f\in L^2(m)\), the definition of the operator associated with the closed symmetric form yields
\[
f\in D(L),\qquad Lf=b_f\quad\text{in }L^2(m).
\tag{III.7}
\]
For \(f=\chi h\), the terms involving \(hD_v\chi\) in the splitting sum cancel between the two orientations. On a neighborhood where \(\chi=1\), the tangential second derivatives of \(h\) vanish and (III.4) reduces exactly to (III.3).

### 4.4. From the operator identity to every deterministic starting point

The measure \(m\) has full support: its all-singleton summand has a strictly positive coefficient multiplying \(n\)-dimensional Haar measure. Let \(P_t\) be the everywhere-defined strong Feller version from Le Jan–Raimond. For the bounded continuous \(f\) above, (III.7) gives the semigroup identity in \(L^2(m)\)
\[
P_t f-f=\int_0^t P_s b_f\,ds.
\tag{III.8}
\]
For every \(s>0\), \(P_s b_f\) is continuous and bounded by \(\|b_f\|_\infty\). Dominated convergence in \(s\) shows that the right side of (III.8), evaluated using the strong Feller version, is continuous in the starting point. The left side is continuous as well. Since two continuous functions equal \(m\)-almost everywhere are equal everywhere when \(m\) has full support, (III.8) holds at every starting point.

For completeness, choosing bounded Borel representatives causes no exceptional-point ambiguity: if \(a=0\) \(m\)-almost everywhere, then \(P_s|a|=0\) \(m\)-almost everywhere by the associated \(L^2\) semigroup. Strong Feller continuity and full support make it zero everywhere for \(s>0\).

The Markov property and conditional Fubini now give, for every initial point and \(0\leq s\leq t\),
\[
\mathbb E\left[
f(X_t)-f(X_s)-\int_s^t b_f(X_r)\,dr
\,\middle|\,\mathcal F_s\right]=0.
\tag{III.9}
\]
Indeed its conditional value is (III.8) at \(X_s\), with time \(t-s\). All quantities are integrable because \(f,b_f\) are bounded. Thus the form calculation yields an actual continuous martingale from every deterministic start, including all collision starts. No statement about capacity or a quasi-everywhere exceptional set is needed.

Choose \(\chi=1\) on a neighborhood of \(\overline W\). Apply (III.9) and optional stopping to \(\chi h\). Equation (III.4) gives (III.2). Apply the same reasoning to cutoff versions of \(z_i\) and \(z_i z_j\). Their splitting sums cancel, because these functions are smooth. Within \(W\),
\[
Lz_i=0,
\qquad
L(z_i z_j)=\rho^2\sum_{B\in\pi(z)}D_B^2(z_i z_j)
=2\rho^2\mathbf 1_{\{z_i=z_j\}}.
\tag{III.10}
\]
The equality holds also for \(i=j\). The product characterization of quadratic covariation for continuous local martingales gives (III.1). Exhausting a common-cut chart by such \(W\) gives the asserted local version throughout the chart.

### 4.5. Exact Howitt–Warren parameters, including zero indices

Howitt–Warren use bracket rate one and vectors with plus signs on a set \(I\) and minus signs on a disjoint set \(J\). Their Definition 2.1 requires chamber-linear martingales and the equality-indicator bracket; Theorem 2.1 gives existence and uniqueness from every real starting point when the nonnegative-index parameter family is consistent and its strictly positive-index entries are nonnegative. [Howitt–Warren, Definition 2.1 and Theorem 2.1](https://arxiv.org/pdf/math/0611292v2).

Set \(c=\alpha/2\) and, for \(k,l\geq1\),
\[
\theta(k:l)=c\frac{(k-1)!(l-1)!}{(k+l-1)!}.
\tag{III.11}
\]
Define \(H_0=0\), \(H_j=\sum_{r=1}^j r^{-1}\), and complete the family by
\[
\theta(k:0)=\theta(0:k)=-cH_{k-1}\quad(k\geq1),
\qquad \theta(0:0)=0.
\tag{III.12}
\]
For positive \(k,l\), the factorial identity immediately gives
\[
\theta(k:l)=\theta(k+1:l)+\theta(k:l+1).
\]
On an axis, the same identity follows from
\[
-cH_{k-1}=-cH_k+\frac{c}{k},
\qquad \theta(k:1)=\frac{c}{k}.
\]
At \((0,0)\) it reads \(0=0+0\). Thus consistency holds at every nonnegative pair. The positive-index entries are positive, as required; the theorem does not require the zero-index entries to be nonnegative. The drift \(\theta(1:0)-\theta(0:1)\) is zero.

For an exact block \(B\), the two zero-index directions have equal coefficients and opposite tangential derivatives, and hence cancel:
\[
\theta(|B|:0)D_{e_B}h+
\theta(0:|B|)D_{-e_B}h=0.
\]
Under the time change \(Y_u=Z_{u/(2\rho^2)}\), equation (III.1) has unit bracket rate and (III.3) becomes the Howitt–Warren operator with (III.11)–(III.12). The correspondence of orientations is \(I=C\), \(J=A\); symmetry of (III.11) makes their coefficient \(\theta(|C|:|A|)=c r(A,C)\). Thus the physical-time coefficient is exactly \(2\rho^2\theta=\alpha\rho^2 r\).

As an independent symbolic normalization check, for \(n=2\) and \(h(z)=|z_1-z_2|\), both oriented derivatives at equality are \(2\), so (III.3) equals \(4\alpha\rho^2\mathbf 1_{\{z_1=z_2\}}\). After division by \(2\rho^2\), this is \(2\alpha\mathbf 1_{\{z_1=z_2\}}=4\theta(1:1)\mathbf 1_{\{z_1=z_2\}}\), matching the direct computation following Howitt–Warren's Definition 2.1. This pair check supplements, and does not replace, the all-block computation (III.5).

### 4.6. Uniqueness for stopped charts and gluing on the circle

First, the real theorem implies uniqueness up to exit from a bounded open set \(O\subset\mathbb R^n\). To see this without presupposing a localization theorem, take any continuous solution of the real martingale identities stopped at its exit time \(\sigma\) from \(O\). At \(\sigma<\infty\), append a fresh global real Howitt–Warren solution started at the exit point. The family of these continuation laws is Borel: Proposition 8.1 gives Feller transition semigroups, and their rational-time finite-dimensional distributions determine the Borel path laws. [Howitt–Warren, Proposition 8.1](https://arxiv.org/pdf/math/0611292v2).

The appended law solves the full real problem. Conditioning before and after \(\sigma\), and optional sampling for the stopped prefix, verify the chamber-linear martingale and coordinate-product identities. Their brackets concatenate in the same way. These checks can first be made with bounded stopping times and then localized. They give true martingales on each finite horizon: coordinate local martingales have bounded bracket rate, hence bounded second moments and square-integrable maxima; every chamber-linear function is globally Lipschitz, and its drift is bounded because the chamber decomposition is finite. These bounds remove the localization. When \(\sigma=\infty\), the original path already supplies the entire solution. Theorem 2.1 therefore determines the appended law and hence its prefix stopped at the first exit from \(O\). This proves stopped uniqueness. Applying the deterministic time change proves the corresponding assertion for the physical rates (III.1)–(III.3).

Apply stopped uniqueness to the lift of \(W\Subset U\). Equality of real coordinates is exactly equality of circle coordinates in this common-cut chart, so the lifted stopped path solves precisely the stopped real problem. The result therefore identifies its entire stopped path law, not just its endpoint distribution.

Finally, choose finitely many nested open sets
\[
\overline V_a\subset W_a,
\qquad \overline W_a\subset U_a,
\]
where each \(U_a\) is a common-cut chart and the \(V_a\) cover \(\mathbb T^n\). Such charts cover the space because a finite configuration always omits some point of the circle; compactness then supplies the finite nested cover. Fix a compatible metric and put
\[
\delta=\min_a\operatorname{dist}(\overline V_a,W_a^c)>0.
\]
Starting at a chart-entry point, choose the first \(a\) with that point in \(V_a\), run until exit from \(W_a\), and repeat. Each finite exit requires a displacement at least \(\delta\). A continuous path is uniformly continuous on every finite time interval, so these exit times cannot accumulate in finite time.

For any proposed circle solution of the local identities, conditional laws at the chart-entry stopping times satisfy the corresponding stopped problem. This follows directly from optional sampling and disintegration, using a finite basis of the chamber-linear space together with the coordinate and coordinate-product tests; rational time tests suffice to obtain one common conditional full-measure set. Stopped uniqueness determines each next segment from its entry point, regardless of earlier history. Induction therefore determines all successive stopped-segment laws. The absence of finite accumulation determines the full continuous path law on every finite horizon, and hence on \([0,\infty)\). The already constructed target satisfies the local identities, so it is this unique law.

## 5. Convergence of the full mass process

The arguments here hold for all microscopic occupation states. Only their final application is restricted to the finite-stack initial sequences in Theorem 1.


### 5.1. Uniform fixed-order semigroups and resolvents

**Lemma 5.1 (uniform microscopic semigroup convergence).** For \(\phi\in C(\mathbb T^n)\), write \(\phi_N(z)=\phi(z/L_N)\), and let \(P_{N,t}^{(n)}\) denote the semigroup of the auxiliary process in Proposition 3.1. Then for every finite \(T\),
\[
\sup_{0\le t\le T}\sup_{z\in(\mathbb Z/L_N\mathbb Z)^n}
\left|P_{N,t}^{(n)}\phi_N(z)
-(P_t^{(n)}\phi)(z/L_N)\right|
\longrightarrow0.
\tag{IV.1.1}
\]
*Proof.* Suppose that the assertion fails. Select a subsequence of \(t_N\in[0,T]\) and starting tuples \(z_N\) witnessing a fixed positive error. Compactness gives a further subsequence with \(t_N\to t\) and \(z_N/L_N\to x\). The prescribed-start path convergence (II.12), whose limit is continuous, gives
\[
P_{N,t_N}^{(n)}\phi_N(z_N)\longrightarrow (P_t^{(n)}\phi)(x).
\]
The target is Feller and strongly continuous on \(C(\mathbb T^n)\), so \((s,y)\mapsto P_s^{(n)}\phi(y)\) is jointly continuous: for \(s_m\to s\), the semigroup law and its contraction property give uniform time continuity, followed by spatial continuity at \(s\). Thus the second term at \((t_N,z_N/L_N)\) has the same limit, a contradiction. This includes \(t=0\).

For every \(\lambda>0\), define the ordinary Laplace resolvents \(R_{N,\lambda}^{(n)}\) and \(R_\lambda^{(n)}\). Integrating (IV.1.1) up to \(T\), and bounding both tails by \(\|\phi\|_\infty e^{-\lambda T}/\lambda\), proves
\[
\sup_z\left|
R_{N,\lambda}^{(n)}\phi_N(z)
-(R_\lambda^{(n)}\phi)(z/L_N)
\right|\longrightarrow0.
\tag{IV.1.2}
\]
This proves the actual all-fixed-order microscopic semigroup and resolvent convergence from prescribed point starts.

### 5.2. Exact factorial lift to the full mass semigroup

Write \(T_{N,t}\) for the full \(N\)-particle occupation semigroup and \(G_{N,n}\) for the occupation generator of the auxiliary order-\(n\) process of Section 3. It is the quotient of the labelled generator on symmetric functions. In particular it uses acceleration \(N^2/d_N\), not \(n^2/d_N\). Fix \(n\ge1\), take \(N\ge n\), and write \(d=d_N\), \(L=L_N\). For an auxiliary occupation \(k\) of total mass \(n\), define
\[
W_k(\eta)=\prod_x\binom{\eta_x}{k_x},\qquad
D_{N,n}f(\eta)=\binom Nn^{-1}\sum_{\sum_x k_x=n}W_k(\eta)f(k).
\tag{IV.2.1}
\]
Here a symmetric tuple function is identified with its occupation function. The binomial theorem gives \(\sum_kW_k(\eta)=\binom Nn\), so \(D_{N,n}\) is an averaging contraction.

We prove its exact intertwining algebraically. On one undirected edge with occupations \(a,b\), put \(J(u,v)=(1+u)^a(1+v)^b\). Its two unaccelerated jump rates give
\[
L^{\mathrm{edge}}J
=d(v-u)(\partial_u-\partial_v)J+(v-u)^2\partial_u\partial_vJ.
\tag{IV.2.2}
\]
Indeed, the two jump increments factor respectively as \((v-u)(1+u)^{a-1}(1+v)^b\) and \((u-v)(1+u)^a(1+v)^{b-1}\). The independent terms give the first summand in (IV.2.2); the terms multiplied by \(ab\) give its second summand.

Fix edge components \(r=k_x\), \(s=k_y\). Extracting the coefficient of \(u^rv^s\), and keeping the unchanged binomial factors at other sites, gives
\[
\begin{aligned}
L^{\mathrm{edge}}W_k={}&(r+1)(d+s-1)W_{k+\delta_x-\delta_y}
+(s+1)(d+r-1)W_{k-\delta_x+\delta_y}\\
&-[r(d+s)+s(d+r)]W_k.
\end{aligned}
\tag{IV.2.3}
\]
Terms with negative occupation indices are absent. This convention also handles \(r=0\) or \(s=0\), with no negative-index binomial being evaluated. Multiplying by \(f(k)\), summing over \(k\), and changing indices in the first two sums gives the two directed inclusion rates acting on \(f\). For example, in the first sum set \(\ell=k+\delta_x-\delta_y\); its coefficient becomes \(\ell_x(d+\ell_y)\) and its test is \(f(\ell-\delta_x+\delta_y)\). The second sum is the reverse direction. Summing the undirected edges and restoring the common acceleration proves
\[
\mathcal L_N D_{N,n}=D_{N,n}G_{N,n}.
\tag{IV.2.4}
\]
For \(L=3\), the three undirected edges still represent exactly the six directed nearest-neighbor jumps, so the same identity holds with no edge-multiplicity change. Only eventually \(L\ge3\) is required by the target.

Both state spaces are finite. Induction on powers of the generators in (IV.2.4), followed by their convergent matrix-exponential series, proves
\[
T_{N,t}D_{N,n}f=D_{N,n}P_{N,t}^{(n)}f.
\tag{IV.2.5}
\]
This is uniform sampling without replacement. It does not assert that specified physical labels evolve autonomously.

For \(f\in C(\mathbb T^n)\), let \(f_N\) be its restriction to the rescaled grid and let
\[
F_f(\mu)=\int f\,d\mu^{\otimes n}.
\]
Symmetrize \(f\) if necessary; this leaves \(F_f\) unchanged, and permutation invariance of both labelled semigroups preserves the symmetrization. Sampling \(n\) physical indices independently with replacement realizes \(F_f(\Phi_N(\eta))\). Conditional on all indices being distinct, their positions realize \(D_{N,n}f_N(\eta)\). The union bound gives repeated-index probability at most \(n(n-1)/(2N)\). Therefore
\[
\sup_{\eta\in\Omega_N}
\left|D_{N,n}f_N(\eta)-F_f(\Phi_N(\eta))\right|
\le\frac{n(n-1)}N\|f\|_\infty.
\tag{IV.2.6}
\]

Put \(\epsilon_N(n,f,T)\) equal to the supremum in (IV.1.1), which tends to zero for every fixed \(n,f,T\). Apply (IV.2.5), the averaging and semigroup contractions, (IV.2.6), and the defining target identity
\(\mathsf P_tF_f(\mu)=\int P_t^{(n)}f\,d\mu^{\otimes n}\).
They give, for every finite \(T\),
\[
\begin{aligned}
\sup_{0\le t\le T}\sup_{\eta\in\Omega_N}
\left|T_{N,t}(F_f\circ\Phi_N)(\eta)
-(\mathsf P_tF_f)(\Phi_N(\eta))\right|
\le \epsilon_N(n,f,T)+\frac{2n(n-1)}N\|f\|_\infty
\longrightarrow0.
\end{aligned}
\tag{IV.2.7}
\]
The second sampling bound here is applied to \(P_t^{(n)}f\), whose norm is at most \(\|f\|_\infty\); hence it is uniform over \(t\).

The space \(\mathcal P(\mathbb T)\) is compact metric in the weak topology. The real algebra generated by \(\mu\mapsto\langle\mu,\varphi\rangle\), for real \(\varphi\in C(\mathbb T)\), contains constants and separates probability measures; each of its products is a mass polynomial. Stone–Weierstrass makes this algebra uniformly dense in \(C(\mathcal P(\mathbb T))\). Approximate a given real continuous \(G\) uniformly by a finite sum of such polynomials. The error contributed by replacing \(G\) is at most twice the approximation error, since both semigroups are contractions. Applying (IV.2.7) to that finite sum and then reducing the approximation error proves
\[
\sup_{0\le t\le T}\sup_{\eta\in\Omega_N}
\left|T_{N,t}(G\circ\Phi_N)(\eta)
-(\mathsf P_tG)(\Phi_N(\eta))\right|\longrightarrow0.
\tag{IV.2.8}
\]
Real and imaginary parts give the same result for complex tests if desired.

For \(\lambda>0\), define the full microscopic resolvent \(\mathcal R_{N,\lambda}\) and mass resolvent \(\mathsf R_\lambda\) by integrating their semigroups against \(e^{-\lambda t}\). The error up to \(T\) is at most \(\lambda^{-1}\) times the supremum in (IV.2.8). The sum of the two tails is at most \(2\|G\|_\infty e^{-\lambda T}/\lambda\). First letting \(N\to\infty\) and then \(T\to\infty\) proves
\[
\sup_{\eta\in\Omega_N}
\left|\mathcal R_{N,\lambda}(G\circ\Phi_N)(\eta)
-(\mathsf R_\lambda G)(\Phi_N(\eta))\right|\longrightarrow0
\quad(\lambda>0,\ G\in C(\mathcal P(\mathbb T))).
\tag{IV.2.9}
\]
In particular, the supremum is over the entire microscopic state space, independently of the initial finite-stack hypothesis.

### 5.3. Continuous paths for the exact target mass semigroup

We verify target continuity directly using its compatible polynomial semigroups. Their compatibility and strong Feller property are part of the construction checked in Section 4; their polynomial identity is the identity in Section 1. Fix a deterministic \(\mu\in\mathcal P(\mathbb T)\), a real smooth periodic \(\varphi\), and \(c=\langle\mu,\varphi\rangle\). If \(\nu\) has mass transition law at time \(t\), expansion of the fourth power and consistency give
\[
\mathbb E_\mu(\langle\nu,\varphi\rangle-c)^4
=\int\mu^{\otimes4}(dx)\,
P_t^{(4)}\left[\prod_{i=1}^4(\varphi(y_i)-\varphi(x_i))\right](x).
\tag{IV.3.1}
\]
For each fixed \(x\), the bracket denotes a function of the terminal vector \(y\). To check (IV.3.1), expand its product by subsets of the four terminal factors. A subset of cardinality \(r\) reduces under coordinate consistency to the \(r\)-point transition; integration of the remaining initial factors gives \(c^{4-r}\). Integrating the selected initial coordinates gives the corresponding degree-\(r\) target mass moment. These are exactly the binomial terms on the left. Every initial integration is deterministic, and the Feller transition kernels make these integrals measurable.

For real \(a_i\), the arithmetic-geometric mean inequality gives \(|a_1a_2a_3a_4|\le\tfrac14\sum_i|a_i|^4\). Each target coordinate is circle Brownian motion with generator \(\rho^2\partial_{xx}\), by Section 4 (or the one-point form and compatibility). Its real lift increment has variance \(2\rho^2t\). Since \(|\varphi(x+u)-\varphi(x)|\le\|\varphi'\|_\infty|u|\) for the periodic lift, its fourth Gaussian moment gives
\[
\mathbb E_\mu|\langle\nu-\mu,\varphi\rangle|^4
\le12\rho^4\|\varphi'\|_\infty^4t^2.
\tag{IV.3.2}
\]
The bound is uniform over deterministic \(\mu\). The Markov property therefore gives, for every deterministic \(s<t\), the same conditional bound with \(t-s\) and the random state at time \(s\). This evaluates a deterministic transition function of that state. It does not integrate an almost-sure kernel identity at an unverified random atom.

Here is an explicit construction of the continuous modification. On level-\(m\) dyadic partitions of a fixed finite horizon, (IV.3.2), Markov's inequality, and the union bound show that the probability of any adjacent \(\varphi\)-coordinate increment exceeding \(2^{-\gamma m}\) is at most a constant times \(2^{-(1-4\gamma)m}\). Choose \(0<\gamma<1/4\). This bound is summable, so Borel–Cantelli implies the adjacent bounds at every sufficiently fine level. For a dyadic point and any finer dyadic approximation, the increments along successive enclosing dyadic intervals are bounded by a constant times the geometric sum \(\sum_{j\ge m}2^{-\gamma j}\). Joining two such chains proves uniform continuity on dyadic times and yields a unique continuous extension. The fourth-moment estimate identifies the extension with the original coordinate at each fixed time by convergence in probability.

Choose a countable uniformly dense collection of real smooth periodic tests, normalize each to norm at most one, and perform this construction simultaneously for these tests and every integer horizon. Their common probability-one event determines a continuous probability-measure-valued path: at any new time, compactness gives subsequential weak limits of the dyadic measures, and agreement of every test coordinate makes all such limits equal. The metric
\[
d_*(\mu,\nu)=\sum_{j\ge1}2^{-j}|\langle\mu-\nu,\varphi_j\rangle|
\]
metrizes the weak topology and proves continuity of this path by uniform control of finitely many coordinates and the summable tail. At each fixed time it equals the original process almost surely. Equality at the countable dense times and right-continuity make it indistinguishable from a càdlàg Feller realization. Equivalently, the continuous modification itself has the same finite-dimensional distributions and hence the same Markov semigroup. This proves the required continuous-path law for every deterministic initial measure without an exceptional-set assumption about random kernel evaluations.

### 5.4. Proof of the full mass convergence theorem

*Proof of Theorem 1.* Apply Theorem C.1 to
\[
E=\mathcal P(\mathbb T),\qquad
S_N=\Omega_N,\qquad
Z_N=\eta_N,\qquad
\pi_N=\Phi_N,\qquad
P_t=\mathsf P_t.
\tag{IV.4.1}
\]
The reference metric on \(E\) can be the Wasserstein distance of order one associated with the bounded geodesic distance on \(\mathbb T\); on a compact underlying space it metrizes weak convergence. Compactness follows from compactness of \(\mathbb T\). Each \(\Omega_N\) is finite and its generator is exactly the accelerated generator in Section 1. The supplied mass semigroup is conservative and strongly continuous Feller; Section 5.3 verifies its continuous-path realization from every state. Equation (IV.2.9) is the uniform positive-resolvent hypothesis of Theorem C.1 for every continuous test and every microscopic state.

Finally, a microscopic jump moves mass \(1/N\) from \(x/L_N\) to a nearest neighbor. Coupling the unchanged mass to itself and the moved mass to its new site gives
\[
\sup_{\mathcal L_N(\eta,\eta')>0}
W_1(\Phi_N(\eta),\Phi_N(\eta'))\le\frac1{NL_N}\longrightarrow0.
\tag{IV.4.2}
\]
Thus every hypothesis of Appendix C is verified, with no restriction of its supremum to isolated or equilibrium states. Its conclusion supplies stopping-time tightness and unique identification of the entire projected path law in \(D([0,\infty),\mathcal P(\mathbb T))\) with the Skorokhod \(J_1\) topology. Its limit is the continuous-path law \(Q_{\mu_0}\), since the semigroup in (IV.4.1) is exactly the target semigroup characterized by the partition forms in Section 1 and the common-flow polynomial identity.

In particular, fix any integer \(k\ge1\), any parameter sequences satisfying \(N/L_N\to\rho\in(0,\infty)\) and \(Nd_N\to\Theta\in(0,\infty)\), and any deterministic initial configurations with at most \(k\) isolated occupied sites and \(\Phi_N(\eta_N^0)\to\mu_0\). These are among the deterministic initial projections allowed in the application above, so
\[
\operatorname{Law}_{\eta_N^0}(\mu_N(\cdot))
\Longrightarrow Q_{\mu_0}
\quad\text{in }D([0,\infty),\mathcal P(\mathbb T)).
\tag{IV.4.3}
\]
No step used a lower bound on an initial normalized stack mass, a lower bound on limiting separation, stationarity, absolute continuity, or a bound on \(k\) independent of the fixed sequence under consideration. Every auxiliary order was arbitrary but fixed, and the dense polynomial algebra supplied all continuous mass tests. Hence (IV.4.3) is the exact claim of Theorem 1, with all of its initial quantifiers, full-law scope, and time normalization. The proof method is microscopic path tightness and martingale identification, followed by the proved factorial lift and the path-transfer theorem in Appendix C; no Mosco convergence is used.

## A. Harmonic corrections and trace estimates

### A.1. Objects and hypotheses

Fix an arbitrary integer \(n\ge2\). Let \(E_n=\mathbb Z^n\), let \(e_i\) be the coordinate unit vectors, and set \(\eta_x(z)=|\{i:z_i=x\}|\). On functions on \(E_n\), define
\[
Rv(z)=\sum_{i=1}^n\sum_{\epsilon\in\{-1,1\}}[v(z+\epsilon e_i)-v(z)],
\]
\[
Iv(z)=\sum_{i=1}^n\sum_{\epsilon\in\{-1,1\}}\sum_{j\ne i}
\mathbf1_{\{z_j=z_i+\epsilon\}}[v(z+\epsilon e_i)-v(z)].
\]
Let \(S_n\) be the set of tuples with no adjacent distinct occupied sites. A stack is the set of labels at one occupied site. A full stack is a tuple with all labels at one site. Consider the continuous-time chain with generator \(I\). Let \(\tau\) be its first entrance in \(S_n\), including time zero. Define the absorption extension and killed potential by
\[
Pb(z)=\mathbb E_z b(X_\tau),\qquad
Uv(z)=\mathbb E_z\int_0^\tau v(X_s)\,ds.
\]
Here \(b\) is initially a bounded function on \(S_n\), and \(v\) is bounded on \(E_n\setminus S_n\); killed potentials are extended by zero on \(S_n\). Absorption extensions also apply to the functions of at most linear growth occurring below. Put
\[
Qb=(RPb)|_{S_n},\qquad Bb=(RURPb)|_{S_n}.
\]
In the second expression \(U\) uses the restriction of \(RPb\) to \(E_n\setminus S_n\). Let \(Y\) denote the \(Q\)-chain. Let \(K(z)\) be the number of occupied sites in \(z\in S_n\). Let \(C_n^{\mathrm{near}}\subset S_n\) consist of tuples with two occupied sites at distance two. Set
\[
c_n=\frac{n(n-1)}4,\qquad a_n=4n^2(n-1),\qquad d_n=\frac1{8nc_n}.
\]

A chamber-affine function means a continuous function \(f:\mathbb R^n\to\mathbb R\) whose restriction to each closed coordinate-order chamber is affine. This includes the chamber-linear functions and their additive constants. Let \(D\ge0\), and require
\[
|f(x)-f(y)|\le D\sum_{i=1}^n|x_i-y_i|\qquad(x,y\in\mathbb R^n).
\]
For its restriction to \(S_n\), define the canonical correction, whenever the integral is absolutely integrable, by
\[
\psi_f(z)=\mathbb E_z\int_0^\infty Qf(Y_s)\,ds,\qquad H_f(z)=f(z)+\psi_f(z).
\]

Write \(x|_B=(x_i)_{i\in B}\) for a coordinate subtuple. For every set partition \(\pi\) of \(\{1,\ldots,n\}\), choose distinct integers \(x_B\), \(B\in\pi\), and let \(z_i=x_B\) for \(i\in B\). For \(\varnothing\ne A\subsetneq B\), define \(v_{A,B}\in\mathbb R^n\) to equal minus one on \(A\), plus one on \(B\setminus A\), and zero off \(B\), and put
\[
\kappa_{A,B}=\frac{(|A|-1)!(|B|-|A|-1)!}{(|B|-1)!},\qquad
\partial_v f(z)=\lim_{t\downarrow0}\frac{f(z+tv)-f(z)}t.
\]
These directional derivatives exist for the specified functions. Sums over proper nonempty subsets of singleton blocks are zero. Every oriented subset is counted separately.

For \(0<d\le d_n\), let \(P_d,U_d,\tau_d\) be the analogous absorption extension, killed potential, and first entrance time for \(I+dR\), and define
\[
T_d=(RP_d)|_{S_n}.
\]
Let \(R^0\) denote \(R\) on zero extensions of bounded functions on \(E_n\setminus S_n\), restricted to this complement. Define \(I^0\) in the same way from \(I\). Operator norms below are supremum norms. Write \(T_0=Q\). For \(f_i(x)=x_i\), set \(H_i=H_{f_i}\), and define
\[
\Gamma_d^{ij}(z)=\sum_{y\in S_n,\ y\ne z}T_d(z,y)
[H_i(y)-H_i(z)][H_j(y)-H_j(z)]
\qquad(0\le d\le d_n).
\]

### A.2. Harmonic correction theorem

**Theorem A.1 (harmonic corrections and trace estimates).** Under the definitions and hypotheses of Section A.1, there exist finite constants \(C_n\ge1\) and, for every real \(p\ge1\), \(C_{n,p}\ge1\). They depend only on the displayed indices. All six assertions below hold with these constants at the same time. The constants are uniform in lattice positions, separations, partitions, and label subsets. They are also uniform in \(f\) subject to its stated bound \(D\).

1. **(A-H1)** Absorption is almost sure and \(\sup_{z\in E_n}\mathbb E_z\tau\le c_n\), \(\|U\|\le c_n\), \(\|P\|\le1\). The operator \(Q\) is a conservative jump generator of total rate at most \(2n\). Each nonzero off-diagonal \(Q\)-transition moves each label by at most two sites. Moreover,
   \[
   QK\le-\mathbf1_{C_n^{\mathrm{near}}},\qquad
   \sup_z\mathbb E_z\int_0^\infty\mathbf1_{C_n^{\mathrm{near}}}(Y_s)\,ds\le n-1,
   \]
   \[
   \sup_z\mathbb E_z\left(\int_0^\infty\mathbf1_{C_n^{\mathrm{near}}}(Y_s)\,ds\right)^2\le2(n-1)^2,
   \qquad
   \mathbb E_z\sup_{0\le s\le t}\max_i|Y_i(s)-z_i|^2\le C_n(t+1)
   \]
   for every \(z\in S_n\) and \(t\ge0\).

2. **(A-H2)** For every \(f,D\) above, the defining potential is absolutely integrable, and
   \[
   \|\psi_f\|_\infty\le a_nD,\qquad QH_f=0,\qquad
   \|RPH_f\|_\infty+\|BH_f\|_\infty\le C_nD.
   \]
   The maps \(f\mapsto\psi_f\) and \(f\mapsto H_f\) are linear. For any coordinate permutation followed by a common integer translation \(g:\mathbb R^n\to\mathbb R^n\), which preserves \(E_n\), \(H_{f\circ g}=H_f\circ g\) on \(S_n\). The correction vanishes on every full-stack tuple. It vanishes identically for every function \(f(x)=b+a\sum_i x_i\), and \(BH_f=0\) for those functions.

3. **(A-H3)** For every real \(R_*\ge16\), every partition and tuple defined above with \(|x_B-x_{B'}|\ge16R_*\) for different blocks, and every allowed \(f\),
   \[
   \left|BH_f(z)-\sum_{B\in\pi}\sum_{\varnothing\ne A\subsetneq B}
   \kappa_{A,B}\partial_{v_{A,B}}f(z)\right|\le C_nD R_*^{-1/8}.
   \]
   For a single full block the displayed expression inside absolute values is exactly zero, without a separation parameter. No exact formula at arbitrary finite separations is asserted.

4. **(A-H4)** The covariance series converge absolutely. They satisfy
   \[
   \sup_{z,i,j}|\Gamma_d^{ij}(z)|\le C_n,\qquad
   \sup_{z,i,j}|\Gamma_d^{ij}(z)-\Gamma_0^{ij}(z)|\le C_nd
   \quad(0<d\le d_n).
   \]
   At every separated-block tuple in (A-H3),
   \[
   |\Gamma_0^{ij}(z)-2\mathbf1_{\{z_i=z_j\}}|\le C_nR_*^{-1/2},\qquad
   |\Gamma_d^{ij}(z)-2\mathbf1_{\{z_i=z_j\}}|\le C_n(R_*^{-1/2}+d).
   \]

5. **(A-H5)** For every \(0<d\le d_n\), absorption for \(I+dR\) is almost sure,
   \[
   U_d=(\operatorname{Id}-dUR^0)^{-1}U,\qquad
   \|U_d\|\le2c_n,\qquad \|U_d-U\|\le8nc_n^2d.
   \]
   The inverse is its norm-convergent Neumann series. The chain with generator \(R+d^{-1}I\), observed in its time spent in \(S_n\), has conservative generator \(T_d\) and total rate at most \(2n\). For every bounded \(b:S_n\to\mathbb R\), the following identities are exact; the absorption difference \(P_db-Pb\) vanishes on \(S_n\):
   \[
   P_db-Pb=dU_dRPb,
   \]
   \[
   T_db=Qb+dBb+d^2(RU_dR^0URPb)|_{S_n}.
   \]
   The same identities hold with \(b=H_f\), whose absorption expectations are finite. Consequently
   \[
   \|T_dH_f-dBH_f\|_\infty\le C_nDd^2,\qquad
   \|T_dH_f\|_\infty\le C_nDd.
   \]

6. **(A-H6)** Fix any \(z\in S_n\) and any initiating independent step \(w=z+\epsilon e_i\). Run \(I+dR\) from \(w\) until its first entrance in \(S_n\). Let \(J\) count the independent \(dR\)-events at excursion times in \((0,\tau_d]\). At time zero, the state is \(w\), immediately after the initiating step. Thus an independent jump that causes entrance is included. If \(w\in S_n\), this excursion has duration zero and \(J=0\). Including the initiating step and writing \(X\) for this excursion path,
   \[
   \mathbb P(J\ge j)\le(2nc_nd)^j\quad(j\in\mathbb N_0),\qquad
   \max_i\sup_{0\le s\le\tau_d}|X_i(s)-z_i|\le n+J
   \quad\hbox{almost surely}.
   \]
   Uniformly over these choices and over \(0<d\le d_n\),
   \[
   \mathbb E(1+J)^p\le C_{n,p},\qquad
   \mathbb E[(1+J)^p\mathbf1_{\{J\ge1\}}]\le C_{n,p}d.
   \]
   For every initial tuple \(x\in E_n\), not only initiating-step states,
   \[
   \mathbb E_x\tau_d^p\le C_{n,p}.
   \]
   In particular, for every allowed \(f\), every \(z\in S_n\), and \(0\le d\le d_n\),
   \[
   \sum_{y\in S_n,\ y\ne z}T_d(z,y)|H_f(y)-H_f(z)|^p\le C_{n,p}D^p.
   \]

**One-label convention.** For \(n=1\), take \(S_1=\mathbb Z\), \(I=0\), \(P=P_d=\operatorname{Id}\), \(U=U_d=0\), \(Q=T_d=R\), \(B=0\), and \(d_1=1\). A chamber-affine \(f\) is affine on \(\mathbb R\), so \(H_f=f\). The near set is empty, the occupation integrals are zero, the separated split sum is empty, \(\Gamma_d^{11}=2\), and all expansion identities hold exactly. Excursions have \(\tau_d=J=0\); the initiating displacement is one. The displacement and trace jump moment bounds hold with finite constants depending only on their stated indices. This convention is part of the statement.

### A.3. Proof conventions

*Proof of Theorem A.1.* Until the last section, \(n\ge2\). A constant denoted \(C_n\) can increase a finite number of times. Each increase depends only on \(n\). Likewise \(C_{n,p}\) depends only on \(n,p\). These conventions produce simultaneous constants by taking the maximum of the finitely many constants required below. All chains below have bounded total rates for fixed \(n,d\). Construct them with exponential clocks. These chains have no explosion. Compensate their jump counts to obtain the stopped Dynkin identities and square-martingale identities below. For each unbounded stopping time, the proof supplies integrability or a bounded approximation.

### A.4. Pure interaction and the leading trace

Interaction jumps only into already occupied sites. The set of occupied sites therefore decreases. From any initial tuple, the chain stays on a finite set of at most \(n\) sites, and within each connected component of that initial set. Each component is an interval of length at most \(n\). In particular every label remains within distance \(n-1\) of its starting site. For
\[
V(z)=\sum_x\eta_x(z)^2,
\]
an interaction edge whose endpoint masses are \(a,b>0\) has two directed occupation jumps, each of rate \(ab\). Their changes of \(V\) are \(2(b-a+1)\) and \(2(a-b+1)\), whose sum is four. Consequently
\[
IV(z)=4\sum_{\{x,x+1\}}\eta_x(z)\eta_{x+1}(z)
\ge4\mathbf1_{S_n^c}(z).
\]
Here \(n\le V\le n^2\). Dynkin's identity stopped at \(t\wedge\tau\) yields \(4\mathbb E_z(t\wedge\tau)\le n^2-n\). Monotone convergence proves almost sure absorption and the bound \(\mathbb E_z\tau\le c_n\). It also proves \(\|U\|\le c_n\); the absorption expectation is a contraction on bounded functions. The chain stays in the finite initial set of sites. Thus \(Pb(z)\) is finite if \(b\) has at most linear growth.

Starting in \(S_n\), perform an independent jump at total attempt rate \(2n\) and then perform pure interaction until absorption. This defines a probability endpoint kernel for each attempt and the generator \(Q=RP|_{S_n}\). Self-return attempts are ignored in its off-diagonal rates. Thus \(Q\) is conservative and has total rate at most \(2n\). The independent step can create an occupied component on at most three consecutive sites. These are the source, its chosen neighbor, and possibly the site two units in that direction. Every other site is unaffected. This remains true if the source site is emptied. Absorption in that component moves every participating label by at most two sites. This proves the claimed jump bound.

A component on three consecutive sites absorbs on either one site or its two endpoints; a component on two sites absorbs on one site. Thus an independent attempt followed by absorption cannot increase the number \(K\) of stacks. Suppose specifically that occupied sites at zero and two have masses \(a,b\). The total rate of attempts into the intervening site is \(a+b\). After each such attempt the intervening population is one. For pure interaction, the population at each specified site is a martingale. Across each edge, its upward and downward changes have the same rate. This rate is the product of the endpoint masses. At absorption the intervening population is either zero or \(a+b\). Bounded optional stopping therefore gives probability \(1/(a+b)\) of a full stack there. The rate of this particular merger is one. Selecting any distance-two pair proves
\[
QK\le-\mathbf1_{C_n^{\mathrm{near}}}.
\]
Dynkin's identity for the bounded function \(K\), then monotone convergence, gives, for every \(z\in S_n\),
\[
\mathbb E_z A\le n-1,\qquad
A=\int_0^\infty\mathbf1_{C_n^{\mathrm{near}}}(Y_s)\,ds.
\]
Tonelli's theorem and the Markov property give
\[
\mathbb E_z A^2
=2\mathbb E_z\int_0^\infty \mathbf1_{C_n^{\mathrm{near}}}(Y_s)
\mathbb E_{Y_s}A\,ds
\le2(n-1)^2.
\]
First use finite integration rectangles. Their time diagonal has Lebesgue measure zero. Then use monotone convergence. It does not require integrability before this argument.

Outside \(C_n^{\mathrm{near}}\), each stack moves one site in each direction at rate one. A stack of size \(a\) initiates an attempt in a specified direction at rate \(a\). Its interaction chain on two sites ends at the new site with probability \(1/a\). The same population martingale gives this probability. No other stack can interact with it. Otherwise the endpoint is the original tuple. In particular \(Qz_i=0\) off the near set, \(|Qz_i|\le4n\) everywhere, and its compensated-coordinate martingale \(M_i\) has predictable quadratic-variation density at most \(8n\). Localization, followed by the bounded jump-rate estimates, gives \(\mathbb E M_i(t)^2\le8nt\) and the square maximal inequality gives \(\mathbb E\sup_{s\le t}|M_i(s)|^2\le32nt\). Hence
\[
Y_i(t)-z_i=M_i(t)+\int_0^t Qz_i(Y_s)\,ds,
\]
and the preceding bound on \(A^2\) proves
\[
\mathbb E_z\sup_{s\le t}\max_i|Y_i(s)-z_i|^2\le C_n(t+1).
\tag{A.1}
\]

### A.5. Construction and basic identities

Continuity of a chamber-affine function implies that its chamber formulas have the common intercept \(f(0)\). Fix an ordering of the stacks. Translate one stack by plus or minus one without passing another stack. The move stays in one closed coordinate-order chamber. The two centered affine increments cancel. By Section A.4 this applies to every \(Q\)-move outside the near set. Also a \(Q\)-move changes the sum distance by at most \(2n\). Thus
\[
|Qf|\le4n^2D\mathbf1_{C_n^{\mathrm{near}}}.
\tag{A.2}
\]
Section A.4 now gives absolute integrability of the defining potential and
\[
\|\psi_f\|_\infty\le4n^2D(n-1)=a_nD.
\tag{A.3}
\]
The Markov property gives, for every \(t\ge0\),
\[
\psi_f=\int_0^t e^{sQ}Qf\,ds+e^{tQ}\psi_f.
\]
The operator \(Q\) has norm at most \(4n\) on bounded functions. Thus its exponential is differentiable in this norm. Differentiating the last identity at zero yields \(Q\psi_f=-Qf\). The formula defining \(Qf\) is a finite sum of finite absorption expectations, even if \(f\) is unbounded. Thus \(QH_f=0\) at every point. This equality does not assert a semigroup domain for unbounded functions.

Linearity follows from the absolutely integrable defining integral. The independent and interaction clocks, their absorption kernels, the near set, and \(Q\) commute with coordinate permutations and common integer translations. Applying such a map to the defining integral proves the claimed covariance of \(H\). From a full stack, the \(Q\)-chain remains a full stack. The restriction of \(f\) to the common diagonal is affine. Hence \(Qf=0\) and \(\psi_f=0\) there.

For \(g(x)=\sum_i x_i\), one has \(Rg=0\). The two directed interaction occupation jumps on each edge have opposite changes of \(g\) and equal rates, so \(Ig=0\). Its pure-interaction path is bounded relative to its initial value by the finite-site argument. Optional stopping gives \(Pg=g\). Hence \(Qg=RPg=0\), \(\psi_g=0\), and \(Bg=RURPg=0\). Linearity includes additive constants and every multiple of \(g\).

For later use, an absorption endpoint from any \(x\in E_n\) has sum distance at most \(n(n-1)\) from \(x\). Therefore, for neighboring tuples \(x,x+\epsilon e_i\),
\[
|PH_f(x+\epsilon e_i)-PH_f(x)|
\le D[2n(n-1)+1]+2a_nD.
\]
Writing
\[
A_n=2n[2n(n-1)+1+2a_n],
\]
we obtain
\[
\|RPH_f\|_\infty\le A_nD,\qquad
\|BH_f\|_\infty\le4nc_nA_nD.
\tag{A.4}
\]
This proves (A-H2).

### A.6. Perturbed excursions and the exact expansion

Fix \(0<d\le d_n\) and put \(q=2nc_nd\le1/4\). Realize \(I+dR\) by pure-interaction clocks and an independent rate-\(2nd\) clock with uniformly selected label and direction. From any state, the probability that this independent clock rings before pure-interaction absorption is
\[
\mathbb E(1-e^{-2nd\tau})\le2nd\mathbb E\tau\le q.
\tag{A.5}
\]
Count each such event, including an event that itself enters \(S_n\), and restart if its new state has not already entered \(S_n\). Thus \(J\) counts independent events on the interval \((0,\tau_d]\) in the excursion clock. It includes an independent jump that causes entrance. If the starting tuple is in \(S_n\), then \(J=0\). The strong Markov property and (A.5) prove \(\mathbb P(J\ge j)\le q^j\), both for excursions after an initiating step and for the corresponding count from an arbitrary starting state. Each interval between restarts has expected length at most \(c_n\). Summing its expectation on the event that it is reached gives
\[
\sup_x\mathbb E_x\tau_d\le\frac{c_n}{1-q}\le2c_n.
\tag{A.6}
\]
In particular absorption is almost sure. Applying Markov's inequality conditionally at deterministic times \(4c_n,8c_n,\ldots\) gives
\[
\sup_x\mathbb P_x(\tau_d>4c_n k)\le2^{-k}\qquad(k\in\mathbb N_0).
\]
Integrating this tail against \(pt^{p-1}\) proves \(\sup_x\mathbb E_x\tau_d^p\le C_{n,p}\) for every real \(p\ge1\).

There is a useful pathwise displacement bound. Take all initially occupied sites and all sites newly occupied by independent events, including the initiating event when present. Interaction never adds to this set. With an initiating event and \(J\) further independent events its cardinality is at most \(n+1+J\). A label's nearest-neighbor trajectory stays in the connected component of this set containing its initial site. On the line every such component is an interval of diameter at most \(n+J\). This proves the asserted pathwise excursion bound, even if previously separate occupied components become joined. Without an initiating event the same argument gives diameter at most \(n-1+J\).

For every real \(p\ge1\), the geometric tail gives
\[
\mathbb E[(1+J)^p\mathbf1_{\{J\ge1\}}]
\le\sum_{j=1}^\infty(1+j)^p q^j
\le q\sum_{j=1}^\infty(1+j)^p4^{1-j}\le C_{n,p}d.
\tag{A.7}
\]
Adding the event \(J=0\) proves the other claimed moment bound.

On bounded functions on the complement of \(S_n\), the potential \(U_d\) in (A.6) solves the killed Dirichlet equation
\[
-(I^0+dR^0)U_dv=v.
\]
Condition on the first holding time and jump to obtain this equation. Bounded total rates and (A.6) justify this step. Let \(w\) be bounded with zero boundary values. The stopped Dynkin identity for pure interaction gives \(U(-I^0w)=w\). The terminal boundary value is zero. Bounded convergence applies at absorption. Apply this identity to \(w=U_dv\) to obtain
\[
U_dv=Uv+dUR^0U_dv.
\]
Since \(\|R^0\|\le4n\) and \(4ndc_n\le1/2\), this proves the norm-convergent Neumann identity and bounds
\[
U_d=(\operatorname{Id}-dUR^0)^{-1}U,
\quad \|U_d\|\le2c_n,
\quad \|U_d-U\|\le8nc_n^2d.
\tag{A.8}
\]
The same series gives the exact resolvent identity
\[
U_d-U=dU_dR^0U.
\tag{A.9}
\]

For bounded boundary data \(b\), its pure absorption extension satisfies \(IPb=0\) off \(S_n\). Stopped Dynkin for \(Pb\) under \(I+dR\), with (A.6) and bounded convergence, yields
\[
P_db-Pb=dU_dRPb.
\tag{A.10}
\]
For \(b=H_f\), (A.4) bounds its residual, and the neighboring-increment bound preceding (A.4) bounds all increments of \(PH_f\). The same stopped calculation applies as follows. From a fixed initial tuple, the maximum excursion displacement is at most \(n-1+J\). Its moments are finite by (A.7). The neighboring-increment bound bounds \(|PH_f(X_s)-PH_f(X_0)|\) by a constant times this sum distance. Thus the stopped terminal values are uniformly integrable. The integral of its bounded residual is dominated in expectation by (A.6). First apply Dynkin at bounded times and with a finite spatial stopping region. Then remove both stops. This proves (A.10) for \(H_f\). In particular its perturbed absorption expectation is finite.

Consider the chain with generator \(R+d^{-1}I\). In \(S_n\), its clock initiates independent steps at total rate \(2n\). Its excursion absorption distribution is \(P_d\): multiplication of the excursion generator by \(d\) gives \(I+dR\). Consequently its trace generator is \(T_d=RP_d|_{S_n}\), with off-diagonal formula
\[
T_d(z,y)=\sum_{i,\epsilon}P_d(z+\epsilon e_i,y)\qquad(y\ne z).
\tag{A.11}
\]
It is conservative and has total rate at most \(2n\). The time change is defined for all trace times. At repeated visits to \(S_n\), the independent attempt holding times are independent exponential variables of rate \(2n\). Their infinite sum is almost surely infinite. Excursions are almost surely finite by (A.6). Ignoring self-return attempts changes neither the generator nor this conclusion.

Apply \(R\) to (A.10), restrict to \(S_n\), and use (A.9). For bounded \(b\), and also for \(H_f\), this gives the exact expansion
\[
T_db=Qb+dBb+d^2(RU_dR^0URPb)|_{S_n}.
\tag{A.12}
\]
For bounded \(b\) the remainder operator has norm at most \(128n^3c_n^2d^2\). For \(H_f\), use (A.4) in place of the bound \(\|RPb\|\le4n\|b\|\) to obtain a remainder at most \(32n^2c_n^2A_nDd^2\). Since \(QH_f=0\) and \(BH_f\) is bounded by (A.4), this proves both corrector estimates for \(T_d\).

Formula (A.11), the pathwise excursion bound, and (A.3) also give every trace jump moment in the statement, because an excursion endpoint \(y\) satisfies
\[
|H_f(y)-H_f(z)|\le Dn(n+J)+2a_nD.
\tag{A.13}
\]
There are \(2n\) initiating choices. For \(d=0\) the identical argument has \(J=0\).

### A.7. Full-block action and labelled factorial coefficients

This section applies the preceding construction with any order \(m\ge2\). Let \(f\) have that order. Suppose two chambers share a facet \(x_i=x_j\). Their gradients differ by a multiple of \(e_i-e_j\). Their affine difference is zero on that hyperplane. Adjacent exchanges connect all coordinate orders, so the sum of gradient coordinates is a common number \(\ell\). It follows that
\[
f(x+t\mathbf1)=f(x)+\ell t.
\]
Subtract \(f(0)+(\ell/m)\sum_i x_i\). By Section A.5 this does not change \(\psi_f\) or \(BH_f\). The reduced function is translation invariant and vanishes on full stacks. The correction and \(H_f\) are translation invariant as well; for the correction this follows directly from the invariance of \(Qf\). All calculations until restoration of the affine term refer to this reduced function.

Index an oriented two-stack tuple by its nonempty proper left subset \(A\subset\{1,\ldots,m\}\). Write \(H(A,r)\) for its corrected value with left site zero and right site \(r\ge2\). Set
\[
c_A=f(0\mathbf1_A+1\mathbf1_{A^c}),\qquad a_A=H(A,2),\qquad
\kappa_A=\frac{(|A|-1)!(m-|A|-1)!}{(m-1)!}.
\]
For \(r\ge3\), the two stack centers move independently at rate one in each direction. Their gap therefore moves in each direction at rate two, without changing the label subset. Translation invariance and \(QH=0\) give zero second difference in \(r\). A sequence with zero second difference for every \(r\ge3\) is affine on \(r\ge2\). Subtract its first two values and use induction. Since \(|H(A,r)-rc_A|\) is bounded by (A.3), its slope is \(c_A\). Thus
\[
H(A,r)=(r-2)c_A+a_A\qquad(r\ge2).
\tag{A.14}
\]

Start with left subset \(A\) at zero and its complement at two. Consider inward independent attempts followed by pure-interaction absorption at the same two sites with left subset \(A'\). Define \(K(A,A')\) as their total rate. Include self-return outcomes in \(K(A,A)\). The total inward attempt rate is \(m\). The center-full-stack outcome has rate one by Section A.4. Every other outcome is either a full stack at an endpoint or a two-stack outcome counted in \(K\). Hence \(K\) is nonnegative and every row sum is at most \(m-1\). Put \(M=m\operatorname{Id}-K\). It is invertible, as is seen from the convergent series for \((\operatorname{Id}-K/m)^{-1}\). The two outward effective translations at gap two contribute \(2c_A\) to \(QH\), and full-stack outcomes have corrected value zero. The remaining inward contribution is \((Ka)_A-ma_A\). Therefore
\[
Ma=2c.
\tag{A.15}
\]

We now prove the weighted symmetry used to evaluate this expression. This does not follow from label exchangeability alone. On a finite cycle of length \(L>6m+10\), the labelled generator \(I+dR\) has positive weights
\[
\omega_d(z)=\prod_{x:\eta_x(z)>0}\prod_{r=0}^{\eta_x(z)-1}(d+r).
\tag{A.16}
\]
Move a specified label from a site of mass \(a\) to a neighboring site of mass \(b\ge0\). The forward rate is \(d+b\). The reverse rate is \(d+a-1\). The ratio of destination weight to source weight is \((d+b)/(d+a-1)\). Thus every off-diagonal detailed-balance identity holds.

Eliminating the complement of \(S_m\) preserves this weighted symmetry. Here is the finite-matrix verification. Write the generator in blocks for \(S_m\) and its complement \(F\), and let \(\Omega_S,\Omega_F\) be the diagonal matrices of its weights. The killed inverse \((-L_{FF})^{-1}\) exists by absorption, and weighted symmetry of \(L\) implies symmetry of \(\Omega_F(-L_{FF})^{-1}\). The trace matrix is
\[
L_{SS}+L_{SF}(-L_{FF})^{-1}L_{FS}.
\]
Using \(\Omega_SL_{SF}=L_{FS}^{\mathsf T}\Omega_F\) shows that its product on the left by \(\Omega_S\) is symmetric. Dividing this trace matrix by \(d\) gives \(T_d\). Therefore \(\omega_d(z)T_d(z,y)=\omega_d(y)T_d(y,z)\).

The preceding arguments also apply to the cycle. Pure interaction cannot add occupied sites. Since \(m<L\), its initial occupied components are paths. The calculation for \(V\) is unchanged. The estimates (A.5)–(A.12) apply with the same bounds. In particular, the expansion converges in the norm for bounded operators. For the tuples under consideration, its coefficients \(Q\) and \(B\) equal the line coefficients. The operators \(P,U\) use only initially occupied components. A coefficient of \(Q\) uses at most one independent event. A coefficient of \(B\) uses at most two. Start with the sites zero and two, or the single site zero. Add at most two neighboring sites. The affected sites lie in the resulting fixed interval. No wrap around can occur for the chosen \(L\). Thus the following finite-cycle coefficient comparisons establish identities for the line.

Between two-stack tuples at sites zero and two, compare the coefficient of \(d^2\) in detailed balance. The leading weight is \(d^2(|A|-1)!(m-|A|-1)!\), and the leading trace operator is \(Q\). Off-diagonal transitions keeping these sites and changing the left subset are exactly those in \(K\). Thus
\[
\kappa_AK(A,A')=\kappa_{A'}K(A',A).
\tag{A.17}
\]
The diagonal case is automatic. Consequently \(M\) is symmetric for the weights \(\kappa_A\).

Let \(o\) be the full stack at zero and let \(s\) be any two-stack tuple. Since \(Q\) never increases the stack count, \(Q(o,s)=0\). For the two-stack tuples of interest its weight divided by \(\omega_d(o)\) equals \(d\kappa_A+O(d^2)\). Compare the coefficient of \(d^2\) in \(\omega_d(o)T_d(o,s)=\omega_d(s)T_d(s,o)\), using (A.12). This proves
\[
B(o,s)=\kappa_AQ(s,o).
\tag{A.18}
\]
The row of \(B\) at \(o\) can have no split destinations except two-stack tuples at \((-1,1)\), \((0,2)\), or \((-2,0)\). Indeed its first independent event creates two neighboring occupied sites; interaction stays within them; one more independent event can adjoin only one neighboring site. A stable subset of the resulting three consecutive sites is a full stack or the two endpoints. Terms arising from the negative parts of either \(R\) yield destinations with fewer additions and obey the same assertion.

For a fixed oriented subset \(A\), the reverse merger rates from these three placements to the full stack at zero sum to \((M\mathbf1)_A\). To see this, start instead with the tuple \(A\) at zero and its complement at two. The three full-stack inward outcomes are at zero, one, and two; their total rate is \(m-\sum_{A'}K(A,A')\). Common translations identify their individual rates with those from the placements \((0,2)\), \((-1,1)\), and \((-2,0)\), respectively, to zero. Their corrected split values are all \(a_A\) by translation invariance and (A.14). Every full-stack value is zero. Therefore (A.18), weighted symmetry (A.17), and (A.15) give
\[
BH_f(o)=\sum_A\kappa_A(M\mathbf1)_Aa_A
=\sum_A\kappa_A(Ma)_A
=2\sum_A\kappa_Ac_A.
\tag{A.19}
\]
For the reduced function, the derivative in direction \(v_{A,\{1,\ldots,m\}}\) is \(2c_A\). To see this, translate that vector by \(\mathbf1\). Then use homogeneity on its chamber. On restoring the subtracted affine term, its derivative contributions cancel in complementary pairs, since \(\kappa_A=\kappa_{A^c}\) and the vectors are opposite. Its \(B\)-action is zero by Section A.5. This proves the exact full-block formula with every oriented subset counted separately. In particular there is no additional factor of two or combinatorial exchange factor.

### A.8. Quantitative localization

Fix a partition \(\pi\), a separated tuple \(z\) as in Sections A.1–A.2, and \(R_*\ge16\). Write \(R_*=r_0\) in this section to distinguish it from the independent generator \(R\). Order the blocks by their sites \(x_B\). Consider real tuples in which every coordinate belonging to an earlier block is less than every coordinate belonging to a later block.

On this region there are globally defined chamber-affine functions \(f_B\) on \(\mathbb R^B\), each with sum-norm Lipschitz bound \(D\), such that
\[
f(x)=f(0)+\sum_{B\in\pi}f_B(x|_B).
\tag{A.20}
\]
Construct these functions as follows. For an internal ordering of a block, take the coordinates of a chamber gradient of \(f\) in that block, using the fixed external block order. These coordinates do not depend on the orders inside other blocks. An adjacent exchange in another block changes the full gradient only by a multiple of the difference of two unit vectors from that other block. Define \(f_B\) on each of its chambers by the corresponding gradient dotted with its coordinates, with zero intercept. Adjacent formulas agree on their common face by the same gradient-difference property. Formulas at any further intersection agree by successively exchanging equal coordinates. Thus they define a continuous global function. All its gradient coordinates have magnitude at most \(D\). Integrate along a line segment through its finite set of chambers to obtain the Lipschitz bound. Finally, summing these chamber formulas gives (A.20) in each permitted chamber, and continuity gives it on the faces.

Evaluate the separate canonical corrections from Sections A.4–A.5 on the subtuples and define on \(S_n\)
\[
W=f+\sum_{B\in\pi}\psi_{f_B},\qquad \delta=H_f-W.
\]
For singleton blocks use the convention proved in Section A.11 below; its correction is zero and its affine generator action is zero. By (A.3),
\[
\|\delta\|_\infty\le C_nD.
\tag{A.21}
\]
When all coordinates of block \(B\) stay within \(4r_0\) of \(x_B\), the blocks remain in their prescribed order and have large intervening gaps. For states whose coordinates are within \(2r_0\) of their respective \(x_B\), all \(Q\)-endpoints remain in that larger region, since individual jumps are at most two. The triggered interaction component lies in one block. On such states \(Q\) acts on sums of block functions as the sum of the isolated block \(Q\)-operators. Equation (A.20) and the harmonicity of each \(H_{f_B}\) therefore imply \(QW=0\), and hence \(Q\delta=0\), throughout the smaller region. This gives bounded stopped harmonicity up to exit from any still smaller region used below.

First consider coarse tuples with one full stack per block. There \(Q\) is the generator of independent walks of the block centers, each jumping left and right at rate one. If \(z'\) is another coarse tuple shifting every center by at most \(a\le r_0/2\), then
\[
|\delta(z')-\delta(z)|
\le C_nD\left(\frac{a+1}{\sqrt{r_0}}+\frac1{r_0}\right).
\tag{A.22}
\]
To prove this, couple corresponding center walks independently until meeting and synchronously thereafter, independently for different blocks. Before meeting their signed difference is a nearest-neighbor symmetric walk with rate two in each direction. Its probability of not having hit zero by time \(t\), from distance \(a\), is at most \(C(a+1)/\sqrt t\). Indeed, when \(a\le\sqrt t\), stop this difference at zero or the integer \(b=\lceil\sqrt t\rceil+a+1\). Its chance to hit \(b\) before zero is \(a/b\), by the stopped coordinate martingale. Its expected stopped time is at most \(ab/4\), since the generator of \(x(b-x)\) is minus four on the interior. Markov's inequality bounds survival without either exit by \(ab/(4t)\). These two bounds give the assertion; when \(a>\sqrt t\), enlarging the constant makes it at least one. The finite-interval stops have finite expectation. For example, each fixed block of sufficiently many jumps has a fixed positive chance of exit. This justifies optional stopping.

Run the coupling to time \(t=r_0\), stopping each vector of centers on leaving the box with centers within \(r_0\) of their original \(x_B\). Its starting displacement is at most \(r_0/2\). The square maximal inequality for each centered walk, whose variance rate is two, bounds its exit probability by \(C/r_0\). Stopped harmonicity of \(\delta\) applies because exit endpoints still lie within \(2r_0\). On the event that neither vector exits and all corresponding walks meet by time \(r_0\), their terminal tuples are identical. Compare their bounded stopped expectations, use (A.21), and sum the meeting and exit failure bounds over at most \(n\) blocks. This proves (A.22).

We also need a quantitative internal merger estimate. For any two-substack isolated block, starting at a gap bounded by two, let \(\sigma\) be its first full-stack time. More generally the following proof gives a bound with a constant depending on any fixed upper bound for the starting gap. At gaps at least three the gap has rates two in each direction. At gap two the total outward rate is two, and the full-merger rate is at least one by Section A.4. Other transitions only redistribute the left label subset. One may split off rate-one killing at gap two and ignore all additional merger killing. The remaining gap motion is the walk with these interior rates, outward rate two at its boundary two, and killing rate one there. This construction is valid through changes of label subset because the specified rates are independent of that subset; additional killing can only shorten the lifetime. Let \(\zeta\) be the lifetime of this latter walk.

For \(s>0\), let \(q_s\in(0,1)\) be the smaller root of \(2(q_s+q_s^{-1}-2)=s\). Direct substitution into the first-step equations gives
\[
\mathbb E_r e^{-s\zeta}=\frac{q_s^{r-2}}{s+3-2q_s},\qquad
q_s=1+\frac{s}{4}-\sqrt{\frac{s}{2}+\frac{s^2}{16}}.
\tag{A.23}
\]
For completeness, the interior equation is \((s+4)u_r=2u_{r-1}+2u_{r+1}\), and the boundary equation is \((s+3)u_2=1+2u_3\). The displayed bounded solution satisfies both. For uniqueness, stop at time \(t\), a finite spatial boundary, or killing. For a difference of two bounded solutions, the stopped discounted value has constant expectation. Use bounded rates to remove the spatial boundary. Then let \(t\to\infty\). The factor \(e^{-st}\) removes the remaining value. This also identifies the displayed solution with the stated expectation, with \(e^{-s\infty}=0\).

For bounded \(r\) and \(0<s\le1\), (A.23) gives \(1-\mathbb E_r e^{-s\zeta}\le C_n\sqrt s\): use \(1-q_s\le C\sqrt s\), \(1-q_s^{r-2}\le(r-2)(1-q_s)\), and \(s+3-2q_s=1+s+2(1-q_s)\ge1\). The limit as \(s\downarrow0\) also proves almost sure finite killing. Since
\[
\mathbf1_{\{\zeta>t\}}\le\frac{1-e^{-\zeta/t}}{1-e^{-1}}\qquad(t>0),
\]
we obtain, also for \(0\le t<1\) by enlarging the constant,
\[
\mathbb P(\sigma>t)\le\mathbb P(\zeta>t)\le C_n(1+t)^{-1/2}.
\tag{A.24}
\]

Let \(s\in S_n\) have every label within two sites of its position in \(z\). Each block is a full stack, with at most one exception. The exceptional block has two substacks at distance two. Run its \(Q\)-chain until the first of internal merger, time \(t=r_0^{1/2}\), and displacement at least \(r=r_0^{3/8}\) from \(s\). Treat a simultaneous merger and displacement exit as a failure. Before displacement exit the blocks remain separated, so the internal motion agrees with the isolated motion in (A.24). The probability of displacement exit by time \(t\) is at most \(C_n(t+1)/r^2\le C_nr_0^{-1/4}\), by (A.1). The probability of failure to merge by time \(t\) without earlier displacement exit is at most the isolated survival bound \(C_nr_0^{-1/4}\). If no block is split, take the merger time to be zero.

On success, the endpoint is coarse. Its center displacement from \(z\) is at most \(r+2\). For \(r_0\ge16\), this is at most \(r_0/2\). At every stopped endpoint, the coordinates are within \(r+4<2r_0\) of the reference sites. Thus bounded stopped harmonicity of \(\delta\) applies. Compare its expectation from \(s\) to \(\delta(z)\), use (A.22) on successful endpoints and (A.21) on failure. This proves
\[
|\delta(s)-\delta(z)|\le C_nD r_0^{-1/8}.
\tag{A.25}
\]
Indeed \((r+3)/\sqrt{r_0}\le C r_0^{-1/8}\), and the failure term has the smaller order \(r_0^{-1/4}\). Thus all stopping regions and the constants here are uniform in the actual block positions and sizes.

The row of \(B\) at the reference coarse state \(z\) has finite support only among states \(s\) just described. Check this directly in \(RURP\). The first independent event creates a neighboring pair in one block or ends in \(S_n\). In the second case, its \(U\)-term is zero. During the pure-interaction integral no new site is occupied. In the inner \(R\), a second event in the same block can create at most three consecutive sites. Absorption produces a full stack or two substacks at distance two. A second event in another block leaves two isolated two-site components, both of which absorb to full stacks. Negative terms omit one of these events and satisfy the same support assertion. In all cases each label moves at most two sites from \(z\). For bounded data,
\[
\|B\|\le\|R\|\|U\|\|R\|\|P\|\le16n^2c_n,
\]
and \(B\mathbf1=0\). This also bounds the total variation of each finite signed row. Equation (A.25) therefore gives \(|B\delta(z)|\le C_nD r_0^{-1/8}\).

We next evaluate \(BW(z)\). On every configuration visited in the above row calculation, (A.20) and independent absorption in the separated groups give
\[
P_nW=f(0)+\sum_{B\in\pi}P_BH_{f_B}.
\]
Here the subscripts specify the particle set, not a new operator definition. After the first independent event only its own block can be transient. Applying the inner \(R\) to this sum gives zero from each other block, since at its full stack \(R_BP_BH_{f_B}=Q_BH_{f_B}=0\). Integrating to absorption therefore gives precisely the killed potential of the affected block applied to its residual. Summing the initiating events proves
\[
BW(z)=\sum_{B\in\pi}B_BH_{f_B}(x_B\mathbf1_B).
\]
The single-block formula (A.19), including its restoration of affine terms, evaluates each summand. By (A.20), its directional derivatives are the corresponding derivatives of \(f\) at \(z\). Combining this identity with the bound for \(B\delta\) proves (A-H3) for every parameter in its statement. The one-block equality was already proved in Section A.7.

### A.9. Coordinate covariances

Fix the coordinate test \(f_i(x)=x_i\). At a coarse state in the previous section all local block corrections vanish. Thus \(\delta\) equals \(\psi_{f_i}\) at every coarse state in the stopping box. Apply (A.22) with \(a=1\) to obtain, for every block \(B\) and \(\epsilon\in\{-1,1\}\),
\[
H_i(z+\epsilon\mathbf1_B)-H_i(z)
=\epsilon\mathbf1_{\{i\in B\}}+O(C_n r_0^{-1/2}).
\tag{A.26}
\]
At this separated state these are all off-diagonal \(Q\)-transitions, each at rate one. Multiplying the two increments and summing gives
\[
\left|\Gamma_0^{ij}(z)-2\mathbf1_{\{z_i=z_j\}}\right|\le C_nr_0^{-1/2}.
\tag{A.27}
\]
The error from multiplying the two errors is bounded by a constant times \(r_0^{-1}\) and is included in the displayed bound. At an arbitrary state, every coordinate increment of \(H_i\) is at most \(2+2a_n\) along a \(Q\)-jump, by (A.3) and Section A.4. The total rate is at most \(2n\), so \(\Gamma_0\) is bounded everywhere.

Couple each perturbed excursion after a fixed initiating step to a pure-interaction excursion until the first additional independent event. Sample the entire pure-interaction chain independently of the extra independent clocks. Continue this sampled pure path if an extra event occurs. The sampled pure chain has the pure-excursion marginal law. If no extra event occurs before absorption, the two endpoints coincide and \(J=0\). On the complementary event \(J\ge1\), the pure endpoint is within \(n\) of the initial tuple coordinatewise, and the perturbed endpoint is within \(n+J\). Their corrected coordinate increments are therefore bounded by \(C_n\) and \(C_n(1+J)\), respectively. It follows that the absolute difference of the products of increments for coordinates \(i,j\) is at most \(C_n[(1+J)^2+1]\mathbf1_{\{J\ge1\}}\). Equation (A.7), summed over the \(2n\) initiating steps in (A.11), gives
\[
\sup_{z,i,j}|\Gamma_d^{ij}(z)-\Gamma_0^{ij}(z)|\le C_nd.
\tag{A.28}
\]
Absolute convergence follows already from the second-moment instance of (A.13), using \(|ab|\le(a^2+b^2)/2\). Combining (A.27), (A.28), and the global bound proves every covariance assertion. Finally, the split sum for a coordinate test is zero. Complementary subsets have equal factorial coefficients and opposite vectors. Thus the split sum in (A-H3) is zero for a coordinate test.

### A.10. Uniformity of the conclusions

Sections A.4–A.5 apply to each fixed integer \(n\ge2\). Section A.6 applies to every \(0<d\le d_n\) and every real \(p\ge1\). It proves the convergent trace expansion before the coefficient comparison in Section A.7. Section A.8 applies to every partition and every \(R_*\ge16\). Its constants do not depend on the block sites or block sizes. Section A.9 proves the covariance bounds at every state and their estimates at separated states. The cycle matrices in Section A.7 prove only the local coefficient identities on the line.

### A.11. The one-label case

For \(n=1\), every site is already in \(S_1\), so both absorption times are zero and both potentials vanish. There are no interaction jumps. Therefore \(P=P_d=\operatorname{Id}\), \(Q=T_d=R\), and \(B=0\), for every \(d>0\), in particular \(0<d\le d_1=1\). A chamber-affine function is simply \(f(x)=ax+b\), with \(|a|\le D\), and \(Rf=0\). Its canonical correction is zero. The coordinate has jumps plus and minus one at rate one. Its covariance density is two. Its square maximal displacement is at most \(8t\). Its trace jump moment is \(2|a|^p\le2D^p\). The near set and every split sum are empty. An initiating step has displacement one and is already in \(S_1\), with \(J=\tau_d=0\). These facts prove the full convention in the statement and the singleton-block facts used in Section A.8.

## B. Positive-layer occupation

For every integer \(L\ge3\), let \(\mathbb T_L=\mathbb Z/(L\mathbb Z)\). For \(x,y\in\mathbb T_L\), define
\[
\operatorname{dist}_L(x,y)=\min\{r,L-r\},
\]
where \(r\in\{0,\ldots,L-1\}\) represents \(y-x\) modulo \(L\).

For every integer \(n\ge2\), the labelled state space is \(\mathbb T_L^n\). If \(z=(z_1,\ldots,z_n)\), then \(z+\varepsilon e_i\) means adding \(\varepsilon\in\{-1,1\}\) to coordinate \(i\), modulo \(L\), leaving all other coordinates unchanged. On real functions \(F:\mathbb T_L^n\to\mathbb R\), define
\[
R_nF(z)=\sum_{i=1}^n\sum_{\varepsilon\in\{-1,1\}}
[F(z+\varepsilon e_i)-F(z)]
\]
and
\[
I_nF(z)=\sum_{i=1}^n\sum_{\varepsilon\in\{-1,1\}}
\sum_{\substack{j=1\\j\ne i}}^n
\mathbf 1_{\{z_j=z_i+\varepsilon\}}
[F(z+\varepsilon e_i)-F(z)].
\]
For every \(q>0\) and \(d>0\), let \(Z=(Z_t)_{t\ge0}\) be the continuous-time Markov chain with generator
\[
G_n=q(R_n+d^{-1}I_n).
\]
Thus each label has independent rate \(q\) to each of its two neighboring sites, plus rate \(q/d\) for each other label occupying the destination site. Both directions occur once; for \(L=3\) they are distinct. The parameters \(n\) and \(q\) are independent, with no scaling relation imposed.

For every integer \(k\) with \(1\le k<L/2\), define the positive-layer pair count
\[
B_k(z)=\sum_{1\le i<j\le n}
\mathbf 1_{\{0<\operatorname{dist}_L(z_i,z_j)\le k\}}.
\]
Pairs at equal sites are excluded.

**Proposition B.1 (conditional occupation estimate).** For every deterministic initial state \(z\in\mathbb T_L^n\), and also for every initial distribution on that state space, equip the chain with its completed right-continuous natural filtration \((\mathcal F_t)_{t\ge0}\). For every deterministic real number \(\delta\ge0\) and every pair of bounded nonnegative stopping times \(\tau,\sigma\) satisfying
\[
\tau\le\sigma\le\tau+\delta\quad\text{almost surely},
\]
the following conditional inequality holds:
\[
\mathbb E\left[\int_\tau^\sigma B_k(Z_s)\,ds
\;\middle|\;\mathcal F_\tau\right]
\le
\binom n2\left[
\frac{2k\delta}{L+1/d}+\frac{Lk}{q}
\right]
\quad\text{almost surely}.
\]

The bound has exactly the displayed constants and is uniform over all the stated parameters, initial states or distributions, and stopping times. No equilibrium or separated-start assumption is imposed. No fixed pair of physical labels is assumed to have autonomous dynamics.

*Proof.* Fix arbitrary parameters and stopping times from the statement. Use the notation \(L,n,q,d,k,\delta,G_n,R_n,I_n,B_k\) and \(\operatorname{dist}_L\). No limit or relationship between \(q\) and \(n\) will be used.

### B.1. The two-particle difference and the three-site case

First set the particle number equal to two, retaining the same \(L,q,d\), and let
\[
r=z_2-z_1\in\mathbb T_L.
\]
Two independent moves increase \(r\) by one and two decrease it by one, each move having rate \(q\). If \(r=1\), either label can jump onto the other label, with additional rate \(q/d\), and both such jumps send \(r\) to zero. If \(r=-1\), the same description holds with the direction reversed. There is no interaction jump at equality.

Consequently, for a function \(v:\mathbb T_L\to\mathbb R\), the difference generator is
\[
\begin{aligned}
\mathcal H v(r)={}&
2q[v(r+1)+v(r-1)-2v(r)]\\
&+\frac{2q}{d}\mathbf 1_{\{r=1\}}[v(0)-v(1)]
+\frac{2q}{d}\mathbf 1_{\{r=-1\}}[v(0)-v(-1)].
\end{aligned}
\tag{B.1.1}
\]
For \(L\ge3\), the residues \(1\) and \(-1\) are distinct. In particular, when \(L=3\), a state \(r=1\) has rate \(2q(1+1/d)\) to zero and rate \(2q\) to \(r=2\), and the analogous statement holds at \(r=2=-1\). The transition between \(1\) and \(2\) is not an extra collision transition. At zero the rates to \(1\) and \(2\) are each \(2q\).

Use representatives \(r=0,\ldots,L-1\), with all subscripts interpreted modulo \(L\). Define positive vertex weights and positive edge coefficients by
\[
m_r=
\begin{cases}
1+1/d,&r=0,\\
1,&r\ne0,
\end{cases}
\qquad
a_r=
\begin{cases}
1+1/d,&r=0\text{ or }r=L-1,\\
1,&\text{otherwise}.
\end{cases}
\tag{B.1.2}
\]
The coefficient \(a_r\) belongs to the edge joining \(r\) to \(r+1\). Comparing each term with (B.1.1) proves the identity
\[
\mathcal H v(r)
=\frac{2q}{m_r}
\left[a_r(v(r+1)-v(r))
-a_{r-1}(v(r)-v(r-1))\right].
\tag{B.1.3}
\]
At zero the two ratios \(a_r/m_r\) are one; at \(1\) and \(-1\) the inward ratio is \(1+1/d\); all other ratios are one. For \(L=3\) the two edges incident to zero are distinct and the remaining edge has coefficient one, so (B.1.3) includes that case exactly. The weights in (B.1.2) are used only in this finite algebraic identity, not as an assumption on the law of the process.

### B.2. A finite pair Poisson equation

Define
\[
b(r)=\mathbf 1_{\{0<\operatorname{dist}_L(r,0)\le k\}},
\qquad
\beta=\frac{2k}{L+1/d},
\qquad
g_r=m_r(b(r)-\beta).
\tag{B.2.1}
\]
The condition \(k<L/2\) means that the layer contains exactly the \(2k\) distinct nonzero residues represented by \(1,\ldots,k\) and \(L-k,\ldots,L-1\). Also \(2k<L<L+1/d\), so \(0<\beta<1\). It follows that
\[
\sum_{r=0}^{L-1}g_r=2k-\beta(L+1/d)=0,
\qquad
\sum_{r=0}^{L-1}(g_r)^+=2k(1-\beta)\le2k,
\tag{B.2.2}
\]
where \(a^+=\max\{a,0\}\). In particular \(g_0=-m_0\beta\); equality is not included in the positive layer.

For \(r=0,\ldots,L-1\), put
\[
S_r=\frac1{2q}\sum_{j=0}^r g_j.
\]
Then \(S_{L-1}=0\), so the cyclic identity
\[
S_r-S_{r-1}=g_r/(2q)
\tag{B.2.3}
\]
also holds at \(r=0\). Every difference of two \(S_r\)'s is a signed sum of \(g_j/(2q)\) over an interval. A positive such sum is at most the total positive sum in (B.2.2); its negative is at most the total negative sum in absolute value, which is the same because the full sum is zero. Therefore
\[
\max_rS_r-\min_rS_r\le k/q.
\tag{B.2.4}
\]

Let
\[
\overline S=
\frac{\sum_{r=0}^{L-1}S_r/a_r}{\sum_{r=0}^{L-1}1/a_r},
\qquad J_r=S_r-\overline S.
\]
All the weights \(1/a_r\) are positive. Hence \(\overline S\) lies between the minimum and maximum of the \(S_r\)'s. Equations (B.2.3)–(B.2.4) give
\[
J_r-J_{r-1}=g_r/(2q),
\qquad
\sum_{r=0}^{L-1}J_r/a_r=0,
\qquad
|J_r|\le k/q.
\tag{B.2.5}
\]

Set \(v(0)=0\) and prescribe the increments
\[
v(r+1)-v(r)=J_r/a_r.
\tag{B.2.6}
\]
The zero sum in (B.2.5) makes this prescription periodic, and hence defines a function on \(\mathbb T_L\). Substituting (B.2.5)–(B.2.6) into (B.1.3) proves
\[
\mathcal H v=b-\beta.
\tag{B.2.7}
\]
Since every \(a_r\ge1\), each increment in (B.2.6) has absolute value at most \(k/q\). Traveling along at most \(L\) edges between any two residues gives
\[
\operatorname{osc}(v):=\max_rv(r)-\min_rv(r)\le Lk/q.
\tag{B.2.8}
\]

The operator (B.1.1) commutes with reflection \(r\mapsto-r\), and \(b\) is even. Thus replacing \(v(r)\) by \((v(r)+v(-r))/2\) preserves (B.2.7). Every new value remains between the old minimum and maximum, so it preserves (B.2.8) as an upper bound. From now on use this even \(v\). No uniqueness assertion for the Poisson equation is needed.

### B.3. The averaged factorial identity

This section proves the averaging identity. Fixed physical labels are not assumed to have autonomous projected dynamics.

For any population size \(a\ge1\), define its occupation space
\[
\Omega_a=\left\{\eta\in\mathbb N_0^{\mathbb T_L}:
\sum_x\eta_x=a\right\}.
\]
The occupation map of a labelled tuple is
\[
\eta_x(z)=\sum_{i=1}^a\mathbf 1_{\{z_i=x\}}.
\]
For a function \(f:\Omega_a\to\mathbb R\), summing the labelled jump rates of all particles at the source gives
\[
\widehat G_a f(\eta)
=\frac qd\sum_{x\in\mathbb T_L}\sum_{y=x\pm1}
\eta_x(d+\eta_y)
[f(\eta-\delta_x+\delta_y)-f(\eta)].
\tag{B.3.1}
\]
Moreover \(G_a(f\circ\eta)=(\widehat G_af)\circ\eta\), directly from the same sum. A coordinate vector \(\delta_x\) in this section has one at site \(x\) and zero elsewhere.

For \(\xi\in\Omega_2\) and \(\eta\in\Omega_n\), put
\[
W_\xi(\eta)=\prod_x\binom{\eta_x}{\xi_x},
\qquad
D_{n,2}f(\eta)=\binom n2^{-1}\sum_{\xi\in\Omega_2}W_\xi(\eta)f(\xi).
\tag{B.3.2}
\]
The binomial convention is \(\binom ab=0\) for integers \(a\ge0\) and \(b>a\), and \(\binom a0=1\). Expressions with a negative component of \(\xi\) are omitted. Choosing two of the \(n\) physical indices according to their sites, or taking the degree-two coefficient of
\[
\prod_x(1+t)^{\eta_x}=(1+t)^n,
\]
proves \(\sum_{\xi\in\Omega_2}W_\xi(\eta)=\binom n2\).

We claim that for every real \(f\) on \(\Omega_2\),
\[
\widehat G_nD_{n,2}f=D_{n,2}\widehat G_2f.
\tag{B.3.3}
\]
To prove this, first consider one undirected edge \(\{x,y\}\) and write \(\eta_x=A,\eta_y=B\). Let \(\mathcal L^{xy}\) denote its two unscaled rates \(A(d+B)\) and \(B(d+A)\). With formal variables \(u,v\), set
\[
J(u,v)=(1+u)^A(1+v)^B.
\]
The increment from \(x\) to \(y\) is
\((v-u)(1+u)^{A-1}(1+v)^B\), multiplied by \(A(d+B)\); the reverse increment has \(u-v\) and the exponents interchanged. If a departure population is zero its whole contribution is zero. Separating the terms involving \(d\) from those involving \(AB\) yields the polynomial identity
\[
\mathcal L^{xy}J
=d(v-u)(\partial_u-\partial_v)J
+(v-u)^2\partial_u\partial_vJ.
\tag{B.3.4}
\]
For the mixed term, the two expressions with factor \(AB\) combine to
\(AB(v-u)^2(1+u)^{A-1}(1+v)^{B-1}\), which is the second term of (B.3.4).

For \(\xi_x=r,\xi_y=s\), extract the coefficient of \(u^rv^s\), retaining the binomial factors at all other sites. The derivative terms produce respectively the two index shifts and the unshifted coefficients. Explicitly the result is
\[
\begin{aligned}
\mathcal L^{xy}W_\xi={}&
(r+1)(d+s-1)W_{\xi+\delta_x-\delta_y}\\
&+(s+1)(d+r-1)W_{\xi-\delta_x+\delta_y}\\
&-[r(d+s)+s(d+r)]W_\xi.
\end{aligned}
\tag{B.3.5}
\]
For example, the \(dv\partial_u\) contribution to the first shifted term is \(d(r+1)\), and the \(v^2\partial_u\partial_v\) contribution is \((r+1)(s-1)\), giving its displayed coefficient. The other shifted coefficient is obtained from the positive term \(du\partial_v\) in the expansion of \(d(v-u)(\partial_u-\partial_v)\), and from \(u^2\partial_u\partial_v\). The unshifted contributions are \(-d(r+s)-2rs\). When \(s=0\) the first shifted term is absent, and when \(r=0\) the second is absent; no negative-index binomial is evaluated.

Multiply (B.3.5) by \(f(\xi)\), and sum over \(\Omega_2\). In the first shifted sum set \(\ell=\xi+\delta_x-\delta_y\). Its coefficient becomes \(\ell_x(d+\ell_y)\), and its test becomes \(f(\ell-\delta_x+\delta_y)\). The omitted-index convention is equivalent to the departure restriction \(\ell_x\ge1\). In the second shifted sum the coefficient and test become \(\ell_y(d+\ell_x)\) and \(f(\ell+\delta_x-\delta_y)\). The diagonal terms give the two corresponding negative terms. This is precisely the generator for the two orientations of the edge acting on \(f\), averaged with weights \(W_\ell(\eta)\).

For \(L\ge3\), the collection
\[
\mathcal E_L=\{\{x,x+1\}:x\in\mathbb T_L\}
\]
consists of \(L\) distinct undirected edges. Its two orientations reproduce each of the \(2L\) directed nearest-neighbor edges in (B.3.1) once. In particular \(L=3\) gives three undirected edges and six directed ones. Summing the preceding edge identity, multiplying by the common factor \(q/d\), and dividing by \(\binom n2\) proves (B.3.3). The sampling order does not change \(q\).

Because \(v\) is even, the two-particle tuple function
\[
f_v(z_1,z_2)=v(z_2-z_1)
\]
is symmetric, so it defines an occupation function \(f_v:\Omega_2\to\mathbb R\). Equation (B.1.1) says that \(\widehat G_2f_v\), evaluated on the occupation of \((z_1,z_2)\), is \(\mathcal Hv(z_2-z_1)\). There are exactly \(W_\xi(\eta(z))\) unordered pairs of distinct physical indices whose sampled occupation is \(\xi\). Hence (B.3.2) gives
\[
V(z):=D_{n,2}f_v(\eta(z))
=\binom n2^{-1}\sum_{1\le i<j\le n}v(z_j-z_i).
\tag{B.3.6}
\]
Combining (B.3.1), (B.3.3), (B.3.6), and (B.2.7) proves the exact labelled-generator identity
\[
G_nV(z)
=\binom n2^{-1}\sum_{i<j}\mathcal Hv(z_j-z_i)
=\binom n2^{-1}B_k(z)-\beta.
\tag{B.3.7}
\]
This is an identity for the average over all physical index pairs. It does not assert an intertwining for the projection onto any fixed two labels. For example the rate at which one selected label moves to a neighboring site is \(q(1+\eta_y/d)\), which depends on unselected labels at that site. The cancellation needed in (B.3.7) is exactly the coefficient-and-reindexing argument above.

Finally every summand of (B.3.6) lies between \(\min v\) and \(\max v\). Thus
\[
\operatorname{osc}(V)\le\operatorname{osc}(v)\le Lk/q.
\tag{B.3.8}
\]

### B.4. Conditional Dynkin identity at stopping times

The labelled state space is finite. Its total jump rate is bounded by
\[
2qn+\frac qd n(n-1),
\]
because for \(L\ge3\) each ordered pair of distinct labels can contribute to at most one directed adjacency term. In particular the chain is nonexplosive. Both \(V\) and \(G_nV\) are bounded.

For completeness the finite-state Markov property and differentiation of the finite matrix exponential imply, for deterministic \(s\le t\),
\[
\mathbb E[V(Z_t)-V(Z_s)\mid\mathcal F_s]
=\mathbb E\left[\int_s^tG_nV(Z_u)\,du
\;\middle|\;\mathcal F_s\right].
\]
One can see this by differentiating
\(\mathbb E[V(Z_{s+r})\mid\mathcal F_s]=(e^{rG_n}V)(Z_s)\)
in \(r\) and integrating; all sums are finite. Therefore
\[
M_t=V(Z_t)-V(Z_0)-\int_0^tG_nV(Z_s)\,ds
\]
is a martingale, also for the usual completed right-continuous natural filtration. On every deterministic bounded time interval it is bounded by a deterministic constant.

Let a deterministic \(T\) bound both \(\tau\) and \(\sigma\). Approximate these stopping times from above by stopping times taking finitely many dyadic values, bounded by \(T+1\). For those times the conditional martingale identity follows by a finite sum of the deterministic-time identities. Right continuity of \(V(Z_t)\), continuity of the time integral, and the preceding boundedness permit dominated convergence, including after multiplication by each bounded \(\mathcal F_\tau\)-measurable random variable. This proves
\[
\mathbb E\left[\int_\tau^\sigma G_nV(Z_s)\,ds
\;\middle|\;\mathcal F_\tau\right]
=
\mathbb E[V(Z_\sigma)-V(Z_\tau)\mid\mathcal F_\tau].
\tag{B.4.1}
\]
No stopping-time independence is used.

Insert (B.3.7) into (B.4.1), and use (B.3.8), \(\beta\ge0\), and \(\sigma-\tau\le\delta\). It follows that
\[
\begin{aligned}
\binom n2^{-1}
\mathbb E\left[\int_\tau^\sigma B_k(Z_s)\,ds
\;\middle|\;\mathcal F_\tau\right]
&=\beta\,\mathbb E[\sigma-\tau\mid\mathcal F_\tau]
+\mathbb E[V(Z_\sigma)-V(Z_\tau)\mid\mathcal F_\tau]\\
&\le\beta\delta+\operatorname{osc}(V)\\
&\le\frac{2k\delta}{L+1/d}+\frac{Lk}{q}.
\end{aligned}
\]
Multiplication by \(\binom n2\) proves the stated inequality.

Every bound used is independent of the starting state or its distribution. The proof applies to all stated finite parameter values, including \(L=3\), and counts only positive pair distances.

## C. Transfer from resolvents to path laws

### C.1. Statement and resolvent identity

**Theorem C.1 (path convergence from uniform resolvents).** Let \((E,d)\) be a compact metric space. Let \((P_t)_{t\ge0}\) be a conservative, strongly continuous Feller semigroup on \(C(E)\). Assume that it has a continuous-path Markov realization with law \(Q_x\) for each \(x\in E\). For \(\lambda>0\) and \(g\in C(E)\), define
\[
R_\lambda g=\int_0^\infty e^{-\lambda t}P_tg\,dt.
\]

For each integer \(N\ge1\), let \(Z_N\) be a continuous-time Markov chain on a finite set \(S_N\). Write \(A_N\) for its generator and \(T_N(t)\) for its transition semigroup. Let \(\pi_N:S_N\to E\), and set \(X_N=\pi_N(Z_N)\). For a real function \(b\) on \(S_N\), define
\[
R_\lambda^N b=\int_0^\infty e^{-\lambda t}T_N(t)b\,dt.
\]
Assume the following two conditions.

1. For every \(\lambda>0\) and every \(g\in C(E)\),
   \[
   \sup_{z\in S_N}
   \left|R_\lambda^N(g\circ\pi_N)(z)
   -(R_\lambda g)(\pi_N(z))\right|\longrightarrow0.
   \]
2. The largest possible projected jump tends to zero:
   \[
   \sup_{\substack{z,w\in S_N\\A_N(z,w)>0}}
   d(\pi_N(z),\pi_N(w))\longrightarrow0.
   \]
   This supremum is zero if there are no such pairs.

For every deterministic sequence \(z_N\in S_N\) such that \(\pi_N(z_N)\to x\in E\), the conclusion is
\[
\operatorname{Law}_{z_N}(X_N)\longrightarrow Q_x
\quad\text{in }D([0,\infty),E)
\]
with the Skorokhod \(J_1\) topology. The proof gives tightness at stopping times and unique identification of the path law. It does not assume that \(X_N\) is Markov with respect to its projected state. The resolvent assumption holds over all microscopic states. Uniform convergence of the semigroups in time is not an additional assumption.

*Proof.* All resolvents use a positive discount. Put \(g_N=g\circ\pi_N\). Both semigroups are contractions, so their resolvents have norm at most \(1/\lambda\). Write
\[
f_N=R_\lambda^N g_N,\qquad f=R_\lambda g.
\]
Assumption 1 gives uniform approximation of \(f_N\) by \(f\circ\pi_N\). The finite-state resolvent identity gives
\[
A_N f_N=\lambda f_N-g_N. \tag{C.1}
\]

### C.2. Uniform exit probabilities and tightness

Fix \(\varepsilon>0\). Compactness gives finitely many centers \(x_i\) whose open balls of radius \(\varepsilon/8\) cover \(E\). Choose continuous functions \(g_i:E\to[0,1]\). Require that \(g_i\) vanish on the closed ball of radius \(\varepsilon/4\) about \(x_i\). Require that \(g_i\) equal one outside the open ball of radius \(\varepsilon/2\). Linear interpolation in the distance constructs these functions, also when a relevant set is empty.

Strong continuity of \(P\) gives \(\lambda R_\lambda g_i\to g_i\) uniformly as \(\lambda\to\infty\). To see this, bound the norm of the difference by
\[
\int_0^\infty \lambda e^{-\lambda t}\|P_tg_i-g_i\|_\infty\,dt.
\]
Split this integral at a fixed small time. Strong continuity controls the first part, and the exponential tail controls the second part.

Fix \(0<a<1/4\). First choose a common \(\lambda\) sufficiently large. Then choose \(N\) sufficiently large, using assumption 1, so that for every \(i\),
\[
h_{N,i}:=\lambda R_\lambda^N(g_i\circ\pi_N),\qquad
\|h_{N,i}-g_i\circ\pi_N\|_\infty\le a. \tag{C.2}
\]
Nonnegativity of the semigroup gives \(h_{N,i}\ge0\). By (C.1), \(e^{-\lambda t}h_{N,i}(Z_N(t))\) is a nonnegative supermartingale. Its discounted drift is
\[
-\lambda e^{-\lambda t}g_i(\pi_N(Z_N(t)))\le0.
\]

For any starting state \(z\), choose \(i\) such that \(d(\pi_N(z),x_i)<\varepsilon/8\). Then \(h_{N,i}(z)\le a\). Let \(\tau\) be the first time at which
\[
d(X_N(t),\pi_N(z))\ge\varepsilon.
\]
If \(\tau<\infty\), the triangle inequality gives
\[
d(X_N(\tau),x_i)\ge7\varepsilon/8.
\]
Thus \(h_{N,i}(Z_N(\tau))\ge1-a\). Optional stopping at \(\tau\wedge\delta\), for \(\delta\ge0\), gives
\[
\mathbb P_z(\tau\le\delta)
\le\frac{a e^{\lambda\delta}}{1-a}. \tag{C.3}
\]
This estimate is uniform over \(z\) and all sufficiently large \(N\). A finite-state chain is nonexplosive. Its first exit occurs at a jump or is infinite, so the exit value used above is attained.

Since \(a\) is arbitrary, (C.3) proves
\[
\lim_{\delta\downarrow0}\limsup_{N\to\infty}
\sup_{z\in S_N}\mathbb P_z\left(
\sup_{0\le t\le\delta}d(X_N(t),X_N(0))\ge\varepsilon
\right)=0. \tag{C.4}
\]
For each \(a\), first choose \(\lambda\) and the threshold for \(N\) as above. Then let \(\delta\) decrease to zero, and finally let \(a\) decrease to zero. This uses no rate of convergence in \(N\).

Let \(\sigma\) be a bounded stopping time of the full microscopic chain. Its strong Markov property applies (C.4) conditionally on \(Z_N(\sigma)\). Thus (C.4) bounds the probability of an \(\varepsilon\) increment from \(\sigma\) to \(\sigma+u\), for every \(0\le u\le\delta\). The bound is uniform over \(\sigma\), initial states, and \(u\). This proves Aldous' stopping-time condition in the microscopic filtration and hence in the projected filtration. Compactness of \(E\) gives compact containment.

The Aldous criterion now gives tightness in \(D([0,T],E)\) for each finite \(T\). Its local form gives tightness in \(D([0,\infty),E)\). The criterion is the sufficient condition from compact containment and stopping-time increments; see D. Aldous, [“Stopping Times and Tightness,” *Annals of Probability* **6** (1978), 335–340](https://doi.org/10.1214/aop/1176995579). For a general compact metric space \(E\), use countably many continuous distance coordinates to embed \(E\). The metric-space version of the same criterion then applies.

Assumption 2 ensures that every convergent subsequence has a continuous limit. The deterministic \(J_1\) argument is as follows. On each horizon whose endpoint is a continuity point of the limit, time changes give uniform closeness to the limit path. Suppose that this path has an interior jump of size \(b>0\). Each one-sided value of the time-changed approximating path is within the uniform error of the corresponding limit value. Thus the approximating path has a jump of size at least \(b\) minus twice that error. Time changes preserve jump sizes. Therefore a jump of a \(J_1\) limit cannot exceed the lower limit of the largest approximating jump sizes. Assumption 2 makes those sizes tend to zero. Apply this argument on all suitable finite horizons. All limit paths are continuous.

### C.3. Martingale identification and uniqueness

Let a subsequence converge to \(X\). This process has continuous paths and starts at \(x\). For \(\lambda>0\) and \(g\in C(E)\), (C.1) gives the martingale
\[
f_N(Z_N(t))-f_N(Z_N(0))
-\int_0^t[\lambda f_N(Z_N(u))-g(X_N(u))]\,du. \tag{C.5}
\]
It is bounded on each finite time interval. Uniform approximation and continuity of \(f\) and \(g\) permit passage to the limit in (C.5), since the limiting paths are continuous. This also holds after multiplication by any bounded continuous function of finitely many earlier projected coordinates. All these products are uniformly bounded on each finite time interval, so their expectations converge.

Such functions generate the natural path filtration, by the monotone-class theorem. First use a countable dense set of times, and then use continuity. It follows that
\[
f(X_t)-f(X_0)-\int_0^t[\lambda f(X_u)-g(X_u)]\,du \tag{C.6}
\]
is a martingale in the natural filtration \((\mathcal F_t^X)_{t\ge0}\) of \(X\). This argument uses no Markov property of \(X_N\) after projection.

These resolvent martingales determine the full law. Discount (C.6) and take conditional expectations after time \(s\ge0\). For finite \(v\ge0\), this gives
\[
\mathbb E\left[
 e^{-\lambda v}f(X_{s+v})
 +\int_0^v e^{-\lambda u}g(X_{s+u})\,du
 \;\middle|\;\mathcal F_s^X\right]=f(X_s).
\]
As \(v\to\infty\), the first term tends to zero uniformly, and the integrals converge boundedly. Hence
\[
\mathbb E\left[
\int_0^\infty e^{-\lambda u}g(X_{s+u})\,du
\;\middle|\;\mathcal F_s^X\right]=(R_\lambda g)(X_s). \tag{C.7}
\]

For any bounded real \(\mathcal F_s^X\)-measurable random variable \(H\), define
\[
b(u)=\mathbb E[H g(X_{s+u})]
-\mathbb E[H(P_u g)(X_s)].
\]
This function is bounded and continuous. Continuity follows from the continuous paths of \(X\), bounded convergence, and strong continuity of \(P\). Equation (C.7) and the definition of \(R_\lambda\) show that the Laplace transform of \(b\) is zero for every \(\lambda>0\).

To prove uniqueness directly, take integers \(\lambda\ge1\) and substitute \(v=e^{-u}\). The bounded function \(b(-\log v)\), for \(0<v\le1\), has integral zero against every polynomial on \([0,1]\). Its value at zero can be assigned arbitrarily. Uniform polynomial density shows that the finite signed measure with this density is zero. Thus \(b\) is zero almost everywhere in \(u\). Continuity gives \(b(u)=0\) for every \(u\ge0\).

It follows that, for every fixed \(s,u\ge0\) and \(g\in C(E)\),
\[
\mathbb E[g(X_{s+u})\mid\mathcal F_s^X]=(P_u g)(X_s).
\]
Use a countable uniformly dense subset of \(C(E)\) to identify the conditional transition probabilities. Compact metrizability makes \(C(E)\) separable, and uniform approximation extends equality of probability integrals to every function in \(C(E)\). Induction identifies every finite-dimensional distribution with that under \(Q_x\). Laws on continuous path space are determined by their finite-dimensional distributions at a countable dense set of times. Hence \(\operatorname{Law}(X)=Q_x\). Every subsequential limit has this law, so tightness gives convergence of the whole sequence in the stated topology.

In the application to Theorem 1, Section 5.2 proves assumption 1 for the full mass process, and Section 5.4 verifies assumption 2.

## References and standard results


Section 4 uses the following continuum construction and uniqueness results, with the normalization derived there.

- Y. Le Jan and O. Raimond, *Sticky flows on the circle*, arXiv:math/0211387v1, Sections 2–3, equation (3.6), Theorem 3.3. The exact partition weights, core closure, compatibility, and strong Feller construction are used. [Versioned PDF](https://arxiv.org/pdf/math/0211387v1).
- C. Howitt and J. Warren, *Consistent families of Brownian motions and stochastic flows of kernels*, *Annals of Probability* 37 (2009), 1237–1272, arXiv:math/0611292v2, Definition 2.1, equations (2.7),(2.9), Theorem 2.1, Proposition 8.1. Only the real continuum martingale problem, its uniqueness for the checked parameter family, and its Feller laws are used. [Versioned PDF](https://arxiv.org/pdf/math/0611292v2).

The target construction is also described in Y. Le Jan and S. Lemaire, [*Products of Beta matrices and sticky flows*](https://arxiv.org/abs/math/0307106), arXiv:math/0307106.

The standard tightness criterion invoked in Section 2 is D. Aldous, *Stopping Times and Tightness*, *Annals of Probability* 6 (1978), 335–340, [DOI](https://doi.org/10.1214/aop/1176995579): compact containment and the displayed stopping-time increment condition give tightness in Skorokhod space. The implication of vanishing jumps under \(J_1\) convergence is explained in Section 2. Other background consists of finite-state Markov chains, their strong Markov property and generator martingales, Dynkin's formula, optional sampling, Doob's inequality, conditional Fubini, Prokhorov and Skorokhod representation on Polish spaces, elementary martingale quadratic covariation, dominated convergence, the monotone-class theorem, Stone–Weierstrass, and elementary properties of closed symmetric forms and their associated semigroups. All model-specific estimates and every passage from these objects to the exact target are either applications of Appendices A–C or arguments displayed above.
