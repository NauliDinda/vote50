# WELCOME TO VOTE 50
# 1. Application Description

As school teachers, we frequently face an election situation such as determin a class leader, chairman of student council or just a leader of class activity small group. During the election, deciding how to process the election in choosing the best candidate sometimes could be challenging, would take more time and it's very consumable to student's or school attention. Consider such a situation, we develop a voting system based on web that hopefully can easily be used by anyone with different purposes.
Here, we set the program with and without candidate profile to meet the user's needs.
If the election has more than three candidates, the Vote 50 is the best solution for time saving.

Link to the video: https://youtu.be/kyvYevfsqpA?si=Ql3naQlcTd_W25Nm

Aim of the project:
1. Help user to set a voting system with different purposes and needs.
2. Reducing time consuming during the vote input, vote counting, and showing result.
3. The result and the voting process are easily watched by the community with a real time result.

Creators of the project are 3 effective teachers with various background form Indonesia :
1. I Kadek Mariassa
2. Reva Rensila Iasha
3. Dinda Nauli Nasution

# 2. Softwares/Modules/Libraries

To use `Vote 50?`, you need to have the following softwares installed in your local computer.

 1. Python 3.11 https://www.python.org/downloads/
 2. PIP https://pip.pypa.io/en/stable/
 3. CS50 Library for Python https://cs50.readthedocs.io/libraries/cs50/python/.
 4. Flask-Session https://flask-session.readthedocs.io/en/latest/
 5. Git https://git-scm.com/doc

## 2.1 Install Python
Refer to this article to install and configure Python: https://realpython.com/installing-python/

## 2.2 Install PIP
Refer to this documentation to install PIP:
https://pip.pypa.io/en/stable/installation/

## 2.3 Install CS50 for Python
Use the following command in your terminal to install CS50 for Python:

    $  pip3 install cs50
The command will also install all other modules used in this project.

## 2.4 Install Flask-Session

Use the following command in your terminal to install Flask-Session:

    $  pip3 install Flask-Session
## 2.5 Install and Configure Git
Refer to this documentation to install and configure Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

# 3. Clone and Launch The Application

 1. Navigate to the project repository using the following link:
https://github.com/code50/148388805/tree/main/project
2. Open terminal window, and change directory to your own choice
3. Use the following command to clone the project:

    `$  git clone https://github.com/code50/148388805/tree/main/project.git`

    Make sure the clone process is finished before proceeding to the next step.

  4. Change directory to the application directory.

		  $  cd project
4. Launch the application

	    $  flask run
	The application run on http://127.0.0.1:5000/ by default. The following landing page should appear:

	![Application landing page](https://markdown-here.com/images/pagehome.png)

# 4. Using The Application

## 4.1 As Administrator
To operate the program, Firstly, register for an Administrator account with:
username : admin
password: admin
Complete the registration process, and log in as administrator.
Once an admin is registered, Administrator needs to register the voters account by providing username, password and email. The character of email should use '@', for example;
username: user1
password: user1
email: use1@user

The following landing page of administrator should appear:

![Admin Dashboard](/images/admin_home.png)

## The Administrator can do the following:

 1. Add, view, edit, or delete voter
 2. Add, view, edit, or delete candidates
 3. View the voter status report ('has voted' or has not voted')
 4. Show the voting result
---

These actions help the administrator to control the voting and the counting vote process.

The following landing page when the administrator edit or delete candidate:

![Register Candidate](https://https://github.com/code50/148388805/tree/main/project/images/reg_edit_candidate.png)

To add candidate, the administrator needs to prepare some data which are; name of candidate, name of party , manifesto or the candidate's program, the logo of the candidate (use an url of a logo)
the landing page to add candidate should appear like this:

![Add Candidate](https://https://github.com/code50/148388805/tree/main/project/images/add_candidate.png)

The landing page where the administrator register voters;

![Register Voter](https://https://github.com/code50/148388805/tree/main/project/images/reg_user.png)

Once the candidates and the voters are ready, then the voter can be processed.

# 4.2. As The Voter
To vote, a voter needs to register in 'log in' menu. A new voter can only log in after the administrator register the account.
This is to control that only the registered voter can vote a candidate in the voting system.

### the landing page of successful registration of a voter should appear:
---
![User Log in Success](https://github.com/code50/148388805/tree/main/project/images/user_login.png)
---

### After log in, the voter will see the page for candidates in the election.
---
![Vote a Candidate](https://github.com/code50/148388805/tree/main/project/images/vote_candidate.png)
---
As a voter, the voter can only log in, vote, log out and view the result.

### the landing page of voting result should appear:
---
![Vote Result](https://github.com/code50/148388805/tree/main/project/images/vote_result.png)
---

If a voter has voted log in, there will be a message saying that "After we check, you have already voted so there is no need to vote again."
Then, the voted voter can only check the voting result.

# 5. FAQs

 1. **Q: Do I need to register before log in to Vote50?** *A: Yes, It's a must.*
 2. **Q: Do I need to log in to see the voting result?** *A: Yes, the program is a one time run.*
 3. **Q: How to be an administrator?** *A: username = admin, password = admin*
