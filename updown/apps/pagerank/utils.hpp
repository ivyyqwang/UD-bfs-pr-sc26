
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <string>
#include <sys/time.h>
#include <sys/types.h>

#ifndef DRAMALLOC
#define DRAMALLOC
#include "dramalloc.hpp"
#endif

bool almostEqual(double a, double b, double epsilon = 1e-6) {
  if (a == 0) {
    return b == 0;
  }
  if (b == 0) {
    return a == 0;
  }
  if (a < b) {
    return (b - a) / a <= epsilon;
  } else {
    return (a - b) / b <= epsilon;
  }
  // return std::abs(a - b)/a <= epsilon;
  // return a == b;
}


uint64_t next_power_of_2(uint64_t n) {
  if (n == 0)
    return 1;
  n--;
  n |= n >> 1;
  n |= n >> 2;
  n |= n >> 4;
  n |= n >> 8;
  n |= n >> 16;
  n |= n >> 32;
  return n + 1;
}

bool is_power_of_2(uint64_t x) { return x && !(x & (x - 1)); }

uint64_t next_power_of_2_or_same(uint64_t n) {
  if (n == 0)
    return 1;
  if (is_power_of_2(n))
    return n;
  return next_power_of_2(n);
}

size_t getMemoryUsageKB() {
  std::ifstream status("/proc/self/status");
  std::string line;
  while (std::getline(status, line)) {
    if (line.rfind("VmRSS:", 0) == 0) {
      std::istringstream iss(line);
      std::string key, value, unit;
      iss >> key >> value >> unit;
      return std::stoul(value); // VmRSS is in KB
    }
  }
  return 0;
}

size_t CopyGlobal2Local(dramalloc::DramAllocator *allocator, uint64_t chunck_size, uint64_t global_addr, uint64_t local_addr, uint64_t copy_size) {
  uint64_t current_copy_size = 0;
  uint64_t current_global_addr = global_addr;
  uint64_t current_local_addr = local_addr;
  while (current_copy_size < copy_size) {
    uint64_t size = chunck_size;
    if ((copy_size - current_copy_size) < size)
      size = copy_size - current_copy_size;
    void *current_global_addr_sa = allocator->translate_udva2sa(current_global_addr);
    memcpy(reinterpret_cast<void *>(current_local_addr), current_global_addr_sa, size);
    current_copy_size = current_copy_size + size;
    current_global_addr = current_global_addr + size;
    current_local_addr = current_local_addr + size;
  }
  return current_copy_size;
}
size_t CopyLocal2Global(dramalloc::DramAllocator *allocator, uint64_t chunck_size, uint64_t global_addr, uint64_t local_addr, uint64_t copy_size) {
  uint64_t current_copy_size = 0;
  uint64_t current_global_addr = global_addr;
  uint64_t current_local_addr = local_addr;
  while (current_copy_size < copy_size) {
    uint64_t size = chunck_size;
    if ((copy_size - current_copy_size) < size)
      size = copy_size - current_copy_size;
    void *current_global_addr_sa = allocator->translate_udva2sa(current_global_addr);
    memcpy(current_global_addr_sa, reinterpret_cast<void *>(current_local_addr), size);
    current_copy_size = current_copy_size + size;
    current_global_addr = current_global_addr + size;
    current_local_addr = current_local_addr + size;
  }
  return current_copy_size;
}
