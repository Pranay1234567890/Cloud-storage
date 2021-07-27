import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'v1uR7NDleB8AAAAAAAAAAWdku-QMzfHgIH3OXYRPKX6wjRSPFiY1a4DTexPkn1ts'
    transferData = TransferData(access_token)

    file_from =  input("ENTER YOUR FILE NAME : ")
    file_to = input("ENTER YOUR DESTINATION : ")  # The full path to upload the file to, including the file name


    transferData.upload_file(file_from, file_to)
    print("FILE UPLOADED")

main()
