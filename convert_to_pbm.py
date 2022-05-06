import argparse
from PIL import Image, ImageFilter


parser=argparse.ArgumentParser(description='Convert_to_pbm tool')
parser.add_argument('-f', required=True, help='Enter filename path')
#parser.add_argument('-s', help='Enter resize (64,64)')
args=parser.parse_args()

filename=args.f
#size=args.s

#Get bite array for oled display
def get_data_array(filename):
    with open(filename, 'rb') as f:
        f.readline()
        f.readline()
        data = bytearray(f.read())
    return data

#Convert any simple image to .pbm format and show data array for oled display
def convert_to_pbm(filename,size=(32,32)):
    img = Image.open(filename).convert('1')
    img = img.resize(size)
    img.save(f'{filename.split(".")[0]}.pbm')
    with open(f'{filename.split(".")[0]}.pbm', 'rb') as f:
        f.readline()
        f.readline()
        data = bytearray(f.read())
    return data

#Simple pre correct image
def pbm_correct(filename,size=(32,32)):
    img = Image.open(filename).convert('L')
    img=img.filter(ImageFilter.GaussianBlur(radius = 0.1))
    img = img.resize(size)
    img.save(f'{filename.split(".")[0]}.pbm')

#Add GaussianBlur
def gauss(filename):
    img = Image.open(filename).convert('L')
    img = img.filter(ImageFilter.GaussianBlur(radius=2))
    img.save(filename)

#Simple resize img
def resize(filename,size=(32,32)):
    img = Image.open(filename).convert('1')
    img = img.resize(size)
    img.save(filename)

def main():
    print(f'Convert finish!!!\nCopy bytearray\n')
    print(convert_to_pbm(filename))

if __name__ == '__main__':
    main()

