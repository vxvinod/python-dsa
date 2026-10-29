import re

class LogChecker:

    def __init__(self):
        self.ip_counter = {}
    
    def top_failed_ips(self, log_text: str, n: int) -> tuple[list[tuple[str, int]], int]:
        ip_regex = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
        fail_regex = re.compile(r"\bFAILED\b")
        for line in log_text.splitlines():
            print(line)
            match = ip_regex.search(line)
            fail_match = fail_regex.search(line)
            if match and fail_match:
                ip_addr = match.group()

                self.ip_counter[ip_addr] = self.ip_counter.get(ip_addr, 0) + 1
        ret_val = tuple()
        print(self.ip_counter)
        for ip, value in self.ip_counter.items():
            if value >= n:
                ret_val += ([(ip, value)],)
        return ret_val+(n,)

lg = LogChecker()
LOG = """2026-10-10T10:00:01Z sshd FAILED user=root ip=203.0.113.7
2026-10-10T10:00:02Z sshd FAILED user=admin ip=203.0.113.7
2026-10-10T10:00:03Z sshd SUCCESS user=alice ip=198.51.100.4
2026-10-10T10:00:04Z sshd FAILED user=root ip=192.0.2.10
garbage line here
2026-10-10T10:00:05Z sshd FAILED user=test ip=203.0.113.7
2026-10-10T10:00:06Z sshd FAILED user=bob ip=192.0.2.10
2026-10-10T10:00:07Z sshd FAILED user=root ip=198.51.100.4
2026-10-10T10:00:08Z sshd FAILED user=root
"""
print(lg.top_failed_ips(LOG, 2))