import math

class FlyGroup:
    # init method or constructor
    def __init__(self, flyArray = []):
        # Using above file path as testing only. Can input other file path instead if necessary.
        self.flyArray = flyArray

    def convert_to_2d_array(self, arr):
        return [[index, value] for index, value in enumerate(arr)]
    # Sample Method
    def printFlies(self):
        print(self.flyArray)

    def appendGroupInterval(self, interval):
        self.flyArray.append(interval)

    def doRegression(self, indexSort = False, Bvalues =
                    [0.270, 0.270, 0.241, 0.199, -0.112, -0.452, -0.577,
                     -0.620, 0.278, 0.482, 0.184, 0.184, -0.702, 0.172,
                     -0.252, 0.179, -0.342, 0.268, 0.268, 0.268, 0.556]
                     , constantBVal = -1.382
                     ):
        #necessary variables for regression
        minuteSums = []

        # Bvalues = [0.270, 0.270, 0.241, 0.199, -0.112, -0.452, -0.577,
        #            -0.620, 0.278, 0.482, 0.184, 0.184, -0.702, 0.172,
        #            -0.252, 0.179, -0.342, 0.268, 0.268, 0.268, 0.556]
        # ExpBvalues = [1.310, 1.310, 1.273, 1.220, 0.894, 0.636, 0.561, 0.538,
        #               1.320, 1.619, 1.202, 1.202, 0.496, 1.188, 0.777,
        #               1.196, 0.710, 1.307, 1.744]

        # constantBVal = -1.382
        constantExpBVal = 0.251

        flyPredVals = []
        # Prediction value = (activity@0)*(0.201) + (activity@6)*(-.429) + … + (activity@20)*(-.901) + (-.901)

        #---
        relativeSeconds = 0
        row = 0
        for interval in self.flyArray:
            #for each interval, increment the relativeSeconds by 15
            #for each fly, keep track of their total movement over minute intervals

            # cuts off early if the file has more than 20 minutes worth of fly data
            if math.floor(relativeSeconds/60) > 20:
                break
            if relativeSeconds%60 == 0:
                minuteSums.append([])


            column = 0
            for activity in interval:
                # print("added row")
                # if column == 2:
                #     #is the time
                if column > 9:
                    # used to find sums for @0, @1, @2, etc. (based on relativeSeconds)
                    adjustedCol = column - 11
                    if relativeSeconds%60 == 0:
                        # minute sums [ interval ] [ fly ]
                        minuteSums[len(minuteSums) - 1].append(float(activity))
                        periodAt = math.floor(relativeSeconds/60)
                        if relativeSeconds == 0:
                                if periodAt > 20:
                                    flyPredVals.append(float(minuteSums[periodAt][adjustedCol]))
                                else:
                                    flyPredVals.append(float(minuteSums[periodAt][adjustedCol])*Bvalues[periodAt])
                        else:
                            if periodAt > 20:
                                flyPredVals[adjustedCol] += float(minuteSums[periodAt][adjustedCol])
                            else:
                                flyPredVals[adjustedCol] += float(minuteSums[periodAt][adjustedCol]) * Bvalues[periodAt]
                    else:
                        minuteSums[len(minuteSums) - 1][adjustedCol] += float(activity)
                    #add the constant value to each minuteSum amount
                    minuteSums[len(minuteSums) - 1][adjustedCol] += constantBVal
                column += 1
            row += 1
            relativeSeconds+=15

        #print out the flyPredVals for now.
        indexedPredVals = self.convert_to_2d_array(flyPredVals)
        # print(indexedPredVals)
        #sort the flyPredVals and keep track of their original indexes.
        indexedPredVals.sort(reverse=True, key=lambda x: x[0 if indexSort else 1])
        self.indexedPredVals = indexedPredVals
        return indexedPredVals
        # sort indexedPredVals

    def top25P(self, indexSort = True):
        indexPredVals = self.doRegression(False)
        numFlies = len(indexPredVals)
        numSuccess = math.floor(numFlies*0.25)
        count = 0
        for tuple in indexPredVals:
            if (count<numSuccess):
                tuple[1] = 1
            else:
                tuple[1] = 0
            count+=1

        if indexSort:
            indexPredVals.sort(key=lambda x : x[0])
        return indexPredVals