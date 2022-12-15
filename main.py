import os

PFS = '/pfs'
INPUT  = '/pfs/data'
OUTPUT = '/pfs/out'

if __name__ == "__main__":
    print('Input folder content:')
    print(os.listdir(PFS))
    print('Environment variables:')
    print(os.environ)
