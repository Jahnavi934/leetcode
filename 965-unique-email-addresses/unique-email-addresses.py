class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.split('+')[0].replace('.', '')
            processed_email = local_name + '@' + domain_name
            unique_emails.add(processed_email)

        return len(unique_emails)

# Example usage:
solution = Solution()
emails1 = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
print(solution.numUniqueEmails(emails1))  # Output: 2

emails2 = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
print(solution.numUniqueEmails(emails2))