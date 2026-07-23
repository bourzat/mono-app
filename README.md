# MONO - Performance & Multi-Sport Tracking Engine

MONO is a personal performance tracking app designed to aggregate multi-sport endurance training data (runs, cycles, swims, and workouts), compute custom athletic metrics, and provide centralized athletic analytics.

---

## 🏗️ System Architecture

MONO is built modularly with a pipeline-first architecture:

1. **Ingestion Layer**: Connects to third-party fitness APIs (Strava) with automated OAuth 2.0 token management.
2. **Persistence Layer**: Stores structured activity data locally for offline analytics and fast querying.
3. **Analytics Engine**: Processes raw telemetry into actionable performance insights.

---

## 🚀 Current Status (Phase 1 Complete)

- [x] **Strava Data Pipeline**: Automated OAuth 2.0 token rotation (`refresh_token` workflow) and REST API integration.
- [ ] **Data Persistence**: Local database storage and schema design.
- [ ] **Telemetry Processing**: Data parsing, distance/time conversions, and sport filtering.
- [ ] **API & Dashboard Interface**: Centralized backend endpoints and user analytics.

---

## 🛠️ Local Development Setup

### 1. Environment Setup

```bash
git clone [https://github.com/YOUR_USERNAME/mono-app.git](https://github.com/YOUR_USERNAME/mono-app.git)
cd mono-app

# Create and activate virtual environment
python3 -m venv mono
source mono/bin/activate

# Install dependencies
pip install requests python-dotenv
