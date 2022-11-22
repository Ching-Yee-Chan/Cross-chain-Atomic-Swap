from bitcoin.core.script import *

######################################################################
# This function will be used by Alice and Bob to send their respective
# coins to a utxo that is redeemable either of two cases:
# 1) Recipient provides x such that hash(x) = hash of secret 
#    and recipient signs the transaction.
# 2) Sender and recipient both sign transaction
# 
# TODO: Fill this in to create a script that is redeemable by both
#       of the above conditions.
# 
# See this page for opcode: https://en.bitcoin.it/wiki/Script
#
#

# This is the ScriptPubKey for the swap transaction
def coinExchangeScript(public_key_sender, public_key_recipient, hash_of_secret):
    return [
        public_key_recipient,       #首先驗證對方簽名，兩種方式都需要
        OP_CHECKSIGVERIFY, 
        OP_IF,                      #為1時，表明用兩個簽名贖回
        public_key_sender,          #驗證創建者簽名
        OP_CHECKSIG, 
        OP_ELSE,                    #為0時，表明用secret x贖回
        OP_HASH160,                 #與所存H(x)比較
        hash_of_secret,
        OP_EQUAL, 
        OP_ENDIF
    ]

# This is the ScriptSig that the receiver will use to redeem coins
def coinExchangeScriptSig1(sig_recipient, secret):
    return [
        secret, 
        OP_0, 
        sig_recipient
    ]

# This is the ScriptSig for sending coins back to the sender if unredeemed
def coinExchangeScriptSig2(sig_sender, sig_recipient):
    return [
        sig_sender, 
        OP_1, 
        sig_recipient
    ]

#
#
######################################################################

