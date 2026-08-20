class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits = collections.defaultdict(int)

        for cpdomain in cpdomains:
            cp, domain = cpdomain.split(" ")

            cnt = ""
            subs = domain.split(".")
            for i in range(len(subs) - 1, -1, -1):
                cnt = (subs[i] + "." + cnt).strip(".")
                visits[cnt] += int(cp)

        res = []
        for domain, count in visits.items():
            res.append(str(count) + " " + domain)

        return res