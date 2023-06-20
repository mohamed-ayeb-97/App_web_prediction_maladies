import streamlit as st
import pandas as pd
import openpyxl
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

def page4():

    st.write("* **Mean_Radius:** mean of distances from center to points on the perimeter")
    st.write("* **Mean_Texture:** standard deviation of gray-scale values")
    st.write("* **Mean_Perimeter:** mean size of the core tumor")
    st.write("* **Mean_Area:** mean area of the core tumor")
    st.write("* **Mean_Smoothness:** mean of local variation in radius lengths")
    st.write("* **Diagnosis:** The diagnosis of breast tissues (1 = malignant, 0 = benign) where malignant denotes that the disease is harmful")

    @st.cache
    def get_dataset(name):
        if name == 'Cancer Du Sein':
            df = pd.read_excel('Data/Breast_cancer.xlsx', engine= 'openpyxl')
            df.reset_index(inplace=True)
        return df

    data_load_state = st.text("Load Data...")
    df = get_dataset('Cancer Du Sein')
    data_load_state.text("Loading Data...Done!")

    st.subheader('Raw Data')
    st.write(df.head())


    df1 = df

    # split the data
    x = df1.iloc[:, 0:5].values
    y = df1.iloc[:, -1].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=123)

    # get the feature input

    def get_user_input():
        mean_radius = st.sidebar.number_input('mean_radius', 6.981, 28.11, 13.00)
        mean_texture = st.sidebar.number_input('mean_texture', 9.71, 39.28, 10.01)
        mean_perimeter = st.sidebar.number_input('mean_perimeter', 43.79, 188.5, 100.0)
        mean_area = st.sidebar.number_input('mean_area', 143.5, 2501.0, 712.0)
        mean_smoothness = st.sidebar.number_input('mean_smoothness', 0.05263, 0.1634, 0.0666)


        # store a dict into a variable
        user_data = {'mean_radius': mean_radius, 'mean_texture': mean_texture,
                     'mean_perimeter': mean_perimeter,
                     'mean_area': mean_area, 'mean_smoothness': mean_smoothness
 }

        # transform the data into a data frame
        features = pd.DataFrame(user_data, index=[0])
        return features

    scaler = StandardScaler()
    x_train_scale = scaler.fit_transform(x_train)
    x_test_scale = scaler.transform(x_test)
    logit_model = LogisticRegression()
    logit_model.fit(x_train_scale, y_train)
    x_pred = logit_model.predict(x_test_scale)
    res = logit_model.score(x_test_scale, y_test)

 #   rf = RandomForestClassifier(n_estimators=5000, max_depth=5, random_state=33)


    # store the user input into a variable
    user_input = get_user_input()

    # set a subheader
    st.subheader('User input : ')
    st.write(user_input)

    # create and train the model
  #  rf.fit(x_train, y_train)

    # show the model metrics
    st.subheader('model test accuracy score :')
    st.write(str(res * 100) + '%')
    #st.write("84.65%")

    # store the model prediction in a varibale
    #pred = rf.predict(user_input)
    pred = logit_model.predict(user_input)
    # set a subheader and display the classification
    st.subheader('classification :')
    st.write(pred)
