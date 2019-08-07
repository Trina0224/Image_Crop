"""
This script is a tool to crop images with known bbox. 
It's for Tensorflow classification 

Ref: https://www.geeksforgeeks.org/working-images-python/
Ref: https://www.e-education.psu.edu/geog485/node/141
Ref: https://stackoverflow.com/questions/15718068/search-file-and-find-exact-match-and-print-line
Ref: https://qiita.com/visualskyrim/items/1922429a07ca5f974467
Ref: https://stackoverflow.com/questions/12517451/automatically-creating-directories-with-file-output


Usage: (For Windows)
python ImageCrop.py --input images --output test

"""
import os
import argparse
import csv
from PIL import Image


def Get_4_numbers(string, fp):
    for line in fp:
        if string in line:
            FourNumbers=line.split(' ')
            #return x,y,w,h so, we need x,y,w+x,h+y for crop
            return float(FourNumbers[2]),float(FourNumbers[3]),float(FourNumbers[4])+float(FourNumbers[2]),float(FourNumbers[5])+float(FourNumbers[3])



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--input', help='image folor name',required=True)
    parser.add_argument(
            '--output', help='output folder name',required=True)
    parser.add_argument(
            '--bbox', help='bbox text inputput file.')
    parser.add_argument(
            '--index', help='image index text file.')
    args = parser.parse_args()

    if not args.bbox:
        bboxfile = './bounding_boxes.txt'
    else:
        bboxfile = args.bbox

    if not args.index:
        indexfile = './images.txt'
    else:
        indexfile = args.index

    #Create out.txt for usage later. We need this file for index right picture and crop right regions.
    #I will update this to [] later
    with open(indexfile) as f1,open(bboxfile) as f2,open("out.txt","w") as f3:
        for x,y in zip(f1,f2):
            locations=y.split(' ')
            f3.write(x.strip()+" "+locations[1]+" "+locations[2]+" "+locations[3]+" "+locations[4]+'\n')
    f3.close()
    
    #I know it's stupid. update later.. actually we dont need f3.
    lineList = [line.rstrip('\n') for line in open("out.txt")]
    
    for path, subdirs,files in os.walk(args.input):
        for name in files:
            FilePath=os.path.join(os.getcwd(), path, name)
            #print(FilePath)
            print(name)
            a,b,c,d = Get_4_numbers(name, lineList)
            
            #print(a,b,c,d)
            savefileto=".\\"+args.output+"\\"+path+"\\"+name
            #print("filesaveto:{}".format(savefileto))

            img = Image.open(FilePath) 
            #width, height = img.size 
          
            area = (int(a), int(b), int(c), int(d)) 
            img = img.crop(area) 
          
            #Saved in the same relative location 
            #img.save(savefileto)  

            if not os.path.exists(os.path.dirname(savefileto)):
                try:
                    os.makedirs(os.path.dirname(savefileto))
                except OSError as exc: # prevent race condition
                    if exc.errno != errno.EEXIST:
                        raise            
            img.save(savefileto)  
            


if __name__ == '__main__':
    main()

