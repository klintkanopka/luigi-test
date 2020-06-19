#!/usr/bin/Rscript

library(tidyverse)

p <- read_csv('data/covid-bay-data.csv') %>% 
  select(-X1, Date = date, `Confirmed Cases` = cases, Deaths = deaths) %>% 
  pivot_longer(-Date, names_to='Type', values_to='Count') %>% 
  ggplot(aes(x=Date, y=Count, color=Type)) + 
  geom_line() +
  ggtitle('Bay Area COVID-19 Numbers') + 
  theme_bw()

ggsave('fig/covid-bay-plot.png')
