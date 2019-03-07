import os

import luigi

class GetData(luigi.Task):

    def requires(self):
        return []

    def output(self):
        return luigi.LocalTarget("billboard.csv")

    def run(self):
        os.system('python 01-get_data.py')


class CleanData(luigi.Task):
    def requires(self):
        return[GetData()]

    def output(self):
        return luigi.LocalTarget("billboard_tidy.csv")


    def run(self):
        os.system('python 02-clean_data.py')


class EDA(luigi.Task):
    def requires(self):
        return(CleanData())

    def output(self):
        luigi.LocalTarget("eda.csv")

    def run(self):
        os.system('python 03-eda.py')

if __name__ == '__main__':
    luigi.run()