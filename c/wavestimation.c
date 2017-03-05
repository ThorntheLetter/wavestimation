// Please do not use C for actual generic things.
// If I were to actually use C I would rewrite this using actual types.
// Seriously though, do not write C like this.

#include <stdlib.h>
#include "wavestimation.h"


// UNTESTED, but it compiles
// fs is garray with data pointing to an array of pointers to functions that take and return a garray
// xs is garray pointing to input
// returns a garray pointing to an array of garrays that contain arrays of output
garray applyAlgs(garray fs, garray xs){
	garray ret;
	ret.size = sizeof(garray);
	ret.length = fs.length;
	ret.data = malloc(fs.length * sizeof(garray));
	for(int i = 0; i < fs.length; i++){
		((garray*)ret.data)[i].size = sizeof(garray);
		((garray*)ret.data)[i].length = xs.length;
		((garray*)ret.data)[i].data = malloc(xs.length * sizeof(garray));
		for(int j = 0; j < xs.length; j++){
			((garray*)((garray*)ret.data)[i].data)[j] = ((garray (**)(garray))fs.data)[i](((garray*)xs.data)[j]);
		}
	}
	return ret;
}