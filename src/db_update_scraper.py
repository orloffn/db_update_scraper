from server import FTPServer
from database import AccessDB


def main():
	ftp = FTPServer()
	db = AccessDB(ftp.get_file())
	for row in db.get_rows_from_date('asdf'):
		print(row)
	ftp.close()


if __name__ == '__main__':
	main()