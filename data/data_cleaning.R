library(dplyr)

col_names <- read.csv("raw_data.csv", nrows = 88)
data_raw <- read.csv("raw_data.csv", skip = 88)
