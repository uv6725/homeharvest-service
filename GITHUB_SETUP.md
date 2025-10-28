# GitHub Setup Guide

## Step 1: Create a GitHub Repository (Browser)

1. Go to **[github.com](https://github.com)**
2. Click the **"+"** in the top right → **"New repository"**
3. Name it: `homeharvest-service`
4. Make it **Public** (or Private if you prefer)
5. **DO NOT** initialize with README, .gitignore, or license
6. Click **"Create repository"**

## Step 2: Create a Personal Access Token

1. Go to GitHub Settings → **[Developer settings](https://github.com/settings/tokens)**
2. Click **"Personal access tokens"** → **"Tokens (classic)"**
3. Click **"Generate new token"** → **"Generate new token (classic)"**
4. Name it: `homeharvest-deployment`
5. Check these permissions:
   - ✅ `repo` (Full control of private repositories)
6. Click **"Generate token"** at bottom
7. **COPY THE TOKEN NOW** (you won't see it again!)
   - It looks like: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

## Step 3: Set up Git and Push

Open PowerShell in the project directory and run:

```powershell
cd C:\Users\uv672\homeharvest-service

# Initialize git
git init

# Configure your name and email (use your GitHub email)
git config user.name "Your Name"
git config user.email "your-email@example.com"

# Add all files
git add .

# Commit
git commit -m "Initial commit - HomeHarvest API"

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/homeharvest-service.git

# Push (this is where you'll use your token!)
git push -u origin main
```

**When prompted for username/password:**
- **Username:** Your GitHub username
- **Password:** **PASTE YOUR PERSONAL ACCESS TOKEN** (from Step 2)

---

## Alternative: Use GitHub Desktop (Easier!)

If you prefer a GUI:

1. Download **[GitHub Desktop](https://desktop.github.com/)**
2. Sign in with your GitHub account
3. File → Add Local Repository
4. Select: `C:\Users\uv672\homeharvest-service`
5. Click "Publish repository"
6. Done!

---

## Troubleshooting

### "Permission denied" error
- Make sure you're using the **Personal Access Token** as password, not your GitHub password
- Token might be expired - generate a new one

### "Repository not found" error
- Check that the repository exists on GitHub
- Verify the URL in `git remote -v`

### Authentication issues
- Clear stored credentials: Windows → Credential Manager → Windows Credentials → Find github.com → Remove
- Try again with fresh credentials

---

## Quick Commands Reference

```bash
# Check if connected
git remote -v

# Add changes
git add .

# Commit changes
git commit -m "Your message"

# Push to GitHub
git push

# Pull from GitHub
git pull
```

