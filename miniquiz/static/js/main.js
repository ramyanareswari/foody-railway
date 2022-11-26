// Make sure if window is loaded
window.onload = function () {
    console.log('hello world')

    // Initialize variables
    const modalBtns = [...document.getElementsByClassName('modal-button')]
    const modalBody = document.getElementById('modal-body-confirm')
    const startBtn = document.getElementById('start-button')
    const url = window.location.href

    // Modal content
    modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
        // Initialize variables
        const name = modalBtn.getAttribute('data-quiz')
        const numQuestions = modalBtn.getAttribute('data-questions')
        const scoreToPass = modalBtn.getAttribute('data-pass')
        const time = modalBtn.getAttribute('data-time')

        // Content in modal body
        modalBody.innerHTML = `
            <div class="h5 mb-3">Are you ready to begin "<b>${name}</b>"?</div>
            <div class="text-muted">
                <ul>
                    <li>number of questions: <b>${numQuestions}</b></li>
                    <li>score to pass: <b>${scoreToPass}%</b></li>
                    <li>time: <b>${time} min</b></li>
                </ul>
            </div>
        `

        // Click to start quiz in modal
        startBtn.addEventListener('click', ()=>{
            window.location.href = url + pk
        })
    
    }))
    
}