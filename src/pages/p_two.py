# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 08:02:47 2022

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
    st.sidebar.info(' 支部“三力”：战斗力、凝聚力、治理力 ')
    
    # 设置主页标题
    col1,col2 = st.columns([2,5])
    with col1:    
        st.image('ceec.jpg',width=300)
    with col2:
        st.title(':computer:'+'党建管理可视化大屏')
        
    #Part1
    xls_file = xlrd.open_workbook('data.xlsx')
    table2 = xls_file.sheet_by_index(2)
    col1_value = table2.col_values(0)  # 部门
    col2_value = table2.col_values(1)  # 人数
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
    
    st.subheader(f'项目党员人数：{s1}人')
    st_pyecharts(pie1)
    with st.expander('党员名单：'):
        st.write(
            ''' 齐亮
                孔德杰
                蒋俊
                黄长平
                李晓丹
                吴俊
                王文远
                汪林宇
                曹宏生
                刘夫尹
                贾晓勇
                陶鹏
                张时昌
                顾营祥
                陈新平
                朱策
                胡利兵
                赵洪涛
                李思松
                ''')
    
    #Part2
    # st.markdown('---')
    st.subheader('公司企业理念查询')
    col1,col2,col3 = st.columns([1,5,2])
    
    with col1:
        st.write('')
    with col2:
        keyword = st.text_input('请输入关键字：',placeholder='在这里输入要查询的内容')
        xls_file = xlrd.open_workbook('data2.xlsx')
        table1 = xls_file.sheet_by_index(0)
        col1 = table1.col_values(0)
        for line in col1:
            if keyword!='':
                if keyword in line:
                    st.info(line)  
    with col3:
        st.write('')