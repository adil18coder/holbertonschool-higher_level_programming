#!/usr/bin/env python3
"""
Generate invitation files from a template and attendee list.
"""

import os


def generate_invitations(template, attendees):
    # -----------------------------
    # 1. Validate input types
    # -----------------------------
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # -----------------------------
    # 2. Handle empty template
    # -----------------------------
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # -----------------------------
    # 3. Handle empty attendee list
    # -----------------------------
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # -----------------------------
    # 4. Process each attendee
    # -----------------------------
    for index, attendee in enumerate(attendees, start=1):
        # Safely fetch values, replace missing/None with "N/A"
        name = attendee.get("name") or "N/A"
        title = attendee.get("event_title") or "N/A"
        date = attendee.get("event_date") or "N/A"
        location = attendee.get("event_location") or "N/A"

        # Replace placeholders in template
        filled = (
            template.replace("{name}", name)
                    .replace("{event_title}", title)
                    .replace("{event_date}", date)
                    .replace("{event_location}", location)
        )

        # Output file name
        filename = f"output_{index}.txt"

        # Create file
        try:
            with open(filename, "w") as f:
                f.write(filled)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
            continue

    # Success message (optional for debugging)
    # print("Invitation files generated successfully.")
