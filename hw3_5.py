
#__1________________________________________________

# #path = '/home/il/v_uglu_scr/3-5'

# file = open('./3-5.txt','r').readlines()
# file_1 = open('./3-5-1.txt','r').readlines()
# file_r = open('./file_r.txt','a')

# for i in file:	
# 	if i not in file_1:
# 		file_r.write(i)

# for j in file_1:	
# 	if j not in file:
# 		file_r.write(j)

# # file.close()          - пишет ошибку, почему?  без закрытия работает
# # file_1.close()		  - пишет ошибку, почему?  без закрытия работает
# # file_r.close()        - пишет ошибку, почему?  без закрытия работает

# print(file_r)		



#__2____________________________________________________


# file = './3-5.txt'

# def count_lines(file):
# 	f = open(file, 'r')
# 	a = len(f.readlines())
# 	f.close()
# 	l = {'count_lines' : a}
# 	#print(l)
# 	return l


		
# def count_characters(file):
# 	f = open(file, 'r')
# 	b = len(f.read())
# 	f.close()
# 	c = {'count_characters' : b}
# 	#print(c)
# 	return c



# def letters(file):
# 	f = open(file, 'r')

# 	consonants = set('бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ')
# 	vowels = set('аеёиоуыэюяАЕЁИОУЫЭЮЯ')
# 	signs = set('ъь')
# 	numbers = set('0123456789')

# 	count_consonants = 0
# 	count_vowels = 0
# 	count_signs = 0
# 	count_numbers = 0
# 	l_type = dict()

# 	for l in f.read():
# 		if l in consonants:
# 			count_consonants += 1
# 			l_type['count_consonants'] = count_consonants
# 		elif l in vowels:
# 			count_vowels += 1
# 			l_type['count_vowels'] = count_vowels
# 		elif l in signs:
# 			count_signs += 1
# 			l_type['count_signs'] = count_signs
# 		else:
# 			count_numbers += 1
# 			l_type['count_numbers'] = count_numbers

# 	f.close()

# 	#print(l_type)
# 	return l_type



# x = count_lines(file)
# y = count_characters(file)
# z = letters(file)

# x.update(y)
# x.update(z)
# #print(x)

# file_s = open('./file_s.txt','a').write(str(x))





#__3__________________________________________________________



# file = open('./3-5.txt','r').readlines()

# a = len(file)
# #print(a)
# b = 0
# new_list = []
# for l in file:
# 	if b < (a - 1):           
# 		new_list.append(l)
# 		b +=1
# n_l = ''.join(str(e) for e in new_list)
# #print(n_l)
# file_wo = open('./file_wo.txt','a').write(n_l)



#___4___________________________________________________________


# with open('./3-5.txt') as file:
#  	print(len(max(file, key = len)))
 	
 	
#___5_____________________________________________________________ 	
#зделаю позже