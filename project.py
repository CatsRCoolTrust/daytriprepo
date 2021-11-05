import random
destinations = ['California', 'Philippines', 'Washington', 'Chicago', 'Milwaukee']
restaurants = ["Chili's", "Red Robbin's", 'IHop']
transportations = ['By Foot', 'By Plane', 'By Vehicle', 'By Train']
entertainments = ['Movies', 'Sightseeing', 'Parks']

def gen_option(some_list):
    list_index = random.randint(0, len(some_list)-1)
    return some_list[list_index]


chosen_dest = gen_option(destinations)
chosen_place_to_eat = gen_option(restaurants)
way_of_transportation = gen_option(transportations)
way_of_fun = gen_option(entertainments)
print(f'\n{chosen_dest}\n{chosen_place_to_eat}\n{way_of_transportation}\n{way_of_fun}\n')

ask = (input("Do you like these choices listed? "))
again = True
while again == True:
    if ask == 'Yes':
        print(f'Your selection process is now complete. ')
        break
    elif ask == 'No':
        print('We shall pick a new agenda for you! ')

        chosen_dest = gen_option(destinations)
        chosen_place_to_eat = gen_option(restaurants)
        way_of_transportation = gen_option(transportations)
        way_of_fun = gen_option(entertainments)
        print(f'\n{chosen_dest}\n{chosen_place_to_eat}\n{way_of_transportation}\n{way_of_fun}\n')
        
    question = input('Do you like your new options? ')
        
    if question == 'Yes':
            print(f"Your final choices: \n\n     {chosen_dest}\n     {chosen_place_to_eat}\n     {way_of_transportation}\n     {way_of_fun}\n")
            print('Have a wonderful day!')
            break
    else:
        again = True
                




    