import numpy as np
import experiment as e
import multiprocessing as mp
import json
import wave

POOL_SIZE = mp.cpu_count()

#takes input frame and width of sample in bytes and transforms it into a number between -1 and 1, assuming it is signed
#might want to change these to be based on range instead of size
def squash(input, width = 2):
    return(input / (2 ** ((8 * width) - 1)))

#reverses squash()
def unsquash(input, width = 2):
    return(input * (2 ** ((8 * width) - 1)))

vsquash = np.vectorize(squash) #might want to do this in parallel once i find out better what the overhead would be
vunsquash = np.vectorize(unsquash)


class sample():
    def __init__(self, target = None, components = None, json = None):
        if(json): self.fromjson(json); return   
        self.target = target #might want to see if it would be easy to insure correct numpy array types
        self.components = 

    def fromjson(self, filename):
        json_file = open(filename)
        json_data = json.load(json_file)
        json_file.close()
        targetfile = wave.open(json_data['target'])
        self.target = vsquash(np.fromstring(targetfile.readframes(targetfile.getnframes()), dtype = 'int16'))
        targetfile.close()
        samplefiles = list(map(wave.open, json_data['components']))
        self.components = np.zeros((len(samplefiles), len(self.target)))
        for i, s in enumerate(samplefiles):
            sample = vsquash(np.fromstring(s.readframes(s.getnframes()), dtype = 'int16'))
            self.components[i] = sample[:len(self.target)]

def main():
    pool = mp.Pool(processes = POOL_SIZE)

if __name__ == '__main__':
    main()