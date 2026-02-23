# NewsWatch 📰

**Automated weekly internet culture digest powered by Reddit trends**

A fully automated newsletter that surfaces the most culturally significant moments from the internet each week. Zero manual work after setup.

## 🌟 Features

- **100% Free** - No API costs, no subscriptions
- **Fully Automated** - Runs every Monday at 6 AM UTC
- **No API Keys** - Uses Reddit's public JSON endpoint
- **7 Weekly Trends** - Auto-curated from 11+ subreddits
- **Auto-Generated Summaries** - Claude writes the digest
- **Beautiful UI** - Modern, responsive design with dark mode

## 🚀 Quick Start

### 1. Fork This Repository

Click the "Fork" button at the top right of this page.

### 2. Enable GitHub Actions

1. Go to the **Actions** tab in your forked repo
2. Click "I understand my workflows, go ahead and enable them"

### 3. Test It Now

1. Go to **Actions** tab
2. Click "Weekly NewsWatch - Fetch Reddit Posts" on the left
3. Click "Run workflow" dropdown (top right)
4. Click green "Run workflow" button
5. Wait 1-2 minutes
6. Scroll down to **Artifacts**
7. Download `weekly-reddit-posts.zip`
8. Extract → `posts.json`

**That's it!** You now have this week's Reddit posts.

## 📥 Weekly Workflow (2 minutes)

Every Monday morning:

### Step 1: Download Posts (30 seconds)
- GitHub → Actions → Latest workflow run
- Download `weekly-reddit-posts.zip`
- Extract → `posts.json`

### Step 2: Generate Digest (60 seconds)
- Go to [claude.ai](https://claude.ai)
- Paste this prompt:
  ```
  Hi Claude! I have my weekly Reddit posts. Please analyze them and create 
  a digest.json file with exactly 7 English trends.
  
  Follow these rules:
  - Use the analysis_prompt.txt format
  - Generate trend names, explanations, and "why viral" in English
  - Include an auto-written editors_note (2-3 sentences about this week's vibe)
  - Set generated_at to today's date (YYYY-MM-DD)
  - Set week_of to this Monday's date (YYYY-MM-DD)
  
  Here are the posts: [upload or paste posts.json]
  ```
- Claude generates `digest.json` instantly
- Download both files

### Step 3: Deploy (30 seconds)
- Upload `digest.json` and `posts.json` to your website
- Or use with our [Lovable.ai template](https://lovable.ai) (instructions below)

**Total time: 2 minutes per week**

## 🎨 Using the Website Template

We provide a complete website template built with React + Tailwind.

### Option 1: Deploy to Lovable.ai (Easiest)

1. Go to [lovable.ai](https://lovable.ai)
2. Create a new project
3. Paste the build prompt from `docs/LOVABLE_PROMPT.md`
4. Upload `digest.json` and `posts.json` to `/public` folder
5. Done! Your site is live

### Option 2: Deploy to Vercel/Netlify

1. Use the code in `/frontend` directory
2. Deploy to Vercel or Netlify
3. Add `digest.json` and `posts.json` to `/public`
4. Configure your deployment

## 🛠 Customization

### Change Subreddits

Edit `subreddits.txt`:

```
# Your subreddits here (one per line)
YourSubreddit
AnotherOne
ThirdOne
```

### Change Schedule

Edit `.github/workflows/weekly-fetch.yml`:

```yaml
schedule:
  - cron: '0 6 * * 1'  # Monday 6 AM UTC
  # Change to: '0 18 * * 5' for Friday 6 PM UTC
```

Cron format: `minute hour day-of-month month day-of-week`

### Change Trend Count

Edit `prompts/analysis_prompt.txt`:

```
Include exactly 7 trend objects.
# Change 7 to any number
```

## 🏗 How It Works

```
Every Monday 6 AM UTC:
  ↓
GitHub Actions runs fetch_reddit_posts.py
  ↓
Fetches top posts from past week via public JSON endpoint
Example: https://www.reddit.com/r/TikTokCringe/top/.json?t=week&limit=50
  ↓
Saves posts.json as artifact
  ↓
You download and send to Claude
  ↓
Claude analyzes → generates digest.json with 7 trends
  ↓
You upload both to your website
```

**No Reddit API keys required!** We use Reddit's public JSON endpoint that requires no authentication.

## 📊 Data Structure

### posts.json
```json
[
  {
    "subreddit": "popculturechat",
    "title": "Post title here",
    "score": 89400,
    "url": "https://i.redd.it/...",
    "permalink": "/r/subreddit/comments/...",
    "author": "username",
    "num_comments": 1234,
    "created_utc": 1234567890
  }
]
```

### digest.json
```json
{
  "title": "Weekly Internet Culture Digest",
  "subtitle": "Week of Feb 17, 2026",
  "generated_at": "2026-02-17",
  "week_of": "2026-02-17",
  "editors_note": "Auto-written summary of the week's internet vibe",
  "trends": [
    {
      "id": 1,
      "name": "Trend Name",
      "status": "fire",
      "explanation": "What it is in 2-3 sentences",
      "why_viral": "Why it spread and what it says culturally",
      "post_permalinks": ["/r/sub/comments/..."]
    }
  ]
}
```

## 💰 Cost

| Service | Cost |
|---------|------|
| GitHub Actions | Free (2,000 min/month for public repos) |
| Reddit API | Free (public JSON endpoint) |
| Claude.ai | Free (with usage limits) |
| **Total** | **$0.00/week** |

## 🔒 Privacy & Rate Limits

- **No authentication required** - Uses public data only
- **2-second delay between requests** - Respects Reddit's servers
- **User-Agent included** - Identifies our bot properly
- **Top 100 posts only** - Keeps requests minimal

## 🐛 Troubleshooting

**Workflow fails:**
- Check Actions logs for error message
- Verify repository is public (required for free Actions)
- Reddit may be rate-limiting (very rare)

**No posts.json generated:**
- Did you click "Run workflow"?
- Check if it's Monday (or manually triggered)
- Review workflow logs in Actions tab

**Claude errors:**
- Make sure you're uploading valid posts.json
- Check that file isn't empty
- Verify JSON format is correct

## 📝 Example Subreddits

Default subreddits tracked (edit `subreddits.txt` to customize):

- **Viral Content**: TikTokCringe, Damnthatsinteresting, meirl
- **Culture**: OutOfTheLoop, InternetIsBeautiful, MemeEconomy, popculturechat
- **Fashion**: streetwear, malefashionadvice
- **Music**: Music, ListenToThis

## 🤝 Contributing

Contributions welcome! Feel free to:
- Add new subreddits to the default list
- Improve the analysis prompt
- Enhance the website template
- Fix bugs or add features

## 📄 License

MIT License - feel free to use this for your own projects!

## 🙏 Acknowledgments

- **Reddit** for the public JSON endpoint
- **Anthropic** for Claude AI
- **GitHub** for free Actions

---

**Built with ❤️ for internet culture enthusiasts**

*Questions? [Open an issue](../../issues) or check the [discussions](../../discussions)*
