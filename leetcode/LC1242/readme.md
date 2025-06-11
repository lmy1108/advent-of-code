https://leetcode.com/problems/web-crawler-multithreaded/solutions/739683/concise-and-beautiful-python
- Summary
We implement a classic BFS but the entries in our queue are future objects instead of primitve values. A pool of at most max_workers threads is used to execute getUrl calls asynchronously. Calling result() on our futures blocks until the task is completed or rejected.

```
from concurrent import futures

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = lambda url: url.split('/')[2]
        seen = {startUrl}
    
        with futures.ThreadPoolExecutor(max_workers=16) as executor:
            tasks = deque([executor.submit(htmlParser.getUrls, startUrl)])
            while tasks:
                for url in tasks.popleft().result():
                    if url not in seen and hostname(startUrl) == hostname(url):
                        seen.add(url)
                        tasks.append(executor.submit(htmlParser.getUrls, url))
        
        return list(seen)
```