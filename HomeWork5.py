my_list = ['apple', 'peach', 'banana', 'melon', 'grape']
print(my_list)
print(my_list[0], my_list[-1])
print(my_list[0:5:4]) #невозможно использовать без знания кол-во элементов в списке, вывод списком. Занимает больше места или времени?
print(my_list[2:5])
my_list[2] = 'kiwi'
print(my_list)

my_dict = {'kiwi': 'киви', 'orange': 'апельсин', 'melon': 'дыня', 'grape': 'виноград', 'peach': 'персик'}
print(my_dict)
print(my_dict.get('grape'))
my_dict['pineapple'] = 'ананас'
my_dict.update({'blueberry': 'черника'})
print(my_dict)
my_dict['blueberry'] = 'голубика'
print(my_dict)