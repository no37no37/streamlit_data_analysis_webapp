
# Imports

import streamlit as st
import pandas as pd
import seaborn as sns

# Title and Subheader
st.title("Data Analysis")
st.subheader("Data Analysis Using Python and Streamlit")

# Upload Dataset
upload = st.file_uploader("Upload your Dataset(In CSV Format)")
if upload is not None:
    data = pd.read_csv(upload)

# Show Dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())


# Check Datatype of Each Column
if upload is not None:
    if st.checkbox("DataType of Each Column"):
        st.text("DataTypes")
        st.write(data.dtypes)



# Find Shape of our Dataset (Number oF Rows and Number of Columns)
if upload is not None:
    data_shape = st.radio("What Dimension Do You Want to Check ?",('Rows','Columns'))

    if data_shape == 'Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape == 'Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])

# Find Null Values in the Dataset
if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox("Null Values in The Dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("Congratulations!!!, No Missing Values")

# Find Duplicate Values in the Dataset
if upload is not None:
    test=data.duplicated().any()
    if test == True:
        st.warning("This Dataset Contains Some Duplicated Values")
        dup=st.selectbox("Do You Want to Remove Duplicate Values?" \
                         ("Select One","Yes","No"))
        if dup == "Yes":
            data=data.drop_duplicates()
            st.text("Duplicate Values are Removed")
        if dup == "No":
            st.text("Ok No Problem")
    


# Get Overall Statistics
if upload is not None:
    if st.checkbox("Summary of The Dataset"):
        st.write(data.describe(include='all'))

# About Selection
if st.button("About App"):
    st.text("Built with Streamlit")
    st.text("Quick Data Analysis")

# By
if st.button("By"):
    st.success("Leon Jose")