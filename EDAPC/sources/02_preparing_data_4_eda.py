"""
@File         : 02_preparing_data_4_eda.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-21 21:27:51
@Email        : cuixuanstephen@gmail.com
@Description  : 为 EDA 准备数据
"""

import pandas as pd

marketing_data = pd.read_csv(
    "DATA/marketing_campaign.csv",
    usecols=[
        "ID",
        "Year_Birth",
        "Education",
        "Marital_Status",
        "Income",
        "Kidhome",
        "Teenhome",
        "Dt_Customer",
        "Recency",
        "NumStorePurchases",
        "NumWebVisitsMonth",
    ],
)


marketing_sample1 = pd.read_csv(
    "DATA/marketing_campaign_append1.csv",
    usecols=[
        "ID",
        "Year_Birth",
        "Education",
        "Marital_Status",
        "Income",
        "Kidhome",
        "Teenhome",
        "Dt_Customer",
        "Recency",
        "NumStorePurchases",
        "NumWebVisitsMonth",
    ],
)

marketing_sample2 = pd.read_csv(
    "DATA/marketing_campaign_append2.csv",
    usecols=[
        "ID",
        "Year_Birth",
        "Education",
        "Marital_Status",
        "Income",
        "Kidhome",
        "Teenhome",
        "Dt_Customer",
        "Recency",
        "NumStorePurchases",
        "NumWebVisitsMonth",
    ],
)

appended_data = pd.concat([marketing_sample1, marketing_sample2])

marketing_sample1 = pd.read_csv("data/marketing_campaign_concat1.csv")
marketing_sample2 = pd.read_csv("data/marketing_campaign_concat2.csv")
concatenated_data = pd.concat([marketing_sample1, marketing_sample2], axis=1)


marketing_sample1 = pd.read_csv("data/marketing_campaign_merge1.csv")
marketing_sample2 = pd.read_csv("data/marketing_campaign_merge2.csv")

merged_data = pd.merge(marketing_sample1, marketing_sample2, on="ID")

sorted_data = marketing_data.sort_values("NumStorePurchases", ascending=False)

marketing_data["bins"] = pd.cut(
    x=marketing_data["NumStorePurchases"],
    bins=[0, 4, 8, 13],
    labels=["Low", "Moderate", "High"],
)

marketing_data = pd.read_csv("data/marketing_campaign.csv")
marketing_data = marketing_data[["Education", "Marital_Status", "Kidhome", "Teenhome"]]
marketing_data_duplicate = marketing_data.drop_duplicates()


marketing_data = pd.read_csv(
    "data/marketing_campaign.csv",
    usecols=["ID", "Year_Birth", "Education", "Marital_Status"],
)


marketing_data = pd.read_csv(
    "data/marketing_campaign.csv",
    usecols=["Education", "Marital_Status", "Kidhome", "Teenhome"],
)
marketing_data["Teenhome_replaced"] = marketing_data["Teenhome"].replace(
    [0, 1, 2], ["has no teen", "has teen", "has teen"]
)


marketing_data = pd.read_csv(
    "data/marketing_campaign.csv",
    usecols=["ID", "Year_Birth", "Marital_Status", "Income"],
)
marketing_data["Income"] = marketing_data["Income"].fillna(0)
marketing_data["Income_changed"] = marketing_data["Income"].astype(0)

marketing_data = pd.read_csv(
    "data/marketing_campaign.csv", usecols=["ID", "Year_Birth", "Education", "Income"]
)
marketing_data_withoutna = marketing_data.dropna(how="any")
