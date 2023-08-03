async function checkQuestionsRemaining(user) {
    var url = "/questions_remaining?userid=" + user.id;

    questionCount = 0;

    try {
        let response = await fetch(url);
        let data = await response.json();

        questionCount = data;
        console.log(data);
    }
    catch (error) {
        console.log(error);
    }

    var questionsRemaining = document.getElementById("questions-remaining");
    questionsRemaining.innerHTML = "Questions remaining: " + questionCount;
}

async function decrementQuestionsRemaining() {
    var url = "/questions_remaining_decrement?userid=" + Clerk.user.id;

    console.log(url);


    try {
        let response = await fetch(url);
        let data = await response.json();
        checkQuestionsRemaining(Clerk.user);
    }
    catch (error) {
        console.log(error);
    }



}