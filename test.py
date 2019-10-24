import unittest
import client
import transaction
import blockchain


class MyTestCase(unittest.TestCase):
    def test_something(self):
        user = client.Client()
        id = user.identity
        print(id)
        self.assertIsNotNone('Our public key: ' + id)

    def test_transaction(self):
        user1 = client.Client()
        user2 = client.Client()
        trans = transaction.Transaction(user1, user2.identity, 5.0)
        signature = trans.sign_transaction()
        self.assertIsNotNone(signature)
        print('Our signature of transaction: ' + signature)

    def test_create_genesis_block(self):
        bc = blockchain.BlockChain()
        bc.create_first_block(bc)
        print(bc.last_block_hash)


if __name__ == '__main__':
    unittest.main()
