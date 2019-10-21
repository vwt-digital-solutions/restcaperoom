#!/usr/bin/env python3
import connexion

from openapi_server import encoder

from flask_cors import CORS

app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.app.config['MAX_CONTENT_LENGTH'] = 30 * 1024 * 1024
app.add_api('openapi.yaml',
            arguments={'title': 'restcaperoom'},
            pythonic_params=True)
CORS(app.app)
