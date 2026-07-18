# Numerically Stable Sigmoid
## The problem

`float64` can represent values up to ~1.8e308. `e^x` crosses that ceiling at:

```
e^x ≈ 1.8e308  →  x ≈ 709.78

```

So `np.exp(710)` returns `inf`, and once `inf` enters the formula, gradients collapse to `0` (or `nan`). Training dies silently.
## Why both "obvious" forms break

Form

Safe when z is

Breaks when z is

`1 / (1 + exp(-z))`

small or **positive**

very **negative** (exp(-z) overflows)

`1 / (1 + exp(+z))`

small or **negative**

very **positive** (exp(+z) overflows)

No single algebraic form covers both tails.
## The fix: branch on sign

Always exponentiate a **non-positive** number (exp of that is ∈ (0, 1] — safe).

```python
def sigmoid(z):
    return np.where(z &gt;= 0,
                    1.0 / (1.0 + np.exp(-z)),
                    np.exp(z) / (1.0 + np.exp(z)))

```

The two branches are algebraically identical (multiply top/bottom of the second by `exp(-z)`).
## In practice

Just use SciPy:

```python
from scipy.special import expit
yhat = expit(z)

```
## The general principle

> Any time you compute `exp`, ask: can the exponent blow up? If yes, subtract a constant large enough to keep it non-positive. The constant cancels algebraically but keeps you in safe numeric territory.

Same trick shows up in:

- **Softmax:** subtract `max(z)` before `exp` → `exp(z - max(z))` ≤ 1
- **Log-sigmoid:** `log(σ(z))` = `-log(1 + exp(-|z|)) - max(z, 0)` (avoids both `log(0)` and overflow)
- **Log-softmax / log-sum-exp:** subtract `max` before exponentiating