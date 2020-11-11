# Quizizz-Hack

Getting Quizizz Answers Manually (Without a bot)

## Current status: Script is broken, Quizizz issued a fix

### Step 1: Getting the Quiz ID (This will be important later)

#### To get your Quiz ID

- Open up Chrome Inspector in the quiz window and go to the network tab (If there is nothing there than reload and keep the inspector open).
- Find a packet that's request url has something to do with `gameSummaryRec`.
- Double click it and find the entire Request url. There will be a parameter in the url called `quizId`, just copy the value of that and keep it in a safe place

![alt text](https://github.com/LQR471814/Quizizz-Hack/blob/master/docs/get-quizID-1.jpg)

### Step 2: Using the Quiz ID to get the answers

- Open your browser go to `https://quizizz.com/quiz/` + `YOUR QUIZ ID`
- Download the text with CTRL + S and store it in a safe place.

#### In this case, it is `https://quizizz.com/quiz/5e9cfb6d707903001b527e47`

#### The output should be a load of text (JSON if you actually know what you are doing)

![alt text](https://github.com/LQR471814/Quizizz-Hack/blob/master/docs/get-answers-1.jpg)

### Step 3: Download the Quizizz Answers parser 

#### You should have python installed to run the answers parser, or you can just use the EXE version (You can download an EXE version of the parser [here](https://github.com/LQR471814/Quizizz-Hack/releases/latest))

#### By now technically if you have the answers in the form of that file you downloaded you could read the answers. Although, that file to someone who isn't technically inclined is pretty much jibberish, and to someone who is technically inclined may be a bit annoying to read (There are a lot of unnecessary nested dictionaries)

#### So I modified a parser from an existing [Quizizz bot](https://github.com/reteps/quizizz-bot). The bot does not currently work at the time of writing but I got some of the parser code from it

#### Once you have the parser downloaded

- Put the `parser.py` and the file you downloaded earlier in the same folder.
- Run `parser.py` and it will output a file called `answers.json`.
- Open `answers.json` and boom! You have your answers.

##### If you can't read .JSON file format, you should probably learn how to but it isn't hard

![alt text](https://github.com/LQR471814/Quizizz-Hack/blob/master/docs/get-answers-2.jpg)

![alt text](https://github.com/LQR471814/Quizizz-Hack/blob/master/docs/get-answers-4.jpg)

### Javascript Function that Parses answers (Contributed by xNetcat)

```javascript
// Here is the function to parse the json object. 
// It returns object with key/value pair where key is the question and value is the answer
function parseFile (fileObject) {
    let allAnswers = {}

    for (question of fileObject.data.quiz.info.questions) {
        let answer;
        if (question.type === "MCQ") {
            if (question.structure.options[question.structure.answer].text == "") {
                answer = question.structure.options[question.structure.answer].media[0].url;
            } else {
                answer = question.structure.options[question.structure.answer].text.replace("<p>", "").replace("</p>", "");
            }
        } else if (question.type == "MSQ") {
            answer = []
            for (answerC in question["structure"]["answer"]) {
                if (question.structure.options[answerC].text == "") {
                    answer.push(question.structure.options[answerC].media[0].url);
                } else {
                    answer.push(question.structure.options[answerC].text.replace("<p>", "").replace("</p>", ""));
                }
            }
        }
    
        questionStr = question.structure.query.text.replace('"', '\\"').replace("<p>", "").replace("</p>", "").replace("<strong>", "").replace("</strong>", "");
        allAnswers[questionStr] = answer;
    
    }
    return allAnswers;
}
```

Example usage with Node.js

```javascript
const fs = require('fs');

fs.readFile('file.json', (err, data) => {
    if (err) throw err;
    const jsonObject = JSON.parse(data);
    console.log(parseFile(jsonObject));
});
```
