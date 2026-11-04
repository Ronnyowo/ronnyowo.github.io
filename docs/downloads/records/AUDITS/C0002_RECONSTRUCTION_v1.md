# C0002 independent reconstruction — v1

This is an independent proof of the auxiliary claim in `CANDIDATES/C0002_resolvent_path_transfer/CONTRACT_v1.md`. It was constructed from the contract, its accepted brief, and `STATEMENT.md` only. No candidate proof or other audit was consulted. This document does not evaluate an unseen proof and does not establish the microscopic hypotheses for SIP or the conclusion of STATEMENT-v1.

## Inputs and scope

The exact source files and SHA-256 hashes are:

- `STATEMENT.md`: `ca925b943f2dc5573b840512e12ebd5f38fbdb15df7a6b02c3dd72f7ac698a97`.
- `CANDIDATES/C0002_resolvent_path_transfer/CONTRACT_v1.md`: `d42cb0e8db6e9667f77d45f7e4d54994179e48b206fb343af6e50eaf67057c6b`.
- `CANDIDATES/C0002_resolvent_path_transfer/BRIEF_v1.md`: `ec44f79e9849a71bc2cad4d75978ffdde78b8748c83bbeb5e991d4529a92b192`.

There are no promoted campaign dependencies. A separate immutable input/exposure record accompanies this proof.

Let the objects and the two assumptions be exactly those in the contract. In particular, every resolvent estimate is uniform over the entire microscopic state space. All functions below are real-valued; this suffices to identify probability laws.

We prove that, whenever the deterministic initial states satisfy
\[
\pi_N(z_N)\longrightarrow x,
\]
the laws of the projected processes converge to the specified law \(Q_x\) on \(D([0,\infty),E)\) with its \(J_1\) topology. The microscopic filtration is used throughout; the projected process is never assumed to be Markov.

## 1. Resolvent identities and approximation of continuous functions

Both semigroups are positive contractions in the supremum norm. Thus, for every \(r>0\),
\[
\|R_r g\|_\infty\leq r^{-1}\|g\|_\infty,
\qquad
\|R_r^N b\|_\infty\leq r^{-1}\|b\|_\infty.
\]

Strong continuity of \(P_t\) gives
\[
\|rR_r g-g\|_\infty\longrightarrow0
\quad\text{as }r\longrightarrow\infty.
\tag{1}
\]
Indeed, the norm is at most
\[
\int_0^\infty r e^{-rt}\|P_tg-g\|_\infty\,dt.
\]
For any prescribed error, choose a small positive time below which strong continuity bounds the integrand's norm by that error. The integral above this time is bounded by \(2\|g\|_\infty\) times an exponentially vanishing tail. This proves (1).

On a finite state space, differentiating \(T_N(t)\) and integrating by parts gives the exact identity
\[
A_NR_r^N b=rR_r^N b-b.
\tag{2}
\]
The boundary at infinity vanishes because the semigroup is a contraction; the boundary at zero is \(-b\).

Fix \(g\in C(E)\), write \(M=\|g\|_\infty\), and, for a fixed \(r>0\), set
\[
F_N=rR_r^N(g\circ\pi_N),
\qquad
H_N=rR_r^N(g^2\circ\pi_N).
\]
These are microscopic functions, which need not be functions of the projected state. Define the deterministic errors
\[
a_N(r,g)=\|F_N-g\circ\pi_N\|_\infty,
\qquad
b_N(r,g)=\|H_N-g^2\circ\pi_N\|_\infty.
\]
By the uniform resolvent hypothesis,
\[
\limsup_{N\to\infty}a_N(r,g)
\leq\|rR_rg-g\|_\infty,
\tag{3}
\]
\[
\limsup_{N\to\infty}b_N(r,g)
\leq\|rR_rg^2-g^2\|_\infty.
\tag{4}
\]
Also, (2) and contraction imply
\[
\|A_NF_N\|_\infty\leq2rM,
\qquad
\|A_NH_N\|_\infty\leq2rM^2.
\tag{5}
\]

## 2. Uniform control at stopping times

