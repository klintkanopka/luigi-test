#!/usr/bin/env python

import luigi
import subprocess
import pandas as pd

class FetchData(luigi.Task):
    
    def output(self):
        return luigi.LocalTarget('data/covid-bay-data.csv')

    def run(self):
        df = pd.read_csv('https://raw.githubusercontent.com/klintkanopka/COVID-19/master/data/bay_area_agg.csv')
        df = df.drop(columns=['positive', 'negative', 'tested'])
        df.to_csv('data/covid-bay-data.csv')

class CreatePlot(luigi.Task):

    def requires(self):
        return FetchData()

    def output(self):
        return luigi.LocalTarget('fig/covid-bay-plot.png')

    def run(self):
        subprocess.call('src/plot_data.R')
