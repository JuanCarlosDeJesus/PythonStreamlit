from pathlib import Path

import streamlit as st
import PIL.Image


# --- PATH SETTINGS ---
THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = THIS_DIR / "assets"
STYLES_DIR = THIS_DIR / "styles"
CSS_FILE = STYLES_DIR / "main.css"

# --- GENERAL SETTINGS ---
STRIPE_CHECKOUT = "https://buy.stripe.com/test_aEU6rm20KgGj86YaEE"
CONTACT_EMAIL = "YOUREMAIL@EMAIL.COM"
PRODUCT_NAME = "Excel Add-In: MyToolBelt"
PRODUCT_TAGLINE = "Ready to Become an Office Superhero? 🚀"
PRODUCT_DESCRIPTION = """
MyToolBelt saves every smart office worker time and effort when it comes to analysis with a unique set of tools you
wont find anywhere else:

- Generate flawless Python code based on your cell selection
- Call Python scripts from Excel without having to lift a finger
- Create Jupyter Notebooks from Excel
- Add tickmarks to cells and highlight key areas
- Create an informative table of contents with ease
- ... and many more powerful features
**This is your new superpower; why fo to work without it?**
"""

# --- PAGE CONFIG ---
st.set_page_config(
    page_title=PRODUCT_NAME,
    page_icon=":star:",  # page for emojies "https://www.webfx.com/tools/emoji-cheat-sheet"
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- MAIN SECTION ---
st.header(PRODUCT_NAME)
st.subheader(PRODUCT_TAGLINE)
left_col, right_col = st.columns((2, 1))
with left_col:
    st.text("")
    st.write(PRODUCT_DESCRIPTION)
    st.markdown(
        f'<a href={STRIPE_CHECKOUT} class="button">👉 Get the Add-In</a>',
        unsafe_allow_html=True,
    )
with right_col:
    product_image = PIL.Image.open(ASSETS_DIR / "toolbelt.png")
    st.image(product_image, width=450)