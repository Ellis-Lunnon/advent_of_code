#include "day6.h"

int main() {
    std::cout << "part 1: ";
    int result1 = part1("day6.txt");
    std::cout << result1 << std::endl;

    std::cout << "part 2: ";
    int result2 = part2("day6.txt");
    std::cout << result2 << std::endl;
    return 0;
};

bool checkBuffer(char buffer[]) {
    // get buffer size
    for (int i = 0; i < 4; i++) {
        int count = 0;
        for (int j = 0; j < 4; j++) {
            if (buffer[i] == buffer[j]) {
                count++;
            }
        }
        if (count > 1) {
            return false;
        };
    };
    return true;
}

bool checkBufferFourteen(char buffer[]) {
    // get buffer size
    for (int i = 0; i < 14; i++) {
        int count = 0;
        for (int j = 0; j < 14; j++) {
            if (buffer[i] == buffer[j]) {
                count++;
            }
        }
        if (count > 1) {
            return false;
        };
    };
    return true;
}

int part1(std::string filename) {
    std::ifstream FileHandler(filename);

    FileHandler.seekg(0, FileHandler.end);
    int sz = FileHandler.tellg();
    FileHandler.seekg(0, FileHandler.beg);

    char *contents = new char[sz];
    FileHandler.read(contents, sz);

    // Start reading characters into the buffer
    char buf[4] = {};

    int maxIdx = sz;
    int idx = 0;
    while (idx <= maxIdx) {
        for (int i = 0; i < 4; i++) {
            buf[i] = contents[idx + i];
        };
        if (checkBuffer(buf)) {
            return idx + 4;
        };
        idx++;
    }
    std::cout << "Failed to find code" << std::endl;
    return 0;
}

int part2(std::string filename) {
    std::ifstream FileHandler(filename);

    FileHandler.seekg(0, FileHandler.end);
    int sz = FileHandler.tellg();
    FileHandler.seekg(0, FileHandler.beg);

    char *contents = new char[sz];
    FileHandler.read(contents, sz);

    // Start reading characters into the buffer
    char buf[14] = {};

    int maxIdx = sz;
    int idx = 0;
    while (idx <= maxIdx) {
        for (int i = 0; i < 14; i++) {
            buf[i] = contents[idx + i];
        };
        if (checkBufferFourteen(buf)) {
            return idx + 14;
        };
        idx++;
    }
    std::cout << "Failed to find code" << std::endl;
    return 0;
}