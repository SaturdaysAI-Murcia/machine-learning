![](https://storage.googleapis.com/kaggle-competitions/kaggle/5407/media/housesbanner.png)

<h1 align="center">Tabular data for regression</h1>
<h3 align="center">Dataset: <a href="https://www.kaggle.com/c/house-prices-advanced-regression-techniques">House prices</a></h3>



# Models

### Decission trees & Random Forest
![](https://scikit-learn.org/stable/_images/sphx_glr_plot_adaboost_regression_001.png)


# Regression metrics

### Simple metrics
| Mean Absolute Error (MAE)   |  Mean Squared Error (MSE) |
|-----------------------------|---------------------------|
| ![](img/MAE_plot.jpg)       | ![](img/MSE_plot.jpg)     |

### All metrics
|          |  Metric                        | Error plot for 5, 6, 8, 9, 27        | Best Constant    | Equivalent         |
|:--------:|--------------------------------|--------------------------------------|----------------- |--------------------|
| **MAE**  | Mean Absolute Error            | ![](img/MAE.png)                     | Median<br>(8)    |                    |
| **MSE**  | Mean Squared Error             | ![](img/MSE.png)                     | Mean<br>(11)     | RMSE,<br>R-squared |
| **MAPE** | Mean Absolute Percentage Error | ![](img/MAPE.png)                    | Weighted median<br>(6) |              |
| **MSPE** | Mean Square Percentage Error   | ![](img/MSPE.png)                    | Weighted mean<br>(6.6) |              |
| **MSLE** | Mean Square Logarithmic Error  | <img src="img/MSLE.png" width="240"> | log(mean)<br>(9.11)    | RMSLE        |
