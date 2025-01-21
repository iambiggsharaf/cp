#include <iostream>
#include <set>

int main() {
    int N, M;
    std::cin >> N; // ���������� ��������� ������� ������

    std::set<int> set1; // ��������� ��� ������� ������
    for (int i = 0; i < N; ++i) {
        int num;
        std::cin >> num;
        set1.insert(num);
    }

    std::cin >> M; // ���������� ��������� ������� ������

    std::set<int> set2; // ��������� ��� ������� ������
    for (int i = 0; i < M; ++i) {
        int num;
        std::cin >> num;
        set2.insert(num);
    }

    // ������� ����������� ���� ��������
    int count = 0;
    for (int num : set1) {
        if (set2.count(num)) {
            ++count;
        }
    }

    std::cout << count << std::endl;

    return 0;
}