Let \(\mathcal F_t^N\) be the microscopic chain's natural filtration. Fix a finite \(T\) and \(0<\delta\leq1\). Let \(\tau,\sigma\) be any stopping times with
\[
0\leq\tau\leq T,
\qquad
\tau\leq\sigma\leq\tau+\delta.
\]
Every expectation in this section can be taken under any microscopic initial distribution. For a microscopic bounded function \(V\), its Dynkin martingale, optional stopping, and any bounded \(\mathcal F_\tau^N\)-measurable variable \(B\) give
\[
\mathbb E\big[B(V(Z_N(\sigma))-V(Z_N(\tau)))\big]
=
\mathbb E\left[B\int_\tau^\sigma A_NV(Z_N(v))\,dv\right].
\tag{6}
\]
All stopping times here are bounded by \(T+1\); finite-state Dynkin martingales are integrable on this interval, so this application of optional stopping is valid.

Abbreviate \(G_t=g(X_N(t))\). Using \(V=H_N\), \(B=1\), and (5) in (6) gives
\[
\left|\mathbb E[G_\sigma^2-G_\tau^2]\right|
\leq2b_N(r,g)+2rM^2\delta.
\tag{7}
\]
Using \(V=F_N\) and \(B=G_\tau\), whose absolute value is at most \(M\), gives
\[
\left|\mathbb E[G_\tau(G_\sigma-G_\tau)]\right|
\leq2M a_N(r,g)+2rM^2\delta.
\tag{8}
\]
Since
\[
(G_\sigma-G_\tau)^2
=G_\sigma^2-G_\tau^2-2G_\tau(G_\sigma-G_\tau),
\]
we obtain the uniform estimate
\[
\mathbb E\big[(g(X_N(\sigma))-g(X_N(\tau)))^2\big]
\leq2b_N(r,g)+4M a_N(r,g)+6rM^2\delta.
\tag{9}
\]
In particular, this estimate has no dependence on the initial state, \(T\), or the particular stopping times.

First take the supremum over these stopping times and all initial states, then take \(\limsup_{N\to\infty}\), then let \(\delta\downarrow0\). Equations (3) and (4) bound the result by
\[
2\|rR_rg^2-g^2\|_\infty
+4M\|rR_rg-g\|_\infty.
\]
Finally let \(r\to\infty\) and use (1), for both \(g\) and \(g^2\). Therefore
\[
\lim_{\delta\downarrow0}\limsup_{N\to\infty}
\sup_{z\in S_N}\sup_{\substack{\tau\leq T\\
\tau\leq\sigma\leq\tau+\delta}}
\mathbb E_z\big[(g(X_N(\sigma))-g(X_N(\tau)))^2\big]=0.
\tag{10}
\]
The second supremum is over stopping times for the microscopic filtration. Hence it includes all stopping times for the projected filtration.

