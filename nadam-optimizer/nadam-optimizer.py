import numpy as np

def nadam_step(w: list, m: list, v: list, grad: list, lr: float = 0.002, beta1: float = 0.9, beta2: float = 0.999, eps: float = 1e-8) -> dict:
    """
    Returns a dictionary with new_w, new_m, and new_v.
    """
    w = np.asarray(w, dtype=float)
    m = np.asarray(m, dtype=float)
    v = np.asarray(v, dtype=float)
    grad = np.asarray(grad, dtype=float)

    m_t = (beta1 * m) + ((1.0-beta1)*grad)
    v_t = (beta2 * v) + ((1.0-beta2)*(grad**2))

    m_hat = beta1*m_t + ((1.0-beta1)*grad)

    w_t = w - lr*(m_hat / (np.sqrt(v_t) + eps))

    sol = { "new_w": w_t, "new_m": m_t, "new_v": v_t }

    return sol