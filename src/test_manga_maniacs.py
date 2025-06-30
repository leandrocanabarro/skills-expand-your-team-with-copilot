#!/usr/bin/env python3
"""
Simple test to verify that Manga Maniacs activity was added correctly
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.database import activities_collection, init_database

def test_manga_maniacs_activity():
    """Test that Manga Maniacs activity exists and has correct properties"""
    
    # Initialize database
    init_database()
    
    # Find Manga Maniacs activity
    manga_activity = activities_collection.find_one({"_id": "Manga Maniacs"})
    
    assert manga_activity is not None, "Manga Maniacs activity not found"
    
    # Check required properties
    expected_props = {
        "description": "Explore the fantastic stories of the most interesting characters from Japanese Manga (graphic novels).",
        "schedule": "Tuesdays, 7:00 PM - 8:30 PM",
        "max_participants": 15,
        "participants": []
    }
    
    for prop, expected_value in expected_props.items():
        actual_value = manga_activity.get(prop)
        assert actual_value == expected_value, f"Property {prop}: expected {expected_value}, got {actual_value}"
    
    # Check schedule details
    schedule_details = manga_activity.get("schedule_details", {})
    assert schedule_details.get("days") == ["Tuesday"], f"Expected days ['Tuesday'], got {schedule_details.get('days')}"
    assert schedule_details.get("start_time") == "19:00", f"Expected start_time '19:00', got {schedule_details.get('start_time')}"
    assert schedule_details.get("end_time") == "20:30", f"Expected end_time '20:30', got {schedule_details.get('end_time')}"
    
    print("✅ All tests passed! Manga Maniacs activity added successfully.")
    return True

if __name__ == "__main__":
    test_manga_maniacs_activity()