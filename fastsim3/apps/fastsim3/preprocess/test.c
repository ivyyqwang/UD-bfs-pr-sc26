#include <stdio.h>
#include <omp.h>
#include <stdint.h>

int main() {
    int64_t counter = 0;

    #pragma omp parallel for
    for (int i = 0; i < 1000000; ++i) {
        __sync_fetch_and_add(&counter, 1);
    }

    printf("Expected: 1000000, Actual: %ld\n", counter);
    return 0;
}