# string comparison is made using '==' for equals and '!=' not equals, both returns True or False
# note: python is case sensitive
jon = 'jon'
ygritte = 'ygritte'
print(jon, '==', ygritte, jon == jon)
print(jon, '==', 'Jon', jon == 'Jon')
print(jon, '==', ygritte, jon == ygritte)
print(jon, '=!', ygritte, jon != ygritte)
