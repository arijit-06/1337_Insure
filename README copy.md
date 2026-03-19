# GigShield
### AI-Powered Parametric Insurance for Gig Delivery Workers
**DEVTrails 2026 – Guidewire Hackathon**

---

## Live Demo

Open `index.html` in any browser — no build step, no server needed.

Or deploy instantly via GitHub Pages:
1. Go to repo **Settings → Pages**
2. Set source to `main` branch, root `/`
3. Your demo is live at `https://<username>.github.io/1337_Insure`

---

## What it does

GigShield automatically compensates gig delivery workers (Swiggy, Zomato, Blinkit, Amazon) when external disruptions prevent them from working — **no claim forms, no waiting**.

| Disruption | Threshold | Auto Payout |
|---|---|---|
| Heavy rain | > 70mm/hr | ₹400 |
| Heatwave | > 42°C | ₹300 |
| Severe pollution | AQI > 350 | ₹300 |
| Flood alert | Level 2+ | ₹500 |
| Curfew / shutdown | Govt alert | ₹500 |

Weekly premium: **₹30** · Max coverage: **₹2,000/week**

---

## Demo Features

- **Dashboard** — registered workers, weekly premiums, live payout counter
- **Trigger Simulator** — drag sliders past thresholds → watch full auto-payout flow
- **AI Risk Engine** — zone-wise ML risk scores + dynamic premium pricing
- **Policies** — all 5 parametric triggers with payout amounts

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, Vanilla JS |
| UI Fonts | DM Sans + DM Mono (Google Fonts) |
| Backend (planned) | FastAPI (Python) |
| AI Layer (planned) | scikit-learn, TensorFlow |
| Database (planned) | PostgreSQL |
| APIs (planned) | OpenWeather, AQI API, Razorpay |

---

## Project Structure

```
├── index.html      # Main app
├── style.css       # Styles
├── app.js          # Logic + simulator
└── README.md
```

---

## Team

- Arijit Das
- Sourashis Sabud
- Sanskriti Ranjan
- Shivansh Dhingra

Built for **Guidewire DEVTrails 2026 Hackathon**
