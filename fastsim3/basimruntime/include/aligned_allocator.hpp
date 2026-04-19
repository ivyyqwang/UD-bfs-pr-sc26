#include <vector>
#include <memory>
#include <cstdlib>
#include <cstddef>
#include <iostream>

#ifdef __cpp_lib_hardware_interference_size
  static constexpr std::size_t hardware_constructive_interference_size = std::hardware_constructive_interference_size;
  static constexpr std::size_t hardware_destructive_interference_size = std::hardware_destructive_interference_size;
#else
  // 64 bytes on x86-64 │ L1_CACHE_BYTES │ L1_CACHE_SHIFT │ __cacheline_aligned
  // │
  // ...
  static constexpr std::size_t hardware_constructive_interference_size = 64;
  static constexpr std::size_t hardware_destructive_interference_size = 64;
#endif


#include <cstddef>
#include <cstdlib>
#include <memory>
#include <stdexcept>
#include <type_traits>

template <typename T, std::size_t Alignment = hardware_constructive_interference_size>
struct AlignedAllocator {
    using value_type = T;
    using pointer = T*;
    using const_pointer = const T*;
    using void_pointer = void*;
    using const_void_pointer = const void*;
    using size_type = std::size_t;
    using difference_type = std::ptrdiff_t;

    template <typename U>
    struct rebind {
        using other = AlignedAllocator<U, Alignment>;
    };

    AlignedAllocator() noexcept = default;

    template <typename U>
    AlignedAllocator(const AlignedAllocator<U, Alignment>&) noexcept {}

    [[nodiscard]] T* allocate(std::size_t n) {
        void* ptr = nullptr;
        if (posix_memalign(&ptr, Alignment, n * sizeof(T)) != 0) {
            throw std::bad_alloc();
        }
        return reinterpret_cast<T*>(ptr);
    }

    void deallocate(T* p, std::size_t) noexcept {
        std::free(p);
    }

    template <typename U, typename... Args>
    void construct(U* p, Args&&... args) {
        ::new((void*)p) U(std::forward<Args>(args)...);
    }

    template <typename U>
    void destroy(U* p) {
        p->~U();
    }

    // Required for C++11 allocator traits
    using is_always_equal = std::true_type;
    using propagate_on_container_move_assignment = std::true_type;
};

template <typename T1, std::size_t A1, typename T2, std::size_t A2>
inline bool operator==(const AlignedAllocator<T1, A1>&, const AlignedAllocator<T2, A2>&) {
    return A1 == A2;
}

template <typename T1, std::size_t A1, typename T2, std::size_t A2>
inline bool operator!=(const AlignedAllocator<T1, A1>& a, const AlignedAllocator<T2, A2>& b) {
    return !(a == b);
}
