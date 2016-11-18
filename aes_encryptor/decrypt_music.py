import sys
import pygst
pygst.require('0.10')
import gst
import gobject
import os


from Cipher import Cipher


class decrypt_music(object):

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

    # @classmethod
    def decrypt_music(self):
        key = self.read_key()
        x = Cipher(key)
        path = path_to_file
        with open(path, 'rb') as musicfile:
            decsound = musicfile.read()

            assert decsound is not None, 'CANNOT READ SOUND FILE!!!'
            decsound = x.decrypt(decsound)
        return decsound

    def main(self, *args, **kwargs):
        sound = self.decrypt_music()
        with open('decrypted2play', 'wb') as fd:
            fd.write(sound)
        mainloop = gobject.MainLoop()
        pl = gst.element_factory_make("playbin", "player")
        pl.set_property('uri', 'file://' + os.path.abspath('decrypted2play'))
        pl.set_state(gst.STATE_PLAYING)
        mainloop.run()


if __name__ == '__main__':
    path_to_keystore = sys.argv[1]
    path_to_file = sys.argv[2]
    decrypt_music(path_to_keystore, path_to_file).main()
