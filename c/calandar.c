#include <stdio.h>

const int aiDaysOfMonth[12] =
{
	31,	29,	31,	30,	31,	30,	31,	31,	30,	31,	30,	31
};

const char* astrDate[7] =
{
	"MON",	"TUE",	"WED",	"THU",	"FRI",	"SAT",	"SUN"
};

void main()
{
	int iYear = 1;
	int iMonth = 1;
	int iDay = 1;
	int iElapsedDay = 0;
	int i = 0;

	printf("연 : ");
	scanf("%d", &iYear);

	printf("월 : ");
	scanf("%d", &iMonth);

	printf("일 : ");
	scanf("%d", &iDay);

	iElapsedDay += (iYear - 1) * 365;

	for( i = 1 ; i< iMonth ; i++ )
	{
		iElapsedDay += aiDaysOfMonth[i - 1];
	}
	iElapsedDay += (iDay - 1);

	printf("%d\n", iElapsedDay);
	printf("%s\n", astrDate[iElapsedDay % 7]);
}
