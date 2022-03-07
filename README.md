# scsuwork
A listing of my projects created while enrolled at SCSU Information Security Program

I held off for several years posting my class work on my public github for concern of students cheating off me. I believe many of the professors for some of the harder classes (crypto for example) have retired or are no longer teaching at SCSU MN. I believe its safe to upload my projects from my class. I expect any good student with ok googlefu to find this document.


--- STUDENTS ARE NOT ALLLOWED TO USE MY WORK IN A CLASS. ---
If you are professor of a class at SCSU MN please note that if you find work that looks a lot like mine its a good idea to confront the student.


Crypto Class CNA 438
- The zip file is what was submitted to the instructor for each assignment.
- Many other files exist that show small code to test or implement smaller parts of the problems/program. For example, CRT (Chinese Remainder Theorem).
- Assignments had a week to be completed with the requirements. Therefor, they might not be great looking or look unprofessional. The goal was to get something working that would get a grade, not create a project that would be running on someones system for a lifetime.
- Some Assignments do not have zip files, the assignemnt was stil sent, however, with a file from the folder. The files might exist on my flash drive I used as my main storage from college. (Please to ask me to upload them)
- AND FINALLY: DON'T USE THESE IN PLACE OF REAL ENCRYPTION LIBRARIES. THIS CODE IS NOT FULLY TESTED AND MEANT AS A TOY. IT MOST SURELY HAS BUGS THAT IMPACT ENCRYPTION. MANY OF THESE METHODS USED ARE NOT SECURE AND ARE OUTDATED.

Dear Students of CNA 438:

If you are trying to complete a programming assignment for this class, I highly recommend you head to the library basement at SCSU. Its very clear from reading these books that the professors at SCSU used these books to construct the class work. I found many books that looked like the course work 1 for 1. So it is worth your time to get to know a few shelves in the basement of the library. (I think Row S, T, R where some of the best rows.) Ask the librarian for help.

A great book is the Handbook of Applied Cryptography Book by Alfred Menezes, Paul van Oorschot, and Scott Vanstone

This huge book has everything you could want for this class. It even has sudo code which can be used to implement your programming into your favorate language.

My second recommendation is a book by CRC Press entitled Algorithmic Cryptanalysis by Antoine Joux.

This is a must read for this class. It has all the good stuff explaned in a way you can understand. I highly recommend this book if you want to learn how to implement popular cryptos.

If you are still confused as a student I would recommend looking at books in the subject of linear algebra.
It is used hevaly in this subject. If you haven't already taken this class it should be done before you sign up for this 400 level course. It makes understanding the basics of matrix work much easier.

You could also review the topic of Descrete Math more. The CRT and co-prime (AKA relative prime numbers) is a major topic in asymmetrical encryption.

CNA 431-432 OSI Model and other subjects

When I took this class we had some side project of Risk Assement that had to be completed on short notice. The focused on evaulating risk. We were given a senario and had to compute the EF, SLE, ARO, and ALE for a set of servers.

CSCI 220

In this class we learned how computers work by boolean math and impliemented that into real wires and descrete ICs. This class is known for having frustrating lab that doesn't work. I can't share my work from this class because this class is still running in the same form and hasn't change much over the years. To share my work would only allow students to cheat of my work. We made decrete adders and a 7 segment driver as projects. The class focused mostly on boolan logic and its applications in computer sci.

What I learned is key (take note future students):

Use a software program to simplify your logic. Use another program to draw your layout on your breadboard. I found a program (name excapes me at this point) that allows for a perfect 1 to 1 printout of the breadboard curcit. This allows you to play LiteBright with your breadboard. You know it will work when you have all the parts connected. Buy your own jumper wires with male pins to make this possible. The community lab provided pins and chips are going to fail on you. If you have another 100$ spend it on your own set of ICs and jumper wires. This will save you a lot of time and get you and your co-lab partern out of hte lab in 20 mins. The lab room isn't very comfy and is very stuffy with 30 students in a small room.


