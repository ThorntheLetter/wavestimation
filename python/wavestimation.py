import numpy as np
import experiment as e
import multiprocessing as mp
import json

POOL_SIZE = mp.cpu_count()

#takes input frame and width of sample in bytes and transforms it into a number between -1 and 1, assuming it is signed
def squash(input, width = 2):
    return((input / (2 ** ((8 * width) - 1))) - 1)

#reverses squash()
def unsquash(input, width = 2):
    return(input * (2 ** ((8 * width) - 1)))

vsquash = np.vectorize(squash) #might want to do this in parallel once i find out better what the overhead would be
vunsquash = np.vectorize(unsquash)


class sample():
    def __init__(self, target = None, samples = None, json = None):
        if(json): self.fromjson
        self.target = target #might want to see if it would be easy to insure correct numpy array types
        self.samples = samples

    def fromjson(self, filename):
        json_data = json.load(open(filename))
        filename.close()
        targetfile = wave.open(json_data['target'])
        self.target = np.fromstring(targetfile.readframes(file.getnframes()),dtype = 'int16')
        self.target = vsquash(self.target)
        targetfile.close()
        samplefiles = json_data['samples']
        samplefiles = map(wave.open, samplefiles)
        self.samples = np.zeros((len(self.target), len(samplefiles)))
        for s, i in enumerate(samplefiles):
            sample = vsquash(np.fromstring(x.readframes(file.getnframes()), dtype = 'int16'))
            self.samples[i] = sample[i,:len(target)]

def main():
    pool = mp.Pool(processes = POOL_SIZE)

if __name__ == '__main__':
    main()