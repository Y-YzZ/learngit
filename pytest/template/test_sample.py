# content of test_sample.py
import pytest

def func(x):
    return x + 1


def test_answer():
    assert func(4) == 5

if __name__ == "__main__":
    # pytest.main('-q test_sample.py')
    # 求和最趋近于10的几个值
    '''
	一堆数值求和，组合列表，求和
    '''
    a = [1, 5, 6, 3, 4, 7]
    wanted = 10
    wanted_list = []
    print(sum(a))
    tmp_list = [0]
    for item in a:
    	tmp_list.append(item)
    	sum_wanted = sum(wanted_list)
    	sum_tmp = sum(tmp_list)
    	if sum_tmp == wanted:
    		wanted_list = tmp_list
    		break
    	elif sum_tmp > wanted:
    		if sum_wanted == 0:
    			wanted_list = tmp_list
    		elif sum_wanted < sum_tmp:
    			tmp_list.pop(1)
    		else:
    			wanted_list = tmp_list
    	else:
    		continue
    	print(tmp_list, wanted_list)
