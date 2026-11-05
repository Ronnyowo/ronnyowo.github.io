### 1.1. Notation and proof structure

Sections 2–4 prove convergence of the auxiliary labelled processes and identify their limits.
Section 5 proves Theorem 1 by sampling and uniform semigroup convergence.
Appendices A–C prove the harmonic correction estimates, the sampling and occupation bounds, and the semigroup path-transfer theorem.
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

Fix an integer \(n\ge2\). On \(\mathbb T_L^n\), use the labelled operators \(R_n,I_n\) defined above. Let \(S\) be the tuples with no adjacent distinct occupied sites. For \(q>0\) and \(0<d\le d_n\), let \(Z\) have generator \(q(R_n+d^{-1}I_n)\). Write
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
This bound includes the complete duration of an excursion that ends after \(T\). Since \(A(t)\le t\), it gives
\[
\sup_{t\le T}|A(t)-t|=T-A(T)\longrightarrow0
\quad\text{in probability}.
\]

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

The trace strong Markov property applies (I.5.2) after each bounded trace stopping time. Compactness gives compact containment. Aldous' criterion therefore gives tightness of the trace. Equation (I.5.3) makes every limit continuous: under \(J_1\) convergence, time changes give uniform approximation, and a limit jump cannot exceed the largest approximating jump plus twice the uniform error.

It remains to transfer tightness to the untraced chain. For a path \(y\), put
\[
w_T(y,\delta)=\sup_{\substack{s,t\le T\\|s-t|\le\delta}}
\operatorname{dist}(y(s),y(t)).
\]
C-tightness of \(\overline Y_N=Y/L\) implies
\[
\lim_{\delta\downarrow0}\limsup_N
\mathbb P\bigl(w_T(\overline Y_N,\delta)>\varepsilon\bigr)=0.
\tag{I.5.4}
\]
Indeed, each subsequence has a further subsequence represented with almost sure \(J_1\) convergence to a continuous path. That convergence is uniform, and the limiting path is uniformly continuous on \([0,T]\).

By (I.3.6),
\[
\sup_{t\le T}\operatorname{dist}(X_N(t),\overline Y_N(t))
\le D_T+w_T(\overline Y_N,\|A-\operatorname{id}\|_\infty)
\longrightarrow0
\quad\text{in probability}.
\tag{I.5.5}
\]
For the last limit, first bound the clock error by a fixed \(\delta\), use (I.5.4), then let \(\delta\downarrow0\). Equations (I.3.1) and (I.3.4) control the clock and excursion errors. Uniform path closeness implies \(J_1\) closeness. Thus \(X_N\) is C-tight and has the same limits as its trace. No stopping-time property of \(A(\tau)\) in a trace filtration is used.

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
\omega_n(\varepsilon L/16)
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
\omega_n(\varepsilon L/16)+d+
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

Finally, choose finitely many triples of chart balls \(V_j,W_j,B_j\) such that \(\overline V_j\subset W_j\), \(\overline W_j\subset B_j\), and the \(V_j\) cover the compact set under consideration. Choose the outer balls \(B_j\) from the good-radius basis. The preceding entry-time argument gives the stopped identities up to exit from \(W_j\). At each entry select the first \(j\) with the entry point in \(V_j\), then run until exit from \(W_j\). Each exit requires displacement at least \(\min_j\operatorname{dist}(\overline V_j,W_j^c)>0\). Continuity prevents these exits from accumulating in finite time. Concatenation gives the identities up to exit from the compact chart region, without a Markov assumption on the limit.

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

### 5.1. Uniform fixed-order semigroups

**Lemma 5.1.** For \(f\in C(\mathbb T^n)\), put \(f_N(z)=f(z/L_N)\). Let \(P_{N,t}^{(n)}\) be the auxiliary semigroup in Proposition 3.1. For every finite \(T\),
\[
e_N(n,f,T):=
\sup_{t\le T}\sup_{z\in\mathbb T_{L_N}^n}
\left|P_{N,t}^{(n)}f_N(z)-(P_t^{(n)}f)(z/L_N)\right|
\longrightarrow0.
\tag{IV.1.1}
\]

*Proof.* If the assertion fails, choose \(t_N\in[0,T]\) and \(z_N\) with an error bounded below by a positive constant. Compactness gives a subsequence with \(t_N\to t\) and \(z_N/L_N\to x\). Proposition 3.1 and continuity of its limit give
\[
P_{N,t_N}^{(n)}f_N(z_N)\longrightarrow(P_t^{(n)}f)(x).
\]
The Feller property and strong continuity imply joint continuity of \((s,y)\mapsto P_s^{(n)}f(y)\). Indeed, the semigroup law and contraction give continuity in time in the uniform norm; spatial continuity then gives the joint assertion. The target term at \((t_N,z_N/L_N)\) has the same limit. This is a contradiction, including when \(t=0\).

### 5.2. Sampling and mass semigroups

Let \(T_{N,t}\) be the full occupation semigroup. For a symmetric order-\(n\) test, with \(N\ge n\), use the sampling operator of Lemma B.1:
\[
D_{N,n}f(\eta)=\binom Nn^{-1}
\sum_{\sum_x k_x=n}\prod_x\binom{\eta_x}{k_x}f(k).
\tag{IV.2.1}
\]
Here \(f\) is identified with its occupation function. The operator averages samples without replacement, so it is a contraction. Lemma B.1, with \(q=N^2\), \(d=d_N\), and \(L=L_N\) at both population orders, gives
\[
T_{N,t}D_{N,n}f=D_{N,n}P_{N,t}^{(n)}f.
\tag{IV.2.2}
\]

