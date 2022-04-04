

def capturing_rainwater(heights):
  if len(heights) < 3:
    return 0
  previousMax = getFirstMax(heights)
  waterBucketTotal = 0
  for i in range(previousMax[1], len(heights[1:])):
    nextMax = findNextMax(heights[i:], previousMax)
    try:
      nextMax[1] = heights[i:].index(nextMax[0]) + i
    except:
      break
    if (abs(previousMax[1] - nextMax[1]) > 1):
      minMax = getMin(previousMax[0], nextMax[0])
      valuesBetween = getValuesBetween(heights, previousMax, nextMax)
      waterBucketTotal += ((minMax * valuesBetween[1]) - valuesBetween[0])
    previousMax = nextMax
    
  return waterBucketTotal

def findNextMax(arr, prev):
  max = 0
  for a in arr:
    if a > max:
      max = a
    if max > prev[0]:
      return [max, 0]
  return [max, 0]

def getMin(a, b):
  if a < b:
    return a
  return b

def getValuesBetween(arr, a, b):
  iterations = 0
  total = 0
  for val in arr[a[1]+1:b[1]]:
    iterations += 1
    total += val
  return [total, iterations]

def getFirstMax(arr):
  previous = arr[0]
  for a in arr[1:]:
    if (a < previous):
      return [previous, arr.index(previous)]
    previous = a
  return [previous, arr.index(previous)]
