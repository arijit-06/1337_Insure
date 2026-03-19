const floodLabels = ['None', 'Watch', 'Warning', 'Alert'];

// Tab switching
document.querySelectorAll('.tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.section').forEach(s => s.classList.remove('visible'));
    tab.classList.add('active');
    document.getElementById('tab-' + tab.dataset.tab).classList.add('visible');
  });
});

// Slider updates
function updateSlider(type) {
  const rain = parseInt(document.getElementById('rain-slider').value);
  const temp = parseInt(document.getElementById('temp-slider').value);
  const aqi = parseInt(document.getElementById('aqi-slider').value);
  const flood = parseInt(document.getElementById('flood-slider').value);

  document.getElementById('rain-val').textContent = rain + ' mm';
  document.getElementById('temp-val').textContent = temp + '°C';
  document.getElementById('aqi-val').textContent = aqi;
  document.getElementById('flood-val').textContent = floodLabels[flood];

  // Live color feedback
  document.getElementById('rain-card').classList.toggle('triggered', rain > 70);
  document.getElementById('temp-card').classList.toggle('triggered', temp > 42);
  document.getElementById('aqi-card').classList.toggle('triggered', aqi > 350);
  document.getElementById('flood-card').classList.toggle('triggered', flood >= 2);
}

['rain', 'temp', 'aqi', 'flood'].forEach(type => {
  document.getElementById(type + '-slider').addEventListener('input', () => updateSlider(type));
});

// Log helper
function addLog(msg, cls) {
  const box = document.getElementById('sim-log');
  const entry = document.createElement('div');
  entry.className = 'log-entry' + (cls ? ' ' + cls : '');
  const t = new Date().toLocaleTimeString();
  entry.textContent = `[${t}] ${msg}`;
  box.appendChild(entry);
  box.scrollTop = box.scrollHeight;
}

// Simulate
document.getElementById('sim-btn').addEventListener('click', () => {
  const rain = parseInt(document.getElementById('rain-slider').value);
  const temp = parseInt(document.getElementById('temp-slider').value);
  const aqi = parseInt(document.getElementById('aqi-slider').value);
  const flood = parseInt(document.getElementById('flood-slider').value);

  const btn = document.getElementById('sim-btn');
  btn.disabled = true;
  document.getElementById('payout-box').classList.remove('show');
  document.getElementById('sim-log').innerHTML = '';

  addLog('Fetching real-time data from APIs...');

  setTimeout(() => {
    addLog(`Rainfall: ${rain}mm | Temp: ${temp}°C | AQI: ${aqi} | Flood: ${floodLabels[flood]}`);
    setTimeout(() => {
      const triggers = [];
      let total = 0;
      if (rain > 70) { triggers.push(`Heavy rain (${rain}mm > 70mm)`); total += 400; }
      if (temp > 42) { triggers.push(`Heatwave (${temp}°C > 42°C)`); total += 300; }
      if (aqi > 350) { triggers.push(`Severe pollution (AQI ${aqi} > 350)`); total += 300; }
      if (flood >= 2) { triggers.push(`Flood alert (${floodLabels[flood]})`); total += 500; }

      if (triggers.length === 0) {
        addLog('All parameters within normal range. No claim triggered.');
        addLog('Workers safe to operate. Monitoring continues.', 'success');
        btn.disabled = false;
        return;
      }

      triggers.forEach(t => addLog('TRIGGER: ' + t, 'alert'));

      setTimeout(() => {
        addLog('Claim auto-initiated for all insured workers in zone...', 'alert');
        setTimeout(() => {
          addLog('Running fraud detection model...');
          setTimeout(() => {
            addLog('Fraud check passed. Processing UPI transfer...');
            setTimeout(() => {
              addLog(`PAYOUT of ₹${total} sent to 4 workers via UPI.`, 'payout');
              document.getElementById('payout-amount').textContent = '₹' + total;
              document.getElementById('payout-msg').textContent = `Sent to 4 workers via UPI — zero manual steps`;
              document.getElementById('payout-box').classList.add('show');

              // Update dashboard
              const perWorker = total;
              const totalPaid = total * 4;
              document.getElementById('d-payouts').textContent = '₹' + totalPaid.toLocaleString('en-IN');
              document.getElementById('d-payout-sub').textContent = triggers.length + ' disruption(s) triggered today';
              document.getElementById('payout-card').classList.add('highlight');

              btn.disabled = false;
            }, 700);
          }, 600);
        }, 500);
      }, 400);
    }, 800);
  }, 600);
});
