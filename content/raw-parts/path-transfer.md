## C. Transfer from resolvents to path laws

### C.1. Statement and resolvent identity

Let \((E,d)\) be a compact metric space. Let \((P_t)_{t\ge0}\) be a conservative, strongly continuous Feller semigroup on \(C(E)\). Assume that it has a continuous-path Markov realization with law \(Q_x\) for each \(x\in E\). For \(\lambda>0\) and \(g\in C(E)\), define
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

All resolvents use a positive discount. Put \(g_N=g\circ\pi_N\). Both semigroups are contractions, so their resolvents have norm at most \(1/\lambda\). Write
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

The argument is conditional on assumption 1. It does not prove that uniform resolvent assumption for the symmetric inclusion process.
