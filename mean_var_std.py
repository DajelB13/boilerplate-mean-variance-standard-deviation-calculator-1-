import numpy as np


#receives a list of 9 numbers, reshaped into a 3x3 numpy matrix to determine mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements; returns a dictionary of all calculations
def calculate(list):
  try:
    array = np.array(list)
    array = np.reshape(array, (3, 3))

    #find mean - columns
    meanCol1 = np.mean(array[:, 0])
    meanCol2 = np.mean(array[:, 1])
    meanCol3 = np.mean(array[:, 2])
    meanCols = [meanCol1, meanCol2, meanCol3]

    #find mean - rows
    meanRow1 = np.mean(array[0, :])
    meanRow2 = np.mean(array[1, :])
    meanRow3 = np.mean(array[2, :])
    meanRows = [meanRow1, meanRow2, meanRow3]

    #find mean - total average
    meanTotal = np.mean(array)

    #find variance - columns
    varCol1 = np.var(array[:, 0])
    varCol2 = np.var(array[:, 1])
    varCol3 = np.var(array[:, 2])
    varCols = [varCol1, varCol2, varCol3]

    #find variance - rows
    varRow1 = np.var(array[0, :])
    varRow2 = np.var(array[1, :])
    varRow3 = np.var(array[2, :])
    varRows = [varRow1, varRow2, varRow3]

    #find variance - total
    varTotal = np.var(array)

    #find std deviation - columns
    stdCol1 = np.std(array[:, 0])
    stdCol2 = np.std(array[:, 1])
    stdCol3 = np.std(array[:, 2])
    stdCols = [stdCol1, stdCol2, stdCol3]

    #find std deviation - rows
    stdRow1 = np.std(array[0, :])
    stdRow2 = np.std(array[1, :])
    stdRow3 = np.std(array[2, :])
    stdRows = [stdRow1, stdRow2, stdRow3]

    #find std deviation - total
    stdTotal = np.std(array)

    #find max - columns
    maxCol1 = np.max(array[:, 0])
    maxCol2 = np.max(array[:, 1])
    maxCol3 = np.max(array[:, 2])
    maxCols = [maxCol1, maxCol2, maxCol3]

    #find max - rows
    maxRow1 = np.max(array[0, :])
    maxRow2 = np.max(array[1, :])
    maxRow3 = np.max(array[2, :])
    maxRows = [maxRow1, maxRow2, maxRow3]

    #find max - total
    maxTotal = np.max(array)

    #find min - columns
    minCol1 = np.min(array[:, 0])
    minCol2 = np.min(array[:, 1])
    minCol3 = np.min(array[:, 2])
    minCols = [minCol1, minCol2, minCol3]

    #find min - rows
    minRow1 = np.min(array[0, :])
    minRow2 = np.min(array[1, :])
    minRow3 = np.min(array[2, :])
    minRows = [minRow1, minRow2, minRow3]

    #find min - total
    minTotal = np.min(array)

    #find sum - columns
    sumCol1 = np.sum(array[:, 0])
    sumCol2 = np.sum(array[:, 1])
    sumCol3 = np.sum(array[:, 2])
    sumCols = [sumCol1, sumCol2, sumCol3]

    #find sum - rows
    sumRow1 = np.sum(array[0, :])
    sumRow2 = np.sum(array[1, :])
    sumRow3 = np.sum(array[2, :])
    sumRows = [sumRow1, sumRow2, sumRow3]

    #find sum - total
    sumTotal = np.sum(array)

    #create and return dictionary with calculations
    calculations = {
      'mean': [meanCols, meanRows, meanTotal],
      'variance': [varCols, varRows, varTotal],
      'standard deviation': [stdCols, stdRows, stdTotal],
      'max': [maxCols, maxRows, maxTotal],
      'min': [minCols, minRows, minTotal],
      'sum': [sumCols, sumRows, sumTotal]
    }
    return calculations

  except:
    raise ValueError("List must contain nine numbers.")
