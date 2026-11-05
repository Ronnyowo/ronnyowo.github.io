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

**Theorem A.1 (harmonic corrections and trace estimates).** Under the definitions and hypotheses of Section A.1, there exist finite constants \(C_n\ge1\) and, for every real \(p\ge1\), \(C_{n,p}\ge1\). They depend only on the displayed indices. All six assertions below hold with these constants at the same time. The constants are uniform in lattice positions, separations, partitions, and label subsets. They are also uniform in \(f\) subject to its stated bound \(D\). There is a nonincreasing function \(\omega_n:[0,\infty)\to[0,1]\), depending only on \(n\), with \(\omega_n(r)\to0\) as \(r\to\infty\).

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
   \kappa_{A,B}\partial_{v_{A,B}}f(z)\right|\le C_nD\omega_n(R_*).
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
   |\Gamma_0^{ij}(z)-2\mathbf1_{\{z_i=z_j\}}|\le C_n\omega_n(R_*),\qquad
   |\Gamma_d^{ij}(z)-2\mathbf1_{\{z_i=z_j\}}|\le C_n(\omega_n(R_*)+d).
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

### A.8. Localization by coupling

Fix a partition and tuple as in (A-H3), with \(R_*\ge16\) and distinct block sites at distance at least \(16R_*\). Order the blocks by their sites. On the region with this strict external block order, there are chamber-affine functions \(f_B:\mathbb R^B\to\mathbb R\), each with sum-norm Lipschitz bound \(D\), such that
\[
f(x)=f(0)+\sum_{B\in\pi}f_B(x|_B).
\tag{A.20}
\]
To construct \(f_B\), restrict each chamber gradient of \(f\) to the coordinates in \(B\), using the fixed external order. These coordinates do not depend on internal orders in other blocks: an adjacent exchange there changes the gradient only by a multiple of the difference of two unit vectors in that other block. Use these restricted gradients as the linear formulas for \(f_B\), with zero intercept. Adjacent formulas agree on their common face. Successive exchanges of equal coordinates give agreement at every further intersection. Thus \(f_B\) is continuous. Its gradient coordinates have absolute value at most \(D\). Integration along a segment proves its Lipschitz bound. The chamber formulas then give (A.20).

Apply the correction construction to each block subtuple and put
\[
W=f+\sum_{B\in\pi}\psi_{f_B},\qquad \Delta=H_f-W.
\]
For singleton blocks use Section A.11; their correction is zero. By (A.3),
\[
\|\Delta\|_\infty\le C_nD.
\tag{A.21}
\]
If every label lies within \(2R_*\) of its reference block site, every \(Q\)-endpoint lies within \(4R_*\). The blocks remain separated and retain their external order. The interaction component of each attempt lies in one reference block. Thus \(Q\) acts on block sums as the sum of the isolated block generators. Equation (A.20) and \(Q_BH_{f_B}=0\) give \(QW=0\), hence \(Q\Delta=0\), on this region.

We first identify the endpoints needed for the \(B\)-row at \(z\). In \(B=RURP|_{S_n}\), the first independent event creates a neighboring pair in one reference block, or ends in \(S_n\). In the latter case the killed potential is zero. During the pure-interaction integral, no new site becomes occupied. The inner \(R\) adds at most one neighboring site. If its event is in the same block, that block has at most three consecutive occupied sites. Absorption gives a full stack or two substacks at distance two. If the event is in another block, the two separate two-site components each absorb to a full stack. Negative terms in either \(R\) omit an event and obey the same bounds. Therefore the signed row has finite support among tuples \(s\) with
\[
|s_i-z_i|\le2\quad\text{for every }i,
\]
where each reference block is full except, at most, one block with two substacks at distance two. Also
\[
\|B\|\le\|R\|\|U\|\|R\|\|P\|\le16n^2c_n,
\qquad B\mathbf1=0.
\]
In particular, this bounds the total variation of the signed row.

