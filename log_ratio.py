#!/usr/bin/env python

import sys
import argparse
import math

class DepthRecord(object):

    def __init__(self, fields):
        self.chrom = fields[0]
        self.start = int(fields[1])
        self.end = int(fields[2])
        self.depth = int(fields[3])
        self.gc = float(fields[4])
        self.gc_mean = float(fields[5])
        self.gc_stdv = float(fields[6])
        self.Z = float(fields[7])

def main():

    #########################################
    # create the top-level parser
    #########################################
    parser = argparse.ArgumentParser(prog='chromcopy')
    parser.add_argument("-v", "--version", help="Installed chromcopy version",
                        action="version")
    parser.add_argument("-1", dest='depth_file1', help="The numeration depth file.")
    parser.add_argument("-2", dest='depth_file2', help="The denominator depth file.")

    args = parser.parse_args()

    if args.depth_file1 is None or args.depth_file2 is None:
        sys.exit('EXITING. You must specify -1 and -2.\n')

    depths_file2 = []
    for line in open(args.depth_file2):
        fields = line.strip().split('\t')
        rec2 = DepthRecord(fields)
        depths_file2.append(rec2.depth)

    for idx, line in enumerate(open(args.depth_file1)):
        fields = line.strip().split('\t')
        rec1 = DepthRecord(fields)
        log2_ratio = math.log((float(rec1.depth + 1) / float(depths_file2[idx] + 1)),2)
        print '\t'.join([str(s) for s in [rec1.chrom, rec1.start, rec1.end, log2_ratio]])


if __name__ == "__main__":
    main()