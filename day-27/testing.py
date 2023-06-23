import os
import tkinter as tk
import tkinter.filedialog as fd
import pandas as pd
# import googleapiclient.discovery


def rename_videos():
    # Get the path to the Excel sheet and the video directory from the GUI
    excel_path = excel_entry.get()
    video_dir = dir_entry.get()

    # Read the Excel sheet into a Pandas DataFrame
    df = pd.read_excel(excel_path)

    # Extract the YouTube URLs and new names from the DataFrame
    urls = df['URL']
    new_names = df['New Name']

    # Use the YouTube Data API to get the video titles
    api_key = 'your_api_key'
    # service = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

    # Iterate over the URLs and rename the corresponding video files
    for url, new_name in zip(urls, new_names):
        video_id = url.split('v=')[1]
        # request = service.videos().list(part='snippet', id=video_id)
        # response = request.execute()
        # video_title = response['items'][0]['snippet']['title']

        # Find the video file with the matching title
        for file in os.listdir(video_dir):
            if file.startswith(video_title):
                old_name = file
                break

        # Rename the file
        old_path = os.path.join(video_dir, old_name)
        new_path = os.path.join(video_dir, new_name)
        os.rename(old_path, new_path)

    # Write the updated DataFrame back to the Excel sheet
    df.to_excel(excel_path, index=False)

    # Display a success message
    # success_label.config(text='Videos successfully renamed!')


# Create the main window
window = tk.Tk()
window.title('Video Renamer')

# Create a label and an entry for the Excel sheet
excel_label = tk.Label(text='Excel Sheet:')
excel_label.pack()
excel_entry = tk.Entry()
excel_entry.pack()

# Create a button for selecting the Excel sheet
excel_button = tk.Button(text='Browse', command=lambda: excel_entry.insert(0, fd.askopenfilename()))
excel_button.pack()

# Create a label and an entry for the video directory
dir_label = tk.Label(text='Video Directory:')
dir_label.pack()
dir_entry = tk.Entry()
dir_entry.pack()

# Create a button for selecting the video directory
dir_button = tk.Button(text='Browse', command=lambda: dir_entry.insert(0, fd.askdirectory()))
dir_button.pack()

window.mainloop()