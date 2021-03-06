import gevent.monkey
import multiprocessing


gevent.monkey.patch_all()

daemon = True
proc_name = 'gunicorn.pid'
pidfile = './log/app_pid.log'
loglevel = 'debug'
logfile = './log/debug.log'
accesslog = './log/access.log'
access_log_format = '%(h)s %(t)s %(U)s %(q)s'
errorlog = './log/error.log'

bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
threads = multiprocessing.cpu_count() * 2
worker_class = 'gevent'
backlog = 2048
keepalive = 5
