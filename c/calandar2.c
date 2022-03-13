#include <stdio.h>

/*
 * 날 수 계산 기준이 되는 날짜
 * 프로그램이 제대로 동작하는지 체크하기 위해 현재 날짜에 비슷하게 바꾼 후에 검증 가능
 */
#define INITIAL_YEAR	1
#define INITIAL_MONTH	1	//Do not change
#define INITIAL_DAY	1	//Do not change
#define INITIAL_DATE	0	//( 0 = MON, 1 = TUE, 2 = WED, 3 = THU, 4 = FRI, 5 = SAT, 6 = SUN)  

/* 한 달에 포함된 날수 */
const int aiDaysOfMonth[2][12] =
{
	/* Non-Lunar Year */
	{	31,	28,	31,	30,	31,	30,	31,	31,	30,	31,	30,	31	},

	/* Lunar Year */
	{	31,	29,	31,	30,	31,	30,	31,	31,	30,	31,	30,	31	}
};

const char* astrDate[7] =
{
	"MON",	"TUE",	"WED",	"THU",	"FRI",	"SAT",	"SUN"
};

void main()
{
	int iYear = 0;
	int iMonth = 0;
	int iDay = 0;
	int iElapsedDay = 0;
	int iLunarYear = 0;
	int i = 0;

	/* 연월일 입력 */
	printf("연 : ");
	scanf("%d", &iYear);

	printf("월 : ");
	scanf("%d", &iMonth);

	printf("일 : ");
	scanf("%d", &iDay);

	/* 1년에 365일씩 더하기 */
	iElapsedDay += (iYear - INITIAL_YEAR) * 365;

	/* 4년마다 오는 윤년은 1일씩 빼기 */
	iElapsedDay += (iYear - INITIAL_YEAR) / 4;

	/* 올해가 윤년인지 여부 (윤년이 아니면 0, 윤년이면 1) */
	if ( ( iYear % 4 ) == 0 )
	{
		iLunarYear = 1;
	}

	/* 월에 해당하는 날짜 수를 더함 */
	for( i = 1 ; i< iMonth ; i++ )
	{
		iElapsedDay += aiDaysOfMonth[iLunarYear][i - 1];
	}

	/* 일 수를 더함 */
	iElapsedDay += iDay;

	printf("%d\n", iElapsedDay);
	printf("%s\n", astrDate[ ( iElapsedDay + INITIAL_DATE - 1 ) % 7]);
}
