import unittest
from event import Event

data = []
result = []

data.append([(1611330113.866415, 798, 200), (1611330113.872132, 790, 268), (1611330113.886407, 780, 290), (1611330113.891287, 770, 243), (1611330113.906759, 713, 3732), (1611330113.912672, 690, 7643), (1611330113.922061, 679, 4935), (1611330113.936946, 668, 6732), (1611330113.947138, 658, 10181), (1611330113.955433, 647, 13283), (1611330113.95965, 636, 14279), (1611330113.97085, 625, 14698), (1611330113.986711, 615, 16659), (1611330113.989782, 604, 18199), (1611330114.004019, 594, 18048), (1611330114.010409, 585, 18524), (1611330114.01967, 575, 14564), (1611330114.030641, 565, 9463), (1611330114.042567, 556, 5826), (1611330114.054683, 547, 5714), (1611330114.061064, 540, 1768), (1611330114.077835, 536, 770), (1611330114.087101, 530, 513), (1611330114.091696, 523, 600), (1611330114.105431, 514, 1405), (1611330114.118515, 505, 3420), (1611330114.123037, 493, 2024), (1611330114.138365, 491, 2510), (1611330114.146226, 484, 3654), (1611330114.154719, 473, 3351), (1611330114.160844, 462, 2595), (1611330114.171583, 458, 5537), (1611330114.18875, 449, 4473), (1611330114.189749, 440, 1424), (1611330114.203587, 438, 421), (1611330114.212605, 433, 296), (1611330114.222787, 427, 309), (1611330114.233332, 428, 282), (1611330114.244409, 432, 369), (1611330114.253403, 430, 476), (1611330114.265963, 428, 454), (1611330114.273371, 427, 428), (1611330114.283808, 426, 352), (1611330114.293689, 424, 284), (1611330114.309401, 425, 209), (1611330114.315264, 425, 145), (1611330114.329899, 424, 118), (1611330114.339685, 425, 101), (1611330114.344043, 425, 94), (1611330114.358308, 426, 94), (1611330114.369447, 427, 92), (1611330114.380095, 427, 101), (1611330114.387847, 427, 91), (1611330114.395466, 429, 98), (1611330114.410449, 429, 136), (1611330114.419411, 429, 140), (1611330114.421405, 428, 97), (1611330114.4372, 429, 83), (1611330114.443607, 430, 79), (1611330114.457199, 431, 79), (1611330114.464208, 431, 81), (1611330114.475373, 432, 75), (1611330114.484951, 433, 87), (1611330114.495166, 434, 102), (1611330114.505201, 434, 153), (1611330114.51613, 435, 291), (1611330114.52508, 437, 456), (1611330114.540752, 434, 565), (1611330114.550702, 431, 570), (1611330114.554896, 427, 481), (1611330114.57092, 423, 335), (1611330114.581602, 423, 139)])
result.append({'numberOfPoints': 14, 'r2': 0.9990421892816421, 'speed': -36.886153846153775})

data.append([(1611330112.238344, 818, 130), (1611330112.250477, 828, 249), (1611330112.260074, 831, 387), (1611330112.275707, 822, 567), (1611330112.28261, 811, 779), (1611330112.295747, 797, 986), (1611330112.305927, 783, 1136), (1611330112.316429, 767, 1616), (1611330112.326123, 748, 7973), (1611330112.335593, 734, 8435), (1611330112.345348, 724, 4741), (1611330112.35541, 713, 6438), (1611330112.364006, 702, 7578), (1611330112.373038, 691, 9543), (1611330112.379028, 681, 12280), (1611330112.389908, 670, 13938), (1611330112.406778, 660, 15076), (1611330112.407775, 650, 15927), (1611330112.42425, 639, 17006), (1611330112.430209, 628, 17412), (1611330112.439726, 618, 15037), (1611330112.450582, 608, 11296), (1611330112.462325, 600, 7193), (1611330112.470097, 590, 3862), (1611330112.48715, 580, 9013), (1611330112.490727, 571, 6128), (1611330112.507017, 562, 7030), (1611330112.513515, 552, 6530), (1611330112.521221, 542, 6683), (1611330112.537371, 535, 5408), (1611330112.547084, 527, 4424), (1611330112.55764, 519, 3989), (1611330112.564894, 511, 3479), (1611330112.573414, 503, 3506), (1611330112.587611, 495, 3699), (1611330112.598218, 488, 4003), (1611330112.606277, 481, 4446), (1611330112.610476, 474, 4793), (1611330112.622137, 468, 4977), (1611330112.63812, 461, 4323), (1611330112.641237, 455, 2944), (1611330112.655519, 451, 1532), (1611330112.663381, 451, 712), (1611330112.672871, 454, 509), (1611330112.683387, 456, 443), (1611330112.698866, 464, 411), (1611330112.70883, 469, 417), (1611330112.712992, 472, 483), (1611330112.723671, 469, 813), (1611330112.738976, 464, 1464), (1611330112.749075, 460, 2033), (1611330112.758424, 457, 2532), (1611330112.761616, 456, 2767), (1611330112.778808, 455, 2862), (1611330112.788541, 454, 2874), (1611330112.799617, 454, 2863), (1611330112.806188, 453, 2853), (1611330112.813926, 453, 2839), (1611330112.829483, 453, 2821), (1611330112.83947, 453, 2800), (1611330112.842277, 453, 2796), (1611330112.855529, 453, 2805), (1611330112.862772, 453, 2808), (1611330112.873114, 453, 2776), (1611330112.883109, 453, 2735), (1611330112.893462, 454, 2694), (1611330112.904539, 454, 2662), (1611330112.91577, 454, 2672), (1611330112.924937, 455, 2702), (1611330112.93739, 453, 2344), (1611330112.944164, 450, 1607), (1611330112.96034, 450, 855), (1611330112.965888, 454, 528), (1611330112.980145, 459, 445), (1611330112.990495, 465, 456), (1611330112.996372, 473, 538), (1611330113.009984, 475, 677), (1611330113.020555, 472, 734), (1611330113.030863, 468, 870), (1611330113.040876, 464, 801), (1611330113.047079, 462, 539), (1611330113.061395, 462, 315), (1611330113.070552, 463, 146), (1611330113.073685, 465, 72)])
result.append({'numberOfPoints': 17, 'r2': 0.99865011795843, 'speed': -36.60351444152695})

