# -*- coding: utf-8 -*-

from ethereum.abi import encode_abi, encode_int

def encode_calldata(arg_types, args):
    args = encode_abi(arg_types, args)
    return args.hex()

if __name__ == '__main__':
    print(encode_abi(['uint256'], [12345]))