"""
Implement a Keyword Filtering System Using remove()

Requirements
You are building a moderation tool for a content platform. The tool should allow moderators to remove offensive or
blacklisted keywords from a list of user-submitted tags.
1. Create a function filter_keywords(tags: list, blacklist: list) that:
    - Iterates through the blacklist and removes matching keywords from the tags list using remove().
    - Ignores blacklist items that are not present in the tags (do not raise an error).
    - Returns the cleaned tags list.
2. Demonstrate the function using:
    - tags = ["fun", "news", "spam", "clickbait", "sports"]
    - blacklist = ["spam", "clickbait", "scam"]
"""
def filter_keywords(tags, blacklist):
    for word in blacklist:
        try:
            tags.remove(word)
        except ValueError:
            # Word not found in tags, skip it
            continue
    return tags

# Example usage
tags = ["fun", "news", "spam", "clickbait", "sports"]
blacklist = ["spam", "clickbait", "scam"]

filtered_tags = filter_keywords(tags, blacklist)
print(filtered_tags)  # Output: ['fun', 'news', 'sports']
