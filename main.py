import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('india.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

cols = df.columns[5:]

st.sidebar.title('India Ka Data Viz')

selected_state = st.sidebar.selectbox('Select a State', list_of_states)

primary = st.sidebar.selectbox('Select Primary Parameter', sorted(cols))
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(cols))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represents primary parameter')
    st.text('Color represents secondary parameter')
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df,lat='Latitude',lon='Longitude',zoom=3,size=primary,color=secondary, mapbox_style='carto-positron',size_max=35,width=1200,height=700)
        st.plotly_chart(fig, use_container_with=True)
    else:
        state_df = df[df['State']==selected_state]
        fig = px.scatter_mapbox(state_df,lat='Latitude',lon='Longitude',zoom=6,size=primary,color=secondary, mapbox_style='carto-positron',size_max=35,width=1200,height=700,hover_name='District')
        st.plotly_chart(fig, use_container_with=True)





