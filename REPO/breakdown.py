import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
import cv2

def download_video():
    video_url = url_entry.get()
    save_path = filedialog.askdirectory()

    try:
        yt = YouTube(video_url)
        video = yt.streams.filter(only_video=True).first()
        video.download(save_path)
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def breakdown_frames():
    video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])
    save_path = filedialog.askdirectory()
    try:
        vidcap = cv2.VideoCapture(video_path)
        success, image = vidcap.read()
        count = 0
        fps = vidcap.get(cv2.CAP_PROP_FPS)

        start_time = int(start_entry.get()) * fps
        end_time = int(end_entry.get()) * fps

        step_size = 10  # Set the step size to 10 frames (adjust as desired)

        while success:
            if count >= start_time and count <= end_time:
                cv2.imwrite(f"{save_path}/frame{count}.jpg", image)

            # Skip frames based on the step size
            for _ in range(step_size):
                success, image = vidcap.read()
                count += 1

        messagebox.showinfo("Success", "Frame breakdown completed!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the Tkinter window
window = tk.Tk()
window.title("YouTube Frame Breakdown")
window.geometry("400x200")

# Create URL label and entry
url_label = tk.Label(window, text="YouTube URL:")
url_label.pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack()
# Create start time label and entry
start_label = tk.Label(window, text="Start Time (seconds):")
start_label.pack()
start_entry = tk.Entry(window, width=10)
start_entry.pack()

# Create end time label and entry
end_label = tk.Label(window, text="End Time (seconds):")
end_label.pack()
end_entry = tk.Entry(window, width=10)
end_entry.pack()

# Create download button
download_button = tk.Button(window, text="Download Video", command=download_video)
download_button.pack()

# Create breakdown button
breakdown_button = tk.Button(window, text="Breakdown Frames", command=breakdown_frames)
breakdown_button.pack()

# Run the Tkinter event loop
window.mainloop()
