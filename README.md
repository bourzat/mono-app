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
```

### 2. Configure Environment Variables

Create a `.env` file in the root directory:

```env
STRAVA_CLIENT_ID="your_client_id"
STRAVA_CLIENT_SECRET="your_client_secret"
STRAVA_REFRESH_TOKEN="your_refresh_token"
```
> **Note:** Do not commit the `.env` file to Git. Ensure `.env` is listed in `.gitignore`.

---

## 🏃 Usage

Run the automated ingestion pipeline to refresh tokens and fetch multi-sport activity data:

```bash
python strava_client.py

### Example Pipeline Output

```text
🔄 Requesting fresh access token from Strava...
✅ Success! Obtained fresh access token.

Successfully fetched 30 activities!
Latest Activity: [BASE] 23.2k | Loresho Loop | MTB 26er
Distance: 23240.6 m
```
## 🔒 Security & Best Practices

* **Zero-Commit Secrets**: All Client ID, Secret, and OAuth Refresh tokens are managed via isolated environment variables (`.env`).
* **Session Persistence**: Access tokens are dynamically requested per pipeline execution using programmatic refresh routines.

---

## 👨‍💻 Author

Built by **Ilyas Bourzat**
