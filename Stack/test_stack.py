import stak

st = stak.Stack()
st.push("bob")
assert st.length == 1, 'first element was the pushed in'



st.push("tam")
st.push("gil")
st.push("rick")
st.push("alex")
assert st.length ==5 ," push method did dont add 5 elements, it instead pushed {0}".format(st.length)

alex  = st.pop()
assert alex == "alex", "pop is not popping correct element, its instead returning {0}".format(alex)
assert st.length == 4 , "stack length incorrect , it is intead {0}".format(st.length)

assert st.peek() == "rick","peek is not correct, it instead returned {0}".format(st.peek())
print("stack ran successfully")