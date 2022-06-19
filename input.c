#include <stdio.h>
#include <stdlib.h>
int cmpfunc(const void *a, const void *b)
{
  return (*(int *)a - *(int *)b);
}
int main()
{
  int t;
  scanf("%d", &t);
  for (int v = 0; v < t; v++)
  {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++)
    {
      scanf("%d", &arr[i]);
    }
    qsort(arr, n, sizeof(int), cmpfunc);
    int c = 0;
    int ar[n];
    int j = 0;
    int temp = arr[0];
    for (int i = 0; i < n; i++)
    {
      if (arr[i] == temp)
      {
        c++;
      }
      else
      {
        ar[j] = c;
        c = 1;
        temp = arr[i];
        j++;
      }
    }
    ar[j] = c;
    j++;
    int max = 0;
    for (int i = 0; i < j; i++)
    {
      if (max < ar[i])
      {
        max = ar[i];
      }
    }
    int count = 0;
    for (int i = 0; i < j; i++)
    {
      if (max == ar[i])
      {
        count++;
      }
    }
    if (max == 1)
    {
      printf("%d\n", n);
      continue;
    }
    int ans = (((n - (max * count)) / (max - 1)) + count) - 1;
    printf("%d\n", ans);
  }
}