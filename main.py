import streamlit as st
import numpy as np
import plotly
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd


crime_data = pd.read_csv('crimedata.csv')
selector1 = st.sidebar.selectbox('correlation between the number of police officers and the number of crimes', ('murdPerPop', 'rapesPerPop', 'robbbPerPop', 'assaultPerPop', 'burglPerPop', 'larcPerPop', 'autoTheftPerPop', 'arsonsPerPop', 'ViolentCrimesPerPop', 'nonViolPerPop'))
df = crime_data[['PolicPerPop', selector1]]
df = df[~pd.isnull(df['PolicPerPop'])]
df = df[~pd.isnull(df[selector1])]
fig = px.scatter(df, x="PolicPerPop", y=selector1, trendline="lowess", trendline_color_override='green')
st.plotly_chart(fig, use_container_width=True)


df = crime_data[~pd.isnull(crime_data['PctPopUnderPov'])]
df = df[~pd.isnull(df['PctLess9thGrade'])]
df = df[~pd.isnull(df['PctNotHSGrad'])]
states = tuple(df['communityName'])
selector2 = st.sidebar.selectbox('correlation between number of people under the poverty level and education level by states', states)
df = crime_data[crime_data['communityName'] == selector2]
df = df[['PctPopUnderPov', 'PctLess9thGrade', 'PctNotHSGrad']]
data = dict(
    number=list(df.iloc[0]),
    stage=list(df.columns)
)
fig = px.funnel(data, x='number', y='stage')
st.plotly_chart(fig, use_container_width=True)


df = crime_data[~pd.isnull(crime_data['PctRecentImmig'])]
df = df[~pd.isnull(df['PctRecImmig5'])]
df = df[~pd.isnull(df['PctRecImmig8'])]
df = df[~pd.isnull(df['PctRecImmig10'])]
df = df[~pd.isnull(df['PctNotSpeakEnglWell'])]
states = tuple(df['communityName'])
selector3 = st.sidebar.selectbox('correlation between number of immigrantes and level of knowledge of English', states)
df = crime_data[crime_data['communityName'] == selector3]
df = df[['PctNotSpeakEnglWell', 'PctRecentImmig', 'PctRecImmig5', 'PctRecImmig8', 'PctRecImmig10']]
fig = px.bar(x=df.columns, y=df.iloc[0])
st.plotly_chart(fig, use_container_width=True)


selector4 = st.sidebar.selectbox('correlation between median family income', ('PctFam2Par', 'PersPerFam', 'PctEmploy'))
df = crime_data[['medFamInc', selector4]]
df = df[~pd.isnull(df['medFamInc'])]
df = df[~pd.isnull(df[selector4])]
fig = px.scatter(df, x="medFamInc", y=selector4, trendline="lowess", trendline_color_override='green')
st.plotly_chart(fig, use_container_width=True)


selector5 = st.sidebar.selectbox('correlation between population density and crimes', ('murdPerPop', 'rapesPerPop', 'robbbPerPop', 'assaultPerPop', 'burglPerPop', 'larcPerPop', 'autoTheftPerPop', 'arsonsPerPop', 'ViolentCrimesPerPop', 'nonViolPerPop'))
df = crime_data[['PopDens', selector5]]
df = df[~pd.isnull(df['PopDens'])]
df = df[~pd.isnull(df[selector5])]
fig = px.scatter(df, x="PopDens", y=selector5, trendline="lowess", trendline_color_override='green')
st.plotly_chart(fig, use_container_width=True)