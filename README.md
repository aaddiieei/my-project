# 🌧️ HydroSense Delhi
### AI + GIS Urban Flood Risk Prediction System

HydroSense is a **Machine Learning + GIS based platform** that predicts urban flood hotspots across Delhi using rainfall intensity, terrain elevation, and drainage capacity indicators.

The system generates **Ward-Level Readiness Scores** and visualizes risk on an interactive map to support **proactive disaster management**.

---



## ⚙️ How It Works

1. ML model predicts flood risk score (0–100)
2. Predictions exported as CSV file
3. Website reads CSV and plots hotspots on map
4. Ward readiness score calculated dynamically
5. SMS alerts sent using Twilio when risk exceeds threshold

---

## 🧠 ML Features Used

| Feature | Purpose |
|--------|--------|
| Rainfall | flood triggering factor |
| Elevation | identifies low-lying areas |
| Drainage capacity | measures infrastructure readiness |
| Urban density proxy | congestion impact |

---

## 🚨 Risk Categories

| Risk Level | Meaning |
|-----------|---------|
| 🔴 Critical | high probability of flooding |
| 🟠 High | waterlogging likely |
| 🟡 Moderate | possible accumulation |
| 🟢 Low | minimal risk |

---

## 📲 SMS Alert System

Python backend integrates **Twilio API** to broadcast alerts in high-risk situations.

Example alert:
> Flood Risk Alert: High waterlogging probability detected in Shahdara ward.

---

## 🛠 Tech Stack

**Frontend**
- HTML
- CSS
- JavaScript
- Leaflet.js
- OpenStreetMap

**Machine Learning**
- Python
- Pandas
- Scikit-learn

**Backend**
- Flask
- Twilio API

---

## 📂 Project Structure
# 🌧️ HydroSense Delhi
### AI + GIS Urban Flood Risk Prediction System

HydroSense is a **Machine Learning + GIS based platform** that predicts urban flood hotspots across Delhi using rainfall intensity, terrain elevation, and drainage capacity indicators.

The system generates **Ward-Level Readiness Scores** and visualizes risk on an interactive map to support **proactive disaster management**.

---



## ⚙️ How It Works

1. ML model predicts flood risk score (0–100)
2. Predictions exported as CSV file
3. Website reads CSV and plots hotspots on map
4. Ward readiness score calculated dynamically
5. SMS alerts sent using Twilio when risk exceeds threshold

---

## 🧠 ML Features Used

| Feature | Purpose |
|--------|--------|
| Rainfall | flood triggering factor |
| Elevation | identifies low-lying areas |
| Drainage capacity | measures infrastructure readiness |
| Urban density proxy | congestion impact |

---

## 🚨 Risk Categories

| Risk Level | Meaning |
|-----------|---------|
| 🔴 Critical | high probability of flooding |
| 🟠 High | waterlogging likely |
| 🟡 Moderate | possible accumulation |
| 🟢 Low | minimal risk |

---

## 📲 SMS Alert System

Python backend integrates **Twilio API** to broadcast alerts in high-risk situations.

Example alert:
> Flood Risk Alert: High waterlogging probability detected in Shahdara ward.

---

## 🛠 Tech Stack

**Frontend**
- HTML
- CSS
- JavaScript
- Leaflet.js
- OpenStreetMap

**Machine Learning**
- Python
- Pandas
- Scikit-learn

**Backend**
- Flask
- Twilio API

---
