import tkinter as tk

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)

    formated_time = ""
    hours_string = f"{hours:02d}h:"
    minutes_string = f"{minutes:02d}min"
    formated_time = f"{hours_string if (hours != 0) else ''}{minutes_string}"
    return formated_time


def time_string_to_seconds(time):
    hours, minutes = map(int, time.split(':'))
    seconds = (minutes * 60) + (hours * 3600)
    return seconds

def calculate():
    arrival = arrival_entry.get()
    lunch_break = lunch_break_entry.get()
    lunch_return = lunch_return_entry.get()
    leaving = leaving_entry.get()

    arrival = time_string_to_seconds(arrival)
    lunch_break = time_string_to_seconds(lunch_break)
    lunch_return = time_string_to_seconds(lunch_return)
    if leaving:
        leaving = time_string_to_seconds(leaving)
        time_worked = (lunch_break - arrival) + (leaving - lunch_return)
        result_text['text'] = format_time(time_worked)
        return
    time_worked = lunch_break - arrival
    leaving_time = time_string_to_seconds('8:00') - time_worked + lunch_return
    result_text['text'] = format_time(leaving_time)
    return

window = tk.Tk()
window.title('Calculator')

arrival_text = tk.Label(window, text='Arrival')
arrival_text.grid(column=2, row=0, padx=10, pady=10)

arrival_entry = tk.Entry(window, width=10)
arrival_entry.grid(column=4, row=0, padx=10, pady=10)

lunch_break_text = tk.Label(window, text='Lunch Break')
lunch_break_text.grid(column=2, row=1, padx=10, pady=10)

lunch_break_entry = tk.Entry(window, width=10)
lunch_break_entry.grid(column=4, row=1, padx=10, pady=10)

lunch_return_text = tk.Label(window, text='Return')
lunch_return_text.grid(column=2, row=2, padx=10, pady=10)

lunch_return_entry = tk.Entry(window, width=10)
lunch_return_entry.grid(column=4, row=2, padx=10, pady=10)

leaving_text = tk.Label(window, text='Leaving')
leaving_text.grid(column=2, row=3, padx=10, pady=10)

leaving_entry = tk.Entry(window, width=10)
leaving_entry.grid(column=4, row=3, padx=10, pady=10)

button = tk.Button(window, text='Calculate', command=calculate)
button.grid(column=3, row=4, padx=10, pady=10)

result_text = leaving_text = tk.Label(window, text='')
result_text.grid(column=3, row=5, padx=10, pady=10)


window.mainloop()

