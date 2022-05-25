#include <stdio.h>

void dump_data( int iRows, int iCols, int (*arr)[3] )
{
  int i = 0;
  int j = 0;

  for ( i = 0 ; i < iRows ; i++ )
  {
    for ( j = 0 ; j < iCols ; j++ )
    {
      printf("%d ", arr[i][j]);
    }
    printf("\n");
  }
}

void main(void)
{
  int arr[2][3] = { 100, 101, 102, 103, 104, 105 };

  dump_data( 2, 3, arr);
}
