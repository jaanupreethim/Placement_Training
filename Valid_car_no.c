#include <stdio.h>

int main()
{
    int carNo, temp, sum = 0;

    printf("Enter the car no:");
    scanf("%d", &carNo);

    if (carNo < 1000 || carNo > 9999)
    {
        printf("%d is not a valid car number", carNo);
        return 0;
    }

    temp = carNo;

    while (temp > 0)
    {
        sum += temp % 10;
        temp /= 10;
    }

    if (sum % 3 == 0 || sum % 5 == 0 || sum % 7 == 0)
        printf("Lucky Number");
    else
        printf("Sorry its not my lucky number");

    return 0;
}
