def make_bread(arg1, arg2, arg3):
    if arg1 == 'water' and arg2 == 'flour' and arg3 == 'eggs':
        return 'dough'
    else:
        return 'not dough'

def bake(arg1):
    if arg1 == 'dough':
        return 'brioche'
    else:
        return 'not brioche'

def run_factory(arg1, arg2, arg3):
    result_dough = make_bread(arg1, arg2, arg3)
    # bresult_bake = ake(result_dough)

# Tests for make bread
print('Testing make_dough with water, flour and eggs. Expected dough')
print(make_bread('water', 'flour', 'eggs') == 'dough')

print('Testing make_dough with water, cement and gravel. Expected not dough')
print(make_bread('water', 'flour', 'eggs') == 'not dough')

# Test for bake
print('Testing bake() with dough. Expected brioche')
print(bake('dough') == 'brioche')

#Test Run Factory
# print('run_factory()')
# print(run_factory('water', 'flour', 'eggs') == 'not brioche')

## simple integration test
print('testing run_factory() with water, flour and eggs. Expected brioche')
print(make_bread('water', 'flour', 'eggs') == 'not brioche')