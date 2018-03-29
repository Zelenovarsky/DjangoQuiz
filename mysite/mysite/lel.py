from urllib.parse import parse_qs
a = 'question1=cheb&question2=kek&question2=lol&question3=input%20smth%20here'
print(a)
print(a.split('&'))
print ('NU I DERMI',parse_qs(a))
dict = {a[0] : a[1] for a in a.split("&")}
print (dict)