data.append([(1611330006.866687, 779, 113, 0), (1611330006.881771, 659, 2715, 1), (1611330006.893117, 623, 6847, 2), (1611330006.897403, 608, 9043, 3), (1611330006.913161, 595, 15790, 4), (1611330006.918572, 584, 7966, 5), (1611330006.933301, 574, 4079, 6), (1611330006.943366, 563, 4300, 7), (1611330006.945763, 550, 4949, 8), (1611330006.958416, 539, 5822, 9), (1611330006.966618, 528, 6872, 10), (1611330006.975054, 516, 7677, 11), (1611330006.987408, 504, 6762, 12), (1611330006.997965, 493, 5814, 13), (1611330007.007821, 481, 4102, 14), (1611330007.018069, 467, 4555, 15), (1611330007.028137, 457, 4675, 16), (1611330007.041297, 445, 4039, 17), (1611330007.048291, 437, 1350, 18), (1611330007.059118, 435, 477, 19), (1611330007.068455, 427, 451, 20), (1611330007.084477, 422, 393, 21), (1611330007.088986, 417, 374, 22), (1611330007.100065, 411, 374, 23), (1611330007.114582, 403, 274, 24), (1611330007.124753, 399, 222, 25), (1611330007.12576, 396, 202, 26), (1611330007.144709, 392, 202, 27), (1611330007.14792, 391, 135, 28), (1611330007.16487, 390, 96, 29), (1611330007.174119, 386, 172, 30), (1611330007.177179, 364, 520, 31), (1611330007.192351, 357, 931, 32), (1611330007.198313, 350, 1063, 33), (1611330007.207332, 351, 1331, 34), (1611330007.218361, 351, 1986, 35), (1611330007.228856, 344, 2204, 36), (1611330007.239608, 334, 1368, 37), (1611330007.249505, 329, 535, 38), (1611330007.257858, 328, 193, 39), (1611330007.26957, 328, 105, 40), (1611330007.279773, 329, 87, 41), (1611330007.295889, 330, 77, 42), (1611330007.300348, 332, 69, 43), (1611330007.312057, 333, 74, 44), (1611330007.325756, 334, 66, 45), (1611330007.329727, 335, 69, 46), (1611330007.342105, 336, 67, 47), (1611330007.398711, 354, 70, 48), (1611330007.409439, 358, 195, 49), (1611330007.4256, 364, 603, 50), (1611330007.429893, 360, 960, 51), (1611330007.442213, 355, 1145, 52), (1611330007.450075, 355, 1372, 53), (1611330007.459674, 351, 1483, 54), (1611330007.470489, 343, 1178, 55), (1611330007.481323, 336, 584, 56), (1611330007.490523, 487, 168, 57), (1611330007.501375, 1057, 197, 58), (1611330007.511386, 1711, 247, 59), (1611330007.526811, 2174, 269, 60), (1611330007.533077, 2438, 260, 61), (1611330007.545166, 2562, 218, 62), (1611330007.557734, 2659, 229, 63), (1611330007.567677, 2730, 236, 64), (1611330007.577717, 2762, 194, 65), (1611330007.588144, 2768, 118, 66), (1611330007.597179, 2775, 99, 67), (1611330007.607132, 2781, 100, 68), (1611330007.616271, 2787, 105, 69), (1611330007.624737, 2792, 105, 70), (1611330007.629607, 2796, 85, 71), (1611330007.640412, 2801, 91, 72), (1611330007.65753, 2806, 105, 73), (1611330007.660879, 2810, 121, 74), (1611330007.674513, 2814, 91, 75)])
result.append({'numberOfPoints': 17, 'r2': 0.99865011795843, 'speed': -36.60351444152695})

