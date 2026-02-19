/* CYBEROUS SEC | TERMINAL INTERFACE LOGIC */

const terminalInput = document.getElementById('terminal-input');
const outputStream = document.getElementById('output-stream');

terminalInput.addEventListener('keydown', async (e) => {
    if (e.key === 'Enter') {
        const cmd = terminalInput.value.trim();
        if (!cmd) return;

        // 1. Display User Command
        appendLog(`>> ${cmd}`, 'user-line');
        terminalInput.value = '';

        // 2. Send to Backend (File 1: main.py)
        try {
            const response = await fetch('/api/terminal', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ input: cmd })
            });

            const data = await response.json();

            // 3. Handle Logic-Lock Status
            if (data.status === 'MASTER') {
                appendLog(`[ADMIN_AUTH] ${data.message}`, 'sys-master');
            } else if (data.status === 'LOCKED') {
                appendLog(`[!] ${data.message}`, 'sys-error');
            } else {
                appendLog(data.message, 'sys-ai');
            }

        } catch (error) {
            appendLog(`SYSTEM_FAULT: UNABLE TO REACH SOVEREIGN CORE.`, 'sys-error');
        }
    }
});

function appendLog(text, className) {
    const p = document.createElement('p');
    p.className = className;
    p.innerText = text;
    outputStream.appendChild(p);
    
    // Pillar 11: Auto-scroll to bottom
    outputStream.scrollTop = outputStream.scrollHeight;
}