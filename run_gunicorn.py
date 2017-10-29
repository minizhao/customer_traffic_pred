#-*- coding: utf-8 -*-

import re
import sys

from gunicorn.app.wsgiapp import run


if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$','',sys.argv[0])
    sys.exit(run())

#sudo nohup python3 run_gunicorn.py  -w 4 -b 0.0.0.0:5000 test:app