#import modules
import plotly.express as px
import pandas as pd
import streamlit as st

#import the data available in the directory
data = pd.read_excel("Locations_export_v1.0_2.csv")

st.set_page_config(layout='wide')

# Plotting Data Centers and POP Locations

fig = px.scatter_geo(data,
                    lat='latitude',
                    lon='longitude',
                    color = data.columns[0],
                    size = 'number',
                    hover_name="name",
                    title = 'InterCloud & Partners locations <br>(Hover for locations names)',
                    width=1000,
                    height=600,
                    projection="natural earth1")


st.plotly_chart(fig, use_container_width=True)