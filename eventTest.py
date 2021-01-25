import unittest
from event import Event

data1 = [(1611330113.866415, 798, 200), (1611330113.872132, 790, 268), (1611330113.886407, 780, 290), (1611330113.891287, 770, 243), (1611330113.906759, 713, 3732), (1611330113.912672, 690, 7643), (1611330113.922061, 679, 4935), (1611330113.936946, 668, 6732), (1611330113.947138, 658, 10181), (1611330113.955433, 647, 13283), (1611330113.95965, 636, 14279), (1611330113.97085, 625, 14698), (1611330113.986711, 615, 16659), (1611330113.989782, 604, 18199), (1611330114.004019, 594, 18048), (1611330114.010409, 585, 18524), (1611330114.01967, 575, 14564), (1611330114.030641, 565, 9463), (1611330114.042567, 556, 5826), (1611330114.054683, 547, 5714), (1611330114.061064, 540, 1768), (1611330114.077835, 536, 770), (1611330114.087101, 530, 513), (1611330114.091696, 523, 600), (1611330114.105431, 514, 1405), (1611330114.118515, 505, 3420), (1611330114.123037, 493, 2024), (1611330114.138365, 491, 2510), (1611330114.146226, 484, 3654), (1611330114.154719, 473, 3351), (1611330114.160844, 462, 2595), (1611330114.171583, 458, 5537), (1611330114.18875, 449, 4473), (1611330114.189749, 440, 1424), (1611330114.203587, 438, 421), (1611330114.212605, 433, 296), (1611330114.222787, 427, 309), (1611330114.233332, 428, 282), (1611330114.244409, 432, 369), (1611330114.253403, 430, 476), (1611330114.265963, 428, 454), (1611330114.273371, 427, 428), (1611330114.283808, 426, 352), (1611330114.293689, 424, 284), (1611330114.309401, 425, 209), (1611330114.315264, 425, 145), (1611330114.329899, 424, 118), (1611330114.339685, 425, 101), (1611330114.344043, 425, 94), (1611330114.358308, 426, 94), (1611330114.369447, 427, 92), (1611330114.380095, 427, 101), (1611330114.387847, 427, 91), (1611330114.395466, 429, 98), (1611330114.410449, 429, 136), (1611330114.419411, 429, 140), (1611330114.421405, 428, 97), (1611330114.4372, 429, 83), (1611330114.443607, 430, 79), (1611330114.457199, 431, 79), (1611330114.464208, 431, 81), (1611330114.475373, 432, 75), (1611330114.484951, 433, 87), (1611330114.495166, 434, 102), (1611330114.505201, 434, 153), (1611330114.51613, 435, 291), (1611330114.52508, 437, 456), (1611330114.540752, 434, 565), (1611330114.550702, 431, 570), (1611330114.554896, 427, 481), (1611330114.57092, 423, 335), (1611330114.581602, 423, 139)]
data2 = [(1611330112.238344, 818, 130), (1611330112.250477, 828, 249), (1611330112.260074, 831, 387), (1611330112.275707, 822, 567), (1611330112.28261, 811, 779), (1611330112.295747, 797, 986), (1611330112.305927, 783, 1136), (1611330112.316429, 767, 1616), (1611330112.326123, 748, 7973), (1611330112.335593, 734, 8435), (1611330112.345348, 724, 4741), (1611330112.35541, 713, 6438), (1611330112.364006, 702, 7578), (1611330112.373038, 691, 9543), (1611330112.379028, 681, 12280), (1611330112.389908, 670, 13938), (1611330112.406778, 660, 15076), (1611330112.407775, 650, 15927), (1611330112.42425, 639, 17006), (1611330112.430209, 628, 17412), (1611330112.439726, 618, 15037), (1611330112.450582, 608, 11296), (1611330112.462325, 600, 7193), (1611330112.470097, 590, 3862), (1611330112.48715, 580, 9013), (1611330112.490727, 571, 6128), (1611330112.507017, 562, 7030), (1611330112.513515, 552, 6530), (1611330112.521221, 542, 6683), (1611330112.537371, 535, 5408), (1611330112.547084, 527, 4424), (1611330112.55764, 519, 3989), (1611330112.564894, 511, 3479), (1611330112.573414, 503, 3506), (1611330112.587611, 495, 3699), (1611330112.598218, 488, 4003), (1611330112.606277, 481, 4446), (1611330112.610476, 474, 4793), (1611330112.622137, 468, 4977), (1611330112.63812, 461, 4323), (1611330112.641237, 455, 2944), (1611330112.655519, 451, 1532), (1611330112.663381, 451, 712), (1611330112.672871, 454, 509), (1611330112.683387, 456, 443), (1611330112.698866, 464, 411), (1611330112.70883, 469, 417), (1611330112.712992, 472, 483), (1611330112.723671, 469, 813), (1611330112.738976, 464, 1464), (1611330112.749075, 460, 2033), (1611330112.758424, 457, 2532), (1611330112.761616, 456, 2767), (1611330112.778808, 455, 2862), (1611330112.788541, 454, 2874), (1611330112.799617, 454, 2863), (1611330112.806188, 453, 2853), (1611330112.813926, 453, 2839), (1611330112.829483, 453, 2821), (1611330112.83947, 453, 2800), (1611330112.842277, 453, 2796), (1611330112.855529, 453, 2805), (1611330112.862772, 453, 2808), (1611330112.873114, 453, 2776), (1611330112.883109, 453, 2735), (1611330112.893462, 454, 2694), (1611330112.904539, 454, 2662), (1611330112.91577, 454, 2672), (1611330112.924937, 455, 2702), (1611330112.93739, 453, 2344), (1611330112.944164, 450, 1607), (1611330112.96034, 450, 855), (1611330112.965888, 454, 528), (1611330112.980145, 459, 445), (1611330112.990495, 465, 456), (1611330112.996372, 473, 538), (1611330113.009984, 475, 677), (1611330113.020555, 472, 734), (1611330113.030863, 468, 870), (1611330113.040876, 464, 801), (1611330113.047079, 462, 539), (1611330113.061395, 462, 315), (1611330113.070552, 463, 146), (1611330113.073685, 465, 72)]

class EventTest(unittest.TestCase):
    def test_basicparameters(self):
        event = Event(data1)
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
        event = Event(data2)
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
        event = Event(data1)
        self.assertEqual((-37.600958045093144, 0.9937095824388414, 14), event.getSpeedFromMaxStrength())

    def test_speedFromMaxStrength2(self):
        event = Event(data2)
        self.assertEqual((-36.55802049469435, 0.9942769301227901, 17), event.getSpeedFromMaxStrength())

if __name__ == '__main__':
    unittest.main()
