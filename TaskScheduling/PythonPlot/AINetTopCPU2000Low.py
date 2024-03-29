#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import matplotlib.pyplot as plt

GA = {0: 5559.644157914909, 1: 1277.475204017577, 2: 2987.0000000000005, 3: 6053.000000000001,
      4: 5522.000000000001, 5: 5460.000579842832, 6: 5594.000274662394, 7: 6028.000000000001,
      8: 6580.000000000001, 9: 8438.0}

ACOInt = {0: 5178.000015259022, 1: 1172.5813152938354, 2: 1010.3887652452595, 3: 3315.2061876470243,
          4: 1485.9457782990512, 5: 3334.0000000000005, 6: 3271.0000000000005, 7: 5694.000000000001,
          8: 6210.000000000001, 9: 7454.000000000001}

IWC = {0: 5559.644157914909, 1: 1277.475204017577, 2: 2987.0000000000005, 3: 5777.000717174029,
       4: 3894.0000000000005, 5: 5525.000000000001, 6: 5622.000000000001, 7: 6028.000000000001,
       8: 6300.000000000001, 9: 8040.000000000001}

PSOInt = {0: 5178.026135904063, 1: 1139.32647365602, 2: 1012.2062977386718, 3: 2096.0005340657663,
          4: 1408.49163116901, 5: 1370.0898489914134, 6: 1547.000289921416, 7: 2442.044362043042,
          8: 3048.178215125852, 9: 4574.0}

WOAInt = {0: 5178.022999318477, 1: 1072.7851518686593, 2: 977.0616477852002, 3: 5474.0, 4: 1742.4974288102026,
          5: 1215.668104914745, 6: 1502.0003051804379, 7: 1911.3152759980499, 8: 2470.102871115104,
          9: 5572.000473029679}

WOABLR = {0: 5178.000015259022, 1: 1083.702506131424, 2: 792.4841326243047, 3: 1690.4913291570356,
             4: 1183.4716768112844, 5: 1270.0, 6: 1376.9962919368882, 7: 1614.992305531448,
             8: 2620.4440841707024, 9: 4854.271391462167}

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
plt.legend(ncol=3, fontsize=10)
plt.savefig("50-svmad-svmm-svm-df-blr.jpg")
plt.show()
