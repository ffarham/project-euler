/**
 * Solution: Brute force.
 * - iterate through all 9 digit combinations multicand, multiplier, and product which are 1-9
 *  pandigital
 * - maintain a set of products already considered
 */

#include <iostream>
#include <string>
#include <unordered_set>

int main() {
    int64_t output{0};
    std::unordered_set<int> visitedProducts{};

    int currentNum{123456789};
    while (currentNum <= 987654321) {
        if (currentNum % 10000000 == 0) std::cout << currentNum << '\n';

        std::string currentNumStr = std::to_string(currentNum);
        for (int i = 1; i < 6; i++) { // operator index
            for (int j = 2; j < 7; j++) { // equal index
                std::string multiplicandStr = currentNumStr.substr(0, i);
                std::string multiplierStr = currentNumStr.substr(i, j - i);
                std::string productStr = currentNumStr.substr(j);

                int multiplicand = atoi(multiplicandStr.c_str());
                int multiplier = atoi(multiplierStr.c_str());
                int product = atoi(productStr.c_str());
                if (multiplicand * multiplier != product) continue;

                if (visitedProducts.find(product) != visitedProducts.end()) continue;

                bool isPanDigital{true};
                for (int k = 1; k <= 9; k++) {
                    bool foundK{false};
                    for (char numChar : currentNumStr) {
                        if (numChar == '0' + k) {
                            foundK = true;
                            break;
                        }
                    }
                    if (!foundK) {
                        isPanDigital = false;
                        break;
                    }
                }
                if (!isPanDigital) continue;
                std::cout << multiplicand << " * " << multiplier << " = " << product << '\n';
                visitedProducts.insert(product);
                output += product;
            }
        }
        ++currentNum;
    }

    std::cout << "Ans: " << output << '\n';
    return 0;
}