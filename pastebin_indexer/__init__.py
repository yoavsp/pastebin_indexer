import logging.config
import os
from os import path

import envdir

log_setting_file_path = path.join(path.dirname(path.abspath(__file__)),
                                  'logging.conf')
logging.config.fileConfig(log_setting_file_path)

ENVDIR_DIRECTORY = os.environ.get("ENVDIR_DIRECTORY",
                                  path.join(".env"))

if os.path.exists(ENVDIR_DIRECTORY):
    envdir.open(ENVDIR_DIRECTORY)
