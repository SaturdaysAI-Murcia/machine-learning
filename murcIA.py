
############# PUT
############# %run ../murcIA.py
############# ON TOP OF YOUR NOTEBOOK


print("                           _____           ")
print("                          |_   _|   /\     ")
print("  _ __ ___  _   _ _ __ ___  | |    /  \    ")
print(" | '_ ` _ \| | | | '__/ __| | |   / /\ \   ")
print(" | | | | | | |_| | | | (__ _| |_ / ____ \  ")
print(" |_| |_| |_|\__ _|_|  \___|_____/_/    \_\ ")
print("                                           ")


##################################################################### IMPORTS
import platform
import datetime
import multiprocessing
import numpy      as np
import pandas     as pd
import matplotlib as mpl
import seaborn    as sns
import altair     as alt
import sklearn    as skl
import xgboost    as xgb
import lightgbm   as lgb
import torch
import fastai
# import category_encoders as ce



##################################################################### GENERAL INFO
print("🕑 Hora:  ", datetime.datetime.now().strftime("%H:%M"))
print("🗓️ Fecha: ", datetime.datetime.now().strftime("%d/%m/%Y"))
print("💻 S.O.:  ", platform.system())
print("🐍 Python:", platform.python_version())
print("🔥 CPU:   ", multiprocessing.cpu_count(), "cores")
print("🔥 GPU:   ", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No")
print("")
print("USING PACKAGES:")
print("  Numpy:     ", np.__version__)
print("  Pandas:    ", pd.__version__)
print("  Matplotlib:", mpl.__version__)
print("  Seaborn:   ", sns.__version__)
print("  Altair:    ", alt.__version__)
print("  Sklearn:   ", skl.__version__)
print("  XGBoost:   ", xgb.__version__)
print("  LightGBM:  ", lgb.__version__)
print("  Pytorch:   ", torch.__version__)
print("  Fast.ai:   ", fastai.__version__)
#print("  Category encoders:", ce.__version__)

import matplotlib.pyplot as plt

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