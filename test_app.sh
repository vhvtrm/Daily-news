#!/bin/bash
# Test script for Vietnam Stock Market News Collector

echo "=== Vietnam Stock Market News Collector - Test Suite ==="
echo ""

echo "Step 1: Generating 100 sample news items..."
python main.py --generate 100
echo ""

echo "Step 2: Showing database statistics..."
python main.py --stats
echo ""

echo "Step 3: Displaying first 15 news items..."
python main.py --show --limit 15
echo ""

echo "Step 4: Searching for VNM ticker..."
python main.py --ticker VNM
echo ""

echo "Step 5: Showing dividend news..."
python main.py --category "CỔ TỨC"
echo ""

echo "Step 6: Exporting to file..."
python main.py --export test_export.txt --limit 30
echo "Created: test_export.txt"
echo ""

echo "Step 7: Testing import functionality..."
python main.py --db test_import.db --import sample_news_input.txt
python main.py --db test_import.db --stats
echo ""

echo "=== All tests completed! ==="
echo ""
echo "Files generated:"
echo "  - vietnam_news.db (main database with 100 items)"
echo "  - test_export.txt (exported news file)"
echo "  - test_import.db (imported news database)"
