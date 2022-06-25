
import os
import datetime



def createDir(dirname):
    try:
        os.makedirs(dirname)
    except FileExistsError:
        pass

class FileLogger:

    def __init__(self, filename):
        self.filename = filename

    def _write_msg(self, level, msg):
        _now = datetime.datetime.now()
        f = open(self.filename, mode='a', encoding='UTF-8')
        f.write(f'[{level}]  -- {_now.strftime("%A %d %B %Y")}] {msg} \n')
        f.close()


    def debug(self, msg):
        self._write_msg('DEBUG', msg)

    def info(self, msg):
        self._write_msg('DEBUG', msg)

    def error(self, msg):
        self._write_msg('DEBUG', msg)

