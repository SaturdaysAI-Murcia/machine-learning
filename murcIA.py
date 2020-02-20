
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

# General libraries
import gc
import time
import platform
import datetime
import multiprocessing
from tqdm import tqdm_notebook as tqdm
import torch

print("🕑 Hora:  ", datetime.datetime.now().strftime("%H:%M"))
print("🗓️ Fecha: ", datetime.datetime.now().strftime("%d/%m/%Y"))
print("💻 S.O.:  ", platform.system())
print("🔥 CPU:   ", multiprocessing.cpu_count(), "cores")
print("🔥 GPU:   ", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No")
print("🐍 Python:", platform.python_version())
print("")
print("PAQUETES:")
print("")

# Data libraries
import numpy             as np; print("  Numpy (np):           ", np.__version__)
import pandas            as pd; print("  Pandas (pd):          ", pd.__version__); pd.set_option('display.max_columns', 1000)
import pandas_profiling  as pp; print("  Pandas Profiling (pp):", pp.__version__)
import missingno         as ms; print("  Missingno (ms):       ", ms.__version__)
import seaborn           as sb; print("  Seaborn (sb):         ", sb.__version__); sb.set()
import altair            as at; print("  Altair (at):          ", at.__version__)
import matplotlib        as mp; print("  Matplotlib (plt):     ", mp.__version__)
import matplotlib.pyplot as plt
import umap;                    print("  UMAP (umap):          ", umap.__version__)
# ML libraries
import sklearn           as skl;print("  Sklearn (skl):        ", skl.__version__)
import xgboost           as xgb;print("  XGBoost (xgb):        ", xgb.__version__)
import lightgbm          as lgb;print("  LightGBM (lgb):       ", lgb.__version__)
from sklearn import preprocessing
from sklearn import model_selection
from sklearn import pipeline
from sklearn import ensemble
from sklearn import impute
from sklearn import compose
from sklearn import metrics

# DL libraries
import fastai
print("  Pytorch:              ", torch.__version__)
print("  Fast.ai:              ", fastai.__version__)
print("")

# Packages still not used
# import datatable         as dt
# import catboost          as cgb
# import h2o.automl        as ml_auto
# import yellowbrick       as ml_vis
# import eli5              as ml_exp
# import arviz             as av
# import category_encoders as ce
# from fbprophet import Prophet

##################################################################### FUNCIONES DISPONIBLES

print("FUNCIONES DISPONIBLES:")
print("")
print("  df = reduce_mem_usage(df)")
print("  plot_num(pandas_series)")
print("  plot_num2(pandas_series)")
print("  plot_ord(pandas_series)")
print("  plot_cat(pandas_series)")


##################################################################### LOADING DATA

# int8    Integer (-128 to 127)
# int16   Integer (-32768 to 32767)
# int32   Integer (-2147483648 to 2147483647)
# int64   Integer (-9223372036854775808 to 9223372036854775807)
# uint8   Unsigned integer (0 to 255)
# uint16  Unsigned integer (0 to 65535)
# uint32  Unsigned integer (0 to 4294967295)
# uint64  Unsigned integer (0 to 18446744073709551615)
def reduce_mem_usage(df):
    start_mem = df.memory_usage().sum() / 1024**2

    for col in df.columns:
        col_type = df[col].dtype
        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if   c_min >= np.iinfo(np.uint8).min   and c_max <= np.iinfo(np.uint8).max:  df[col] = df[col].astype(np.uint8)
                elif c_min >= np.iinfo(np.int8).min    and c_max <= np.iinfo(np.int8).max:   df[col] = df[col].astype(np.int8)
                elif c_min >= np.iinfo(np.uint16).min  and c_max <= np.iinfo(np.uint16).max: df[col] = df[col].astype(np.uint16)
                elif c_min >= np.iinfo(np.int16).min   and c_max <= np.iinfo(np.int16).max:  df[col] = df[col].astype(np.int16)
                elif c_min >= np.iinfo(np.uint32).min  and c_max <= np.iinfo(np.uint32).max: df[col] = df[col].astype(np.uint32)
                elif c_min >= np.iinfo(np.int32).min   and c_max <= np.iinfo(np.int32).max:  df[col] = df[col].astype(np.int32)
                elif c_min >= np.iinfo(np.uint64).min  and c_max <= np.iinfo(np.uint64).max: df[col] = df[col].astype(np.uint64)
                elif c_min >= np.iinfo(np.int64).min   and c_max <= np.iinfo(np.int64).max:  df[col] = df[col].astype(np.int64)
            else:
                if   c_min >= np.finfo(np.float16).min and c_max <= np.finfo(np.float16).max: df[col] = df[col].astype(np.float16)
                elif c_min >= np.finfo(np.float32).min and c_max <= np.finfo(np.float32).max: df[col] = df[col].astype(np.float32)
                elif c_min >= np.finfo(np.float64).min and c_max <= np.finfo(np.float64).max: df[col] = df[col].astype(np.float64)
        #else:
        #    df[col] = df[col].astype('category')

    end_mem = df.memory_usage().sum() / 1024**2
    percent = 100 * (start_mem - end_mem) / start_mem
    print("Memory decreased from {:.2f} MB to {:.2f} MB ({:.1f}%)".format(start_mem, end_mem, percent))
    
    return df




##################################################################### EDA

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
    sb.violinplot(variable, cut=0, palette="Set3", inner="box", ax=ax)
    sb.scatterplot(variable, y=variable.index, color="grey", linewidth=0, s=20, alpha=.3, ax=ax2).invert_yaxis()


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
    sb.violinplot(variable, cut=0, palette="Set3", inner="quart" )
    sb.stripplot(variable, color="grey", alpha=.5).set_title(title, fontsize=20);


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
    sb.countplot(variable, color='royalblue').set_title(title, fontsize=20);


# Variables categoricas
def plot_cat(variable, title="", top=False, normalize=False, dropna=False, size=(16,4)):
    plt.figure(figsize=size)
    cats = variable.value_counts(normalize=normalize, dropna=dropna)
    if top:
        cats = cats[:top]
        title += " (top "+str(top)+")"
    sb.barplot(x=cats, y=cats.index).set_title(title, fontsize=20);





##################################################################### PREPROCESSING


def preprocessor(num_feats, cat_feats):
    num_preprocessing = pipeline.Pipeline(steps=[
        ('imputer', impute.SimpleImputer(strategy='median')),
        ('encoder', preprocessing.StandardScaler())
    ])

    # preprocessing.OneHotEncoder()
    cat_preporcessing = pipeline.Pipeline(steps=[
        ('imputer', impute.SimpleImputer(strategy='constant', fill_value='missing')),
        ('encoder', preprocessing.OrdinalEncoder())
    ])

    return compose.ColumnTransformer(transformers=[
        ('num', num_preprocessing, num_feats),
        ('cat', cat_preporcessing, cat_feats)
    ])

# prep_model = pipeline.Pipeline(steps=[
#     ('preprocessor', preprocessor),
#     ('classifier', ensemble.RandomForestClassifier(n_estimators=500))
# ])

##################################################################### MODELS

