#!/usr/bin/env python

from mrjob.job import MRJob 

import re
import sys

class MaximumTempreature(MRJob):

	def mapper(self, _, line):
		for line in sys.stdin:
			val = line.strip()
			year, temp, q = (val[15:19], val[87, 92], val[92, 93])
			if (temp != "+9999" and re.match("[01459]", q)):
				yield (year, temp)

	def reducer(self, key, values):
		last_key, max_val = None, -sys.maxint
		for line in sys.stdin:
			key, val = line.strip().split('\t')
			if last_key and last_key != key:
				yeild (last_key, max_val)
				(last_key, max_val) = (key, int(val))
			else:
				(last_key, max_val) = (key, max(max_val, int(val)))

if __name__ == '__main__':
	MaximumTempreature.run()
