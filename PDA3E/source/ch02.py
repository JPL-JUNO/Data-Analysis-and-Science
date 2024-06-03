"""
@File         : ch02.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-06-03 16:02:07
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import numpy as np
import pandas as pd

arr = np.arange(12)
new_arr = arr.reshape(4, 3)
new_arr
arr.reshape(3, 4)
arr = np.arange(1, 10).reshape(3, 3)
arr
arr.flatten()
arr.ravel()
arr.transpose()
arr.resize(1, 9)
arr


arr1 = np.arange(1, 10).reshape(3, 3)
arr2 = 2 * arr1

arr3 = np.hstack([arr1, arr2])
arr3

arr4 = np.concatenate([arr1, arr2], axis=1)
arr4

arr5 = np.vstack((arr1, arr2))
arr5
arr6 = np.concatenate((arr1, arr2), axis=0)

arr7 = np.dstack((arr1, arr2))
arr7


arr1 = np.arange(4, 7)
arr2 = 2 * arr1
np.column_stack((arr1, arr2))

np.row_stack((arr1, arr2))


arr = np.arange(1, 10).reshape(3, 3)
np.hsplit(arr, 3)

np.vsplit(arr, 3)
np.split(arr, 3, axis=0)
np.split(arr, 3, axis=1)

arr = np.arange(1, 10).reshape(3, 3)
print("Integer Array:", arr)

arr = arr.astype(float)
print("Float Array:", arr)

print("Changed Datatype:", arr.dtype)

arr = np.arange(1, 10)
arr.tolist()


arr = np.arange(1, 5).reshape(2, 2)
arr

arr_no_copy = arr
arr_copy = arr.copy()
arr_view = arr.view()

print("Original Array: ", id(arr))
print("Assignment: ", id(arr_no_copy))
print("Deep Copy: ", id(arr_copy))
print("Shallow Copy(View): ", id(arr_view))


arr[1] = [99, 89]
print("View array:\n", arr_view)
print("Copied Array:\n", arr_copy)

arr = np.arange(0, 10)
arr[3:6]
arr[3:]
arr[-3:]
arr[2:7:2]

arr = np.arange(21, 42, 2)
print("Original Array:\n", arr)
print("After Boolean Condition:\n", arr[arr > 30])

arr = np.arange(1, 21).reshape(5, 4)
print("Original Array:\n", arr)

# Selecting 2nd and 3rd row
indices = [1, 2]
print("Selected 1st and 2nd Row:\n", arr[indices])
# Selecting 3nd and 4th row
indices = [2, 3]
print("Selected 3rd and 4th Row:\n", arr[indices])

row = np.array([1, 3])
col = np.array([0, 2])
print("Selected Sub-Array:", arr[row, col])

arr1 = np.arange(1, 5).reshape(2, 2)

arr2 = np.arange(5, 9).reshape(2, 2)
arr1 + arr2
arr1 + 3

# Create empty DataFrame
df = pd.DataFrame()
df.head()

# Create dictionary of list
data = {
    "Name": ["Vijay", "Sundar", "Satyam", "Indira"],
    "Age": [23, 45, 46, 52],
}
df = pd.DataFrame(data)
df.head()

data = [
    {"Name": "Vijay", "Age": 23},
    {"Name": "Sundar", "Age": 25},
    {"Name": "Shankar", "Age": 26},
]
# Creates DataFrame.
df = pd.DataFrame(data, columns=["Name", "Age"])
# Print dataframe header
df.head()

# Creating DataFrame using list of tuples.
data = [("Vijay", 23), ("Sundar", 45), ("Satyam", 46), ("Indira", 52)]
# Create dataframe
df = pd.DataFrame(data, columns=["Name", "Age"])
# Print dataframe header
df.head()

# Creating Pandas Series using Dictionary
dict1 = {0: "Ajay", 1: "Jay", 2: "Vijay"}
series = pd.Series(dict1)
series

# Create NumPy array
arr = np.array([51, 65, 48, 59, 68])
# Create Pandas Series
series = pd.Series(arr)
series

series = pd.Series(10, index=[0, 1, 2, 3, 4, 5])
series

df = pd.read_csv("dataset/WHO_first9cols.csv")
df.head()
country_series = df["Country"]
type(country_series)

print("Shape:", df.shape)
print("List of Columns:", df.columns)
print("Data types:", df.dtypes)

import quandl

sunspots = quandl.get("SIDC/SUNSPOTS_A")
sunspots.head()
sunspots.tail()
sunspots_filtered = sunspots[
    ["Yearly Mean Total Sunspot Number", "Definitive/Provisional Indicator"]
]
sunspots_filtered["2002-01-01":"2013-12-31"]

# Boolean Filter
sunspots[
    sunspots["Yearly Mean Total Sunspot Number"]
    > sunspots["Yearly Mean Total Sunspot Number"].mean()
]

df.describe()

df.groupby("Continent").mean(numeric_only=True)
df.groupby("Continent").mean(numeric_only=True)["Adult literacy rate (%)"]

dest = pd.read_csv("dataset/dest.csv")
tips = pd.read_csv("dataset/tips.csv")

df_inner = pd.merge(dest, tips, on="EmpNr", how="inner")
df_inner

df_outer = pd.merge(dest, tips, on="EmpNr", how="outer")
df_outer

df_right = pd.merge(dest, tips, on="EmpNr", how="right")
df_right

df_left = pd.merge(dest, tips, on="EmpNr", how="left")
df_left

df.isnull().sum()
# pd.isnull(df).sum()

df.dropna(inplace=True)
df.info()

df.fillna(0, inplace=True)

purchase = pd.read_csv("dataset/purchase.csv")
purchase.head()

pd.pivot_table(
    purchase,
    values="Number",
    index=["Weather"],
    columns=["Food"],
    aggfunc=np.sum,
)

pd.date_range("2000-01-01", periods=45, freq="D")

pd.to_datetime("1970-01-01")

pd.to_datetime(["20000101", "20000201"], format="%Y%m%d")

pd.to_datetime(["20200101", "Not a date"])
pd.to_datetime(["20200101", "Not a date"], errors="coerce")
