#include <stdlib.h>
#include <stdio.h>

int main() {
  int a = 5;
  int *p = NULL;

  p = &a;
  *p = 20;

  // printf("a = %d\n", a);

  int **p2 = &p;
  **p2 = 30;

  printf("a = %d\n", a);
}