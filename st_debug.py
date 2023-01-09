import streamlit as st
import datetime
from inspect import getframeinfo, stack

# ----- [DEBUG] initize debug elements -----


def debug(input):
    if "debug_string" not in st.session_state:
        st.session_state["debug_string"] = "<b>Debug window ☝️</b>"
    now = datetime.datetime.now()
    st.session_state["debug_string"] = (
        "<div style='border-bottom: dotted; border-width: thin;border-color: #cccccc;'>"
        + str(now.hour)
        + ":"
        + str(now.minute)
        + ":"
        + str(now.second)
        + " Debug.print["
        + str(getframeinfo(stack()[1][0]).lineno)
        + "] "
        + str(input)
        + "</div>"
        + st.session_state["debug_string"]
    )
