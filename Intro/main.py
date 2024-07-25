import streamlit as st
import pandas as pd

# remove "hamburger" - options on top right and others
st.text("Streamlit cleanup - hamburger and deploy, right click on hamburger and click inspect")
st.text("Then use .markdown, in class names use '.' for blank space")
st.markdown("""
<style>
.st-emotion-cache-6q9sum.ef3psqc4
{
    visibility: hidden;
}
.st-emotion-cache-1wbqy5l.e17vllj40
{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

tbl=pd.DataFrame({"Column 1": [1,2,3,4,5,6,7], "Column 2": [11,12,13,14,15,16,17]})

st.title("This is st.title")
st.subheader("This is st.subheader")
st.header("This is st.header")
st.text("This is st.text - use it in place of paragraphs")
# markdown 
st.markdown("[st.markdown(MarkdownGuide.org)](https://www.markdownguide.org)")
st.markdown("---")
st.caption("Hi i am st.caption")
st.markdown("[The latex expression is made with st.latex(katex.org)](https://www.katex.org)")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
json={"a":"1,2,3","b":"4,5,6"}
st.json(json)
code="""
print("Hello World!")
def func():
    return 0;"""
st.code(code, language="python")
st.text("st.write() allows us to implement markdown, latex, code, json ...")
st.write("## H2")
st.text("using st.metric....")
st.metric(label="Wind Speed", value="120ms⁻¹", delta="-1.4ms⁻¹")
st.text("st.table is static")
st.table(tbl)
st.text("st.dataframe can be manipulated")
st.dataframe(tbl)

# display media files
st.text("Display media files with .audio, .image, .video")
st.image("images.jpg", caption="This is my image", width=680)
st.audio("KavinskyNightcall.mp3")
st.video("KaliLinuxInstall.mp4")

# display interactive widgets
st.text("Display interactive widgets - CHeckBox")
st.checkbox("Checkbox", value=True)
# using logic
st.text("widgets with python logic")
state = st.checkbox("State", value=True)
if state:
    st.write("True")
else:
    st.write("False")
# adding an on_change function
st.text("Using on_change widget property")
def changes():
    print("Checkbox changed!")
box_on_change = st.checkbox("Chkbx", value=True, on_change=changes)
st.text("Adding a key id property")
def keyid():
    print(st.session_state.chkr)
box_with_keyid = st.checkbox("KeyID", value=True, on_change=keyid, key="chkr")
st.text("Display interactive widgets - RadioButton")
rdo_btn = st.radio("Where do you live?", options=("U.S.A.","uk","canada"))
st.text("Display Radio Button choice")
rdo_disp = st.radio("Display choice in terminal", options=("U.S.A.","uk","canada"))
st.write(rdo_disp)
st.text("Display interactive widgets - Buttons")
def btn_clk():
    print("Ya clicked me!")
btn = st.button("Click Me!", on_click=btn_clk)
st.text("Display interactive widgets - SelectBox")
select_box = st.selectbox("What is your favorite car?", options=("Mustang","Camaro","Corvette"))
print(select_box)
st.text("Display interactive widgets - MultiSelectBox")
multi_select = st.multiselect("What is your favorite car?", options=("Mustang","Camaro","Corvette"))
st.write(multi_select)
