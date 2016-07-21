import os, argparse, smtplib, zipfile, tempfile
# from email import Encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def email_dir_zipped(sender, recipient):
    zf = tempfile.TemporaryFile(prefix='mail', suffix='.zip')
    zip = zipfile.ZipFile(zf, 'w')
    print "Zipping current dir: %s" % os.getcwd()
    for file_name in os.listdir(os.getcwd()):
        zip.write(file_name)
    zip.close()
    zf.seek(0)

    print "Creating email message..."
    email_msg = MIMEMultipart()
    email_msg['Subject'] = 'File from path %s' % os.getcwd()
    email_msg['To'] = ','.join(recipient)
    email_msg['From'] = sender
    email_msg.preamble = 'Testing email from Python.\n'
    msg = MIMEBase('application', 'zip')
    msg.set_payload(zf.read())
    Encoders.encode_base64(msg)
    msg.add_header('Content-Disposition', 'attachment', filename=os.getcwd()[-1] + '.zip')
    email_msg.attach(msg)
    email_msg = email_msg.as_string()
    print 'Sending email message...'
    try:
        smtp = smtplib.SMTP('localhost')
        smtp.set_debuglevel(1)
        smtp.sendmail(sender, recipient, email_msg)
    except Exception, e:
        print "Error: %s" % str(e)
    finally:
        smtp.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Email Example')
    parser.add_argument('--sender', action='store', dest='sender', default='884015671@qq.com')
    parser.add_argument('--recipient', actino='store', dest='recipient')
    given_args = parser.parse_args()
    email_dir_zipped(given_args.sender, given_args.recipient)
