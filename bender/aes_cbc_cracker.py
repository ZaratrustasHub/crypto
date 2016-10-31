
import base64
import os
import string
import sys
from itertools import izip
from timeit import default_timer as timer

import itertools

from Crypto.Cipher import AES


class AesCracker(object):

    def __init__(self, path_to_cryptograms_folder, number_of_process):

        self.INITZALIZATION_VECTORS = iter(['498d770786c54bf5468433a44137ca43', '87ff831c4c39769d2517b3480a045062',
                                       '27be4ab54661a917814ffdf80d7c57a0', 'e03953b5a43f298162812cddff460543',
                                       'db14ae0a77c544a4c8a989c2f0f3f0e0', 'ba7b119d5c038931a192aaaec1212ed5',
                                       '070527382aaf2d612d9d0f127ee039ec', 'a04b6d3ca8bbbb1e12b61e45baebebdb',
                                       '24ebdb2a7d6468b048f67402a3931e96'])
        self.KEY_SUFIXS = iter(['1bd093a03bdab46c597a1f564ba634c7646007d4e96109dec263e931',
                           '3663dfe5befefd8d9942f2d76001939684c0bab7b76c7d86c4bf4c16',
                           '38f5785130517f59837ffc82a3a641d1cd165c2f7a8375f7f5a0734',
                           '620e6ad1b994f12c94c9561fe51c2e1e41ef0077e5bf485169c9c0',
                           '15c867f586938fe8bec14a1a9c22e6bab66cfce5c40263175e320',
                           '643e2bf797dfe46fa0bab6c8859855267f08db8c52e025395e2c',
                           '2852aef9aa2e739211eac401962c62314edfddc125b93847bc2',
                           'e6952727a3057b389ef7c353763715ecdd7f628e4edac6da71',
                           'd52ccec8cd01a354a0e123b05181b21f52760ca5a970b02dd',
                           ])
        self.KEY_LENGTH = 64
        self.HEXADECIMAL_CHARACTERS = '0123456789abcdef'

        self.START_MESSAGE = '''BEGINING ENCRYPTION OF CRYPTOGRAM {file_name}
                               INITZALIZATION VECOTR: {initzalization_vector}
                               KEY SUFIX: {key_sufix}
                               CRYPTOGRAM IN BASE64: {cryptopgram}'''
        self.END_MESSAGE = '''DECRYPTED MESSAGE: {message}
                             BAD KEYS NUMBER: {number_of_keys}
                             BAD KEYS: {bad_keys}
                             GOOD KEY: {good_key}'''

        self.PROGRESS_MESAGGE = ['''Trying encrypting...
                                USING POSSBILE KEY: {possbile_key}''',
                            '''START DECRYPTING''', ]
        self.MESSAGE_TO_RESULT_FILE = '''CRYPTOGRAM: {cryptogram_name}
                                        INITZALIZATION_VECTOR: {initzalization_vector}
                                        CRYPTOGRAM_IN_BASE64: {cryptogram}
                                        PLAIN TEXT: {plain_text}
                                        BAD KEYS: {bad_keys}
                                        BAD KEYS NUMBER: {bad_keys_number}
                                        GOOD KEY: {good_key}
                                        NUMBER OF PROCESS: {number_of_process}
                                        EXECUTION TIME: {execution_time}
                                        '''

        self.PATH_TO_CRYPTOGRAMS_FOLDER = None
        self.NUMBER_OF_PROCESS = None

        self.CRACKER_TIME = 0
        self.START_TIME = 0
        self.STOP_TIME = 0

        self.KEY_CHECKS_LIST = {'GOOD_KEY': None, 'BAD_KEYS': []}
        self.CRACKER_TIME_LIST = []
        self.PATHS_TO_CRYPTOGRAMS = None
        self.CURRENT_PATH_TO_CRYPTOGRAM = None





        self.PATH_TO_CRYPTOGRAMS_FOLDER = path_to_cryptograms_folder
        self.PATHS_TO_CRYPTOGRAMS = iter(os.listdir(self.PATH_TO_CRYPTOGRAMS_FOLDER))
        self.NUMBER_OF_CRYPTOGRAMS = len(os.listdir(self.PATH_TO_CRYPTOGRAMS_FOLDER))
        self.NUMBER_OF_PROCESS = number_of_process
        assert self.NUMBER_OF_PROCESS is not None, 'NUMBER OF PROCESS IS NONE!!!'
        assert self.PATH_TO_CRYPTOGRAMS_FOLDER is not None, 'PATH TO CRYPTOGRAMS IS NONE!!!'

    #@classmethod
    def reset_counters(self):
        self.CRACKER_TIME = 0
        self.START_TIME = 0
        self.STOP_TIME = 0

    #@classmethod
    def start_measure_time(self):
        self.START_TIME = timer()

    #@classmethod
    def stop_measure_time(self):
        self.STOP_TIME = timer()
        self.CRACKER_TIME = self.START_TIME - self.STOP_TIME

    #@classmethod
    def add_measurements_to_lists(self):
        self.KEY_CHECKS_LIST.append(self.KEY_CHECKS_LIST)
        self.CRACKER_TIME_LIST.append(self.CRACKER_TIME)

    #@classmethod
    def is_string_printable(self, text):

        for letter in text:
            if letter not in string.printable:
                return False

        return True

    #@classmethod
    def string_to_hex(self, text):
        assert len(text) % 2 == 0, 'IT SHOULD BE ALWAYS ODD!!!'
        result = r''
        for i in range(0, len(text), 2):
            result += r"\x%s%s" % (text[i], text[i + 1])

        # pairwaise = izip(text, text)#izip(reversed(text), reversed(text))
        # for lsb, msb in pairwaise:
        #     result += r'\x{}{}'.format(lsb, msb)

        return result.decode('string_escape')

    #@classmethod
    def is_utf8_encoding(self, text):
        try:
            text.encode('UTF-8')
            return True
        except UnicodeDecodeError:
            return False

    #@classmethod
    def try_decrypt_message(self, text):
        pass

    #@classmethod
    def read_cryptogram(self):
        #print self.PATHS_TO_CRYPTOGRAMS
        self.CURRENT_PATH_TO_CRYPTOGRAM = self.PATHS_TO_CRYPTOGRAMS.next()
        path = '{}/{}'.format(self.PATH_TO_CRYPTOGRAMS_FOLDER, self.CURRENT_PATH_TO_CRYPTOGRAM)
        with open(path, 'r') as cryptogram_file:
            cryptogram = cryptogram_file.read().strip()
        assert cryptogram is not None, 'CANNOT READ CRYPTOGRAM FILE!!!'
        return cryptogram

    #@classmethod
    def load_initzalization_vector_and_key_prefix(self):
        return self.string_to_hex(self.INITZALIZATION_VECTORS.next()), self.KEY_SUFIXS.next()

    #@classmethod
    def decode_cryptogram(self):
        file_content = self.read_cryptogram()
        cryptogram = base64.b64decode(file_content)
        initzalization_vector, key_sufix = self.load_initzalization_vector_and_key_prefix()
        key_prefix_length = self.KEY_LENGTH - len(key_sufix)
        generataed_prefix = itertools.product(self.HEXADECIMAL_CHARACTERS, repeat=key_prefix_length)
        counter = 0
        for prefix in generataed_prefix:
            plain_text = self.check_key(prefix=prefix, key_sufix=key_sufix, initzalization_vector=initzalization_vector,
                          cryptrogram=cryptogram)
            counter += 1
            #print plain_text
            print 'We curently checked {}/{} keys'.format(counter, str(16**key_prefix_length))
            if self.KEY_CHECKS_LIST['GOOD_KEY'] is not None:
                print 'We found key!'
                print self.KEY_CHECKS_LIST['GOOD_KEY']
                break
        self.stop_measure_time()
        self.write_results(initzalization_vector=initzalization_vector, cryptogram=cryptogram, plain_text=plain_text)


    #@classmethod
    def check_key(self, prefix, key_sufix, initzalization_vector, cryptrogram):

        possible_key = ''.join([''.join(prefix), key_sufix])
        possible_key = self.string_to_hex(possible_key)
        chiper = AES.new(possible_key, AES.MODE_CBC, initzalization_vector)
        plain_text = chiper.decrypt(cryptrogram)
        if self.is_string_printable(plain_text[:-16]):
            self.KEY_CHECKS_LIST['GOOD_KEY'] = possible_key
            return plain_text
        else:
            self.KEY_CHECKS_LIST['BAD_KEYS'].append(possible_key)
            return None


    #@classmethod
    def write_results(self,initzalization_vector, cryptogram, plain_text):
        path_to_result_file = self.CURRENT_PATH_TO_CRYPTOGRAM.replace('cryptogram_1', 'plain_text_1')
        with open(path_to_result_file,'w') as fd:
            fd.write(self.MESSAGE_TO_RESULT_FILE.format(cryptogram_name=self.CURRENT_PATH_TO_CRYPTOGRAM,
                                                       initzalization_vector=initzalization_vector, cryptogram=cryptogram,
                                                       plain_text=plain_text, bad_keys=self.KEY_CHECKS_LIST['BAD_KEYS'],
                                                       bad_keys_number=len(self.KEY_CHECKS_LIST['BAD_KEYS']),
                                                       good_key=self.KEY_CHECKS_LIST['GOOD_KEY'], number_of_process='',
                                                       execution_time=self.CRACKER_TIME))

    #@classmethod
    def main(self, *args, **kwargs):
        for _ in range(0, self.NUMBER_OF_CRYPTOGRAMS):
            self.reset_counters()
            self.start_measure_time()
            self.decode_cryptogram()


if __name__ == "__main__":
    path_to_cryptograms = sys.argv[1]
    number_of_process = sys.argv[2]
    aes_cracker = AesCracker(path_to_cryptograms_folder=path_to_cryptograms, number_of_process=number_of_process)
    aes_cracker.main()