# candidates for enhanced algorithm
data.append([(1611329665.407458, 897, 105, 0), (1611329665.41394, 899, 135, 1), (1611329665.423531, 904, 161, 2), (1611329665.431475, 915, 183, 3), (1611329665.441493, 931, 238, 4), (1611329665.451874, 941, 209, 5), (1611329665.462014, 948, 185, 6), (1611329665.471559, 951, 173, 7), (1611329665.48745, 954, 162, 8), (1611329665.497845, 954, 141, 9), (1611329665.506184, 955, 128, 10), (1611329665.516494, 956, 120, 11), (1611329665.528409, 957, 119, 12), (1611329665.538497, 958, 119, 13), (1611329665.543207, 959, 107, 14), (1611329665.555663, 960, 99, 15), (1611329665.560022, 960, 89, 16), (1611329665.578959, 961, 90, 17), (1611329665.587886, 962, 93, 18), (1611329665.59188, 962, 95, 19), (1611329665.605641, 963, 91, 20), (1611329665.612001, 964, 82, 21), (1611329665.623108, 965, 83, 22), (1611329665.632859, 966, 84, 23), (1611329665.643316, 966, 83, 24), (1611329665.653447, 967, 80, 25), (1611329665.664663, 967, 79, 26), (1611329665.673674, 967, 82, 27), (1611329665.683609, 968, 84, 28), (1611329665.693713, 968, 89, 29), (1611329665.709392, 968, 91, 30), (1611329665.713588, 968, 103, 31), (1611329665.724823, 968, 122, 32), (1611329665.739779, 969, 140, 33), (1611329665.749951, 969, 157, 34), (1611329665.760181, 970, 181, 35), (1611329665.761179, 971, 195, 36), (1611329665.780028, 973, 223, 37), (1611329665.790028, 974, 249, 38), (1611329665.796942, 976, 251, 39), (1611329665.810077, 976, 218, 40), (1611329665.812631, 977, 198, 41), (1611329665.823418, 978, 191, 42), (1611329665.84046, 979, 178, 43), (1611329665.841459, 978, 184, 44), (1611329665.855176, 977, 256, 45), (1611329665.864471, 972, 398, 46), (1611329665.874186, 974, 516, 47), (1611329665.884927, 979, 559, 48), (1611329665.896057, 986, 529, 49), (1611329665.904545, 992, 616, 50), (1611329665.920055, 999, 1133, 51), (1611329665.924461, 1005, 2348, 52), (1611329665.940996, 1011, 4082, 53), (1611329665.950868, 1019, 5299, 54), (1611329665.958276, 1026, 7451, 55), (1611329665.970628, 1035, 10000, 56), (1611329665.97438, 1043, 11905, 57), (1611329665.987571, 1054, 4854, 58), (1611329665.992914, 1062, 3926, 59), (1611329666.011039, 1070, 3654, 60), (1611329666.02086, 1079, 3821, 61), (1611329666.023772, 1087, 9909, 62), (1611329666.038337, 1097, 6605, 63), (1611329666.044777, 1113, 1884, 64), (1611329666.054121, 1127, 1068, 65), (1611329666.066047, 1136, 983, 66), (1611329666.076321, 1144, 1190, 67), (1611329666.086342, 1152, 1206, 68), (1611329666.097295, 1159, 1161, 69), (1611329666.106643, 1166, 1125, 70), (1611329666.116262, 1173, 1160, 71), (1611329666.126626, 1182, 1232, 72), (1611329666.142148, 1192, 1194, 73), (1611329666.152566, 1201, 1239, 74), (1611329666.15664, 1209, 1222, 75), (1611329666.17252, 1217, 1174, 76), (1611329666.176008, 1225, 1169, 77), (1611329666.192081, 1234, 1145, 78), (1611329666.193119, 1242, 1149, 79), (1611329666.212699, 1250, 893, 80), (1611329666.222162, 1257, 825, 81), (1611329666.229558, 1266, 790, 82), (1611329666.242875, 1275, 669, 83), (1611329666.243873, 1284, 610, 84), (1611329666.256172, 1293, 626, 85), (1611329666.273103, 1304, 1463, 86), (1611329666.27413, 1312, 3408, 87), (1611329666.288187, 1322, 4558, 88), (1611329666.297423, 1331, 3166, 89), (1611329666.307, 1340, 2973, 90), (1611329666.317645, 1347, 3999, 91), (1611329666.333719, 1356, 3732, 92), (1611329666.337516, 1362, 3424, 93), (1611329666.353243, 1372, 3180, 94), (1611329666.357801, 1384, 1514, 95), (1611329666.37377, 1392, 507, 96), (1611329666.379265, 1393, 141, 97)])

data.append([(1611329687.620821, 1090, 99, 0), (1611329687.625008, 1091, 103, 1), (1611329687.636925, 1091, 112, 2), (1611329687.645303, 1092, 112, 3), (1611329687.655791, 1094, 117, 4), (1611329687.665438, 1095, 113, 5), (1611329687.68158, 1095, 118, 6), (1611329687.68684, 1096, 112, 7), (1611329687.70135, 1096, 111, 8), (1611329687.705312, 1097, 104, 9), (1611329687.721482, 1097, 105, 10), (1611329687.728708, 1098, 105, 11), (1611329687.73913, 1098, 106, 12), (1611329687.746804, 1099, 102, 13), (1611329687.760925, 1099, 103, 14), (1611329687.771648, 1099, 94, 15), (1611329687.773552, 1100, 94, 16), (1611329687.791851, 1101, 86, 17), (1611329687.794594, 1100, 88, 18), (1611329687.804881, 1101, 87, 19), (1611329687.822418, 1101, 87, 20), (1611329687.823417, 1101, 82, 21), (1611329687.837903, 1101, 88, 22), (1611329687.845287, 1101, 93, 23), (1611329687.855116, 1101, 91, 24), (1611329687.866281, 1101, 99, 25), (1611329687.876766, 1101, 103, 26), (1611329687.886451, 1101, 113, 27), (1611329687.902106, 1101, 119, 28), (1611329687.904826, 1102, 130, 29), (1611329687.921989, 1103, 128, 30), (1611329687.932745, 1103, 126, 31), (1611329687.937929, 1104, 147, 32), (1611329687.953213, 1106, 175, 33), (1611329687.961256, 1108, 216, 34), (1611329687.972944, 1116, 269, 35), (1611329687.977117, 1125, 317, 36), (1611329687.993237, 1133, 330, 37), (1611329688.002695, 1140, 337, 38), (1611329688.005716, 1150, 479, 39), (1611329688.020503, 1165, 971, 40), (1611329688.023848, 1175, 1841, 41), (1611329688.037356, 1185, 2696, 42), (1611329688.05322, 1194, 3539, 43), (1611329688.056121, 1204, 4354, 44), (1611329688.070171, 1213, 5899, 45), (1611329688.077134, 1222, 10227, 46), (1611329688.087644, 1233, 10258, 47), (1611329688.098361, 1242, 13509, 48), (1611329688.108121, 1253, 7653, 49), (1611329688.119857, 1264, 5183, 50), (1611329688.128301, 1279, 1733, 51), (1611329688.138466, 1292, 854, 52), (1611329688.153406, 1303, 1222, 53), (1611329688.163893, 1313, 2044, 54), (1611329688.172766, 1324, 2489, 55), (1611329688.179094, 1335, 3090, 56), (1611329688.19434, 1346, 3365, 57), (1611329688.204372, 1357, 3436, 58), (1611329688.205374, 1369, 3615, 59), (1611329688.22182, 1382, 3522, 60), (1611329688.234522, 1394, 3692, 61), (1611329688.244677, 1406, 3948, 62), (1611329688.253903, 1418, 3746, 63), (1611329688.262468, 1430, 2747, 64), (1611329688.272416, 1441, 2493, 65), (1611329688.280249, 1454, 1956, 66), (1611329688.28745, 1465, 1474, 67), (1611329688.305332, 1480, 1772, 68), (1611329688.306332, 1494, 2989, 69), (1611329688.320732, 1504, 2954, 70), (1611329688.328885, 1515, 3265, 71), (1611329688.33923, 1524, 4184, 72), (1611329688.34934, 1535, 4016, 73), (1611329688.365533, 1544, 2771, 74), (1611329688.369586, 1555, 2393, 75), (1611329688.385655, 1570, 578, 76), (1611329688.395133, 1573, 153, 77)])

