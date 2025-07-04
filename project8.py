"""
Project building concedpt
1. What is project
2. How I can do
3. concept Writing & why these concept are used in this project
4. psudo code writing

"""
#  fake Funny Headline Generator for sport , politics & acters.
import random

sport_subjects = [
    'Imran Khan',
    'Babar azam',
    'Bhoom Bhoom Afridi',
    'Hasan Ali',
    'Sultan of Swing(Wasim akram)',
    'The Rawalpindi Express(Shoaib akhter)',
    'Khauf Express(Haris rauf)',
    'The Eagle(shahine)',
    'The Maestro(Miandad)',
    'saifi'
]

sport_action =[
    'is the leader Since 1749',
    'is the CEO of Elegant Shots Pvt. Ltd',
    'is the Official Supplier of Free Balls to the Crowd',
    'is the Professor of Curve and Confusion',
    'is the Train That Doesn’t Stop at Wickets',
    'is the Fright Delivery Services (FDS)',
    'is the Air Strike Commander of First Overs',
    'is the Master of Mind Games and Mince Runs',
    'is the Captain Commentary Machine 24/7',
    'is the funny acter of cricket world'
]


sport_Places_things = [
    'at robotic world',
    'at khuar river',
    'at Raiwind',
    'at Adiala Jail',
    'at Garbaje city',
    'at renewable energy sources',
    'inside the hub dame',
    'at pakistan door',
    'at General headquarter',
    'at army chief house'
]

political_subjects = [
    'Mian Vote Sharif',
    'Papa Diesel (Maulana Fazl)',
    'Sir Container Khan',
    'Bilawal English Bhutto',
    'Captain Selfie (Murad Saeed)',
    'The Silent Speaker (Asad Qaiser)',
    'Tind Master (Shehbaz Sharif)',
    'Mr. Neutral (General Banda)',
    'King of Statements (Rana Sana)',
    'Drama Minister (Fawad Chaudhry)'
]

political_actions = [
    'is the Inventor of U-Turn Engineering',
    'is the Ambassador of Free WiFi in Jungles',
    'is the CEO of Political Yoga Moves',
    'is the Certified Speech Repeater Level 99',
    'is the Master of Mic-Snatching Techniques',
    'is the President of Self-Clapping Association',
    'is the Voted Most Likely to Blame the Weather',
    'is the TikTok Policy Analyst',
    'is the Advisor to NASA on Rickshaw Engines',
    'is the Host of “Politics with Popcorn” Podcast'
]

political_places_things = [
    'from Secret Biryani Bunker',
    'live at Container Planet HQ',
    'inside the Parliament Playland',
    'from Under the Metro Bus',
    'directly reporting from Twitter Jail',
    'spotted in the Committee Room Cafeteria',
    'at the VIP Queue of NADRA',
    'hiding behind the Economy Graph',
    'broadcasting from “Lifafa Lounge”',
    'lost in the Circular Debt Jungle'
]

actors_subjects = [
    'Drama King (Fahad Mustafa)',
    'The Slap Specialist (Humayun Saeed)',
    'Mr. Overacting (Feroze Khan)',
    'Queen of Tears (Ayeza Khan)',
    'Sir Slow Motion (Imran Abbas)',
    'Madam Expressionless (Hania Aamir)',
    'The Whispering Legend (Fawad Khan)',
    'Voice Cracker (Yasir Hussain)',
    'Captain Cry Cry (Iqra Aziz)',
    'Action Hero in Shaadi Scenes (Adnan Siddiqui)'
]

actors_actions = [
    'is the Ambassador of Slow Claps',
    'is the Inventor of 5-Minute Flashbacks',
    'is the President of Suspense Staring League',
    'is the Winner of “Cried Without Reason” Award',
    'is the National Supplier of Background Music Looks',
    'is the Certified Mirror-Staring Expert',
    'is the Holder of Longest Dramatic Pause Record',
    'is the Director of Self-Falling Scenes',
    'is the Invented Crying While Drinking Water Technique',
    'is the Professor of Overzoom Reactions'
]

actors_places_things = [
    'in the Land of Flashbacks',
    'from the Set of 999th Episode',
    'inside the Slow-Mo Department',
    'at the Crying Academy of Arts',
    'from the Overacting Olympics',
    'inside the Background Music Studio',
    'at the 3rd Wedding Scene of the Day',
    'reporting live from Drama Triangle HQ',
    'hidden in the Make-Up Room Fog',
    'at the Mansion of Repeated Dialogues'
]


while True:
    headline_for_any = input("chose any of these sport , politics & actors for fake and funny headline generating: ").strip().lower()
    if(headline_for_any == "sport"):
       SPot_subject = random.choice(sport_subjects)
       SPOT_actions = random.choice(sport_action)
       SPOT_Place_thing = random.choice(sport_Places_things)
       headline = f'\n fake and funny headline for sport: {SPot_subject} {SPOT_actions} {SPOT_Place_thing}'
       print(headline)
    elif(headline_for_any == "politics"):
       P_subject = random.choice(political_subjects)
       P_actions = random.choice(political_actions)
       P_Place_thing = random.choice(political_places_things)
       headline = f'\n fake and funny headline for politics: {P_subject} {P_actions} {P_Place_thing}'
       print(headline)
    else:
       A_subject = random.choice(actors_subjects)
       A_actions = random.choice(actors_actions)
       A_Place_thing = random.choice(actors_places_things)
       headline = f'\n fake and funny headline for acters: {A_subject} {A_actions} {A_Place_thing}'
       print(headline)

    saved_not = input("if you want to save these funny &fake headline in your file.(saved or not)").strip().lower()
    if saved_not == "saved":
         with  open("project8_1.txt" , "a") as file:
             content = file.write("\n" + headline)
             print(content)  

    user_input = input("\n Do you want another headline (yes/No)").strip().lower()
    if user_input == "no" :
         break         

print("\n Thanks for using fake funny Headline generator, Have a fun day. ")      