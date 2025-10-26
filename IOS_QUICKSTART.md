# iOS Quick Start Guide - 5 Minutes to News!

Get Vietnam Stock Market News running on your iPhone in just 5 minutes!

## Method 1: Quick Copy-Paste (Easiest - 5 min)

### Step 1: Get Pythonista
1. Download "Pythonista 3" from App Store ($9.99)
2. Open the app

### Step 2: Copy Files
You need to copy 6 files to Pythonista. Here's how:

**On your computer:**
1. Go to your GitHub repository
2. For each file below, click on it, then click "Raw"
3. Copy the entire content

**On your iPhone/iPad:**
1. Open Pythonista
2. Tap the "📄" icon (top right)
3. Tap "+" to create new file
4. Paste the code
5. Name it exactly as shown below
6. Tap "Done"

**Files to copy (in this order):**
1. ✅ `models.py`
2. ✅ `database.py`
3. ✅ `news_collector.py`
4. ✅ `news_formatter.py`
5. ✅ `sample_data.py`
6. ✅ `main_ios.py`

### Step 3: Run!
1. Tap on `main_ios.py`
2. Tap the ▶️ play button
3. Choose option "1" to generate 100 news
4. Choose option "2" or "3" to view news

**Done! 🎉**

---

## Method 2: Via iCloud (Faster if on Mac)

### On your Mac:
```bash
cd Daily-news
zip -r vietnam-news-ios.zip *.py
```

### On your iPhone/iPad:
1. Upload zip to iCloud Drive
2. Open Pythonista
3. Tap ⚙️ wrench icon > External Files > iCloud
4. Find and extract the zip file
5. Run `main_ios.py`

---

## Method 3: All-in-One File (Single File - Coming Soon)

We're creating a single-file version that contains everything in one file for even easier deployment!

---

## What You'll See

```
=== VIETNAM STOCK MARKET NEWS ===
1. Generate 100 news items
2. Show all news
3. Show 20 most recent news
4. Search by ticker symbol
5. Show by category
6. Export to file
7. Show statistics
8. Clear database
0. Exit
===================================
Choose option:
```

## Quick Commands

| What you want | Choose |
|---------------|--------|
| Generate fresh news | 1 |
| See all news | 2 |
| See top 20 | 3 |
| Search VNM stock | 4, then type "VNM" |
| Export to file | 6 |
| See statistics | 7 |

## Viewing Exported Files

After exporting (option 6):
1. Open Files app on iOS
2. Go to Pythonista 3 > Documents
3. Find your .txt file
4. Tap to view or share

## Tips

💡 **First Time**: Choose option 1 to generate 100 news items
💡 **Quick View**: Option 3 shows just 20 items (faster)
💡 **Share**: Export to file (option 6), then share via Messages/Email
💡 **Clean Start**: Option 8 clears database to start fresh

## Troubleshooting

**"No module named 'models'"**
- Make sure all 6 files are in the same folder in Pythonista

**Can't find exported file**
- Files are in: Pythonista 3/Documents/
- Access via Files app

**App crashes**
- Restart Pythonista
- Make sure you have iOS 15+

## Next Steps

Once running:
1. ✅ Generate 100 news (option 1)
2. ✅ View them (option 2 or 3)
3. ✅ Search by ticker (option 4)
4. ✅ Export to share (option 6)

**Enjoy your Vietnam stock market news on the go! 📱📈**

---

Need help? Check the full guide: `ios_deployment.md`
