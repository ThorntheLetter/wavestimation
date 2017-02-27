import numpy as np
import multiprocessing as mp

POOL_SIZE = mp.cpu_count()

#p: process pool
#fs: list of estimation algorithms
#ds: list of samples
#returns a list of lists, [[f1d1,f1d2,f1d3...],[f2d1,f2d2,f2d3...]...]
def applyAlgs(p, fs, ds):
    return list(map(lambda f: p.map_async(f,ds), fs))

#p: process pool
#evals: list of evaluation algorithms
#correct: list of correct answers
#resultsList: list of lists as given by applyAlgs
#returns list of list of lists [[[f1e1d1,f1e1d2...],[f1e2d1,f1e2d2...]...][[f2e1d1,f2e1d2...],[f2e2d1,f2e2d2...]...]...]
def evalAlgs(p, evals, correct, resultsList):
    return [[p.starmap_async(j, zip(correct, i)) for j in evals] for i in resultsList]

#p: process pool
#evals: list of evaluation algorithms
#correct: list of correct answers
#resultsList: list of lists as given by applyAlgs
#returns list of lists [[f1e1ds, f1e2ds...],[f2e1ds,f2e2ds...]...]
def evalAlgs2(p, evals, correct, resultsList):
    return [[p.apply_async(f, args = (correct, i)) for f in evals] for i in resultsList]

def main():
    pool = mp.Pool(processes = POOL_SIZE)

if __name__ == '__main__':
    main()