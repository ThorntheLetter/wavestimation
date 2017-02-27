module Framework where

-- apply all the algorithms to all the samples
-- xs: list of functions to apply
-- ys: list of samples
-- returns list of lists, [[fx1, f1x2...],[f2x1, f2x2...]...]
applyAlgs :: [a -> b] -> [a] -> [[b]]
applyAlgs [] _  = []
applyAlgs (f:fs) xs = map f xs : applyAlgs fs xs

-- evaluate accuracy of results from applyAlgs using all methods
-- eva: list of evaluation algorithms
-- correct: list of correct answers (or other data needed to determine them)
-- returns list of lists of lists, [[[f1e1x1, f1e1x2...],[f1e2x1, f1e2x2...]...],[[f2e1x1, f2e1x2...],[f2e2x1, f2e2x2...]...]...]
evalAlgs :: [a -> b -> c] -> [a] -> [[b]] -> [[[c]]]
evalAlgs [] _ _ = []
evalAlgs eva correct results = [[zipWith f correct result | f <- eva] | result <- results]

-- evaluate accuracy of results from applyAlgs using all methods, but all samples together
-- eva: list of evaluation algorithms
-- correct: list of correct answers (or other data needed to determine them)
-- returns list of lists, [[f1e1xs, f1e2xs...],[f2e1xs, f2e2xs]...]
evalAlgs2 :: [[a] -> [b] -> c] -> [a] -> [[b]] -> [[c]]
evalAlgs2 [] _ _ = []
evalAlgs2 eva correct results = [[f correct result | f <- eva] | result <- results]