# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 08:00:05 2022

@author: BANJIAJIA
"""

import streamlit as st
import xlrd
from pyecharts import options as opts
from pyecharts.charts import Pie
from streamlit_echarts import st_pyecharts
import requests,json
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
    
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_code_sunny = load_lottie('https://assets3.lottiefiles.com/packages/lf20_i7ixqfgx.json')
lottie_code_cloudy = load_lottie('https://assets3.lottiefiles.com/packages/lf20_dxkh5nn5.json')
lottie_code_raining = load_lottie('https://assets3.lottiefiles.com/packages/lf20_mhlhglws.json')



# # 设置侧边栏显示
# st.sidebar.header('生产管理系统')
# st.sidebar.markdown('* 项目部管理人员')
# st.sidebar.markdown('* 施工人员')
# st.sidebar.markdown('* 西区进度偏差趋势分析')

def write():
    st.sidebar.markdown('---')
    st.sidebar.write('每日一贴:sunny:')
    st.sidebar.info('“234”工程：推进大安全管理体系和本质安全管理能力“两个建设”，深化基层、基础、基本功“三基管理”，落实专业化、标准化、数字化、精细化“四化要求”')
    st.sidebar.write('[:office: 联系我们 ](http://www.aepc1.ceec.net.cn/)')
    
    # 设置主页标题
    col1,col2 = st.columns([2,5])
    with col1:    
        st.image('ceec.jpg',width=300)
    with col2:
        st.title(':computer:'+'生产管理可视化大屏')
    
    # 显示天气
    r = requests.get('https://devapi.qweather.com/v7/weather/now?location=101280101&key=2b8e90ae78be4a278c625c52dfc9b380')
    r.encoding = 'utf-8'
    data = json.loads(r.text)
    city = '广州恒运'
    weather = data['now']['text'] 
    temp = data['now']['temp'] + '℃'
    fengli = data['now']['windScale'] + '级'
    
    col1,col2,col3,col4,col5 = st.columns(5)
    col1.metric('项目',city)
    col3.metric('天气',weather)
    with col2:
        st_lottie(lottie_code_cloudy,height=100,key='coding')
    col4.metric('温度',temp)
    col5.metric('风力',fengli)
        
    st.markdown('---')
    
    # Part1,2
    col1,col2 = st.columns(2)
    with col1:
        # Part1
        xls_file = xlrd.open_workbook('data.xlsx')
        table1 = xls_file.sheet_by_index(0)
        col1_value = table1.col_values(0)  # 部门
        col2_value = table1.col_values(1)  # 人数
        del(col1_value[0])  # 去除标题行
        del(col2_value[0])  # 去除标题行
        s1 = int(sum(col2_value))
        
        pie1 = (
            Pie()
            .add('',
                 [list(z) for z in zip(col1_value,col2_value)],
                 # rosetype="radius",
                 # radius="90%",
                 center=['40%','50%'])
            .set_global_opts(title_opts=opts.TitleOpts(title="", subtitle=""),
                             legend_opts=opts.LegendOpts(type_="scroll", pos_left="75%", orient="vertical"),
                             )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            )
        
        st.subheader(f'项目部管理人员：{s1}人')
        st_pyecharts(pie1)
    
    with col2:
        # Part2
        x_data = ["项目部", "建筑", "热动", "电仪"]
        y_data = [45, 194, 100, 82]
        s2 = sum(y_data)
        st.subheader(f'施工人员：{s2}人')
        
        pie2 = (
            Pie()
            .add('',
                 [list(z) for z in zip(x_data,y_data)],
                 # rosetype="radius",
                 # radius="90%",
                 center=['40%','50%'])
            .set_global_opts(title_opts=opts.TitleOpts(title="", subtitle=""),
                             legend_opts=opts.LegendOpts(type_="scroll", pos_left="75%", orient="vertical"),
                             )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            )
        st_pyecharts(pie2)
    
    st.markdown('---')
    
    # Part3
    st.subheader('西区进度偏差趋势分析')
    f = open('b.html')
    r = f.read()
    components.html(
        r,
        height=500
        )
    
    with st.expander('查看详细计划盘点'):
        st.image('./analysis/20220929_1.jpg')
        st.image('./analysis/20220929_2.jpg')
        
    # st.markdown('---')
    
    # Part4
    st.subheader('现场航拍图')
    tab1,tab2,tab3=st.tabs(['主厂区','附属厂区','效果图'])
    with tab1:
        st.image('east.jpg')
    with tab2:
        st.image('west.jpg')
    with tab3:
        st.image('rendering.jpg')
        
    st.write('[:office:联系我们](http://www.aepc1.ceec.net.cn/)')