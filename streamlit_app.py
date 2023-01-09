import streamlit as st
import st_debug as d
import numpy as np
import random


# ---------------- CSS ----------------


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("debug.css")

# --------------- EXAMPLE -----------------


if "counter" not in st.session_state:
    st.session_state["counter"] = 1

a = np.matrix("1 2; 3 4")
st.session_state["counter"] += 1

st.title("This is an app")
st.write("A eally cool app")

k = random.randint(5, 10)
st.write(k)

d.debug(k)

d.debug("counter" + str(st.session_state["counter"]))

d.debug("this presents state of the matrix " + str(a))


# ----- [DEBUG DIV] initize debug elements -----

st.markdown(
    f'<div class="debug">{ st.session_state["debug_string"]}</div>',
    unsafe_allow_html=True,
)
