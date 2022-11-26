// Make sure if window is loaded
window.onload = function () {

    // Initialize variables
    const url = window.location.href;
    const quizBox = document.getElementById("quiz-box");
    const scoreBox = document.getElementById("score-box");
    const summaryTitle = document.getElementById("sumarry-title");
    const summary = document.getElementById("summary");
    const timerBox = document.getElementById("timer");
    const display_result = document.getElementById("result");
    let stopTimer = false;
  
    // Activate timer when quiz started
    const activateTimer = (time) => {
  
      // Initialize strTime and append display it in html
      strTime = ("00"+time).slice(-2)
      timerBox.innerHTML = `<b>${strTime}:00</b>`
  
      // Variable for timer
      let minutes = time - 1;
      let seconds = 60;
      let displaySeconds;
      let displayMinutes;
  
      // Function for countdown the timer
      const timer = setInterval(() => {
        seconds -= 1;
  
        // When second <0, change it to 59 and subtract minute by 1
        if (seconds < 0) {
          seconds = 59;
          minutes -= 1;
        }
        displayMinutes = ("00"+minutes).slice(-2)
  
        // When minutes < 0, set displaySecond and displayMinutes to 0
        if (minutes < 0) {
          displaySeconds = 0;
          displayMinutes = 0;
        }
        displaySeconds = ("00"+seconds).slice(-2)
  
        // When minutesd and second <=0 send data to the server and stop quiz
        if (minutes <= 0 && seconds <= 0) {
          setTimeout(() => {
            alert("Time Over!!");
            clearInterval(timer);
            timerBox.innerHTML = `<b>00:00</b>`;
            sendData(true);
          }, 400);
        }
  
        // Excecuted when there is an event from submit button. Set timer to 00:00
        if (stopTimer) {
          setTimeout(() => {
            clearInterval(timer);
            timerBox.innerHTML = `<b>00:00</b>`;
            //sendData(true);
          }, 0);
        }
  
        // Display timer into timerBox
        timerBox.innerHTML = `<b>${displayMinutes}:${displaySeconds}</b>`;
      }, 1000);
    };
  
    $.ajax({
      type: "GET",
      url: `${url}data`,
      success: function (response) {
  
        // Response.data contains question as key and qnswer as value
        data = response.data;
  
        // Looping data
        data.forEach((el) => {
  
          // Get question and answer from data and then add it into quizBox
          for (const [question, answers] of Object.entries(el)) {
            quizBox.innerHTML += `
                          <hr>
                          <div class ="mb-1 questions">
                              <b> ${question} </b>
                          </div>`;
  
            // Looping all answer for each question and display it into quizBox
            answers.forEach((answer) => {
              quizBox.innerHTML += `
                              <div class="form-field">
                                  <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}"></input>
                                  <label for="${question}-${answer}">${answer}</label>
                              </div>`;
            });
          }
        });
  
        // Activated timer when all question and answer is loaded
        activateTimer(response.time);
      },
      error: function (error) {
        
        console.log(error);
      },
    });
  
    // Get quiz-from and csrfmiddlewaretoken
    const quizForm = document.getElementById("quiz-form");
    const csrf = document.getElementsByName("csrfmiddlewaretoken");
    
    // SendData funtion for send user answer to the server
    const sendData = (truth) => {
  
      // Elements contain all answer from each quiz
      const data = {};
      const elements = [...document.getElementsByClassName("ans")];
      data["csrfmiddlewaretoken"] = csrf[0].value;
  
      // Looping elements and get checked answer
      elements.forEach((el) => {
  
        // Append user answer to data
        if (el.checked) {
          data[el.name] = el.value;
        } 
  
        // Executed when user doesn't check this answer
        else {
          if (!data[el.name]) {
            data[el.name] = null;
          }
        }
      });
  
      $.ajax({
        type: "POST",
        url: `${url}save`,
        data: data,
        success: function (response) {
         
          // Executed when user answer all questions or user haven't answer all questions until timeover
          if (response.full == "True" || truth) {
  
            // Stop timer
            stopTimer = true;
            
            // Get all user answer 
            const results = response.results;
            
            // Hide quiz form and display result 
            quizForm.classList.add("disp_none");
            display_result.style.display='flex';
            summaryTitle.classList.remove('disp_none');
  
            // Add this text to scoreBox
            scoreBox.innerHTML = `${
              response.score > 30
                ? "Congratulations. Your awareness level is high high up! :D"
                : "You have a low level of awareness... Take a tour on our website to get more insight!"}
                Your score is ${response.score}%`;
  
            // Looping all result and display itu
            results.forEach((res) => {
  
              const restDiv = document.createElement("div");
              
              for (const [question, resp] of Object.entries(res)) {
                restDiv.innerHTML += question;
                const cls = ["p-3", "h6", "container", "text-white"];
                restDiv.classList.add(...cls);
  
                const answer = resp["answered"];
                const correct = resp["correct_answer"];
  
                if (resp == "not answered") {
                  restDiv.innerHTML += " | Not Answered";
                  restDiv.classList.add("bg-secondary");
                } else {
                  if (answer == correct) {
                    restDiv.classList.add("bg-success");
                    restDiv.innerHTML += ` | ${answer}`;
                  } else {
                    restDiv.classList.add("bg-danger");
                    restDiv.innerHTML += ` | ${answer}`;
                  }
                }
              }
  
              // Append resDiv into summary
              summary.append(restDiv);
            });
          } else {
            alert("Answer all the Questions!!");
          }
        },
        error: function (error) {
          console.log(error);
        },
      });
    };
  
    // Listeter for quizForm, if button clicked, sendData to the server and display result
    quizForm.addEventListener("submit", (e) => {
     
      e.preventDefault();
      sendData(true);
    });
  };