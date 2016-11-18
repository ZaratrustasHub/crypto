import sys
from Cipher import Cipher


class aes_encrypt(object):

    def __init__(self, path_to_keystore, path_to_file):
        self.path_to_keystore = None
        self.path_to_file = None

    #@classmethod
    def read_key(self):
        path = path_to_keystore
        with open(path, 'r') as keystore:
            key = keystore.read()
        assert key is not None, 'CANNOT READ KEYSTORE FILE!!!'
        return key

    def main(self, *args, **kwargs):
        secret = self.read_key()
        x = Cipher(secret)
        content = None


        with open(path_to_file, 'rb') as fd:
            content = fd.read()
        assert content is not None, 'CANNOT READ FILE TO ENCRYPTION!!!'

        a = x.encrypt(content)
        with open('output1', 'wb') as fd:
            fd.write(a)
        #b = x.decrypt(a)
        #with open('output2', 'wb') as fd:
         #   fd.write(b)

if __name__ == '__main__':
    path_to_keystore = sys.argv[1]
    path_to_file = sys.argv[2]
    aes_encrypt(path_to_keystore, path_to_file).main()
