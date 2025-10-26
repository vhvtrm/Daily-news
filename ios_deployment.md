# Deploy Vietnam Stock Market News to iOS via Pythonista

This guide will help you run the Vietnam Stock Market News app on your iPhone/iPad using Pythonista.

## What is Pythonista?

Pythonista is a complete Python IDE for iOS that allows you to run Python scripts on your iPhone or iPad.

- **App Store Link**: https://apps.apple.com/app/pythonista-3/id1085978097
- **Price**: $9.99 (one-time purchase)
- **Requirements**: iOS 15.0 or later

## Step-by-Step Installation

### Step 1: Install Pythonista

1. Open the App Store on your iPhone/iPad
2. Search for "Pythonista 3"
3. Purchase and install the app ($9.99)

### Step 2: Transfer Files to iOS

You have several options to transfer the app files:

#### Option A: Via iCloud (Recommended)

1. On your computer, compress the Daily-news folder:
   ```bash
   zip -r daily-news-ios.zip *.py requirements.txt sample_news_input.txt
   ```

2. Upload `daily-news-ios.zip` to your iCloud Drive

3. On your iPhone/iPad:
   - Open Pythonista
   - Tap the wrench icon (⚙️) > External Files > iCloud Drive
   - Navigate to the zip file and extract it

#### Option B: Via GitHub

1. Open Safari on your iPhone/iPad
2. Go to your GitHub repository
3. Copy the raw URL of each Python file
4. In Pythonista:
   - Tap the "+" icon to create a new file
   - Paste the code from GitHub
   - Save with the correct filename

#### Option C: Via Copy-Paste

1. Open each .py file on your computer
2. Copy the entire content
3. On your iPhone/iPad in Pythonista:
   - Create a new file with the same name
   - Paste the code
   - Save

### Step 3: Install Required Files

Transfer these files to Pythonista:
- ✅ `models.py`
- ✅ `database.py`
- ✅ `news_collector.py`
- ✅ `news_formatter.py`
- ✅ `sample_data.py`
- ✅ `main_ios.py` (iOS-optimized version - see below)
- ⚠️ `sample_news_input.txt` (optional)

### Step 4: Run the App

1. Open Pythonista
2. Navigate to your files
3. Tap on `main_ios.py`
4. Tap the ▶️ (play) button at the top

## Using the iOS Version

The iOS version provides a simple menu interface:

```
=== VIETNAM STOCK MARKET NEWS ===
1. Generate 100 news
2. Show all news
3. Show 20 news
4. Search by ticker
5. Export to file
6. Show stats
0. Exit

Choose option:
```

### Example Usage:

**Generate News:**
- Choose option 1
- Wait for generation to complete
- News will be saved to database

**View News:**
- Choose option 2 or 3
- News will display in the console with URLs

**Search by Ticker:**
- Choose option 4
- Enter ticker symbol (e.g., VNM, HPG, TCB)
- Results will display

**Export:**
- Choose option 5
- File will be saved in Pythonista's directory
- Access via Files app or share

## File Locations in Pythonista

All files are stored in:
```
Pythonista 3/Documents/
```

You can access them via:
- Pythonista's file browser
- iOS Files app
- Share to other apps

## Tips for iOS Usage

### 1. Database Location
The SQLite database (`vietnam_news.db`) is automatically created in Pythonista's Documents folder.

### 2. Viewing Exported Files
- Tap the folder icon in Pythonista
- Find your `.txt` export files
- Tap to view or share

### 3. Sharing Output
- After exporting, tap the share icon
- Share via Messages, Email, Notes, etc.

### 4. Shortcuts Integration
You can create iOS Shortcuts to run the app:
1. Open Shortcuts app
2. Create new shortcut
3. Add "Run Python Script" action
4. Select your Pythonista script

### 5. Widget Support
Add Pythonista widget to your home screen for quick access.

## Limitations on iOS

⚠️ **Things that work differently:**
- File paths use Pythonista's sandbox
- No command-line arguments (use menu instead)
- Limited background execution
- Cannot install pip packages (use built-in only)

✅ **Things that work perfectly:**
- SQLite database
- All core functionality
- News generation
- Search and filter
- Export to files

## Troubleshooting

### "Module not found" error
- Ensure all .py files are in the same directory
- Check file names are correct (case-sensitive)

### Database errors
- Pythonista has full SQLite support
- Check write permissions
- Ensure enough storage space

### Export file not found
- Files are saved in Pythonista's Documents folder
- Use the folder icon to browse files

### Performance issues
- Generating 100 news items works fine
- Close other apps for better performance
- Restart Pythonista if needed

## Alternative: Pythonista UI Version

For a better iOS experience, you can use the UI version (coming soon) which includes:
- Native iOS interface
- Tap-friendly buttons
- Swipe gestures
- Share sheet integration

## Next Steps

Once you have the app running:
1. Generate your first 100 news items
2. Export to a text file
3. Share the file via Messages or Email
4. Set up iOS Shortcuts for automation

## Support

For issues specific to:
- **Pythonista app**: https://omz-software.com/pythonista/
- **This app**: Check the main README.md

---

Enjoy reading Vietnam stock market news on your iPhone! 📱📈
