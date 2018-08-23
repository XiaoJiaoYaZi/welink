
cdef extern from "persion.cpp":
    pass

cdef extern from "persion.h":
    struct person_info_t:
        int age
        char *gender
    ctypedef person_info_t person_info

    void print_person_info(char *name, person_info *info)