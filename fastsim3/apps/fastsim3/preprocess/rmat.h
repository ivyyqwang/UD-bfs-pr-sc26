#ifndef RMAT_H
#define RMAT_H

void atomic_min(int64_t *addr, int64_t val) {
    int old = *addr;
    while ((old == 0 || old > val) && !__sync_bool_compare_and_swap(addr, old, val)) {
        old = *addr;  // 如果失败则重新读值再试
    }
}

void atomic_max(int64_t *addr, int64_t val) {
    int old = *addr;
    while (old < val && !__sync_bool_compare_and_swap(addr, old, val)) {
        old = *addr;  // 如果失败则重新读值再试
    }
}

#define NRAND(ne) (5 * SCALE * (ne))

static void rmat_edge (struct packed_edge *out, int SCALE, double A, double B, double C, double D, const double *rn)
{
    size_t rni = 0;
    int64_t i = 0, j = 0;
    int64_t bit = ((int64_t)1) << (SCALE-1);

    while (1) {
        const double r = rn[rni++];
        if (r > A) { /* outside quadrant 1 */
            if (r <= A + B) /* in quadrant 2 */
                j |= bit;
            else if (r <= A + B + C) /* in quadrant 3 */
                i |= bit;
            else { /* in quadrant 4 */
                j |= bit;
                i |= bit;
            }
        }
        if (1 == bit) break;

        /*
        Assuming R is in (0, 1), 0.95 + 0.1 * R is in (0.95, 1.05).
        So the new probabilities are *not* the old +/- 10% but
        instead the old +/- 5%.
        */
        A *= 0.95 + rn[rni++]/10;
        B *= 0.95 + rn[rni++]/10;
        C *= 0.95 + rn[rni++]/10;
        D *= 0.95 + rn[rni++]/10;
        /* Used 5 random numbers. */

        {
            const double norm = 1.0 / (A + B + C + D);
            A *= norm; B *= norm; C *= norm;
        }
        /* So long as +/- are monotonic, ensure a+b+c+d <= 1.0 */
        D = 1.0 - (A + B + C);
        
        bit >>= 1;
    }
    /* Iterates SCALE times. */
    write_edge(out, i, j);
    write_edge(out, j, i);
}

void rmat_edgelist_deg (int64_t *deg_in, int64_t nedge, int SCALE, double A, double B, double C){
    double D = 1.0 - (A + B + C);

    OMP("omp parallel") {
        int64_t k;
    #if !defined(__MTA__)
        double * restrict Rlocal = alloca (NRAND(1) * sizeof (*Rlocal));
    #endif
        mrg_state new_st = *(mrg_state*)prng_state;

        OMP("omp for") MTA("mta assert parallel") MTA("mta use 100 streams")
        for (k = 0; k < nedge; ++k) {
            struct packed_edge IJ;
            int k2;
            #if defined(__MTA__)
                double * restrict Rlocal = alloca (NRAND(1) * sizeof (*Rlocal));
            #endif
            mrg_skip (&new_st, 1, NRAND(1)*k, 0);
            for (k2 = 0; k2 < NRAND(1); ++k2)
                Rlocal[k2] = mrg_get_double_orig (&new_st);
            rmat_edge (&IJ, SCALE, A, B, C, D, Rlocal);
            uint64_t idx1 = IJ.v0*2 + 1;
            uint64_t idx2 = IJ.v1*2 + 1;
        if(idx1 != idx2){
            // __sync_fetch_and_add((volatile int64_t *)&(deg_in[idx1]), 1);
            // __sync_fetch_and_add((volatile int64_t *)&(deg_in[idx2]), 1);
            #ifdef _OPENMP
            #pragma omp atomic
            #endif    
                deg_in[idx1]++;

            #ifdef _OPENMP
            #pragma omp atomic
            #endif 
                deg_in[idx2]++;
            }
        }
    }
    mrg_skip (prng_state, 1, NRAND(1)*nedge, 0);
}

void rmat_vertex_structure (int64_t *new_id, int64_t nedge, int SCALE, double A, double B, double C, int64_t *new_deg_list){
    double D = 1.0 - (A + B + C);

    OMP("omp parallel") {
        int64_t k;
    #if !defined(__MTA__)
        double * restrict Rlocal = alloca (NRAND(1) * sizeof (*Rlocal));
    #endif
        mrg_state new_st = *(mrg_state*)prng_state;

        OMP("omp for") MTA("mta assert parallel") MTA("mta use 100 streams")
        for (k = 0; k < nedge; ++k) {
            struct packed_edge IJ;
            int k2;
            #if defined(__MTA__)
                double * restrict Rlocal = alloca (NRAND(1) * sizeof (*Rlocal));
            #endif
            mrg_skip (&new_st, 1, NRAND(1)*k, 0);
            for (k2 = 0; k2 < NRAND(1); ++k2)
                Rlocal[k2] = mrg_get_double_orig (&new_st);
            rmat_edge (&IJ, SCALE, A, B, C, D, Rlocal);
            uint64_t v0 = new_id[IJ.v0];
            uint64_t v1 = new_id[IJ.v1];
            if(v1 < v0){
                #ifdef _OPENMP
                #pragma omp atomic
                #endif    
                    new_deg_list[v0]++;
                // atomic_min(&(min_vid_list[v0]), v1);
                // atomic_max(&(max_vid_list[v0]), v1);
            }else if(v0 < v1){
                #ifdef _OPENMP
                #pragma omp atomic
                #endif    
                    new_deg_list[v1]++;
                // atomic_min(&(min_vid_list[v1]), v0);
                // atomic_max(&(max_vid_list[v1]), v0);
            }
        }
    }
    mrg_skip (prng_state, 1, NRAND(1)*nedge, 0);
}

