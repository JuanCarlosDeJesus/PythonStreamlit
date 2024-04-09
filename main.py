import streamlit as st
import pandas as pd

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