# histPlot
Plot histograms from data list in lines


`Usage: histPlot.py [--help] [options] numbersList`

Utility for plot histgram from a file with numbers list in lines

```
Options:
  -h, --help            show this help message and exit
  -T PLOTTYPE, --Type=PLOTTYPE
                        plot type lineplot or hitogram [line|hist]
  -o OUTPUT, --output=OUTPUT
                        output filename [default: output.pdf]
  -t TITLE, --title=TITLE
                        figure title
  -x XLAB, --xlabel=XLAB
                        xlabel
  -y YLAB, --ylabel=YLAB
                        ylabel
  --logy                set log scale y axis
  -l LABEL, --legend=LABEL
                        legend of the figure
```


input numbersList example:
```
0.60629
1.02817
0.67808
1.07342
0.62173
0.78609
0.75305
0.55838
0.54763
0.79545
0.76268
0.63324
0.69430
...
```
