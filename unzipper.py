import os, sys, pyminizip, getpass, zipfile    
import pyfiglet

def banner():
    ascii_banner = pyfiglet.figlet_format("Zippy Ransom - Unzipper")
    print(ascii_banner)

def main():
    try:
        # provide path (BE CAREFUL!!!)
        path = input("Enter path to unzip: ")

        if not os.path.exists(path):
            raise Exception("Path does not exits")

        # get password from user
        passwd = getpass.getpass()

        # ensure password is not blank
        if passwd == "" or passwd.strip() == "":
            raise Exception("Password cannot be blank")

        # iterate through dictories starting with the path given
        for root, dirs, files in os.walk(path, topdown=False):
            try:
                for name in files:
                    inpt = os.path.join(root, name)
                    print(inpt)

                    if zipfile.is_zipfile(inpt):
                        # decompress file
                        pyminizip.uncompress(inpt, passwd, root, 0)

                        # delete zip file
                        os.remove(inpt) 

            except Exception as e:
                print("Error 2:", e)
                continue


        print("Files has been unzipped!")

    except Exception as e:
        print("Error 1")
        sys.exit(e)
    
if __name__=="__main__":
    banner()
    main()