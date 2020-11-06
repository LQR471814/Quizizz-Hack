# Quizizz-Hack
Getting Quizizz Answers Manually (Without a bot)

### Current status: Script is broken, Quizizz issued a fix

### Step 1: Getting the Quiz ID (This will be important later)

#### To get your Quiz ID:
 - Open up Chrome Inspector in the quiz window and go to the network tab (If there is nothing there than reload and keep the inspector open). 
 - Find a packet that's request url has something to do with `gameSummaryRec`. 
 - Double click it and find the entire Request url. There will be a parameter in the url called `quizId`, just copy the value of that and keep it in a safe place

![alt text](https://github.com/LQR471814/Quizizz-Hack/blob/master/get-quizID-1.jpg)

### Step 2: Using the Quiz ID to get the answers

 - Open your browser go to `https://quizizz.com/quiz/` + `YOUR QUIZ ID` 
 - Download the text with CTRL + S and store it in a safe place.
 
 #### In this case, it is `https://quizizz.com/quiz/5e9cfb6d707903001b527e47` 
 #### The output should be a load of text (JSON if you actually know what you are doing) 

![alt text](https://github.com/LQR471814/Quizizz-Hack/blob/master/get-answers-1.jpg)

### Step 3: Download the Quizizz Answers parser 
##### You should have python installed to run the answers parser, or you can just use the EXE version (You can download an EXE version of the parser [here](https://github.com/LQR471814/Quizizz-Hack/releases/latest))

#### By now technically if you have the answers in the form of that file you downloaded you could read the answers. Although, that file to someone who isn't technically inclined is pretty much jibberish, and to someone who is technically inclined may be a bit annoying to read (There are a lot of unnecessary nested dictionaries). 
#### So I modified a parser from an existing [Quizizz bot](https://github.com/reteps/quizizz-bot). The bot does not currently work at the time of writing but I got some of the parser code from it.

#### Once you have the parser downloaded:
 - Put the `parser.py` and the file you downloaded earlier in the same folder. 
 - Run `parser.py` and it will output a file called `answers.json`. 
 - Open `answers.json` and boom! You have your answers. 
 
 ##### If you can't read .JSON file format, you should probably learn how to but it isn't hard.

![alt text](https://github.com/LQR471814/Quizizz-Hack/blob/master/get-answers-2.jpg)

![alt text](https://github.com/LQR471814/Quizizz-Hack/blob/master/get-answers-4.jpg)
