from collections import deque


def to_minutes(time_str: str) -> int:
    """Converts a 'HH:MM' string into total minutes."""
    hours, minutes = map(int, time_str.split(":"))
    return (hours * 60) + minutes


def fmt(minutes: int) -> str:
    """Converts total minutes back into a zero-padded 'HH:MM' string."""
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours:02d}:{mins:02d}"

class AccountLockTracker:

    def __init__(self):
        self.account_track = {}

    def process(self, line):
        #{state: lock/active, last_login_success: time, last_5_min_attempt:[], account_lock_time: time}
        # parse the line if Fail add to the dic and add to last_5_min_attempt
            # if attempt goes >=3 make the state as locked and make sure last_5_min_attempt is cleaned and update the account_lock_time + 5min
        # if Success check the account is locked ignore, check account_lock_time > then allow else reject
            # if active make the last_5_min as empty and account_lock_time as empty

        # clean_last_5_min  
        try:
            info = line.split()
            
            if info[0] == "STATUS":
                self.status(info[1])
            print(info)
            state, name, time = info[0], info[1], info[2]
            print(f"process-#{state}--{name}---{time}")
            
            if state == "FAIL":
                self.fail_attempt(name, to_minutes(time))
            elif state == "SUCCESS":
                self.success_attempt(name, to_minutes(time))
            else:
                raise ValueError("Unknown state")
        except Exception as e:
            print(f"Exception raised {e}")    

    def clean_5_min_window(self, name, time):
        five_min_window =  self.account_track[name]["last_5_min_attempt"]
        while five_min_window and time - five_min_window[0] > 5:
            five_min_window.popleft()

    def fail_attempt(self, name, time):
        
        if name not in self.account_track:
            self.add_name_to_caccount_tracker(name, {"state": "active",
                                                "last_login_success": 0,
                                                "last_5_min_attempt": deque([time]),
                                                "account_lock_time": 0})
        if self.account_track[name]["account_lock_time"] >= time:
            return

        if len(self.account_track[name]["last_5_min_attempt"]) >=3:
            self.account_track[name]["state"] = "locked"
            self.account_track[name]["last_5_min_attempt"] = []
            self.account_track[name]["account_lock_time"] = time + 15
        else:
            self.account_track[name]["last_5_min_attempt"].append(time)
            self.account_track[name]["state"] = "active"
            self.clean_5_min_window(name, time)
        
    def success_attempt(self, name, time):
        if self.account_track[name]["account_lock_time"] >= time:
            self.account_track[name]["state"] == "active"
            return
        if self.account_track[name]["state"] == "locked":
            return
        
        print("success inside")
        self.account_track[name]["last_5_min_attempt"] = []
        self.account_track[name]["account_lock_time"] = 0
        
            




    def add_name_to_caccount_tracker(self, name, info):
        self.account_track[name] = info

    def status(self, time):
        for name, info in self.account_track.items():
            if info["state"] == "active":
                print(f"{name}: {info["state"]}") 
            else:
                print(f"{name}: {info["state"]} until {fmt(info["account_lock_time"])}") 

alt = AccountLockTracker()
alt.process("FAIL carol 09:50")
alt.process("FAIL carol 09:51")
alt.process("FAIL carol 09:52")
alt.process("FAIL alice 10:00")
alt.process("FAIL bob 10:00")
alt.process("FAIL alice 10:02")
alt.process("SUCCESS alice 10:03")
alt.process("FAIL alice 10:04")
alt.process("FAIL alice 10:05")
alt.process("FAIL bob 10:06")
alt.process("FAIL bob 10:07")
alt.process("SUCCESS carol 10:08")
alt.process("FAIL alice 10:09")
alt.process("SUCCESS alice 10:20")
alt.process("STATUS 10:21")


    