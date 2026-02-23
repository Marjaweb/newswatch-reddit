# NewsWatch - 100% Free Automated Reddit Fetch

Your existing `fetch_reddit_posts.py` script works perfectly - it uses Reddit's public JSON endpoint (no API keys needed!). This GitHub Actions setup runs it automatically every Monday.

## 🎉 Warum dein Code besser ist

Du hast **Reddit's öffentliches JSON-Endpoint** genutzt:
```
https://www.reddit.com/r/{subreddit}/top/.json
```

Das braucht:
- ❌ Keine API-Keys
- ❌ Keine Genehmigung
- ❌ Keine Kosten
- ✅ Funktioniert einfach!

## 🚀 Setup (2 Minuten)

### Schritt 1: GitHub Repository erstellen

1. Gehe zu https://github.com/new
2. Repository Name: `newswatch`
3. **Public** (für kostenlose GitHub Actions)
4. "Create repository"

### Schritt 2: Dateien hochladen

Lade alle Dateien aus diesem Ordner hoch:

```
newswatch/
├── .github/workflows/weekly-fetch.yml
├── scripts/fetch_reddit_posts.py
├── subreddits.txt
├── prompts/analysis_prompt.txt
├── data/
└── requirements.txt
```

**Einfachster Weg:** Drag & Drop den ganzen Ordner in GitHub's Web-Interface.

### Schritt 3: Fertig!

Keine Secrets, keine API-Keys, keine Konfiguration. Einfach hochladen und los.

## ✅ Sofort testen

1. Gehe zu **Actions** Tab
2. Klick "Weekly NewsWatch - Fetch Reddit Posts"
3. Klick "Run workflow" (Dropdown rechts oben)
4. Klick grünen "Run workflow" Button
5. Warte 1-2 Minuten
6. Scroll runter zu **Artifacts**
7. Download `weekly-reddit-posts.zip`
8. Entpacken → `posts.json`

## 📥 Dein wöchentlicher Workflow (2 Minuten)

**Jeden Montag:**

1. **Posts herunterladen** (30 Sekunden)
   - GitHub → Actions → Neuester Run
   - Download `weekly-reddit-posts.zip`
   - Entpacken → `posts.json`

2. **Digest generieren mit mir (Claude)** (60 Sekunden)
   - Gehe zu claude.ai
   - Sage: "Hi Claude! Bitte erstelle meinen NewsWatch Digest für diese Woche"
   - Lade `posts.json` hoch
   - Ich generiere `digest.json` sofort
   - Download beide Dateien

3. **Upload zu Lovable** (30 Sekunden)
   - Beide Dateien in `/public` hochladen
   - Fertig!

## 🎯 Schneller Prompt für mich

Wenn du `posts.json` hast, paste das in claude.ai:

```
Hi Claude! Hier sind meine wöchentlichen Reddit-Posts.

Bitte analysiere sie und erstelle eine digest.json mit genau 7 Trends 
auf Englisch, basierend auf der analysis_prompt.txt die du kennst.

Stelle sicher:
- generated_at = heutiges Datum (YYYY-MM-DD)
- week_of = Montag dieser Woche (YYYY-MM-DD)
- Alle Texte auf Englisch

Hier sind die Posts: [posts.json hochladen]
```

Ich generiere dir die komplette `digest.json` in Sekunden.

## 💰 Kosten

| Service | Kosten |
|---------|--------|
| GitHub Actions | €0 (öffentliche Repos) |
| Reddit (öffentliches JSON) | €0 |
| Claude.ai (mich) | €0 |
| **Gesamt** | **€0.00/Woche** |

## 🔧 Anpassungen

### Andere Subreddits

Bearbeite `subreddits.txt`:
```
# Deine Subreddits hier
YourSubreddit
AnotherOne
```

### Anderer Zeitplan

Bearbeite `.github/workflows/weekly-fetch.yml`:
```yaml
schedule:
  - cron: '0 6 * * 1'  # Montag 6 Uhr UTC
  # Ändere zu: '0 18 * * 5' für Freitag 18 Uhr UTC
```

Cron Format: `minute hour day-of-month month day-of-week`

## 🛠 Wie es funktioniert

```
Jeden Montag 6 Uhr UTC:
  ↓
GitHub Actions startet
  ↓
Führt dein fetch_reddit_posts.py aus
  ↓
Nutzt: https://www.reddit.com/r/{sub}/top/.json?t=week&limit=50
  ↓
Speichert posts.json
  ↓
Du lädst herunter + gibst mir die Posts
  ↓
Ich generiere digest.json
  ↓
Du lädst beide in Lovable hoch
```

**Gesamtaufwand: 2 Minuten pro Woche**

## 🐛 Troubleshooting

**Workflow schlägt fehl:**
- Prüfe Actions Logs
- Stelle sicher Repository ist Public
- Reddit könnte rate-limiting haben (selten)

**Keine posts.json:**
- Hast du "Run workflow" geklickt?
- Prüfe ob es Montag ist (oder manuell getriggert)

## ⚡ Option B (Referenz)

Falls du doch API wolltest (NICHT empfohlen, da dein Code besser ist):
- Web Scraping mit Selenium/Puppeteer
- Komplexer, anfälliger für Blockierung
- Gegen Reddit's TOS

Dein JSON-Endpoint-Ansatz ist die **beste Lösung**.

---

**Das war's!** Dein Code funktioniert perfekt. GitHub Actions macht es wöchentlich automatisch. Du lädst Posts herunter, gibst sie mir, ich generiere den Digest, du lädst in Lovable hoch. **Komplett kostenlos.**
