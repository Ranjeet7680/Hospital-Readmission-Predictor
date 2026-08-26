import os
import sys

# Ensure all relevant directories (root, api, cwd) are in sys.path
api_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(api_dir)
cwd = os.getcwd()

for p in [root_dir, api_dir, cwd]:
    if p and p not in sys.path:
        sys.path.insert(0, p)

from app.main import app

# Expose both app and handler for maximum compatibility with serverless runners
handler = app
