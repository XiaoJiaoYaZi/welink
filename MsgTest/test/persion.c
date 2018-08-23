#include <stdio.h>
#include "persion.h"

void print_person_info(char *name, person_info *info)
{
    printf("name: %s, age: %d, gender: %s\n",
            name, info->age, info->gender);
}
