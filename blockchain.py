import client
import transaction
import block


class BlockChain:

    last_block_hash = ''

    @staticmethod
    def create_first_block(self):
        user = client.Client()
        t0 = transaction.Transaction('Genesis', user.identity, 500.0)
        b0 = block.Block()
        b0.previous_block_hash = None
        b0.Nonce = None
        b0.verified_transactions.append(t0)
        digest = hash(b0)
        self.last_block_hash = digest