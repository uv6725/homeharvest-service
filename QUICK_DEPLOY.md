# 🚀 Quick Deploy Guide - 5 Minutes to Online

## Fastest Way: Railway (Recommended)

### Step 1: Push to GitHub (2 min)

```bash
cd C:\Users\uv672\homeharvest-service

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Ready for deployment"

# Create a repo on GitHub.com, then:
git remote add origin https://github.com/YOUR_USERNAME/homeharvest-service.git
git push -u origin main
```

### Step 2: Deploy on Railway (2 min)

1. Go to **[railway.app](https://railway.app)** and sign up with GitHub
2. Click **"New Project"** → **"Deploy from GitHub repo"**
3. Select your **homeharvest-service** repository
4. Railway auto-detects Python and deploys
5. Wait for deployment (about 2 minutes)

### Step 3: Get Your URL (1 min)

- Railway gives you a URL like: `https://homeharvest-service-production-xxxx.up.railway.app`
- Click to copy your public URL

### Step 4: Test It!

Open in browser or test with curl:
```bash
curl https://your-railway-url.railway.app/health
```

You should see:
```json
{
  "status": "healthy"
}
```

**Done! Your API is now online! 🎉**

---

## Using Your API in Your App

Once deployed, you'll get a URL like:
- Railway: `https://your-app.railway.app`

### Example JavaScript:
```javascript
const response = await fetch('https://your-app.railway.app/property', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    address: '123 Main St, San Diego, CA',
    zip: '92104'
  })
});
const data = await response.json();
```

### Example Python:
```python
import requests

response = requests.post(
    'https://your-app.railway.app/property',
    json={'address': '123 Main St, San Diego, CA', 'zip': '92104'}
)
print(response.json())
```

