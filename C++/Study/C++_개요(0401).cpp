
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
    int num = 0b00010010; // 10진수 18
    int bit_position = 5; // 5번째 비트 (0부터 시작)
    
    num |= (1 << bit_position); // 5번째 비트를 1로 설정
    
    std::cout << "결과: " << num << " (2진수: " << std::bitset<8>(num) << ")" << std::endl;

    return 0;
}

//실습2.
#include <iostream>
#include <bitset>

int main() {
    int num = 0b10101111; // 10진수 175
    int bit_position = 2; // 2번째 비트 (0부터 시작)
    
    num &= ~(1 << bit_position); // 2번째 비트를 0으로 설정
    
    std::cout << "결과: " << num << " (2진수: " << std::bitset<8>(num) << ")" << std::endl;

    return 0;
}
