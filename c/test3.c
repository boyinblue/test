#include <stdio.h>

int main(void)
{
  int month;
  int fee;

  printf("what month? ");
  scanf("%d", &month);
  fee = ( month >= 6 && month <= 8 )? 70000:35000;
  printf("entrance fee = %d\n", fee);
}
