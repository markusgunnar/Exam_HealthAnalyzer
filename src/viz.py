import matplotlib.pyplot as plt
import numpy as np

def plot_histogram(_data, _mask, _bins=30, _colors=["skyblue"]):
	"""
	Takes a DataFrame of one column and plots a histogram with _bins nr of bins
	Args:
		_data (DataFrame): DataFrame where the data to plot is located
		_mask (Series): each series to plot
		_bins (int): nr of bins to use
		_colors (list): list of colors to use. One for each dataset to plot
	"""
	fig, ax = plt.subplots(figsize=(9, 5))
	ax.hist(_data[_mask], bins=_bins, color=_colors, edgecolor="black")
	ax.set_xlabel(_mask)
	ax.set_ylabel("Amount")
	ax.set_title(f"{_mask} distribution")
	ax.grid(axis="y")
	plt.show()

def plot_boxplot(_data, _cat: str, _cat_groups: list, _cat_plot: str):
	"""
	Takes a DataFrame and plots boxplots according to _cat, _cat_groups and _cat_plot
	Args:
		_data (DataFrame): DataFrame where the data is located
		_cat (str): column of _data DataFrame to plot. Ex "sex" or "primes"
		_cat_groups (list()): criteras for the _group_cat. Ex ["F", "M"] or [2, 3, 5, 7] will only look for "F" and "M" or the primes 2, 3, 5 and 7
		_cat_plot (str): what to plot the _cat_vals against. Ex "weight" or "amount"
	"""
	fig, ax = plt.subplots(figsize=(9, 5))

	x_data = [_data[_data[_cat] == v][_cat_plot] for v in _cat_groups]
	y_data = _cat_groups
	ax.boxplot(x_data,
			tick_labels=y_data,
			widths=0.8)

	ax.set_xlabel(_cat)
	ax.set_ylabel(_cat_plot)
	ax.set_title(f"{_cat_plot} per {_cat} distribution")
	plt.show()

def plot_barplot(_data, _cat: str, _cat_groups: list):
	"""
	Takes a DataFrame and plots a barplot according to _cat, _cat_groups and _cat_plot
	Args:
		_data (DataFrame): DataFrame where the data is located
		_cat (str): column of _data DataFrame to plot. Ex "sex" or "primes"
		_cat_groups (list()): criteras for the _group_cat. Ex ["F", "M"] or [2, 3, 5, 7] will only look for "F" and "M" or the primes 2, 3, 5 and 7
	"""
	fig, ax = plt.subplots(figsize=(9, 5))

	x_data = _cat_groups
	y_data = [_data[_data[_cat] == v][_cat].count() for v in _cat_groups]
	
	ax.bar(x_data, y_data, color="skyblue", alpha=0.8)
	ax.set_title(f"{_cat}s vs Non-{_cat}s")
	ax.set_xlabel(_cat)
	ax.set_ylabel("Count")
	ax.grid(axis="y")
	plt.show()

def plot_normal_pdf(_x, _m, _s):
	"""
	Calculates th y-values for the normal probability density function given x-values, mean and standard deviation.
	Args:
		_x (array-like): x-values
		_m (float): Mean
		_s (float): Standard deviation
	Returns:
		y (array-like): y-values
	"""
	_x = np.asarray(_x, dtype=float)
	if _s <= 0 or not np.isfinite(_s):
		raise ValueError("Standard deviation must be positive and finite!")
	
	norm = 1.0 / (_s * np.sqrt(2.0 * np.pi))
	z = (_x - _m) / _s
	y = norm * np.exp(-0.5 * z ** 2)
	return y