"""
WSGI config for deployment - completely isolated from ML dependencies
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

# Force deployment mode with minimal settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings_deployment')
os.environ['USE_SIMPLE_PROCESSOR'] = 'true'
os.environ['RENDER'] = 'true'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Ensure we're in the right directory
sys.path.insert(0, os.path.dirname(__file__))

application = get_wsgi_application()