void rmat_generate_edges(int64_t *new_id, int64_t nedge, int SCALE, double A, double B, double C, int64_t *offset_list, int64_t *edge_list, int64_t min_vid, int64_t max_vid, int64_t start_offset){
    double D = 1.0 - (A + B + C);

    OMP("omp parallel") {
        int64_t k;
    #if !defined(__MTA__)
        double * restrict Rlocal = alloca (NRAND(1) * sizeof (*Rlocal));
    #endif
        mrg_state new_st = *(mrg_state*)prng_state;

        OMP("omp for") MTA("mta assert parallel") MTA("mta use 100 streams")
        for (k = 0; k < nedge; ++k) {
            struct packed_edge IJ;
            int k2;
            #if defined(__MTA__)
                double * restrict Rlocal = alloca (NRAND(1) * sizeof (*Rlocal));
            #endif
            mrg_skip (&new_st, 1, NRAND(1)*k, 0);
            for (k2 = 0; k2 < NRAND(1); ++k2)
                Rlocal[k2] = mrg_get_double_orig (&new_st);
            rmat_edge (&IJ, SCALE, A, B, C, D, Rlocal);
            uint64_t v0 = new_id[IJ.v0];
            uint64_t v1 = new_id[IJ.v1];
            if(v1 < v0){
                if(min_vid <= v0 && v0 < max_vid){
                    int64_t offset = __sync_fetch_and_add(&(offset_list[v0]), 1);
                    offset = (offset - start_offset);
                    // printf("offset_list0[%ld] = %ld\n", v0, offset); fflush(stdout);
                    edge_list[offset] = v1;
                }
            }else if(v0 < v1){
                if(min_vid <= v1 && v1 < max_vid){
                    int64_t offset = __sync_fetch_and_add(&(offset_list[v1]), 1);
                    offset = (offset - start_offset);
                    // printf("offset_list1[%ld] = %ld\n", v1, offset); fflush(stdout);
                    edge_list[offset] = v0;
                }
            }
        }
    }
    mrg_skip (prng_state, 1, NRAND(1)*nedge, 0);
}


void rmat_edgelist (struct packed_edge *IJ_in, int64_t nedge, int SCALE, double A, double B, double C){
    struct packed_edge * restrict IJ = IJ_in;
    double D = 1.0 - (A + B + C);

    // int64_t* restrict iwork;
    // iwork = xmalloc_large_ext ((1L<<SCALE) * sizeof (*iwork));

    OMP("omp parallel") {
        int64_t k;
    #if !defined(__MTA__)
        double * restrict Rlocal = alloca (NRAND(1) * sizeof (*Rlocal));
    #endif
        mrg_state new_st = *(mrg_state*)prng_state;

        OMP("omp for") MTA("mta assert parallel") MTA("mta use 100 streams")
        for (k = 0; k < nedge; ++k) {
            int k2;
            #if defined(__MTA__)
                double * restrict Rlocal = alloca (NRAND(1) * sizeof (*Rlocal));
            #endif
            mrg_skip (&new_st, 1, NRAND(1)*k, 0);
            for (k2 = 0; k2 < NRAND(1); ++k2)
                Rlocal[k2] = mrg_get_double_orig (&new_st);
            rmat_edge (&IJ[k], SCALE, A, B, C, D, Rlocal);
        }

        // OMP("omp single")
        // mrg_skip (prng_state, 1, NRAND(nedge), 0);
        // OMP("omp barrier");
        // new_st = *(mrg_state*)prng_state;
        // permute_vertex_labels (IJ, nedge, (1L<<SCALE), &new_st, iwork);
        // OMP("omp single")
        // mrg_skip (prng_state, 1, (1L<<SCALE), 0);
        // OMP("omp barrier");
        // new_st = *(mrg_state*)prng_state;
        // permute_edgelist (IJ, nedge, &new_st);
    }
    mrg_skip (prng_state, 1, NRAND(1)*nedge, 0);

    // xfree_large (iwork);
}

