# ZeroDelay ⚡
### Parametric Income Insurance for Gig Delivery Workers

> **DEVTrails 2026 — Guidewire Hackathon | Phase 1 Submission**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20Site-1D9E75?style=flat-square)](https://1337insure.vercel.app/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)]()

> *Disruption hits. Money lands. Zero delay.*

---

## The Problem

India has **7 million+ gig delivery workers** on Swiggy, Zomato, Blinkit, and Amazon. Their income depends entirely on completing deliveries — but they have zero protection when the world stops them from working.

Heavy rain. Flash floods. Heatwaves. AQI spikes. Sudden curfews.

**One bad week = no income. No safety net. No insurance.**

---

## The Solution

ZeroDelay is a **parametric micro-insurance platform** that automatically pays workers when disruptions hit — no claim forms, no waiting, no rejection.

The system monitors real-time environmental and social conditions. The moment a threshold is breached, the payout fires automatically to the worker's UPI account within minutes.

```
Rainfall detected: 82mm  →  Threshold: 70mm  →  ₹400 sent via UPI ✓
```

---

## How It Works

| Disruption | Trigger Condition | Auto Payout |
|---|---|---|
| Heavy rain | Rainfall > 70mm/hr | ₹400 |
| Heatwave | Temperature > 42°C | ₹300 |
| Severe pollution | AQI > 350 | ₹300 |
| Flood / waterlogging | Govt Level 2+ alert | ₹500 |
| Curfew / zone shutdown | Government notification | ₹500 |

**Weekly premium: ₹30 · Max coverage: ₹2,000/week**

No manual verification. No adjuster. No delay.

---

## Live Demo

| Tab | What it shows |
|---|---|
| **Dashboard** | Registered workers, premiums collected, live payout counter |
| **Trigger Simulator** | Drag sliders past thresholds → full auto-payout flow with live log |
| **AI Risk Engine** | Zone-wise ML risk scores + dynamic premium pricing per area |
| **Policies** | All 5 parametric triggers with amounts and data sources |

---

## Features

- **Worker onboarding** — register with platform, zone, and weekly earnings
- **AI risk profiling** — ML model scores each delivery zone on historical disruption data
- **Dynamic premium pricing** — high-risk zones pay more, low-risk zones get discounts
- **Real-time monitoring** — continuous polling of weather, AQI, and government alert APIs
- **Automated claim trigger** — zero human intervention from detection to payout
- **Fraud detection** — anomaly detection flags GPS spoofing and duplicate claims
- **Instant UPI payout** — money reaches workers within minutes of a trigger event

---

## Architecture

```
Worker App (Web / Mobile)
        │
        ▼
   Frontend — React.js
        │  REST APIs
        ▼
   Backend — Node.js / FastAPI
        │
   ┌────┴────┐
   ▼         ▼
AI Risk    Fraud
Engine     Detection
   │         │
   └────┬────┘
        ▼
   PostgreSQL Database
   Workers | Policies | Claims | Payouts
        │
        ▼
   External APIs
   OpenWeather · AQI · Google Maps · Razorpay · NDMA
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend (demo) | HTML, CSS, Vanilla JS |
| Frontend (production) | React.js + Tailwind CSS |
| Backend | FastAPI (Python) / Node.js + Express |
| AI / ML | scikit-learn, TensorFlow, Pandas, NumPy |
| Database | PostgreSQL |
| Payments | Razorpay / Stripe sandbox |
| Weather | OpenWeather API |
| Air quality | AQI APIs |
| Govt alerts | NDMA / Government alert feeds |

---

## Business Model

**Revenue streams:**
1. **Premium collection** — ₹30/worker/week. At 100K users = ₹30L weekly revenue
2. **Platform partnerships** — Swiggy / Zomato subsidize premiums to improve worker retention
3. **Risk analytics** — urban disruption data sold to insurers and logistics platforms
4. **Enterprise integration** — co-branded policies with existing insurers

**Market opportunity:**
- Current gig workforce: **7 million**
- Projected by 2030: **23 million**
- Gig economy market size: **$455 billion**

---

## Local Setup

No build step. Just open the file.

```bash
git clone https://github.com/arijit-06/1337_Insure
cd 1337_Insure
open index.html
```

**Deploy to Vercel:**
1. Import repo at [vercel.com](https://vercel.com)
2. Framework preset: **Other**
3. Deploy — live in ~30 seconds

**Deploy via GitHub Pages:**
1. Repo Settings → Pages → Source: `main` branch, root `/`
2. Live at `https://arijit-06.github.io/1337_Insure`

---

## Project Structure

```
├── index.html       # App shell + all tabs
├── style.css        # Styles + responsive layout
├── app.js           # Tab logic + trigger simulator
└── README.md
```

---

## Team

| Name | Role |
|---|---|
| Arijit Das | |
| Sourashis Sabud | |
| Sanskriti Ranjan | |
| Shivansh Dhingra | |

---

> Built for **Guidewire DEVTrails 2026 Hackathon**
