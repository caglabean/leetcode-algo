#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int romanToInt(char *s)
{
    int nums[] = {1, 5, 10, 50, 100, 500, 1000};
    char romans[] = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
    int len = 0;
    char c = s[0];
    while (s[len] != '\0')
    {
        if (s[len] != '\0')
        {
            c = s[len];
        }
        len++;
    }
    int *roman_to_nums = (int *)malloc(len * sizeof(int));

    printf("Length of char array: %d\n", len);
    int first = 0, last = len - 1, result = 0;
    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < 7; j++)
        {
            if (s[i] == romans[j])
            {
                roman_to_nums[i] = nums[j];
                printf("%d. index: %c -> %d\n ", i, s[i], roman_to_nums[i]);
            }
        }
    }

    while (first <= last)
    {
        if (roman_to_nums[first] < roman_to_nums[first + 1])
        {
            result += roman_to_nums[first + 1] - roman_to_nums[first];
            first += 2;
        }
        else if (roman_to_nums[first] == roman_to_nums[first + 1])
        {
            result += roman_to_nums[first + 1] + roman_to_nums[first];
            first += 2;
        }
        else
        {
            result += roman_to_nums[first];
            first++;
        }
    }
    free(roman_to_nums);
    return result;
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

    return 0;
}