data.append([(1611329976.125265, 955, 108, 0), (1611329976.14184, 958, 152, 1), (1611329976.15246, 975, 187, 2), (1611329976.168526, 1000, 230, 3), (1611329976.173258, 1022, 277, 4), (1611329976.184097, 1039, 316, 5), (1611329976.19876, 1046, 407, 6), (1611329976.208305, 1052, 488, 7), (1611329976.218907, 1056, 571, 8), (1611329976.225927, 1060, 622, 9), (1611329976.235387, 1064, 626, 10), (1611329976.241265, 1063, 606, 11), (1611329976.259381, 1062, 610, 12), (1611329976.268353, 1062, 605, 13), (1611329976.27364, 1062, 617, 14), (1611329976.283657, 1062, 627, 15), (1611329976.299428, 1063, 630, 16), (1611329976.302163, 1063, 631, 17), (1611329976.312929, 1063, 627, 18), (1611329976.323484, 1065, 606, 19), (1611329976.333781, 1068, 579, 20), (1611329976.344089, 1068, 542, 21), (1611329976.354106, 1069, 483, 22), (1611329976.366467, 1069, 395, 23), (1611329976.37408, 1069, 320, 24), (1611329976.389665, 1067, 309, 25), (1611329976.393254, 1064, 358, 26), (1611329976.406462, 1062, 454, 27), (1611329976.420442, 1066, 568, 28), (1611329976.430423, 1072, 661, 29), (1611329976.437031, 1080, 737, 30), (1611329976.450261, 1089, 755, 31), (1611329976.4605, 1097, 740, 32), (1611329976.467033, 1107, 770, 33), (1611329976.474696, 1116, 829, 34), (1611329976.484939, 1128, 873, 35), (1611329976.500144, 1138, 802, 36), (1611329976.502725, 1150, 722, 37), (1611329976.51746, 1162, 688, 38), (1611329976.524318, 1175, 644, 39), (1611329976.535084, 1185, 581, 40), (1611329976.544847, 1198, 571, 41), (1611329976.555899, 1210, 542, 42), (1611329976.566314, 1223, 533, 43), (1611329976.575237, 1238, 515, 44), (1611329976.583667, 1252, 525, 45), (1611329976.595297, 1267, 507, 46), (1611329976.605361, 1279, 452, 47), (1611329976.621624, 1291, 418, 48), (1611329976.624903, 1304, 390, 49), (1611329976.638792, 1320, 380, 50), (1611329976.651674, 1333, 350, 51), (1611329976.66133, 1347, 331, 52), (1611329976.667889, 1367, 354, 53), (1611329976.681937, 1386, 338, 54), (1611329976.68534, 1397, 233, 55), (1611329976.701267, 1405, 173, 56), (1611329976.705055, 1408, 123, 57), (1611329976.722203, 1413, 71, 58)])

data.append([(1611330006.866687, 779, 113, 0), (1611330006.881771, 659, 2715, 1), (1611330006.893117, 623, 6847, 2), (1611330006.897403, 608, 9043, 3), (1611330006.913161, 595, 15790, 4), (1611330006.918572, 584, 7966, 5), (1611330006.933301, 574, 4079, 6), (1611330006.943366, 563, 4300, 7), (1611330006.945763, 550, 4949, 8), (1611330006.958416, 539, 5822, 9), (1611330006.966618, 528, 6872, 10), (1611330006.975054, 516, 7677, 11), (1611330006.987408, 504, 6762, 12), (1611330006.997965, 493, 5814, 13), (1611330007.007821, 481, 4102, 14), (1611330007.018069, 467, 4555, 15), (1611330007.028137, 457, 4675, 16), (1611330007.041297, 445, 4039, 17), (1611330007.048291, 437, 1350, 18), (1611330007.059118, 435, 477, 19), (1611330007.068455, 427, 451, 20), (1611330007.084477, 422, 393, 21), (1611330007.088986, 417, 374, 22), (1611330007.100065, 411, 374, 23), (1611330007.114582, 403, 274, 24), (1611330007.124753, 399, 222, 25), (1611330007.12576, 396, 202, 26), (1611330007.144709, 392, 202, 27), (1611330007.14792, 391, 135, 28), (1611330007.16487, 390, 96, 29), (1611330007.174119, 386, 172, 30), (1611330007.177179, 364, 520, 31), (1611330007.192351, 357, 931, 32), (1611330007.198313, 350, 1063, 33), (1611330007.207332, 351, 1331, 34), (1611330007.218361, 351, 1986, 35), (1611330007.228856, 344, 2204, 36), (1611330007.239608, 334, 1368, 37), (1611330007.249505, 329, 535, 38), (1611330007.257858, 328, 193, 39), (1611330007.26957, 328, 105, 40), (1611330007.279773, 329, 87, 41), (1611330007.295889, 330, 77, 42), (1611330007.300348, 332, 69, 43), (1611330007.312057, 333, 74, 44), (1611330007.325756, 334, 66, 45), (1611330007.329727, 335, 69, 46), (1611330007.342105, 336, 67, 47), (1611330007.398711, 354, 70, 48), (1611330007.409439, 358, 195, 49), (1611330007.4256, 364, 603, 50), (1611330007.429893, 360, 960, 51), (1611330007.442213, 355, 1145, 52), (1611330007.450075, 355, 1372, 53), (1611330007.459674, 351, 1483, 54), (1611330007.470489, 343, 1178, 55), (1611330007.481323, 336, 584, 56), (1611330007.490523, 487, 168, 57), (1611330007.501375, 1057, 197, 58), (1611330007.511386, 1711, 247, 59), (1611330007.526811, 2174, 269, 60), (1611330007.533077, 2438, 260, 61), (1611330007.545166, 2562, 218, 62), (1611330007.557734, 2659, 229, 63), (1611330007.567677, 2730, 236, 64), (1611330007.577717, 2762, 194, 65), (1611330007.588144, 2768, 118, 66), (1611330007.597179, 2775, 99, 67), (1611330007.607132, 2781, 100, 68), (1611330007.616271, 2787, 105, 69), (1611330007.624737, 2792, 105, 70), (1611330007.629607, 2796, 85, 71), (1611330007.640412, 2801, 91, 72), (1611330007.65753, 2806, 105, 73), (1611330007.660879, 2810, 121, 74), (1611330007.674513, 2814, 91, 75)])

