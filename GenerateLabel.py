"""
This script is a tool to create train.txt and test.txt

Usage: (for Linux)
python GenerateLabel.py 

"""
import os
import argparse
#import csv
import random


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--classes', help='classes.txt file.')
    args = parser.parse_args()

    if not args.classes:
        bboxfile = './classes.txt'
    else:
        bboxfile = args.bbox

    lineList = [line.rstrip('\n') for line in open(bboxfile)]
    string4print=""
    labelResult=[]
    with open("./labels.txt", 'w') as f:
        for item in range(len(lineList)):
            Sections=lineList[item].split(' ')
            GetLabel=Sections[1].split('.')
            print(GetLabel[1])
            f.write("%s\n" % GetLabel[1])
        f.close()

if __name__ == '__main__':
    main()

