
// 변수 저장 방법: 자료형 식별자 = 데이터;(int data = 100;)

#include <iostream>
#include <string>

int main() {
    string name;
    int age;

    // 이름 입력
    std::cout << "이름을 입력하세요: ";
    std::cin >> name;

    // 나이 입력
    std::cout << "나이를 입력하세요: ";
    std::cin >> age;

    // 출력
    std::cout << "안녕하세요! " << name << "님(" << age << "세)" << std::endl;

    return 0;
}

// 실습1.
#include <iostream>

int main() {
    int num = 0b00010010;
    int bit_position = 5;
    
    num |= (1 << bit_position);
    
    std::cout << "결과: " << num << " (2진수: " << std::bitset<8>(num) << ")" << std::endl;

    return 0;
}

//실습2.
#include <iostream>
#include <bitset>

int main() {
    int num = 0b10101111;
    int bit_position = 2;
    
    num &= ~(1 << bit_position);
    
    std::cout << "결과: " << num << " (2진수: " << std::bitset<8>(num) << ")" << std::endl;

    return 0;
}

//실습3.
#include <iostream>

int main() {
    unsigned int num = 0b11011010;
    unsigned int mask = 1 << 3;

    num ^= mask;

    std::cout << "반전된 결과: " << std::bitset<8>(num) << std::endl;

    return 0;
}

//실습4.
#include <iostream>

int main() {
    unsigned int num;
    std::cout << "숫자를 입력하세요: ";
    std::cin >> num;

    unsigned int bit = (num >> 3) & 1; // 4번째 비트(0-based index) 추출

    std::cout << "4번째 비트: " << bit << std::endl;

    return 0;
}

//실습5.
#include <iostream>

int main() {
    int num;
    std::cout << "숫자를 입력하세요: ";
    std::cin >> num;

    if (num % 2 == 0) {
        std::cout << num << "은(는) 짝수입니다." << std::endl;
    } else {
        std::cout << num << "은(는) 홀수입니다." << std::endl;
    }

    return 0;
}

//실습6.
#include <iostream>

bool isPowerOfTwo(unsigned int num) {
    return (num > 0) && ((num & (num - 1)) == 0);
}

int main() {
    unsigned int num;
    std::cout << "숫자를 입력하세요: ";
    std::cin >> num;

    if (isPowerOfTwo(num)) {
        std::cout << num << "은(는) 2의 거듭제곱입니다." << std::endl;
    } else {
        std::cout << num << "은(는) 2의 거듭제곱이 아닙니다." << std::endl;
    }

    return 0;
}

//실습7.
#include <iostream>
#include <bitset>

int findLeftmostSetBit(unsigned int num) {
    if (num == 0) return -1; // 1이 없을 경우 -1 반환

    int position = 0;
    while (num != 0) {
        position++;
        num >>= 1;
    }
    return position;
}


int main() {
    unsigned int num;
    std::cout << "숫자를 입력하세요: ";
    std::cin >> num;

    int leftmostBitPosition = findLeftmostSetBit(num);
    
    if (leftmostBitPosition != -1) {
        std::cout << "가장 왼쪽에 있는 1 비트의 위치: " << leftmostBitPosition << std::endl;
    } else {
        std::cout << "1 비트가 존재하지 않습니다." << std::endl;
    }

    return 0;
}

//실습8.
#include <iostream>

int findRightmostSetBit(unsigned int num) {
    if (num == 0) return -1; // 1이 없을 경우 -1 반환
    return __builtin_ctz(num) + 1; // 가장 오른쪽 1 비트의 위치 (1-based index)
}

int main() {
    unsigned int num;
    std::cout << "숫자를 입력하세요: ";
    std::cin >> num;

    int rightmostBitPosition = findRightmostSetBit(num);
    
    if (rightmostBitPosition != -1) {
        std::cout << "가장 오른쪽에 있는 1 비트의 위치: " << rightmostBitPosition << std::endl;
    } else {
        std::cout << "1 비트가 존재하지 않습니다." << std::endl;
    }

    return 0;
}


// 실습1.
int age;
cout << "나이를 입력하세요: ";
cin >> age;

if (age >= 1 && age <= 7) {
cout << "유아입니다.\n";
} else if (age >= 8 && age <= 13) {
cout << "초등학생입니다.\n";
} else if (age >= 14 && age <= 16) {
cout << "중학생입니다.\n";
} else if (age >= 17 && age <= 19) {
cout << "고등학생입니다.\n";
} else if (age >= 20 && age < 200) {
cout << "성인입니다.\n";
} else if (age >= 200) {
cout << "나이가 너무 많습니다.\n";
} else {
cout << "올바른 나이를 입력하세요.\n";
    }

int num;
cout << "숫자를 입력하세요: ";
cin >> num;

cout << (num % 5 == 0 ? to_string(num) + "는 5의 배수입니다." : to_string(num) + "는 5의 배수가 아니네요 ㅠㅠ") << std::endl;

// 실습1

int num;
cout << "숫자를 입력하세요: ";
cin >> num;

for (int i = 0; i < num; i++) {
    for (int j = 0; j <= i; j++) {
        cout << "*";
    }
    cout << endl;
}

// 실습2

for (int i = 1; i <= 9; i++) {
    for (int j = 1; j <= 9; j++) {
        cout << i << " x " << j << " = " << i * j << "\n";
    }

cout << endl;
