import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets


happy = pd.read_csv("http://knuth.luther.edu/~maulsy01/happy.csv")
happy = happy.drop(columns=["Unnamed: 0"])

family_by_region = happy.groupby('Region')['Family'].mean()
freedom_by_region = happy.groupby('Region')['Freedom'].mean()
dystopia_by_region = happy.groupby('Region')['Dystopia Residual'].mean()
economy_by_region = happy.groupby('Region')['Economy (GDP per Capita)'].mean()
health_by_region = happy.groupby('Region')['Health (Life Expectancy)'].mean()
trust_by_region = happy.groupby('Region')['Trust (Government Corruption)'].mean()

def f(x):
    fig,ax = plt.subplots(figsize=(35,15))
    ax.set_xlabel('Region')
    ax.set_ylabel('Mean Score')
    if x == 0:
        ax.bar(family_by_region.index.values, family_by_region)
    elif x == 1:
        ax.bar(freedom_by_region.index.values, freedom_by_region)
    elif x == 2:
        ax.bar(dystopia_by_region.index.values, dystopia_by_region)
    elif x == 3:
        ax.bar(economy_by_region.index.values, economy_by_region)
    elif x == 4:
        ax.bar(health_by_region.index.values, health_by_region)
    else:
        ax.bar(trust_by_region.index.values, trust_by_region)

category = {"Family":0, "Freedom":1, "Dystopia Residual":2, "Economy":3, "Health":4, "Trust":5}
interact(f, x=category)