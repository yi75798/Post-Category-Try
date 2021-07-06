#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
貼文類型差異檢定試作
Created on Mon Jul  5 19:18:51 2021

@author: liang-yi
"""
### 0.載入套件
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
from scipy.stats.mstats import kruskalwallis

### 1.讀取資料
df = pd.read_csv("/Users/liang-yi/Desktop/Covid19與團結效應/tsai_dealed.csv")

## 依分群篩選資料
fliter = (df["label"] == 1)
df_1 = df[fliter]

fliter = (df["label"] == 0)
df_0 = df[fliter]

### 2.依各互動數佔總反應數比例作圖
## 群體1
Like_1 = round(df_1["Likes"].sum() / df_1["Reaction"].sum(), 3)
Love_1 = round(df_1["Love"].sum() / df_1["Reaction"].sum(), 3)
Wow_1 = round(df_1["Wow"].sum() / df_1["Reaction"].sum(), 3)
Haha_1 = round(df_1["Haha"].sum() / df_1["Reaction"].sum(), 3)
Sad_1 = round(df_1["Sad"].sum() / df_1["Reaction"].sum(), 3)
Angry_1 = round(df_1["Angry"].sum() / df_1["Reaction"].sum(), 3)
Care_1 = round(df_1["Care"].sum() / df_1["Reaction"].sum(), 3)
x = [Like_1, Love_1, Wow_1, Haha_1, Sad_1, Angry_1, Care_1]
pie_label = ["Like", "Love", "Wow", "Haha", "Sad", "Angry", "Care"]
color = ["dodgerblue", "magenta", "gold", "lime", "cyan", "red", "orange"]

plt.figure(1, figsize=(7, 7))
plt.pie(x, labels= x, colors=color,
        textprops={"fontsize":14}, labeldistance=0.6, explode=(0, 0, 0.2, 0.4, 0, 0, 0))
plt.title("Category 1", {"fontsize": 18})
plt.axis("equal")
plt.legend(pie_label,loc=1)
plt.show()

## 群體0
Like_0 = round(df_0["Likes"].sum() / df_0["Reaction"].sum(), 3)
Love_0 = round(df_0["Love"].sum() / df_0["Reaction"].sum(), 3)
Wow_0 = round(df_0["Wow"].sum() / df_0["Reaction"].sum(), 3)
Haha_0 = round(df_0["Haha"].sum() / df_0["Reaction"].sum(), 3)
Sad_0 = round(df_0["Sad"].sum() / df_0["Reaction"].sum(), 3)
Angry_0 = round(df_0["Angry"].sum() / df_0["Reaction"].sum(), 3)
Care_0 = round(df_0["Care"].sum() / df_0["Reaction"].sum(), 3)
x = [Like_0, Love_0, Wow_0, Haha_0, Sad_0, Angry_0, Care_0]
pie_label = ["Like", "Love", "Wow", "Haha", "Sad", "Angry", "Care"]
color = ["dodgerblue", "magenta", "gold", "lime", "cyan", "red", "orange"]

plt.figure(1, figsize=(7, 7))
plt.pie(x, labels= x, colors=color,
        textprops={"fontsize":14}, labeldistance=0.6, explode=(0, 0, 0.2, 0.4, 0, 0, 0))
plt.title("Category 0", {"fontsize": 18})
plt.axis("equal")
plt.legend(pie_label,loc=1)
plt.show()

### 3.假設檢定
## 因為樣本分佈非常態，故採用K-W檢定兩組差異
print("----------各項互動差異顯著性----------")
print("Likes: %1.6f" % (kruskalwallis(df_0["Likes"].values, df_1["Likes"].values)[1]))
print("Angry: %1.6f" % (kruskalwallis(df_0["Angry"].values, df_1["Angry"].values)[1]))
print("Love: %1.6f" % (kruskalwallis(df_0["Love"].values, df_1["Love"].values)[1]))
print("Haha: %1.6f" % (kruskalwallis(df_0["Haha"].values, df_1["Haha"].values)[1]))
print("Wow: %1.6f" % (kruskalwallis(df_0["Wow"].values, df_1["Wow"].values)[1]))
print("Sad: %1.6f" % (kruskalwallis(df_0["Sad"].values, df_1["Sad"].values)[1]))
print("Care: %1.6f" % (kruskalwallis(df_0["Care"].values, df_1["Care"].values)[1]))

