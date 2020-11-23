### You know we should have a happy bot as well. Or also a anxious bot, an embarassed bot, and a overwhelmed bot.

import praw
import threading
import time
import joke
from random import randint
from ast import literal_eval

userAgent = 'comfortbot'
cID = 'wZk6Brr5M5oKFA'
cSC= 'unSfyEJnSvbDkIjG2KTYehtZDc4yWA'
userN = 'harry_peng'
userP ='BruhMoment123'
numFound = 0
reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)

subreddit = reddit.subreddit('all') #any subreddit I want to monitor



def sad_action():
  ##if len(comment.split(" ")) <= 7:
    comment.reply("Don't be sad. Here's a hug. \n https://media.giphy.com/media/3M4NpbLCTxBqU/giphy.gif")
    '''
    comment.reply(' "'+comment.body.replace("don't quote me on that",   '')+'" '+'/n----'+comment.author.name)
    '''
  

def bored_action():
  ##if len(comment.split(" ")) <= 7:
    ### I'm bored
    list_of_jokes = joke.return_list()
    random_joke = list_of_jokes[randint(0,len(list_of_jokes)-1)]

    comment.reply("Here's a joke! " + str(random_joke))

def happy_action():
  ##if len(comment.split(" ")) <= 7:
    list_of_happy = ["Hope you have a great day!",":D","You're Awesome!","Nice!","Hope you do well!",":)"]
    comment.reply(list_of_happy[randint(0,len(list_of_happy)-1)])

def anxious_action():
  ##if len(comment.split(" ")) <= 7:
    comment.reply("Don't be anxious! It's no big deal!")

def overwhelmed_action():
  ##if len(comment.split(" ")) <= 7:
    comment.reply("It's alright! You'll do great!")

def happy_face_action():
  comment.reply(":D")

file2read = open("id.txt","r").read()
replied_to = literal_eval(file2read)

sad_keywords = "sad"
bored_keywords = "bored"
happy_keywords = "happy"
anxious_keywords = "anxious"
overwhelmed_keywords ="overwhelmed"
happy_face_keywords = ":)"

def print_stats():
              print('Bot replying to: ') 
              print("comment: ", comment.body)
              print("user: ", comment.author)
              print("score: ", comment.score)
              print("time: "+str(time.time()))
              print("comment id: "+comment.id)

try:
  while True:
    

      for submission in subreddit.hot(limit=300): #this views the top 10 posts in that subbreddit
          submission.comments.replace_more(limit=0)
          for comment in submission.comments:
              
              if bored_keywords in comment.body.lower() and comment.id not in replied_to:       
                  numFound = numFound + 1
                  print('bored')
                  print_stats()
                  bored_action()
                  print('replied!')
                  print("---------------------------------")
                  replied_to.append(comment.id)
                  ##'''
              elif sad_keywords in comment.body.lower() and comment.id not in replied_to:
                  numFound = numFound + 1
                  print('sad')
                  print_stats()
                  sad_action()
                  print('replied!')
                  print("---------------------------------")
                  replied_to.append(comment.id)
              
              elif happy_keywords in comment.body.lower() and comment.id not in replied_to:
                  numFound = numFound + 1
                  print('happy')
                  print_stats()
                  happy_action()
                  print('replied!')
                  print("---------------------------------")
                  replied_to.append(comment.id)

              elif anxious_keywords in comment.body.lower() and comment.id not in replied_to:
                  numFound = numFound + 1
                  print('anxious')
                  print_stats()
                  anxious_action()
                  print('replied!')
                  print("---------------------------------")
                  replied_to.append(comment.id)

              elif overwhelmed_keywords in comment.body.lower() and comment.id not in replied_to:
                  numFound = numFound + 1
                  print('overwhelmed')
                  print_stats()
                  overwhelmed_action()
                  print('replied!')
                  print("---------------------------------")
                  replied_to.append(comment.id)

              elif happy_face_keywords in comment.body.lower() and comment.id not in replied_to:
                  numFound = numFound + 1
                  print('happy_face')
                  print_stats()
                  happy_face_action()
                  print('replied!')
                  print("---------------------------------")
                  replied_to.append(comment.id)

              with open("id.txt","w") as file:
                file.write(str(replied_to))

    ##'''
      if numFound == 0:
          print()
          print("no posts with keyword")
          print()
      numFound = 0
      time.sleep(20)
except Exception:
      pass  
