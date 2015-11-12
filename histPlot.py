#!/usr/bin/env python
import numpy as np
import matplotlib.pylab as plt
import sys
from optparse import OptionParser


class histPlot(object):
    """Utility for plot histgram from a file with numbers list in lines"""
    def __init__(self, argv):
        self.__parseOptions(argv)

    def __parseOptions(self, argv):
        usage = 'Usage: %prog [--help] [options] numbersList'
        parser = OptionParser(usage=usage, description=histPlot.__doc__)
        parser.add_option('-b','--bins', type='int',dest='bins',default=20,
                          help="Number of bins shows in the final plot")
        parser.add_option('-o','--output', type='string',dest='output',
                          help="output filename [default: output.pdf]", default="output.pdf")
        parser.add_option('-t','--title',type="string",dest="title",
                          help="figure title",default="")
        parser.add_option('-x','--xlabel',type="string",dest="xlab",
                          help="xlabel",default="")
        parser.add_option('-y','--ylabel',type="string",dest="ylab",
                          help="ylabel",default="")

        self.options, self.args=parser.parse_args(argv)
        if len(self.args)!=2:
            parser.error('Expected 1 argument')

        self.inFilename = self.args[1]
	self.outFilename = self.options.output
	

    def run(self):
	lines = open(self.inFilename).readlines()
	data = []
	for line in lines:
	    data.append(float(line.strip()))
	x = np.asarray(data)
        plt.figure(figsize=(7,5))
        plt.xlabel(self.options.xlab)
        plt.xlim((0,x.max()))
        plt.ylabel(self.options.ylab)
        plt.title(self.options.title)
	n,bins,patches = plt.hist(x, self.options.bins,  histtype='bar',
                                  color=['crimson'],normed=False, alpha=0.85)
	plt.savefig(self.outFilename)


if __name__ == '__main__':
    app = histPlot(sys.argv)
    sys.exit(app.run())

