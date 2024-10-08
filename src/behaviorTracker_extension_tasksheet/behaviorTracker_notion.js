// behaviorTracker_notion.js
(function() {
// check if the current page is valid
    function checkValidPage() {
        const currentUrl = window.location.href;
        if (!currentUrl.includes('docs.google.com/forms')) {
            if (currentUrl.includes('chat.openai.com')) {
                alert("Reminder: This extension should not be activated on the GPT website. Please activate it on the tasksheet (Google Form) window!");
            } else {
                alert("Reminder: You should activate the extension on the tasksheet (Google Form) window!");
            }
            return false;
        }
        return true;
    }

    // Check if the page is valid before proceeding
    if (!checkValidPage()) {
        return; // Stop execution if the page is not valid
    }


    // Timer variables
    let countdownTimer;
    let timeLeft = 18 * 60; // 18 minutes in seconds
    let timerDisplay;
    let warningDisplay;

    // Behavior tracking variables
    let behaviorData = [];
    let copyCount = 0;
    let totalCopyCount = 0;
    let totalPasteCount = 0;
    let lastCopiedText = '';
    let lastPastedText = '';
    let totalMouseMovement = 0;

    // Timer functions
    function updateTimerDisplay() {
        let minutes = Math.floor(timeLeft / 60);
        let seconds = timeLeft % 60;
        timerDisplay.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    }

     function startTimer() {
        if (countdownTimer) {
            clearInterval(countdownTimer);
        }
        timeLeft = 18 * 60; // Reset time to 18 minutes
        updateTimerDisplay();
        countdownTimer = setInterval(updateTimer, 1000);
    }

//final warning
let centerMessageDisplay;

function createCenterMessageDisplay() {
    centerMessageDisplay = document.createElement('div');
    centerMessageDisplay.style.position = 'fixed';
    centerMessageDisplay.style.top = '50%';
    centerMessageDisplay.style.left = '50%';
    centerMessageDisplay.style.transform = 'translate(-50%, -50%)';
    centerMessageDisplay.style.backgroundColor = 'rgba(0, 0, 0, 0.8)';
    centerMessageDisplay.style.color = 'white';
    centerMessageDisplay.style.padding = '20px';
    centerMessageDisplay.style.borderRadius = '10px';
    centerMessageDisplay.style.fontSize = '24px';
    centerMessageDisplay.style.fontWeight = 'bold';
    centerMessageDisplay.style.zIndex = '10000';
    centerMessageDisplay.style.display = 'none';
    document.body.appendChild(centerMessageDisplay);
}

function showCenterMessage(message) {
    centerMessageDisplay.textContent = message;
    centerMessageDisplay.style.display = 'block';
}

function hideCenterMessage() {
    centerMessageDisplay.style.display = 'none';
}



function updateTimer() {
    timeLeft--;
    updateTimerDisplay();

    if (timeLeft <= 120 && timeLeft > 0) {
        warningDisplay.textContent = "Warning: Time is almost up.";
    } else if (timeLeft <= 0) {
        stopTimer();
        warningDisplay.textContent = "Time's up! Click 'Finish' to save your data.";
        showCenterMessage("Time is out, click 'Finish' and download the file");
    }
}

function setupUI() {
    // ... [Previous UI setup code]

    let finishButton = document.createElement('button');
    finishButton.innerText = 'Finish';
    finishContainer.appendChild(finishButton);

    finishButton.addEventListener('click', function() {
        clearInterval(countdownTimer);
        exportBehaviorData();
        startContainer.style.display = 'block';
        chrome.storage.local.set({isTracking: false});
        hideCenterMessage(); // Hide the center message when Finish is clicked
    });

    // ... [Rest of the setupUI function]
}




    // Event listeners
    document.addEventListener('click', function(event) {
        let clickData = {
            type: 'click',
            e: 'click',
            timestamp: new Date().toISOString(),
            target: event.target.tagName,
            x: event.clientX,
            y: event.clientY
        };
        behaviorData.push(clickData);
        console.log('Click event:', clickData);
    });

    window.addEventListener('wheel', function(event) {
        let mousewheelData = {
            type: 'mousewheel',
            timestamp: new Date().toISOString(),
            deltaY: event.deltaY
        };
        behaviorData.push(mousewheelData);
        console.log('Scroll event:', mousewheelData);
    });

    document.addEventListener('mousemove', function(event) {
        if (event.movementX || event.movementY) {
            totalMouseMovement += Math.sqrt(event.movementX ** 2 + event.movementY ** 2);
            let mouseMovementData = {
                type: 'mouseMovement',
                timestamp: new Date().toISOString(),
                totalMouseMovement: totalMouseMovement
            };
            behaviorData.push(mouseMovementData);
            console.log('Total Mouse Movement:', totalMouseMovement);
        }
    });

    let timer; // For scroll event

    function handleWheelEvent(event) {
        clearTimeout(timer);
        timer = setTimeout(() => {
            let scrollEventData = {
                type: 'scroll',
                timestamp: new Date().toISOString(),
                deltaY: event.deltaY,
            };
            behaviorData.push(scrollEventData);
            console.log('Scroll event data:', scrollEventData);
        }, 500);
    }

    document.addEventListener('wheel', handleWheelEvent);

    document.addEventListener('copy', function(event) {
        let copiedText = window.getSelection().toString().trim();
        if (copiedText && copiedText !== lastCopiedText) {
            totalCopyCount++;
            lastCopiedText = copiedText;
            let copyData = {
                type: 'copy',
                timestamp: new Date().toISOString(),
                text: copiedText,
                textLength: copiedText.length
            };
            behaviorData.push(copyData);
            console.log('Copy event:', copyData);
            console.log('Total copy count:', totalCopyCount);
            console.log('Copied text length:', copiedText.length);
        }
    });

    document.addEventListener('paste', function(event) {
        let pastedText = (event.clipboardData || window.clipboardData).getData('text').trim();
        if (pastedText && pastedText !== lastPastedText) {
            totalPasteCount++;
            lastPastedText = pastedText;
            let pasteData = {
                type: 'paste',
                timestamp: new Date().toISOString(),
                text: pastedText,
                textLength: pastedText.length
            };
            behaviorData.push(pasteData);
            console.log('Paste event:', pasteData);
            console.log('Total paste count:', totalPasteCount);
            console.log('Pasted text length:', pastedText.length);
        }
    });

    document.addEventListener('keydown', function(event) {
        if (event.key === 'Delete' || event.key === 'Backspace') {
            let deleteEventData = {
                type: 'deleteAction',
                timestamp: new Date().toISOString(),
                key: event.key
            };
            behaviorData.push(deleteEventData);
            console.log('Delete action event:', deleteEventData);
        }
    });

    document.addEventListener('keypress', function(event) {
        let keyPressData = {
            type: 'keypress',
            timestamp: new Date().toISOString(),
            key: event.key,
            keyCode: event.keyCode,
            target: event.target.tagName
        };
        behaviorData.push(keyPressData);
        console.log('Keypress event:', keyPressData);
    });

    document.addEventListener('mouseup', function(event) {
        let highlightedText = window.getSelection().toString().trim();
        if (highlightedText) {
            let highlightEventData = {
                type: 'highlight',
                timestamp: new Date().toISOString(),
                highlightedText: highlightedText,
                highlightedTextLength: highlightedText.length
            };
            behaviorData.push(highlightEventData);
            console.log('Highlight event:', highlightEventData);
            resetIdleTimer();
        }
    });

    // Idle timer
    let idleTimer;
    let lastActionTime = Date.now();
    let idleTimes = [];

    function resetIdleTimer() {
        clearTimeout(idleTimer);
        idleTimer = setTimeout(function() {
            let currentTime = Date.now();
            let idleDuration = currentTime - lastActionTime;
            let idleData = {
                type: 'idle',
                timestamp: new Date().toISOString(),
                duration: idleDuration
            };
            idleTimes.push(idleData);
            behaviorData.push(idleData);
            console.log(`距离上次操作已经过去 ${idleDuration} 毫秒`);
        }, 2000);
    }

    function handleUserAction() {
        lastActionTime = Date.now();
        resetIdleTimer();
    }

    document.addEventListener('mousemove', handleUserAction);
    document.addEventListener('keypress', handleUserAction);
    document.addEventListener('scroll', handleUserAction);

    resetIdleTimer();

 // UI elements
    let startContainer = document.createElement('div');
    startContainer.style.position = 'fixed';
    startContainer.style.top = '10px';
    startContainer.style.right = '10px';
    startContainer.style.zIndex = 1000;
    document.body.appendChild(startContainer);

    let finishContainer = document.createElement('div');
    finishContainer.style.position = 'fixed';
    finishContainer.style.top = '50px';
    finishContainer.style.right = '10px';
    finishContainer.style.zIndex = 1000;
    document.body.appendChild(finishContainer);

    let startButton = document.createElement('button');
    startButton.innerText = 'Start';
    startContainer.appendChild(startButton);

    let finishButton = document.createElement('button');
    finishButton.innerText = 'Finish';
    finishContainer.appendChild(finishButton);

    // Create timer display
    timerDisplay = document.createElement('div');
    timerDisplay.style.position = 'fixed';
    timerDisplay.style.top = '90px';
    timerDisplay.style.right = '10px';
    timerDisplay.style.zIndex = 1000;
    document.body.appendChild(timerDisplay);

    warningDisplay = document.createElement('div');
    warningDisplay.style.position = 'fixed';
    warningDisplay.style.top = '110px';
    warningDisplay.style.right = '10px';
    warningDisplay.style.zIndex = 1000;
    warningDisplay.style.color = 'red';
    document.body.appendChild(warningDisplay);

    startButton.addEventListener('click', function() {
        behaviorData = [];
        copyCount = 0;
        console.log('Behavior data cleared.');
        alert('Start Now！');
        startTimer();
        startContainer.style.display = 'none'; // Hide start button
    });

    finishButton.addEventListener('click', function() {
        clearInterval(countdownTimer);
        exportBehaviorData();
        startContainer.style.display = 'block'; // Show start button
    });

    function exportBehaviorData() {
        let dataStr = JSON.stringify(behaviorData, null, 2);
        let blob = new Blob([dataStr], { type: 'application/json' });
        let url = URL.createObjectURL(blob);
        let a = document.createElement('a');
        a.href = url;
        a.download = 'tasksheet_data.json';
        a.click();
        URL.revokeObjectURL(url);
        console.log('Behavior data exported:', dataStr);
    }


})();