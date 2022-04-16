from datetime import datetime
import hashlib
from transaction import Transaction


class Block:
    def __init__(self, date, transaction, prev_hash=None):
        self.__date = date
        self.__transaction = transaction
        self.__prev_hash = prev_hash
        self.__nonce = 0
        self.__hash = self.calculate_hash()

    def calculate_hash(self):
        date = str(self.__date).encode()
        transaction = str(self.__transaction).encode()
        prev_hash = self.__prev_hash.hexdigest().encode() if self.__prev_hash else str(None).encode()
        nonce = str(self.__nonce).encode()
        return hashlib.sha256(date + transaction + prev_hash + nonce)

    def mine_block(self, difficulty):
        while self.__hash.hexdigest()[0:difficulty] != '0' * difficulty:
            self.__nonce +=1
            self.__hash = self.calculate_hash()

    def get_hash(self):
        return self.__hash

    def get_prev_hash(self):
        return self.__prev_hash

    def set_prev_hash(self, _hash):
        self.__prev_hash = _hash


    def __str__(self):
        if self.__prev_hash is None:
            return f"Block: {self.get_hash().hexdigest()};Transaction: {self.__transaction}; Previous hash: {None}"
        return f"Block: {self.get_hash().hexdigest()};Transaction: {self.__transaction}; Previous hash: {self.get_prev_hash().hexdigest()}"


if __name__=="__main__":
    # GENESIS BLOCK
    b1 = Block(datetime.now(), Transaction("Nexi", "Lia", 1))

    b2 = Block(datetime.now(),Transaction('F', 'I', 25), b1.get_hash())
    b3 = Block(datetime.now(),Transaction('K', 'L', 100), b2.get_hash())

    print(b1)
    print(b2)
    print(b3)


