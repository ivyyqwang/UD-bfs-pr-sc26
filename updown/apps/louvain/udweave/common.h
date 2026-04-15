#ifndef LOUVAIN_H
#define LOUVAIN_H

#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
#include <sys/types.h>
#include <sys/time.h>
#include <cassert>

/* --------- UpDown Header --------- */
#include <simupdown.h>
#include <dramalloc.hpp>
#include <basimupdown.h>
#include "louvain_exe.hpp"

using namespace std;

typedef struct vertex{
  uint64_t* neigh_ptr;
  uint64_t deg;
  uint64_t edges_before;
  uint64_t vid;
  int64_t community;  
  double tot;
  double in;
  double* weight_ptr; 
  uint64_t* neigh_pos;  
  double weight;
  int64_t new_community;  
  double new_increase;  
  uint64_t vertex_weight;   
  int64_t old_community;  
  uint64_t reserved3;  
  uint64_t reserved4;
} vertex_t;


#define NUM_THREAD 64


#endif // LOUVAIN_H
