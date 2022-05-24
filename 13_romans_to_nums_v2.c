#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int romanToInt(char *s)
{
    int num = 0;
    int ascii_to_int[89];  // decimal eq. of X=88
    ascii_to_int['I'] = 1; // ascii_to_int[73]
    ascii_to_int['V'] = 5;
    ascii_to_int['X'] = 10;
    ascii_to_int['L'] = 50;
    ascii_to_int['C'] = 100;
    ascii_to_int['D'] = 500;
    ascii_to_int['M'] = 1000;
    ascii_to_int['\0'] = 0;

    for (int i = 0; s[i] != '\0'; i++)
    {
        if (ascii_to_int[s[i]] < ascii_to_int[s[i + 1]])
        {
            num += ascii_to_int[s[i + 1]] - ascii_to_int[s[i]];
            i++;
        }
        else
        {
            num += ascii_to_int[s[i]];
        }
    }
    return num;
}

int main()
{
    char arr[] = "LVIII";
    printf("Input: %s\n", arr);
    printf("Output: %d\n", romanToInt(arr));

    strcpy(arr, "MCMXCIV");

    printf("Input: %s\n", arr);
    printf("Output: %d\n", romanToInt(arr));

    strcpy(arr, "III");

    printf("Input: %s\n", arr);
    printf("Output: %d\n", romanToInt(arr));
}