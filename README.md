# GigShield
### AI-Powered Parametric Insurance Platform for Gig Delivery Workers

DEVTrails 2026 – Guidewire Hackathon  
Phase 1 Submission

---

# Overview

GigShield is an **AI-powered parametric insurance platform** designed to protect gig delivery workers from income loss caused by external disruptions such as extreme weather, pollution, curfews, or regional shutdowns.

Delivery partners working for platforms such as **Swiggy, Zomato, Blinkit, Amazon, and Zepto** rely on continuous work to maintain stable income. However, unpredictable disruptions can prevent them from completing deliveries and directly impact their earnings.

GigShield introduces a **fully automated insurance model** where payouts are triggered automatically based on real-time environmental or social conditions.

Instead of manual claim filing, the system continuously monitors disruption parameters using external data sources and automatically compensates workers when conditions exceed predefined thresholds.

---

# Problem Statement

India has more than **7 million gig workers**, many of whom depend on delivery platforms for their livelihood. These workers face multiple uncontrollable disruptions including:

- Extreme rainfall
- Flooded streets
- Heatwaves
- Severe air pollution
- Government curfews
- Local strikes or shutdowns

Since their earnings depend on the number of deliveries completed, these disruptions cause **immediate income loss**.

Currently, there is **no insurance product specifically designed to protect gig workers against lost income caused by external disruptions.**

---

# Solution

GigShield provides a **parametric income protection insurance platform** that automatically compensates gig workers when environmental or social disruptions prevent them from working.

Key characteristics of the platform include:

- Weekly subscription-based insurance model
- AI-powered risk profiling
- Automatic disruption detection
- Real-time claims triggering
- Instant payout processing
- Fraud detection using machine learning

This creates a **transparent, scalable, and low-cost insurance solution tailored specifically for gig workers.**

---

# Target Persona

### Example Persona

Name: Ravi Kumar  
Age: 28  
City: Chennai  
Platform: Swiggy  
Weekly Income: ₹6000  

### Challenges

- Heavy rain floods streets and prevents deliveries
- Extreme heat reduces working hours
- Pollution makes outdoor work unsafe
- Curfews block delivery zones

These disruptions directly reduce Ravi's weekly income.

GigShield ensures Ravi receives **financial compensation whenever such disruptions occur.**

---

# Product Features

## Worker Onboarding

Workers register by providing:

- Name
- Delivery platform
- Delivery zone
- Average weekly earnings
- Work schedule

The system creates a worker profile used for risk evaluation.

---

## AI Risk Profiling

The platform evaluates environmental and operational risk factors such as:

- Historical weather patterns
- Pollution levels
- Flood-prone zones
- Traffic congestion
- Local disruption frequency

Machine learning models calculate a **risk score** for the worker's operating area.

---

## Policy Creation

Based on the risk score, GigShield generates a weekly insurance policy.

Example:

Weekly Premium: ₹30  
Coverage Limit: ₹2000  
Coverage Period: 7 days  

Coverage triggers include environmental and social disruption events.

---

## Real-Time Monitoring

The platform continuously monitors external data sources including:

- Weather APIs
- Air quality APIs
- Government alerts
- Traffic disruption feeds

These data streams help detect disruption conditions affecting workers.

---

## Automated Claim Trigger

When disruption parameters exceed defined thresholds, the system automatically initiates a claim.

Example:

Rainfall detected: 82mm  
Threshold: 70mm  

Claim automatically triggered.

---

## Instant Payout

Workers receive payouts through:

- UPI transfer
- Payment gateways
- Digital wallets

This ensures immediate financial support during disruptions.

---

# Business Model

GigShield follows a **micro-insurance subscription model** designed specifically for gig workers.

## Weekly Subscription Model

Workers pay a small weekly premium to remain insured.

Example:

Weekly Premium: ₹30  
Monthly Equivalent: ₹120  

Coverage: ₹2000 per week

---

## Revenue Model

GigShield generates revenue through the following channels.

### 1 Premium Collection

Workers subscribe to weekly insurance plans.

Example:

100,000 users × ₹30 weekly premium  
= ₹3,000,000 weekly revenue

---

### 2 Platform Partnerships

Delivery platforms may partner with GigShield to provide income protection to their workers.

Potential partners:

- Swiggy
- Zomato
- Blinkit
- Amazon Logistics

Platforms may subsidize insurance premiums to improve worker retention.

---

### 3 Data-Driven Risk Analytics

GigShield collects valuable insights regarding:

- Urban disruption patterns
- Environmental risk zones
- Worker activity patterns

These analytics can be sold to insurers and logistics platforms.

---

### 4 Enterprise Insurance Integration

GigShield can integrate with existing insurance providers to offer co-branded policies.

---

# Market Opportunity

India’s gig economy is rapidly growing.

Key statistics:

- Estimated gig workforce: **7 million**
- Expected by 2030: **23 million workers**
- Gig economy market size: **$455 billion projected**

Delivery services represent one of the largest segments of gig workers.

GigShield addresses a **previously unserved niche in micro-insurance.**

---

# Parametric Trigger Events

