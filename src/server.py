import paramiko
import json


class FTPServer:
    """docstring for FTPServer"""
    def __init__(self):
        self.config = self.__read_config('../conf/config.cfg')
        self.client, self.sftp_client = self.__connect_sftp()

    def __read_config(self, file):
        fh = open(file)
        return(json.load(fh)['server'])

    def __connect_sftp(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(self.config['address'],
                       self.config['port'],
                       self.config['username'],
                       self.config['password'])
        return client, client.open_sftp()

    def get_file(self, fdir, fname):
        self.sftp_client.get("{0}/{1}".format(fdir, fname),
                             "/tmp/{0}".format(fname))
        return "/tmp/{0}".format(fname)