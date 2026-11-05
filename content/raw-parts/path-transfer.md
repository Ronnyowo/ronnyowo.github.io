## C. From semigroups to path laws

**Theorem C.1 (uniform semigroup transfer).** Let \((E,d)\) be a compact metric space. Let \((P_t)_{t\ge0}\) be a conservative, strongly continuous Feller semigroup on \(C(E)\). For each \(N\), let \(Z_N\) be a continuous-time Markov chain on a finite set \(S_N\), with generator \(A_N\) and semigroup \(T_N(t)\). Let \(\pi_N:S_N\to E\), and set \(X_N=\pi_N(Z_N)\). Assume that, for every real \(g\in C(E)\) and finite \(T\),
\[
\epsilon_N(g,T):=
\sup_{0\le t\le T}\sup_{z\in S_N}
\left|T_N(t)(g\circ\pi_N)(z)-(P_tg)(\pi_N(z))\right|
\longrightarrow0.
\tag{C.1}
\]
Assume also that
\[
j_N:=\sup_{\substack{z,w\in S_N\\A_N(z,w)>0}}
d(\pi_N(z),\pi_N(w))\longrightarrow0.
\tag{C.2}
\]
Set the empty supremum to zero. For every deterministic sequence \(z_N\in S_N\) with \(\pi_N(z_N)\to x\), the laws of \(X_N\) converge in \(D([0,\infty),E)\) with the Skorokhod \(J_1\) topology. The limit has continuous paths. Its finite-dimensional distributions are those given by the initial point \(x\) and \((P_t)\). The projection \(X_N\) need not be Markov in its projected state.

*Proof.* Fix a real \(g\in C(E)\). Let \(\tau\) be a bounded stopping time for the microscopic chain, and let \(0\le h\le\delta\le1\) be deterministic. Its strong Markov property gives
\[
\begin{aligned}
&\mathbb E\left[(g(X_N(\tau+h))-g(X_N(\tau)))^2
\;\middle|\;\mathcal F_\tau\right]\\
&\quad\le \|P_hg^2-g^2\|_\infty
+2\|g\|_\infty\|P_hg-g\|_\infty\\
&\qquad\quad+\epsilon_N(g^2,1)
+2\|g\|_\infty\epsilon_N(g,1).
\end{aligned}
\tag{C.3}
\]
Indeed, expand the square. Its conditional expectation is
\[
T_N(h)(g^2\circ\pi_N)(Z_N(\tau))
-2g(X_N(\tau))T_N(h)(g\circ\pi_N)(Z_N(\tau))
+g(X_N(\tau))^2.
\]
Insert (C.1) into its first two terms. Strong continuity makes the bound in (C.3) tend to zero, uniformly for \(h\le\delta\), when first \(N\to\infty\) and then \(\delta\downarrow0\).

Choose a countable separating family \((g_j)\subset C(E)\). For each \(\varepsilon>0\), compactness of \(\{(x,y):d(x,y)\ge\varepsilon\}\) gives a finite \(J\) and \(b>0\) such that
\[
d(x,y)\ge\varepsilon
\quad\Longrightarrow\quad
\max_{j\le J}|g_j(x)-g_j(y)|\ge b.
\]
Apply (C.3) to these finitely many tests. Markov's inequality gives Aldous' stopping-time condition for the metric \(d\). Compactness gives compact containment. Thus the path laws are tight on each finite horizon. The deterministic-lag form used here is stated in Aldous, [*Weak Convergence and the General Theory of Processes*, Section 4, condition (4.2), Theorem (4.4)(ii), pages 25–26](https://www.stat.berkeley.edu/~aldous/Papers/weak-gtp.pdf). The paragraph after that theorem gives the extension to Polish state spaces.

Every limit is continuous. Under \(J_1\) convergence, time changes give uniform approximation on suitable finite horizons. This also bounds the left limits. A jump of the limit is at most \(j_N\) plus twice the uniform error. Equation (C.2) therefore excludes limit jumps.

To identify the law, fix \(0\le t_1<\cdots<t_r\) and continuous tests \(g_1,\ldots,g_r\). Define the target recursion by
\[
H_r=g_r,\qquad
H_j=g_jP_{t_{j+1}-t_j}H_{j+1}
\quad(j=r-1,\ldots,1).
\]
Each \(H_j\) is continuous by the Feller property. Repeated microscopic conditioning, starting at \(t_r\), and (C.1) show
\[
\mathbb E_{z_N}\prod_{j=1}^r g_j(X_N(t_j))
\longrightarrow(P_{t_1}H_1)(x).
\tag{C.4}
\]
At each step the transition is replaced by its target transition with a uniform error tending to zero. Multiplication by a fixed bounded test and contraction of the transition operators preserve this error bound. Continuity handles the convergent initial states.

Every subsequential limit is continuous, so evaluation at each fixed time preserves convergence along that subsequence. Products of continuous tests determine every finite-dimensional law. A continuous-path law is determined by these laws at a countable dense set of times. Thus all subsequential limits agree, and the whole sequence converges. This proves the theorem.

The argument also constructs a continuous realization of \((P_t)\) at every point that is a limit of projected initial states. It does not require target path continuity as an extra hypothesis.
