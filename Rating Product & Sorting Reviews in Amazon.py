
# PROJE: Rating Product & Sorting Reviews in Amazon

import pandas as pd
import math
import scipy.stats as st

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# Reading the Data Set and Calculating the Average Score of the Product

df = pd.read_csv("Miuul_Measurement/Datasets/amazon_review.csv")
df.head(100)
df.info()
df.describe()
df["overall"].mean()  # 4.587589013224822

df["total_vote"].sort_values(ascending=False).head(20)

# Calculating the Weighted Score Average by Date

df["reviewTime"] = pd.to_datetime(df["reviewTime"])


def time_based_weighted_average(dataframe, w1=28, w2=26, w3=24, w4=22):
    return dataframe.loc[df["day_diff"] <= 30, "overall"].mean() * w1 / 100 + \
        dataframe.loc[(dataframe["day_diff"] > 30) & (dataframe["day_diff"] <= 90), "overall"].mean() * w2 / 100 + \
        dataframe.loc[(dataframe["day_diff"] > 90) & (dataframe["day_diff"] <= 180), "overall"].mean() * w3 / 100 + \
        dataframe.loc[(dataframe["day_diff"] > 180), "overall"].mean() * w4 / 100


time_based_weighted_average(df)  # 4.6987161061560725


# Displaying the Product on the Product Detail Page and Determining 20 Reviews

df["helpful_no"] = df["total_vote"] - df["helpful_yes"]

# Calculating score_pos_neg_diff, score_average_rating and wilson_lower_bound Scores and Adding them to the Data


def score_up_down_diff(up, down):
    return up - down


def score_average_rating(up, down):
    if up + down == 0:
        return 0
    return up / (up + down)


def wilson_lower_bound(up, down, confidence=0.95):
    n = up + down
    if n == 0:
        return 0
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    phat = 1.0 * up / n
    return (phat + z * z / (2 * n) - z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)) / (1 + z * z / n)


df["score_up_down_diff"] = df.apply(lambda x: score_up_down_diff(x["helpful_yes"],x["helpful_no"]),axis=1)
df["score_average_rating_score"] = df.apply(lambda x: score_average_rating(x["helpful_yes"],x["helpful_no"]), axis=1)
df["wilson_review_score"] = df.apply(lambda x: wilson_lower_bound(x["helpful_yes"], x["helpful_no"]))

# Listing 20 review 

df.sort_values("wilson_review_score",ascending=False).head(20)








