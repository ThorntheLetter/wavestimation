import unittest
import wavestimation as w
import multiprocessing as mp

def add1(x):
    return x + 1

def mul2(x):
    return x * 2

def add(x,y):
    return x + y

def mul(x,y):
    return x * y

def app(x,y):
    x.append(y)
    return x

def ext(x,y):
    x.extend(y)
    return x

class FrameworkTests(unittest.TestCase):

    def test_applyAlgs(self):
        p = mp.Pool(w.POOL_SIZE)
        res1 = w.applyAlgs(p, [add1, mul2], [1,2,3,4])
        res2 = list(map(lambda x: x.get(), res1))
        self.assertEqual(res2, [[2,3,4,5], [2,4,6,8]])

    def test_evalAlgs(self):
        p = mp.Pool(w.POOL_SIZE)
        res1 = w.evalAlgs(p, [add, mul], [1,2], [[1,2],[3,4]])
        res2 = [[list(b.get()) for b in a] for a in res1]
        self.assertEqual(res2, [[[2,4],[1,4]],[[4,6],[3,8]]])

    def test_evalAlgs2(self):
        p = mp.Pool(w.POOL_SIZE)
        res1 = w.evalAlgs2(p, [app, ext], [1,2], [[1,2],[3,4]])
        res2 = [[list(b.get()) for b in a] for a in res1]
        self.assertEqual(res2, [[[1,2,[1,2]],[1,2,1,2]],[[1,2,[3,4]],[1,2,3,4]]])


if __name__ == '__main__':
    unittest.main()