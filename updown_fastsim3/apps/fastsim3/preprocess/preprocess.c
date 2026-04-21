#include "common.h"
#include "random.h"
#include "xalloc.h"
#include "timer.h"
#include "rmat.h"
#include <string.h>

#include <time.h>


#if defined(CLOCK_MONOTONIC)
#define TICTOC_CLOCK CLOCK_MONOTONIC
#define TICTOC_CLOCK_NAME "CLOCK_MONOTONIC"
#elif defined(CLOCK_REALTIME)
#define TICTOC_CLOCK CLOCK_REALTIME
#define TICTOC_CLOCK_NAME "CLOCK_REALTIME"
#else
#error "Failed to find a timing clock."
#endif

int main (int argc, char **argv){
	struct timespec whole_time_start, whole_time_end, tmp_time_start, tmp_time_end;
	double out_time = 0;
	if (sizeof (int64_t) < 8) {
		fprintf (stderr, "No 64-bit support.\n");
		return EXIT_FAILURE;
	}
	if(argc!= 4)
    {
        printf("%s <scale> <output_filename> <max_deg>\n",argv[0]);
        return 1;
    }

	clock_gettime (TICTOC_CLOCK, &whole_time_start);
	SCALE = atoi(argv[1]);
	int64_t nvtx_scale = ((int64_t)1)<<SCALE;
	char* filename = argv[2];
	int max_degree = atoi(argv[3]);

	int64_t nedge = nvtx_scale * edgefactor;
	
	assert (nedge >= nvtx_scale);
	assert (nedge >= edgefactor);

	init_random();
	printf("build_degree_vec %lu\n", (nvtx_scale * sizeof (int64_t))); fflush(stdout);
	int64_t *deg_list = xmalloc_large_ext (nvtx_scale * sizeof (int64_t));
    memset(deg_list, 0, nvtx_scale * sizeof (int64_t));
	
	TIME(generation_time, rmat_edgelist_deg_bfs(deg_list, nedge, SCALE, A, B, C));

	printf ("build deg time: %20.17e\n", generation_time); fflush(stdout);

	printf ("deglist[0]: %ld, deglist[1]: %ld\n", deg_list[0], deg_list[1]); fflush(stdout);

	generation_time = 0;

	
	clock_gettime (TICTOC_CLOCK, &tmp_time_start);
	int64_t num_nodes = 0;
	int64_t num_split_nodes = 0;
	OMP("omp parallel") {
		int64_t i;
		#pragma omp parallel for reduction(+:num_nodes, num_split_nodes)
		for(i = 0; i < nvtx_scale; i++){
			if(deg_list[i] > 0){
				num_nodes++;
				int64_t num_split = (deg_list[i] - 1) / max_degree;
				if(num_split > 0)
					num_split_nodes = num_split_nodes + num_split + 1;
			}
		}
	}
	clock_gettime (TICTOC_CLOCK, &tmp_time_end);
	out_time = (tmp_time_end.tv_nsec - (double)tmp_time_start.tv_nsec) * 1.0e-9;
	out_time += (tmp_time_end.tv_sec - (double)tmp_time_start.tv_sec);
	printf ("compute split verts time: %20.17e\n", out_time); fflush(stdout);
	printf ("num of verts = %lu, num of split verts = %lu, default num of verts = %lu\n",  num_nodes, num_split_nodes, nvtx_scale);

	int64_t total_nodes = num_nodes + num_split_nodes;

	int64_t *deg_list2 = xmalloc_large_ext (total_nodes * sizeof (int64_t));
	int64_t *orig_vid_list2 = xmalloc_large_ext (total_nodes * sizeof (int64_t));
	int64_t *offset_list2 = xmalloc_large_ext ((total_nodes + 1) * sizeof (int64_t));
	int64_t *split_start_vid_list2 = xmalloc_large_ext (total_nodes * sizeof (int64_t));
	int64_t *split_end_vid_list2 = xmalloc_large_ext (total_nodes * sizeof (int64_t));
	offset_list2[0] = 0;

	clock_gettime (TICTOC_CLOCK, &tmp_time_start);
	int64_t *new_id = xmalloc_large_ext (nvtx_scale * sizeof (int64_t));
	int64_t vid = 0;
	int64_t split_vid = num_nodes;
	for(int64_t i = 0; i < nvtx_scale; i++){
		if(deg_list[i] > 0){
			new_id[i] = vid;
			orig_vid_list2[vid] = vid;
			int64_t num_split = (deg_list[i] - 1) / max_degree;
			int64_t deg = deg_list[i];
			if(num_split == 0) { // not split
				deg_list2[vid] = deg;
				split_start_vid_list2[vid] = 0;
				split_end_vid_list2[vid] = 0;
			}else{
				deg_list2[vid] = 0;
				num_split = num_split + 1;
				int64_t vid_start = split_vid;
				int64_t vid_end = vid_start + num_split;
				split_start_vid_list2[vid] = vid_start;
				split_end_vid_list2[vid] = vid_end;
				for(; split_vid < vid_end; split_vid++){
					int64_t split_deg = deg / num_split;
					if((split_vid - vid_start) < deg % num_split){
						split_deg++;
					}
					deg_list2[split_vid] = split_deg;
					orig_vid_list2[split_vid] = vid;
					split_start_vid_list2[split_vid] = vid_start;
					split_end_vid_list2[split_vid] = vid_end;
				}

			}
			vid++;
		}
	}
	clock_gettime (TICTOC_CLOCK, &tmp_time_end);
	out_time = (tmp_time_end.tv_nsec - (double)tmp_time_start.tv_nsec) * 1.0e-9;
	out_time += (tmp_time_end.tv_sec - (double)tmp_time_start.tv_sec);
	printf ("build vertex structure time: %20.17e\n", out_time); fflush(stdout);
	xfree_large (deg_list);
	deg_list = NULL;
	
	int64_t block_size = 256 * 1024 * 1024; // 256MB
	int64_t int64_block = block_size / sizeof(int64_t); // 256MB

	int64_t edge_block_length = nvtx_scale * 8;
	int64_t num_block = edgefactor * 2 / 8 + 8;
	int64_t vid_range[num_block + 1];
	vid_range[0] = 0;

	int64_t* buffer = xmalloc_large_ext(block_size);
	memset(buffer, 0, block_size);
	int64_t* buffer2 = xmalloc_large_ext(block_size);
	memset(buffer2, 0, block_size);
	int64_t num_vid = int64_block / 8;
	int64_t vid_size = num_vid * 8 * sizeof(int64_t);
	int64_t next_vid = 0;
	int64_t offset = 0;
	int64_t iter = 1;
	int64_t previous_offset = 0;

	/*---------------------- Write to gv file ---------------------- */
	clock_gettime (TICTOC_CLOCK, &tmp_time_start);

	char binfile_bfs_gv[256];
	snprintf(binfile_bfs_gv, sizeof(binfile_bfs_gv), "%s_gv.bin", filename);
	char* binfilename = binfile_bfs_gv; 
	printf("Binfile:%s\n", binfilename);
	FILE* out_file0 = fopen(binfilename, "wb");
    if (!out_file0) {
          exit(EXIT_FAILURE);
    }
    fseek(out_file0, 0, SEEK_SET);
    printf("Size of uint64_t:%d, writing num_vertices:%llu, num_split_vertices:%llu in new file\n", sizeof(uint64_t), num_nodes, total_nodes);
	fwrite(&num_nodes, sizeof(int64_t), 1, out_file0);
    fwrite(&total_nodes, sizeof(int64_t), 1, out_file0);

	offset = 0;
	for(int64_t k = 0; k < total_nodes; k++){
		int64_t deg = deg_list2[k];
		offset += deg;
		if((offset % 8) > 0)
			offset = offset + (8 - (offset % 8));
		offset_list2[k + 1] = offset;
		if((offset - previous_offset) > (edge_block_length)){
			if(split_start_vid_list2[k] == 0 || split_start_vid_list2[k] == k){
				vid_range[iter] = k;
				iter++;
				previous_offset = offset_list2[k];
			}else{
				vid_range[iter] = split_start_vid_list2[k];
				iter++;
				previous_offset = offset_list2[split_start_vid_list2[k]];
			}
		}
	}

	vid_range[iter] = total_nodes;
	

	clock_gettime (TICTOC_CLOCK, &tmp_time_end);
	out_time = (tmp_time_end.tv_nsec - (double)tmp_time_start.tv_nsec) * 1.0e-9;
	out_time += (tmp_time_end.tv_sec - (double)tmp_time_start.tv_sec);
	printf ("compute offset time: %20.17e\n", out_time); fflush(stdout);


	/*---------------------- Write to nl file ---------------------- */
	clock_gettime (TICTOC_CLOCK, &tmp_time_start);

	char binfile_nl[256];
	snprintf(binfile_nl, sizeof(binfile_nl), "%s_nl.bin", filename);
	binfilename = binfile_nl; 
    printf("Binfile:%s\n", binfilename);
    FILE* out_file1 = fopen(binfilename, "wb");
    if (!out_file1) {
          exit(EXIT_FAILURE);
    }
    fseek(out_file1, 0, SEEK_SET);
	fwrite(&(offset_list2[total_nodes]), sizeof(uint64_t), 1, out_file1);
	fwrite(&(offset_list2[total_nodes]), sizeof(uint64_t), 1, out_file1);

	printf("num_offset[%lu] = %lu\n", total_nodes, offset_list2[total_nodes]); fflush(stdout);


	int64_t *offset_list = xmalloc_large_ext ((total_nodes+1) * sizeof (int64_t));
	memcpy((void *)offset_list, (void *)offset_list2, (num_nodes+1) * sizeof (int64_t));

	int64_t *offset_list3 = xmalloc_large_ext ((total_nodes+1) * sizeof (int64_t));
	memcpy((void *)offset_list3, (void *)offset_list2, (total_nodes+1) * sizeof (int64_t));
	
	int64_t *edge_list = xmalloc_large_ext (edge_block_length * sizeof (int64_t));
	int64_t *edge_list2 = xmalloc_large_ext (edge_block_length * sizeof (int64_t));
	printf("edge_block_length = %ld\n", edge_block_length); fflush(stdout);
	offset = 0;

	int64_t *idx_list = xmalloc_large_ext (num_nodes * sizeof (int64_t));
	int64_t edge_offset = 0;
	int64_t edges = 0;

	size_t written = 0;

	for(int64_t i=0; i<iter; i++){
		memset(edge_list, 0, edge_block_length * sizeof (int64_t));
		memset(edge_list2, 0, edge_block_length * sizeof (int64_t));
		memset(idx_list, 0, num_nodes * sizeof (int64_t));
		init_random();
		printf("iter:%ld, min_vid:%ld, max_vid:%ld, min_offset:%ld, max_offset:%ld\n", i, vid_range[i], vid_range[i+1], offset_list2[vid_range[i]], offset_list2[vid_range[i+1]]);
		TIME(generation_time, rmat_generate_bfs_edges (new_id, nedge, SCALE, A, B, C, offset_list3, edge_list, idx_list, split_start_vid_list2, split_end_vid_list2, vid_range[i], vid_range[i+1], offset_list2[vid_range[i]]));
		printf ("build edgelist time: %20.17e\n", generation_time); fflush(stdout);
		generation_time = 0;
		int64_t length = (offset_list2[vid_range[i+1]] - offset_list2[vid_range[i]]);
		// printf("iter:%ld, min_vid:%ld, max_vid:%ld, min_offset:%ld, max_offset:%ld\n", i, vid_range[i], vid_range[i+1], offset_list2[vid_range[i]], offset_list2[vid_range[i+1]]);
		if(length > edge_block_length){
			printf("error, length = %ld > edge_block_length = %ld\n", length, edge_block_length);
			exit(1);
		}
		int64_t start_offset = offset_list2[vid_range[i]];
		OMP("omp parallel") {
			OMP("omp for") 
			for(int64_t j = vid_range[i]; j < vid_range[i+1]; j++){
				int64_t * addr = &(edge_list[(offset_list2[j] - start_offset)]);
				qsort(addr, deg_list2[j], sizeof(int64_t), compare_first_inc);
				int64_t deg = 0;
				if(deg_list2[j] > 0){
					int64_t * addr1 = &(edge_list[(offset_list2[j] - start_offset) + 1]);
					int64_t * addr2 = &(edge_list[(offset_list2[j] - start_offset) + deg_list2[j]]);
					for(; addr1 < addr2; addr1 = addr1 + 1){
						if (addr1[0] != addr[deg]) {
							deg++;
							addr[deg] = addr1[0];
						}
					}
					deg++;
					deg_list2[j] = deg;
					edges = edges + deg;
				}
			}
		}
		// printf ("sort edgelist finish\n"); fflush(stdout);
		next_vid = vid_range[i];
		offset_list[0] = 0;
		int64_t start_offset0 = offset_list[vid_range[i]];
		int64_t end_vid = vid_range[i+1];
		for(int64_t k = vid_range[i]; k < end_vid;){
			// printf("k = %ld\n", k); fflush(stdout);
			int64_t i;
			for(i = 0; i < num_vid; i++){
				// printf("k = %ld, i = %ld, vid = %ld, end_vid = %ld\n", k, i, next_vid + i, end_vid); fflush(stdout);
				int64_t deg = deg_list2[next_vid + i];
				if((next_vid + i) >= end_vid){
					k = end_vid;
					break;
				}
				buffer[8*i] = deg;
				buffer2[4*i] = next_vid + i;
				buffer[8*i+1] = next_vid + i;
				buffer2[4*i+1] = deg;
				memcpy(&(edge_list2[(offset_list[next_vid + i] - start_offset0)]), &(edge_list[(offset_list2[next_vid + i] - start_offset)]), deg*sizeof(int64_t));
				offset += deg;
				while((offset % 8) > 0){
					edge_list2[offset - start_offset0] = -1;
					offset++;
				}
				offset_list[next_vid + i + 1] = offset;
				buffer[8*i+2] = offset_list[next_vid + i];
				buffer2[4*i+2] = offset_list[next_vid + i];
				buffer[8*i+3] = orig_vid_list2[next_vid + i];
				buffer2[4*i+3] = 1.0;
				buffer[8*i+4] = split_start_vid_list2[next_vid + i];
				buffer[8*i+5] = split_end_vid_list2[next_vid + i];
				buffer[8*i+6] = 0;
				buffer[8*i+7] = -1;
				
				// if((next_vid + i) == 17759405){
				// 	printf("N(17759405) (deg:%llu, offset:%llu, %llu) = [", deg, offset_list[next_vid + i], offset_list[next_vid + i + 1]);
				// 	for(int64_t j = 0; j < 10; j++){
				// 		printf(" %llu(%llu)", edge_list2[(offset_list[next_vid + i] - start_offset0) + j], (offset_list[next_vid + i] - start_offset) + j);
				// 	}
				// 	printf("]\n");
				// }
			}
			written = fwrite(buffer, sizeof(int64_t), 8*i, out_file0);
			// printf("k = %ld, i = %ld, num_vid = %ld, iter = %ld, offset = %ld, written = %ld, sizeof(int64_t) = %ld\n", k, i*8, num_vid, iter, offset, written, sizeof(int64_t)); fflush(stdout);
			k += i;
			next_vid = next_vid + i;
		}
		start_offset = offset_list[vid_range[i]];

		// /* print some neighbor to check */
		// for(int64_t j = vid_range[i]; j < vid_range[i]+10; j++){
		// 	printf("vid = %ld, deg = %ld: ", j, new_deg_list[j]);
		// 	int64_t * addr1 = &(edge_list2[(offset_list[j] - start_offset)]);
		// 	int64_t * addr2 = &(edge_list2[(offset_list[j+1] - start_offset)]);
		// 	for(; addr1 < addr2; addr1 = addr1 + 1){
		// 		printf("%ld, ", *addr1);
		// 	}
		// 	printf("\n");
		// 	fflush(stdout);
		// }
		int64_t total_len = offset_list[vid_range[i+1]] - offset_list[vid_range[i]];
		edge_offset = edge_offset + total_len;
		printf("total_len = %ld, edge_offset = %lld\n", total_len, edge_offset);
		fflush(stdout);
		for(int64_t offset = 0; offset < total_len; offset += int64_block){
			int64_t len = int64_block;
			// if(offset == 0){
			// 	for(int k = 0; k < 10; k = k + 1){
			// 		printf("%ld, ", edge_list2[offset + k]);
			// 	}
			// 	printf("\n");
			// 	fflush(stdout);
			// }
			if((offset + len) > total_len){
				len = total_len - offset;
				fwrite(&(edge_list2[offset]), sizeof(int64_t), len, out_file1);
				break;
			}
			fwrite(&(edge_list2[offset]), sizeof(int64_t), len, out_file1);
		}
	}

	fseek(out_file1, 0, SEEK_SET);
	fwrite(&edges, sizeof(uint64_t), 1, out_file1);
	fwrite(&edge_offset, sizeof(uint64_t), 1, out_file1);

	fclose(out_file0);
	fclose(out_file1);

	clock_gettime (TICTOC_CLOCK, &tmp_time_end);
	out_time = (tmp_time_end.tv_nsec - (double)tmp_time_start.tv_nsec) * 1.0e-9;
	out_time += (tmp_time_end.tv_sec - (double)tmp_time_start.tv_sec);
	printf ("write bin_nl_file time: %20.17e\n", out_time); fflush(stdout);


	clock_gettime (TICTOC_CLOCK, &whole_time_end);
	out_time = (whole_time_end.tv_nsec - (double)whole_time_start.tv_nsec) * 1.0e-9;
	out_time += (whole_time_end.tv_sec - (double)whole_time_start.tv_sec);
	printf ("Total time: %20.17e\n", out_time); fflush(stdout);

	return 0;

}