import json
import ftplib


_TIMEOUT_ = 3


class FTPServer:
    """docstring for FTPServer"""
    def __init__(self):
        self.config = self.__read_config('../conf/config.cfg')
        self.ftp = ftplib.FTP(host=self.config['address'],
                              user=self.config['username'],
                              passwd=self.config['password'],
                              timeout=_TIMEOUT_)

    def __read_config(self, file):
        fh = open(file)
        return(json.load(fh)['server'])

    def get_file(self):
        self.ftp.cwd(self.config['directory'])
        local_file = '/tmp/%s' % self.config['file']
        fh = open(local_file, 'wb')
        self.ftp.retrbinary('RETR %s' % local_file, fh.write)
        fh.close()
        return local_file

    def close(self):
        self.ftp.quit()
        