class Process:
    def __init__(self, p_id, name, start_time, priority):
        self.p_id = p_id
        self.name = name
        self.start_time = start_time
        self.priority = priority

    def __str__(self):
        return f"P{self.p_id} {self.name} {self.start_time} {self.priority}"

def sort_and_print(processes, sort_option):
    if sort_option == 1:
        sorted_processes = sorted(processes, key=lambda p: p.p_id)
    elif sort_option == 2:
        sorted_processes = sorted(processes, key=lambda p: p.start_time)
    elif sort_option == 3:
        sorted_processes = sorted(processes, key=lambda p: (p.priority, p.start_time))
    else:
        print("Invalid sort option")
        return

    print("\nSorted Processes:")
    for process in sorted_processes:
        print(process)

def main():
    processes = [
        Process(1, "VSCode", 100, "MID"),
        Process(23, "Eclipse", 234, "MID"),
        Process(93, "Chrome", 189, "High"),
        Process(42, "JDK", 9, "High"),
        Process(9, "CMD", 7, "High"),
        Process(87, "NotePad", 23, "Low")
    ]

    while True:
        print("\nMenu:")
        print("1. Sort by Process ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("4. Quit")
        choice = int(input("Enter your choice: "))

        if choice == 4:
            break

        sort_and_print(processes, choice)

if __name__ == "__main__":
    main()
