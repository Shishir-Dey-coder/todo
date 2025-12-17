# gunicorn_config.py
import multiprocessing

# Server socket
bind = "0.0.0.0:10000"  # Render default port

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"

# Logging
accesslog = "-"  # stdout
errorlog = "-"   # stdout
loglevel = "info"

# Process naming
proc_name = "todo_app"

# Worker timeout (seconds)
timeout = 120
keepalive = 5

# Max requests per worker
max_requests = 1000
max_requests_jitter = 50

# Security
limit_request_line = 4096
limit_request_fields = 100