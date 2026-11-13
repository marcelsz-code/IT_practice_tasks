#SURVEY Are you interested in computer science? (y/n): y
#Do you like playing computer games? (y/n): n
#Do you have an Instagram account? (y/n): y

#SURVEY RESULTS Interested in computer science: Yes
#Playing computer games: No
#Has an Instagram account: Yes

CS = input('SURVEY Are you interested in computer science? (y/n)')
CG = input('Are you interested in computer games? (y/n)')
instagram = input('Do you have an Instagram account? (y/n)')

if CS == 'y':
    print('SURVEY RESULTS Interested in computer science: Yes')
else:
    print('SURVEY RESULTS Interested in computer science: No')
if CG == 'y':
    print('Playing computer games: Yes')
else:
        print('Playing computer games: No')
if instagram == 'y':
    print('Has an Instagram account: Yes')
else:
        print('Has an Instagram account: No')