For any such local tuple \(s\), run two products of isolated block \(Q_B\)-chains from \(s\) and \(z\). The split block in the first product merges almost surely in finite time. Indeed, above gap two its gap has rates two in each direction. It returns to gap two almost surely: from \(r>2\), the chance to hit \(M>r\) before two is \((r-2)/(M-2)\), by the stopped coordinate martingale. Let \(M\to\infty\). At gap two, the merger rate is at least one and the total attempt rate is at most \(2n\), by Section A.4. Each attempt from gap two therefore gives conditional merger probability at least \(1/(2n)\). An attempt that leaves gap two without merger is followed by a return almost surely. The probability of avoiding merger for \(k\) such trials is at most \((1-1/(2n))^k\). Recurrence and the strong Markov property prove the assertion. These bounds hold after every redistribution of labels. If no block is split, take the merger time to be zero.

Run the products independently until that merger. Each reference block is then a full stack in both products. Couple each corresponding pair of stack centers independently until they meet, then synchronously. Full stacks jump left and right at rate one. The difference of two corresponding centers is recurrent, so each pair meets in finite time almost surely. Use separate clock systems for different reference blocks and fresh exponential clocks at each switch. In the joint filtration, each marginal retains the sum of its isolated block generators.

Let \(T\) be the time by which all corresponding centers have met. Let \(R\) be the largest displacement from the reference block sites by either product up to \(T\). There are finitely many blocks, so \(T<\infty\) almost surely. Bounded jump rates then give \(R<\infty\) almost surely. After separate translations of the reference blocks, this coupling depends only on the partition, the split subset, and the offsets in \(\{-2,-1,0,1,2\}\). There are finitely many such local types for fixed \(n\). Hence
\[
\omega_n(r)=\max_{\text{local types}}\mathbb P(R\ge r)
\longrightarrow0\qquad(r\to\infty).
\tag{A.22}
\]
This defines one nonincreasing function for every partition, reference position, and allowed test \(f\).

Stop the products at \(T\) or when either displacement reaches \(R_*\), whichever occurs first. Before this stop the marginal generators agree with \(Q\). Each product is stable within its reference blocks. All stopped endpoints lie within \(R_*+2<2R_*\) of their reference sites, and different reference blocks remain nonadjacent. Thus the endpoints belong to \(S_n\). The two stopped \(\Delta\)-processes are bounded martingales in the joint filtration. If coupling occurs before displacement exit, their terminal values agree. Bounded optional sampling therefore gives
\[
|\Delta(s)-\Delta(z)|\le2\|\Delta\|_\infty\omega_n(R_*).
\tag{A.25}
\]
For the unbounded stop, first impose a deterministic time bound, then use bounded convergence. The signed row has zero mass, so (A.25) yields
\[
|B\Delta(z)|\le C_nD\omega_n(R_*).
\]

It remains to evaluate \(BW(z)\). On every configuration used in this local row calculation, (A.20) and independent block absorption give
\[
P_nW=f(0)+\sum_{B\in\pi}P_BH_{f_B}.
\]
Here the subscripts specify the particle set. After the first independent event, only its own block can be transient. Each other block remains full and satisfies \(R_BP_BH_{f_B}=Q_BH_{f_B}=0\). Thus the inner \(R\) and the killed potential contribute only in the affected block. Summing the initiating events gives the exact factorization
\[
BW(z)=\sum_{B\in\pi}B_BH_{f_B}(x_B\mathbf1_B).
\]
The full-block formula (A.19) evaluates each term. By (A.20), its directional derivatives are those of \(f\) at \(z\). The bound for \(B\Delta\) proves (A-H3). A single full block uses the exact formula from Section A.7.

### A.9. Coordinate covariances

