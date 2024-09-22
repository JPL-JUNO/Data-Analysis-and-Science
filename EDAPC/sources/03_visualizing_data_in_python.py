"""
@File         : 03_visualizing_data_in_python.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-09-22 11:44:10
@Email        : cuixuanstephen@gmail.com
@Description  : 使用 Python 进行数据可视化
"""

import pandas as pd

houseprices_data = pd.read_csv(
    "DATA/HousingPricesData.csv", usecols=["Zip", "Price", "Area", "Room"]
)

houseprices_data["PriceperSqm"] = houseprices_data["Price"].div(
    houseprices_data["Area"]
)

import matplotlib.pyplot as plt

houseprices_sorted = houseprices_data.sort_values("Price", ascending=False)

plt.figure(figsize=(12, 6))
x = houseprices_sorted["Zip"].iloc[0:10]
y = houseprices_sorted["Price"].iloc[0:10]
plt.bar(x, y)
plt.show()

plt.figure(figsize=(12, 6))
plt.bar(x, y)
plt.title(label="Top 10 Areas with the highest house prices", fontsize=15)
plt.xlabel(xlabel="Zip code", fontsize=12)
plt.xticks(fontsize=10)
plt.ylabel(ylabel="House prices in millions", fontsize=12)
plt.yticks(fontsize=10)
plt.show()


fig, ax = plt.subplots(figsize=(12, 6))
y1 = houseprices_sorted["PriceperSqm"].iloc[0:10]

plt.subplot(1, 2, 1)
plt.bar(x, y)
plt.xticks(fontsize=17)
plt.ylabel("House prices in millions", fontsize=25)
plt.yticks(fontsize=20)
plt.title("Top 10 Areas with the highest house prices", fontsize=25)

plt.subplot(1, 2, 2)
plt.bar(x, y1)
plt.xticks(fontsize=17)
plt.ylabel("House prices per sqm", fontsize=25)
plt.yticks(fontsize=20)
plt.title("Top 10 Areas with the highest house prices per sqm", fontsize=25)
plt.show()

import seaborn as sns

plt.figure(figsize=(12, 6))
data = houseprices_sorted[0:10]
ax = sns.barplot(data=data, x="Zip", y="Price")
ax.set_xlabel("Zip code", fontsize=15)
ax.set_ylabel("House prices in millions", fontsize=15)
ax.set_title("Top 10 Areas with the highest house prices", fontsize=20)

fig, ax = plt.subplots(1, 2, figsize=(40, 18))
sns.set_theme(font_scale=3)
ax1 = sns.barplot(data=data, x="Zip", y="Price", ax=ax[0])
ax1.set_xlabel("Zip code")
ax1.set_ylabel("House prices in millions")
ax1.set_title("Top 10 Areas with the highest house prices")

ax2 = sns.barplot(data=data, x="Zip", y="PriceperSqm", ax=ax[1])
ax1.set_xlabel("Zip code")
ax1.set_ylabel("House price per sqm")
ax1.set_title("Top 10 Areas with the highest house price per sqm")

from plotnine import ggplot, aes, geom_bar, scale_x_discrete, theme, labs, element_text

chart_data = houseprices_data[0:10]
(
    ggplot(chart_data, aes(x="Zip", y="Price"))
    + geom_bar(stat="identity")
    + labs(
        y="House prices in millions",
        x="Zip code",
        title="Top 10 Areas with the highest house prices",
    )
    + scale_x_discrete(limits=chart_data["Zip"].tolist())
    + theme(
        figure_size=(16, 8),
        axis_title=element_text(face="bold", size=12),
        axis_text=element_text(face="italic", size=8),
        plot_title=element_text(face="bold", size=12),
    )
)


from bokeh.plotting import figure, show
import bokeh.plotting as bk_plot

# from bokeh.io import output_notebook
# output_notebook()

data = houseprices_sorted[0:10]
fig = figure(
    x_range=data["Zip"],
    plot_width=700,
    plot_height=500,
    # Addition information
    title="Top 10 Areas with the highest house prices",
    x_axis_label="Zip code",
    y_axis_label="House prices in millions",
)
fig.vbar(x=data["Zip"], top=data["Price"], width=0.9)
fig.xaxis.axis_label_text_font_size = "15pt"
fig.xaxis.major_label_text_font_size = "10pt"
fig.yaxis.axis_label_text_font_size = "15pt"
fig.yaxis.major_label_text_font_size = "10pt"
fig.title.text_font_size = "15pt"
show(fig)


p1 = figure(
    x_range=data["Zip"],
    plot_width=480,
    plot_height=400,
    title="Top 10 Areas with the highest house prices",
    x_axis_label="zip code",
    y_axis_label="House prices in millions",
)
p1.vbar(x=data["Zip"], top=data["Price"], width=0.9)
p2 = figure(
    x_range=data["Zip"],
    plot_width=480,
    plot_height=400,
    title="Top 10 Areas with the highest house prices per sqm",
    x_axis_label="Zip code",
    y_axis_label="House prices per sqm",
)
p2.vbar(x=data["Zip"], top=data["PriceperSqm"], width=0.9)
gp = bk_plot.gridplot(children=[[p1, p2]])
bk_plot.show(gp)
