#include <stdio.h>

void main(void)
{
  int arr[2][3] = { 100, 101, 102, 103, 104, 105 };

  int (*p)[3] = arr;
  
  printf("%d", p[1][2]);
}
