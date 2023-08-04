def read_file():
    with open('secret','r') as file:
        secret = {
            line.split('=')[0]: line.split('=')[1].rstrip() for line in file.readlines()
        }
    return secret