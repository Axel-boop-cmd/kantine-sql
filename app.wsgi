import sys
import site
import os

site.addsitedir('/var/www/mysql/env/lib/python3.13/site-packages')

sys.path.insert(0, '/var/www/mysql')

os.chdir('/var/www/mysql')

os.environ['VIRTUAL_ENV'] = '/var/www/mysql/env'
os.environ['PATH'] = '/var/www/mysql/env/bin:' + os.environ['PATH']

from app import app as application
