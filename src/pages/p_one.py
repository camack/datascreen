# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 08:02:36 2022

@author: BANJIAJIA
"""

import streamlit as st
import xlrd
from pyecharts import options as opts
from pyecharts.charts import Pie
from streamlit_echarts import st_pyecharts

def write():      
    # 初始化设置
    # st.set_page_config(page_title='可视化大屏',page_icon=':computer:',layout='wide')
    
    st.sidebar.markdown('---')
    st.sidebar.write('每日一贴:sunny:')
    st.sidebar.info('“三全管理”：全面预算管理、全成本核算管理、全面绩效考核管理')
    # 设置主页标题
    col1,col2 = st.columns([2,5])
    with col1:    
        st.image('ceec.jpg',width=300)
    with col2:
        st.title(':computer:'+'经营管理可视化大屏')
    
    
    col1,col2,col3,col4 = st.columns(4)
    col1.metric('合同总额','35797 万元')
    col2.metric('累计确认产值','2500 万元')
    col3.metric('累计收取资金','2223 万元')
    col4.metric('累计发生成本','2850 万元')