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
