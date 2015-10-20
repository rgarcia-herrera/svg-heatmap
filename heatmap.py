from symmheat import *

samples = [
    'adm1',
    'adm2',
    'adm3',
    'tep1',
    'tep2',
    'tar1',
    'tar2',
    'tot1',
    'tot2',
    'zap1',
    'zap2',
    'nah1',
    'nah2',
    'may1',
    'may2',
]

pairs = { ('adm1', 'may2') : 2325281,
          ('tot2', 'zap2') : 2395415,
          ('tot1', 'nah1') : 2382490,
          ('may1', 'tep1') : 2353029,
          ('tep2', 'nah1') : 2344770,
          ('tot2', 'adm3') : 2289440,
          ('zap1', 'zap2') : 2390450,
          ('adm1', 'adm2') : 2293905,
          ('zap1', 'tep1') : 2348760,
          ('tar1', 'nah2') : 2344735,
          ('tot2', 'tot1') : 2469812,
          ('nah1', 'may2') : 2392002,
          ('adm1', 'adm3') : 2779347,
          ('may1', 'adm2') : 2284289,
          ('nah2', 'nah1') : 2373961,
          ('nah1', 'zap2') : 2385882,
          ('may2', 'may1') : 2411659,
          ('zap1', 'tot1') : 2373545,
          ('adm1', 'nah2') : 2316735,
          ('tar1', 'may1') : 2353554,
          ('tep2', 'tar2') : 2332148,
          ('adm1', 'may1') : 2330973,
          ('zap2', 'adm2') : 2275730,
          ('nah1', 'adm2') : 2268358,
          ('tot1', 'tep1') : 2350471,
          ('adm3', 'tar2') : 2257514,
          ('zap1', 'tot2') : 2393498,
          ('tep2', 'zap1') : 2338436,
          ('zap2', 'tep1') : 2356340,
          ('nah1', 'tep1') : 2359761,
          ('adm1', 'tep1') : 2312421,
          ('may2', 'adm2') : 2278849,
          ('tep2', 'tar1') : 2336437,
          ('may2', 'adm3') : 2292290,
          ('tot1', 'adm2') : 2270089,
          ('zap1', 'adm3') : 2287291,
          ('adm1', 'nah1') : 2310322,
          ('tot2', 'may1') : 2396921,
          ('may1', 'tar2') : 2350836,
          ('tot1', 'may2') : 2383942,
          ('adm1', 'zap2') : 2332523,
          ('tar1', 'tep1') : 2336928,
          ('adm2', 'tar2') : 2237841,
          ('tep2', 'may2') : 2358657,
          ('tot2', 'tar2') : 2351905,
          ('nah2', 'adm2') : 2265470,
          ('zap1', 'may1') : 2389671,
          ('tar1', 'adm2') : 2257916,
          ('zap1', 'tar2') : 2342447,
          ('tar1', 'nah1') : 2349414,
          ('tot1', 'tar2') : 2340479,
          ('tot1', 'may1') : 2383250,
          ('nah2', 'zap2') : 2386562,
          ('tep2', 'may1') : 2354608,
          ('nah2', 'tep1') : 2343591,
          ('tot2', 'adm2') : 2268229,
          ('zap1', 'may2') : 2383705,
          ('nah2', 'adm3') : 2283741,
          ('adm1', 'tot1') : 2318601,
          ('tep2', 'tep1') : 2390953,
          ('tep1', 'tar2') : 2319075,
          ('nah1', 'adm3') : 2288034,
          ('adm3', 'tep1') : 2290190,
          ('tot2', 'adm1') : 2321360,
          ('zap1', 'tar1') : 2336632,
          ('may1', 'zap2') : 2393289,
          ('tep2', 'adm2') : 2254839,
          ('zap2', 'adm3') : 2295672,
          ('may2', 'tep1') : 2343517,
          ('tep2', 'tot2') : 2346904,
          ('nah1', 'tar2') : 2328799,
          ('tot2', 'may2') : 2405035,
          ('tep2', 'tot1') : 2342836,
          ('adm1', 'tar2') : 2291406,
          ('tar1', 'may2') : 2357268,
          ('tep2', 'adm1') : 2294796,
          ('tot2', 'tar1') : 2353874,
          ('tot1', 'zap2') : 2377513,
          ('may1', 'adm3') : 2306530,
          ('nah2', 'may1') : 2389674,
          ('tep2', 'zap2') : 2358718,
          ('nah2', 'tar2') : 2344564,
          ('zap2', 'tar2') : 2341652,
          ('tot2', 'tep1') : 2358732,
          ('zap1', 'nah1') : 2374440,
          ('tar1', 'adm3') : 2273468,
          ('tar1', 'tot1') : 2340187,
          ('tot2', 'nah2') : 2390414,
          ('tar1', 'tar2') : 2387099,
          ('nah2', 'may2') : 2402294,
          ('nah1', 'may1') : 2385340,
          ('may2', 'zap2') : 2390302,
          ('zap1', 'nah2') : 2374940,
          ('tar1', 'adm1') : 2293645,
          ('zap1', 'adm1') : 2314168,
          ('tar1', 'zap2') : 2345064,
          ('may2', 'tar2') : 2354731,
          ('tep1', 'adm2') : 2265813,
          ('tot1', 'adm3') : 2292756,
          ('tot2', 'nah1') : 2380673,
          ('adm3', 'adm2') : 2767276,
          ('tot1', 'nah2') : 2379684,
          ('tep2', 'nah2') : 2344523,
          ('zap1', 'adm2') : 2271876,
          ('tep2', 'adm3') : 2274094 }



h = Heatmap('prueba.svg', samples, pairs)
h.draw()
h.save()
