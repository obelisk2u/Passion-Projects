#include <iostream>
#include <vector>
#include <algorithm>  
#include <random>    
#include <ctime>  
#include <chrono>

using namespace std;

bool isSorted(const vector<int>& arr) {
    for (size_t i = 1; i < arr.size(); ++i) {
        if (arr[i] < arr[i - 1]) {
            return false;
        }
    }
    return true;
}

double bogoSort(vector<int>& arr) {
    mt19937 rng(time(0));  
    int i = 0;
    auto start = chrono::high_resolution_clock::now();
    while (!isSorted(arr)) {
        shuffle(arr.begin(), arr.end(), rng); 
        i++; 
    }
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;
    cout << "Sorted in: " << i << endl;
    return duration.count();
}

vector<int> new_array(){
    vector<int> arr;  
    random_device rd;   
    mt19937 gen(rd());   
    uniform_int_distribution<> dist(0, 7);   
    
    for (int j = 0; j < 10; ++j) {
        arr.push_back(dist(gen));   
    }

    return arr;
}

int main() { 

    double runtime;
    vector<double> times;
    for(int i = 0;i<100;i++){
        vector<int> arr = new_array();
        runtime = bogoSort(arr);
        times.push_back(runtime);
    }

    double sum = 0;
    for(int i=0;i<size(times);i++){
        sum+=times[i];
    }
    double avg = sum/size(times);
    printf("Average runtime: %.2f\n", avg);

    return 0;
}
