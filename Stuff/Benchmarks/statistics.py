# NEEDS DATA
# statistics
#!/usr/bin/python
# $Id: moments-python.code,v 1.7 2004/12/05 01:58:28 bfulgham Exp $
# http://shootout.alioth.debian.org/
#
# Updated by Antoine Pitrou
# 1.  Simple loops are often faster than 'reduce'.
# 2.  'abs' function is referenced by a local variable.  (Local variables
#     are optimized by the Python interpreter.
# 3.  Some loop invariants are lifted to tighten up the code.

import sys, string, math


#DEJAVU
'''
{
'NAME':"Statistics",
'DESC':"Statistics from computer language shootout",
'GROUP':'real-bench',
'CMPOUT':1,
'ARGS':"1",
'BARGS':"1000",
}
'''

def main(N):
	sum = 0
	nums = []
	_abs = abs

	nums = [float(s) for s in file('DATA/moments-input.txt')]
	for CNT in N:
	 for num in nums:
		sum += num

	 n = len(nums)
	 mean = sum/n
	 average_deviation = 0
	 standard_deviation = 0
	 variance = 0
	 skew = 0
	 kurtosis = 0

	 for num in nums:
		deviation = num - mean
		d2 = deviation**2
		average_deviation += _abs(deviation)
		variance += d2
		skew += deviation*d2
		kurtosis += d2**2

	 average_deviation /= n
	 variance /= (n - 1)
	 standard_deviation = math.sqrt(variance)

	 if variance > 0.0:
		skew /= (n * variance * standard_deviation)
		kurtosis = kurtosis/(n * variance * variance) - 3.0

	 nums.sort()
	 mid = n / 2

	 if (n % 2) == 0:
		median = (nums[mid] + nums[mid-1])/2
	 else:
		median = nums[mid]

	print "n:                  %d" % n
	print "median:             %f" % median
	print "mean:               %f" % mean
	print "average_deviation:  %f" % average_deviation
	print "standard_deviation: %f" % standard_deviation
	print "variance:           %f" % variance
	print "skew:               %f" % skew
	print "kurtosis:           %f" % kurtosis

main(range (int (sys.argv [1])))
