#################################### IMPORTS

import numpy             as np
import pandas            as pd
import seaborn           as sns
import matplotlib.pyplot as plt
import altair            as alt

sns.set()


#################################### EDA


# Variables numéricas
def plot_num(variable, title="", min=False, max=False, zeros=True, size=(16,4)):
    if not zeros:
        variable=variable[variable!=0]
        title += " (no zeros)"
    if min:
        variable = variable[variable >= min]
        title += " (min: "+str(min)+")"
    if max:
        variable = variable[variable <= max]
        title += " (max: "+str(max)+")"
    fig, ax = plt.subplots(figsize=size)
    ax.set_title(title, fontsize=20)
    ax2 = ax.twinx()
    sns.violinplot(variable, cut=0, palette="Set3", inner="box", ax=ax)
    sns.scatterplot(variable, y=variable.index, color="grey", linewidth=0, s=20, alpha=.3, ax=ax2).invert_yaxis()
    
def plot_num2(variable, title="", min=False, max=False, zeros=True, size=(16,4)):
    if not zeros:
        variable=variable[variable!=0]
        title += " (no zeros)"
    if min:
        variable = variable[variable >= min]
        title += " (min: "+str(min)+")"
    if max:
        variable = variable[variable <= max]
        title += " (max: "+str(max)+")"
    plt.figure(figsize=size)
    sns.violinplot(variable, cut=0, palette="Set3", inner="quart" )
    sns.stripplot(variable, color="grey", alpha=.5).set_title(title, fontsize=20);

# Variables ordinales
def plot_ord(variable, title="", min=False, max=False, zeros=True, size=(16,4)):
    if not zeros:
        variable=variable[variable!=0]
        title += " (no zeros)"
    if min:
        variable = variable[variable >= min]
        title += " (min: "+str(min)+")"
    if max:
        variable = variable[variable <= max]
        title += " (max: "+str(max)+")"
    plt.figure(figsize=size)
    sns.countplot(variable, color='royalblue').set_title(title, fontsize=20);
    
# Variables categoricas
def plot_cat(variable, title="", top=False, normalize=False, dropna=False, size=(16,4)):
    plt.figure(figsize=size)
    cats = variable.value_counts(normalize=normalize, dropna=dropna)
    if top:
        cats = cats[:top]
        title += " (top "+str(top)+")"
    sns.barplot(x=cats, y=cats.index).set_title(title, fontsize=20);