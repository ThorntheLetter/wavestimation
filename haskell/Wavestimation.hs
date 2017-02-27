import Framework
import Data.Complex
import Numeric.LinearAlgebra


-- wave: array in either time or frequency domain
-- type Wave = [Double] -- might change to int or unsigned int, still dont know where i will get data from and how it will be formatted
type Wave = Vector R -- Double Vector

-- sample: the target wave and the components used to try and reconstruct it
data Sample = Sample {target::Wave, components::Matrix R}

type Result = Vector R

-- compsToWave :: Result -> [Wave] -> Wave
-- compsToWave ms cs = 
--   do
--     let compsList = zipWith multComp ms cs
--     addComps (replicate (length compsList) 0) compsList

-- multComp :: Double -> Wave -> Wave
-- multComp k w = map ((*) k) w
 
-- addComps :: Wave -> [Wave] -> Wave
-- addComps base [] = base
-- addComps base (w:ws) = addComps (zipWith (+) base w) ws

compsToWave :: Result -> Matrix R -> Wave
compsToWave weights components = components #> weights








test :: (Num a) => a -> a -> a
test q w = q + w

test2 :: (Num a) => a -> a -> a
test2 q w = q * w


main =
  do
    putStrLn (show (evalAlgs [test, test2] [1,2] [[1,4],[2,5],[3,6]]))




-- result: target::wave, predicted::wave or maybe just multiplicities of the components. but what to do about phase?
-- algorithm: input::instance -> predicted::wave/result 
-- errcalc: input:result || predicted::wave, target::wave -> some insightful output, IO String maybe?