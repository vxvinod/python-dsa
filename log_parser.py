from collections import deque
class LogParser:

    def __init__(self):
        self.logs = {}

    def process_log(self, logs):
        
        try:
            self.logs = logs
            for log in logs:
                request_id, ts, status_code = log[0], log[1], log[2]
                self.parse_log(request_id, ts, status_code)

        except Exception as e:
            print(f"Exception occured {e}")
    

    def parse_log(self, request_id, ts, status_code):

        seen = {}
        req_id_more_3_fail = {}
        if request_id not in seen:
            if status_code == 429 or status_code == 500:
                seen[request_id] = deque([ts])
        else:        
            if status_code == 429 or status_code == 500:
                seen[request_id].append([ts])   # += append

        # iterate the values check current time - value of list is > 60 pop
        for t in seen[request_id]:
            if ts - t > 60:
                t.popleft()
        return seen

    def identify_ouput(self):
        for req_id, timestamps in seen.items():
            if len(timestamps) >=3:
                req_id_more_3_fail[request_id] = timestamps
        




lp = LogParser()
logs = [
    ("u1", 10, 200),
    ("u1", 20, 500),
    ("u2", 25, 429),
    ("u1", 40, 503),
    ("u1", 65, 429),
    ("u2", 70, 200),
    ("u1", 75, 500),
    ("u2", 80, 500),
    ("u2", 90, 503)
]
lp.process(logs)
print(lp.parse_log())