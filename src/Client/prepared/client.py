import ftplib
from ftplib import FTP

host = "192.168.1.101"
user = "user"
password = "12345"


def getFTPFilenames(remoteWorkingDirectory)->str:
    ftp = ftplib.FTP(timeout=30)
    ftp.connect(host,2121)
    ftp.login(user,password)

    if not (remoteWorkingDirectory == None or remoteWorkingDirectory.strip() == ""):
        _ = ftp.cwd(remoteWorkingDirectory)

    fnames = []

    try:
        fnames=ftp.nlst()
    except ftplib.error_perm as resp:
        if str(resp) == "550 No files found":
            fnames = []
        else:
            raise
    return fnames


def basicConnection()->None:
    # TODO for not local host, the bellow line should use the "host" variable
    with FTP("localhost", timeout=30) as ftp:
        ftp.connect(host, 2121)
        ftp.login(user=user, passwd=password)
        print(ftp.getwelcome())

        targetfile ='hllo.txt'
        localfilepath = targetfile

        with open('test.txt', 'wb') as f:
            retCode = ftp.retrbinary(f"RETR {targetfile}", f.write, 1024)


        with open(localfilepath, 'rb') as f:
            retCode = ftp.storbinary(f"STOR {targetfile}", f)
            if retCode.startswith("226"):
                print("upload usccess!")
            else:
                print("upload not succesful...")

        # show files in the cwd
        fnames = ftp.nlst()
        print(fnames)



        ftp.quit()

basicConnection()
print(getFTPFilenames("directory/here"))