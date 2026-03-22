const alarm = document.getElementById("alarmSound");
const statusText = document.getElementById("statusText");
const earText = document.getElementById("ear");
const marText = document.getElementById("mar");

let isPlaying = false;

function startAlarm() {
    if (!isPlaying) {
        alarm.loop = true;        
        alarm.play();
        isPlaying = true;
    }
}

function stopAlarm() {
    alarm.pause();               
    alarm.currentTime = 0;       
    isPlaying = false;
}

async function updateData() {
    const res = await fetch('/status');
    const data = await res.json();

    earText.innerText = data.EAR;
    marText.innerText = data.MAR;

    if (data.drowsy) {
        statusText.innerText = "DROWSY ⚠️";
        statusText.className = "status drowsy";
        startAlarm();   
    } else {
        statusText.innerText = "ACTIVE ✅";
        statusText.className = "status active";
        stopAlarm();   
    }
}


setInterval(updateData, 1500);