Fix the coordinate test \(f_i(x)=x_i\). At a tuple with one full stack per reference block, each local correction vanishes. Apply (A.25) with \(s=z+\epsilon\mathbf1_B\), for \(\epsilon\in\{-1,1\}\). This tuple is one of the unsplit local types. Since \(\Delta=\psi_{f_i}\) at both endpoints,
\[
H_i(z+\epsilon\mathbf1_B)-H_i(z)
=\epsilon\mathbf1_{\{i\in B\}}+O(C_n\omega_n(R_*)).
\tag{A.26}
\]
At this separated state these are all off-diagonal \(Q\)-transitions, each at rate one. Multiplying the two increments and summing gives
\[
\left|\Gamma_0^{ij}(z)-2\mathbf1_{\{z_i=z_j\}}\right|\le C_n\omega_n(R_*).
\tag{A.27}
\]
Since \(0\le\omega_n\le1\), products of error terms are included in the same bound. At an arbitrary state, every coordinate increment of \(H_i\) is at most \(2+2a_n\) along a \(Q\)-jump, by (A.3) and Section A.4. The total rate is at most \(2n\), so \(\Gamma_0\) is bounded everywhere.

Couple each perturbed excursion after a fixed initiating step to a pure-interaction excursion until the first additional independent event. Sample the entire pure-interaction chain independently of the extra independent clocks. Continue this sampled pure path if an extra event occurs. The sampled pure chain has the pure-excursion marginal law. If no extra event occurs before absorption, the two endpoints coincide and \(J=0\). On the complementary event \(J\ge1\), the pure endpoint is within \(n\) of the initial tuple coordinatewise, and the perturbed endpoint is within \(n+J\). Their corrected coordinate increments are therefore bounded by \(C_n\) and \(C_n(1+J)\), respectively. It follows that the absolute difference of the products of increments for coordinates \(i,j\) is at most \(C_n[(1+J)^2+1]\mathbf1_{\{J\ge1\}}\). Equation (A.7), summed over the \(2n\) initiating steps in (A.11), gives
\[
\sup_{z,i,j}|\Gamma_d^{ij}(z)-\Gamma_0^{ij}(z)|\le C_nd.
\tag{A.28}
\]
Absolute convergence follows already from the second-moment instance of (A.13), using \(|ab|\le(a^2+b^2)/2\). Combining (A.27), (A.28), and the global bound proves every covariance assertion. Finally, the split sum for a coordinate test is zero. Complementary subsets have equal factorial coefficients and opposite vectors. Thus the split sum in (A-H3) is zero for a coordinate test.

### A.10. Uniformity of the conclusions

Sections A.4–A.5 apply to each fixed integer \(n\ge2\). Section A.6 applies to every \(0<d\le d_n\) and every real \(p\ge1\). It proves the convergent trace expansion before the coefficient comparison in Section A.7. Section A.8 applies to every partition and every \(R_*\ge16\). Its finite set of local coupling types gives one function \(\omega_n\) for all block sites and block sizes. Section A.9 proves the covariance bounds at every state and their estimates at separated states. The cycle matrices in Section A.7 prove only the local coefficient identities on the line.

### A.11. The one-label case

For \(n=1\), every site is already in \(S_1\), so both absorption times are zero and both potentials vanish. There are no interaction jumps. Therefore \(P=P_d=\operatorname{Id}\), \(Q=T_d=R\), and \(B=0\), for every \(d>0\), in particular \(0<d\le d_1=1\). A chamber-affine function is simply \(f(x)=ax+b\), with \(|a|\le D\), and \(Rf=0\). Its canonical correction is zero. The coordinate has jumps plus and minus one at rate one. Its covariance density is two. Its square maximal displacement is at most \(8t\). Its trace jump moment is \(2|a|^p\le2D^p\). Set \(\omega_1=0\). The near set and every split sum are empty. An initiating step has displacement one and is already in \(S_1\), with \(J=\tau_d=0\). These facts prove the full convention in the statement and the singleton-block facts used in Section A.8.
