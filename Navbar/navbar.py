import streamlit as st
from streamlit_option_menu import option_menu



# selection function
def menubar_selection(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu", # required - if you don't want to display anything use "None"
                options=["Home","Projects","Contact"], # required - selection in list
                icons=["house","book","envelope"], # optional - use bootstrapt icon list = https://icons.getbootstrap.com/
                menu_icon="cast", # optional - again bootstrap icon list
                default_index=0, # optional - where the default menu starts with
            )
        return selected
    
    if example == 2:
        # 2. as horizontalbar menu
        selected = option_menu(
            menu_title="Main Menu", # required - if you don't want to display anything use "None"
            options=["Home","Projects","Contact"], # required - selection in list
            icons=["house","book","envelope"], # optional - use bootstrapt icon list = https://icons.getbootstrap.com/
            menu_icon="cast", # optional - again bootstrap icon list
            default_index=0, # optional - where the default menu starts with
            orientation="horizontal", # display horizontal bar
            )
        return selected

    if example == 3:
        # 3. as horizontalbar menu with custom style
        selected = option_menu(
            menu_title="Main Menu", # required - if you don't want to display anything use "None"
            options=["Home","Projects","Contact"], # required - selection in list
            icons=["house","book","envelope"], # optional - use bootstrapt icon list = https://icons.getbootstrap.com/
            menu_icon="cast", # optional - again bootstrap icon list
            default_index=0, # optional - where the default menu starts with
            orientation="horizontal", # display horizontal bar
            styles={
                        "container": {"padding": "0!important", "background-color": "#fafafa"},
                        "icon": {"color": "orange", "font-size": "25px"},
                        "nav-link": {
                            "font-size": "25px",
                            "text-align": "left",
                            "margin": "0px",
                            "--hover-color": "#eee",
                        },
                        "nav-link-selected": {"background-color": "green"},
                    },
            )
        return selected

# Menu selection = 1. sidebar, 2. horizontal bar, 3. horizontal bar with style
rdo_disp = st.radio("Display choice in Menu", options=("Sidebar","Horizontal bar","Horizontal bar with options"))
if rdo_disp == "Sidebar":
    example_no = 1
elif rdo_disp == "Horizontal bar":
    example_no = 2
else:
    example_no = 3

selected = menubar_selection(example=example_no)

# validate selection
if selected == "Home":
    st.title(f"You have selected {selected}"
    )
if selected == "Projects":
    st.title(f"You have selected {selected}"
    )
if selected == "Contact":
    st.title(f"You have selected {selected}"
    )