CNA 425

- A several labs with software from Riverbed Opnet.
- A Group project to Evaulate how XSS atacks work (Using SEED LAB)

CNA 426

Covered networking algos and other related topics. I learned how to compute checksums and how the IP protocol works. We did routing of packets by hand on paper to understand how  switches work.

- Group Project was on how Dijkstra's algo works. What I have from that project are listed in this repo (not complete)

CNA 397

This was an interesting class. It had a lot of different topics. Computer history, command line scripts, programming in ASM, and more. My most notiable acheivement from this class was having a ASM program compile and work correctly on the first try. I thought I made a mistake. It doesn't happen like that.

- See lab 8, 9, 10, 11, ASM programming in x32.
- Lab 12 is an intro to bash scripting.
- Wrote a term paper on Linux and its different parts. (File is not found at this time)


CNA 465

This class focused on wireless communication.

Projects include:

- Created a radio antenna and attempted to communicate with Ham radio sats.
- Follwed CISCO Campus Lan and Wireless Design Guide to create a plan network design for a hypothetical hospital.
- Attempted to frag attack on my old wifi raouter to break the encryption.
- Wrote a paper on a wireless Sybil Attacks (51% attacks) [project 6]

CNA 436

This class was focused on web dev. I do not have the files from this class for my major project. I quickly removed them from the schools server after delivering the project (for reasons I will explain later). The professor of this class had projects along side the other assigned work that included work with SQL databases. The first one was Access databases. We had to create a database from scrach that could work as a hospital building system. Later, we took the same model and had to create a database that would work with a website. Most of the day to day assignemtns and tests were focused on front end web dev activities. The backend work was the side project.

Front-end projects included:
- CSS and HTML
- Following best practices for accessibility
- Troubleshooting issues with front-end development.

I did complete and deploy a simple billing system with a working backend that could generate simple billing reports. This back end took me about 2 weekends to create while taking a full load of classes and doing the projects from all of them at the same time. The backend was a wrote in a LAMP stack. Since this project was a rush as students tend to be, I posted it for the teacher and quickly removed it. It had many issues around webpage security that I didn't have time to work out before the due date. I didn't want to put the college's webserver it was running at risk of an attack. The overall topic of this class was design of websites and administrating databases. I didn't need to explain why my code was used to take over a server. Even if there existed controls I didn't know about that would have blocked issues I didn't want to find out the hard way. I don't believe I have this code at this time for this repo.

Takeways from backend database project:
- Takes more time than one might expect to create a solid database backend.
- Security has to be part of the design upfront (this is why I took it down as soon as it was graded; security creating a backend wasn't a requirement for this project)
- Learned how to administrate MySQL database from the command line
- Created complex joins to match data from more than one table to other tables to get the information out of the database as requsted by the reports.
- Sourced my own dummy information to test the database.


CNA 473 - Final Project

For my final project of this class I anwswered a question left by two master students lexander Orosz Edward and Hunter Young of Kennesaw State University in “Ultrasonic Data Transmission and Steganography" "On the complete opposite end of the spectrum exists the concept of infrasound, or sounds so low that humans are unable to hear them. These sounds are essentially nothing but vibrations that can be felt rather than heard, and they exist below 20 Hz. Since low frequencies propagate so well through solid objects, special bass transducers could potentially be used to exfiltrate data from a building using the same modulation techniques applied in this project to ultrasonic signals.” (Young)"



I investigated this question using a subwoofer and a microphone. A short class presentation was given about the findings. Yes, it is possible, however, the datarate is related to the freq of the waves used, so the bit rate is so slow its not likely to be used for anything other than a covert command and control channel. Bit rates are as low as 1 byte per second. Since the time of writing this paper, other covert channels have been investaged and provent to exist. Blinking lights on a computer, the speakers on a computer can be turned into mircophones, and using a laser targeting mics (https://lightcommands.com/). 
