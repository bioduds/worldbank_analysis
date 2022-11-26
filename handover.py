# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:17:07 2021
@author: Andi5
"""
import streamlit as st
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly.figure_factory as ff


st.set_page_config(page_title='SWAST - Handover Delays',  layout='wide', page_icon=':ambulance:')

#this is the header

t1, t2 = st.columns((0.07,1)) 

t1.image('images/ufmg.jpg', width = 120)
t2.title("Laboratório de Dados - Jonas Jr.")
t2.markdown(" **tel:** 01392 451192 **| website:** https://www.swast.nhs.uk **| email:** mailto:data.science@swast.nhs.uk")


## Data

with st.spinner('Tá rodando...') :
    
    #Metrics setting and rendering

    wb_df = pd.read_excel('worldbank.xlsx',sheet_name = 'Data')
    wb_df_countries = pd.read_excel('worldbank.xlsx',sheet_name = 'Metadata - Countries')
    countries = wb_df_countries['TableName']
    inds_all = wb_df['Indicator Name']
    inds = sorted( set( inds_all ) )
    
    ind_options = st.multiselect( 'Escolha os indicadores', inds, [] )
    st.write( '### Indicadores selecionados:' )
    
    for ind in ind_options :
        wb_df_ind_loc = wb_df.loc[ wb_df['Indicator Name'] == ind]
        
        # grafico 1
        wb_df_ind_clean1a = wb_df_ind_loc.drop( wb_df_ind_loc.columns[1:51], axis=1 )
        wb_df_ind_clean1b = wb_df_ind_clean1a.drop( wb_df_ind_clean1a.columns[8:17], axis=1 )
        wb_df_ind_T1 = wb_df_ind_clean1b.T
        wb_df_ind_T1.columns = wb_df_ind_T1.iloc[0]
        wb_df_ind_T1 = wb_df_ind_T1.iloc[1: , :]

        # grafico 2
        wb_df_ind_clean1a = wb_df_ind_loc.drop( wb_df_ind_loc.columns[1:62], axis=1 )
        wb_df_ind_T2 = wb_df_ind_clean1a.T
        wb_df_ind_T2.columns = wb_df_ind_T2.iloc[0]
        wb_df_ind_T2 = wb_df_ind_T2.iloc[1: , :]
        
        with st.expander( ind ) :
            df1, df2 = st.columns((1,1))
            df1.write( wb_df_ind_T1 )
            df2.write( wb_df_ind_T2 )
            
        g1, g2 = st.columns( ( 1, 1 ) )
        
        # Create distplot with custom bin_size
        fig1 = px.line( wb_df_ind_T1, title='2006-2013' )
        fig2 = px.line( wb_df_ind_T2, title='2018-2021' )

        # Plot
        g1.plotly_chart(fig1, use_container_width=True)
        g2.plotly_chart(fig2, use_container_width=True)
                           
with st.spinner('Terminou de rodar!'):
    time.sleep(1)     
            
        
        
        
        
        
        
        