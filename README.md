# SaveAFriend
Suicide is one of the leading causes of deaths in the world with over
hundreds of thousands people affected every single year. Depression is
one of the main factors that causes people to have thoughts of ending their
lives. People resort to many ways to cope against the painful thoughts, whether
it is seeking therapy, talking with loved ones, or writing in a journal. 
Unfortunately, many experience it worse enough to avoid any resources that 
could give them a reason they have all the reasons to live. With the world evolving
into a digital-centric society. People's digital footprint, all the social media
posts, photos, words, we've posted on the internet--paints a bigger picture
of our lives than we realize; particularly their mental health. With
billions of users using the platform everyday, there is no telling how many
people reach the climax of their mental breakdown, and leave their final message
to the world before they leave. AI, an revolutionary investment in technology has
great potential to solve many world problems, including this one. Therefore,
we decided to create a project that incorporates aspects of machine learning into
an application of artificial intelligence with the means to save the thousands of people
who need help.

## What it does
SaveAFriend uses an innovative learning model adapted from the [NPJ Digital Medicine Journal](https://www.nature.com/articles/s41746-020-0287-6) to identify suicidal ideation (SI) in an individual. All a concerned friend needs to do is enter their friend's social media handle @user and we parse through their social medias where we look for themes of SI and alerting the necessary authorities to bring help to their way. The application of the AI takes user input of specific users from common social media platforms such as Twitter, Reddit, and Facebook, and calculates the [AUS](https://arize.com/blog/what-is-auc/#:~:text=To%20calculate%20AUC%2C%20we%20need,positive%20and%20negative%20classes%2C%20respectively) of each user based on their suicidal idiation, based on the time they posted, the amount of times they posted, to determine the seriousness of the situation. With the info, the AI can automatically alert authorities that specialize in online crime with the info automatically sent so the social media user gets the assistance they need. 

## How we Built it
Primarily using the [Cohere API](https://docs.cohere.ai/)'s Classify, we created the AI module within Python with datasets in
csv format. This handled with the inner structures of the AI and the training process
to bring the AI into action. Afterwards, we integrated the back-end of the project into
a mobile application. This was created with Flask and Anvil which we then brought it
available onto iOS using the Anvil IDE. For the inner algorithms that dealt with AUS, we
worked with python modules such as numPy and scikit for optimizing the AI's accuracy.

## Challenges
The process of training the AI to first identify suicide-related phrases was a difficult task as the ideal accuracy we expected
needed more resources and datasets. The implementation of the AUS algorithm was also a challenge since there are many factors
when it comes to human emotions. After all, AI can't perfectly detect whether someone is exerting symptoms of serious depression vs detecting whether prompts are suicide-related or not. We also considered implementing a frequency-based algorithm to also track how frequent the person has posted suicide-related prompts either consecutively or within a short timespan. However, considering how complex human emotions are, we can't weed out those who post less frequent, since they have as much of a chance of experiencing the same pain as others.

## Accomplishments that we're proud of
When we got the AI to finally decipher prompts correctly, we were astonded by how the AI came to life within the little time we worked on it. Using the Cohere API was rather a new experience for us, in addition to our basic knowledge of machine learning in general. 

## What we Learned
We worked with many different frameworks, languages, and APIs and we learned how to train AI efficiently to filter out certain terms in English on the back-end. With that component of the project, we learned how to integrate it into a suitable GUI for day to day users to interact with using front-end development. We learned about a crucial algorithm that can detect common patterns in human emotion which often lead them to commit to certain acts, which we then attempted to implement into our AI for more of an accurate identification when users input their friends.

## What's next for Save A Friend
When the AI sprouted into a functional data filtering system, our brains also sprouted with new ideas we can implement to further improve the project in the future. This includes expansion to other social media platforms, using other forms of social media posts (ie. photos, videos, stories), and considering more scenarios of human emotion that would use algorithms distinct from AUS, such as dealing with frequency as previous discussed in our challenges. We could also add more to the AI and familiarize it with other aspects of ideations, whether it is homicidal or hate speech. With these additions, we can contact authorities who specialize in these areas to stop any form of digital abuse. With these ideas, more people can recieve the help they need to get back on their feet and enjoy their life to the fullest. 
