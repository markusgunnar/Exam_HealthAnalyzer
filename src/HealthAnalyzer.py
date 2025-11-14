import pandas as pd, matplotlib.pyplot as plt, numpy as np

class HealthAnalyzer:
	def __init__(self) -> None:
		"""
		Initializes a DataFrame and a default mask that is used.
		"""
		self.df = pd.DataFrame
		self.mask = ["age", "weight", "height", "systolic_bp", "cholesterol"]

	def read_csv(self, _path: str) -> None:
		"""
		Reads a .csv file and loads it to self.df given a path
		Args:
			_path (str): path to .csv file
		"""
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

	def desc_analysis(self) -> pd.DataFrame:
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

	def sick_rate(self, _data) -> float:
		"""
		Returns the rate of sick people
		Returns:
			sick_rate (float): the percentage of sick people
		"""
		sick = len(_data[_data["disease"] == 1])
		sick_rate = sick / len(_data)

		return sick_rate
	
	def male_rate(self, _data) -> float:
		"""
		Returns the rate of males
		Returns:
			male_rate (float): the percentage of male people
		"""
		males = len(_data[_data["sex"] == "M"])
		male_rate = males / len(_data)

		return male_rate
	
	def smoker_rate(self, _data) -> float:
		"""
		Returns the rate of smokers
		Returns:
			smoker_rate (float): the percentage of smoker people
		"""
		smokers = len(_data[_data["smoker"] == "Yes"])
		smoker_rate = smokers / len(_data)

		return smoker_rate

	def simulate_data(self, _nr) -> pd.DataFrame:
		"""
		Simulates _n number of rows with the desc_analysis data to keep the mean, median, min, max and std on average
		Args:
			_nr (int): number of simulated people to make
		Returns:
			sim_df (DataFrame): Simulated DataFrame containing _nr of people
		"""
		sim_df = pd.DataFrame()
		sim_df["id"] = range(1, _nr + 1)
		sim_df["age"] = np.random.normal(self.df["age"].mean(), self.df["age"].std(), _nr).round().astype(int)
		sim_df["sex"] = np.random.choice(["M", "F"], _nr, p=[self.male_rate(self.data()), 1 - self.male_rate(self.data())])
		sim_df["weight"] = np.random.normal(self.df["weight"].mean(), self.df["weight"].std(), _nr).round(2).astype(float)
		sim_df["height"] = np.random.normal(self.df["height"].mean(), self.df["height"].std(), _nr).round(2).astype(float)
		sim_df["systolic_bp"] = np.random.normal(self.df["systolic_bp"].mean(), self.df["systolic_bp"].std(), _nr).round(2).astype(float)
		sim_df["cholesterol"] = np.random.normal(self.df["cholesterol"].mean(), self.df["cholesterol"].std(), _nr).round(2).astype(float)
		sim_df["smoker"] = np.random.choice(["Yes", "No"], _nr, p=[self.smoker_rate(self.data()), 1 - self.smoker_rate(self.data())])
		sim_df["disease"] = np.random.choice([1, 0], _nr, p=[self.sick_rate(self.data()), 1 - self.sick_rate(self.data())])

		return sim_df

	def data(self) -> pd.DataFrame:
		"""
		Returns the loaded DataFrame
		Returns:
			self.df (DataFrame): The loaded DataFrame
		"""
		return self.df