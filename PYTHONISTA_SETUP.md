# Complete Pythonista Setup Guide

## What is Pythonista?

Pythonista is a complete Python 3 development environment for iOS. It includes:
- ✅ Python 3.11
- ✅ Full standard library
- ✅ SQLite database support
- ✅ File management
- ✅ iOS integration (share sheet, notifications, etc.)

## Why Pythonista for This App?

Perfect for Vietnam Stock Market News because:
- ✅ **No server needed** - runs entirely on your iPhone
- ✅ **Offline capable** - works without internet after installation
- ✅ **Native SQLite** - full database support
- ✅ **File export** - easily share news via Messages, Email
- ✅ **Widgets** - can add to home screen
- ✅ **Shortcuts** - integrate with iOS automation

## Installation

### 1. Purchase Pythonista
- **App Store**: https://apps.apple.com/app/pythonista-3/id1085978097
- **Cost**: $9.99 (one-time, no subscription)
- **Size**: ~50MB
- **Requirements**: iOS 15.0+

### 2. File Transfer Options

#### Option A: GitHub to Pythonista (Recommended)

1. **On your iPhone**, open Safari
2. Go to your GitHub repo
3. For each .py file:
   - Tap the file
   - Tap "Raw" button
   - **Long press** anywhere on the code
   - Select "Select All"
   - Select "Copy"
4. Open Pythonista
5. Tap 📄 (files icon)
6. Tap + (new file)
7. **Long press** in editor
8. Tap "Paste"
9. Tap "⚙️" > "Rename" > Enter filename
10. Tap "Done"

Repeat for all 6 files:
- models.py
- database.py
- news_collector.py
- news_formatter.py
- sample_data.py
- main_ios.py

#### Option B: Via Working Copy App (Git Clone)

If you have Working Copy app:
1. Clone your repo in Working Copy
2. In Pythonista: ⚙️ > External Files > Working Copy
3. Navigate to your repo
4. Files are accessible

#### Option C: Via Computer & iCloud

**On computer:**
```bash
cd Daily-news
zip vietnam-news.zip models.py database.py news_collector.py news_formatter.py sample_data.py main_ios.py
```

Upload to iCloud Drive

**On iPhone:**
1. Pythonista: ⚙️ > External Files > iCloud Drive
2. Find zip file
3. Extract

## First Run

1. In Pythonista, find `main_ios.py`
2. Tap to open
3. Tap ▶️ (play button)
4. You'll see the menu

```
🇻🇳 VIETNAM STOCK MARKET NEWS
1. Generate 100 news items
2. Show all news
...
```

5. Type `1` and press Enter
6. Wait ~10 seconds for news generation
7. Type `3` to view 20 news items

## File Locations

Pythonista organizes files in:
```
Pythonista 3/
├── Documents/          ← Your app files go here
│   ├── main_ios.py
│   ├── models.py
│   ├── database.py
│   ├── news_collector.py
│   ├── news_formatter.py
│   ├── sample_data.py
│   ├── vietnam_news.db       (created automatically)
│   └── exported_news.txt     (after export)
└── site-packages/      ← External modules (not needed)
```

## Using the App

### Menu Options Explained

**1. Generate 100 news items**
- Creates fresh news in database
- Takes ~10-15 seconds
- Can run multiple times (adds to database)

**2. Show all news**
- Displays every news item
- Includes source URLs
- May be slow if 1000+ items

**3. Show 20 most recent news**
- ⚡ Faster option
- Perfect for quick check
- Shows newest first

**4. Search by ticker symbol**
- Enter: VNM, HPG, TCB, etc.
- Shows all news for that stock
- Case insensitive

**5. Show by category**
- Browse by type:
  - Enterprise news
  - Dividends
  - Market movements
  - etc.

**6. Export to file**
- Saves to .txt file
- Accessible via Files app
- Can share to other apps

**7. Show statistics**
- Total news count
- Breakdown by category
- Quick overview

**8. Clear database**
- Removes all news
- Fresh start
- Cannot undo!