data.append([(1611330032.238366, 743, 231, 0), (1611330032.257503, 658, 7606, 1), (1611330032.271735, 635, 7057, 2), (1611330032.277094, 621, 10610, 3), (1611330032.288255, 608, 15609, 4), (1611330032.2974, 597, 10988, 5), (1611330032.307452, 586, 3896, 6), (1611330032.320773, 573, 3114, 7), (1611330032.3335, 560, 3385, 8), (1611330032.334504, 547, 3393, 9), (1611330032.35315, 535, 3391, 10), (1611330032.357236, 523, 2323, 11), (1611330032.371757, 509, 6569, 12), (1611330032.378643, 497, 5507, 13), (1611330032.393773, 488, 1789, 14), (1611330032.403427, 481, 872, 15), (1611330032.413197, 469, 721, 16), (1611330032.422249, 457, 712, 17), (1611330032.429868, 449, 596, 18), (1611330032.444543, 441, 624, 19), (1611330032.454287, 432, 603, 20), (1611330032.456959, 424, 460, 21), (1611330032.474601, 422, 3015, 22), (1611330032.475599, 420, 5433, 23), (1611330032.486577, 403, 1188, 24), (1611330032.497968, 394, 457, 25), (1611330032.508744, 386, 348, 26), (1611330032.518908, 376, 457, 27), (1611330032.52896, 365, 1133, 28), (1611330032.537318, 365, 1164, 29), (1611330032.548968, 369, 952, 30), (1611330032.559102, 367, 1054, 31), (1611330032.574803, 362, 2163, 32), (1611330032.578583, 356, 3115, 33), (1611330032.59527, 355, 3932, 34), (1611330032.605271, 355, 3803, 35), (1611330032.61531, 355, 3545, 36), (1611330032.625418, 354, 3472, 37), (1611330032.627412, 354, 3452, 38), (1611330032.645197, 353, 3514, 39), (1611330032.655628, 353, 3550, 40), (1611330032.662109, 352, 3578, 41), (1611330032.675895, 352, 3641, 42), (1611330032.676894, 352, 3719, 43), (1611330032.688919, 351, 3593, 44), (1611330032.704866, 352, 3488, 45), (1611330032.708067, 352, 3487, 46), (1611330032.720593, 353, 3498, 47), (1611330032.730109, 354, 3564, 48), (1611330032.741427, 356, 4298, 49), (1611330032.750385, 355, 5227, 50), (1611330032.76035, 350, 3842, 51), (1611330032.770956, 355, 1662, 52), (1611330032.780719, 363, 1122, 53), (1611330032.790657, 365, 966, 54), (1611330032.806199, 364, 1311, 55), (1611330032.810334, 361, 1592, 56), (1611330032.821995, 356, 1027, 57), (1611330032.837089, 359, 312, 58), (1611330032.846534, 361, 110, 59)])

data.append([(1611330043.994766, 787, 139, 0), (1611330043.997716, 775, 207, 1), (1611330044.012185, 754, 279, 2), (1611330044.019427, 731, 316, 3), (1611330044.030027, 715, 309, 4), (1611330044.039646, 682, 981, 5), (1611330044.050678, 653, 11677, 6), (1611330044.059638, 639, 4486, 7), (1611330044.075476, 627, 8032, 8), (1611330044.082211, 615, 11551, 9), (1611330044.095325, 602, 13329, 10), (1611330044.099529, 590, 13523, 11), (1611330044.115635, 578, 14127, 12), (1611330044.120733, 566, 13602, 13), (1611330044.136097, 554, 14466, 14), (1611330044.14581, 542, 14102, 15), (1611330044.153132, 530, 9980, 16), (1611330044.162358, 519, 5558, 17), (1611330044.168812, 508, 3791, 18), (1611330044.179725, 502, 1087, 19), (1611330044.196538, 492, 676, 20), (1611330044.197537, 483, 436, 21), (1611330044.21429, 472, 416, 22), (1611330044.219398, 453, 620, 23), (1611330044.231923, 438, 789, 24), (1611330044.239801, 428, 625, 25), (1611330044.250547, 422, 424, 26), (1611330044.260533, 418, 340, 27), (1611330044.270554, 413, 306, 28), (1611330044.278733, 406, 327, 29), (1611330044.296448, 396, 357, 30), (1611330044.30162, 385, 299, 31), (1611330044.31702, 382, 217, 32), (1611330044.326936, 378, 254, 33), (1611330044.332901, 373, 521, 34), (1611330044.346145, 366, 714, 35), (1611330044.353572, 360, 604, 36), (1611330044.362095, 362, 536, 37), (1611330044.377191, 364, 570, 38), (1611330044.386583, 365, 677, 39), (1611330044.393167, 360, 500, 40), (1611330044.400283, 358, 251, 41), (1611330044.41146, 358, 163, 42), (1611330044.427461, 359, 221, 43), (1611330044.430664, 359, 312, 44), (1611330044.444092, 356, 319, 45), (1611330044.450193, 354, 304, 46), (1611330044.460102, 352, 320, 47), (1611330044.470931, 350, 442, 48), (1611330044.482364, 352, 1613, 49), (1611330044.493732, 341, 2926, 50), (1611330044.501991, 335, 1314, 51), (1611330044.510502, 339, 383, 52), (1611330044.528333, 342, 318, 53), (1611330044.538424, 343, 305, 54), (1611330044.544747, 343, 314, 55), (1611330044.551928, 343, 312, 56), (1611330044.568592, 342, 309, 57), (1611330044.578627, 345, 312, 58), (1611330044.587741, 344, 292, 59), (1611330044.595926, 345, 286, 60), (1611330044.602574, 344, 270, 61), (1611330044.612716, 345, 265, 62), (1611330044.628751, 346, 319, 63), (1611330044.631827, 346, 269, 64), (1611330044.644825, 346, 238, 65), (1611330044.65252, 347, 513, 66), (1611330044.662269, 350, 1937, 67), (1611330044.672948, 340, 1148, 68), (1611330044.684693, 338, 398, 69), (1611330044.693346, 336, 367, 70), (1611330044.70443, 341, 314, 71), (1611330044.714315, 346, 376, 72), (1611330044.727418, 355, 541, 73), (1611330044.734677, 356, 580, 74), (1611330044.745579, 361, 589, 75), (1611330044.760045, 369, 760, 76), (1611330044.770004, 370, 955, 77), (1611330044.774133, 364, 865, 78), (1611330044.78685, 355, 1675, 79), (1611330044.799785, 343, 1748, 80), (1611330044.809999, 342, 512, 81), (1611330044.820909, 338, 508, 82), (1611330044.830247, 340, 218, 83), (1611330044.833008, 343, 67, 84)])

