def zipMaker(list1,list2):
  return zip(list1,list2)

test1 = [1,2,3]
test2 = ['Applicant1', 'Applicant2', 'Applicant3']

zipped = zipMaker(test1,test2)

for item in zipped:
  print(item)

#prints=>
#(1, 'Applicant1')
#(2, 'Applicant2')
#(3, 'Applicant3')
