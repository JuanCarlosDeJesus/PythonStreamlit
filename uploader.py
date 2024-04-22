import streamlit as st

st.title("File Uploader in Streamlit")
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
st.markdown("---")
img = st.file_uploader("Please upload an image: ", type=["png","jpg","jpeg"])
if img is not None:
    st.image(img)
imgs = st.file_uploader("Please upload images: ", type=["png","jpg","jpeg"], accept_multiple_files= True)
if imgs is not None:
    for i in imgs:
        st.image(i)
aud = st.file_uploader("Please upload an audio: ", type="mp3")
if aud is not None:
    st.audio(aud)
vid = st.file_uploader("Please upload a video: ", type="mp4")
if vid is not None:
    st.video(vid)

# using slider
val = st.slider("This is a .slider()", value=70)
print(val)
st.write(val)
# using select_slider
color = st.select_slider("This is a .select_slider(), select colors:", options=["Black","Red","Blue"])
st.write(color)

# Text Input
txt = st.text_input("Enter your course title:", max_chars=60)
print(txt)
st.write(txt)

# text area
txt_area = st.text_area("Course Description: ")
print(txt_area)

# Date input
dt = st.date_input("Enter the date: ")
print(dt)

# Time input

tm = st.time_input("Enter the time: ")
print(tm)