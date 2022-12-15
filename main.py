import os

INPUT  = '/pfs/data'
OUTPUT = '/pfs/out'

if __name__ == "__main__":
    print('Input folder content:')
    print(os.listdir(INPUT))
    print('Environment variables:')
    print(os.environ)
