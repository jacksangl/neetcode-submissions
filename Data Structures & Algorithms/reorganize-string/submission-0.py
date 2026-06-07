class Solution:
    def reorganizeString(self, s: str) -> str:
        
        
        counts = Counter(s)
        counts = counts.most_common()
        res = ""
        n = len(s)
        heap = []
        
        for char, freq in counts:
            heapq.heappush(heap, (-freq, char))
        
        if -heap[0][0] > (n+1) // 2: return ""
        
        while heap:
            most, m_c = heapq.heappop(heap)
            most = -most
            res = res + m_c
            most -= 1
            if len(heap) > 0:
                sec, s_c = heapq.heappop(heap)
                sec = -sec
                res = res + s_c
                sec -= 1
                if sec != 0:
                    heapq.heappush(heap, (-sec, s_c))
        
            if most != 0:
                heapq.heappush(heap, (-most, m_c))
        return res
