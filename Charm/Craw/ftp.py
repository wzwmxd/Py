FTP_SERVER_URL = 'home.ustc.edu.cn'
import ftplib


def test_ftp_connection(path, username, password):
    ftp = ftplib.FTP(path, user=username, password=password)
    ftp.cwd('/pub')
    print  "File list at: %s" % path
    files = ftp.dir()
    print files
    ftp.quit()


if __name__ == '__main__':
    test_ftp_connection(path=FTP_SERVER_URL, username='xushijie', password='4181456')
