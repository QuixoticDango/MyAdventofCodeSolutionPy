# import time
# start = time.time()
# class Ruler:
#     def __init__(self, t: int, n: int):
#         self.t = t
#         self.n = n
    
#     def draw(self):
#         major_ticks = ['-' * self.t + ' ' + str(i) for i in range(self.n + 1)]
#         tick_size = self.t
#         loop_count = 0
#         while tick_size > 1:
#             if loop_count == 0:
#                 idx = 0
#                 while idx < len(major_ticks) - 1:
#                     if any(ch.isnumeric() for ch in major_ticks[idx]):
#                         major_ticks.insert(idx+1, '-' * (tick_size - 1))
#                     idx += 1
#                 tick_size -= 1
#                 loop_count += 1
#             else:
#                 idx = 0
#                 while idx < len(major_ticks):
#                     if len(major_ticks[idx]) == tick_size:
#                         major_ticks.insert(idx+1, '-' * (tick_size - 1))
#                         major_ticks.insert(idx, '-' * (tick_size - 1))
#                         idx += 1
#                     idx += 1
#                 tick_size -= 1
#         return '\n'.join(major_ticks)
# print(Ruler(3, 3).draw())
# print(f"Execution time: {(time.time() - start) * 1000} ms")

from collections import deque
a = [1,2,3]
del a[1]
print(a)