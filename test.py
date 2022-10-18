# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 15:30:22 2022

@author: BANJIAJIA
"""

import streamlit as st
import xlrd

keyword = st.text_input('企业理念查询：',placeholder='在这里输入要查询的内容')

xls_file = xlrd.open_workbook('data2.xlsx')
table1 = xls_file.sheet_by_index(0)
col1 = table1.col_values(0)

for line in col1:
    if keyword!='':
        if keyword in line:
            st.write(line)   

# with open('data.txt','r',encoding='utf-8') as f:
#     lines = f.readlines()

# for line in lines:
#     if keyword!='':
#         if keyword in line:
#             st.write(line)


# import streamlit as st
# from streamlit_timeline import timeline
# from streamlit_tags import st_tags
# import hydralit_components as hc
# import datetime
# from st_btn_select import st_btn_select
# from streamlit_option_menu import option_menu
# import src.pages.p_main
# import src.pages.p_one
# import src.pages.p_two


# st.set_page_config(page_title="Timeline Example", layout="wide")

# PAGES = {
#     "🏠 生产管理": src.pages.p_main,
#     "💰 经营管理": src.pages.p_one,
#     "🚩 党建管理": src.pages.p_two,

# }
# with st.sidebar:
#     selected = option_menu("数据可视化系统", list(PAGES.keys()), 
#         icons=['dot','dot','dot'], menu_icon="cast", default_index=0)
#     page = PAGES[selected]
# page.write()

# page = st_btn_select(
#   # The different pages
#   ('home', 'about', 'docs', 'playground'),
#   # Enable navbar
#    nav=True,
#   # You can pass a formatting function. Here we capitalize the options
#   # format_func=lambda name: name.capitalize(),
# )

# # Display the right things according to the page
# if page == 'home':
#   st.write('HOMEPAGE')

# # keywords = st_tags(
#     label='# Enter Keywords:',
#     text='Press enter to add more',
#     value=['Zero', 'One', 'Two'],
#     suggestions=['five', 'six', 'seven', 
#                  'eight', 'nine', 'three', 
#                  'eleven', 'ten', 'four'],
#     maxtags = 4,
#     key='1')

# st.write(keywords)

#can apply customisation to almost all the properties of the card, including the progress bar
# theme_bad = {'bgcolor': '#FFF0F0','title_color': 'red','content_color': 'red','icon_color': 'red', 'icon': 'fa fa-times-circle'}
# theme_neutral = {'bgcolor': '#f9f9f9','title_color': 'orange','content_color': 'orange','icon_color': 'orange', 'icon': 'fa fa-question-circle'}
# theme_good = {'bgcolor': '#EFF8F7','title_color': 'green','content_color': 'green','icon_color': 'green', 'icon': 'fa fa-check-circle'}

# cc = st.columns(2)

# with cc[0]:
#     # can just use 'good', 'bad', 'neutral' sentiment to auto color the card
#     hc.info_card(title='Some heading GOOD', content='All good!', sentiment='good',bar_value=77)

# with cc[1]:
#     hc.info_card(title='Some BAD BAD', content='This is really bad',bar_value=12,theme_override=theme_bad)

# # with cc[2]:
# #     hc.info_card(title='Some NEURAL', content='Oh yeah, sure.', sentiment='neutral',bar_value=55)

# # with cc[3]:
# #     #customise the the theming for a neutral content
# #     hc.info_card(title='Some NEURAL',content='Maybe...',key='sec',bar_value=5,theme_override=theme_neutral)

# # define what option labels and icons to display
# option_data = [
#    {'icon': "bi bi-hand-thumbs-up", 'label':"Agree"},
#    {'icon':"fa fa-question-circle",'label':"Unsure"},
#    {'icon': "bi bi-hand-thumbs-down", 'label':"Disagree"},
# ]

# # override the theme, else it will use the Streamlit applied theme
# over_theme = {'txc_inactive': 'white','menu_background':'purple','txc_active':'yellow','option_active':'blue'}
# font_fmt = {'font-class':'h2','font-size':'150%'}

# # display a horizontal version of the option bar
# # op = hc.option_bar(option_definition=option_data,title='Feedback Response',key='PrimaryOption',override_theme=over_theme,font_styling=font_fmt,horizontal_orientation=True)

# # display a version version of the option bar
# op2 = hc.option_bar(
#     option_definition=option_data,
#     title='Feedback Response',
#     key='PrimaryOption',
#     override_theme=over_theme,
#     font_styling=font_fmt,
#     horizontal_orientation=False)
# st.write(op2)

# # can apply customisation to almost all the properties 0f the progress ba
# override_theme_1 = {'bgcolor': '#EFF8F7','progress_color': 'green'}
# override_theme_2 = {'bgcolor': 'green','content_color': 'white','progress_color': 'red'}
# override_theme_3 = {'content_color': 'red','progress_color': 'orange'}

# # can just use 'good', 'bad', 'neutral' sentiment to auto color the bar
# hc.progress_bar(25,'Something something')
# hc.progress_bar(35,'Something something',sentiment='good')
# hc.progress_bar(95,'Something something',sentiment='neutral')
# hc.progress_bar(47,'Something something',sentiment='bad')

# # customise the the theming for a neutral content
# hc.progress_bar(5,'Something something - 1a',key='pa1',override_theme=override_theme_1)
# hc.progress_bar(35,'Something something - 2a',key='pa2',sentiment='good',override_theme=override_theme_2)
# hc.progress_bar(95,'Something something - 3a',key='pa3',sentiment='neutral')
# hc.progress_bar(47,'Something something - 4a',key='pa4',sentiment='bad',override_theme=override_theme_3)

#make it look nice from the start

# specify the primary menu definition
# menu_data = [
#     {'icon': "far fa-copy", 'label':"Left End"},
#     {'id':'Copy','icon':"🐙",'label':"Copy"},
#     {'icon': "fa-solid fa-radar",'label':"Dropdown1", 'submenu':[{'id':' subid11','icon': "fa fa-paperclip", 'label':"Sub-item 1"},{'id':'subid12','icon': "💀", 'label':"Sub-item 2"},{'id':'subid13','icon': "fa fa-database", 'label':"Sub-item 3"}]},
#     {'icon': "far fa-chart-bar", 'label':"Chart"},#no tooltip message
#     {'id':' Crazy return value 💀','icon': "💀", 'label':"Calendar"},
#     {'icon': "fas fa-tachometer-alt", 'label':"Dashboard",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
#     {'icon': "far fa-copy", 'label':"Right End"},
#     {'icon': "fa-solid fa-radar",'label':"Dropdown2", 'submenu':[{'label':"Sub-item 1", 'icon': "fa fa-meh"},{'label':"Sub-item 2"},{'icon':'🙉','label':"Sub-item 3",}]},
# ]

# over_theme = {'txc_inactive': '#FFFFFF','menu_background':'#393D49'}
# menu_id = hc.nav_bar(
#     menu_definition=menu_data,
#     override_theme=over_theme,
#     home_name='Home',
#     login_name='Logout',
#     hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
#     sticky_nav=True, #at the top or not
#     sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
# )

# if st.button('click me'):
#   st.info('You clicked at: {}'.format(datetime.datetime.now()))


# if st.sidebar.button('click me too'):
#   st.sidebar.info('You clicked at: {}'.format(datetime.datetime.now()))

# #get the id of the menu item clicked
# st.info(f"{menu_id}")

