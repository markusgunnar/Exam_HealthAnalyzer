import pandas as pd, matplotlib.pyplot as plt, numpy as np

class HealthAnalyzer:
	def __init__(self) -> None:
		self.df = pd.DataFrame
		self.mask = ["age", "weight", "height", "systolic_bp", "cholesterol"]

	def read_csv(self, _path: str) -> None:
		try:
			self.df = pd.read_csv(_path)
			print(f"File '{_path}' read successfully!")
		except FileNotFoundError:
			print(f"The file '{_path}' was not found!")

	def mean(self, _mask = None) -> pd.DataFrame:
		"""
		Returns the mean of given mask as a DataFrame if a list of mask
		values was passed. Otherwise returns mean as float
		Args:
			_mask (str): The mask to return mean for
		Returns:
			- a (DataFrame) - multiple mask strings
			- b (float) - one mask string
		"""
		_mask = self.mask if _mask is None else _mask
		if type(_mask) is str:
			return float(self.df[_mask].mean())
		else:
			return self.df[_mask].mean()
	
	def median(self, _mask = None) -> pd.DataFrame:
		"""
		Returns the median of given mask as a DataFrame if a list of mask
		values was passed. Otherwise returns median as float
		Args:
			_mask (str): The mask to return median for
		Returns:
			- a (DataFrame) - multiple mask strings
			- b (float) - one mask string
		"""
		_mask = self.mask if _mask is None else _mask
		if type(_mask) is str:
			return float(self.df[_mask].median())
		else:
			return self.df[_mask].median()
	
	def min(self, _mask = None) -> pd.DataFrame:
		"""
		Returns the min of given mask as a DataFrame if a list of mask
		values was passed. Otherwise returns min as float
		Args:
			_mask (str): The mask to return min for
		Returns:
			- a (DataFrame) - multiple mask strings
			- b (float) - one mask string
		"""
		_mask = self.mask if _mask is None else _mask
		if type(_mask) is str:
			return float(self.df[_mask].min())
		else:
			return self.df[_mask].min()
	
	def max(self, _mask = None) -> pd.DataFrame:
		"""
		Returns the max of given mask as a DataFrame if a list of mask
		values was passed. Otherwise returns max as float
		Args:
			_mask (str): The mask to return max for
		Returns:
			- a (DataFrame) - multiple mask strings
			- b (float) - one mask string
		"""
		_mask = self.mask if _mask is None else _mask
		if type(_mask) is str:
			return float(self.df[_mask].max())
		else:
			return self.df[_mask].max()
	
	def std(self, _mask = None) -> pd.DataFrame:
		"""
		Returns the std of given mask as a DataFrame if a list of mask
		values was passed. Otherwise returns std as float
		Args:
			_mask (str): The mask to return std for
		Returns:
			- a (DataFrame) - multiple mask strings
			- b (float) - one mask string
		"""
		_mask = self.mask if _mask is None else _mask
		if type(_mask) is str:
			return float(self.df[_mask].std())
		else:
			return self.df[_mask].std()

	def desc_analysis(self):
		"""
		Returns a DataFrame containing the mean, median, min and max
		of the masked columns
		Returns:
			temp_df (DataFrame): DataFrame containg a descriptive analysis
		"""
		temp_df = pd.DataFrame({
			"Mean": self.mean(),
			"Median": self.median(),
			"Min": self.min(),
			"Max": self.max(),
			"Std": self.std()
		})

		return temp_df

	def cat(self, _category: str) -> pd.DataFrame:
		"""
		Returns the chosen category from the DataFrame
		Args:
			_category (str): Chosen category to return
		Returns:
			self.df["_category"] (DataFrame): The column corresponding to the category argument
		"""
		return self.df[_category]

	def compare_sick(self):
		"""
		Compares the sickness rate between _a to _b
		"""
		actual_sick = len(self.df[self.df["disease"] == 1])
		actuaL_not_sick = len(self.df) - actual_sick
		sick_rate = actual_sick / len(self.df)

		return sick_rate

	def simulate_data(self):
		"""
		Simulates _n number of rows with the desc_analysis data to keep the mean, median, min, max and std on average
		"""
		pass

	def data(self) -> pd.DataFrame:
		"""
		Returns the loaded DataFrame
		Returns:
			self.df (DataFrame): The loaded DataFrame
		"""
		return self.df