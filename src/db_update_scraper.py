from server import FTPServer
from database import AccessDB
from mail import Message


def main():
	ftp = FTPServer()
	db = AccessDB(ftp.get_file())
	for row in db.get_rows_from_date('asdf'):
		print(row)
	ftp.close()
	# write spreadsheet
	email = Message()
	email.add_spreadsheet("asdf")
	email.send()


if __name__ == '__main__':
	main()