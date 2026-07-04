class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        sent = set()

        for email in emails:
            local, domain = email.split('@')
            tmp = []
            for c in local:
                if c == '+':
                    break
                
                if c == '.':
                    continue

                tmp.append(c)

            local = ''.join(tmp)
            sent.add((local, domain))

        return len(sent)