import os

INPUT  = '/pfs/images'
OUTPUT = '/pfs/out'

if __name__ == "__main__":
    print('Input folder content:')
    print(os.listdir(INPUT))
