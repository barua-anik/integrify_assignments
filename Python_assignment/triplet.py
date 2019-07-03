a = [10, 50, 5, 1]
b = [10, 2, 5, 1, 8, 20]
c = [12, 6]
d = [15, 30, -1, 'v', 5]
e = [4, 3, 1, 2, 6]

def tri_count(l_nums):
   if len(l_nums) < 3:
       return 0
   for i in range(len(l_nums)):
       if not isinstance(l_nums[i], int):
           print(i)
           return 0

   l_nums.sort()

   p = 0
   while p in range(len(l_nums)-2):
       q= p+1
       r= q+1

       if check_triple(l_nums[p], l_nums[q], l_nums[r]):
           return 1
       p+=2
   return 0


def check_triple(p, q, r):

   return (((p+q) > r) and ((q+r) > p) and ((p+r) > q))

#print(tri_count(a))
#print(tri_count(b))
#print(tri_count(c))
#print(tri_count(d))

def find_num(a):
   input_sum = sum(a)
   n = len(a) + 1

   return (n*(n+1)/2 - input_sum)


#print(find_num(e))

def rotate_arr(a, k):

   for i in range(k):
       a = [a[-1]] + a[:-1]
   return a
print(rotate_arr(a, 2))