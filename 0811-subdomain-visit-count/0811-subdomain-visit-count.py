class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = Counter()
        for line in cpdomains:
            count, domain = line.split()
            count = int(count)
            for subdomain in self.findAllSubdomains(domain):
                counter[subdomain] += count
        return [' '.join([str(freq), domain]) for domain, freq in counter.items()]
            
    def findAllSubdomains(self, domain):
        subdomains = []
        words = domain.split('.')
        for i in range(len(words)):
            subdomains.append('.'.join(words[i:]))
        return subdomains