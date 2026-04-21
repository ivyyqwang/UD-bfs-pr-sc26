#if !defined(COMMON_HEADER_)
#define COMMON_HEADER_

#include <unistd.h>
#include <stdio.h>
#include <stdint.h>
#include <assert.h>
#include <stdlib.h>
#include "splittable_mrg.h"
#include "compat.h"

#define A_PARAM 0.57
#define B_PARAM 0.19
#define C_PARAM 0.19
/* Hence D = 0.05. */
#define default_edgefactor ((int64_t)16)

static double generation_time;

double A = A_PARAM;
double B = B_PARAM;
double C = C_PARAM;
double D = 1.0 - (A_PARAM + B_PARAM + C_PARAM);

int64_t edgefactor = default_edgefactor;
int64_t SCALE = 14;

uint64_t userseed;
uint_fast32_t prng_seed[5];
static mrg_state prng_state_store;
void *prng_state = &prng_state_store;


typedef struct packed_edge {
  int64_t v0;
  int64_t v1;
} packed_edge;

static inline int64_t get_v0_from_edge(const packed_edge* p) {
  return p->v0;
}

static inline int64_t get_v1_from_edge(const packed_edge* p) {
  return p->v1;
}

static inline void write_edge(packed_edge* p, int64_t v0, int64_t v1) {
  p->v0 = v0;
  p->v1 = v1;
}

int compare_second_desc(const void* a, const void* b) {
    int64_t a1 = ((const int64_t*)a)[1];
    int64_t b1 = ((const int64_t*)b)[1];
    if (a1 > b1) return -1;  // 降序
    if (a1 < b1) return 1;
    return 0;
}

int compare_first_inc(const void* a, const void* b) {
    int64_t a1 = ((const int64_t*)a)[0];
    int64_t b1 = ((const int64_t*)b)[0];
    if (a1 > b1) return 1;  // 升序
    if (a1 < b1) return -1;
    return 0;
}

#endif