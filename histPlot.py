#!/usr/bin/env python
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pylab as plt
import sys
from optparse import OptionParser


class histPlot(object):
    """Utility for plot histgram from a file with numbers list in lines."""
    
    def __init__(self, argv):
        self.__parseOptions(argv)

    def __parseOptions(self, argv):
        usage = 'Usage: %prog [--help] [options] numbersList'
        parser = OptionParser(usage=usage, description=histPlot.__doc__)
        parser.add_option('-T', '--Type',type="string", dest='plotType',default='line',
                          help="plot type lineplot or hitogram [line|hist]")              
        parser.add_option('-o','--output', type='string',dest='output',
                          help="output filename [default: output.pdf]", default="output.pdf")
        parser.add_option('-t','--title',type="string",dest="title",
                          help="figure title",default="")
        parser.add_option('-x','--xlabel',type="string",dest="xlab",
                          help="xlabel",default="")
        parser.add_option('-y','--ylabel',type="string",dest="ylab",
                          help="ylabel",default="")        
        parser.add_option('--logy', action = 'store_true',dest='logy',default=False,
                          help="set log scale y axis")        
        parser.add_option('-l','--legend',type="string",dest="label",
                          help="legend of the figure",default="")        

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
        fig = plt.figure(figsize=(7, 3))        
     
        ax = fig.add_subplot(111)
        plt.subplots_adjust(left = 0.15, bottom = 0.15, wspace = 0)
        plt.xlabel(self.options.xlab)
       
        
        plt.ylabel(self.options.ylab)
        if self.options.logy == True:
            ax.set_yscale('log')
        plt.title(self.options.title)
        if self.options.plotType == 'hist':
            plt.xlim(0,x.max())
            n,bins,patches = plt.hist(x, 20,  histtype='bar',
                                 color=['crimson'],normed=False, alpha=0.85)
        else:
            plt.xlim(0,x.size)
            line, = plt.plot(range(x.size), x, 'r-', label = self.options.label)
        ax.legend()
        plt.savefig(self.outFilename)


if __name__ == '__main__':
    app = histPlot(sys.argv)
    sys.exit(app.run())