| Event | Condition | Payout |
|------|-----------|--------|
Heavy Rain | Rainfall > 70mm | ₹400 |
Heatwave | Temperature > 42°C | ₹300 |
Severe Pollution | AQI > 350 | ₹300 |
Flood | Waterlogging alerts | ₹500 |
Curfew | Government zone shutdown | ₹500 |

These triggers ensure **objective claims processing without manual verification.**

---

# AI / Machine Learning Integration

AI plays a critical role in multiple components of the system.

## Risk Prediction Model

Machine learning models analyze historical disruption data to estimate risk levels.

Inputs:

- Weather history
- Flood data
- Pollution patterns
- Traffic conditions

Outputs:

- Zone risk score
- Premium adjustment factor

---

## Dynamic Premium Pricing

AI dynamically adjusts weekly premiums based on real-time risk levels.

Example:

Low-risk zone → lower premium  
High-risk zone → higher premium

---

## Fraud Detection

Fraud detection models identify suspicious activities such as:

- GPS spoofing
- Duplicate claims
- False disruption reporting
- Unusual user activity patterns

Techniques used:

- Anomaly detection
- Pattern analysis
- Cross-validation with external data sources

---

# Technology Stack

## Frontend

React.js  
Bootstrap / Tailwind CSS

Features:

- Worker dashboard
- Policy management interface
- Claims history
- Subscription management

---

## Backend

Node.js / Express  
or  
FastAPI (Python)

Responsibilities:

- Policy management
- Risk calculation
- Claims automation
- API integration

---

## AI Layer

Python

Libraries:

- Scikit-learn
- TensorFlow / PyTorch
- Pandas
- NumPy

---

## Database

PostgreSQL

Stores:

- Worker profiles
- Policies
- Risk scores
- Claims history
- Payout records

---

## External APIs

Weather data  
OpenWeather API

Air quality  
AQI APIs

Traffic data  
Google Maps API

Payments  
Razorpay / Stripe sandbox

---

# System Architecture

The GigShield platform follows a modular architecture consisting of four main layers:

1. Client Layer  
2. Application Layer  
3. Intelligence Layer  
4. Data & Integration Layer  

This architecture enables scalable insurance automation with real-time disruption monitoring.

---

## High-Level Architecture

            ┌──────────────────────┐
            │   Worker Application  │
            │   (Web / Mobile App)  │
            └──────────┬───────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │     Frontend UI       │
            │        React          │
            └──────────┬───────────┘
                       │ REST APIs
                       ▼
            ┌──────────────────────┐
            │      Backend API      │
            │   Node.js / FastAPI   │
            └───────┬───────┬──────┘
                    │       │
                    │       │
                    ▼       ▼
     ┌─────────────────┐   ┌─────────────────┐
     │   AI Risk Engine │   │ Fraud Detection │
     │   (ML Models)    │   │   ML Models     │
     └─────────┬────────┘   └─────────┬───────┘
               │                      │
               ▼                      ▼
        ┌────────────────────────────────┐
        │        PostgreSQL Database      │
        │ Workers | Policies | Claims     │
        │ Risk Scores | Payout Records    │
        └────────────────────────────────┘
                       │
                       ▼
        ┌────────────────────────────────┐
        │       External Integrations     │
        │                                 │
        │  Weather APIs (OpenWeather)     │
        │  Air Quality APIs (AQI)         │
        │  Traffic APIs (Google Maps)     │
        │  Payment Gateway (Razorpay)     │
        │  Government Alert Systems       │
        └────────────────────────────────┘

        
---

## Component Responsibilities

### Worker Application
Interface used by delivery workers to:

- Register on the platform
- View insurance coverage
- Track claims and payouts
- Manage subscriptions

---

### Frontend Layer

Built using **React.js**.

Responsibilities:

- Worker dashboard
- Policy management UI
- Claim history display
- Payment management

---

### Backend API Layer

Built using **Node.js / FastAPI**.

Responsibilities:

- Worker authentication
- Policy creation
- Premium calculation
- Claim triggering
- API integrations
- Payment processing

---

### AI Intelligence Layer

Handles all machine learning operations.

Includes:

**Risk Prediction Model**
- Calculates disruption probability for each zone.

**Dynamic Pricing Model**
- Adjusts weekly premiums.

**Fraud Detection Model**
- Detects GPS spoofing or duplicate claims.

---

### Data Layer

PostgreSQL database storing:

- Worker profiles
- Insurance policies
- Risk scores
- Claim records
- Payment history

---

### External Data Integrations

GigShield relies on real-time data feeds from external APIs.

These include:

Weather Data  
OpenWeather API

Air Quality Monitoring  
AQI APIs

Traffic Disruption Data  
Google Maps API

Payment Processing  
Razorpay / Stripe sandbox

Government Alerts  
Public disaster and restriction notifications

---

This architecture enables **fully automated parametric insurance payouts**, ensuring rapid claim processing and minimal manual intervention.


---

# Team

Team Name: (Your Team Name)

Members:

- ARIJIT DAS
- SOURASHIS SABUD
- SANSKRITI RANJAN
- SHIVANSH DHINGRA

---

# License

Developed for Guidewire DEVTrails 2026 Hackathon
