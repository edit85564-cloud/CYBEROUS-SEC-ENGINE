/* CYBEROUS SEC | PROCEDURAL AUDIO ENGINE */

const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
let nextNoteTime = 0.0;
const tempo = 126.0; // The Unstoppable Beat
let isBeatRunning = false;

function playKick(time) {
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();

    osc.type = 'triangle'; // Industrial texture
    osc.frequency.setValueAtTime(60, time);
    osc.frequency.exponentialRampToValueAtTime(0.01, time + 0.5);

    gain.gain.setValueAtTime(0.2, time);
    gain.gain.exponentialRampToValueAtTime(0.001, time + 0.5);

    osc.connect(gain);
    gain.connect(audioCtx.destination);

    osc.start(time);
    osc.stop(time + 0.5);
}

function scheduler() {
    while (nextNoteTime < audioCtx.currentTime + 0.1) {
        playKick(nextNoteTime);
        nextNoteTime += 60.0 / tempo;
    }
    if (isBeatRunning) {
        setTimeout(scheduler, 25);
    }
}

function startBeat() {
    if (audioCtx.state === 'suspended') {
        audioCtx.resume();
    }
    isBeatRunning = true;
    nextNoteTime = audioCtx.currentTime;
    scheduler();
}