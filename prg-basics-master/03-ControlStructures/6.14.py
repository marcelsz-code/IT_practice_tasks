answer1 = input("Do you have a facebook account?Y/N: ")
if answer1 == 'Y':
    facebook = True
else:
    facebook = False
print(f'facebook = {facebook}')
answer2 = input("Do you have a twitter account?Y/N: ")
if answer2 == 'Y':
    twitter = True
else:
    twitter = False
print(f'twitter = {twitter}')
answer3 = input("Do you have a instagram account?Y/N: ")
if answer3 == 'Y':
    instagram = True
else:
    instagram = False
print(f'instagram = {instagram}')
if facebook == True and instagram == True:
    print("You're a good influencer")
elif facebook == True and twitter == True:
    print("You're a good influencer")
elif twitter == True and instagram == True:
    print("You're a good influencer")

