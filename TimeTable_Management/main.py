import pandas as pd

# Sheet 1: Rooms Availability
rooms = {"Room Number": ["A101", "A102", "A103", "A104"],
         "Time Slot": ["9:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "12:00 - 1:00"],
         "Availability": ["Yes", "No", "Yes", "Yes"]}
df_rooms = pd.DataFrame(rooms)

# Sheet 2: Teacher Availability
teachers = {"Teacher Name": ["Dr. Smith", "Dr. Johnson", "Dr. Brown", "Dr. Davis"],
            "Time Slot": ["9:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "12:00 - 1:00"],
            "Availability": ["No", "Yes", "No", "Yes"]}
df_teachers = pd.DataFrame(teachers)

# Sheet 3: Subject Information
subjects = {"Subject Code": ["CSC101", "MAT101", "PHY101", "CHE101"],
            "Teacher Name": ["Dr. Smith", "Dr. Johnson", "Dr. Brown", "Dr. Davis"],
            "Room Number": ["A101", "A102", "A103", "A104"],
            "Time Slot": ["9:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00", "12:00 - 1:00"]}
df_subjects = pd.DataFrame(subjects)

# Sheet 4: Timetable
df_timetable = df_subjects.copy()
df_timetable["Availability"] = df_timetable.apply(lambda x: "Yes" if ((df_rooms["Availability"][df_rooms["Room Number"] == x["Room Number"]] == "Yes").bool() &
                                                                    (df_teachers["Availability"][df_teachers["Teacher Name"] == x["Teacher Name"]] == "Yes").bool())
                                                    else "No", axis=1)


# Generate Excel File
writer = pd.ExcelWriter("timetable.xlsx")
df_rooms.to_excel(writer, sheet_name="Rooms Availability", index=False)
df_teachers.to_excel(writer, sheet_name="Teacher Availability", index=False)
df_subjects.to_excel(writer, sheet_name="Subject Information", index=False)
df_timetable.to_excel(writer, sheet_name="Timetable", index=False)
writer.save()
