import binary__search as bs 

b1 = bs.bs([1,2,4,5,7],5)
assert b1 == 3 , 'bs is not working, instead returns {0} '.format(b1)

b1 = bs.bs([1,2,4,5,7],7)
assert b1 == 4 , 'bs is not working, instead returns {0} '.format(b1)

b1 = bs.bs([1,2,4,5,7],2)
assert b1 == 1, 'bs is not working, instead returns {0} '.format(b1)

b1 = bs.bs([1,2,4,5,7],4)
assert b1 == 2 , 'bs is not working, instead returns {0} '.format(b1)

b1 = bs.bs([1,2,4,5,7],1)
assert b1 == 0 , 'bs is not working, instead returns {0} '.format(b1)

b1 = bs.bs([1,2,4,5,7],10)
assert b1 == -4 , 'bs is not working, instead returns {0} '.format(b1)
print("bs done")