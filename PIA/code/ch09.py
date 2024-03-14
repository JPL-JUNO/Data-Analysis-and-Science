"""
@File         : ch09.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-03-13 20:31:30
@Email        : cuixuanstephen@gmail.com
@Description  : GroupBy 对象
"""

import pandas as pd

food_data = {
    "Item": ["Banana", "Cucumber", "Orange", "Tomato", "Watermelon"],
    "Type": ["Fruit", "Vegetable", "Fruit", "Vegetable", "Fruit"],
    "Price": [0.99, 1.25, 0.25, 0.33, 3.00],
}
supermarket = pd.DataFrame(data=food_data)
supermarket

groups = supermarket.groupby("Type")
groups

groups.get_group("Fruit")
groups.get_group("Vegetable")

groups.mean(numeric_only=True)

fortune = pd.read_csv("../data/fortune1000.csv")
fortune

retailing_mask = fortune["Sector"] == "Retailing"
retail_companies = fortune[retailing_mask]
retailing_mask.head()
retail_companies["Revenues"].head()
retail_companies["Revenues"].mean()

sectors = fortune.groupby("Sector")

len(sectors)

fortune["Sector"].nunique()

sectors.size()

sectors.groups

sectors.first()

sectors.last()

sectors.nth(0)

sectors.head()

sectors.tail()

sectors.get_group("Apparel")

sectors.sum(numeric_only=True).head(3)

sectors.mean(numeric_only=True).head()

sectors["Revenues"]

sectors["Revenues"].max().head(1)
sectors["Revenues"].min().head(1)

aggregations = {"Revenues": "min", "Profits": "max", "Employees": "mean"}
sectors.agg(aggregations).head()

fortune.nlargest(5, columns="Profits")


def get_largest_row(df):
    return df.nlargest(1, "Revenues")


sectors.apply(get_largest_row).head()


def get_largest_row(df, columns="Revenues"):
    return df.nlargest(1, columns=columns)


sectors.apply(get_largest_row, columns="Profits")


def get_smallest_row(df, columns="Profits"):
    return df.nsmallest(1, columns=columns)


def get_max(df, columns):
    return df[columns].max()


def get_min(df, columns):
    return df[columns].min()


def get_value(df, columns):
    return (get_min(df, columns), get_max(df, columns))


def get_max(df, columns):
    return df[columns].max()


def get_min(df, columns):
    return df[columns].min()


sectors.apply(
    lambda x: pd.Series(
        {
            "Profits": get_max(x, columns="Profits"),
            "Revenues": get_min(x, columns="Revenues"),
        }
    )
)

sectors.apply(get_value, columns="Profits").head()

sectors_and_industry = fortune.groupby(by=["Sector", "Industry"])
sectors_and_industry.size()

sectors_and_industry.get_group(("Business Services", "Education"))

sectors_and_industry.sum(numeric_only=True).head()

sectors_and_industry["Revenues"].mean().head(5)
