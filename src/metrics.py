import numpy as np
from scipy import stats

def normal_ci95(_sample) -> tuple:
		"""
		Calculates the 95% confidence interval for the mean using the normal approximation method.
		Bounds: mean ± 1.96 * (std / sqrt(n))
		Args:
			_x (array-like): Sample data
		Returns:
			tuple: lower bound, higher bound, sample mean, sample std
		"""
		_sample = np.asarray(_sample, dtype=float)
		mean = float(np.mean(_sample))
		std = float(np.std(_sample, ddof=1))
		z_crit = 1.96
		error = z_crit * (std / np.sqrt(len(_sample)))
		return float(mean - error), float(mean + error), float(mean), float(std)

def bootstrap_ci95(_sample, _resample_size=5000, _confidence=0.95) -> tuple:
	"""
	Calculates the 95% confidence interval for the mean using the normal approximation method.
	Bounds: mean ± 1.96 * (std / sqrt(n))
	Args:
		_x (array-like): Sample data
	Returns:
		tuple: lower bound, higher bound, sample mean, sample std
	"""
	_sample = np.asarray(_sample, dtype=float)
	_sample_size = len(_sample)
	boot_means = np.empty(_resample_size)
	for i in range(_resample_size):
		boot_sample = np.random.choice(_sample, size=_sample_size)
		boot_means[i] = np.mean(boot_sample)

	alpha = (1 - _confidence) / 2.0
	lo, hi = np.percentile(boot_means, [100.0*alpha, 100.0*(1.0 - alpha)])
	return float(lo), float(hi), float(_sample.mean()), float(_sample.std())

def sample_mean(_sample) -> tuple:
	"""
	Calculates and returns the mean of the given sample
	Args:
		_data (DataFrame): Sample to take mean of
	Returns:
		sample mean (float): the mean of the given sample
	"""
	return np.mean(np.random.choice(_sample, size=len(_sample), replace=False))

def standard_t_test(_group_a, _group_b, _tail) -> tuple:
	"""
	Calculates and returns the t and p-values using a two-sample t-test given two groups and tail
	Args:
		_group_a (DataFrame): group A
		_group_b (DataFrame): group B
		_tail (str): less, greater, two-sided
	Returns:
		t-stat, p-value (tuple): t and p-value from the t-test
	"""
	t_stat, p_val = stats.ttest_ind(_group_a, _group_b, equal_var=True, alternative=_tail)
	return (float(t_stat), float(p_val))