/*---------------------- pr and bfs ----------------------*/
void rmat_edgelist_deg_bfs (int64_t *deg_in, int64_t nedge, int SCALE, double A, double B, double C){
    double D = 1.0 - (A + B + C);

    OMP("omp parallel") {
        int64_t k;
    #if !defined(__MTA__)
        double * restrict Rlocal = alloca (NRAND(1) * sizeof (*Rlocal));
    #endif
        mrg_state new_st = *(mrg_state*)prng_state;

        OMP("omp for") MTA("mta assert parallel") MTA("mta use 100 streams")
        for (k = 0; k < nedge; ++k) {
            struct packed_edge IJ;
            int k2;
            #if defined(__MTA__)
                double * restrict Rlocal = alloca (NRAND(1) * sizeof (*Rlocal));
            #endif
            mrg_skip (&new_st, 1, NRAND(1)*k, 0);
            for (k2 = 0; k2 < NRAND(1); ++k2)
                Rlocal[k2] = mrg_get_double_orig (&new_st);
            rmat_edge (&IJ, SCALE, A, B, C, D, Rlocal);
            uint64_t idx1 = IJ.v0;
            uint64_t idx2 = IJ.v1;
        if(idx1 != idx2){
            // __sync_fetch_and_add((volatile int64_t *)&(deg_in[idx1]), 1);
            // __sync_fetch_and_add((volatile int64_t *)&(deg_in[idx2]), 1);
            #ifdef _OPENMP
            #pragma omp atomic
            #endif    
                deg_in[idx1]++;

            #ifdef _OPENMP
            #pragma omp atomic
            #endif 
                deg_in[idx2]++;
            }
        }
    }
    mrg_skip (prng_state, 1, NRAND(1)*nedge, 0);
}

void rmat_generate_bfs_edges(int64_t *new_id, int64_t nedge, int SCALE, double A, double B, double C, int64_t *offset_list, int64_t *edge_list, int64_t *idx_list, int64_t *split_start_vid_list, int64_t *split_end_vid_list, int64_t min_vid, int64_t max_vid, int64_t start_offset){
    double D = 1.0 - (A + B + C);

    OMP("omp parallel") {
        int64_t k;
    #if !defined(__MTA__)
        double * restrict Rlocal = alloca (NRAND(1) * sizeof (*Rlocal));
    #endif
        mrg_state new_st = *(mrg_state*)prng_state;

        OMP("omp for") MTA("mta assert parallel") MTA("mta use 100 streams")
        for (k = 0; k < nedge; ++k) {
            struct packed_edge IJ;
            int k2;
            #if defined(__MTA__)
                double * restrict Rlocal = alloca (NRAND(1) * sizeof (*Rlocal));
            #endif
            mrg_skip (&new_st, 1, NRAND(1)*k, 0);
            for (k2 = 0; k2 < NRAND(1); ++k2)
                Rlocal[k2] = mrg_get_double_orig (&new_st);
            rmat_edge (&IJ, SCALE, A, B, C, D, Rlocal);
            uint64_t v0 = new_id[IJ.v0];
            uint64_t v1 = new_id[IJ.v1];
            if(split_start_vid_list[v0] > 0){ // split
                int64_t idx = __sync_fetch_and_add(&(idx_list[v0]), 1);
                int64_t split_num = split_end_vid_list[v0] - split_start_vid_list[v0];
                idx = idx % split_num;
                v0 = split_start_vid_list[v0] + idx;
                // if(min_vid <= v0 && v0 < max_vid){
                //     printf("v0 = %lu, new split v0 = %lu\n", new_id[IJ.v0], v0); fflush(stdout);
                // }
            }
            if(split_start_vid_list[v1] > 0){ // split
                int64_t idx = __sync_fetch_and_add(&(idx_list[v1]), 1);
                int64_t split_num = split_end_vid_list[v1] - split_start_vid_list[v1];
                idx = idx % split_num;
                v1 = split_start_vid_list[v1] + idx;
                // if(min_vid <= v1 && v1 < max_vid){
                //     printf("v1 = %lu, new split v1 = %lu\n", new_id[IJ.v1], v1); fflush(stdout);
                // }
            }
            if(min_vid <= v0 && v0 < max_vid){
                int64_t offset = __sync_fetch_and_add(&(offset_list[v0]), 1);
                offset = (offset - start_offset);
                // if(v0 == 9359623)
                //     printf("offset_list0[%ld] = %ld, v1 = %ld\n", v0, offset, v1); fflush(stdout);
                edge_list[offset] = v1;
            }
            if(min_vid <= v1 && v1 < max_vid){
                int64_t offset = __sync_fetch_and_add(&(offset_list[v1]), 1);
                offset = (offset - start_offset);
                // if(v1 == 9359623)
                //     printf("offset_list1[%ld] = %ld, v0 = %ld\n", v1, offset, v0); fflush(stdout);
                edge_list[offset] = v0;
            }

        }
    }
    mrg_skip (prng_state, 1, NRAND(1)*nedge, 0);
}

#endif