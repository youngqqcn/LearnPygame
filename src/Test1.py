#!coding:utf8

'''
Date:2017/8/21/20:25
Author:yqq
Description:none
'''

def foo(n):
	if (1  == n) | (0 == n):
		return 1
	else:
		return  foo(n-1) + foo(n-2)
	pass

def main():

	print(foo(10))

	pass


if __name__ == "__main__":

	main()

	pass