To pass from functions to the metric, fix \(\varepsilon>0\), and choose a finite open \(\varepsilon/4\)-net \(e_1,\ldots,e_m\) in the compact space \(E\). Put
\[
g_i(y)=d(y,e_i).
\]
If \(d(y,y')>\varepsilon\), choose \(i\) with \(d(y,e_i)<\varepsilon/4\). The triangle inequality yields
\[
|g_i(y)-g_i(y')|>\varepsilon/2.
\]
Consequently, by the union bound and the elementary second-moment probability bound,
\[
\mathbb P_z\big(d(X_N(\sigma),X_N(\tau))>\varepsilon\big)
\leq\frac{4}{\varepsilon^2}
\sum_{i=1}^m
\mathbb E_z\big[(g_i(X_N(\sigma))-g_i(X_N(\tau)))^2\big].
\]
Applying (10) to this finite list gives
\[
\lim_{\delta\downarrow0}\limsup_{N\to\infty}
\sup_{z\in S_N}\sup_{\substack{\tau\leq T\\
\tau\leq\sigma\leq\tau+\delta}}
\mathbb P_z\big(d(X_N(\sigma),X_N(\tau))>\varepsilon\big)=0.
\tag{11}
\]
This explicitly proves the stopping-time increment condition, uniformly over all microscopic starting states. Compact containment is automatic because \(E\) is compact. The Aldous tightness criterion, which the contract expressly permits, now gives tightness on every finite time interval and on \(D([0,\infty),E)\) with the local \(J_1\) topology. Here the infinite-horizon assertion is the local form of that criterion, or equivalently its finite-horizon form followed by the usual diagonal compactness argument. The finitely many indices excluded by any eventual estimate do not affect tightness.

## 3. Every subsequential limit is continuous

Let
\[
j_N=\sup\{d(\pi_N(z),\pi_N(w)):A_N(z,w)>0,\ z\ne w\},
\]
with value zero for an empty set. By assumption, \(j_N\to0\). Almost surely every jump of \(X_N\) has size at most \(j_N\): the microscopic finite-state chain jumps only along positive-rate transitions.

For completeness, the relevant deterministic \(J_1\) fact follows directly from its time changes. If \(y_N\to y\) in \(J_1\) on a finite interval, take increasing continuous time changes \(\lambda_N\) fixing the endpoints such that
\[
\eta_N=\sup_t d(y_N(\lambda_N(t)),y(t))\longrightarrow0.
\]
For any \(t>0\), taking left limits preserves this bound, and hence
\[
d(y(t-),y(t))
\leq2\eta_N+
 d(y_N(\lambda_N(t)-),y_N(\lambda_N(t)))
\leq2\eta_N+\sup_s d(y_N(s-),y_N(s)).
\tag{12}
\]
Thus vanishing maximal jump size forces \(y\) to have no jumps, and a cadlag path with no jumps is continuous.

By tightness, Prokhorov's theorem and the Skorokhod representation theorem can be applied to any weakly convergent subsequence. On its coupling, local \(J_1\) convergence gives finite-interval \(J_1\) convergence at every endpoint where the limit is continuous. A cadlag path has at most countably many discontinuities, so every finite time lies strictly below some such endpoint. Apply (12) on these intervals. It follows that the limiting path is continuous everywhere, almost surely.

We will also use the elementary consequence that \(J_1\) convergence to a continuous limit is uniform on compact time intervals. Indeed, combine the time-change bound with uniform continuity of the limit on each compact interval. The assumed initial convergence and continuity of evaluation at zero show that every subsequential limit satisfies \(X(0)=x\) almost surely.

## 4. Resolvent martingale identities pass to the limit

Take any subsequential limiting law and let \(X\) denote its canonical process. It is supported on continuous paths by the preceding section. Fix \(\lambda>0\) and \(g\in C(E)\), and define
\[
u=R_\lambda g,
\qquad
u_N=R_\lambda^N(g\circ\pi_N),
\qquad
b=\lambda u-g.
\]
The Feller property and the resolvent integral give \(u,b\in C(E)\). By assumption and (2),
\[
\epsilon_N=\|u_N-u\circ\pi_N\|_\infty\longrightarrow0,
\]
\[
A_Nu_N=\lambda u_N-g\circ\pi_N,
\qquad
\|A_Nu_N-b\circ\pi_N\|_\infty\leq\lambda\epsilon_N.
\tag{13}
\]
Moreover \(\|u_N\|_\infty\leq\|g\|_\infty/\lambda\) and \(\|A_Nu_N\|_\infty\leq2\|g\|_\infty\).

Fix deterministic times \(0\leq t_1,\ldots,t_m\leq s<t\) and continuous functions \(h_1,\ldots,h_m\) on \(E\). Let
\[
B_N=\prod_{i=1}^m h_i(X_N(t_i)),
\qquad
B=\prod_{i=1}^m h_i(X(t_i)).
\]
The empty product is also allowed. The microscopic Dynkin martingale gives
\[
\mathbb E\left[B_N\left(
 u_N(Z_N(t))-u_N(Z_N(s))
 -\int_s^t A_Nu_N(Z_N(v))\,dv\right)\right]=0.
\tag{14}
\]
Replacing the microscopic functions inside this expectation by \(u(X_N)\) and \(b(X_N)\) changes it by at most
\[
\left(\prod_{i=1}^m\|h_i\|_\infty\right)
(2+\lambda(t-s))\epsilon_N.
\tag{15}
\]
This replacement is made before passing to a coupling or limit. It avoids any assumption that \(u_N\) is a function of the projection or that microscopic states can be reconstructed from a projected path.

After the replacement, the expression is a bounded functional of the projected path alone. At any continuous limiting path, convergence in \(J_1\) gives convergence of all displayed evaluations and of the time integral, by uniform convergence on \([0,t]\) and uniform continuity of the functions involved. Skorokhod representation and bounded convergence, together with (15), therefore imply
\[
\mathbb E\left[B\left(
 u(X(t))-u(X(s))-
 \int_s^t(\lambda u-g)(X(v))\,dv\right)\right]=0.
\tag{16}
\]
This holds for every such cylinder multiplier, every \(s<t\), and every \(\lambda>0\), \(g\in C(E)\).

## 5. The limiting law is uniquely determined by the semigroup

We derive the transition identities directly from (16); no separate martingale-problem uniqueness theorem is required.

Fix \(s\geq0\), a continuous cylinder multiplier \(B\) depending on times at most \(s\), a function \(g\in C(E)\), and \(\lambda>0\). With \(u=R_\lambda g\), put, for \(r\geq0\),
\[
v(r)=\mathbb E[B u(X(s+r))],
\qquad
k(r)=\mathbb E[B g(X(s+r))].
\]
Both functions are bounded and continuous, because the limiting paths are continuous and the spatial functions are bounded continuous. Equation (16) gives
\[
v(r)-v(0)=\int_0^r(\lambda v(a)-k(a))\,da.
\]
Thus \(v\) is continuously differentiable and \(v'=\lambda v-k\). Multiplying by \(e^{-\lambda r}\), integrating, and sending the upper endpoint to infinity gives
\[
\int_0^\infty e^{-\lambda r}\mathbb E[B g(X(s+r))],dr
=\mathbb E[B R_\lambda g(X(s))].
\tag{17}
\]
The terminal term vanishes because \(v\) is bounded. The resolvent definition and bounded Fubini interchange rewrite the right side as
\[
\int_0^\infty e^{-\lambda r}
\mathbb E[B P_rg(X(s))],dr.
\]
It follows, for every \(\lambda>0\), that the bounded function
\[
q(r)=\mathbb E[B(g(X(s+r))-P_rg(X(s)))]
\]
has zero Laplace transform. This function is continuous: the first term is continuous by path continuity and bounded convergence, and the second by strong continuity of the semigroup.

Here is an elementary uniqueness argument in the exact form needed. For any bounded continuous \(q\) with zero Laplace transform for all positive parameters, use \(\lambda=n+1\) and \(a=e^{-r}\) to obtain
\[
\int_0^1 a^n q(-\log a)\,da=0
\quad\text{for every integer }n\geq0.
\]
The value of the bounded integrand at zero can be assigned arbitrarily. The associated finite signed measure on \([0,1]\) annihilates all polynomials, and therefore all continuous functions by Stone–Weierstrass. It is zero. Thus \(q(-\log a)=0\) for almost every \(a\in(0,1)\), and continuity gives \(q(r)=0\) for every \(r\geq0\).

Applying this to (17) proves
\[
\mathbb E[B g(X(s+r))]
=\mathbb E[B P_rg(X(s))]
\quad\text{for every }r\geq0.
\tag{18}
\]
In particular, every joint continuous test-function moment at a finite list of deterministic times is determined recursively by \(P_t\) and the initial point \(x\): apply (18) to its last factor, and then proceed backwards through the times. The recursive functions remain continuous by the Feller property. The same recursion holds under the given Markov law \(Q_x\), so the two laws have identical finite-dimensional distributions. Products of continuous functions determine the distributions on each compact product \(E^m\), by Stone–Weierstrass.

Both laws are supported on continuous paths. On continuous-path space, evaluations at nonnegative rational times generate the Borel sigma-field: suprema of distances over compact time intervals can be taken over rational times. Consequently equality of these finite-dimensional distributions implies equality of the entire path laws. Every subsequential limiting law is therefore \(Q_x\).

Tightness and uniqueness of the subsequential limit prove
\[
\operatorname{Law}_{z_N}(X_N)
\Longrightarrow Q_x
\quad\text{in }D([0,\infty),E)
\text{ with the Skorokhod }J_1\text{ topology}.
\]
The limit is supported on \(C([0,\infty),E)\), as required.

## Dependencies and mathematical boundary

The proof uses precisely these kinds of ordinary background, all permitted by the contract:

1. Finite-state semigroup differentiation, bounded Dynkin martingales, and optional stopping at bounded stopping times.
2. Compactness of \(E\), finite nets, and Stone–Weierstrass.
3. The Aldous tightness criterion for cadlag processes in a metric state space, with compact containment. The estimate (11) verifies its stopping-time hypothesis explicitly.
4. Prokhorov's theorem and Skorokhod representation on the Polish Skorokhod space.
5. Elementary time-change properties of \(J_1\); the jump and continuity implications used here were explained directly in Section 3.
6. Bounded convergence and Fubini interchange for bounded functions against finite or exponentially weighted measures.

Approximation of the identity by the resolvent, all required generator/resolvent identities, the stopping-time estimates, and uniqueness from Laplace transforms were proved in this document. No external text was consulted. No campaign result, microscopic SIP estimate, equilibrium limit, Mosco argument, or uniform-in-time semigroup convergence was used.

The abstract contract is therefore proved independently. Its application to STATEMENT-v1 remains conditional on establishing the full-state microscopic resolvent assumption and the other contract hypotheses for the chosen microscopic and continuum systems. This reconstruction supplies none of those system-specific assertions.
