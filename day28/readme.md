# Day 28 - Pomodoro App

## What I Learned:

- **Python Basics:** Implemented a simple Pomodoro timer app using `Tkinter` for GUI development.
  
- **Timer Mechanism:** Understanding how to create countdown timers and manage repeated events using the `after` method in Tkinter.

- **Functionality of Pomodoro Technique:** Applied the Pomodoro Technique to break work into focused intervals (25 minutes of work, followed by short breaks and long breaks after every 4 sessions).

- **UI Design with Tkinter:** Learned how to design a simple, functional, and aesthetic user interface with labels, buttons, and a canvas in Tkinter.

- **Mathematics in Programming:** Using basic math operations like `floor` and modulus for calculating time intervals.

## Additional Features Added

### Timer Mechanism:
- **Work Session:** Users work for 25 minutes, marked by a green timer label.
  
- **Short Break:** After a work session, a 5-minute short break follows, marked by a pink timer label.
  
- **Long Break:** After 4 work sessions, a 20-minute long break occurs, marked by a red timer label.

### Real-Time Countdown:
- The timer countdown updates in real-time every second, and the remaining time is shown in `MM:SS` format.

### Task Completion Tracking:
- After each work session, a green checkmark (`✓`) is displayed, showing how many sessions have been completed. This helps users track their progress.

### Reset Function:
- Users can reset the timer at any point, which will stop the countdown and reset the session count.

### Improved User Interface:
- The app has a clean and simple UI with a tomato image in the center, representing the Pomodoro Technique.
  
- A clear, easy-to-read timer display shows the remaining time.
  
- Buttons are provided to start and reset the timer, making it interactive and easy to use.

## How It Works:

1. **Start Timer:**
   - Click the **Start** button to begin a work session.
   - The timer will count down for 25 minutes for work, 5 minutes for short breaks, and 20 minutes for long breaks after 4 work sessions.

2. **Reset Timer:**
   - Click the **Reset** button at any time to stop the timer and reset everything.

3. **Track Progress:**
   - After completing each work session, a green checkmark will appear, showing how many sessions you’ve completed.

## Code Structure

- **start_timer:** Starts the timer and determines whether it’s a work session, short break, or long break.
- **count_down:** Updates the countdown every second and switches between work and break periods.
- **reset_timer:** Stops the timer and resets the session counter.
- **UI Components:** Includes the timer display, start and reset buttons, and progress tracking via checkmarks.


