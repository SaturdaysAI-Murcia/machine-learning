![](img/header.jpg)
<h1 align="center">Tabular data for classification</h1>
<h3 align="center">Dataset: <a href="https://www.kaggle.com/c/titanic">Titanic</a></h3>




> ### Index
>
> - Feature preprocessing
>   - [**Categorical**](#categorical-features)
>   - [**Numerical**](#numerical-features)
>   - [**Ordinal**](#ordinal-features)
>   - **Text**: *Ver sesión de NLP*
>   - **Date or Time**: *Ver sesión de series temporales*
>   - **Feature generation**
> - Models
> - Validation
> - Classification metrics
> - [**Conclussion**](#conclussion)



# Categorical features

### Label Encoding
👉 Use this encoding for **tree based models** (Random Forest, Gradient Boosting...)

![](img/label-encoding.png)

### One-hot Encoding
👉 Use this encoding for **not tree based models** (Linear models, Neural Networks, Support Vector Machines...)
![](img/one-hot-encoding.png)

## Numerical features
Números enteros o decimales: Ej: *Edad*, *medidas*, *precios*, ...

## Ordinal features
Categorias con orden. No podemos asegurar que los intervalos son iguales. Ej: *Carnet de conducir*, *nivel de educación*, *tipo de ticket*



## Feature generation: CREATIVITY + DOMOAIN KNOWLEDGE

- Si tienes el precio de la casa y los metros cuadrados, puedes añadir el precio del metro cuadrado.
- Si tines la distancia en el eje x e y, puedes añadir la distancia directa por pitagoras.
- Si tines precios, puedes añanir la parte fraccionaria pq es muy subjetiva en la gente.


## Models
| Model                 | Comment                              | Library                    | More info |
|:---------------------:|--------------------------------------|----------------------------|-----------|
| **Decission Tree**    | Simple and explicable.               | Sklearn                    |           |
| **Linear models**     | Simple and explicable.               | Sklearn                    |           |
| **Random Forest**     | Good starting point (tree enesemble) | Sklearn                    |           |
| **Gradient Boosting** | Usually the best (tree enesemble)    | XGBoost, LighGBM, Catboost |           |
| **Neural Network**    | Good if lot of data.                 | Fast.ai v2                 | [blog](https://hackernoon.com/gain-state-of-the-art-results-on-tabular-data-with-deep-learning-and-embedding-layers-a-how-to-guide-r17b36k8) |


![](https://scikit-learn.org/stable/_images/sphx_glr_plot_classifier_comparison_001.png)

## [Jeremy Howard on twitter](https://twitter.com/jeremyphoward/status/1223777020934361088): Our advice for tabular modeling

We have two approaches to tabular modelling: decision tree ensembles, and neural networks. And we have mentioned two different decision tree ensembles: random forests, and gradient boosting. Each is very effective, but each also has compromises:

### Random Forest

Are the easiest to train, because they are extremely resilient to hyperparameter choices, and require very little preprocessing. They are very fast to train, and should not overfit, if you have enough trees. But, they can be a little less accurate, especially if extrapolation is required, such as predicting future time periods

<p align="center"><img width="50%" src="img/RandomForest.png" /></p>

### Gradient Boosting

In theory are just as fast to train as random forests, but in practice you will have to try lots of different hyperparameters. They can overfit. At inference time they will be less fast, because they cannot operate in parallel. But they are often a little bit more accurate than random forests.

<p align="center"><img width="50%" src="img/GradientBoosting.png" /></p>


- 🔷: Increase parameter for overfit,  decrease for underfit.
- 🔶: Increase parameter for underfit, decrease for overfit. (regularization)

|                                      | sklearn RandomForest | XGBoost          | LightGBM         | Try |
|--------------------------------------|----------------------|------------------|------------------|-------------|
| 🔷 Number of trees                   | N_estimators         | num_round        | num_iterations   | 100         |
| 🔷 Max depth of the tree             | max_depth            | max_depth        | max_depth        | 7           |
| 🔶 Min cases per final tree leaf     | min_samples_leaf     | min_child_weight | min_data_in_leaf |             |
| 🔷 % of rows used to build the tree  |                      | subsample        | bagging_fraction | 0.8         |
| 🔷 % of feats used to build the tree | max_features         | colsample_bytree | feature_fraction |             |
| 🔷 Speed of training                 | NOT IN FOREST        | eta              | learning_rate    |             |
| 🔶                                   | NOT IN FOREST        | lambda           | lambda_l1        |             |
| 🔶                                   | NOT IN FOREST        | alpha            | lambda_l2        |             |
| Random seed                          | random_state         | seed             | _seed            |             |


### Neural Network

Take the longest time to train, and require extra preprocessing such as normalisation; this normalisation needs to be used at inference time as well. They can provide great results, and extrapolate well, but only if you are careful with your hyperparameters, and are careful to avoid overfitting.

<p align="center"><img width="80%" src="img/NeuralNet.png" /></p>


# Validation

### Cross Validation
![](img/cross-validation.png)


# Conclussion

We suggest starting your analysis with a random forest. This will give you a strong baseline, and you can be confident that it's a reasonable starting point. You can then use that model for feature selection and partial dependence analysis, to get a better understanding of your data.

From that foundation, you can try Gradient Boosting and Neural Nets, and if they give you significantly better results on your validation set in a reasonable amount of time, you can use them.


<table>
  <tr>
    <tD></tD>
    <tD>
      <h4>Tree based models</h4>
      <ul>
        <li>Decission tree</li>
        <li>Random Forest</li>
        <li>Extra trees</li>
        <li>Adaboost</li>
        <li>Gradient Boosting</li>
        <li>XGBoost</li>
        <li>LightGBM</li>
        <li>CatBoost</li>
      </ul>
    </tD>
    <td>
      <h4>No-tree based models</h4>
      <ul>
        <li>Linear Models</li>
        <li>Neural Networks</li>
        <li>K-Nearest Neighbors</li>
        <li>Suport Vector Machines</li>
      </ul>
    </td>
  </tr>
  <tr>
    <th>Categorical<br>Ordinal</th>
    <td>
      <ul>
        <li>Label encoding</li>
        <li>Frequency encoding</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>One hot encoding</li>
        <li>Embedding</li>
      </ul>
    </td>
  </tr>
  <tr>
    <th>Numerical</th>
    <td>Nothing</td>
    <td>
      <ul>
        <li>MinMaxScaler</li>
        <li>StandarScaler</li>
        <li>Skewed?
          <ul>
            <li>np.log(1+x)</li>
            <li>np.sqrt(x+2/3)</li>
          </ul>
        </li>
      </ul>
    </td>
  </tr>
</table>


# Example code

```python
##################################################### Imports
import pandas            as pd
import category_encoders as ce

from sklearn import preprocessing
from sklearn import impute
from sklearn import compose
from sklearn import pipeline
from sklearn.model_selection import train_test_split
from sklearn.ensemble        import RandomForestClassifier


##################################################### Numerical variables
num_encoder   = preprocessing.StandardScaler
# num_encoder = preprocessing.MinMaxScaler
# num_encoder = preprocessing.minmax_scale
# num_encoder = preprocessing.MaxAbsScaler
# num_encoder = preprocessing.RobustScaler
# num_encoder = preprocessing.Normalizer
# num_encoder = preprocessing.QuantileTransformer
# num_encoder = preprocessing.PowerTransformer

num_transformer = pipeline.Pipeline(steps=[
    ('imputer', impute.SimpleImputer(strategy='median')),
    ('encoder', num_encoder())
])
    
##################################################### Categorial variables
cat_encoder   = ce.OrdinalEncoder()
# cat_encoder = ce.OneHotEncoder()
# cat_encoder = ce.BinaryEncoder()
# cat_encoder = ce.TargetEncoder()
# cat_encoder = ce.CatBoostEncoder()
# cat_encoder = ce.BackwardDifferenceEncoder()
# cat_encoder = ce.BaseNEncoder()
# cat_encoder = ce.HashingEncoder()
# cat_encoder = ce.HelmertEncoder()
# cat_encoder = ce.JamesSteinEncoder()
# cat_encoder = ce.LeaveOneOutEncoder()
# cat_encoder = ce.MEstimateEncoder()
# cat_encoder = ce.SumEncoder()
# cat_encoder = ce.PolynomialEncoder()
# cat_encoder = ce.WOEEncoder()

cat_transformer = pipeline.Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('encoder', cat_encoder())
])

##################################################### Do the preprocessing
preprocessor = compose.ColumnTransformer(transformers=[
    ('num', numeric_transformer, numeric_features),
    ('cat', categorical_transformer, categorical_features)
])

##################################################### Train the model
pipe = pipeline.Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=500))
])

model = pipe.fit(X_train, y_train)

##################################################### Evaluate the model
y_pred = model.predict(X_test)
print(f1_score(y_test, y_pred, average='macro'))
```
