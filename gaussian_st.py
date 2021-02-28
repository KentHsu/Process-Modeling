import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from gaussian_basis import GaussianFeatures


def gaussian_regression():

    # setup sidebar for Gaussian regression
    st.sidebar.title('Dimension and Width')
    dimension = st.sidebar.slider('Adjust to change the dimension',\
                                   10, 30, value=20)
    width = st.sidebar.slider('Adjust to change the width',\
                               0.5, 5.5, value=3.0, step=0.25)


    # Gaussian regresion model
    rng = np.random.RandomState(100)
    x = 10 * rng.rand(50)
    y = 0.5 * (rng.rand(50) - 0.5)
    gauss_model = make_pipeline(GaussianFeatures(dimension, width),\
                                LinearRegression())
    gauss_model.fit(x[:, np.newaxis], y)

    xfit = np.linspace(0, 10, 1000)
    yfit = gauss_model.predict(xfit[:, np.newaxis])


    # Streamlit application
    st.title('Gaussian Function Basis Regression')
    st.header("Fitting dimension & Gaussian function width")
    st.markdown("* The more fitting dimensions we set, the worse the overfitting is.")
    st.markdown("* The shorter the width we set, the worse the overfitting is.")
    fig, ax = plt.subplots()
    plt.plot(xfit, yfit)
    plt.scatter(x, y, color='orange')
    plt.ylim(-3, 3)
    st.pyplot(fig)

