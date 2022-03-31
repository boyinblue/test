#include <stdio.h>
#include <stdlib.h>

typedef struct _A
{
	int size; // 아래에서 사용될 배열의 크기를 정합니다.
	int* matrix; // 포인터만 가지고 실제 크기는 동적 할당 합니::wq
} A;

int main()
{
	A stA;

	stA.size = 100;
	stA.matrix = malloc(stA.size);
}
