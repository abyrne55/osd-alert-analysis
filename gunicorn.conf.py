"""
GUnicorn WSGI server config. 
"""
# pylint: disable=invalid-name
bind="0.0.0.0:8080"
# Temporary fix to very-long database queries (see OSD-14138)
timeout = 60
