import sys  # only use python standard library
import csv
from datetime import datetime
from math import ceil


class BorderAnalytics:
    """The class to analyse the border crossing data."""

    def __init__(self):
        self.data = []      # list for loading the useful data from CSV
        self.crossing = {}  # dictionary with date,border,measure as a key and sum of the values as value
        self.year_list = []  # year list
        self.border_measure_list = []  # border_measure list
        self.total = []  # list of running averages
        self.report = []  # unsorted list of results
        self.sorted_report = []  # sorted based on Date, Value, Measure and Border

    def read_input(self, infile):
        """Reads input CSV file as the list of lists"""
        with open(infile) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            for row in reader:
                self.data.append([str(row[4]), str(row[3]), str(row[5]), int(row[6])])

    def value_sum(self):
        """calculate the value of each type, regardless of port entered."""
        for row in self.data:
            id = ','.join([row[0], row[1], row[2]])  # create a unique dict key with Date, Border and Measure
            if id not in self.crossing:
                self.crossing[id] = row[3]
            else:
                self.crossing[id] += row[3]

    def prepare(self):
        """outputs year_list and border_measure_list in order to calculate the running average."""
        for k, v in self.crossing.items():
            date = k.split(',')[0]
            year = int(date[6:10])
            border_measure = ','.join([k.split(',')[1], k.split(',')[2]])
            if year not in self.year_list:
                self.year_list.append(year)
            if border_measure not in self.border_measure_list:
                self.border_measure_list.append(border_measure)

    def running_avg(self):
        """calculate the running average"""
        for y in self.year_list:
            yearly_crossing = {k: v for (k, v) in self.crossing.items() if str(y) in k}
            for border_measure in self.border_measure_list:
                dd = dict(sorted((k, v) for (k, v) in yearly_crossing.items() if border_measure in k))
                dd_value = list(dd.values())
                cumsum, rolling_avg = [0], [0]           # rolling average of January is 0 based on instruction
                for i, x in enumerate(dd_value, 1):      # loop over enumerated value_sum within each year
                    cumsum.append(cumsum[i - 1] + x)     # sum up the value sum of previous months
                    rolling_avg.append(ceil((cumsum[i - 1] + x) / i))     # cumsum of previous months divided by months
                rolling_avg.pop()                        # delete the 13th rolling average of each year
                list_avg = list(zip(dd.keys(), dd.values(), rolling_avg))
                self.total.append(list_avg)
        for i in self.total:
            for j in i:
                self.report.append([str(list(j)[0]).split(',')[1], str(list(j)[0]).split(',')[0],
                                    str(list(j)[0]).split(',')[2], list(j)[1], list(j)[2]])
        self.sorted_report = sorted(self.report, key=lambda y: (datetime.strptime(y[1], '%m/%d/%Y %I:%M:%S %p'),
                                                                y[3], y[2], y[0]), reverse=True)

    def write_output(self, outfile):
        """writes the result in a CSV file"""
        with open(outfile, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            header = ["Border", "Date", "Measure", "Value", "Average"]
            writer.writerow(header)
            for line in self.sorted_report:
                writer.writerow(line)


if __name__ == '__main__':
    """Instantiate and execute the BorderAnalytics class"""
    infile = sys.argv[1]
    outfile = sys.argv[2]
    ba = BorderAnalytics()
    ba.read_input(infile)
    ba.value_sum()
    ba.prepare()
    ba.running_avg()
    ba.write_output(outfile)
