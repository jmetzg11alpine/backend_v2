from deta import Deta

deta = Deta('a0499p4s_aP4D8LBstFNj8tujRmuz6vGdVMYfBRB5')

users = deta.Base('users')
q1 = deta.Base('q1')
q2 = deta.Base('q2')
q3 = deta.Base('q3')
q4 = deta.Base('q4')

users.insert({'name': 'one', 'password': 'one'})
q1.insert({'name':'two', 'score': 10})
q2.insert({'name': 'three', 'score': 9})
q3.insert({'name': 'four', 'score': 8})
q4.insert({'name': 'five', 'score': 7})