data.append([(1611330067.061957, 805, 88, 0), (1611330067.075185, 805, 82, 1), (1611330067.084719, 806, 85, 2), (1611330067.100666, 805, 91, 3), (1611330067.10759, 805, 116, 4), (1611330067.120946, 803, 124, 5), (1611330067.125203, 801, 135, 6), (1611330067.140796, 793, 171, 7), (1611330067.145101, 734, 762, 8), (1611330067.1593, 697, 5414, 9), (1611330067.164031, 682, 11418, 10), (1611330067.180982, 671, 13773, 11), (1611330067.183192, 664, 3733, 12), (1611330067.193835, 654, 4977, 13), (1611330067.211552, 646, 5716, 14), (1611330067.212551, 636, 5507, 15), (1611330067.225572, 627, 5229, 16), (1611330067.241394, 619, 4623, 17), (1611330067.244533, 609, 3996, 18), (1611330067.255063, 599, 4423, 19), (1611330067.26491, 590, 4776, 20), (1611330067.275156, 581, 3971, 21), (1611330067.286055, 573, 4462, 22), (1611330067.296255, 562, 8785, 23), (1611330067.3115, 554, 4138, 24), (1611330067.318555, 548, 1468, 25), (1611330067.330012, 544, 693, 26), (1611330067.342214, 539, 520, 27), (1611330067.346296, 533, 475, 28), (1611330067.361096, 520, 483, 29), (1611330067.372567, 509, 565, 30), (1611330067.382562, 495, 677, 31), (1611330067.392343, 484, 754, 32), (1611330067.400869, 475, 764, 33), (1611330067.410496, 467, 727, 34), (1611330067.415189, 459, 650, 35), (1611330067.424804, 451, 624, 36), (1611330067.442806, 444, 740, 37), (1611330067.444579, 436, 851, 38), (1611330067.458817, 430, 811, 39), (1611330067.467427, 423, 647, 40), (1611330067.477791, 419, 401, 41), (1611330067.487569, 414, 290, 42), (1611330067.497563, 411, 252, 43), (1611330067.508614, 408, 246, 44), (1611330067.517639, 406, 256, 45), (1611330067.527676, 404, 368, 46), (1611330067.543033, 401, 684, 47), (1611330067.548862, 395, 973, 48), (1611330067.560978, 391, 946, 49), (1611330067.567637, 390, 792, 50), (1611330067.579342, 392, 812, 51), (1611330067.593426, 398, 1011, 52), (1611330067.598028, 400, 1350, 53), (1611330067.609045, 395, 1620, 54), (1611330067.617452, 389, 1400, 55), (1611330067.634097, 385, 1058, 56), (1611330067.644064, 384, 814, 57), (1611330067.644848, 384, 784, 58), (1611330067.659409, 386, 784, 59), (1611330067.66764, 385, 769, 60), (1611330067.675957, 385, 766, 61), (1611330067.691884, 384, 745, 62), (1611330067.698795, 384, 754, 63), (1611330067.709258, 387, 1319, 64), (1611330067.71902, 393, 6786, 65), (1611330067.729215, 384, 12259, 66), (1611330067.741415, 374, 8121, 67), (1611330067.74936, 372, 1476, 68), (1611330067.759457, 377, 647, 69), (1611330067.774752, 379, 584, 70), (1611330067.78012, 379, 564, 71), (1611330067.792597, 380, 571, 72), (1611330067.799426, 381, 575, 73), (1611330067.811592, 381, 588, 74), (1611330067.825377, 380, 592, 75), (1611330067.828827, 380, 584, 76), (1611330067.84264, 381, 555, 77), (1611330067.848452, 380, 511, 78), (1611330067.865709, 382, 492, 79), (1611330067.875191, 382, 470, 80), (1611330067.878288, 383, 499, 81), (1611330067.892672, 384, 556, 82), (1611330067.898978, 383, 614, 83), (1611330067.909226, 384, 630, 84), (1611330067.91955, 384, 649, 85), (1611330067.9316, 383, 677, 86), (1611330067.940684, 385, 758, 87), (1611330067.950676, 393, 5299, 88), (1611330067.960713, 385, 8441, 89), (1611330067.970629, 377, 4545, 90), (1611330067.98083, 366, 5402, 91), (1611330067.996034, 362, 3286, 92), (1611330068.000389, 357, 3225, 93), (1611330068.015152, 376, 894, 94), (1611330068.026074, 386, 883, 95), (1611330068.032997, 390, 930, 96), (1611330068.041614, 389, 850, 97), (1611330068.05016, 395, 837, 98), (1611330068.06693, 407, 1183, 99), (1611330068.076922, 410, 1717, 100), (1611330068.084001, 407, 2178, 101), (1611330068.091416, 400, 2170, 102), (1611330068.107309, 393, 1710, 103), (1611330068.110217, 386, 1233, 104), (1611330068.12746, 384, 948, 105), (1611330068.128463, 384, 958, 106), (1611330068.143935, 385, 1011, 107), (1611330068.157543, 384, 1078, 108), (1611330068.160526, 385, 1149, 109), (1611330068.178169, 389, 2175, 110), (1611330068.17917, 387, 4970, 111), (1611330068.193472, 379, 7490, 112), (1611330068.207651, 371, 2138, 113), (1611330068.21096, 365, 1141, 114), (1611330068.222208, 354, 1925, 115), (1611330068.238401, 358, 323, 116)])