## Viewing Exported Files

After choosing option 6:

1. **Open Files app** on iOS
2. Navigate: On My iPhone > Pythonista 3 > Documents
3. Find your .txt file
4. Tap to view
5. Tap share icon to send

## Sharing News

**Via Messages:**
1. Export (option 6)
2. Files app > your file
3. Share icon > Messages
4. Select contact

**Via Email:**
1. Export (option 6)
2. Files app > your file
3. Share icon > Mail
4. Compose email

**Via Notes:**
1. Export (option 6)
2. Files app > your file
3. Share icon > Notes
4. Choose note or create new

## Advanced: iOS Shortcuts Integration

Create a shortcut for one-tap news:

1. Open Shortcuts app
2. Create new shortcut
3. Add action: "Run Python Script"
4. Select Pythonista
5. Choose "main_ios.py"
6. Add to home screen

## Advanced: Home Screen Widget

1. Long press on home screen
2. Tap + (top left)
3. Find "Pythonista"
4. Choose widget size
5. Add widget
6. Configure to run main_ios.py

## Troubleshooting

### Module Not Found
**Problem:** "No module named 'models'"
**Solution:**
- Ensure all 6 .py files are in Documents folder
- Check filenames are exact (case-sensitive)
- Restart Pythonista

### Can't Find Database
**Problem:** No news showing after generation
**Solution:**
- Check option 7 (stats) to verify news count
- Database is in Documents/vietnam_news.db
- Try option 8 to clear and regenerate

### App Crashes
**Problem:** App stops unexpectedly
**Solution:**
- Close other apps
- Restart Pythonista
- Check iOS storage space
- Update to latest iOS

### Slow Performance
**Problem:** Takes too long to show news
**Solution:**
- Use option 3 instead of 2 (shows 20 instead of all)
- Close other apps
- If database has 10,000+ items, clear it (option 8)

### Export File Not Found
**Problem:** Can't find exported .txt file
**Solution:**
- Files app > On My iPhone > Pythonista 3 > Documents
- OR in Pythonista: tap 📄 icon to browse files
- Look for filename you entered

## Performance Tips

**Fast Loading:**
- Use option 3 (20 news) instead of 2 (all news)
- Export to file for offline reading

**Battery Saving:**
- Close app when not using
- Export to file and read in Notes app

**Storage:**
- Database grows ~100KB per 100 news items
- Clear old news periodically (option 8)
- Export before clearing to save

## Comparison: Pythonista vs Web App

| Feature | Pythonista | Web App |
|---------|-----------|---------|
| Cost | $9.99 one-time | Free |
| Internet Required | Only for install | Always |
| Speed | Very fast | Depends on connection |
| Offline | ✅ Yes | ❌ No |
| Data Privacy | ✅ Local only | Depends on hosting |
| iOS Integration | ✅ Full | ⚠️ Limited |
| Setup Complexity | Medium | Easy |

## FAQ

**Q: Do I need internet to use the app?**
A: Only for initial file transfer. After setup, works 100% offline.

**Q: Can I use it on iPad?**
A: Yes! Pythonista works on both iPhone and iPad.

**Q: Will it sync across devices?**
A: Not automatically. Use iCloud export/import for manual sync.

**Q: Can I add real news sources?**
A: Yes! Edit the code to add web scraping. See main README.md

**Q: Is my data safe?**
A: 100% local. Nothing leaves your device.

**Q: Can I automate daily news?**
A: Yes! Use iOS Shortcuts to schedule automatic runs.

## Next Steps

✅ Install Pythonista ($9.99)
✅ Copy 6 Python files
✅ Run main_ios.py
✅ Generate news (option 1)
✅ View news (option 3)
✅ Export and share (option 6)

**Enjoy Vietnam stock market news on your iPhone! 📱📈**

---

For more help:
- Quick Start: `IOS_QUICKSTART.md`
- Deployment Guide: `ios_deployment.md`
- Checklist: `IOS_CHECKLIST.txt`
