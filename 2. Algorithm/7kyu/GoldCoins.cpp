#include<stdio.h>

int main()
{
   int num, i, cnt = 1;
   int sum = 0;
   int coin = 1;
   printf("* 기사의 근무일수를 입력하세요 : ");
   scanf("%d", &num);

   while(1)
   {
   		for(i = 0 ; i < coin ; i++)
   		{
   			sum += coin;
   			cnt++;
   			if ( cnt == num){ break; }
   		}

   		coin++;
   }





   printf("근무일 : %d / 총 금화수 : %d\n", num, sum);
   return 0;
}

1 2 3 4 5 6 7 8 9 10

1 2 2 3 3 3 4 4 4 4  5 5 5 5 6 6 6 6 