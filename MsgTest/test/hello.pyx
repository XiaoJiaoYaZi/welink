
cdef extern from "persion.h":
    struct person_info_t:
        int age
        char *gender
    ctypedef person_info_t person_info

    void print_person_info(char *name, person_info *info)

def cyprint_person_info(name, info):
    cdef person_info pinfo
    pinfo.age = info.age
    pinfo.gender = info.gender
    print_person_info(name, &pinfo)

