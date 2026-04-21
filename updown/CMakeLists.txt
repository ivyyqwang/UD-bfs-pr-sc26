cmake_minimum_required(VERSION 3.13.4)

# Enable compile_commands.json generation for clangd and other tools
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

project(UpDown C CXX)

set(UPDOWN_INSTALL_DIR "${CMAKE_INSTALL_PREFIX}/updown")
set(UPDOWN_HEADERS_INSTALL_PATH "${UPDOWN_INSTALL_DIR}/include")
set(UPDOWN_LIB "${UPDOWN_INSTALL_DIR}/lib")
set(UPDOWN_RUNTIME_LIBRARY_INSTALL_PATH "${UPDOWN_INSTALL_DIR}/libraries")
set(UPDOWN_BIN "${UPDOWN_INSTALL_DIR}/bin")
set(UPDOWN_APPS "${UPDOWN_INSTALL_DIR}/apps")
set(UPDOWN_ASSEMBLER "${PROJECT_SOURCE_DIR}/udbasim/assembler")
set(UDWEAVE_DIR "${PROJECT_SOURCE_DIR}/udweave")
set(UDWEAVE "${UDWEAVE_DIR}/UDweave.py")
set(LINKER_DIR "${PROJECT_SOURCE_DIR}/linker")
set(LINKER "${LINKER_DIR}/EFAlinker.py")

# Setting the library path the the path in the installed directory.
# Otherwise, the compiled apps will not find the libraries copied to 
# ${CMAKE_INSTALL_PREFIX}/updown/libs.
set(CMAKE_INSTALL_RPATH "${UPDOWN_LIB}")
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

add_compile_definitions(BASE_PATH="${CMAKE_INSTALL_PREFIX}")

if (UPDOWN_ENABLE_FASTSIM)
  add_compile_definitions(FASTSIM=1)
  if (UPDOWN_FASTSIM_TRACE_MSG)
    add_compile_definitions(FASTSIM_TRACE_MSG=1)
  endif()
  if(UPDOWN_FASTSIM_NETWOORK_TRACE_MSG)
    add_compile_definitions(FASTSIM_NETWORK_TRACE=1)
  endif()
else()
    add_compile_definitions(GEM5_MODE=1)
    add_compile_definitions(GEM5SIM=1)
endif()

if(UPDOWN_ENABLE_BASIM)
  add_compile_definitions(BASIM=1)
endif()

if(UPDOWN_ENABLE_ASST_FASTSIM)
  add_compile_definitions(ASST_FASTSIM=1)
endif()

if(UPDOWN_SENDPOLICY)
  add_compile_definitions(SENDPOLICY=1)
endif()

if(UPDOWN_INST_TRACE)
  add_compile_definitions(DEBUG_INST_TRACE=1)
endif()
if(UPDOWN_DETAIL_STATS)
  add_compile_definitions(DETAIL_STATS=1)
  add_compile_definitions(MAX_BINS=2000)
  add_compile_definitions(BUCKET_SIZE=20)
  add_compile_definitions(MAX_COUNT_BINS=2000)
  add_compile_definitions(COUNT_BUCKET_SIZE=1)
  add_compile_definitions(MAX_BYTES_BINS=4096)
  add_compile_definitions(BYTES_BUCKET_SIZE=64)
  add_compile_definitions(NETWORK_STATS=1)
endif()
if(UPDOWN_ENABLE_FP)
  add_compile_definitions(ACTIVATE_FP=1)
endif()
if(UPDOWN_NETWORK_STATS)
  add_compile_definitions(NETWORK_STATS=1)
endif()

if(UPDOWN_DETAIL_INST_HIST)
  add_compile_definitions(INST_HIST=1)
endif()

if (UPDOWN_ENABLE_DEBUG)
  add_compile_definitions(DEBUG_MODE=1)
  if (DEFINED DEBUG_LOG_LEVEL)
    add_compile_definitions(DEBUG_MODE_LEVEL=${DEBUG_LOG_LEVEL})
  endif()
  set(UPDOWN_DEBUG True)
  # SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17 -fopenmp -ggdb -O0 -fsanitize=address -fno-omit-frame-pointer -static-libasan")
  SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17 -fopenmp -ggdb -O2")
else()
  set(UPDOWN_DEBUG False)
  # SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17 -fopenmp -ggdb -O3 -fsanitize=address -fno-omit-frame-pointer -static-libasan")
  SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17 -fopenmp -O3")
endif()

# Enable GNU Profiler
if (GPROF_ENABLE)
  SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17 -fopenmp -O3 -pg")
endif()

if (DEBUG_SYMBOLS)
  SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17 -fopenmp -ggdb -O3 ")
endif ()

if (DEFINED CMAKE_GEM5_BASE)
  set(GEM5_BASE_DIR "${CMAKE_GEM5_BASE}")
endif()

find_package(Python3 COMPONENTS Interpreter QUIET)

# check of the Python interpreter is available. It is not mandatory, but without it UDWeave will not work
if (NOT Python3_Interpreter_FOUND)
    message(WARNING "Python3 interpreter not found. You will not be able to compile UpDown applications.")
endif()

# check, if the udweave repository has been checked out
if (NOT EXISTS "${UDWEAVE}")
    message(WARNING "'${UDWEAVE}' does not exist! You will not be able to compile UDW sources. Have you checked out the git submodule (git submodule init; git submodule update in ${UDWEAVE_DIR})?")
endif()

include_directories(BEFORE
    udbasim/common/include
    udbasim/accel/include
    udbasim/lane/include
    udbasim/isa/include
    udbasim/mem/include
    ../common/include
    common/include
    runtime/include
    simruntime/include
    basimruntime/include)

if (ENABLE_SQLITE)
    include_directories(BEFORE ext/sqlite3)
    add_compile_definitions(ENABLE_SQLITE=1)
endif ()

if (ENABLE_LIBCONFIG)
    include_directories(BEFORE ext/libconfig/lib)
endif ()
set(APPS_WITH_LIBCONFIG "wf2k2_exactMatch")

install(FILES common/include/debug.h DESTINATION ${UPDOWN_HEADERS_INSTALL_PATH})


include(${CMAKE_CURRENT_SOURCE_DIR}/CMakeListsCompileAndInstall.txt)

## Building runtime system
add_subdirectory(runtime)
add_subdirectory(simruntime)
add_subdirectory(udbasim)
add_subdirectory(basimruntime)
add_subdirectory(libraries)

if (UPDOWNRT_ENABLE_APPS)
  add_subdirectory(apps)
endif()

if (UPDOWNRT_ENABLE_TE)
  add_subdirectory(te)
endif()

add_subdirectory(ext)

