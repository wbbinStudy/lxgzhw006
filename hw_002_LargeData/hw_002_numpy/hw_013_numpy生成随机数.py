"""
正太分布 中间大两边小
均匀分布 每个位置上的概率都一样

"""
import numpy as np

"""
    randint(low, high=None, size=None, dtype='l')
    
            Return random integers from `low` (inclusive) to `high` (exclusive).
    
            Return random integers from the "discrete uniform" distribution of
            the specified dtype in the "half-open" interval [`low`, `high`). If
            `high` is None (the default), then results are from [0, `low`).
    
            Parameters
            ----------
            low : int
                Lowest (signed) integer to be drawn from the distribution (unless
                ``high=None``, in which case this parameter is one above the
                *highest* such integer).
            high : int, optional
                If provided, one above the largest (signed) integer to be drawn
                from the distribution (see above for behavior if ``high=None``).
            size : int or tuple of ints, optional
                Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
                ``m * n * k`` samples are drawn.  Default is None, in which case a
                single value is returned.
            dtype : dtype, optional
                Desired dtype of the result. All dtypes are determined by their
                name, i.e., 'int64', 'int', etc, so byteorder is not available
                and a specific precision may have different C types depending
                on the platform. The default value is 'np.int'.
    
                .. versionadded:: 1.11.0
    
            Returns
            -------
            out : int or ndarray of ints
                `size`-shaped array of random integers from the appropriate
                distribution, or a single such random int if `size` not provided.
    
            See Also
            --------
            random.random_integers : similar to `randint`, only for the closed
                interval [`low`, `high`], and 1 is the lowest value if `high` is
                omitted. In particular, this other one is the one to use to generate
                uniformly distributed discrete non-integers.
    
            Examples
            --------
            >>> np.random.randint(2, size=10)
            array([1, 0, 0, 0, 1, 1, 0, 0, 1, 0])
            >>> np.random.randint(1, size=10)
            array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    
            Generate a 2 x 4 array of ints between 0 and 4, inclusive:
    
            >>> np.random.randint(5, size=(2, 4))
            array([[4, 0, 2, 1],
                   [3, 2, 2, 0]])

"""
t1 = np.random.randint(10, 20, (4, 5))
"""
创建一个四行五列的随机数组,取值为10-20之间的随机值
[[11 18 18 14 16]
 [10 15 12 19 19]
 [16 13 18 17 19]
 [16 16 17 10 18]]
"""
print(t1)
"""
.uniform 产生均匀分布的数组
.normal 正态分布
.seed 随机种子
"""
"""
seed(seed=None)
    
Seed the generator.

This method is called when `RandomState` is initialized. It can be
called again to re-seed the generator. For details, see `RandomState`.

Parameters
----------
seed : int or 1-d array_like, optional
    Seed for `RandomState`.
    Must be convertible to 32 bit unsigned integers.

See Also
--------
RandomState
"""
np.random.seed(10)  # 让每次产生的随机种子都一样
t2 = np.random.randint(0, 20, (3, 3))
print(t2)
"""
添加随机种子以后,结果总是一样的
[[ 9  4 15]
 [ 0 17 16]
 [17  8  9]]
"""
