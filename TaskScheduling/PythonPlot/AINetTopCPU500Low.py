#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import matplotlib.pyplot as plt
GA = {0: 5636.2725725048695, 1: 1277.475204017577, 2:3369.0000000000005, 3: 6369.000000000001,
      4: 5943.000000000001, 5: 5910.000000000001, 6: 6020.000000000001, 7: 6409.000000000001,
      8: 7169.000000000001, 9: 10024.0}

ACOInt = {0: 5256.500891724084, 1: 1161.5744087052124, 2: 1160.4974288102026, 3: 3244.3887600539056,
          4: 3725.0, 5: 3900.0000000000005, 6: 5622.000000000001, 7: 5885.000000000001,
          8: 6750.000000000001, 9: 8653.0}

IWC = {0: 5636.2725725048695, 1: 1277.475204017577, 2: 3369.0000000000005, 3: 6369.000000000001,
       4: 5897.000000000001, 5: 3683.0000000000005, 6: 5939.000000000001, 7: 6391.000000000001,
       8: 6908.000000000001, 9: 9630.0}

PSOInt = {0: 5178.027277775824, 1: 1072.8886207381574, 2: 1055.2144131034406, 3: 2904.25717778776,
          4: 2214.59493317903, 5: 1920.7689178979886, 6: 1840.320754374898, 7: 2286.0560575255167,
          8: 3420.9016838674634, 9: 6585.083513114343}

WOAInt = {0: 5433.068867683101, 1: 1072.7851518686593, 2: 1493.0000305180438, 3: 3816.000289921416,
          4: 2746.9130840696876, 5: 2258.438371816127, 6: 2083.0002288853284, 7: 5301.000167849241,
          8: 4318.333410557883, 9: 7143.000701915007}

WOABLR = {0: 5178.022999318477, 1: 1077.628146441922, 2: 1005.9428654455812, 3: 2236.365688449131,
             4: 1720.203868880018, 5: 1625.112838774389, 6: 1541.3897278669347, 7: 2042.0,
             8: 3217.000167849241, 9: 6128.0005035477225}

ga = list(GA.values())
acoInt = list(ACOInt.values())
iwc = list(IWC.values())
psoInt = list(PSOInt.values())
woaInt = list(WOAInt.values())
woablr = list(WOABLR.values())

x = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

plt.plot(x, ga, linestyle="--", marker=",", linewidth='1', label="GA")
plt.plot(x, acoInt, linestyle="--", marker="+", linewidth='1', label="ACO")
plt.plot(x, iwc, linestyle="-.", marker="x", linewidth='1', label="IWC")
plt.plot(x, psoInt, linestyle="-", marker="v", linewidth='1', label="PSO")
plt.plot(x, woaInt, linestyle="-.", marker="*", linewidth='1', label="WOA")
plt.plot(x, woablr, linestyle="-", marker="o", linewidth='1', label="RTGS")
plt.xlabel('task number', fontsize=12)
plt.ylabel('final finish time gap', fontsize=12)
#plt.title("a. busy period; short jobs")
plt.legend(ncol=3, fontsize=10)
plt.savefig("50-svmad-svmm-svm-df-blr.jpg")
plt.show()