#end of new

data.append([(1611329806.225139, 1051, 71), (1611329806.230707, 1052, 85), (1611329806.241483, 1052, 110), (1611329806.258201, 1053, 159), (1611329806.2592, 1054, 439), (1611329806.273791, 1049, 984), (1611329806.282463, 1053, 1387), (1611329806.296279, 1060, 939), (1611329806.302692, 1067, 1186), (1611329806.313776, 1076, 1895), (1611329806.322512, 1087, 2905), (1611329806.33847, 1098, 3158), (1611329806.342212, 1109, 7556), (1611329806.358972, 1122, 5494), (1611329806.369031, 1133, 3608), (1611329806.379204, 1145, 2993), (1611329806.388688, 1154, 3742), (1611329806.398795, 1166, 2836), (1611329806.406402, 1174, 3442), (1611329806.415711, 1184, 10251), (1611329806.423918, 1195, 9264), (1611329806.439404, 1205, 7114), (1611329806.441865, 1218, 4279), (1611329806.456789, 1232, 1715), (1611329806.462784, 1235, 410), (1611329806.473346, 1239, 226), (1611329806.482957, 1246, 214), (1611329806.493241, 1256, 230), (1611329806.505803, 1267, 227), (1611329806.514329, 1273, 192), (1611329806.524708, 1281, 189), (1611329806.540376, 1295, 222), (1611329806.546977, 1311, 226), (1611329806.559858, 1330, 248), (1611329806.566666, 1352, 288), (1611329806.579725, 1381, 492), (1611329806.590042, 1407, 1170), (1611329806.598422, 1424, 2052), (1611329806.60732, 1437, 2518), (1611329806.615056, 1450, 3117), (1611329806.630033, 1462, 3367), (1611329806.64081, 1474, 2538), (1611329806.643209, 1487, 2365), (1611329806.659496, 1505, 1116), (1611329806.667041, 1515, 193)])

data.append([(1611329826.492835, 816, 114), (1611329826.507255, 812, 170), (1611329826.520281, 793, 250), (1611329826.530221, 735, 1603), (1611329826.540154, 703, 6558), (1611329826.550616, 687, 9604), (1611329826.558686, 672, 15251), (1611329826.561164, 658, 14184), (1611329826.574418, 646, 4630), (1611329826.590738, 631, 3984), (1611329826.594051, 617, 4538), (1611329826.606726, 603, 5395), (1611329826.615314, 588, 5351), (1611329826.626405, 575, 3803), (1611329826.635459, 562, 2753), (1611329826.645489, 548, 6112), (1611329826.656523, 533, 7749), (1611329826.670763, 517, 7234), (1611329826.676262, 505, 3500), (1611329826.690517, 492, 2796), (1611329826.693683, 479, 3024), (1611329826.707958, 470, 1552), (1611329826.721217, 467, 674), (1611329826.726219, 461, 477), (1611329826.741659, 456, 263), (1611329826.74762, 455, 146), (1611329826.761794, 455, 80), (1611329826.791782, 442, 284), (1611329826.793587, 422, 939), (1611329826.806416, 414, 856), (1611329826.814086, 413, 1082), (1611329826.825016, 413, 1121), (1611329826.833192, 411, 856), (1611329826.84677, 406, 597), (1611329826.854766, 404, 386), (1611329826.872534, 406, 269), (1611329826.875037, 407, 212), (1611329826.888947, 408, 177), (1611329826.902673, 408, 160), (1611329826.913096, 408, 147), (1611329826.914095, 409, 141), (1611329826.932816, 409, 154), (1611329826.939814, 409, 184), (1611329826.948366, 409, 177), (1611329826.962885, 409, 149), (1611329826.973185, 409, 140), (1611329826.980909, 410, 134), (1611329826.990445, 411, 126), (1611329826.993921, 411, 129), (1611329827.006867, 412, 176), (1611329827.022705, 413, 310), (1611329827.031466, 419, 1855), (1611329827.034648, 410, 1852), (1611329827.047138, 409, 1097), (1611329827.055842, 409, 1056), (1611329827.073796, 409, 750), (1611329827.078526, 408, 521), (1611329827.093624, 411, 302), (1611329827.09949, 412, 135)])

data.append([(1611329833.72101, 736, 738), (1611329833.737375, 718, 885), (1611329833.740693, 683, 1766), (1611329833.752672, 644, 6641), (1611329833.76747, 628, 5110), (1611329833.770134, 613, 7625), (1611329833.785375, 600, 9859), (1611329833.790843, 585, 9087), (1611329833.801467, 572, 7973), (1611329833.811304, 559, 6869), (1611329833.821864, 545, 7555), (1611329833.832028, 532, 6863), (1611329833.8432, 520, 4045), (1611329833.850532, 505, 4745), (1611329833.86221, 498, 1105), (1611329833.872295, 488, 930), (1611329833.888381, 468, 3876), (1611329833.893646, 458, 3887), (1611329833.908493, 451, 3560), (1611329833.918453, 442, 2022), (1611329833.919453, 435, 1790), (1611329833.938578, 428, 2982), (1611329833.940617, 415, 1943), (1611329833.956268, 406, 663), (1611329833.967638, 400, 270), (1611329833.971525, 399, 139), (1611329833.984389, 399, 89), (1611329833.998991, 398, 132), (1611329834.001237, 394, 291), (1611329834.019132, 387, 419), (1611329834.024936, 380, 391), (1611329834.032243, 376, 255), (1611329834.042249, 376, 144), (1611329834.052265, 375, 115), (1611329834.062349, 376, 84), (1611329834.072551, 378, 74), (1611329834.083053, 379, 74), (1611329834.095658, 378, 69), (1611329834.102576, 378, 68), (1611329834.119376, 378, 75), (1611329834.129512, 378, 89), (1611329834.137811, 378, 79), (1611329834.149893, 378, 82), (1611329834.160422, 377, 72), (1611329834.167779, 377, 75), (1611329834.173751, 378, 72), (1611329834.185208, 378, 69), (1611329834.200461, 379, 145), (1611329834.21059, 381, 269), (1611329834.216834, 381, 340), (1611329834.222934, 377, 306), (1611329834.233981, 377, 205), (1611329834.250395, 378, 88)])

