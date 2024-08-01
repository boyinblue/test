#include <stdio.h>

void print_unicode(FILE* fp, unsigned long ulStart, unsigned long ulCnt)
{
  int i = 0 ;
  unsigned long ulCode = ulStart;

  for( i = 0 ; i < ulCnt ; i++ )
  {
    fprintf(fp, "0x%lx : ", ulCode);
    fwrite(&ulCode, sizeof(ulCode), 1, fp);
    fprintf(fp, "\n");
    ulCode += 0x01000000;
  }
}

void main()
{
  FILE* fp = NULL;

  fp = fopen("output.txt","w");

//print_unicode(fp, 0xF09F9880, 0x100);
  print_unicode(fp, 0x80989FF0, 0x100);
}
