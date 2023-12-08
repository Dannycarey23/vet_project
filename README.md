# CodeClan Solo Python Project

This is the first project that I built while studying at CodeClan. The project was built in just under one week. 
Tech Stack: HTML5, CSS3, Python3, Flask, PostgreSQL

## Vet Management App

A veterinary practice has approached you to build a web application to help them manage their animals and vets. A vet may look after many animals at a time. An animal is registered with only one vet.

## MVP

- The practice wants to be able to register / track animals. Important information for the vets to know is -
  - Name
  - Date Of Birth (use a VARCHAR initially)
  - Type of animal
  - Contact details for the owner
  - Treatment notes
- Be able to assign animals to vets
- CRUD actions for vets / animals - remember the user - what would they want to see on each View? What Views should there be?

## Possible Extensions

- Mark owners as being registered/unregistered with the Vet. unregistered owners won't be able to add any more animals.
- If an owner has multiple animals we don't want to keep updating contact details separately for each pet. Extend your application to reflect that an owner can have many pets and to more sensibly keep track of owners' details (avoiding repetition / inconsistencies)
- Handle check-in / check-out dates
- Let the practice see all animals currently in the practice (today's date is between the check-in and check-out?)
- Sometimes an owner does not know the DOB. Allow them to enter an age instead. Try and make sure this always up to date - ie if they visit again a year from now a 3 yr old dog is now 4.
- Add extra functionality of your choosing - assigning treatments, a more comprehensive way of maintaining treatment notes over time. Appointments. Pricing / billing.

## INSTALLATION GUIDE (mac)
- Download and install Postgresql: https://www.postgresql.org/
- Terminal commands: "pip3 install flask", "pip3 install python-dotenv" & "pip3 install psycopg2"
- Clone the repo.
- In terminal, cd into the project directory "../vet_project"
- Connect the db; In terminal type "psql -d hutchVets -f db/hutchVets.sql"
- Run the console file; In the terminal type "python3 console.py"
- Initiate flask; In the console type "flask run"


### Attributions
- "Radagast" image from: <a href="https://www.freepik.com/free-ai-image/portrait-wizard-medieval-times_81397576.htm#query=crazy%20wizard&position=13&from_view=search&track=ais&uuid=4a5e486d-affd-4808-abe1-3fb74b4aead3">Image By freepik</a>
- "Steve Irwin" image - Photo by cottonbro studio: https://www.pexels.com/photo/man-in-white-and-red-plaid-dress-shirt-wearing-black-and-white-cap-4918105/
- "Herschell" image Photo by <a href="https://www.shopify.com/stock-photos/@matthew_henry?utm_campaign=photo_credit&amp;utm_content=High+Res+Bearded+Man+Portrait+Picture+%E2%80%94+Free+Images&amp;utm_medium=referral&amp;utm_source=credit">Matthew Henry</a> from <a href="https://www.shopify.com/stock-photos/senior?utm_campaign=photo_credit&amp;utm_content=High+Res+Bearded+Man+Portrait+Picture+%E2%80%94+Free+Images&amp;utm_medium=referral&amp;utm_source=credit">Burst</a>
- The image in the main banner - Photo by Tima Miroshnichenko: https://www.pexels.com/photo/a-vet-checking-a-sick-rough-collie-6235231/
- Dolly, Denver, Holly & Layla images are my own. 
