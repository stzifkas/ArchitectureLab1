#include <stdio.h>
#include <math.h>
//compiled with: arm-linux-gnueabihf-gcc -o arm_program --static roots.c -lm 
int main()
{
    double D, root1, root2, realPart, imaginaryPart;
    double a = 2;
    double b = 3;
    double c = 4;
    D = b*b-4*a*c;

    if (D >=0)
    {
        root1 = (-b+sqrt(D))/(2*a);
        root2 = (-b-sqrt(D))/(2*a);
        printf("root1 = %.2lf and root2 = %.2lf",root1 , root2);
    }
    else
    {
        realPart = -b/(2*a);
        imaginaryPart = sqrt(-D)/(2*a);
        printf("root1 = %.2lf+%.2lfi and root2 = %.2f-%.2fi", realPart, imaginaryPart, realPart, imaginaryPart);
    }
    return 0;
}
