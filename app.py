"""Streamlit entrypoint shim.

Some environments default to running `app.py`. This module ensures the
main dashboard in `streamlit_app.py` is loaded regardless of entrypoint.
"""

from streamlit_app import *  # noqa: F401,F403