For \(f\in C(\mathbb T^n)\), let \(F_f(\mu)=\int f\,d\mu^{\otimes n}\). We may symmetrize \(f\): this leaves \(F_f\) unchanged and commutes with both labelled semigroups. Sampling physical indices with replacement gives \(F_f(\Phi_N(\eta))\). Conditional on distinct indices, this gives \(D_{N,n}f_N(\eta)\). The repeated-index probability is at most \(n(n-1)/(2N)\). Hence
\[
\left\|D_{N,n}f_N-F_f\circ\Phi_N\right\|_\infty
\le\frac{n(n-1)}N\|f\|_\infty.
\tag{IV.2.3}
\]
Use (IV.2.2), (IV.2.3), Lemma 5.1, and the target identity from Section 1. Contraction gives
\[
\begin{aligned}
&\sup_{t\le T,\eta\in\Omega_N}
\left|T_{N,t}(F_f\circ\Phi_N)(\eta)
-(\mathsf P_tF_f)(\Phi_N(\eta))\right|\\
&\qquad\le e_N(n,f,T)+\frac{2n(n-1)}N\|f\|_\infty
\longrightarrow0.
\end{aligned}
\tag{IV.2.4}
\]
The second sampling error is applied to \(P_t^{(n)}f\), whose norm is at most \(\|f\|_\infty\).

The space \(E=\mathcal P(\mathbb T)\) is compact in the weak topology. Mass polynomials form a real algebra: products correspond to tensor products of tests. This algebra contains constants and separates probability measures. Stone–Weierstrass makes it uniformly dense in \(C(E)\). Replacing a continuous test by a polynomial approximation contributes at most twice the approximation error, since both semigroups are contractions. Thus (IV.2.4) gives, for every real \(G\in C(E)\),
\[
\sup_{t\le T,\eta\in\Omega_N}
\left|T_{N,t}(G\circ\Phi_N)(\eta)
-(\mathsf P_tG)(\Phi_N(\eta))\right|
\longrightarrow0.
\tag{IV.2.5}
\]
The supremum is over all microscopic occupation states.

### 5.3. Proof of Theorem 1

*Proof.* Give \(E=\mathcal P(\mathbb T)\) the Wasserstein distance of order one for the bounded geodesic distance on \(\mathbb T\). It metrizes weak convergence and makes \(E\) compact. Apply Theorem C.1 with
\[
S_N=\Omega_N,\qquad Z_N=\eta_N,\qquad
\pi_N=\Phi_N,\qquad P_t=\mathsf P_t.
\]
The supplied target semigroup is conservative and strongly continuous Feller. Equation (IV.2.5) verifies its uniform semigroup hypothesis. A microscopic jump transports mass \(1/N\) to a neighboring site. Coupling all other mass to itself gives
\[
\sup_{\mathcal L_N(\eta,\eta')>0}
W_1(\Phi_N(\eta),\Phi_N(\eta'))
\le\frac1{NL_N}\longrightarrow0.
\tag{IV.3.1}
\]
This verifies the projected-jump hypothesis. Theorem C.1 gives tightness and a continuous limit. Its finite-dimensional laws are those of the target mass semigroup, so its law is \(Q_{\mu_0}\).

The initial configurations in Theorem 1 satisfy \(\Phi_N(\eta_N^0)\to\mu_0\). They are therefore allowed in this application, and
\[
\operatorname{Law}_{\eta_N^0}(\mu_N(\cdot))
\Longrightarrow Q_{\mu_0}
\quad\text{in }D([0,\infty),\mathcal P(\mathbb T)).
\tag{IV.3.2}
\]
The limit is continuous. The argument imposes no lower bound on the normalized stack masses or the macroscopic separations. This proves all the initial-state assertions of Theorem 1.


## 6. References and standard results

Section 4 uses the following continuum construction and uniqueness results, with the normalization derived there.

- Y. Le Jan and O. Raimond, *Sticky flows on the circle*, arXiv:math/0211387v1, Sections 2–3, equation (3.6), Theorem 3.3. The exact partition weights, core closure, compatibility, and strong Feller construction are used. [Versioned PDF](https://arxiv.org/pdf/math/0211387v1).
- C. Howitt and J. Warren, *Consistent families of Brownian motions and stochastic flows of kernels*, *Annals of Probability* 37 (2009), 1237–1272, arXiv:math/0611292v2, Definition 2.1, equations (2.7),(2.9), Theorem 2.1, Proposition 8.1. Only the real continuum martingale problem, its uniqueness for the checked parameter family, and its Feller laws are used. [Versioned PDF](https://arxiv.org/pdf/math/0611292v2).

The target construction is also described in Y. Le Jan and S. Lemaire, [*Products of Beta matrices and sticky flows*](https://arxiv.org/abs/math/0307106), arXiv:math/0307106.

The tightness criterion is D. Aldous, *Stopping Times and Tightness*, *Annals of Probability* 6 (1978), 335–340, [DOI](https://doi.org/10.1214/aop/1176995579). Its deterministic-lag form and Polish-space extension are stated in Aldous, [*Weak Convergence and the General Theory of Processes*, Section 4, condition (4.2), Theorem (4.4)(ii), pages 25–26](https://www.stat.berkeley.edu/~aldous/Papers/weak-gtp.pdf). Compact containment and the stopping-time increment bounds in Section 2 and Appendix C verify its hypotheses.

The remaining background is finite-state generator martingales, the strong Markov property, Dynkin's formula, optional sampling, Doob's inequality, conditional Fubini, Prokhorov and Skorokhod representation on Polish spaces, quadratic covariation, dominated convergence, the monotone-class theorem, Stone–Weierstrass, and closed symmetric forms. The model-specific estimates and the identification of the exact target are proved above.
