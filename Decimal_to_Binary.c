#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, temp, count1 = 0, i = 0;

    printf("Enter a decimal number: ");
    scanf("%d", &n);

    if (n < 0)
    {
        printf("Invalid Input\n");
        return 0;
    }

    temp = n;

    if (n == 0)
    {
        printf("Binary: 0\n");
        printf("Invalid Input\n");
        return 0;
    }

    int *binary = (int *)malloc(32 * sizeof(int));

    while (temp > 0)
    {
        binary[i] = temp % 2;

        if (binary[i] == 1)
            count1++;

        temp = temp / 2;
        i++;
    }

    printf("Binary: ");

    for (int j = i - 1; j >= 0; j--)
        printf("%d", binary[j]);

    printf("\n");

    if (count1 > 0)
        printf("Count of 1's = %d\n", count1);
    else
        printf("Invalid Input\n");

    free(binary);

    return 0;
}
