import logging

import openapi_server

from Flask_AuditLog import AuditLog
from Flask_No_Cache import CacheControl

app = openapi_server.app
flaskapp = app.app

logging.basicConfig(level=logging.INFO)

AuditLog(app)
CacheControl(app)
