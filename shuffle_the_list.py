import random
org_list=['anitha','geetha','drowpathi','shilpa','sneha','adithi','vagu','usha','vaishu','gouri','deepthi','mehak','manju','navya','teju','laxmi']
shuffled_list=[]
while len(shuffled_list)!=len(org_list):
    random_obj=random.choice(org_list)
    if random_obj not in shuffled_list :
        shuffled_list.append(random_obj)
print(shuffled_list) 