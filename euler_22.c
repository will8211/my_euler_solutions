/*
Project Euler Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void my_fn(char token[100])
{
    printf("%s", token);
}

int main()
{
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;
    char *str;

    fp = fopen("/home/william/Dropbox/euler/p022_names.txt", "r");

    while ((read = getline(&line, &len, fp)) != -1) {
        printf("%s", line);
        sprintf(str, "%s", line);
    }

    //char *token;

    //while ((token = strsep(&str, ","))) {
    //    my_fn(token);
    //}

    fclose(fp);
}

/*
width open('p022_names.txt') as f:
    for line in f:
        names = line[1:-1].split('","')
names = sorted(names)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_dict = {}
for i in range(len(alphabet)):
    alpha_dict[alphabet[i]] = i+1

total = 0
for i, name in enumerate(names):
    my_sum = 0
    for letter in name:
        my_sum += alpha_dict[letter]
    total += my_sum*(i+1)

print(total)
*/
