// #define NDEBUG

#include "wavestimation.h"
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>


garray plus1(garray in){
    assert(in.size == sizeof(int));
    assert(in.length == 1);
    int *y = malloc(sizeof(int)); // need to allocate new memory or else they will all point to the same stack memory
    *y = *((int*)in.data) + 1;
    garray ret = {.size = sizeof(int), .length = 1, .data = y};
    return ret;
}

garray mult2(garray in){
    assert(in.size == sizeof(int));
    assert(in.length == 1);
    int *y = malloc(sizeof(int));
    *y = *((int*)in.data) * 2;
    garray ret = {.size = sizeof(int), .length = 1, .data = y};
    return ret;
}


void testapplyAlgs(){
    int xs[2] = {1, 2};
    garray xdata[2] = {{.size = sizeof(int), .length = 1, .data = xs}, {.size = sizeof(int), .length = 1, .data = xs + 1}};
    garray (*fdata[2]) (garray) = {&plus1, &mult2};
    garray data = {.size = sizeof(int), .length = 2, .data = xdata};
    garray algs = {.size = sizeof(&plus1), .length = 2, .data = fdata};
    garray result = applyAlgs(algs, data);
    printf("testapplyAlgs:\nTARGET:\t[[2,3,],[2,4,],]\nRESULT:\t[");
    for(int i = 0; i < result.length; i++){
        printf("[");
        for(int j = 0; j < ((garray*)result.data)[i].length; j++){
            printf("%d,", *((int*)((garray*)((garray*)result.data)[i].data)[j].data)       );
        }
        printf("],");
    }
    printf("]\n");
}

int main(int argc, char** argcv){
    testapplyAlgs();
    return 0;
}