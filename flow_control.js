async function syncIdentity() {
    try {
        const response = await fetch('/static/identity.json');
        const data = await response.json();
        
        const priceDisplay = document.querySelector('.price-display');
        const walletDisplay = document.querySelector('.wallet-box code');
        
        if(priceDisplay) {
            priceDisplay.innerHTML = `$${data.financial_config.entry_fee_usd.toFixed(2)} <small>USD</small>`;
        }
        if(walletDisplay) {
            walletDisplay.innerText = data.financial_config.vault_address;
        }
    } catch (e) {
        console.error("IDENTITY_SYNC_FAIL");
    }
}

window.addEventListener('load', () => {
    syncIdentity();
    // Existing ignition logic...
});