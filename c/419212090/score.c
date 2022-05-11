#include <stdio.h>
#define MAX_STU 100
#define MAX_COURSE 10
#define MAX_NAME_SIZE

void temp_score(int nstu, int ncrs, int s[MAX_STU][MAX_COURSE+2],int ss[MAX_STU]){
    for (int i = 0; i < nstu; i++) {
        for (int j = 0; j < (nstu - 1) - i; j++) {
            if (ss[j] < ss[j + 1]) {   

                int temp2 = ss[j];
                ss[j] = ss[j+1];
                ss[j + 1] = temp2;

                for (int k = 0; k < ncrs; k++) {
                    int temp = s[j][k];
                    s[j][k] = s[j + 1][k];
                    s[j + 1][k] = temp;
                }
            }
        }
    }
}

void input_scores(int nstu, int ncrs,int s[MAX_STU][MAX_COURSE+2],int ss[MAX_STU]){
    for(int i=0;i<nstu;i++){
        scanf("%d",&s[i][0]);
    }
    for(int n=0;n<ncrs;n++){
        for(int stu=0;stu<nstu;stu++){
            scanf("%d",&s[stu][n+1]);
            ss[stu] += s[stu][n+1];
        }
    }
}

void printf_scores(int nums,int ncrs,int s[MAX_STU][MAX_COURSE+2],int ss[MAX_STU]){
    int sum[MAX_STU]={0};
    printf("학번\t이름\t");
    for(int crs=1;crs<=ncrs;crs++){
        printf("과목%d\t",crs);
        if (crs == ncrs) {
            printf("총합");
        }
    }
    printf("\n");
    for(int stu=0;stu<nums;stu++){
    for(int crs=0;crs<=ncrs;crs++){  
        printf("%d\t",s[stu][crs]);
    }

    printf("%d", ss[stu]);       
    printf("\n");
    }
}

int main()
{
    int score[MAX_STU][MAX_COURSE+2];
    int numStu; //학생수
    int numCourse;//과목수 
    int score_sum[MAX_STU] = { 0 };
    char names[MAX_STU][;
    
    if(scanf("%d%d",&numStu,&numCourse) !=2){
        printf("입력오류\n");
        return 1;
    }

    //크기 check
    input_scores(numStu, numCourse,score,score_sum);
    temp_score(numStu,numCourse,score,score_sum);
    printf_scores(numStu,numCourse,score,score_sum);
}
