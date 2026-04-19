# Tenqiva Website

Static website for [tenqiva.com](https://tenqiva.com) — hosted on GitHub Pages.

## Setup

### 1. Configure your details

```bash
cp .env.example .env
```

Open `.env` and fill in your company details:

```
COMPANY_NAME=Tenqiva Private Limited
CIN=U72900DL2026PTC000000
GSTIN=07AABCT0000A1Z0
PHONE=9876543210
ADDRESS=123 Main Street, Sector 5
CITY_STATE_PIN=New Delhi, Delhi, 110001
FULL_ADDRESS=123 Main Street, Sector 5, New Delhi, Delhi, 110001
CITY=New Delhi
GRIEVANCE_OFFICER=Sanjeev Goyal
```

### 2. Build the site

```bash
python build.py
```

This reads your `.env`, replaces placeholders in `src/` templates, and outputs the final HTML to `docs/`.

### 3. Preview locally

Open `docs/index.html` in your browser to preview.

## Deploy to GitHub Pages

### First time setup

1. **Create a GitHub repository:**
   - Go to [github.com/new](https://github.com/new)
   - Name it `tenqiva_website` (or any name)
   - Keep it **Public** (required for free GitHub Pages)
   - Click **Create repository**

2. **Push your code:**
   ```bash
   cd tenqiva_website
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/tenqiva_website.git
   git push -u origin main
   ```

3. **Enable GitHub Pages:**
   - Go to your repo → **Settings** → **Pages** (in left sidebar)
   - Under **Source**, select **Deploy from a branch**
   - Branch: **main**, Folder: **/docs**
   - Click **Save**
   - Wait 1-2 minutes, your site will be live at `https://YOUR_USERNAME.github.io/tenqiva_website/`

4. **Connect your custom domain (tenqiva.com):**
   - In the same **Settings → Pages** section, under **Custom domain**, enter `tenqiva.com` and click **Save**
   - Check **Enforce HTTPS**
   - Add these DNS records at your domain registrar:

     | Type  | Name | Value                              |
     |-------|------|------------------------------------|
     | A     | @    | 185.199.108.153                    |
     | A     | @    | 185.199.109.153                    |
     | A     | @    | 185.199.110.153                    |
     | A     | @    | 185.199.111.153                    |
     | CNAME | www  | YOUR_USERNAME.github.io            |

   - DNS may take up to 24 hours to propagate

### Updating the site

```bash
# Edit your .env or src/ templates
python build.py
git add .
git commit -m "Update site"
git push
```

GitHub Pages will automatically redeploy within a minute.

## Project Structure

```
├── src/              # HTML templates (with {{PLACEHOLDER}} tokens)
│   ├── index.html
│   ├── pricing.html
│   ├── privacy.html
│   ├── terms.html
│   └── refund.html
├── docs/             # Built site (served by GitHub Pages)
│   ├── CNAME
│   ├── index.html
│   ├── pricing.html
│   ├── privacy.html
│   ├── terms.html
│   └── refund.html
├── .env.example      # Template for your details
├── .env              # Your actual details (gitignored)
├── build.py          # Build script
└── README.md
```
