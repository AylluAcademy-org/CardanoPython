from src.cardano.base import Node
from src.cardano.base import Keys

node = Node()
key = Keys()

address = 'addr_test1qrp2m43wryxjm95jhq02q4vg8tjq82k5t6paay87u90xyxz6rf3adxm3anceu8wd3zv4gmr4kl5kl3qth4mlqd8alhls4kpp0t'

transactions = node.get_transactions(wallet_id= address)
print(transactions)
# balance = node.get_balance(address)
# print(balance)

# ##########################################
# wallet_name2 = 'ForMinting'

# key_hash = key.keyHashing(wallet_name2)

# script_name = 'ForMinting'
# type = ''
# required = ''

# result = node.create_multisig_script(script_name, type, required, [key_hash])


# #############################################
# address_origin = 'ForMinting'

# address_destin = 'addr_test1qzz7l5yx4pvqcd3lgnay95g7mpn4vfce49htshwtpxw3ypyes4gaskwme3lygpq6elm702mf\
#                     jcyt257lhz6rs80f0x0s50329z'

# # print(node.get_balance(address_destin))

# metadata = {
#     "1456": "Hola Mundo"
# }
# address_destin = [
#         {
#           "address": "addr_test1qzz7l5yx4pvqcd3lgnay95g7mpn4vfce49htshwtpxw3ypyes4gaskwme3lygpq6elm702m\
#                         fjcyt257lhz6rs80f0x0s50329z",  # noqa: E501
#           "amount": {
#                 "quantity": 5000000,
#                 "unit": "lovelace"
#             },
#           "assets": {},
#         },
#       ]

# witness = 1

# hash = key.keyHashing('ForMinting')

# policyID = node.create_multisig_script('ForMinting', 'all', '', [hash])

# policyID = node.create_policy_id('ForMinting')

# scriptName = 'ForMinting'

# mint = {policyID: [{
#     "name": "1042Prueba",
#     "amount": 2
# }]
# }

# params = {
#     "message": {
#         "tx_info": {
#             "address_origin": address_origin,
#             "address_destin": None,
#             "change_address": address_origin,
#             "metadata": metadata,
#             "mint": None,
#             "script_path": None,
#             "witness": witness,
#         }
#     }
# }

# result = node.build_tx_components(**params)
# node.sign_transaction(address_origin)
# node.submit_transaction()
