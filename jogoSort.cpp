#include <iostream>
#include <vector>
#include <algorithm>
#include <cuda_runtime.h>

__global__ void check_sorted(int *permutations, bool *result, int numPermutations, int arraySize) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;

    if (idx < numPermutations) {
        bool isSorted = true;
        for (int i = 0; i < arraySize - 1; ++i) {
            if (permutations[idx * arraySize + i] > permutations[idx * arraySize + i + 1]) {
                isSorted = false;
                break;
            }
        }
        result[idx] = isSorted;
    }
}

int main() {
    const int arraySize = 10;
    const int numPermutations = 50;

    int permutations[numPermutations][arraySize] = {
            {1, 2, 3, 4, 5, 6, 7, 8, 0, 9},
            {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}, 
        };

    int *d_permutations;
    bool *d_result;
    bool *result = new bool[numPermutations];

    cudaMalloc((void **)&d_permutations, numPermutations * arraySize * sizeof(int));
    cudaMalloc((void **)&d_result, numPermutations * sizeof(bool));

    cudaMemcpy(d_permutations, permutations, numPermutations * arraySize * sizeof(int), cudaMemcpyHostToDevice);
    int blockSize = 256;  
    int numBlocks = (numPermutations + blockSize - 1) / blockSize;   
    check_sorted<<<numBlocks, blockSize>>>(d_permutations, d_result, numPermutations, arraySize);

    cudaMemcpy(result, d_result, numPermutations * sizeof(bool), cudaMemcpyDeviceToHost);

    for (int i = 0; i < numPermutations; ++i) {
        if (result[i]) {
            std::cout << "Sorted permutation found at index " << i << std::endl;
            for (int j = 0; j < arraySize; ++j) {
                std::cout << permutations[i][j] << " ";
            }
            std::cout << std::endl;
            break;
        }
    }

    cudaFree(d_permutations);
    cudaFree(d_result);
    delete[] result;

    return 0;
}
