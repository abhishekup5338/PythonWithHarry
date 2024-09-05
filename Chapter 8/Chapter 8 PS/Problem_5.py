
#Write a python function to print thr n line of the following pattern:
'''
* * *
 * *
  *
'''

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

print(pattern(6))