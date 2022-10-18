# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 16:09:07 2022

@author: BANJIAJIA
"""

import streamlit as st
from streamlit_option_menu import option_menu
import src.pages.p_main
import src.pages.p_one
import src.pages.p_two

st.set_page_config(page_title='可视化大屏',page_icon=':computer:',layout='wide')

def app_write():    
    PAGES = {
        "🏠 生产管理": src.pages.p_main,
        "💰 经营管理": src.pages.p_one,
        "🚩 党建管理": src.pages.p_two,
    
    }
    
    with st.sidebar:
        selected = option_menu("数据可视化系统", list(PAGES.keys()), 
            icons=['dot','dot','dot'], menu_icon="cast", default_index=0)
        page = PAGES[selected]
    
    page.write()
    
app_write()