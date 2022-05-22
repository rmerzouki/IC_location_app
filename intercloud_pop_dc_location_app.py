#import modules
import plotly.express as px
import pandas as pd
import streamlit as st

#import the data available in the directory
data = pd.read_excel("locations_export_v1_rm.xls")

st.set_page_config(layout='wide')

# Plotting Data Centers and POP Locations

fig = px.scatter_mapbox(data, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="name",
                        size = 'number', 
                        color = data.columns[0], 
                        zoom=3, 
                        height=600, 
                        width=1000
                       )
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},title = '<br>InterCloud & Partners locations <br>(Hover for locations names)')

st.plotly_chart(fig, use_container_width=True)