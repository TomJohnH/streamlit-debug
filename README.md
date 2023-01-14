# streamlit-debug

A handy tool for streamlit app debugging. Example: [https://stdebug.streamlit.app/](https://stdebug.streamlit.app/)

## Usage:

1. Download `st_debug.py` and `debug.css`
2. Import module

```
import st_debug as d
```

3. Load css

```
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("debug.css")
```

4. At the bottom of your code make additional div:

```
if "debug_string" in st.session_state:
    st.markdown(
        f'<div class="debug">{ st.session_state["debug_string"]}</div>',
        unsafe_allow_html=True,
    )
```

5. Write debugging commands

```
a = np.matrix("1 2; 3 4")
d.debug("this presents state of the matrix " + str(a))
```

## Changelog:

14.01.2023

- css update, new better visuals

