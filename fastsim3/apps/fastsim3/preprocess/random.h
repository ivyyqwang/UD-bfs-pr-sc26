#if !defined(RANDOM_HEADER_)
#define RANDOM_HEADER_

#include "common.h"

/* Spread the two 64-bit numbers into five nonzero values in the correct
 * range. */
static void make_mrg_seed(uint64_t userseed, uint_fast32_t* seed) {
  seed[0] = (userseed & 0x3FFFFFFF) + 1;
  seed[1] = ((userseed >> 30) & 0x3FFFFFFF) + 1;
  seed[2] = (userseed & 0x3FFFFFFF) + 1;
  seed[3] = ((userseed >> 30) & 0x3FFFFFFF) + 1;
  seed[4] = ((userseed >> 60) << 4) + (userseed >> 60) + 1;
}

void init_random (void)
{
	long seed = 0xDECAFBAD;
	userseed = seed;
	make_mrg_seed (seed, prng_seed);
	mrg_seed(&prng_state_store, prng_seed);
}

#endif