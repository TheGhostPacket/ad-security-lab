# 🚀 Deployment Guide - AD Security Lab

This guide covers deploying the AD Security Lab to various platforms.

## 📋 Table of Contents

- [Local Development](#local-development)
- [Deploy to Render](#deploy-to-render)
- [Deploy to Heroku](#deploy-to-heroku)
- [Deploy to Railway](#deploy-to-railway)
- [Environment Variables](#environment-variables)

---

## 🏠 Local Development

### Setup
```bash
# Clone repository
git clone https://github.com/TheGhostPacket/ad-security-lab.git
cd ad-security-lab

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### Access
Navigate to `http://localhost:5000` in your browser.

---

## 🌐 Deploy to Render (Recommended - Free Tier)

### Prerequisites
- GitHub account
- Render account (free)

### Steps

1. **Push to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/ad-security-lab.git
git push -u origin main
```

2. **Create `render.yaml` in project root**
```yaml
services:
  - type: web
    name: ad-security-lab
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

3. **Deploy on Render**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Use these settings:
     - **Name**: `ad-security-lab`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Instance Type**: `Free`
   - Click "Create Web Service"

4. **Access Your App**
   - Your app will be available at: `https://ad-security-lab.onrender.com`
   - Initial deploy takes 2-3 minutes

### Notes
- Free tier may sleep after 15 minutes of inactivity
- First request after sleep takes 30-60 seconds to wake up

---

## 🟣 Deploy to Heroku

### Prerequisites
- Heroku account
- Heroku CLI installed

### Steps

1. **Create `Procfile` in project root**
```
web: gunicorn app:app
```

2. **Login to Heroku**
```bash
heroku login
```

3. **Create Heroku App**
```bash
heroku create ad-security-lab
```

4. **Deploy**
```bash
git push heroku main
```

5. **Open App**
```bash
heroku open
```

### Useful Commands
```bash
# View logs
heroku logs --tail

# Restart app
heroku restart

# Scale dynos
heroku ps:scale web=1
```

---

## 🚂 Deploy to Railway

### Prerequisites
- Railway account (free)
- GitHub repository

### Steps

1. **Go to Railway**
   - Visit [railway.app](https://railway.app)
   - Sign in with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your `ad-security-lab` repository

3. **Configure Build**
   - Railway auto-detects Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Add environment variable:
     - `PORT`: `5000`

4. **Generate Domain**
   - Go to Settings → Domains
   - Click "Generate Domain"

5. **Deploy**
   - Railway automatically deploys on push to main branch

---

## ⚙️ Environment Variables

### Required Variables
- `PORT`: Port number (default: 5000)

### Optional Variables for Production
```bash
# Flask Configuration
FLASK_ENV=production
SECRET_KEY=your-secret-key-here

# Gunicorn Configuration  
WEB_CONCURRENCY=2
```

### Setting Environment Variables

**Render:**
```bash
# In Render Dashboard → Environment → Add Environment Variable
```

**Heroku:**
```bash
heroku config:set FLASK_ENV=production
```

**Railway:**
```bash
# In Railway Dashboard → Variables → New Variable
```

---

## 🔒 Production Checklist

Before deploying to production:

- [ ] Set `FLASK_ENV=production`
- [ ] Generate and set strong `SECRET_KEY`
- [ ] Disable debug mode
- [ ] Set up proper logging
- [ ] Configure gunicorn workers
- [ ] Add rate limiting (optional)
- [ ] Set up monitoring (optional)

---

## 🐛 Troubleshooting

### App Won't Start
```bash
# Check logs
heroku logs --tail  # Heroku
# or check Render/Railway dashboard logs
```

### Port Issues
Make sure your app uses the PORT environment variable:
```python
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

### Dependencies Not Installing
Ensure `requirements.txt` is in root directory and properly formatted.

---

## 📊 Performance Tips

### Optimize for Free Tier

1. **Keep App Active** (Render/Heroku)
   - Use [UptimeRobot](https://uptimerobot.com/) to ping your app every 5 minutes
   - Prevents sleep on free tier

2. **Reduce Cold Start Time**
   - Minimize dependencies
   - Use lightweight libraries

3. **Caching**
   - Implement caching for repeated calculations
   - Use in-memory storage for logs (already implemented)

---

## 🎉 Next Steps

After deployment:
1. Test all attack simulations
2. Check logs for errors
3. Share your live demo link
4. Add to your portfolio
5. Monitor performance

---

## 📞 Support

Having issues? 
- Check the [main README](README.md)
- Open an issue on GitHub
- Contact: contact@theghostpacket.com

---

Made with ❤️ by TheGhostPacket