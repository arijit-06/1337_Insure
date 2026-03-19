'use strict';

// ── Demo users DB ──
const USERS = {
  '9876543210': { password: 'ravi123', name: 'Ravi Kumar', platform: 'Swiggy', zone: 'Velachery, Chennai', income: 6000, upi: 'ravi.kumar@upi', initials: 'RK' },
  '9123456780': { password: 'priya456', name: 'Priya Selvam', platform: 'Blinkit', zone: 'T Nagar, Chennai', income: 4800, upi: 'priya.selvam@upi', initials: 'PS' },
};

const FLOOD_LABELS = ['None', 'Watch', 'Warning', 'Alert'];
const PAYOUT_MAP = { rain: 400, heat: 300, aqi: 300, flood: 500, curfew: 500, strike: 500, other: 200 };

let currentUser = null;
let pendingCount = 0;

// ── Screen navigation ──
function showScreen(id) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById(id).classList.add('active');
  window.scrollTo(0, 0);
}
window.showScreen = showScreen;

// ── Tab switching ──
document.querySelectorAll('.tab').forEach(tab => {
  tab.addEventListener('click', () => {
    const bar = tab.closest('.tab-bar');
    bar.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    const section = tab.closest('.dash-wrap') || tab.closest('.app-wrap');
    section.querySelectorAll('.section').forEach(s => s.classList.remove('visible'));
    tab.classList.add('active');
    document.getElementById('tab-' + tab.dataset.tab).classList.add('visible');
  });
});

// ── Login ──
function doLogin() {
  const phone = document.getElementById('login-phone').value.trim();
  const pass  = document.getElementById('login-pass').value;
  const errEl = document.getElementById('login-error');
  errEl.textContent = '';

  if (!phone || phone.length !== 10) { errEl.textContent = 'Enter a valid 10-digit mobile number.'; return; }
  if (!pass) { errEl.textContent = 'Enter your password.'; return; }

  const user = USERS[phone];
  if (!user || user.password !== pass) { errEl.textContent = 'Invalid mobile number or password.'; return; }

  currentUser = { phone, ...user };
  loadDashboard();
  showScreen('screen-dashboard');
}
window.doLogin = doLogin;

// ── Register ──
function doRegister() {
  const name     = document.getElementById('reg-name').value.trim();
  const phone    = document.getElementById('reg-phone').value.trim();
  const platform = document.getElementById('reg-platform').value;
  const zone     = document.getElementById('reg-zone').value.trim();
  const income   = document.getElementById('reg-income').value.trim();
  const upi      = document.getElementById('reg-upi').value.trim();
  const pass     = document.getElementById('reg-pass').value;
  const pass2    = document.getElementById('reg-pass2').value;
  const errEl    = document.getElementById('reg-error');
  errEl.textContent = '';

  if (!name)              { errEl.textContent = 'Enter your full name.'; return; }
  if (phone.length !== 10){ errEl.textContent = 'Enter a valid 10-digit mobile number.'; return; }
  if (!platform)          { errEl.textContent = 'Select your delivery platform.'; return; }
  if (!zone)              { errEl.textContent = 'Enter your delivery zone.'; return; }
  if (!income || isNaN(income)) { errEl.textContent = 'Enter your weekly income.'; return; }
  if (!upi)               { errEl.textContent = 'Enter your UPI ID.'; return; }
  if (pass.length < 6)    { errEl.textContent = 'Password must be at least 6 characters.'; return; }
  if (pass !== pass2)     { errEl.textContent = 'Passwords do not match.'; return; }
  if (USERS[phone])       { errEl.textContent = 'This mobile number is already registered.'; return; }

  const initials = name.split(' ').map(w => w[0]).join('').toUpperCase().slice(0, 2);
  USERS[phone] = { password: pass, name, platform, zone, income: parseInt(income), upi, initials };
  currentUser = { phone, ...USERS[phone] };
  loadDashboard();
  showScreen('screen-dashboard');
}
window.doRegister = doRegister;

// ── Logout ──
function doLogout() {
  currentUser = null;
  document.getElementById('login-phone').value = '';
  document.getElementById('login-pass').value = '';
  document.getElementById('login-error').textContent = '';
  showScreen('screen-landing');
}
window.doLogout = doLogout;

// ── Load dashboard with user data ──
function loadDashboard() {
  const u = currentUser;
  document.getElementById('nav-worker-name').textContent = u.name.split(' ')[0] + ' ' + u.initials.slice(-1) + '.';
  document.getElementById('dash-av').textContent   = u.initials;
  document.getElementById('dash-name').textContent = u.name;
  document.getElementById('dash-meta').textContent = `${u.platform} · ${u.zone} · Active since Mar 2026`;
  document.getElementById('ov-zone').textContent   = u.zone.split(',')[0];
  document.getElementById('dash-upi').textContent  = u.upi;
  document.getElementById('pol-name').textContent  = u.name;
  document.getElementById('pol-platform').textContent = u.platform;
  document.getElementById('pol-zone').textContent  = u.zone;
  document.getElementById('pol-id').textContent    = 'ZD-CHN-' + Math.floor(1000 + Math.random() * 8999);

  // Reset tabs to overview
  document.querySelectorAll('.tab-bar .tab').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.section').forEach(s => s.classList.remove('visible'));
  document.querySelector('.tab-bar .tab[data-tab="overview"]').classList.add('active');
  document.getElementById('tab-overview').classList.add('visible');

  // Reset report form
  resetReport();
  pendingCount = 0;
  document.getElementById('pending-count').textContent = '0';
}

