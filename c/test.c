#include <stdio.h>

int* MAX(int* ar);
int* MIN(int* ar);

int main() {
	int N;
	scanf("%d", &N);
	int ar[100];
	int i, cnt = 0;
	for (i = 0; i < N; i++) {
		while (1) {
			scanf("%d", (ar + cnt));
			if (*(ar + cnt) == 0) {
				printf("%d %d", *MAX(ar), *MIN(ar));
				cnt = 0;
				break;
			}
			else {
				cnt++;
			}
		}
	}
}

int* MAX(int* ar) {
	int* p;
	int max = *ar , *index = ar;
	int count = 0;
	while (*(ar + count) != 0) {
		count++;
	}
	for (p = ar; p < ar+count; p++) {
		if (max < *p) {
			max = *p;
			index = p;
		}
	}
	return index;
}

int* MIN(int* ar) {
	int* p;
	int min = *ar, *index = ar;
	int count = 0;
	while (*(ar + count) != 0) {
		count++;
	}
	for (p = ar; p < ar + count; p++) {
		if (min > *p) {
			min = *p;
			index = p;
		}
	}
	return index;
}
