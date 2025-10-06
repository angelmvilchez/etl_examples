# ETL examples

ETL examples using Python and different data sources.

Location: [/python](/python)

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pandas.

```bash
pip install pandas
```

## Description

### Flat files ETL

This case consists in creating two reports of total amount spent by region and category, respectively. The source of the data are three files located in [/data](/data), with the execution returning the output in it's corresponding directory [/output](/output).

#### Data sources
- customers.csv
- orders.csv
- products.csv

#### Output files
- spent_by_region.csv
- spent_per_category.csv

#### PD: Each .py file contains more details commented inside the code.

## Usage

### Flat files ETL

```bash
git clone https://github.com/angelmvilchez/etl_examples.git
```

#### Execute [file_example.py](/python/file_example.py).