// ── Report: show payout estimate on type change ──
document.getElementById('rep-type').addEventListener('change', function () {
  const val = this.value;
  const box = document.getElementById('payout-estimate');
  const amt = document.getElementById('pe-amount');
  if (val && PAYOUT_MAP[val]) {
    amt.textContent = '₹' + PAYOUT_MAP[val];
    box.style.display = 'flex';
  } else {
    box.style.display = 'none';
  }
});

function showFileName(input) {
  const el = document.getElementById('file-name');
  el.textContent = input.files[0] ? '📎 ' + input.files[0].name : '';
}
window.showFileName = showFileName;

function submitReport() {
  const type  = document.getElementById('rep-type').value;
  const date  = document.getElementById('rep-date').value;
  const area  = document.getElementById('rep-area').value.trim();
  const hours = document.getElementById('rep-hours').value;
  const errEl = document.getElementById('rep-error');
  errEl.textContent = '';

  if (!type)  { errEl.textContent = 'Select the type of disruption.'; return; }
  if (!date)  { errEl.textContent = 'Select the date of disruption.'; return; }
  if (!area)  { errEl.textContent = 'Enter the affected area.'; return; }
  if (!hours) { errEl.textContent = 'Select how long you were unable to work.'; return; }

  const amt = PAYOUT_MAP[type] || 300;
  const ticket = Math.floor(100000 + Math.random() * 900000);
  document.getElementById('rep-payout-amt').textContent = amt;
  document.getElementById('ticket-id').textContent = ticket;
  document.getElementById('report-success').style.display = 'block';
  document.querySelector('.panel .ph').closest('.panel').style.display = 'none';

  pendingCount++;
  document.getElementById('pending-count').textContent = pendingCount;
}
window.submitReport = submitReport;

function resetReport() {
  ['rep-type','rep-date','rep-time','rep-area','rep-hours','rep-desc'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.value = '';
  });
  document.getElementById('file-name').textContent = '';
  document.getElementById('rep-error').textContent = '';
  document.getElementById('payout-estimate').style.display = 'none';
  document.getElementById('report-success').style.display = 'none';
  const firstPanel = document.querySelector('#tab-report .panel');
  if (firstPanel) firstPanel.style.display = 'block';
}
window.resetReport = resetReport;

// ── Mini simulator sliders (Policy tab) ──
const MINI = [
  { id: 'rain',  fmt: v => v + ' mm',   triggered: v => v > 70,  payout: 400 },
  { id: 'temp',  fmt: v => v + '°C',    triggered: v => v > 42,  payout: 300 },
  { id: 'aqi',   fmt: v => 'AQI ' + v,  triggered: v => v > 350, payout: 300 },
  { id: 'flood', fmt: v => FLOOD_LABELS[v], triggered: v => v >= 2, payout: 500 },
];
MINI.forEach(({ id, fmt, triggered }) => {
  const sl = document.getElementById('m-' + id + '-slider');
  const vl = document.getElementById('m-' + id + '-val');
  const bg = document.getElementById('m-' + id + '-badge');
  const cd = document.getElementById('m-' + id + '-card');
  sl.addEventListener('input', () => {
    const v = parseInt(sl.value);
    vl.textContent = fmt(v);
    const t = triggered(v);
    cd.classList.toggle('triggered', t);
    bg.textContent = t ? 'TRIGGERED' : 'Safe';
    bg.className = 'mtc-badge ' + (t ? 'alert' : 'safe');
  });
});

function mLog(msg, cls) {
  const box = document.getElementById('m-sim-log');
  const el = document.createElement('div');
  el.className = 'log-line' + (cls ? ' ' + cls : '');
  el.textContent = `[${new Date().toLocaleTimeString()}] ${msg}`;
  box.appendChild(el);
  box.scrollTop = box.scrollHeight;
}

function runMiniSim() {
  const vals = MINI.map(({ id, fmt, triggered, payout }) => {
    const v = parseInt(document.getElementById('m-' + id + '-slider').value);
    return { id, val: v, fmt: fmt(v), triggered: triggered(v), payout };
  });

  const btn = document.getElementById('m-sim-btn');
  btn.disabled = true;
  document.getElementById('mini-payout').style.display = 'none';
  document.getElementById('m-log-wrap').style.display = 'block';
  document.getElementById('m-sim-log').innerHTML = '';

  mLog('Connecting to real-time data APIs...');
  setTimeout(() => {
    vals.forEach(v => mLog(`${v.id.toUpperCase()}: ${v.fmt}`));
    setTimeout(() => {
      const hits = vals.filter(v => v.triggered);
      const total = hits.reduce((s, v) => s + v.payout, 0);

      if (!hits.length) {
        mLog('All conditions within safe range. No payout triggered.', 'ok');
        btn.disabled = false;
        return;
      }

      hits.forEach(h => mLog('TRIGGER: ' + h.id + ' exceeded threshold → ₹' + h.payout, 'warn'));
      setTimeout(() => {
        mLog('Fraud detection running...');
        setTimeout(() => {
          mLog('Fraud check passed.', 'ok');
          setTimeout(() => {
            mLog('Initiating UPI transfer of ₹' + total + '...', 'ok');
            setTimeout(() => {
              mLog('PAYOUT SENT — ₹' + total + ' → ' + (currentUser?.upi || 'your UPI ID'), 'pay');
              const mpTxt = document.getElementById('mp-txt');
              mpTxt.textContent = '₹' + total + ' sent to ' + (currentUser?.upi || 'your UPI ID');
              document.getElementById('mini-payout').style.display = 'flex';
              btn.disabled = false;
            }, 600);
          }, 500);
        }, 700);
      }, 500);
    }, 800);
  }, 600);
}
window.runMiniSim = runMiniSim;

// ── Enter key on login ──
document.getElementById('login-pass').addEventListener('keydown', e => {
  if (e.key === 'Enter') doLogin();
});
