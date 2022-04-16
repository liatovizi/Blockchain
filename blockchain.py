from block import Block
from datetime import datetime
from transaction import Transaction

class Blockchain:
    def __init__(self):
        self.__chain = [Block(datetime.now(), Transaction('A', 'B', 66))]
        self.__difficulty = 4
        if self.__chain[0].get_prev_hash() is None:
            self.__chain[0].mine_block(self.__difficulty)

    def add_block(self, new_block):
        new_block.set_prev_hash(self.get_last_block().get_hash())
        new_block.mine_block(self.__difficulty)
        self.__chain.append(new_block)

    def get_last_block(self):
        return self.__chain[-1]

    def show_chain(self):
        for block in self.__chain:
            print(block)

    def is_chain_valid(self):
        for index, block in enumerate(self.__chain):
            current_block = self.__chain[index]
            previous_block = self.__chain[index -1]

            if current_block.get_hash().hexdigest() != current_block.calculate_hash().hexdigest():
                return False
            if current_block.get_prev_hash() is not None:
                if current_block.get_prev_hash().hexdigest() != previous_block.get_hash().hexdigest():
                    return False
        return True

if __name__ == "__main__":
    NexiCoin = Blockchain()
    NexiCoin.add_block(Block(datetime.now(), Transaction('R', 'L', 80)))
    NexiCoin.add_block(Block(datetime.now(), Transaction('B', 'D', 99)))

    NexiCoin.show_chain()
    print(F' Is chain valid? {NexiCoin.is_chain_valid()}')