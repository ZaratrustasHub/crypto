import os
import hashlib
import Crypto.Cipher.AES as AES


class Cipher:

        @staticmethod
        def md5sum(raw):
                m = hashlib.md5()
                m.update(raw)
                return m.hexdigest()

        BS = AES.block_size

        @staticmethod
        def pad(s):
                return s + (Cipher.BS - len(s) % Cipher.BS) * chr(Cipher.BS - len(s) % Cipher.BS) #secure +


        @staticmethod
        def unpad(s):
                return s[0:-ord(s[-1])]

        def __init__(self, key):
                self.key = Cipher.md5sum(key)
                self.cnter_cb_called = 0
                self.secret = None

        def _reset_counter_callback_state(self, secret):
                self.cnter_cb_called = 0
                self.secret = secret

        def _counter_callback(self):
                self.cnter_cb_called += 1
                return self.secret[self.cnter_cb_called % Cipher.BS] * Cipher.BS

        def encrypt(self, raw):
                secret = os.urandom(Cipher.BS) #rekomendowane
                self._reset_counter_callback_state(secret)
                cipher = AES.new(self.key, AES.MODE_CTR, counter=self._counter_callback)
                raw_padded = Cipher.pad(raw)
                enc_padded = cipher.encrypt(raw_padded)
                return secret+enc_padded

        def decrypt(self, enc):
                secret = enc[:Cipher.BS]
                self._reset_counter_callback_state(secret)
                cipher = AES.new(self.key, AES.MODE_CTR, counter=self._counter_callback)
                enc_padded = enc[Cipher.BS:]
                raw_padded = cipher.decrypt(enc_padded)
                return Cipher.unpad(raw_padded)