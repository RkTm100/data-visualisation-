import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)


def main():
    access_token='TDzM9WmlR9MAAAAAAAAAAXdBkV2scPr5z2dotfK3jK8gj8zK2iwPm-2mgyBdB6Rb'
    transferData=TransferData(access_token)
    file_from=input("What file path would you like transfer?: ")
    file_to=input("enter the full path to upload to dropbox: ")
    transferData.upload_file(file_from,file_to)
    print("file has been moved")


main()
