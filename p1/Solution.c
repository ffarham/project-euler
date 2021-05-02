#include <stdio.h>
#include <stdbool.h>

/* Function Prototypes */
bool isMultiple(int);   // returns true if the given int is either a multiple of 3 or 5 and false otherwise 
//--

int main(){
    int i, sum = 0;
    for(i = 1; i < 1000; i++){
        if(isMultiple(i)){sum += i;}    // updates the sum if i is a multiple
    }
    printf("Ans: %d\n", sum);
}

bool isMultiple(int n){
    return n % 3 == 0 || n % 5 == 0;
}