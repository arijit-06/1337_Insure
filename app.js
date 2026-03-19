const FLOOD_LABELS = ['None', 'Watch', 'Warning', 'Alert'];

// ── Tab switching ──
document.querySelectorAll('.tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.section').forEach(s => s.classList.remove('visible'));
    tab.classList.add('active');
    document.getElementById('tab-' + tab.dataset.tab).classList.add('visible');
  });
});

// ── Sliders ──
const sliders = {
  rain:  { id: 'rain',  max: 150, threshold: 70,  fmt: v => v + ' mm',    badge: v => v > 70  },
  temp:  { id: 'temp',  max: 55,  threshold: 42,  fmt: v => v + '°C',     badge: v => v > 42  },
  aqi:   { id: 'aqi',   max: 500, threshold: 350, fmt: v => 'AQI ' + v,   badge: v => v > 350 },
  flood: { id: 'flood', max: 3,   threshold: 2,   fmt: v => FLOOD_LABELS[v], badge: v => v >= 2 }
};

Object.values(sliders).forEach(({ id, fmt, badge }) => {
  const slider = document.getElementById(id + '-slider');
  const valEl  = document.getElementById(id + '-val');
  const badgeEl = document.getElementById(id + '-badge');
  const card   = document.getElementById(id + '-card');
  slider.addEventListener('input', () => {
    const v = parseInt(slider.value);
    valEl.textContent = fmt(v);
    const triggered = badge(v);
    card.classList.toggle('triggered', triggered);
    badgeEl.textContent = triggered ? 'TRIGGERED' : 'Safe';
    badgeEl.className = 'tc-badge ' + (triggered ? 'alert' : 'safe');
  });
});

// ── Log helper ──
function log(msg, cls) {
  const box = document.getElementById('sim-log');
  const el = document.createElement('div');
  el.className = 'log-line' + (cls ? ' ' + cls : '');
  el.textContent = `[${new Date().toLocaleTimeString()}] ${msg}`;
  box.appendChild(el);
  box.scrollTop = box.scrollHeight;
}

// ── Simulate ──
document.getElementById('sim-btn').addEventListener('click', () => {
  const rain  = parseInt(document.getElementById('rain-slider').value);
  const temp  = parseInt(document.getElementById('temp-slider').value);
  const aqi   = parseInt(document.getElementById('aqi-slider').value);
  const flood = parseInt(document.getElementById('flood-slider').value);

  const btn = document.getElementById('sim-btn');
  btn.disabled = true;
  document.getElementById('payout-box').classList.remove('show');
  document.getElementById('sim-log').innerHTML = '';

  log('Connecting to external APIs...');

  setTimeout(() => {
    log(`Data received — Rainfall: ${rain}mm | Temp: ${temp}°C | AQI: ${aqi} | Flood: ${FLOOD_LABELS[flood]}`);
    setTimeout(() => {
      const triggers = [];
      let total = 0;
      if (rain > 70)  { triggers.push(`Heavy rain (${rain}mm exceeds 70mm threshold)`);  total += 400; }
      if (temp > 42)  { triggers.push(`Heatwave (${temp}°C exceeds 42°C threshold)`);    total += 300; }
      if (aqi > 350)  { triggers.push(`Severe pollution (AQI ${aqi} exceeds 350)`);      total += 300; }
      if (flood >= 2) { triggers.push(`Flood alert level: ${FLOOD_LABELS[flood]}`);       total += 500; }

      if (!triggers.length) {
        log('All parameters within safe range — no claim triggered.');
        log('Workers safe to operate. Monitoring continues.', 'ok');
        btn.disabled = false;
        return;
      }

      triggers.forEach(t => log('TRIGGER DETECTED: ' + t, 'warn'));

      setTimeout(() => {
        log('Auto-initiating claim for all 4 insured workers...', 'warn');
        setTimeout(() => {
          log('Running fraud detection model (anomaly scan)...');
          setTimeout(() => {
            log('Fraud check passed — no suspicious activity detected.', 'ok');
            setTimeout(() => {
              log(`Processing UPI transfer of ₹${total} × 4 workers = ₹${total * 4}...`);
              setTimeout(() => {
                log(`PAYOUT COMPLETE — ₹${total} sent to each worker via UPI.`, 'pay');
                document.getElementById('payout-amount').textContent = '₹' + total;
                document.getElementById('payout-box').classList.add('show');
                document.getElementById('d-payouts').textContent = '₹' + (total * 4).toLocaleString('en-IN');
                document.getElementById('d-payout-sub').textContent = triggers.length + ' disruption(s) triggered today';
                document.getElementById('payout-card').classList.add('accent');
                btn.disabled = false;
              }, 600);
            }, 500);
          }, 700);
        }, 500);
      }, 400);
    }, 900);
  }, 600);
});
