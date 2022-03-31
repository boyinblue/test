#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS

int main() {
	int arr[3] = {0,};
	char id[7+1];

	FILE* fp = fopen("in.txt", "r");
	FILE* fp2 = fopen("out.txt", "w");

	printf(" \n           중간 고사 성적 일람표      \n");
	fprintf(fp2, " \n           중간 고사 성적 일람표      \n");
	printf("\n=====================================\n");
	fprintf(fp2, "\n=====================================\n");
	printf("  학번   국어   영어  수학  총점  평균\n");
	fprintf(fp2, "  학번   국어   영어  수학  총점  평균\n");
	printf("\n=====================================\n");
	fprintf(fp2, "\n=====================================\n");
	while (fscanf(fp, "%s %lf %lf %lf", id, &kor, &eng, &mat) != EOF) {

		sum += kor + eng + mat;

		printf("\n%s %lf %lf %lf %lf %lf", id, kor, eng, mat, sum, sum / 3);
		fprintf(fp2, "\n%s %lf %lf %lf %lf %lf", id, kor, eng, mat, sum, sum / 3);
	}
	fclose(fp);
	fclose(fp2);
	return 0;
}
