codex/create-amazon-ppc-dashboard-web-app-dvy9h2
"""Streamlit entrypoint shim.

Some environments default to running `app.py`. This module ensures the
main dashboard in `streamlit_app.py` is loaded regardless of entrypoint.
"""

"""Streamlit entrypoint shim."""
 main
from streamlit_app import *  # noqa: F401,F403
