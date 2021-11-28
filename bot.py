import praw
import random
import datetime
import time 
from textblob import TextBlob

# FIXME:
# copy your generate_comment function from the madlibs assignment here
madlibs = [
    "[COMP_SCI] is very [INTERESTING] however it can be [DIFFICULT] and [FRUSTRATING]. I now [UNDERSTAND] why the [HARVEY_MUDD] kids are such [NERDS].", 
    "My [ROOMATE] ate all my [APPLES] today. This is a [TRUE] story. They were [EXPENSIVE] for [ME], but if I [CONFRONT] [HER], she will [CRY].", 
    "[I] miss [MY_CAT] [SO_MUCH]. I wish I could bring her as an [EMOTIONAL] [SUPPORT] [ANIMAL]. ", 
    "I used to [PLAY] [MADLIBS] with my [LITTLE] [COUSIN] on long [CAR_RIDES]. They would always [CHEAT]. And somehow I was the one who got [IN_TROUBLE].", 
    "[JOE_BIDEN] is such a [HANDSOME] fellow. He is incredibly [CHARMING], [STRONG], and [SMART].", 
    " I love [BIRDS]. I love [CATS]. I love [DOGS]. I love [PIGS]. I love [HORSES]."

    ]


replacements = {
    'COMP_SCI': ['Comp sci', 'math', 'reading', 'art'],
    'INTERESTING': ['boring', 'fascinating', 'weird', 'interesting'],
    'DIFFICULT': ['hard', 'annoying', 'intriguing', 'difficult'], 
    'FRUSTRATING': ['make you want to scream', 'push you to the edge', 'frustrating'], 
    'UNDERSTAND': ['see', 'get', 'understand'], 
    'HARVEY_MUDD': ['Scripps', 'Harvey Mudd', 'Pitzer', 'Pomona'],
    'NERDS': ['losers,', 'nerds', 'weirdos'], 
    'ROOMATE': ['roomate', 'friend', 'boyfriend'], 
    'APPLES': ['apples', 'bananas', 'cookies'], 
    'TRUE': ['true', 'false'], 
    'EXPENSIVE': ['expensive', 'cheap'],
    'ME': ['a broke college student', 'me', 'my taste'], 
    'CONFRONT': ['get mad at', 'yell at', 'confront'], 
    'HER': ['her', 'him'],
    'CRY': ['cry', 'get upset', 'have a fit'], 
    'I': ['I', 'we', ], 
    'MY_CAT': ['my cat', 'my dog', 'my house'], 
    'SO_MUCH': ['so much', 'more than anything', 'an insane amount'], 
    'EMOTIONAL': ['mental', 'emotional'], 
    'SUPPORT': ['support', 'sanity', 'crutch'], 
    'ANIMAL': ['animal', 'friend', 'pet'], 
    'PLAY': ['play', 'write', 'do'], 
    'MADLIBS': ['games like this', 'games', 'madlibs', 'tic tac toe'], 
    'LITTLE': ['little', 'younger', 'baby'], 
    'COUSIN': ['cousin', 'sister', 'brother'], 
    'CAR_RIDES': ['car rides', 'trips', 'flights'], 
    'CHEAT': ['cheat', 'be annoying', 'whine'], 
    'IN_TROUBLE': ['in trouble', 'yelled at'], 
    'JOE_BIDEN': ['Joe Biden', 'Donald Trump', 'Obama'], 
    'HANDSOME': ['brave', 'weird', 'handsome'], 
    'CHARMING': ['annoying', 'loud', 'charming'], 
    'STRONG': ['weird', 'strange', 'strong'], 
    'SMART': ['crazy', 'smart', 'powerful'], 
    'BIRDS': ['birds', 'cats', 'dogs', 'horses', 'pigs'], 
    'CATS': ['birds', 'cats', 'dogs', 'horses', 'pigs'], 
    'DOGS': ['birds', 'cats', 'dogs', 'horses', 'pigs'], 
    'HORSES': ['birds', 'cats', 'dogs', 'horses', 'pigs'], 
    'PIGS': ['birds', 'cats', 'dogs', 'horses', 'pigs'], 
    }

def generate_comment():
    s= random.choice(madlibs)
    for k in replacements.keys(): 
        s= s.replace('['+k+']', random.choice(replacements[k])) 
    return s

# FIXME:
# connect to reddit 
reddit = praw.Reddit('lt25botcs40')

# FIXME:
# select a "home" submission in the /r/BotTown subreddit to post to,
# and put the url below
submission_url = 'https://www.reddit.com/r/BotTown2/comments/r29czx/analysis_trump_escalates_his_january_6_coverup_as/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once 
while True:
    try:
        print()
        print('New Iteration At: ', datetime.datetime.now())
        print('Title of Submission: ', submission.title)
        print('URL of Submission: ', submission.url)
        submission.comments.replace_more(limit=None)

        # Task 0 (2 points)
        all_comments = []
        for comment in submission.comments.list():
            all_comments.append(comment)

        print('Number of Comments: ', len(all_comments))

        # Task 1 (2 points)
        not_my_comments = []
        for comment in all_comments:
            if comment.author != 'lt25bot':
                not_my_comments.append(comment)

        print('Number of Not My Comments: ', len(not_my_comments))

        # Task 2 (2 points)
        has_not_commented = len(not_my_comments) == len(all_comments)

        if has_not_commented is True:
            reply = generate_comment()
            submission.reply(reply)
        # Task 3
        else:
            comments_without_my_replies = []
            for comment in not_my_comments:
                if comment.author != 'lt25bot':
                    response = False
                    for reply in comment.replies:
                        if str(reply.author) == 'lt25bot':
                            response = True
                if response is False:
                    comments_without_my_replies.append(comment)
            print('Number of Comments Without My Replies: ', len(comments_without_my_replies))

        # Task 4 (2 points)
            for comments in comments_without_my_replies:
                selection = random.choice(comments_without_my_replies)
                selection.reply(generate_comment())
                time.sleep(5)

        # Task 5 (2 points)
        randomnumber = random.random()
        allsubmissions = []
        if randomnumber >= 0.8:
            print('Original Submission')
            submission = reddit.submission(url='https://www.reddit.com/r/BotTown2/comments/r29czx/analysis_trump_escalates_his_january_6_coverup_as/')
            submission.reply(generate_comment())
        if randomnumber < 0.8:
            print('Top Subreddit Submission')
            for submission in reddit.subreddit('BotTown2').hot(limit=5):
                allsubmissions.append(submission)
            newsubmission = random.choice(allsubmissions)
            submission = reddit.submission(id=newsubmission)
            print('Submission ID: ', newsubmission)
            print(newsubmission.title)

        # We sleep just for 1 second at the end of the while loop.
        # This doesn't avoid rate limiting
        # (since we're not sleeping for a long period of time),
        # but it does make the program's output more readable.
        

        for comment in submission.comments.list():
            if 'Comp sci' in comment.body.lower():
                comment.downvote()
                print('Comment Downvoted')


        # Downvote and upvote comments for opposition using TextBlob 
        for comment in submission.comments.list():
            blob = TextBlob(str(comment.body))
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity

            if 'interesting' in comment.body.lower() and polarity > 0.5:
                    comment.upvote()
            if 'difficult' in comment.body.lower() and polarity > 0.5:
                    comment.downvote()
            if 'interesting' in comment.body.lower() and subjectivity > 0:
                    comment.upvote()
            if 'difficult' in comment.body.lower() and subjectivity > 0:
                    comment.downvote()
    except praw.exceptions.RedditAPIException:
        pass 
        time.sleep(1)



