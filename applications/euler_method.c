#include <stdlib.h>
#include <stdio.h>
#include <math.h>

typedef double (*deriv_f)(double, double);
#define FMT " %7.3f"

void ivp_euler(deriv_f f, double y, int step, int end_t)
{
  int t = 0;

  //printf(" Step %2d: ", (int)step);
  do {
    //if (t % 10 == 0) printf(FMT, y);
    y += step * f(t, y);
  } while ((t += step) <= end_t);
  //printf("\n");
}


double cooling(double t, double temp)
{
  return -0.07 * (temp - 20);
}

int run_benchmark()
{
  ivp_euler(cooling, 100, 2, 100);
  ivp_euler(cooling, 100, 5, 100);
  ivp_euler(cooling, 100, 10, 100);

  return 0;
}

int main(int argc, char *argv[])
{
  int n = atoi(argv[1]);
  for (int i = 0; i < n; ++i)
    run_benchmark();
  return 0;
}
