import hashlib
import sys

from Crypto import Random
from Crypto.Cipher import AES


def encrypt(bytes_to_encrypt, key):
    key_256 = hashlib.sha256(key.encode()).digest()
    iv = Random.new().read(AES.block_size)
    aes = AES.new(key_256, AES.MODE_OFB, iv)
    return iv + aes.encrypt(bytes_to_encrypt)


def decrypt(bytes_to_decrypt, key):
    key_256 = hashlib.sha256(key.encode()).digest()
    iv = bytes_to_decrypt[:AES.block_size]
    aes = AES.new(key_256, AES.MODE_OFB, iv)
    return aes.decrypt(bytes_to_decrypt[AES.block_size:])


def read_file_bytes(filename):
    in_file = open(filename, "rb")
    bytes_read = in_file.read()
    in_file.close()
    return bytes_read


def write_file_bytes(filename, bytes_to_write):
    out_file = open(filename, "wb")
    out_file.write(bytes_to_write)
    out_file.close()


if __name__ == "__main__":
    args = sys.argv
    arg_action = args[1]
    arg_filename = args[2]
    arg_key = args[3]
    if arg_action == "encrypt":
        file_bytes = read_file_bytes(arg_filename)
        encrypted_bytes = encrypt(file_bytes, arg_key)
        write_file_bytes("encrypted", encrypted_bytes)
    elif arg_action == "decrypt":
        file_bytes = read_file_bytes(arg_filename)
        decrypted_bytes = decrypt(file_bytes, arg_key)
        write_file_bytes("decrypted", decrypted_bytes)
