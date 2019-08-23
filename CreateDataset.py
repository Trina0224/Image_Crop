"""
This script is a tool to create train.txt and test.txt

Usage: (for Linux)
python CreateDataset.py --train xxx --test yyy

"""
import os
import argparse
#import csv
import random


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--train', help='folor name for train',required=True)
    parser.add_argument(
            '--test', help='folder name for test',required=True)
    parser.add_argument(
            '--bbox', help='bbox text inputput file.')
    parser.add_argument(
            '--index', help='image index text file.')
    args = parser.parse_args()

    if not args.bbox:
        bboxfile = './train_test_split.txt'
    else:
        bboxfile = args.bbox

    if not args.index:
        indexfile = './images.txt'
    else:
        indexfile = args.index

    #Create out.txt for usage later. We need this file for index right picture and crop right regions.
    #I will update this to [] later
    with open(indexfile) as f1,open(bboxfile) as f2,open("out2.txt","w") as f3:
        for x,y in zip(f1,f2):
            locations=y.split(' ')
            f3.write(x.strip()+" "+locations[1])
    f3.close()
    
       
    #I know it's stupid. update later.. actually we dont need f3.
    lineList = [line.rstrip('\n') for line in open("out2.txt")]
    trainlist=[]
    testlist=[]
    string4print=""
    for item in range(len(lineList)):
        Sections=lineList[item].split(' ')
        GetLabel=Sections[1].split('.')
        string4print=Sections[1]+" "+GetLabel[0]
        if int(Sections[2]) == 1:
            trainlist.append(string4print)
        else:
            testlist.append(string4print)
    
    #print("train length:{}".format(len(trainlist))) ==5994
    #print("test length:{}".format(len(testlist))) ==5794
    random.shuffle(trainlist)
    random.shuffle(testlist)

    trainfile="./"+args.train+"/"+"train.txt"
    with open(trainfile, 'w') as f:
        for item in trainlist:
            f.write("%s\n" % item)
        f.close()
    
    testfile="./"+args.test+"/"+"test.txt"
    with open(testfile, 'w') as f:
        for item in testlist:
            f.write("%s\n" % item)
        f.close()        

if __name__ == '__main__':
    main()

