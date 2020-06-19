# luigi-test
new boot goofin' with luigi to schedule Python and R tasks

![Doin' Thangs](https://img.discogs.com/4CuTJ1wi-xQtzsmuhijlbaVbhNo=/fit-in/600x579/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-1491773-1550557303-7099.png.jpg)

First install `luigi` (more info [here](https://luigi.readthedocs.io/en/stable/))
```
pip install luigi
```

Then you can try to create a plot from the command line:
```
luigi --module luigi_tasks CreatePlot --local-scheduler
```

If it complains about the module not being found, you can try:
```
PYTHONPATH='.' luigi --module luigi_tasks CreatePlot --local-scheduler
```

It won't actually do anything, because the target files (or products) already exist. If you clear out everything in the `data` and `fig` folders and rerun, you'll see that it knows that `CreatePlot` depends on `FetchData` and will run that first. Cool.

There's also a central scheduler that you can invoke and mess around with to see the dependency graph and all, but this example is pretty much trivial.
