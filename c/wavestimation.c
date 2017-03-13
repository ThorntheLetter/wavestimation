// Please do not use C for actual generic things.
// If I were to actually use C I would rewrite this using actual types.
// Seriously though, do not write C like this.

#include <stdlib.h>
#include "wavestimation.h"
#include <stdio.h>

garray applyAlgs(garray fs, garray xs){
    garray ret = {.size = sizeof(garray), .length = fs.length, .data = malloc(ret.length * ret.size)};
    for(int i = 0; i < fs.length; i++){
        ((garray*)ret.data)[i] = (garray){.size = sizeof(garray), .length = xs.length, .data = malloc(xs.length * sizeof(garray))};
        for(int j = 0; j < xs.length; j++){
            ((garray*)((garray*)ret.data)[i].data)[j] = ((garray (**)(garray))fs.data)[i](((garray*)xs.data)[j]);
        }
    }
    return ret;
}

garray evalAlgs(garray eva, garray correct, garray results){
    garray ret;
    ret.size = sizeof(garray);
    ret.length = results.length;
    ret.data = malloc(results.length * sizeof(garray));
    for(int i = 0; i < results.length; i++){
        ((garray*)ret.data)[i].size = sizeof(garray);
        ((garray*)ret.data)[i].length = eva.length;
        ((garray*)ret.data)[i].data = malloc(eva.length * sizeof(garray));
        for(int j = 0; j < eva.length; j++){
            ((garray*)((garray*)ret.data)[i].data)[j].size = sizeof(garray);
            ((garray*)((garray*)ret.data)[i].data)[j].length = correct.length;
            ((garray*)((garray*)ret.data)[i].data)[j].data = malloc(correct.length * sizeof(garray));
            for(int k = 0; k < correct.length; k++){
                ((garray*)((garray*)((garray*)ret.data)[i].data)[j].data)[k] = ((garray (**)(garray, garray))eva.data)[j](((garray*)correct.data)[k], ((garray*)((garray*)results.data)[i].data)[k]);
            }
        }
    }
    return ret;
}