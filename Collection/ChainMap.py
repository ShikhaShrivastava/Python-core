'''__________________Chainmap______________________'''
print()
print("ChainMap")
from collections import ChainMap
def connecting_multi_dict():
    stud={'id':'12hnjde','name':'amar','college':'ssec'}
    marks={'sub1':56,'sub2':78,'sub3':69,'sub4':92,'sub5':64}
    Student=ChainMap(stud,marks)
    print(stud)
    print(marks)
    print(Student)
    print(type(Student))
    print(list(Student.keys()))
    print(list(Student.values()))
    print(Student['id'])
    print(Student['name'])
    print(Student['college'])
    Student['name']='Shikha'
    print(Student)
    marks['sub2']=99
    print(Student)
    lst=Student.maps
    print(lst)
    result={}
    total=0
    for marks in marks.values():
        total+=marks
    percentage=total/500*100
    result['total']=total
    result['percentage']=percentage
    update_student=Student.new_child(result)
    print(update_student)
    print()
    print(update_student.parents)

def main():
    connecting_multi_dict()

if __name__=="__main__":
    main()
