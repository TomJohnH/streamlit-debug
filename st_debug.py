import streamlit as st
import datetime
from inspect import getframeinfo, stack

# ----- Function storing debug info -----


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


# ----- function storing js script for CTRL + Q toggle -----


def js_code():
    return """
    <script>
    function myFunction() {
    
    var x = window.parent.document.getElementById("debug");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
    }

    function KeyPress(e) {
        var evtobj = window.event? event : e
        if (evtobj.keyCode == 81 && evtobj.ctrlKey) myFunction();
    }

    const doc = window.parent.document;
    doc.onkeydown = KeyPress;

    </script>
    """
