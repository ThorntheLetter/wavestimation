#ifndef WAVESTIMATION_H
#define WAVESTIMATION_H
// Please do not use C for actual generic things.
// If I were to actually use C I would rewrite this using actual types.
// Seriously though, do not write C like this.

// generic array, just call it gary
typedef struct garray{
    unsigned int size; // size of an item in the array
    unsigned int length; // number of items in array
    void* data; // pointer to array data
} garray;

// UNTESTED, but it compiles
// fs is garray with data pointing to an array of pointers to functions that take and return a garray
// xs is garray pointing to input
// returns a garray pointing to an array of garrays that contain arrays of output
garray applyAlgs(garray fs, garray xs);

// UNTESTED, but it compiles
// eva is garray of pointers to the evaluation 
// correct is a garray of the correct input, or other data needed to evaluate the solution
// results is garray of garrays in the format that should be returned by applyAlgs
// returns a garray of garrays of garrays formatted in a way that just look at one of the other sources
garray evalAlgs(garray eva, garray correct, garray results);



#endif