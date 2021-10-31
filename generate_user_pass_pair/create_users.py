from pprintpp import pprint

passwords = """password
123456
123456789
12345678
1234567
password1
12345
1234567890
1234
qwerty123
qwertyuiop
1q2w3e4r
1qaz2wsx
superman
iloveyou
qwerty1
qwerty
123456a
letmein
michael
monkey
football"""

users = """5. averagestudent

6. BadKarma

7. google_was_my_idea

8. cute.as.ducks

Related: 101 Funny Group Chat Names

9. casanova

10. real_name_hidden

11. HairyPoppins

12. fedora_the_explorer 

13. OP_rah

14. YellowSnowman

15. Joe Not Exotic

16. username_copied

17. whos_ur_buddha

18. unfinished_sentenc

19. AllGoodNamesRGone

20. Something

21. me_for_president

22. tinfoilhat

23. oprahwindfury

24. anonymouse

25. Definitely_not_an_athlete
"""

passwords = passwords.split('\n')
print(len(passwords))

# usernames = [user.split(' ')[1] for user in users if user != '']
usernames = [user.split(' ')[1] for user in users.split('\n') if user != '']
pprint(len(usernames))

user_pass = [(usernames[i], passwords[i]) for i in range(len(passwords))]
pprint(user_pass)


import csv


headers = ('Username', 'Password')

with open('../user_pass.txt', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(user_pass)
