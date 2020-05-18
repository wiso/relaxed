__all__ = ["to_bounded_vec", "to_bounded", "to_inf_vec", "to_inf"]

# Cell
import jax
import jax.numpy as jnp

# avoid those precision errors!
jax.config.update("jax_enable_x64", True)

# [-inf, inf] -> [a,b] (vectors)
def to_bounded_vec(param, bounds):
    bounds = jnp.asarray(bounds)
    a, b = bounds[:, 0], bounds[:, 1]
    return a + (b - a) * 0.5 * (jnp.sin(param) + 1.0)


# [-inf, inf] -> [a,b]
def to_bounded(param, bounds):
    a, b = bounds
    return a + (b - a) * 0.5 * (jnp.sin(param) + 1.0)


# [-inf, inf] <- [a,b] (vectors)
def to_inf_vec(param, bounds):
    bounds = jnp.asarray(bounds)
    a, b = bounds[:, 0], bounds[:, 1]
    x = (2.0 * param - a) / (b - a) - 1.0
    return jnp.arcsin(x)


# [-inf, inf] <- [a,b]
def to_inf(param, bounds):
    a, b = bounds
    # print(f"a,b: {a,b}")
    x = (2.0 * param - a) / (b - a) - 1.0
    return jnp.arcsin(x)
