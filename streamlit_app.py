import streamlit as st
import streamlit.components.v1 as components
import st_debug as d
import numpy as np
import random


# ---------------- CSS ----------------


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("debug.css")

# --------------- EXAMPLE -----------------


st.title("This is an app")
st.write(
    "This is an example how you can debug your code and view variables directely in sticky bottom debug div:"
)

st.write("1. Create a matrix")
st.code(
    """a = np.matrix("1 2; 3 4")
d.debug("this presents state of the matrix " + str(a))"""
)
a = np.matrix("1 2; 3 4")
d.debug("this presents state of the matrix " + str(a))

st.write("2. Create a counter in session state")

st.code(
    """if "counter" not in st.session_state:
    st.session_state["counter"] = 1

d.debug("counter " + str(st.session_state["counter"]))

st.session_state["counter"] += 1"""
)


if "counter" not in st.session_state:
    st.session_state["counter"] = 1

d.debug("counter " + str(st.session_state["counter"]))

st.session_state["counter"] += 1

st.write("At the bottom of the app you should see a debug div.")
st.write(
    "Debug div contains info about: time of calculation, line from which debug command was executed and saved debug info. Hit R to recalculate the app."
)

# ----- [DEBUG DIV] initize debug elements -----

if "debug_string" in st.session_state:
    st.markdown(
        f'<div class="debug" id="debug">{ st.session_state["debug_string"]}</div>',
        unsafe_allow_html=True,
    )

components.html(
    d.js_code(),
    height=0,
    width=0,
)