data.append([(1611329798.477872, 702, 69), (1611329798.48284, 714, 96), (1611329798.498044, 774, 226), (1611329798.508103, 864, 691), (1611329798.518411, 891, 1671), (1611329798.528083, 901, 2875), (1611329798.531255, 912, 4100), (1611329798.548607, 924, 4978), (1611329798.549606, 937, 5299), (1611329798.562457, 950, 7113), (1611329798.570558, 962, 7170), (1611329798.582607, 975, 7017), (1611329798.590761, 987, 10061), (1611329798.602849, 1000, 13013), (1611329798.61284, 1012, 14881), (1611329798.628734, 1025, 11882), (1611329798.63877, 1039, 8090), (1611329798.646826, 1052, 4664), (1611329798.658345, 1068, 1297), (1611329798.669098, 1078, 364), (1611329798.678507, 1094, 317), (1611329798.683456, 1124, 629), (1611329798.699081, 1154, 1054), (1611329798.701664, 1168, 1650), (1611329798.719244, 1182, 1997), (1611329798.728579, 1195, 1684), (1611329798.731041, 1206, 1722), (1611329798.746438, 1217, 1781), (1611329798.751369, 1227, 1732), (1611329798.761572, 1236, 5792), (1611329798.770802, 1247, 12053), (1611329798.784473, 1260, 4861), (1611329798.795635, 1277, 12484), (1611329798.804341, 1294, 11248), (1611329798.814505, 1305, 7758), (1611329798.829604, 1321, 7647), (1611329798.840176, 1337, 4596), (1611329798.846631, 1355, 1563), (1611329798.858868, 1361, 225)])

data.append([(1611330007.791637, 3037, 105, 0), (1611330007.809414, 3037, 113, 1), (1611330007.818968, 3038, 114, 2), (1611330007.829386, 3040, 119, 3), (1611330007.839574, 3042, 124, 4), (1611330007.849646, 3045, 111, 5), (1611330007.859632, 3048, 116, 6), (1611330007.862367, 3051, 106, 7), (1611330007.876823, 3055, 80, 8)])

data.append([(1611329991.738186, 869, 109, 0), (1611329991.752192, 879, 140, 1), (1611329991.75542, 955, 265, 2), (1611329991.772466, 1049, 603, 3), (1611329991.775112, 1087, 1233, 4), (1611329991.79284, 1098, 1356, 5), (1611329991.802748, 1105, 970, 6), (1611329991.805795, 1118, 876, 7), (1611329991.822887, 1133, 1060, 8), (1611329991.825796, 1148, 1250, 9), (1611329991.837689, 1161, 1793, 10), (1611329991.847459, 1174, 2062, 11), (1611329991.857082, 1189, 1616, 12), (1611329991.86756, 1202, 1525, 13), (1611329991.878605, 1215, 1331, 14), (1611329991.88662, 1230, 1184, 15), (1611329991.897899, 1243, 1691, 16), (1611329991.907954, 1253, 6436, 17), (1611329991.92312, 1268, 9263, 18), (1611329991.929476, 1282, 11470, 19), (1611329991.944107, 1299, 14219, 20), (1611329991.954058, 1315, 14124, 21), (1611329991.958233, 1329, 12667, 22), (1611329991.973104, 1343, 11037, 23), (1611329991.980973, 1359, 9806, 24), (1611329991.994097, 1377, 7212, 25), (1611329992.00329, 1395, 5278, 26), (1611329992.014337, 1411, 3292, 27), (1611329992.020944, 1434, 2779, 28), (1611329992.026764, 1454, 2184, 29), (1611329992.036558, 1467, 1200, 30), (1611329992.053627, 1480, 1192, 31), (1611329992.056951, 1495, 983, 32), (1611329992.070672, 1509, 423, 33), (1611329992.079021, 1512, 148, 34)])


class EventTest(unittest.TestCase):
    def test_basicparameters(self):
        event = Event(data[0])
        self.assertEqual(798, event.getStartDistance())
        self.assertEqual(423, event.getEndDistance())
        self.assertAlmostEqual(0.7151870727539062, event.getDuration())
        self.assertEqual(423, event.getMinDistance())
        self.assertEqual(798, event.getMaxDistance())
        self.assertEqual(375, event.getMeasuredDistance())
        self.assertEqual(75, event.getMinStrength())
        self.assertEqual(18524, event.getMaxStrength())
        self.assertEqual('TOWARDS', event.getDirection())

    def test_basicparameters2(self):
        event = Event(data[1])
        self.assertEqual(818, event.getStartDistance())
        self.assertEqual(465, event.getEndDistance())
        self.assertAlmostEqual(0.835341, event.getDuration())
        self.assertEqual(450, event.getMinDistance())
        self.assertEqual(831, event.getMaxDistance())
        self.assertEqual(381, event.getMeasuredDistance())
        self.assertEqual(72, event.getMinStrength())
        self.assertEqual(17412, event.getMaxStrength())
        self.assertEqual('TOWARDS', event.getDirection())


    def test_speedFromMaxStrength(self):
        for i in range(min(len(data), len(result))):
            event = Event(data[i])
            self.assertEqual(result[i], event.getSpeedFromMaxStrength())

    def test_singleEventspeed(self):
        i = 2
        event = Event(data[i])
        print(event)
        print(event.getSpeedFromMaxStrength(plot=True))


if __name__ == '__main__':
    unittest.main()
