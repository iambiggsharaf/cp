#include <iostream>
#include <set>

int main() {
    int N, M;
    std::cin >> N; // Количество элементов первого списка

    std::set<int> set1; // Множество для первого списка
    for (int i = 0; i < N; ++i) {
        int num;
        std::cin >> num;
        set1.insert(num);
    }

    std::cin >> M; // Количество элементов второго списка

    std::set<int> set2; // Множество для второго списка
    for (int i = 0; i < M; ++i) {
        int num;
        std::cin >> num;
        set2.insert(num);
    }

    // Считаем пересечение двух множеств
    int count = 0;
    for (int num : set1) {
        if (set2.count(num)) {
            ++count;
        }
    }

    std::cout << count << std::endl;

    return 0;
}
