#include <stdio.h>

struct fraction {
  int numerator;
  int denominator;
  char code;
  long filler;
};

struct node {
  int data;
  struct node* next;
};

typedef struct fraction Fraction;

int main() {
  /* Regular struct */ 
  struct fraction f1, f2;
  f1.numerator = 22;
  f1.denominator = 7;

  f2 = f1;

  // printf("Fraction 1 numerator = %d, denominator = %d\n", f1.numerator, f1.denominator);
  // printf("Fraction 2 numerator = %d, denominator = %d\n", f2.numerator, f2.denominator);

  /* Array of struct */
  struct fraction numbers[100];
  numbers[0].numerator = 22;
  numbers[0].denominator = 7;

  numbers[1] = numbers[0];
  
  // printf("Fraction 1 numerator = %d, denominator = %d\n", numbers[0].numerator, numbers[0].denominator);
  // printf("Fraction 2 numerator = %d, denominator = %d\n", numbers[1].numerator, numbers[1].denominator);

  /* Onto pointers */
  struct fraction *fn = numbers;
  fn[0].numerator = 24;
  fn[0].denominator = 8;

  fn[1] = fn[0];

  // printf("Fraction 1 numerator = %d, denominator = %d\n", numbers[0].numerator, numbers[0].denominator);
  // printf("Fraction 2 numerator = %d, denominator = %d\n", numbers[1].numerator, numbers[1].denominator);

  /* Manual pointer increment on second fraction*/
  (*(fn + 1)).numerator = 16;
  (*(fn + 1)).denominator = 60;
  printf("Fraction 2 numerator = %d, denominator = %d\n", numbers[1].numerator, numbers[1].denominator);
  
  /* More pointer manipulations - cast to a void* and manually increment, in this case, editing fifth fraction*/
  (*((struct fraction*)((void*)fn + 4 * sizeof(struct fraction)))).numerator = 20;
  (*((struct fraction*)((void*)fn + 4 * sizeof(struct fraction)))).denominator = 30;
  printf("Fraction 5 numerator = %d, denominator = %d\n", numbers[4].numerator, numbers[4].denominator);


}